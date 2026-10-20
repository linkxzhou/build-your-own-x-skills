The user wants to design a simple RISC-V CPU in Verilog and simulate it. They ask "First step?"

There's a skill available: build-your-own-x, which covers "an interpreter/compiler/programming language, an OS, an emulator... a CPU". The description says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills... It picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution."

A RISC-V CPU in Verilog matches "a CPU" category. So I should read the SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. I need to see the category map to find the slug for CPU. Let me read more of the file, and also check the skills directory for a CPU track skill.The map routes "CPU / Verilog / RISC-V" to the `processor` track, and there's a matching per-tutorial skill `processor-riscv-verilog`. Reading both now.Both skills loaded. Let me read the truncated tail of the track skill and its references (tutorial list + tutorial map) so I follow the coaching rules exactly.Skills loaded. The track is `processor` with the upstream guide [_From Blinker to RISC-V_](https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV) (BrunoLevy's learn-fpga). Before proposing milestone 1, let me check your workspace and which simulator tools you already have.**Where we are:** milestone 1/7 — blinker + testbench. Before any CPU, you prove the simulation loop works: clock, reset, registers, waveform dump. The upstream guide we'll follow is [_From Blinker to RISC-V_](https://github.com/BrunoLevy/learn-fpga/tree/master/FemtoRV/TUTORIALS/FROM_BLINKER_TO_RISCV) (BrunoLevy/learn-fpga), adapted to a simulation-only path.

**The concept:** a CPU is clocked registers plus combinational logic. Milestone 1 builds the smallest possible clocked design — a counter that toggles an "LED" every N cycles — plus a testbench that generates the clock, applies reset, and dumps a VCD waveform you can inspect. Everything later (ALU, register file, PC) is just more of the same two ingredients.

**Toolchain:** you have no simulator installed. Run these yourself (I won't install):

```bash
brew install icarus-verilog      # iverilog + vvp simulator
brew install --cask gtkwave      # waveform viewer (optional but recommended)
```

**What to write** — two files, fill the TODOs:

```verilog
// blinker.v
module blinker(
    input  wire clk,
    input  wire rst,
    output reg  led
);
    reg [23:0] count;   // TODO: on posedge clk, increment; on rst, clear
                        // TODO: toggle led when count hits a threshold (e.g. 24'd100)
endmodule
```

```verilog
// tb.v
module tb;
    reg clk = 0, rst = 1;
    wire led;
    blinker uut(.clk(clk), .rst(rst), .led(led));
    always #5 clk = ~clk;              // 100 MHz-ish: 10ns period
    initial begin
        $dumpfile("blinker.vcd");
        $dumpvars(0, tb);
        #20 rst = 0;
        #1000;
        $display("led = %b", led);     // expect it to have toggled
        $finish;
    end
endmodule
```

**Check it:**

```bash
iverilog -o blinker.vvp blinker.v tb.v && vvp blinker.vvp
```

Expected: `led = 1` (or 0, depending on your threshold vs. sim time), and `blinker.vcd` opens in GTKWave showing `count` ramping and `led` as a square wave.

Two scope questions, with my defaults if you don't care:
1. FPGA board in the picture, or simulation-only? Default: simulation-only.
2. Follow the BrunoLevy tutorial's FemtoRV style closely, or go straight to a clean single-cycle RV32I subset? Default: the milestone table above (blinker → ALU → regfile/PC → single-cycle RV32I → memory/UART → compliance tests), which mirrors the tutorial's arc.

Write the two files, run the check, and paste the output — we debug from there.