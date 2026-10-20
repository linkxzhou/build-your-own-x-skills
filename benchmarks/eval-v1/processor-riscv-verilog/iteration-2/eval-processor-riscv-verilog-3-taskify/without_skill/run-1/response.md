The user wants me to convert the FemtoRV tutorial "FROM_BLINKER_TO_RISCV" from BrunoLevy's learn-fpga repository into a Claude Code executable learning task list. Let me first fetch the tutorial content to understand what it covers.

Let me start by fetching the tutorial from GitHub.GitHub 页面抓取的内容大多是导航信息。让我来获取原始的 README。README 文件很大。我把它下载到工作区，以便完整阅读。文件已存在（可能是之前下载的）。我来阅读一下 README 以了解教程结构。I now have a comprehensive understanding of the tutorial. Let me also check the FIRMWARE_Makefile and run.sh scripts to understand the tooling, then design the Claude Code executable learning task list.

Let me look at the remaining files quickly.Now I have a complete picture of the tutorial. Let me design the Claude Code executable learning task list.

The tutorial has:
- Prerequisites: clone repo, install iverilog, yosys/nextpnr toolchain
- Step 1: first blinky (SOC module, count, LEDs)
- Step 2: slower blinky (Clockworks gearbox, RESET)
- Step 3: blinker loading LED patterns from ROM (PC, MEM fetch)
- RISC-V ISA intro (11 instruction types)
- Step 4: instruction decoder (opcode, rs1/rs2/rd, funct3/funct7, 5 immediate formats)
- Step 5: register bank + state machine (FETCH_INSTR, FETCH_REGS, EXECUTE)
- Step 6: ALU (funct3-based operations)
- Step 7: VERILOG assembler (riscv_assembly.v, PC as address)
- Step 8: jumps (JAL, JALR, nextPC)
- Step 9: branches (6 variants, takeBranch)
- Step 10: LUI and AUIPC
- Step 11: Memory in separate module (Memory/Processor split, mem_addr/rdata/rstrb)
- Step 12: size optimization (33-bit subtract trick, EQ/LT/LTU, shrinking)
- Step 13: subroutines v1 (JAL x1, JALR return, x10 LEDs)
- Step 14: subroutines v2 (ABI names, pseudo-instructions LI/CALL/RET/MV/NOP/J)
- Step 15: Load (LW/LB/LBU/LH/LHU, sign extension, byte/halfword selection)
- Step 16: Store (SW/SB/SH, mem_wdata/mem_wmask, state machine changes)
- Step 17: memory-mapped devices (IO page bit 22, 1-hot addressing, LEDs, UART, putc)
- Step 18: Mandelbrot set (fixed point, mulsi3, ASCII art)
- Step 19: Verilator (faster simulation)
- Step 20: GNU toolchain - assembly (riscv64-unknown-elf-as, ld, firmware.hex, $readmemh)
- Step 21: GNU toolchain - C (sieve.c, mandel_C.c, riscv_logo.c, libgcc, print.c)
- Step 22: SPI flash (MappedSPIFlash, memory quadrants, mem_rbusy, 4-state machine, optimizations)
- Step 23: running programs from SPI flash (WAIT_INSTR busy wait, jump to 0x00820000, spiflash0.ld, iceprog)
- Step 24: better linker script (reset to flash, bss zero-init, data copy, fastcode section)

Now, the user wants this converted into a "Claude Code 可执行的学习任务清单" (Claude Code executable learning task list). This means creating a task list document that Claude Code can execute step by step — like a TODO.md or TASKS.md with concrete, verifiable tasks.

The workspace is empty: /Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-processor-riscv-verilog-3

The user is on macOS (Darwin). The tutorial is Linux-oriented (apt-get), but on macOS we can use brew or oss-cad-suite. Since the user may not have a board, simulation-only path should be emphasized (the tutorial says "If you do not have a board, you can run everything in simulation").

I should create a task list file (e.g., TASKS.md or LEARNING_TASKS.md) in the workspace that:
1. Is structured for Claude Code to execute: each task has clear objective, files to create, commands to run, and verification criteria (acceptance criteria).
2. Covers all 24 steps + prerequisites.
3. Is simulation-first (macOS, no board assumed), with optional device steps marked.
4. Each task should be independently executable by Claude Code in a session: "implement stepN.v, create bench, run iverilog, verify output".

Design considerations for "Claude Code executable":
- Tasks should be phrased as imperative instructions with clear deliverables and verification commands.
- Include a progress checkbox format (- [ ]) so Claude Code can track.
- Include environment setup task (install iverilog/verilator via brew, clone learn-fpga).
- Include verification: run.sh equivalent commands, expected outputs.
- Group into phases/milestones.
- Each task should reference the tutorial section for context.

Since the workspace is empty and this is a "build your own x processor riscv verilog" eval folder, the user probably wants me to generate the task list file. Let me create a well-structured TASKS.md (in Chinese, since the user asked in Chinese) that Claude Code can execute.

Let me think about what makes each task executable and verifiable in simulation:

Phase 0: Environment setup
- T0.1: Install tools: iverilog, verilator (brew install icarus-verilog verilator), or oss-cad-suite. Verify: iverilog -V, verilator --version.
- T0.2: Clone learn-fpga repo (reference only, we write our own code in workspace). Verify: ls FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV.
- T0.3: Create workspace skeleton: steps/ dir, bench_iverilog.v, run.sh.

