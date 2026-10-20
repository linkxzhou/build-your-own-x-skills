The user wants to build their own RISC-V CPU in Verilog but has no FPGA board. This matches the build-your-own-x skill — specifically the "CPU" category. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it, and also find the CPU track skill. The category map was truncated. Let me read more of the SKILL.md and look at the skills directory.The category map maps RISC-V/Verilog → `processor` track. Let me read that track skill.The track confirms simulation-only is fine. Let me read the per-tutorial skill for the RISC-V/Verilog track and check what simulators are already available in this environment.No simulators installed. The skill says: never install anything myself; print the exact command for the learner. Also check the tutorial-map.md and concepts.md for milestone details. Let me read those two reference files quickly.Yes — an FPGA board is optional for this whole project. Simulation is the standard way to learn CPU design, and it's actually better for debugging: you get full waveforms of every wire, every cycle, which a real board can't give you. Hardware only becomes relevant at the final stretch milestone, and everything before it runs entirely on your machine.

Here's the path (from the [From Blinker to RISC-V](https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV) tutorial, the upstream guide we'll follow):

| # | Milestone | You learn | Checkpoint |
|---|---|---|---|
| 1 | Blinker + testbench | modules, clocks, reset, waveforms | LED signal toggles in a VCD you open in GTKWave |
| 2 | ALU | combinational logic, opcodes | testbench checks add/sub/and/or against expected values |
| 3 | Register file + PC | sync write, async read, x0=0 | written registers read back correctly |
| 4 | Single-cycle RV32I subset | decode, immediates, branches | hand-assembled program computes sum 1..10 = 55 |
| 5 | Memory + I/O | instruction/data memory, MMIO | program prints to a simulated UART |
| 6 | Compliance tests | riscv-tests | RV32I test suite passes |
| 7 | Stretch: pipeline / FPGA | hazards, CPI, real board | pipelined core passes the same tests |

**Toolchain** — you need a simulator and a waveform viewer. I checked this workspace: neither is installed yet, so run the one for your OS yourself:

- Ubuntu/Debian/WSL: `sudo apt install iverilog gtkwave`
- macOS: `brew install icarus-verilog` and `brew install --cask gtkwave`
- Windows: easiest is WSL2 with the Ubuntu command above; alternatively the [OSS CAD Suite](https://github.com/YosysHQ/oss-cad-suite-build) bundles everything natively

Milestone 1's check will be: `iverilog -o blink.vvp blink.v blink_tb.v && vvp blink.vvp` printing toggle messages, with a `blink.vcd` you open in GTKWave.

Two questions to set the scope:

1. Which OS are you on, so I give you the right install command and any platform quirks?
2. Have you written any Verilog (or other HDL) before? If yes we can compress milestones 1–2; if this is your first HDL, we start from the blinker exactly as listed.