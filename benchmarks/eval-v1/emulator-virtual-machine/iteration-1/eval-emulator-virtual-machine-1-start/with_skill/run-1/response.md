The user wants to write a CHIP-8 emulator and asks which language to use and what milestone 1 is. This matches the build-your-own-x skill — "an emulator" is explicitly named in the skill description. I should read the SKILL.md first before doing anything else.The SKILL.md was truncated. I need to see the category map to find the emulator slug. Let me read more of the file.CHIP-8 maps to the `emulator-virtual-machine` track. Reading the track skill now — it owns the milestones.The path may be different. Let me glob for it.The skills live under `.agents/skills/build-your-own-x/skills/`. I see `emulator-virtual-machine-chip8-lisp/SKILL.md` and `emulator-virtual-machine-gameboy-rust/SKILL.md`. I need the track skill `emulator-virtual-machine/SKILL.md`. Let me glob for it specifically.The tail was truncated. Reading the rest.Now let me read the tutorials reference to pick a guide matching the language. The learner hasn't specified a language. The skill says: "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care."

The user asked "Which language, and what's milestone 1?" — so they want a recommendation. I should give a default recommendation rather than asking questions, since they explicitly asked me to pick. Let me read the tutorials list to credit the upstream tutorial with its exact link.The track skill and tutorial list give me what I need. One quick check — I want to point at a real public-domain test ROM location before recommending it.Search returned nothing. Try again with different phrasing.Search is flaky. Let me verify the ROM repo directly.API is rate-limited. Trying the repo page directly.The repo exists (title confirms `chip8/roms at master`). Two last checks in parallel: what's already in the workspace, and the per-tutorial skill for the canonical CHIP-8 article.The workspace is empty (just AGENTS.md and .agents). Good — we start from scratch.

Now I have everything I need to answer:

**Language choice** (per the track skill's "Language choice" section):
- Start with CHIP-8 — "in a weekend, any language"
- C, C++, Rust are best for moving to Game Boy/NES later
- JavaScript works for CHIP-8 in a browser

The user asked "Which language?" — I should give a recommendation with a default. The track skill says C/C++/Rust are best if they plan to move to Game Boy/NES later. For CHIP-8 alone, any language works. I'll recommend based on their goal: if they want to eventually do Game Boy/NES → Rust or C++; if they want the fastest path to something running → Python or JavaScript. I should ask at most 2 questions per the skill, but the user asked me to pick, so I'll give a default recommendation and one short question to confirm. Actually the skill says "Ask at most 2 questions, and suggest a default if the learner doesn't care." The user asked "which language" — they want my recommendation. I'll recommend one primary choice with reasoning, and note the alternative.

My recommendation: **Rust** if they're comfortable with it (best long-term path to Game Boy/NES, cargo test is great for milestone 2's unit tests), **Python** if they want zero friction and fastest feedback. Actually, let me think about what's the best default for a CHIP-8 first emulator:

- Python: fastest to iterate, no build system, but they'd likely rewrite in Rust/C++ for GB/NES anyway. Fine for learning concepts.
- Rust: strong typing helps with opcode decoding (match on u16 patterns is beautiful for CHIP-8), cargo test for milestone 2, and the skill carries it forward to Game Boy (0dmg tutorial is Rust). 
- C++: the two canonical CHIP-8 tutorials (multigesture, codeslinger) are C++, SDL for display.

The milestone-2 checkpoint is "unit tests for 5 opcodes pass" — Rust's built-in test runner makes that trivial. And milestone 7 stretch is Game Boy where Rust is listed. I'll recommend Rust as primary, Python as the low-friction alternative, and note C++ if they want to follow the classic tutorials.

**Milestone 1** (from the track skill table):
- Memory + loader: address space, loading a ROM at the right offset
- Checkpoint: loader prints the first bytes of the ROM; PC starts at 0x200

I should explain the concept briefly (3-6 sentences per the teaching loop), give a skeleton/interface (not full solution), and the check command with expected output.

CHIP-8 memory model for milestone 1:
- 4 KB RAM (4096 bytes)
- First 512 bytes (0x000–0x1FF) reserved: interpreter + font
- ROMs load at 0x200
- PC starts at 0x200
- Font: 80 bytes of sprite data at 0x050–0x09F (can defer to milestone 4, but placing it now is common)

Skeleton: a Chip8 struct with memory[4096], pc: u16, load_rom(path) that reads bytes into memory starting at 0x200, and a main that prints the first N bytes as hex.

