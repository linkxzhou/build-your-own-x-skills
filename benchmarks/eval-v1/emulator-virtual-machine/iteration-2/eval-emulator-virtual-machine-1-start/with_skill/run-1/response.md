The user wants to write a CHIP-8 emulator and asks which language to use and what milestone 1 is. This matches the build-your-own-x skill — CHIP-8 emulator is explicitly mentioned in the skill description ("my CHIP-8 draws garbage"). I should read the skill's SKILL.md first before doing anything else.The file was truncated. Let me read the rest of the SKILL.md, and also look for the track skill for emulators. The category slug for emulator is probably "emulator". Let me check the skills directory.The map routes CHIP-8 to the `emulator-virtual-machine` track. Reading that skill now.Reading the rest of the track skill and the tutorials reference in parallel.I have the track skill. Now, per the skill workflow:

1. Agree on scope: language, target, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide matching the language.
3. Work milestone by milestone.

The user asked: "Which language, and what's milestone 1?"

The skill says: Start with CHIP-8 (in a weekend, any language) or LC-3 VM (C). The user already picked CHIP-8. For language: the skill says C, C++, Rust are best for Game Boy/NES; JavaScript works for CHIP-8 in browser. For CHIP-8, any language works. I should ask at most 2 questions and suggest a default. The user asked "which language" — so they want a recommendation. I should give a recommendation with a default, and maybe ask one question about their comfort/preference.

Per the coaching rules: "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care."

The user asked two things: which language, and what's milestone 1. I can answer both directly:

Language recommendation: For CHIP-8, any language works — it's ~35 opcodes, no timing-critical weirdness. Recommendation depends on goals:
- C: closest to the metal, teaches manual memory, matches most tutorials (LC-3 VM in C). 
- Rust: modern, safe, good for later Game Boy/NES.
- Python: fastest to get running, but slow and less "systems" feel.
- JavaScript: runs in browser, zero install for display/input via canvas.

Default suggestion: If they want to later move to Game Boy/NES, C or Rust. If they want quickest visible result, Python or JS. I should ask one question: which language are they most comfortable in? Actually the skill says ask at most 2 questions and suggest a default. The user explicitly asked "which language" — so they want my recommendation. I'll give a default (C or Rust for systems learning; Python if they want speed of iteration) and ask one short question about their comfort.

Milestone 1 per the track skill: Memory + loader. Core concepts: address space, loading a ROM at the right offset. Checkpoint: loader prints the first bytes of the ROM; PC starts at 0x200.

I should explain the concept briefly (3-6 sentences), give a skeleton/interface, and end with the runnable check (command + expected output). Per "Output for each turn": Where we are (milestone 1/6), the concept, what to write next (skeleton/TODO, not full answer), how to check it.

Also: "Do not dump a full solution. Give complete code only for the current milestone, and only when asked, or after the learner has tried." The user hasn't asked for code yet; they asked which language and what milestone 1 is. So I give the concept + skeleton (interface), not full implementation.

Also credit the upstream tutorial with exact link. For CHIP-8: C++ multigesture article, Python omokute, etc. I'll pick based on language default. Since language isn't settled, I can name the guide per language choice.

Also the skill says "Stay in the learner's workspace" — I could offer to scaffold the project. But no install commands. I shouldn't create files yet until language is agreed? The workflow says "Then start milestone 1 in the learner's workspace" after agreeing on scope. Since language is undecided, I should ask the one question and give the default. But the user asked "what's milestone 1" — I can describe it fully so they can start immediately.

Should I check the workspace for existing files? The user hasn't started yet presumably. Let me quickly check if there's anything in the workspace. Actually, a quick glob for existing project files would be useful to see if they already have code. Let me do a quick check — glob for common source files. That's cheap and parallel. Actually the workspace is probably empty. Let me check quickly.

Also per-tutorial skills: `ls skills | grep '^emulator-virtual-machine-'`. The tutorials.md says "Most links also have a per-tutorial coaching skill". From the glob output earlier I saw various skills but the output was truncated. Let me check for emulator-virtual-machine-* skills to know if there's a per-tutorial skill for the CHIP-8 tutorials (multigesture C++, codeslinger C++, omokute Python). That would matter for handoff. Let me glob that.

I'll do: glob for emulator-virtual-machine-* and glob for top-level workspace files in parallel.**Language:** CHIP-8 is small (~35 opcodes, 4 KB of RAM, zero performance pressure) so any language works — pick the one you already write comfortably, since the learning target is the emulation model and fighting unfamiliar syntax doubles the time. My default is **C**: most CHIP-8 reference material is C/C++, the explicit byte-and-pointer work is exactly the skill this project builds, and it carries straight over if you continue to Game Boy or NES later. Rust is the other strong pick; Python gets you a working emulator fastest and is perfectly adequate here.

One question to lock scope: which language do you already write comfortably? If you truly have no preference, say "C" and we start.

Upstream guides I'll coach against: [How to write an emulator (CHIP-8 interpreter)](http://www.multigesture.net/articles/how-to-write-an-emulator-chip8-interpreter/) (C++) or [Emulation Basics: Write your own Chip 8 Emulator/Interpreter](http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8.html) (Python) — there's a per-tutorial coaching skill for each once the language is fixed.

**Roadmap** — each milestone ends with a runnable check:

1. Memory + loader — ROM bytes land at 0x200
2. Fetch–decode–execute — 5 opcodes, unit-tested
3. Full instruction set — a test ROM reports all opcodes OK
4. Display — the IBM logo ROM renders
5. Input + timers — a game is playable at the right speed
6. Debugger — `--step` dumps PC/opcode/registers each cycle

**Milestone 1 — memory + loader**

Concept: a CHIP-8 machine is 4096 bytes of RAM, sixteen 8-bit registers V0–VF, a 16-bit I register, a stack, and a program counter. ROMs load at address 0x200 because on the original hardware 0x000–0x1FF was occupied by the CHIP-8 interpreter itself; your emulator just reserves that region (the built-in font lives at 0x050–0x0A0 — you'll need it at milestone 4, loading it now is optional). Instructions are 2 bytes, big-endian, and PC starts at 0x200. Milestone 1 is: allocate the memory, read a ROM file into it at 0x200, and prove the bytes landed.

Skeleton (C; translates 1:1 to any language) — you write the bodies:

```c
// chip8.h
#include <stdint.h>
#include <stddef.h>

#define MEM_SIZE  4096
#define ROM_START 0x200

typedef struct {
    uint8_t  mem[MEM_SIZE];
    uint16_t pc;
} Chip8;

void   chip8_init(Chip8 *c);                       /* zero mem, pc = 0x200 */
size_t chip8_load_rom(Chip8 *c, const char *path); /* read file at 0x200, return byte count */
```

`main.c`: init, load `argv[1]`, print `pc` and the first 16 bytes at 0x200 in hex. You'll also need a ROM — public-domain ones only; the IBM logo ROM is the standard first target, and I'll fetch it into the workspace when we start.

Check:

```
$ cc -o chip8 main.c chip8.c && ./chip8 ibm.ch8
PC=0x200 loaded=<n>
00 e0 a2 2a 60 0c d0 14 ...
```

`<n>` must equal `wc -c < ibm.ch8`, and the hex dump must match `xxd -g1 ibm.ch8 | head` byte for byte (the IBM ROM's first instruction is 00E0, clear-screen). When it matches we log it in `PROGRESS.md` and move to fetch–decode–execute.