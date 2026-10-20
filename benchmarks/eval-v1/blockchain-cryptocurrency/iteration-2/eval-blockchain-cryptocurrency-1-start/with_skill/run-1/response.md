The user wants to build a simple blockchain in Python, step by step. This matches the build-your-own-x skill — "从零实现、自己动手写一个 X、造轮子学原理" triggers. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it.主题是区块链 → 轨道 `blockchain-cryptocurrency`。现在正在读取轨道技能（强制）。轨道技能位于 `.agents/skills/build-your-own-x/skills/blockchain-cryptocurrency/`，并且有一个 Python 特定的教程技能。现在开始读取这两个文件。两个文件都被截断了。我正在读取剩余部分以及教程列表。正在读取 Python 教程的参考文件，并检查工作区状态。工作区是空的，Python 3.14.7 可用，纯标准库就够。先记录探索结论并制定里程碑计划。骨架和进度文件建好，核心留给你写。**里程碑 1/5：Block + hash**

**概念（30 秒版）**：区块链 = 一串用哈希串起来的块。每个块记录自己的内容 + 上一个块的哈希。SHA-256 是个单向函数：输入变一个字节，输出的 64 位十六进制指纹就面目全非。所以“改了历史数据”必然导致哈希对不上——这就是防篡改的全部原理。

**你的任务**：打开 `blockchain.py:19`，实现 `compute_hash()`，3 行以内。骨架里的 TODO 注释就是步骤。唯一容易踩的坑：`json.dumps` 必须带 `sort_keys=True`，否则 dict 顺序不稳定，哈希就不可复现。

**检查**（写完后跑两次）：

```
python3 blockchain.py
```

预期输出：

```
index: 0
data:  genesis
prev:  0
hash:  <64位十六进制>
```

通过标准有三条：两次运行 hash 完全一致；hash 长度是 64；把 `data="genesis"` 临时改成 `"genesis!"` 再跑，hash 应完全变样（改完记得改回来）。

跑完把输出贴给我，或者直接说“过了”，我们就进里程碑 2：把块串成链并写校验函数。