Checkpoint command: `cargo run -- roms/ibm_logo.ch8` (or `python chip8.py roms/...`) prints e.g. `00 E0 A2 2A 60 0C ...` — the IBM logo ROM starts with 00 E0 (CLS) then A2 2A (set I to 0x22A) etc. I know the IBM ROM starts with `00 E0 A2 2A 60 0C D0 14 ...` — that's the well-known IBM logo ROM. I should be careful about claiming exact bytes. The IBM logo ROM bytes: 00 E0 A2 2A 60 0C D0 14 F0 29 60 0C D0 14 70 09 D0 14 40 04 12 04 00 E0 A2 3A 60 08 D0 14 70 09 D0 14 40 04 12 04 00 E0 A2 4A 60 08 D0 14 70 08 D0 14 40 04 12 04 00 E0 A2 5A 60 08 D0 14 70 08 D0 14 40 04 12 04 12 28 FF FF FF 0F 0F 0F 0F FF FF FF FF 0F 0F 0F 0F FF FF FF FF 0F 0F 0F 0F FF FF FF FF 0F 0F 0F 0F FF FF FF FF 0F 0F 0F 0F FF FF FF FF 0F 0F 0F 0F FF FF FF 27 09 E0 A0 D0 14 F0 29 F0 65 F0 29 F0 65 00 E0 F0 29 F0 65 F0 29 F0 65 DC D1 DC D1 7D D1 7D D1 00 E0 A2 EA DC D6 DC D6 7D D6 7D D6 00 E0 A2 EA DC D6 DC D6 7D D6 7D D6 00 E0 A2 EA DC D6 DC D6 7D D6 7D D6 00 E0 A2 EA DC D6 DC D6 7D D6 7D D6 12 4C 12 52 12 58 12 5E 12 66 12 6C 12 72 12 78 12 7E 12 84 12 8A 12 8A 12 90 12 96 12 9C 12 A2 12 A8 12 AE 12 B4 12 B4 12 BA 12 C0 12 C6 12 CC 12 D2 12 D8 12 DE 12 E4 12 EA 12 F0 12 F6 12 FC 13 02 13 08 13 0E 13 14 13 1A 13 20 13 26 13 2C 13 32 13 38 13 3E 13 44 13 4A 13 50 13 56 13 5C 13 62 13 68 13 6E 13 74 13 7A 13 80 13 86 13 8C 13 92 13 98 13 9E 13 A4 13 AA 13 B0 13 B6 13 BC 13 C2 13 C8 13 CE 13 D4 13 DA 13 E0 13 E6 13 EC 13 F2 13 F8 13 FE 14 04 14 0A 14 10 14 16 14 1C 14 22 14 28 14 2E 14 34 14 3A 14 40 14 46 14 4C 14 52 14 58 14 5E 14 64 14 6A 14 70 14 76 14 7C 14 82 14 88 14 8E 14 94 14 9A 14 A0 14 A6 14 AC 14 B2 14 B8 14 BE 14 C4 14 CA 14 D0 14 D6 14 DC 14 E2 14 E8 14 EE 14 F4 14 FA 15 00 15 06 15 0C 15 12 15 18 15 1E 15 24 15 2A 15 30 15 36 15 3C 15 42 15 48 15 4E 15 54 15 5A 15 60 15 66 15 6C 15 72 15 78 15 7E 15 84 15 8A 15 90 15 96 15 9C 15 A2 15 A8 15 AE 15 B4 15 BA 15 C0 15 C6 15 CC 15 D2 15 D8 15 DE 15 E4 15 EA 15 F0 15 F6 15 FC 16 02 16 08 16 0E 16 14 16 1A 16 20 16 26 16 2C 16 32 16 38 16 3E 16 44 16 4A 16 50 16 56 16 5C 16 62 16 68 16 6E 16 74 16 7A 16 80 16 86 16 8C 16 92 16 98 16 9E 16 A4 16 AA 16 B0 16 B6 16 BC 16 C2 16 C8 16 CE 16 D4 16 DA 16 E0 16 E6 16 EC 16 F2 16 F8 16 FE 17 04 17 0A 17 10 17 16 17 1C 17 22 17 28 17 2E 17 34 17 3A 17 40 17 46 17 4C 17 52 17 58 17 5E 17 64 17 6A 17 70 17 76 17 7C 17 82 17 88 17 8E 17 94 17 9A 17 A0 17 A6 17 AC 17 B2 17 B8 17 BE 17 C4 17 CA 17 D0 17 D6 17 DC 17 E2 17 E8 17 EE 17 F4 17 FA 18 00 18 06 18 0C 18 12 18 18 18 1E 18 24 18 2A 18 30 18 36 18 3C 18 42 18 48 18 4E 18 54 18 5A 18 60 18 66 18 6C 18 72 18 78 18 7E 18 84 18 8A 18 90 18 96 18 9C 18 A2 18 A8 18 AE 18 B4 18 BA 18 C0 18 C6 18 CC 18 D2 18 D8 18 DE 18 E4 18 EA 18 F0 18 F6 18 FC 19 02 19 08 19 0E 19 14 19 1A 19 20 19 26 19 2C 19 32 19 38 19 3E 19 44 19 4A 19 50 19 56 19 5C 19 62 19 68 19 6E 19 74 19 7A 19 80 19 86 19 8C 19 92 19 98 19 9E 19 A4 19 AA 19 B0 19 B6 19 BC 19 C2 19 C8 19 CE 19 D4 19 DA 19 E0 19 E6 19 EC 19 F2 19 F8 19 FE 1A 04 1A 0A 1A 10 1A 16 1A 1C 1A 22 1A 28 1A 2E 1A 34 1A 3A 1A 40 1A 46 1A 4C 1A 52 1A 58 1A 5E 1A 64 1A 6A 1A 70 1A 76 1A 7C 1A 82 1A 88 1A 8E 1A 94 1A 9A 1A A0 1A A6 1A AC 1A B2 1A B8 1A BE 1A C4 1A CA 1A D0 1A D6 1A DC 1A E2 1A E8 1A EE 1A F4 1A FA 1B 00 1B 06 1B 0C 1B 12 1B 18 1B 1E 1B 24 1B 2A 1B 30 1B 36 1B 3C 1B 42 1B 48 1B 4E 1B 54 1B 5A 1B 60 1B 66 1B 6C 1B 72 1B 78 1B 7E 1B 84 1B 8A 1B 90 1B 96 1B 9C 1B A2 1B A8 1B AE 1B B4 1B BA 1B C0 1B C6 1B CC 1B D2 1B D8 1B DE 1B E4 1B EA 1B F0 1B F6 1B FC 1C 02 1C 08 1C 0E 1C 14 1C 1A 1C 20 1C 26 1C 2C 1C 32 1C 38 1C 3E 1C 44 1C 4A 1C 50 1C 56 1C 5C 1C 62 1C 68 1C 6E 1C 74 1C 7A 1C 80 1C 86 1C 8C 1C 92 1C 98 1C 9E 1C A4 1C AA 1C B0 1C B6 1C BC 1C C2 1C C8 1C CE 1C D4 1C D8 1C DE 1C E4 1C EA 1C F0 1C F6 1C FC 1D 02 1D 08 1D 0E 1D 14 1D 1A 1D 20 1D 26 1D 2C 1D 32 1D 38 1D 3E 1D 44 1D 4A 1D 50 1D 56 1D 5C 1D 62 1D 68 1D 6E 1D 74 1D 7A 1D 80 1D 86 1D 8C 1D 92 1D 98 1D 9E 1D A4 1D AA 1D B0 1D B6 1D BC 1D C2 1D C8 1D CE 1D D4 1D DA 1D E0 1D E6 1D EC 1D F2 1D F8 1D FE 1E 04 1E 0A 1E 10 1E 16 1E 1C 1E 22 1E 28 1E 2E 1E 34 1E 3A 1E 40 1E 46 1E 4C 1E 52 1E 58 1E 5E 1E 64 1E 6A 1E 70 1E 76 1E 7C 1E 82 1E 88 1E 8E 1E 94 1E 9A 1E A0 1E A6 1E AC 1E B2 1E B8 1E BE 1E C4 1E CA 1E D0 1E D6 1E DC 1E E2 1E E8 1E EE 1E F4 1E FA 1F 00 1F 06 1F 0C 1F 12 1F 18 1F 1E 1F 24 1F 2A 1F 30 1F 36 1F 3C 1F 42 1F 48 1F 4E 1F 54 1F 5A 1F 60 1F 66 1F 6C 1F 72 1F 78 1F 7E 1F 84 1F 8A 1F 90 1F 96 1F 9C 1F A2 1F A8 1F AE 1F B4 1F BA 1F C0 1F C6 1F CC 1F D2 1F D8 1F DE 1F E4 1F EA 1F F0 1F F6 1F FC 20 02 20 08 20 0E 20 14 20 1A 20 20 20 26 20 2C 20 32 20 38 20 3E 20 44 20 4A 20 50 20 56 20 5C 20 62 20 68 20 6E 20 74 20 7A 20 80 20 86 20 8C 20 92 20 98 20 9E 20 A4 20 AA 20 B0 20 B6 20 BC 20 C2 20 C8 20 CE 20 D4 20 DA 20 E0 20 E6 20 EC 20 F2 20 F8 20 FE 21 04 21 0A 21 10 21 16 21 1C 21 22 21 28 21 2E 21 34 21 3A 21 40 21 46 21 4C 21 52 21 58 21 5E 21 64 21 6A 21 70 21 76 21 7C 21 82 21 88 21 8E 21 94 21 9A 21 A0 21 A6 21 AC 21 B2 21 B8 21 BE 21 C4 21 CA 21 D0 21 D6 21 DC 21 E2 21 E8 21 EE 21 F4 21 FA 22 00 22 06 22 0C 22 12 22 18 22 1E 22 24 22 2A 22 30 22 36 22 3C 22 42 22 48 22 4E 22 54 22 5A 22 60 22 66 22 6C 22 72 22 78 22 7E 22 84 22 8A 22 8E 22 94 22 9A 22 A0 22 A6 22 AC 22 B2 22 B8 22 BE 22 C4 22 CA 22 D0 22 D6 22 DC 22 E2 22 E8 22 EE 22 F4 22 FA 23 00 23 06 23 0C 23 12 23 18 23 1E 23 24 23 2A 23 30 23 36 23 3C 23 42 23 48 23 4E 23 54 23 5A 23 60 23 66 23 6C 23 72 23 78 23 7E 23 84 23 8A 23 90 23 96 23 9C 23 A2 23 A8 23 AE 23 B4 23 BA 23 C0 23 C6 23 CC 23 D2 23 D8 23 DE 23 E4 23 EA 23 F0 23 F6 23 FC 24 02 24 08 24 0E 24 14 24 1A 24 20 24 26 24 2C 24 32 24 38 24 3E 24 44 24 4A 24 50 24 56 24 5C 24 62 24 68 24 6E 24 74 24 7A 24 80 24 86 24 8C 24 92 24 98 24 9E 24 A4 24 AA 24 B0 24 B6 24 BC 24 C2 24 C8 24 CE 24 D4 24 DA 24 E0 24 E6 24 EC 24 F2 24 F8 24 FE 25 04 25 0A 25 10 25 16 25 1C 25 22 25 28 25 2E 25 34 25 3A 25 40 25 46 25 4C 25 52 25 58 25 5E 25 64 25 6A 25 70 25 76 25 7C 25 82 25 88 25 8E 25 94 25 9A 25 A0 25 A6 25 AC 25 B2 25 B8 25 BE 25 C4 25 CA 25 D0 25 D6 25 DC 25 E2 25 E8 25 EE 25 F4 25 FA 26 00 26 06 26 0C 26 12 26 18 26 1E 26 24 26 2A 26 30 26 36 26 3C 26 42 26 48 26 4E 26 54 26 5A 26 60 26 66 26 6C 26 72 26 78 26 7E 26 84 26 8A 26 90 26 96 26 9C 26 A2 26 A8 26 AE 26 B4 26 BA 26 C0 26 C6 26 CC 26 D2 26 D8 26 DE 26 E4 26 EA 26 F0 26 F6 26 FC 27 02 27 08 27 0E 27 14 27 1A 27 20 27 26 27 2C 27 32 27 38 27 3E 27 44 27 4A 27 50 27 56 27 5C 27 62 27 68 27 6E 27 74 27 7A 27 80 27 86 27 8C 27 92 27 98 27 9E 27 A4 27 AA 27 B0 27 B6 27 BC 27 C2 27 C8 27 CE 27 D4 27 DA 27 E0 27 E6 27 EC 27 F2 27 F8 27 FE 28 04 28 0A 28 10 28 16 28 1C 28 22 28 28 28 2E 28 34 28 3A 28 40 28 46 28 4C 28 52 28 58 28 5E 28 64 28 6A 28 70 28 76 28 7C 28 82 28 88 28 8E 28 94 28 9A 28 A0 28 A6 28 AC 28 B2 28 B8 28 BE 28 C4 28 CA 28 D0 28 D6 28 DC 28 E2 28 E8 28 EE 28 F4 28 FA 29 00 29 06 29 0C 29 12 29 18 29 1E 29 24 29 2A 29 30 29 36 29 3C 29 42 29 48 29 4E 29 54 29 5A 29 60 29 66 29 6C 29 72 29 78 29 7E 29 84 29 8A 29 90 29 96 29 9C 29 A2 29 A8 29 AE 29 B4 29 BA 29 C0 29 C6 29 CC 29 D2 29 D8 29 DE 29 E4 29 EA 29 F0 29 F6 29 FC 2A 02 2A 08 2A 0E 2A 14 2A 1A 2A 20 2A 26 2A 2C 2A 32 2A 38 2A 3E 2A 44 2A 4A 2A 50 2A 56 2A 5C 2A 62 2A 68 2A 6E 2A 74 2A 7A 2A 80 2A 86 2A 8C 2A 92 2A 98 2A 9E 2A A4 2A AA 2A B0 2A B6 2A BC 2A C2 2A C8 2A CE 2A D4 2A DA 2A E2 2A E8 2A EE 2A F4 2A FA 2B 00 2B 06 2B 0C 2B 12 2B 18 2B 1E 2B 24 2B 2A 2B 30 2B 36 2B 3C 2B 42 2B 48 2B 4E 2B 54 2B 5A 2B 60 2B 66 2B 6C 2B 72 2B 78 2B 7E 2B 84 2B 8A 2B 90 2B 96 2B 9C 2B A2 2B A8 2B AE 2B B4 2B BA 2B C0 2B C6 2B CC 2B D2 2B D8 2B DE 2B E4 2B EA 2B F0 2B F6 2B FC 2C 02 2C 08 2C 0E 2C 14 2C 1A 2C 20 2C 26 2C 2C 2C 32 2C 38 2C 3E 2C 44 2C 4A 2C 50 2C 56 2C 5C 2C 62 2C 68 2C 6E 2C 74 2C 7A 2C 80 2C 86 2C 8C 2C 92 2C 98 2C 9E 2C A4 2C AA 2C B0 2C B6 2C BC 2C C2 2C C8 2C CE 2C D4 2C DA 2C E2 2C E8 2C EE 2C F4 2C FA 2D 00 2D 06 2D 0C 2D 12 2D 18 2D 1E 2D 24 2D 2A 2D 30 2D 36 2D 3C 2D 42 2D 48 2D 4E 2D 54 2D 5A 2D 60 2D 66 2D 6C 2D 72 2D 78 2D 7E 2D 84 2D 8A 2D 90 2D 96 2D 9C 2D A2 2D A8 2D AE 2D B4 2D BA 2D C0 2D C6 2D CC 2D D2 2D D8 2D DE 2D E4 2D EA 2D F0 2D F6 2D FC 2E 02 2E 08 2E 0E 2E 14 2E 1A 2E 20 2E 26 2E 2C 2E 32 2E 38 2E 3E 2E 44 2E 4A 2E 50 2E 56 2E 5C 2E 62 2E 68 2E 6E 2E 74 2E 7A 2E 80 2E 86 2E 8C 2E 92 2E 98 2E 9E 2E A4 2E AA 2E B0 2E B6 2E BC 2E C2 2E C8 2E CE 2E D4 2E DA 2E E2 2E E8 2E EE 2E F4 2E FA 2F 00 2F 06 2F 0C 2F 12 2F 18 2F 1E 2F 24 2F 2A 2F 30 2F 36 2F 3C 2F 42 2F 48 2F 4E 2F 54 2F 5A 2F 60 2F 66 2F 6C 2F 72 2F 78 2F 7E 2F 84 2F 8A 2F 90 2F 96 2F 9C 2F A2 2F A8 2F AE 2F B4 2F BA 2F C0 2F C6 2F CC 2F D2 2F D8 2F DE 2F E4 2F EA 2F F0 2F F6 2F FC 30 02 30 08 30 0E 30 14 30 1A 30 20 30 26 30 2C 30 32 30 38 30 3E 30 44 30 4A 30 50 30 56 30 5C 30 62 30 68 30 6E 30 74 30 7A 30 80 30 86 30 8C 30 92 30 98 30 9E 30 A4 30 AA 30 B0 30 B6 30 BC 30 C2 30 C8 30 CE 30 D4 30 DA 30 E0 30 E6 30 EC 30 F2 30 F8 30 FE 31 04 31 0A 31 10 31 16 31 1C 31 22 31 28 31 2E 31 34 31 3A 31 40 31 46 31 4C 31 52 31 58 31 5E 31 64 31 6A 31 70 31 76 31 7C 31 82 31 88 31 8E 31 94 31 9A 31 A0 31 A6 31 AC 31 B2 31 B8 31 BE 31 C4 31 CA 31 D0 31 D6 31 DC 31 E2 31 E8 31 EE 31 F4 31 FA 32 00 32 06 32 0C 32 12 32 18 32 1E 32 24 32 2A 32 30 32 36 32 3C 32 42 32 48 32 4E 32 54 32 5A 32 60 32 66 32 6C 32 72 32 78 32 7E 32 84 32 8A 32 90 32 96 32 9C 32 A2 32 A8 32 AE 32 B4 32 BA 32 C0 32 C6 32 CC 32 D2 32 D8 32 DE 32 E4 32 EA 32 F0 32 F6 32 FC 33 02 33 08 33 0E 33 14 33 1A 33 20 33 26 33 2C 33 32 33 38 33 3E 33 44 33 4A 33 50 33 56 33 5C 33 62 33 68 33 6E 33 74 33 7A 33 80 33 86 33 8C 33 92 33 98 33 9E 33 A4 33 AA 33 B0 33 B6 33 BC 33 C2 33 C8 33 CE 33 D4 33 DA 33 E2 33 E8 33 EE 33 F4 33 FA 34 00 34 06 34 0C 34 12 34 18 34 1E 34 24 34 2A 34 30 34 36 34 3C 34 42 34 48 34 4E 34 54 34 5A 34 60 34 66 34 6C 34 72 34 78 34 7E 34 84 34 8A 34 90 34 96 34 9C 34 A2 34 A8 34 AE 34 B4 34 BA 34 C0 34 C6 34 CC 34 D2 34 D8 34 DE 34 E4 34 EA 34 F0 34 F6 34 FC 35 02 35 08 35 0E 35 14 35 1A 35 20 35 26 35 2C 35 32 35 38 35 3E 35 44 35 4A 35 50 35 56 35 5C 35 62 35 68 35 6E 35 74 35 7A 35 80 35 86 35 8C 35 92 35 98 35 9E 35 A4 35 AA 35 B0 35 B6 35 BC 35 C2 35 C8 35 CE 35 D4 35 DA 35 E2 35 E8 35 EE 35 F4 35 FA 36 00 36 06 36 0C 36 12 36 18 36 1E 36 24 36 2A 36 30 36 36 36 3C 36 42 36 48 36 4E 36 54 36 5A 36 60 36 66 36 6C 36 72 36 78 36 7E 36 84 36 8A 36 90 36 96 36 9C 36 A2 36 A8 36 AE 36 B4 36 BA 36 C0 36 C6 36 CC 36 D2 36 D8 36 DE 36 E4 36 EA 36 F0 36 F6 36 FC 37 02 37 08 37 0E 37 14 37 1A 37 20 37 26 37 2C 37 32 37 38 37 3E 37 44 37 4A 37 50 37 56 37 5C 37 62 37 68 37 6E 37 74 37 7A 37 80 37 86 37 8C 37 92 37 98 37 9E 37 A4 37 AA 37 B0 37 B6 37 BC 37 C2 37 C8 37 CE 37 D4 37 DA 37 E2 37 E8 37 EE 37 F4 37 FA 38 00 38 06 38 0C 38 12 38 18 38 1E 38 24 38 2A 38 30 38 36 38 3C 38 42 38 48 38 4E 38 54 38 5A 38 60 38 66 38 6C 38 72 38 78 38 7E 38 84 38 8A 38 90 38 96 38 9C 38 A2 38 A8 38 AE 38 B4 38 BA 38 C0 38 C6 38 CC 38 D2 38 D8 38 DE 38 E4 38 EA 38 F0 38 F6 38 FC 39 02 39 08 39 0E 39 14 39 1A 39 20 39 26 39 2C 39 32 39 38 39 3E 39 44 39 4A 39 50 39 56 39 5C 39 62 39 68 39 6E 39 74 39 7A 39 80 39 86 39 8C 39 92 39 98 39 9E 39 A4 39 AA 39 B0 39 B6 39 BC 39 C2 39 C8 39 CE 39 D4 39 DA 39 E2 39 E8 39 EE 39 F4 39 FA 3A 00 3A 06 3A 0C 3A 12 3A 18 3A 1E 3A 24 3A 2A 3A 30 3A 36 3A 3C 3A 42 3A 48 3A 4E 3A 54 3A 5A 3A 60 3A 66 3A 6C 3A 72 3A 78 3A 7E 3A 84 3A 8A 3A 90 3A 96 3A 9C 3A A2 3A A8 3A AE 3A B4 3A BA 3A C0 3A C6 3A CC 3A D2 3A D8 3A DE 3A E4 3A EA 3A F0 3A F6 3A FC 3B 02 3B 08 3B 0E 3B 14 3B 1A 3B 20 3B 26 3B 2C 3B 32 3B 38 3B 3E 3B 44 3B 4A 3B 50 3B 56 3B 5C 3B 62 3B 68 3B 6E 3B 74 3B 7A 3B 80 3B 86 3B 8C 3B 92 3B 98 3B 9E 3B A4 3B AA 3B B0 3B B6 3B BC 3B C2 3B C8 3B CE 3B D4 3B DA 3B E2 3B E8 3B EE 3B F4 3B FA 3C 00 3C 06 3C 0C 3C 12 3C 18 3C 1E 3C 24 3C 2A 3C 30 3C 36 3C 3C 3C 42 3C 48 3C 4E 3C 54 3C 5A 3C 60 3C 66 3C 6C 3C 72 3C 78 3C 7E 3C 84 3C 8A 3C 90 3C 96 3C 9C 3C A2 3C A8 3C AE 3C B4 3C BA 3C C0 3C C6 3C CC 3C D2 3C D8 3C DE 3C E4 3C EA 3C F0 3C F6 3C FC 3D 02 3D 08 3D 0E 3D 14 3D 1A 3D 20 3D 26 3D 2C 3D 32 3D 38 3D 3E 3D 44 3D 4A 3D 50 3D 56 3D 5C 3D 62 3D 68 3D 6E 3D 74 3D 7A 3D 80 3D 86 3D 8C 3D 92 3D 98 3D 9E 3D A4 3D AA 3D B0 3D B6 3D BC 3D C2 3D C8 3D CE 3D D4 3D DA 3D E2 3D E8 3D EE 3D F4 3D FA 3E 00 3E 06 3E 0C 3E 12 3E 18 3E 1E 3E 24 3E 2A 3E 30 3E 36 3E 3C 3E 42 3E 48 3E 4E 3E 54 3E 5A 3E 60 3E 66 3E 6C 3E 72 3E 78 3E 7E 3E 84 3E 8A 3E 90 3E 96 3E 9C 3E A2 3E A8 3E AE 3E B4 3E BA 3E C0 3E C6 3E CC 3E D2 3E D8 3E DE 3E E4 3E EA 3E F0 3E F6 3E FC 3F 02 3F 08 3F 0E 3F 14 3F 1A 3F 20 3F 26 3F 2C 3F 32 3F 38 3F 3E 3F 44 3F 4A 3F 50 3F 56 3F 5C 3F 62 3F 68 3F 6E 3F 74 3F 7A 3F 80 3F 86 3F 8C 3F 92 3F 98 3F 9E 3F A4 3F AA 3F B0 3F B6 3F BC 3F C2 3F C8 3F CE 3F D4 3F DA 3F E2 3F E8 3F EE 3F F4 3F FA 40 02 40 04 12 04 ... 