Phase 1: Blinker basics (steps 1-3)
- T1: step1.v blinky + bench simulation. Verify: vvp output shows LEDS counting.
- T2: step2.v with Clockworks gearbox SLOW parameter. Verify: simulation shows slower counting.
- T3: step3.v ROM pattern tinsel with PC. Verify: pattern cycles.

Phase 2: RISC-V datapath (steps 4-7)
- T4: instruction decoder (isXXX signals, register ids, funct3/7, 5 immediate formats). Verify: bench displays recognized instruction for a few encoded words.
- T5: register bank + 3-state FSM. Verify: state machine cycles.
- T6: ALU. Verify: run test program, LEDs show expected.
- T7: VERILOG assembler integration + PC as byte address. Verify: same program result as step6.

Phase 3: Control flow (steps 8-10)
- T8: JAL/JALR + nextPC. Verify: infinite loop program runs.
- T9: branches (6 variants + takeBranch). Verify: count 0..31 loop stops.
- T10: LUI/AUIPC. Verify: writeBackData mux.

Phase 4: Memory & optimization (steps 11-12)
- T11: Memory module split (mem_addr/rdata/rstrb). Verify: program still runs.
- T12: ALU shrink (33-bit subtract, EQ/LT/LTU). Verify: program still runs; optionally check LUT count with yosys.

Phase 5: Subroutines (steps 13-14)
- T13: wait function with JAL/JALR, x10 LEDs. Verify: blinky works.
- T14: ABI names + pseudo-instructions. Verify: same blinky rewritten.

Phase 6: Load/Store (steps 15-16)
- T15: Load instructions (LW/LB/LBU/LH/LHU + LOAD_data mux). Verify: test program loads data.
- T16: Store (SW/SB/SH + wmask + FSM changes). Verify: store/load roundtrip test.

Phase 7: SOC & software (steps 17-19)
- T17: memory-mapped IO (1-hot, LEDs device, UART TX, putc). Verify: "Hello" printed in terminal/simulation.
- T18: Mandelbrot in assembly (fixed point, mulsi3). Verify: ASCII art in output.
- T19: Verilator setup. Verify: run_verilator.sh works, faster.

Phase 8: GNU toolchain (steps 20-21)
- T20: riscv toolchain install + blinker.S + firmware.hex + $readmemh. Verify: blinky runs from compiled firmware.
- T21: C programs (sieve.c, mandel_C.c). Verify: output correct.

Phase 9: SPI flash (steps 22-24) — mostly device-oriented; simulation can partially verify
- T22: MappedSPIFlash module + memory quadrants + mem_rbusy + 4-state FSM. Verify in simulation with a fake flash model.
- T23: run from flash (spiflash0.ld, iceprog). Device required; simulation alternative.
- T24: better linker script (bss/data init, fastcode). Device required.

Since the user is on macOS without a board mentioned, I'll mark device tasks as optional and provide simulation-only verification paths. For SPI flash steps, simulation with a behavioral flash model is possible but complex; I'll note that.

Also should include "Try this" exercises from the tutorial as optional stretch tasks (knight driver etc.) — good for learning.

Format for Claude Code executability: each task should have:
- 目标 (goal)
- 产出文件 (deliverables)
- 参考教程章节 (reference)
- 实现要点 (key implementation points)
- 验收标准 (acceptance criteria with concrete commands and expected output)

I'll write this as TASKS.md in the workspace root. Also maybe a CLAUDE.md so Claude Code picks up context automatically? The user asked for a "学习任务清单" (learning task list). A single TASKS.md is the core deliverable. Adding a small CLAUDE.md that points to TASKS.md and defines conventions (how to run sims, where files live) would make it genuinely "Claude Code executable" — Claude Code auto-reads CLAUDE.md at session start. That's a reasonable, minimal addition.

Let me also record an explore note first per the instructions (explore → plan → execute). I've done extensive exploration. Let me call explore to consolidate, then plan, then write the files.

Actually, the instructions say: "Before modifying code, call `explore` once to record the files you have read". I've read the tutorial docs. Let me do that now, then plan, then write.

One important decision: language. The user wrote in Chinese, so the task list should be in Chinese (with code/commands in English). 

Another decision: should tasks copy tutorial files or write from scratch? The tutorial's pedagogy is progressive: each step builds on the previous. For Claude Code execution, the cleanest approach: create each stepN.v in the workspace (self-contained, following the tutorial), with a shared bench_iverilog.v and run.sh. The tutorial files are available in the cloned repo for reference/diffing. The task list should instruct Claude Code to write the code itself (learning) and compare with the reference when stuck.

Also note: the tutorial's bench_iverilog.v uses BOARD_FREQ etc. and the run.sh passes -DBENCH -DSIM -DPASSTHROUGH_PLL. The Clockworks module handles PLL passthrough in simulation. For simplicity in our workspace, I'll define a simpler convention: each step file includes clockworks.v (copied from repo) and the bench toggles CLK. Actually the tutorial's approach works: copy bench_iverilog.v, clockworks.v, riscv_assembly.v from the repo into the workspace lib/ directory. That's the pragmatic path — those are infrastructure files, and the learning is in stepN.v.

Wait — but for a learning task list, should Claude Code copy infrastructure files or write them? The tutorial itself provides clockworks.v and riscv_assembly.v as given files (the tutorial text shows their content and explains them). Copying them from the cloned repo is faithful to the tutorial. The learning happens in the SOC/Processor code. I'll structure it that way: T0.3 copies infra files (bench_iverilog.v, clockworks.v, riscv_assembly.v, run.sh) from the cloned repo into workspace.

