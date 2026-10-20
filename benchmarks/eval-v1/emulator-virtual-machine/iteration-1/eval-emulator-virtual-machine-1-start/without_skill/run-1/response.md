The user wants to write a CHIP-8 emulator and asks which language to use and what milestone 1 should be. This is a question, not a code modification task. The workspace is a "build-your-own-x" repo about emulators/VMs — likely the CHIP-8 guide is in there. Let me check the workspace for relevant reference material to ground my answer.

I should look at what's in the workspace. Let me glob for CHIP-8 related files. This is a simple advisory question, so I don't need plan/todo. A quick exploration of the repo's CHIP-8 guide would let me give a grounded milestone 1. Let me do a glob and maybe grep in parallel.The workspace appears empty (or glob isn't matching). Let me check with bash ls to be sure.Workspace is empty, so this is greenfield. My recommendation:

**Language: C.** CHIP-8 is small enough that C's manual memory model is a feature — the emulator is literally `uint8_t memory[4096]`, `uint8_t V[16]`, `uint16_t I, pc`, and a switch statement. Nearly every reference implementation and test-log tooling is in C. Rust is a fine second choice if you want safety rails; Python works for learning the concepts but you'll fight it when you get to timing and the display loop.

**Milestone 1: a headless CPU core that fetches, decodes, and executes — no graphics, no sound, no input.**

Concretely, done when:
1. ROM loaded into `memory` at `0x200`, PC starts there.
2. Opcode dispatch skeleton (big `switch (opcode & 0xF000)`) with the trivial opcodes implemented: `00E0` (CLS as a no-op for now), `1NNN` (jump), `2NNN`/`00EE` (call/return), `6NNN`/`7NNN` (set/add register), `ANNN` (set I).
3. A trace mode printing `PC opcode` each cycle.
4. Verified by running the IBM Logo ROM and diffing your trace against a known-good log (Laurent Couvidou's / "chip8-test-rom" logs are the standard).

Everything else — `DXYN` drawing, timers, keypad, sound — builds on this loop, so resist adding graphics until the core is proven against a reference trace.