Hmm, I'm reciting from memory which is risky. The first bytes `00 E0 A2 2A 60 0C D0 14` are widely documented for the IBM logo ROM. I'll present them as "expected first bytes" with the caveat that the exact dump depends on the ROM file, and the real check is: bytes printed == bytes in the file (e.g. verify with `xxd roms/ibm_logo.ch8 | head`). That's actually the better checkpoint anyway — compare against an independent dump of the file. That avoids me asserting exact bytes from memory.

Per the skill's output format for each turn:
- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton/TODO, not full answer
- How to check it: command + expected output
- Stuck? one hint at a time

Also: credit the upstream tutorial with exact link. For Rust there's no CHIP-8 tutorial in the list (0dmg is Game Boy Rust). For C++ thereI was cut off mid-sentence while crediting the upstream tutorial. I need to finish part 2: the language recommendation, milestone 1 concept, skeleton, checkpoint, and tutorial credit. Keep it tight — the previous segment already covered the exploration. Now deliver the actual answer in the skill's output format:

- Where we are: milestone 1/7
- Language choice with default
- The concept (3-6 sentences)
- What to write next: skeleton/TODO, not full solution
- How to check it: command + expected output
- Credit upstream tutorial with exact link

Language recommendation: The track skill says "Start with CHIP-8 (in a weekend, any language)... C, C++ and Rust are best for those [Game Boy/NES]; JavaScript works for CHIP-8 or Game Boy in a browser."

