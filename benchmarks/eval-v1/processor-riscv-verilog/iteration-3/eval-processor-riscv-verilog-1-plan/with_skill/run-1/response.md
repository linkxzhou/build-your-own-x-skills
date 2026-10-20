The user wants to learn and implement "From Blinker to RISC-V" in Verilog from scratch. They want me to first plan milestones and create a minimal project skeleton.

This matches the build-your-own-x skill. I should read the SKILL.md first before doing anything else.

Let me read the skill file.The skill file was truncated. Let me read the rest of it.该主题对应到 `processor` 轨道。现在正在读取轨道技能（必选），并检查是否有针对该特定教程的技能。Now let me check the tutorials reference and per-tutorial skills for "From Blinker to RISC-V".学习者明确指出了「From Blinker to RISC-V」，因此我需要阅读针对该教程的技能。技能已加载。现在检查工作区状态和可用工具链（按技能要求：不代装工具，先探测已有环境）。技能已加载（track: `processor`，per-tutorial: `processor-riscv-verilog`）。工作区为空，iverilog/verilator/gtkwave 均未安装。先记录探索结论并制定计划。里程碑规划与骨架已就绪。当前进度：M1/7。

**里程碑**（详见 `TASKS.md`，任务化自 Bruno Levy 的教程，原文：https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV）：

1. **Blinker + testbench** — 模块、时钟、复位、波形
2. **ALU** — 组合逻辑、操作码
3. **寄存器堆 + PC** — 同步写/异步读，x0 恒 0
4. **单周期 RV32I 子集** — 译码、立即数、访存、分支；检查点：算出 1..10=55
5. **存储器 + I/O** — MMIO LED/UART，模拟串口打印
6. **合规测试** — rv32ui-p-* 通过
7. **挑战** — 5 级流水线（报 CPI）或 FPGA 上板

**骨架**：`Makefile`（`sim/lint/wave/clean`，`TOP`/`TB` 切换里程碑）、`rtl/blinker.v`（两处 TODO 留给你写：计数器 + LED 翻转）、`tb/tb_blinker.v`（自检，PASS/FAIL 自动判定）、`TASKS.md`、`PROGRESS.md`。工具链未装，安装命令在 README（`brew install icarus-verilog gtkwave`），由你自己执行。

**M1 概念**（30 秒版）：`always @(posedge clk)` 里的赋值在每个时钟沿生效，这就是寄存器；blinker = 一个循环计数的寄存器 + 计到顶时翻转 LED 寄存器。先想清楚「cnt==0 出现在计数到顶的下一拍」再动手。

检查点（装好工具链后运行）：

```sh
make sim
# 期望输出: M1 PASS: LED toggled 4 times
```

卡住就把报错贴出来；PASS 后在 `PROGRESS.md` 记一行，进 M2。