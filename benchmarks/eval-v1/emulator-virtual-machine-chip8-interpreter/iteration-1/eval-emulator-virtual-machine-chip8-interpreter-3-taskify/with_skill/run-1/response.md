The user wants me to convert a tutorial (how to write a CHIP-8 emulator) into a Claude Code executable learning task list. This matches the build-your-own-x skill — "an emulator" is explicitly named. I should read the skill first.

Let me read the SKILL.md, and also fetch the tutorial URL to understand its content.The skill says: read the track skill `skills/<slug>/SKILL.md` for the mapped category. The category here is "emulator" — let me check the category map. The truncated part of SKILL.md has the category map. Let me read the rest of the SKILL.md and check the skills directory for the emulator track skill. Also, there might be a per-tutorial skill for this exact article (multigesture chip-8). Let me check `skills/x-skills-manifest.json` and `ls skills | grep chip`.

Also I should get the full article content — it was truncated. Let me fetch more of it.存在一个针对该教程的技能：`emulator-virtual-machine-chip8-interpreter`（以及 `-cpp` / `-python` 变体）。根据路由，先读取轨道技能，然后读取教程技能。Per-tutorial skill points to `references/tutorial-map.md`. Reading it plus the remaining article content.提取器主要捕获了导航内容。让我通过 `curl` 获取文章正文，并提取实际的文章内容。I now have the full article content. Let me also check the truncated middle part (lines 380-500) about opcode examples and the truncated part around 560-626 (input details, opcode table). Let me quickly read the remaining bits to make sure I capture all tutorial content: "Loading the program into the memory" (lines ~382-448), "Opcode examples" (448-496), and the input section detail (560-626).我已经阅读了完整的教程内容。在编写任务列表之前，让我先整合并检查一下工作区。工作区是空的（只有 `.agents/` 和 `AGENTS.md`），教程全文、track skill 和 per-tutorial skill 都已读完。现在把教程映射成可执行任务清单，写入 `TASKS.md`。自查发现两处错误：FX33 测试断言算错了（0x7B=123 的 BCD 是 1,2,3），以及 T4 用到的 `--dump` 没出现在 T0 的用法行里。修正：任务清单已写入 `TASKS.md`，基于教程全文（已抓取并核对原文）+ 仓库里的 `emulator-virtual-machine-chip8-interpreter` 技能转换而成。

结构：8 个任务（T0–T7），每个任务块包含「给 Claude Code 的提示词 + 验收命令 + 概念要点」，映射关系如下：

| 任务 | 教程章节 | 验收 |
|---|---|---|
| T0 骨架 + 游戏循环 | Game Loop | 构建通过，打印用法 |
| T1 CPU 状态 + 字体集 + ROM 加载 | CPU Specifications / Getting started / fontset | 单测：字体集在 0x50、ROM 在 0x200 |
| T2 取指-译码-执行 + 定时器 | Emulation cycle | ANNN/00E0/00EE/1NNN/2NNN 单测 |
| T3 完整 35 条指令 | Opcode examples + Cowgod 手册 | 全指令族单测 |
| T4 DXYN + 帧缓冲 | Handling graphics and input | IBM logo ROM 终端渲染出 "IBM" |
| T5 输入 + 60Hz 节拍 | Input 一节 | 游戏 ROM 可玩 |
| T6 调试器 | （2003 版 myChip8 思路） | `--step` 逐周期打印状态 |
| T7 进阶 | Suggestions | 函数分发表 / Super-CHIP / 移植 |

转换时做的几个关键决策：

- **教练模式**：每个提示词都约束 Claude Code 先讲概念、给骨架、由你写核心，完整代码只在你尝试后给——这是技能文件要求的，避免它直接把模拟器写完。
- **教程勘误已内嵌**：原文有三处坑（字体集位置正文与代码矛盾、“每次跳转都压栈”过度概括、"60 opcodes/秒"太慢），清单在对应任务里给了正确做法，另附「勘误与坑」一节。
- **验收全部可执行**：单测用无依赖 assert，T4 用终端 ASCII 渲染代替 SDL 窗口作为硬验收，保证每个任务都有客观通过标准。
- **分歧点显式化**：FX55/FX65 的 I 自增、8XY6/8XY7 移位源、DXYN 越界行为，要求各选一种写进 README——测试 ROM 对这些很敏感。

开始方式：把 `TASKS.md` 放在工作区，对 Claude Code 说「按 TASKS.md 做 T0」即可。