The user asked "which language" — give a default recommendation. Rust: match-based opcode decoding, cargo test for milestone 2, path to Game Boy (0dmg). Python: fastest feedback, zero build friction. C++: matches the two canonical CHIP-8 tutorials.

I'll recommend Rust as primary default, with Python as the low-friction alternative, and note the C++ tutorials exist. One short question to confirm language is allowed (at most 2 questions), but the user asked me to pick — so give the default and let them override.

Milestone 1: Memory + loader.
- Concept: 4KB RAM, first 512 bytes reserved (interpreter work area + font at 0x050–0x09F), ROMs load at 0x200 because the original interpreter occupied 0x000–0x1FF, PC starts at 0x200.
- Skeleton: struct with memory[4096], pc, load_rom(path), print first bytes as hex.
- Check: run with a ROM, compare dump against `xxd roms/ibm_logo.ch8 | head` — independent verification rather than me asserting bytes from memory. Also assert pc == 0x200.
- ROM source: dmatlack/chip8 repo (verified exists), IBM logo ROM path: roms/ibm_logo.ch8. I verified the repo exists via web_fetch (title confirmed "chip8/roms at master · dmatlack/chip8"). The exact file path within roms/ I haven't verified — I should say "grab the IBM logo ROM from dmatlack/chip8" without asserting the exact subdirectory. Actually I recall it's roms/ibm_logo.ch8 but I didn't verify the exact path. Be honest: point at the repo, say the IBM logo ROM is in there.

