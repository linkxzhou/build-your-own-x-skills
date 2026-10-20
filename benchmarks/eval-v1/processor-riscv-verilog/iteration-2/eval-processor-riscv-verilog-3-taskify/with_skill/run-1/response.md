The user wants me to convert the FemtoRV tutorial "FROM_BLINKER_TO_RISCV" from BrunoLevy's learn-fpga repository into a Claude Code executable learning task list.

Let me first fetch the tutorial content to understand what it covers, then convert it into a structured task list that Claude Code can execute.

Let me start by fetching the tutorial from GitHub.README 被截断了。让我获取完整内容，并查看目录结构以了解所有步骤。已获取完整 README：24 个步骤，共 3702 行。让我阅读一下关键章节，以了解每一步的要求。The read tool is restricted to the workspace. Let me find the workspace root.让我继续阅读剩余的步骤，以获取每个步骤的详细信息。Now I have a good understanding of the tutorial. Let me also check the remaining sections I haven't read in detail (steps 2, 7-9, 12, 14-15, 17, 21-22) — I've read most of them in the truncated portions. Let me quickly check a few specific parts I missed: Step 2 (slower blinky), Step 7 (VERILOG assembler), Step 12 (shrinking core), Step 17 (memory-mapped devices/UART), Step 21 (C compilation), Step 22 (more memory).

Let me read those sections quickly.I now have a comprehensive understanding of the tutorial. Let me also check the "Files for all the steps" section at the end and the "Next tutorial" section.我已经掌握了完整的教程结构。由于这是一个 build-your-own-x 学习任务，让我先检查一下可用的技能。技能工作流已明确：从离线引用构建任务列表，以 `TASKS.md` 交付，并以第一个可运行的检查点结束。让我验证一下本地环境，并获取两个辅助脚本（`run.sh`、`FIRMWARE/Makefile`），以便验证命令准确无误。环境已确认：macOS arm64，git 可用，尚未安装 FPGA 工具。让我验证一下 FIRMWARE 工具链的配置，以确保任务列表中的工具链说明准确无误。技能的 taskify 工作流很清晰。在编写任务列表之前，让我先从本地副本中验证 step 17 中 UART/IO 的细节。在编写任务列表之前，我先准确阅读一下第 12 步（我之前只看过部分内容）。我已经全面了解了全部 24 个步骤。现在，我将按照技能的 taskify 工作流（离线引用 + 已获取的 README，交付 `TASKS.md`，并以第一个可运行的检查点结束）来记录探索并制定计划。现在我来交叉核对任务列表与 README 的步骤列表以及 Try-this 练习。覆盖率已确认，但编号存在一个易混淆的偏移（T1=Step2）。让我重新编号，以便 **Tn = Step n**，并将环境设置作为 T0 —— 这样在执行过程中更清晰。所有 25 个任务 (T0–T24) 均已存在，行引用与 README 标题完全匹配，且 Tn=Step n 的映射关系保持一致。现在我来清理临时文件。任务清单已写入 `TASKS.md`，覆盖教程全部 24 个 Step（T0 环境准备 + T1–T24，任务编号与 Step 编号一一对应），每个任务含目标、涉及文件、核心概念、验证命令与预期输出、自检问题，并标注了原文行号方便对照。

结构上按学习曲线分成 6 个阶段：

| 阶段 | 任务 | 内容 |
|---|---|---|
| P0 | T0 | 克隆仓库、装 iverilog |
| P1 | T1–T3 | blinky → 时钟分频 → ROM 查表彩灯 |
| P2 | T4–T7 | 译码器 → 寄存器堆+状态机 → ALU → 内嵌汇编器 |
| P3 | T8–T10 | JAL/JALR → 分支 → LUI/AUIPC（11 类指令收官） |
| P4 | T11–T12 | 存储器独立模块 → 核心瘦身到 839 LUT |
| P5 | T13–T18 | 子程序/ABI → Load/Store → MMIO+UART → Mandelbrot |
| P6 | T19–T24 | Verilator → GNU 工具链 → C 程序 → SPI Flash 执行 |

几个关键设计决策：

- **仿真优先**：所有任务默认 `./run.sh my_stepN.v` 验证，上板步骤全部标为可选——无板子也能走完全程。
- **学习者自己写**：任务要求新建 `my_stepN.v` 而非直接抄官方 `stepN.v`，保留“自己动手”的学习价值；Claude Code 的角色是教练（讲解、陪写、跑验证、调试），一次只做一个任务。
- **环境适配已内置**：本机是 macOS arm64，工具链前缀是 `riscv-none-embed-*`（README 写的 `riscv64-unknown-elf-*` 是 Linux x86 的），附录 B 有说明；工具安装命令只列出、由你自己执行。
- **原文 Try-this 练习**全部保留并映射到对应任务。

第一个可执行检查点（T0）：

```bash
git clone https://github.com/BrunoLevy/learn-fpga.git
brew install icarus-verilog   # macOS；Linux 用 sudo apt-get install iverilog
cd learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV
./run.sh step1.v
```

预期输出：终端持续打印 `LEDS = xxxxx`，二进制值每拍递增。看到它，就可以对 Claude Code 说“执行任务 T1”了。