The user is asking whether they can build their own RISC-V CPU in Verilog without an FPGA board. This is a conceptual/advisory question, not a coding task in the workspace. Let me check what's in the workspace first — the directory name is "build-your-own-x-processor-3" which suggests there might be relevant materials here. Let me take a quick look before answering.

Actually, this is a question that deserves a direct answer: yes, absolutely — simulation-only workflows work fine. Tools like Icarus Verilog/Verilator for simulation, riscv-tests or custom testbenches for verification, and optionally things like web-based FPGA tools (EDA Playground, Icarus on WSL), or free FPGA toolchains (Yosys/nextpnr with open-source boards like iCE40/Tang Nano which are cheap). But since they said they don't have a board, the answer is: simulation is enough to build and verify a full RV32I core.

Let me check the workspace to see if there's existing context — maybe there's a project already started here.Yes — simulation is a complete workflow for this. An FPGA board is only needed at the very end (and optionally even then). Everything that makes you a CPU designer happens on your machine:

**Toolchain (all free, runs on macOS)**
- **Icarus Verilog** (`brew install icarus-verilog`) — simple, great for testbench-driven development.
- **Verilator** — compiles your Verilog to a fast C++ model; the standard for serious verification and running real programs.
- **GTKWave** or **Surfer** — view waveforms when something misbehaves.

**Verification without hardware**
- Write a testbench that loads a program into memory, clocks your core, and checks register/memory state.
- Use the official **riscv-tests** compliance suite (`rv32ui-p-add`, etc.) — each test writes a pass/fail code to a known address; your testbench just watches for it.
- Install `riscv-none-elf-gcc`, compile real C programs, and run them on your simulated core. People have booted Linux on simulated cores — slow, but it proves the design.

**Typical roadmap**
1. RV32I single-cycle core (fetch, decode, ALU, regfile, load/store) + testbench.
2. Pass the full `rv32ui-p-*` test suite.
3. 5-stage pipeline with hazard detection, forwarding, branch flushing.
4. Add CSRs, interrupts, maybe a simple AXI-Lite bus interface.

**When you eventually want real silicon behavior**
- Boards are cheap when you're ready: Tang Nano 9K/20K (~$15–30) works with the fully open Yosys/nextpnr toolchain.
- Zero-install option for quick experiments: EDA Playground in the browser.

The empty workspace here is a fine place to start — the natural first artifact is `cpu.v` (PC + fetch stage) and `tb.v` (a testbench that toggles the clock and dumps waveforms).