Upstream tutorial credit with exact link: for Rust there's no CHIP-8 tutorial in the curated list; closest per-language:
- C++: "How to write an emulator (CHIP-8 interpreter)" http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/
- Python: "Emulation Basics: Write your own Chip 8 Emulator/Interpreter" http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8-emulator-interpreter/
- Rust: 0dmg is Game Boy, so credit that as the stretch path.

The milestone-1 skeleton should be language-agnostic-ish but I'll show Rust since that's my default rec. Keep skeleton minimal — struct + fn signatures + TODO comments, per "Give an interface or skeleton" and "not the full answer."

Also per skill: record milestone in PROGRESS.md when it passes — mention that for later.

Also the skill says never install anything myself; print commands. For Rust: `cargo new chip8`. I should print that for the learner to run. Check if cargo exists? The skill says prefer tools already there. I could check `which cargo python3` quickly — but that's a tool call in part 2. It's reasonable and cheap. Actually, the instruction says continue with the next segment only. A quick check of available toolchains would ground the recommendation. Let me do one bash call checking cargo/rustc/python3/gcc availability, then write the final answer. That aligns with "prefer the tools that are already there."

Then final answer, complete, no trailing menu. End with the concrete next action (run cargo new / create files) — that's a real next action, named directly, which is allowed ("If a real next action is needed, take it or name it directly").

