The user is asking about skipping CHIP-8 and going straight to a Game Boy emulator. This matches the build-your-own-x skill — specifically the "my CHIP-8..." / emulator track. The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md BEFORE doing anything else, then follow it.

Let me read the skill file first.The file was truncated. Let me read the rest of the SKILL.md.The topic maps to the `emulator-virtual-machine` track. Reading the track skill now.The path may be different. Let me glob for skills directories.The track skill lives under `build-your-own-x/skills/`. Reading the track skill, and the Game Boy per-tutorial skill since it's directly relevant.The track skill was truncated. Reading the rest, plus the tutorials reference.Quick check that the test ROM link I'll give you is live:Yes — CHIP-8 is a warm-up, and the Game Boy is a legitimate first target if you accept a longer runway. The skills I coach from agree: the emulator track lists Game Boy as the stretch goal after CHIP-8, but the real prerequisite is the fetch–decode–execute loop, which you can learn directly on the Game Boy's LR35902 CPU.

What you take on by skipping CHIP-8:

- **~500 opcodes instead of 35.** Same decode-dispatch pattern, just a bigger table. The LR35902 is close to the Z80, and most instructions share encodings, so it's tedium rather than difficulty.
- **Real hardware quirks from day one.** Memory-mapped I/O, the boot ROM handoff at 0x100, MBC bank switching, and PPU timing with scanline-accurate rendering. CHIP-8 hides all of this.
- **Debugging without a reference.** CHIP-8 test suites are forgiving; the Game Boy equivalent is Blargg's `cpu_instrs`, which prints PASS/FAIL to serial output — you'll want a serial stub early because it's your only feedback for weeks.

The payoff is that you skip a throwaway project and every hour goes into the machine you actually wanted to build.

Milestone plan (each ends with a runnable check):

1. **Skeleton + ROM loader** — read the ROM, print the header (title, cartridge type, ROM size) and the first bytes at 0x100.
2. **CPU core** — registers, fetch-decode-execute, a handful of opcodes; unit tests on register state.
3. **Full instruction set** — run `cpu_instrs` with a serial logger; each of its 11 sub-tests prints its own result.
4. **Memory map + MBC1** — banking, so bigger ROMs load.
5. **PPU + interrupts + timers** — first visible output, then a playable game.
6. **Debugger** — step mode, register dump, breakpoints.

Pick a guide and language: [Cinoop (C)](https://cturt.github.io/cinoop.html), [codeslinger's GameBoy tutorial (C++)](http://www.codeslinger.co.uk/pages/projects/gameboy.html), [GameBoy Emulation in JavaScript](http://imrannazar.com/GameBoy-Emulation-in-JavaScript), or [0dmg (Rust)](https://jeremybanks.github.io/0dmg/). Test ROMs: [retrio/gb-test-roms](https://github.com/retrio/gb-test-roms) (public-domain Blargg ROMs — use those only, since commercial ROMs are copyrighted).

Which language do you want to build it in? Once you pick, I'll scaffold milestone 1 in your workspace and we start with the ROM header parser.