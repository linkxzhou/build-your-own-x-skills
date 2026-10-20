The user wants me to convert a tutorial (how to write a CHIP-8 emulator/interpreter) into a Claude Code executable learning task list. Let me first fetch the tutorial content to understand what it covers, then convert it into a task list.

Let me fetch the article first.文章被截断了，让我获取完整内容。工具输出被截断，改用 curl 下载后本地解析。教程内容已完整提取。文章结构：模拟器概念 → CHIP-8 规格（内存/寄存器/栈/键盘）→ Game Loop → 取指/译码/执行 → 3 条指令示例（2NNN/8XY4/FX33）→ DXYN 绘图 → 输入映射 → 字体集 → 初始化/加载 ROM → 进阶建议。现在把它转成可执行任务清单。The write tool requires 'path' parameter. I provided content but the path seems to have been misplaced. Let me retry with correct parameters.文件已写入。核对指令数：附录 A 目前 34 条，教程说 35 条——缺 `0NNN`（RCA 1802 调用，惯例忽略）。修正计数一致性，并把 9XY0 补进 T3.4 标题。The grep for `^- \[ \]` returned 0 because the checkboxes are in `### - [ ] T0.1` format (with ### prefix). Let me verify the checkbox count differently.`TASKS.md` 已生成，教程全文已解析并转换为 19 个可执行任务（2+3+3+6+3+2，全部 checkbox 未勾选，ID 与任务数一致）。

**结构**（对应教程章节）：

| 阶段 | 任务 | 对应教程内容 |
|------|------|-------------|
| 0 环境骨架 | T0.1–T0.2 | Before you start / Game Loop |
| 1 机器状态 | T1.1–T1.3 | CPU Specifications / Initialize / loadGame |
| 2 取指-译码-执行 | T2.1–T2.3 | Emulation cycle / Timers |
| 3 指令集 | T3.1–T3.6 | 35 条指令分 6 组，含教程 3 条示例（2NNN/8XY4/FX33）+ DXYN 绘图 |
| 4 图形输入音频 | T4.1–T4.3 | Handling graphics and input |
| 5 端到端 | T5.1–T5.2 | ROM 验证 / Suggestions 进阶 |

**为可执行性做的关键设计**：

- 每个任务带「目标 / 步骤 / 验收」，验收全部是可运行命令（cmake 构建、无头单测、真实 ROM 表现），Claude Code 可自行判断完成与否。
- 架构约束：核心 `chip8.cpp` 禁止 include SDL，使阶段 5 测试可无头运行。
- 附录 A 是 35 条指令速查表（教程只详讲 3 条，其余标注了对应任务号）；附录 B 记录了 5 处教程勘误/语义决策（字体集地址 0x50 vs 0x00 的正文矛盾、1NNN 压栈笔误、移位指令现代语义等），执行时按此裁决。

使用方式：对 Claude Code 说「阅读 TASKS.md，执行 T0.1」或「继续下一个未完成的任务」即可逐项推进，每项完成需跑通验收、勾选 checkbox 并 git commit。