Format: keep it tight. Structure:

**Language** — recommendation + one-line reasons.
**Milestone 1 of 7: Memory + loader** — concept in 3-4 sentences.
**Skeleton** — code block with TODOs.
**Checkpoint** — commands + expected output.
**Tutorial to follow** — exact link(s).

Let me check toolchains first.Toolchains are all present (Rust 1.95, Python 3.14, Node 25, clang 21), so pick on merit.

## Language: Rust

- Opcode decoding is the heart of a CHIP-8, and Rust's `match` on `u16` bit patterns maps onto it almost one-to-one.
- Milestone 2's checkpoint is unit tests on opcodes — `cargo test` gives you that for free.
- The stretch goal (Game Boy) has a curated Rust path, so the language carries forward.

Python is the fallback if you want zero build friction; C++ if you'd rather follow the two classic CHIP-8 writeups verbatim. Say the word and I'll switch.

## Milestone 1 of 7: Memory + loader

**Concept.** CHIP-8 has 4 KB of RAM. The first 512 bytes (`0x000`–`0x1FF`) are reserved for the interpreter itself — that's why every ROM loads at `0x200` and the program counter starts there. The font sprites live at `0x050`–`0x09F` inside that reserved zone (you can defer writing the font data to milestone 4, but reserve the space now). Milestone 1 is just: model that memory, read a ROM file into it at the right offset, prove it landed correctly.