Hmm, but bench_iverilog.v in the repo references BOARD_FREQ and PASSTHROUGH_PLL defines. The run.sh passes those. Fine.

Also for macOS: brew install icarus-verilog verilator. riscv toolchain: brew install riscv-tools? Actually there's `riscv64-elf-gcc` formula in homebrew (riscv64-elf-gcc, riscv64-elf-binutils). Or use the prebuilt from the FemtoRV makefile (which downloads xPack or similar). The tutorial's makefile downloads a toolchain. On macOS, xPack riscv-none-elf-gcc works. I'll offer: `brew install riscv64-elf-gcc riscv64-elf-binutils` (names: riscv64-elf-gcc exists in homebrew). Let me not over-specify; the task can say install riscv64-elf-gcc via brew or use FemtoRV's make target.

For the SPI flash steps on macOS without board: mark as "device required" and provide simulation alternative (behavioral flash model). Actually step22's read_spiflash can be simulated if we add a simple SPI flash simulation model... that's complex. The tutorial's spi_flash.v has a BENCH mode? Not sure. I'll mark steps 22-24 as advanced/optional with device recommended, simulation partial.

Let me now also think: the eval folder name is "build-your-own-x-processor-riscv-verilog-3" — this is likely from the build-your-own-x list. The user wants a task list that Claude Code can execute. So the deliverable is the task list document itself. I'll create:

1. `TASKS.md` — the main learning task list (Chinese), with phases, tasks, acceptance criteria, checkboxes.
2. `CLAUDE.md` — brief conventions for Claude Code sessions (workspace layout, how to run simulation, task execution protocol: pick next unchecked task, implement, verify, check off).

Keep it focused. Let me write these now.

Structure of TASKS.md:

# From Blinker to RISC-V — Claude Code 学习任务清单

简介: 基于 BrunoLevy/learn-fpga FemtoRV 教程, 24 步从 blinky 到 RV32I SoC。仿真优先 (macOS 无板也可完成 ~90%), 开发板任务标记 [板卡]。

## 使用方法 (给 Claude Code 的执行协议)
- 每次会话: 读 TASKS.md, 找第一个未完成任务, 按"实现要点"写代码, 跑"验收标准"里的命令, 全部通过后把 `- [ ]` 改成 `- [x]` 并在任务末尾追加一行完成记录 (日期 + 关键观察)。
- 一次只做一个任务。卡住时参考 .tutorial-ref/README.md 对应章节或克隆仓库里的 stepN.v 参考实现。
- 不跳步: 每一步建立在上一步之上。

## 里程碑总览
M0 环境 → M1 闪烁灯 (step1-3) → M2 数据通路 (4-7) → M3 控制流 (8-10) → M4 存储与优化 (11-12) → M5 子程序 (13-14) → M6 Load/Store (15-16) → M7 SoC 与软件 (17-19) → M8 GNU 工具链 (20-21) → M9 SPI Flash (22-24, 板卡)

## Phase M0: 环境准备
### T0.1 安装仿真工具
- 命令: brew install icarus-verilog verilator
- 验收: iverilog -V; verilator --version
### T0.2 克隆参考仓库
- git clone --depth 1 https://github.com/BrunoLevy/learn-fpga.git reference/learn-fpga
- 验收: reference/learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/step1.v 存在
### T0.3 搭建工作区骨架
- mkdir steps; 拷贝 bench_iverilog.v clockworks.v riscv_assembly.v run.sh terminal.sh
- 验收: ./run.sh steps/step1.v 能跑通 (用参考 step1 先验证基础设施) — hmm, 或者直接进入 T1。

Actually simpler: T0.3 copies infra files and verifies with the reference step1.v copied temporarily. Or just verify iverilog works on a trivial file. I'll make T0.3 copy infra + verify with reference step1.v (sanity check of infra), then T1 writes our own step1.v.

## Phase M1: 三个 blinky (教程 Step 1-3)
### T1 step1.v — 第一个 blinky
- 产出: steps/step1.v
- 要点: SOC 模块端口 CLK/RESET/LEDS[4:0]/RXD/TXD; 5 位计数器; assign LEDS = count
- 验收: ./run.sh steps/step1.v 输出 LEDS 递增序列; 回答"为什么板上看不见闪烁"
- 思考题(可选): 减速; knight rider
### T2 step2.v — Clockworks 变速箱
- 要点: SLOW 参数, 2^SLOW 分频, resetn
- 验收: 仿真计数变慢
### T3 step3.v — ROM 图案
- 要点: MEM[0:20] initial 块, PC 循环
- 验收: 图案循环输出

## Phase M2: 处理器数据通路 (Step 4-7)
### T4 step4.v — 指令译码器
- 要点: 10 个 isXXX opcode 信号; rs1Id/rs2Id/rdId; funct3/funct7; Uimm/Iimm/Simm/Bimm/Jimm 符号扩展
- 验收: 内存放几条手工编码指令, 仿真打印识别结果
### T5 step5.v — 寄存器堆 + 状态机
- 要点: RegisterBank[0:31]; FETCH_INSTR/FETCH_REGS/EXECUTE; writeBack (rdId!=0)
- 验收: 状态机循环
### T6 step6.v — ALU
- 要点: aluIn1/2, funct3 case, shamt, ADD/SUB via funct7[5]&instr[5]
- 验收: 执行一段 ALU 程序, 结果写入 LEDS/x1 观察
### T7 step7.v — VERILOG 汇编器 + PC 字节地址
- 要点: include riscv_assembly.v; PC+4; MEM[PC[31:2]]
- 验收: 用汇编重写 step6 程序, 结果一致

