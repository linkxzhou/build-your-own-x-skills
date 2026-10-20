The user wants to learn and implement "From Blinker to RISC-V" using Verilog from scratch. They want me to first plan milestones and create a minimal project skeleton.

This matches the build-your-own-x skill — "从零实现" (implement from scratch), building a RISC-V CPU. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read more of it, and also check the skills directory for the relevant track skill. The topic is "From Blinker to RISC-V" — a CPU/RISC-V implementation in Verilog. Let me find the category slug. Likely "cpu" or similar. Let me read the rest of SKILL.md and list the skills directory.The category is `processor`. The track skill is mandatory reading. Let me read it and check for a per-tutorial skill matching "From Blinker to RISC-V".有一个匹配的教程技能：`processor-riscv-verilog`。让我阅读轨道技能的其余部分以及该教程技能。我来阅读教程技能的其余部分和 tutorial-map 参考。我来阅读一下剩余的参考资料：concepts.md 和 minimal example scaffold 指南。技能已加载。现在我来检查工作区状态和可用的工具链，然后再进行规划。工作区是空的（只有 agent config），且 HDL 工具链尚未安装——我会记下这一点，并只把安装命令提供给你。让我先梳理一下探索结果，然后制定计划。测试平台（testbench）需要修正：`final` 块是 SystemVerilog 特有的（与 `-g2001` 冲突），且边沿采样节奏检查存在时钟竞争（clock races）。我将重写它，使其与相位无关（phase-independent）：测量连续 `led` 翻转之间的间隔，并让 Makefile 对 `PASS` 行进行 `grep` 检查以确定退出状态。`iverilog` 缺失，所以我无法运行仿真。让我检查一下是否有其他 Verilog 解析器来进行语法验证，并重新读取我编写的文件以进行仔细的静态检查。静态审查发现了一些实际问题，我来修复它们：

1. **TB 会误报通过/失败**：已寄存器的 `led` 在第一次时钟边沿之前为 `X`；`X→0` 的复位转换会触发 `always @(led)` 并破坏间隔测量。我需要跳过 `X` 初始化边沿。
2. **Blinker 提示与 TB 不一致**：如果学习者忘记复位 `led_r`，在 t=26ns 时 `led` 为 `X`，“复位后 led=0”的检查就会失败 —— 提示必须明确要求复位 `led_r`。
3. **注释矛盾**：概念图将 `led` 称为组合逻辑，而任务需要的是寄存器输出。示例解决方案的完整时序追踪揭示了另一个误报：初始化的 `X→0` 边沿与第一个真实触发点（reset release + BLINK_PERIOD 周期）之间的间隔为 50ns，而非 40ns。在 `@(led)` 处进行间隔测量从根本上就很脆弱。我将把检查器切换为在每个上升沿对 `led` 进行采样（由于非阻塞赋值，这不存在竞态条件），并计算变化之间的周期数。周期精确仿真确认了检查器：预期的解决方案会产生 9 次变化，且没有错误，每次变化之间恰好有 4 个周期；X-led 错误会触发监视器，而差一错误（off-by-one）会产生 FAIL。让我对 Makefile 进行 dry-run，并验证最终的文件集。里程碑和骨架都已就绪。路线按上游教程（BrunoLevy/learn-fpga 的 FROM_BLINKER_TO_RISCV）拆成 7 个里程碑，每个都有可运行的检查点：

| 阶段 | 内容 | 检查点 |
|---|---|---|
| M1 | 闪灯 + testbench | `make sim` 输出 PASS，VCD 可看波形 |
| M2 | ALU | testbench 逐个比对运算结果 |
| M3 | 寄存器堆 + PC | 写入可读回，x0 恒为 0 |
| M4 | 单周期 RV32I 子集 | 手写机器码算出 1+…+10=55 |
| M5 | 存储器 + I/O | 程序往仿真 UART 打印 |
| M6 | 一致性测试 | RV32I 测试项通过 |
| M7 | 进阶（可选） | 五级流水线 + CPI 报告 / 上板 |

已创建的骨架：

- `Makefile` — `make sim`（编译+运行+grep PASS 判定）、`make wave`、`make clean`
- `rtl/blinker.v` — M1 骨架，核心逻辑留了 `TODO(learner)`，注释里给了递进提示
- `tb/tb_blinker.v` — 自检 testbench：查复位后 led 干净为 0、每 BLINK_PERIOD 周期恰好变化一次、带看门狗
- `README.md` — 完整路线表 + 环境安装命令；`PROGRESS.md` — 进度打勾表；`docs/notes.md` — 笔记模板

两点说明：

1. **工具链需要你自己装**（我这边没有 iverilog，也不代装）：`brew install icarus-verilog gtkwave`（Ubuntu 用 `sudo apt install iverilog gtkwave`）。装好后 `make sim` 即可跑通检查点。testbench 的判定逻辑我已逐周期推演验证过：正确实现得 9 次变化零报错，忘复位 led 会报 X，周期差一会被抓出来。
2. **你的第一个任务**：打开 `rtl/blinker.v`，让 `led` 每 `BLINK_PERIOD` 个周期变化一次——大约 4 行代码，提示在注释里。跑 `make sim` 看到 PASS 后，在 `PROGRESS.md` 勾掉 M1，我们就进 M2 的 ALU。