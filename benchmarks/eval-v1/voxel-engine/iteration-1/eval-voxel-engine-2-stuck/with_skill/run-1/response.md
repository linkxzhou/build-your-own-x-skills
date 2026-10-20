The user says: "My voxel world has low framerate, every block draws 6 faces." This is a performance question about voxel rendering. They're speaking Chinese. I should respond in Chinese.

This is a classic voxel engine optimization problem: hidden face culling / greedy meshing / chunk meshing. I should check if there's a skill match — "build-your-own-x" mentions voxel? Let me check: the skill covers Git, Redis, shell, Docker, interpreter, OS, emulator, web server, browser, regex engine, game, neural network, blockchain, LLM, malloc, CPU. Voxel isn't explicitly listed but "game" is. The user isn't asking to build from scratch — they have an existing voxel world with low FPS. This is a debugging/optimization question, not a "recommend a project" question. The skill says use it "whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills, asks which build-your-own project to start with, or names a category". The user has an existing project with a perf problem. Hmm, it's borderline. The skill is about picking a topic and coaching through building. The user already has a voxel world. I think this is a direct performance question — I should answer it directly. But maybe I should check the workspace for their code first?

The user says "我的体素世界" — my voxel world. There might be code in the workspace. Let me check the workspace for files. If there's code, I should look at it and give specific advice. If not, give general advice.

Let me glob for files to see if there's a project in the workspace.

Actually, per instructions: "Before modifying code, call explore once" — but I'm not modifying code yet. Let me first look at what's in the workspace.

I'll do a quick glob to see if there's any code.

Then answer: the core fix is face culling — only draw faces adjacent to air/transparent blocks, plus chunking + one mesh per chunk (batch draw calls), frustum culling, greedy meshing, texture atlas, etc.

Let me check the workspace first.工作区里没有你的项目代码，所以我按通用情况给方案。你描述的症状(每方块 6 面)是体素渲染最典型的性能杀手，修复路径按收益排序：

## 1. 面剔除(收益最大，先做这个)

一个方块只有暴露在空气/透明方块旁边的面才需要画。埋在地里的方块 6 个面全是浪费，通常能直接砍掉 90% 以上的三角形：

```js
for each block (x, y, z) with block != AIR:
    for each of 6 directions d:
        neighbor = getBlock(x + d.dx, y + d.dy, z + d.dz)
        if neighbor == AIR or isTransparent(neighbor):
            emitFace(x, y, z, d)   // 只有这里才生成顶点
```

注意边界：邻居查询要能跨 chunk 取方块，否则 chunk 接缝处会多出一墙内侧面。

## 2. 分块 + 合批

把世界切成 16×16×16(或 16×16×世界高度)的 chunk,每个 chunk 把所有可见面写进**一个**顶点缓冲，一次 draw call 画完。判断标准：如果你的 draw call 数量接近方块数，这就是主要瓶颈；合批后 draw call ≈ 可见 chunk 数(几十到几百)。

数据结构上，chunk 内部用扁平数组 `blocks[x + z*16 + y*16*16]`,别用 Map/字典逐方块查——meshing 时邻居查询是每方块 6 次，哈希查找会成为 CPU 瓶颈。

## 3. 视锥剔除

每帧对每个 chunk 的 AABB 做视锥体测试，只画视野内的 chunk。实现简单，收益和视角相关(通常砍一半以上)。

## 4. 贪心合并(greedy meshing)

同一平面、同材质的相邻面合并成一个大四边形，顶点数再降一个数量级。实现比前三步复杂(需要处理 UV 平铺)，建议前三步做完帧率还不够再上。

## 5. 顺手检查的几项

- 开启背面剔除 `gl.enable(CULL_FACE)`,面片顶点顺序统一逆时针。
- 用纹理图集(atlas),整个世界一次纹理绑定，避免逐方块切换。
- meshing 放后台线程/分帧处理，玩家改方块时只重建受影响的那 1~2 个 chunk,别全图重算。

做完第 1、2 步，典型场景(几万到几十万方块)就能从个位数帧率回到 60 FPS。如果你把代码放进工作区或贴出渲染循环，我可以指出具体哪一步卡住。