## Phase M3: 控制流 (Step 8-10)
### T8 step8.v — JAL/JALR
### T9 step9.v — 分支
### T10 step10.v — LUI/AUIPC (里程碑: 8/11 类指令完成)

## Phase M4: 存储与瘦身 (Step 11-12)
### T11 step11.v — Memory 独立模块
### T12 step12.v — ALU 瘦身 (33 位减法技巧)

## Phase M5: 子程序 (Step 13-14)
### T13 step13.v — JAL/JALR 调用约定, x10→LEDS
### T14 step14.v — ABI 名字 + 伪指令

## Phase M6: Load/Store (Step 15-16)
### T15 step15.v — 5 种 Load
### T16 step16.v — 3 种 Store + wmask (里程碑: 完整 RV32I 核心)

## Phase M7: SoC 与软件 (Step 17-19)
### T17 step17.v — 内存映射 IO + UART + putc
### T18 step18.v — Mandelbrot 汇编 (定点数, mulsi3)
### T19 Verilator 加速仿真

## Phase M8: GNU 工具链 (Step 20-21)
### T20 汇编工具链: riscv64-unknown-elf-as/ld, firmware.hex, $readmemh
### T21 C 工具链: sieve.c / mandel_C.c, libgcc

## Phase M9: SPI Flash (Step 22-24) [需要板卡, 仿真部分可选]
### T22 step22.v — MappedSPIFlash + 四象限地址 + mem_rbusy + 4 状态 FSM
### T23 step23.v — 从 Flash 执行 (spiflash0.ld, iceprog -o 128k)
### T24 step24.v — 完整链接脚本 (bss 清零, data 拷贝, fastcode)

## 附录
- 常见陷阱 (来自教程): case 需要 default 防止 latch; x0 写忽略; IceStick 复位按钮=触摸 pin47; BRAM 6KB 限制; firmware_words 95% 警告
- 参考文件清单

For each task I should include: 教程章节 anchor, 产出, 实现要点 (bullet list of the key verilog changes), 验收标准 (concrete commands + expected), 可选练习 (the "Try this" items).

This will be a long file but that's the point — it's a complete executable task list. Let me keep each task tight though. I'll write it now.

Also CLAUDE.md — short, pointing to TASKS.md, workspace conventions:
- steps/ contains stepN.v
- infra files at root: bench_iverilog.v, clockworks.v, riscv_assembly.v, run.sh
- run simulation: ./run.sh steps/stepN.v
- reference: reference/learn-fpga/... and .tutorial-ref/README.md
- protocol: one task per session, verify before checking off, append completion note.

Wait — should I put the reference repo clone inside the workspace? The .tutorial-ref dir I created has the docs. I'll keep .tutorial-ref (rename to docs/ maybe? It's fine as is, but a cleaner name: tutorial-docs/). Actually I already created .tutorial-ref with README.md, PIPELINE.md, INTERRUPTS.md, toolchain.md, FIRMWARE_Makefile, bench_iverilog.v, run.sh, run_verilator.sh, step20.v, terminal.sh. Hmm, those infra files (bench_iverilog.v, run.sh, etc.) came from the earlier download — wait, how did those get there? The /tmp/femtorv dir already had them before my curl (the ls showed INTERRUPTS.md etc. with earlier timestamps 10:50-10:55 while my curl was 10:56). Interesting — maybe a previous session downloaded them. Anyway, they're useful.

Plan: 
- Keep .tutorial-ref/ as the local doc reference (it has README.md + infra file samples).
- TASKS.md instructs T0.2 to clone the full repo into reference/learn-fpga for stepN.v reference implementations and BOARDS/ scripts.

Actually, wait: do I want the infra files copied from the repo at T0.3? The repo's TUTORIALS/FROM_BLINKER_TO_RISCV dir contains bench_iverilog.v, run.sh, clockworks.v, riscv_assembly.v, sim_main.cpp, run_verilator.sh, terminal.sh. Yes — T0.3 copies those into workspace root. That gives us the exact tutorial infrastructure.

One more consideration: the tutorial's run.sh hardcodes BOARD_FREQ=10 etc. and bench_iverilog.v handles PLL passthrough with -DPASSTHROUGH_PLL. Good, works on macOS with iverilog.

For Verilator on macOS via brew: fine. sim_main.cpp comes from the repo.

