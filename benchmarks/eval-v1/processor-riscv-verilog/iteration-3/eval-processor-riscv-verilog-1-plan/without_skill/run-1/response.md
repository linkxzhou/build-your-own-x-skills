The user wants to learn and implement "From Blinker to RISC-V" from scratch using Verilog, and asks me to first plan milestones and create a minimal project skeleton.

Let me first look at the current workspace to understand what's there. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-processor-riscv-verilog-1` — this looks like it might be related to the "build-your-own-x" repo, possibly containing a tutorial about building a RISC-V processor in Verilog ("From Blinker to RISC-V" sounds like a specific tutorial).

Let me explore the workspace first to see what's there, then plan milestones and create a minimal skeleton.

Per my instructions: Before modifying code, call `explore` once to record files read/intended. For multi-step change, call `plan`. Let me first look at the directory contents.

Let me start with glob to see what's in the workspace.工作区是空的。先确认一下「From Blinker to RISC-V」这个教程的实际章节结构，让里程碑对齐原教程。搜索无结果，直接查 build-your-own-x 原始列表确认教程出处。找到了：教程出自 `BrunoLevy/learn-fpga` 的 `FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV`。拉取教程目录确认章节结构。教程结构确认：24 个 Step + Episode II (流水线) + Episode III (中断)。检查本机可用的仿真/综合工具链，然后规划。本机没有任何 FPGA 工具链（iverilog/verilator/yosys 均未安装），骨架将以仿真优先设计，Makefile 做工具探测。教程共 24 个 Step + 两个进阶 Episode，里程碑按此映射。brew 安装被环境拦截。退而验证 Makefile 的工具探测路径与整体骨架，仿真留给你本机一条命令跑通。工具探测与报错路径符合预期。修正一个兼容性风险：`$fatal` 需要 SystemVerilog 模式，把 Makefile 编译选项从 `-g2005` 换成 `-g2012`（Icarus 11+，brew 装的是 12.x）。安装类命令均被环境拦截，仿真验证只能由你本机执行。做最后的结构核对。核对里程碑覆盖度时发现遗漏：教程 Step 13–14（子程序调用约定）未映射到任何里程碑。补进 M4（保持与教程顺序一致），Step 12 也从“选读”改为显式列出。Step 14/21/24 藏在 "Step 13–14"、"Step 20–21"、"Step 23–24" 区间写法里，单独确认一下：里程碑与骨架已就绪，Step 1–24 + Episode II/III 全部映射完毕。

**里程碑**（`docs/MILESTONES.md`）：M0 点灯 → M1 ROM+FSM 建立“取指-执行”直觉 → M2 译码器/寄存器堆/ALU 三件套 → M3 控制流（jumps/branches/LUI/AUIPC）→ M4 存储+子程序+load/store（此时已是完整 RV32I 微控制器）→ M5 MMIO/Verilator/GNU 工具链 → M6 SPI Flash 启动 + 流水线 + 中断。策略是仿真优先，每步都有可自检产物，上板作为可选验证。

**骨架**：
- `rtl/step1_blinker.v` — 计数器 MSB 点灯（教程 Step 1 原样）
- `tb/tb_step1.v` — 自检 testbench：校验 LED 翻转周期恰为 2^(WIDTH-1) 个时钟、无 X/Z，PASS/FAIL 决定退出码
- `Makefile` — `make sim`（默认）/ `lint` / `clean`，工具缺失时给出安装提示；用 `-g2012` 因为 testbench 用了 `$fatal`
- `README.md` — 进度清单，随学习勾选

**待你执行的一步**：环境拦截了 brew 安装，本机跑 `brew install icarus-verilog && make sim`，看到 `PASS: 3 toggles observed` 即骨架验证通过。之后按里程碑推进，每完成一个 Step 就在 README 勾掉对应项。