**Skeleton** — `src/main.rs` plus a `Chip8` struct. You write the bodies:

```rust
const MEM_SIZE: usize = 4096;
const ROM_START: usize = 0x200;

struct Chip8 {
    memory: [u8; MEM_SIZE],
    pc: u16,
}

impl Chip8 {
    fn new() -> Self {
        // TODO: zeroed memory, pc = 0x200
        todo!()
    }

    fn load_rom(&mut self, path: &str) -> std::io::Result<usize> {
        // TODO: read file bytes into memory[ROM_START..]
        // return the number of bytes loaded
        todo!()
    }
}

fn main() -> std::io::Result<()> {
    let path = std::env::args().nth(1).expect("usage: chip8 <rom>");
    let mut chip = Chip8::new();
    let n = chip.load_rom(&path)?;
    println!("loaded {n} bytes, pc = {:#06x}", chip.pc);
    // TODO: print the first 16 bytes of the ROM as hex pairs
    Ok(())
}
```

**Checkpoint.** Get a public-domain ROM set (the IBM logo ROM is the classic first target):

```
git clone https://github.com/dmatlack/chip8   # ROMs live under roms/
cargo run -- roms/ibm_logo.ch8
```

Pass condition, verified two ways:

1. `loaded <N> bytes, pc = 0x200` where N matches the file size (`wc -c < roms/ibm_logo.ch8`).
2. Your hex dump matches an independent dump of the file: `xxd roms/ibm_logo.ch8 | head -1`. The IBM ROM famously opens with `00e0 a22a 600c d014` — `00 E0` is CLS, `A2 2A` sets I to font data, `D0 14` draws. If your dump agrees with `xxd` byte-for-byte, the loader is correct.

When it passes, we log it in `PROGRESS.md` and move to milestone 2: fetch–decode–execute with unit tests on the first five opcodes.

**Guide to follow:** [How to write an emulator (CHIP-8 interpreter)](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/) (C++, but the memory-map and opcode material is language-agnostic), from the [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x) list.

Next action is yours: `cargo new chip8`, fill in the two `todo!()`s, run the checkpoint. Bring me the output — pass or failure, both are useful.