For the RISC-V toolchain on macOS: `brew install riscv64-elf-gcc riscv64-elf-binutils` provides riscv64-elf-gcc/as/ld (note: prefix is riscv64-elf- not riscv64-unknown-elf-). The FIRMWARE Makefile uses variables RVAS/RVLD etc. from makefile.inc — might need overriding. I'll note in T20: either use FemtoRV's `make ICESTICK.firmware_config` toolchain download (Linux-oriented binaries may be x86_64 Linux — won't work on macOS!) or brew's riscv64-elf-gcc and adjust the prefix. Important macOS gotcha: the FemtoRV bundled toolchain is Linux x86_64, so on macOS use brew. I'll write that.

Actually the makefile.inc probably detects. To be safe, T20 will say: on macOS install `brew install riscv64-elf-gcc riscv64-elf-binutils`, then either symlink riscv64-unknown-elf-* names or pass make vars. Keep it as a hint, Claude Code will figure out details at execution time.

Also firmware_words tool: built from FemtoRV/FIRMWARE/TOOLS (C program, compiles on macOS fine with make/gcc/clang).

Now, regarding "验收标准" for each step — concrete and checkable:

T1: `./run.sh steps/step1.v` prints LEDS values incrementing (binary counter). Expected: lines "LEDS = 00001" etc. Actually with count starting 0 and 5 bits, output shows counting. Good.

T2: same but slower — in simulation with SLOW=2 or so, fewer LED changes per time. The bench prints on change; verification: it still counts, and with SLOW parameter the rate decreases. Concrete: set SLOW=2 in sim (via `ifdef BENCH?) — the tutorial's clockworks uses SLOW parameter; in bench the tutorial passes -DPASSTHROUGH_PLL? Hmm, actually looking at run.sh: -DPASSTHROUGH_PLL — that likely makes Clockworks skip the PLL in simulation. The SLOW gearbox still applies? In step2 the tutorial says run ./run.sh step2.v and "the counter is now much slower" — so gearbox applies in sim. OK verification: LEDS change every 2^SLOW clocks; can verify by counting clock cycles between changes in output... simpler: visually confirm slower + design synthesizable. I'll phrase: 仿真输出仍为递增计数, 且相邻两次 LEDS 变化之间隔 2^SLOW 个时钟 (可在 bench 里加 $display 统计). Keep it simple: "LEDS 仍递增; 将 SLOW 调大后输出变化频率明显降低".

T4: put 3-4 hand-encoded instructions in MEM, bench displays which isXXX fires. The tutorial's step4 lights different LEDs per instruction. Verification: for a known ADDI encoding (0x00100093), isALUimm==1. In bench, $display the recognized class. Concrete: `./run.sh steps/step4.v` prints recognized instruction names matching the encoded words.

T5: state machine cycles through states; LEDs show state. Verification: bench prints state transitions FETCH→FETCH_REGS→EXECUTE.

T6: run the tutorial's step6 program (ADDI x1 four times, ADD x2, ADD x3, SRLI/SLLI/SRAI, SRLI → LEDS). Expected final LEDS value. The tutorial program: x1=4, x2=4, x3=8, SRLI(x3,3)→1, SLLI(x3,31)→0x80000000, SRAI(x3,5)→0xFC000000, SRLI(x1,x3,26)→0xF (15). So LEDS = 0b01111 = 15. Verification: final LEDS == 15 (5-bit). Nice concrete check. Let me double check: x3 = 0x80000000; SRAI 5: 0x80000000 >> 5 arithmetic = 0xFC000000. x1 = 0xFC000000 >> 26 = 0b1111 = 15? 0xFC000000 = 1111 1100 ... top 6 bits are 111111, >>26 gives 6 bits: 0b111111 = 63, but LEDS is 5 bits → 0b01111 = 15. Yes LEDS=15.

T7: same program via assembler, same result LEDS=15.

T8: infinite loop incrementing x1 wired to LEDS; sim shows LEDS incrementing forever (stop with ctrl-c / finish). Verification: LEDS increments.

T9: count 0→31 then EBREAK stops (PC stays). Verification: LEDS reaches 31 and stops changing. In bench, EBREAK → isSYSTEM... tutorial: EBREAK halts? In their design, SYSTEM instr does nothing and PC doesn't advance? Actually in step22 EXECUTE: if(!isSYSTEM) PC <= nextPC — so SYSTEM instructions stall the CPU (halt). In earlier steps, EBREAK just... hmm, in step9 the program counts 0..31 and stops — because after EBREAK, PC keeps incrementing into empty memory (MEM initialized to 0 = ? opcode... instr 0 is not any known opcode, so no writeback, PC increments through zeros — effectively does nothing visible). LEDs stay at 31. Verification: output shows LEDS reaching 11111 and no further change.

T10: LUI/AUIPC test — tutorial says run step10; program probably loads constants. Verification: write a small program using LUI+AUIPC, check register values via LEDs or $display. I'll suggest: LUI(x1, 0x12345) then display; and AUIPC check. Concrete: use bench $display of writeBackData? Simpler: program: LUI(x5,0xDEADB); EBREAK; bench displays RegisterBank[5]? The bench only sees LEDS. Hmm — wire x10 to LEDs? At step10 LEDs are wired to x1 still (until step13). Program can copy: LUI(x1,...). Fine: LUI(x1,0x0000B); ADDI... Actually simplest: verify via simulation $display in design? The tutorial design doesn't $display. Alternative: MV via ADD. Let me just specify: 程序 LUI(x1,32'h12345) → LEDS 应显示 0x12345 的低 5 位 (10101); AUIPC(x1,0) → LEDS 显示当前 PC 低 5 位. Good enough, concrete.

T11: memory split; same program runs (LEDS=15 program or loop). Verification: step9-style loop still works with separate Memory module.

T12: after shrink, same tests pass (T6 program LEDS=15, T9 loop). Verification: regression — run both programs.

T13: blinky with wait subroutine; LEDs increment slowly. Verification: sim shows LEDS incrementing (with slow_bit=15 in BENCH).

T14: same blinky with ABI names/pseudo-instrs. Verification: same behavior.

T15: load test: store... wait, no store yet at step15! How to get data into memory to load? The tutorial step15: memory contains data words placed via DATAB or initial; program does LW from a label. The tutorial's step15 program: uses LW to read... I recall it loads from memory-mapped... Let me not overthink: program places a known constant word in MEM via the assembler's DATAB/word directive, LW it into x1 → LEDS. Also test LB/LBU sign extension with a byte 0xFF: LB → 32'hFFFFFFFF (LEDS=31), LBU → 0xFF (LEDS=31 too, 5 bits...). Hmm 5-bit LEDS can't distinguish. Use $display in bench? The bench only monitors LEDS. For verification, I can suggest temporarily wiring LEDS to different registers or adding a $display in the Memory/Processor for load results (simulation-only). Simplest: route x1 to LEDS and choose test values whose low 5 bits differ: LB of 0x80 → 0xFFFFFF80 (low5=00000), LBU of 0x80 → 0x00000080 (low5=00000)... same. Pick byte 0xA0: LB→0xFFFFFFA0 low5=00000; LBU→0xA0 low5=00000. Ugh, bit5 set in 0xA0. 0x80: low 5 bits both 0. Pick 0x90: LB→0xFFFFFF90 (low5=10000=16), LBU→0x90 (low5=10000=16). Same again — sign extension only affects upper bits! Low 5 bits always identical for LB vs LBU. So LEDS can't distinguish; must check full 32 bits. Solution: bench enhancement — add $display of mem_rdata/writeBack, or wire LEDS = x1 in one test and use $display in design under `ifdef BENCH. I'll specify: 在 `ifdef BENCH 下加 $display 打印 writeBackData, 验证 LB(0x90)→0xFFFFFF90, LBU(0x90)→0x00000090. That's a clean, concrete acceptance criterion and teaches simulation debugging. 

T16: store/load roundtrip: SW then LW; SB to byte 1 of a word then LW check. Verification: roundtrip values match via $display or LEDS.

T17: UART putc prints "Hello" — in iverilog bench, TXD toggles; the tutorial's bench_iverilog.v probably decodes UART TX? The repo bench has UART decoding? sim_main.cpp for verilator decodes LEDs; for iverilog, terminal.sh uses a UART decoder? terminal.sh: let me check — it's 459 bytes; likely uses a python/awk UART decoder on TXD? Actually terminal.sh probably runs `uart_tty` something. Hmm. In simulation, capturing UART TXD requires a decoder. The repo's bench_iverilog.v might include a UART RX decoder printing characters. I can't be sure without reading it. Let me read .tutorial-ref/bench_iverilog.v (426 bytes — small, probably no UART decode). 426 bytes is tiny — just clock wiggler. So for T17 verification in iverilog sim: either add a UART TX decoder to the bench (a nice exercise; ~30 lines: sample at baud, deserialize, $display char) or verify TXD waveform toggles. I'll make the task: extend bench with a UART TX decoder (spec: 115200 given BOARD_FREQ, sample mid-bit) and verify "Hello from FemtoRV" appears. That's executable and satisfying. Alternatively run on device + terminal.sh. I'll offer both, sim decoder as the sim path.

Actually wait — the repo's TUTORIALS dir may have a uart decoder in bench_iverilog.v... 426 bytes says no. But FEMTOCRV main SoC tests? Whatever — writing a small UART decoder in the bench is a good learning task and makes T17/T18 verifiable in sim. 

T18: Mandelbrot — verification: sim output shows ASCII mandelbrot/disk pattern.

T19: verilator run of step18 — faster; verification: obj_dir/VSOC runs and prints same art.

T20: compiled blinker.S → firmware.hex → step20.v $readmemh → sim blinks (LEDS toggling pattern 5/10). Verification: sim shows LEDS alternating between 5 (00101) and 10 (01010).

T21: sieve.c compiled → sim prints primes via UART decoder. Verification: primes 2,3,5,7... appear in output.

T22: SPI flash — sim: instantiate MappedSPIFlash with a behavioral flash model (simple: preloaded array responding to SPI commands — that's real work). The repo's spi_flash.v might have a BENCH model. To keep the task list honest: mark T22-T24 as [板卡推荐]; sim alternative: write a minimal SPI flash slave model (read command 0x03, quad I/O) — doable but advanced. I'll phrase acceptance for device path primarily, with sim fallback = implement flash model and verify read_spiflash prints SOC.bin header. Keep it as stretch.

Given macOS + likely no board, I should be explicit: M9 tasks are optional/advanced; core learning outcome (RV32I core running C) is achieved by T21.

Also add a final "capstone" task: T25 (optional): run PIPELINE.md episode II? That's beyond scope; mention as next steps link.

Now the completion-record convention: after each task, append `- ✅ 完成 2026-10-20: <notes>` — but no emojis per style guide. Use `- [x]` plus a `> 完成: ...` line. Keep simple: change checkbox and append one line `<!-- done: date, evidence -->`? Simpler: a "完成记录" section per task where Claude Code appends `- 2026-10-20 通过: LEDS=15`. I'll define that in the protocol.

File layout decision: steps in `steps/`, infra at root. run.sh from repo does `iverilog ... bench_iverilog.v $1 $2` — works with paths.

Let me also include in CLAUDE.md the tool availability check and macOS notes.

Length control: TASKS.md will be ~400-500 lines. That's appropriate for 24 steps. Let me write it efficiently — each task compact: 目标/产出/要点/验收/可选.

Let me write the explore note first (required by instructions before editing), then plan, then write files. Actually I've already done the exploration reading. I'll call explore + plan in parallel? plan depends on nothing from explore output; both are just records. I can call them in one block. Then write the two files, then verify by re-reading.

One more check: the user said "把这个教程转换成 Claude Code 可执行的学习任务清单" — deliverable is the task list. I'll create TASKS.md + CLAUDE.md. I should also clean up: .tutorial-ref stays as local reference (mentioned in docs). Fine.

Let me now write the content. I'll write TASKS.md in Chinese. Keep code identifiers in English.

Draft TASKS.md:

# From Blinker to RISC-V — Claude Code 可执行学习任务清单

来源: [BrunoLevy/learn-fpga · FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV](https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV)
本地文档: `.tutorial-ref/README.md`(教程全文), `.tutorial-ref/PIPELINE.md`(续集), `.tutorial-ref/toolchain.md`(工具链)

最终目标: 从一个 LED 闪烁电路出发, 每次只改一件事, 逐步长出一个能运行 gcc 编译的 C 程序的 RV32I 片上系统 (约 200 行 Verilog)。

环境说明: 本清单按 macOS + 纯仿真路径编写 (无需开发板即可完成 M0-M8); 标注 [板卡] 的任务需要真实 FPGA, 标注 [板卡推荐] 的任务有仿真替代方案。

## 执行协议 (Claude Code 必读)

1. 每个会话只处理一个任务: 从头扫描本文件, 取第一个未勾选 (`- [ ]`) 的任务。
2. 实现前先读 `.tutorial-ref/README.md` 中对应章节 (每个任务都标了章节号)。
3. 代码一律自己写, 写完后才允许对照 `reference/learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/stepN.v` 参考实现找差异 (T0.2 会克隆)。
4. 验收标准里的命令必须全部实际执行并通过, 才能把 `- [ ]` 改为 `- [x]`, 并在该任务末尾追加一行: `> done YYYY-MM-DD: <证据摘要, 如 LEDS=15>`。
5. 验收不过时优先读仿真输出调试; 连续两次失败再对照参考实现。
6. 不跳步、不合并任务; 每一步只引入教程该步的新概念。

## 里程碑总览

| 里程碑 | 任务 | 内容 | 教程章节 |
|---|---|---|---|
| M0 环境 | T0.1-T0.3 | 工具安装、克隆仓库、骨架 | Prerequisites |
| M1 闪烁灯 | T1-T3 | blinky → 变速箱 → ROM 图案 | Step 1-3 |
| M2 数据通路 | T4-T7 | 译码器、寄存器堆+状态机、ALU、汇编器 | Step 4-7 |
| M3 控制流 | T8-T10 | JAL/JALR、分支、LUI/AUIPC | Step 8-10 |
| M4 存储与瘦身 | T11-T12 | 存储独立模块、ALU 优化 | Step 11-12 |
| M5 子程序 | T13-T14 | 调用约定、ABI 与伪指令 | Step 13-14 |
| M6 Load/Store | T15-T16 | 5 种 Load、3 种 Store | Step 15-16 |
| M7 SoC 与软件 | T17-T19 | 内存映射 IO+UART、Mandelbrot、Verilator | Step 17-19 |
| M8 GNU 工具链 | T20-T21 | 汇编、C (里程碑: 跑 gcc 产物) | Step 20-21 |
| M9 SPI Flash | T22-T24 | 大内存、从 Flash 执行、链接脚本 | Step 22-24 |

---

## M0 环境准备

### - [ ] T0.1 安装仿真与综合工具
...

Let me write all tasks concretely. I need to be careful with acceptance commands.

T0.1: 
```
brew install icarus-verilog verilator
```
验收: `iverilog -V | head -1` 和 `verilator --version` 均有输出。
(可选, 板卡用户: 按 .tutorial-ref/toolchain.md 安装 yosys/nextpnr/icestorm, 或直接用 oss-cad-suite 预编译包)

T0.2:
```
git clone --depth 1 https://github.com/BrunoLevy/learn-fpga.git reference/learn-fpga
```
验收: `test -f reference/learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/step1.v && echo OK`

T0.3: 搭骨架
```
mkdir -p steps
cp reference/learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/{bench_iverilog.v,run.sh,clockworks.v,riscv_assembly.v} .
chmod +x run.sh
```
验收: `cp reference/.../step1.v /tmp/step1.v && ./run.sh /tmp/step1.v`... hmm run.sh does `iverilog ... bench_iverilog.v $1` — path relative fine. Actually simpler: `./run.sh reference/learn-fpga/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV/step1.v` prints LEDS counting → 基础设施可用. Then delete nothing (we didn't copy step1). Good.

Wait — does bench_iverilog.v include clockworks? step1.v doesn't include clockworks (plain SOC). step2.v includes "clockworks.v" via `include — include path: iverilog searches the directory of the including file? It searches cwd + -I. run.sh doesn't pass -I. The tutorial runs from the tutorial dir where all files sit together. In our layout, steps/stepN.v includes "clockworks.v" — iverilog resolves includes relative to... the includer's directory? Icarus Verilog searches the directory of the file containing the include directive first? Actually iverilog searches include path: current directory and -I dirs. Hmm, I believe iverilog looks in the directory of the source file containing the `include as well. To be safe, T0.3 can add `-I .` or copy infra into steps/ too. Simplest robust choice: put infra files (bench_iverilog.v, clockworks.v, riscv_assembly.v, run.sh) at workspace root AND run from root with `./run.sh steps/stepN.v`; iverilog's include search: it searches the directory containing the source file... Let me just add `-Isteps -I.` to run.sh in T0.3 to be safe. I'll write: 修改 run.sh, 在 iverilog 参数中加 `-I steps -I .`。That guarantees includes resolve. Good.

Also bench_iverilog.v itself is passed as a compile unit; it doesn't include anything (426 bytes). OK.

M1:

T1 (Step 1): 产出 steps/step1.v。要点: module SOC(CLK,RESET,LEDS[4:0],RXD,TXD); reg [4:0] count; always @(posedge CLK) count <= count+1; assign LEDS=count; assign TXD=0。
验收: `./run.sh steps/step1.v` 输出 LEDS 二进制递增序列 (00000→00001→...)。
理解题 (在完成记录里用一句话回答): LED 在板上为什么"看不见闪"?
可选: knight-rider 版本。

T2 (Step 2): 产出 steps/step2.v。要点: `include clockworks.v; Clockworks #(.SLOW(21)) 分频 2^SLOW; count 用 clk (内部分频后时钟) 与 resetn。
验收: `./run.sh steps/step2.v` 仍输出递增 LEDS; 把 SLOW 改成 2 再跑, 单位仿真时间内变化次数明显变多 (即分频生效)。
可选: RESET 切换方向。

T3 (Step 3): 产出 steps/step3.v。要点: reg [4:0] MEM[0:20] initial 图案; PC 计数循环 (PC==20 归零); leds <= MEM[PC]。
验收: 仿真输出按预存图案循环。
可选: 多模式 + RESET 切换。

M2:

T4 (Step 4): 译码器。产出 steps/step4.v。要点: instr reg; 10 个 isXXX; rs1Id/rs2Id/rdId; funct3/funct7; Uimm/Iimm/Simm/Bimm/Jimm (符号扩展)。
验收: MEM 手工编码 ≥4 条指令 (如 ADDI=0x00100093, ADD=0x002081B3... wait let me compute: ADD x3,x1,x2I was in the middle of drafting TASKS.md content in my thinking. I need to continue and actually write the files. Let me proceed: call explore + plan (records), then write TASKS.md and CLAUDE.md, then verify.

Actually, the previous response was truncated mid-thinking. I should now just take action: write the files. Let me do the explore/plan records quickly and then write TASKS.md and CLAUDE.md.

Let me finalize the task list content and write it. I'll keep each task compact. Key verification details I worked out:

- T6/T7: tutorial step6 program → final LEDS = 15 (0b01111)
- T9: count 0..31 stops at 11111
- T15: LB vs LBU sign extension — low 5 bits identical, so need $display under `ifdef BENCH of writeBackData: LB(0x90)→0xFFFFFF90, LBU(0x90)→0x00000090
- T17: UART TX decoder in bench needed for iverilog sim verification
- T20: macOS brew riscv64-elf-gcc (prefix riscv64-elf-), FemtoRV bundled toolchain is Linux-only
- M9: device recommended, sim fallback with behavioral flash model

Let me write the files now. I'll write TASKS.md (comprehensive) and CLAUDE.md (short conventions). Then verify by checking the files exist and re-reading key sections.

For the ADDI encoding example in T4: ADDI x1, x0, 1 = imm[11:0]=001h, rs1=x0(00000), funct3=000, rd=x1(00001), opcode=0010011 → 0000 0001 0000 0000 0000 0001 0001 0011 = 0x00100093. Correct.

ADD x3,x1,x2: funct7=0000000, rs2=x2(00010), rs1=x1(00001), funct3=000, rd=x3(00011), opcode=0110011 → 0000000 00010 00001 000 00011 0110011 = 0x002081B3. Correct.

Now write. Keep TASKS.md focused but complete. I'll aim for a well-structured ~450 line file.The grep for '^- \[ \]' returned 0. Let me check the actual checkbox format in the file. I wrote "### - [ ] T0.1 ..." — the checkbox is inside a heading, so it's `### - [ ]`. Let me adjust the grep.27 tasks = T0.1–T0.3 + T1–T24, and every tutorial step 1–24 maps to a task (Step 19 is T19, which has no stepN.v file so no "(Step 19)" tag). Final check on T19 and file integrity:完成。已把教程转换为两个文件：

**`TASKS.md`** (360 行) — 27 个可执行任务，覆盖教程全部 24 步：
- **M0** 环境 (T0.1–T0.3): brew 装 iverilog/verilator、克隆参考仓库、拷贝基础设施并冒烟测试
- **M1–M8** (T1–T21): blinky → 译码器/寄存器堆/ALU → 跳转/分支/LUI → 存储拆分/瘦身 → 子程序/ABI → Load/Store (完整 RV32I) → MMIO+UART/Mandelbrot/Verilator → GNU 汇编与 C 工具链
- **M9** (T22–T24): SPI Flash 三步，标注 `[板卡]` 并各附仿真替代验收

每个任务包含：教程章节锚点、产出文件、实现要点 (关键 Verilog 片段)、**可实际执行的验收命令与期望输出** (如 T6 的 `LEDS=01111`、T15 的 `LB→0xFFFFFF90` 符号扩展检查)、教程的 "Try this" 练习。附录 A 汇总了教程全部陷阱 (latch、x0 写忽略、BRAM 读延迟、macOS 工具链前缀等)。

**`CLAUDE.md`** — Claude Code 会话自动读取的执行协议： 一次一个任务、先读教程章节再动手、验收全过才勾选并追加 `> done YYYY-MM-DD: <证据>`、卡住两次才准看参考实现。

针对你的环境做了两个适配： 全程 macOS + 纯仿真路径 (无板卡可完成 M0–M8 核心目标)；T20 标注了教程自带工具链是 Linux x86_64、macOS 需用 `brew install riscv64-elf-gcc`。教程全文已缓存在 `.tutorial-ref/README.md` 供任务执行时查阅。