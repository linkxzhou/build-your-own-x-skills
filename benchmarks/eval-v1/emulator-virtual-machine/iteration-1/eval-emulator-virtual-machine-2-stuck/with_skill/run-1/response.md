The user is speaking Chinese. They have a CHIP-8 emulator, running the IBM logo ROM shows garbled pixels, and they mention their DXYN draw instruction uses direct pixel assignment (直接赋值像素).

This is a debugging question about CHIP-8 emulator. The classic issue: DXYN should XOR pixels into the framebuffer, not assign/set them. If you use direct assignment (setting pixel to 1), sprites won't erase themselves and collision detection breaks, causing garbled display.

Also other common causes:
1. Using assignment instead of XOR — sprite drawing must XOR with existing pixels, and set VF=1 when a pixel is erased.
2. Coordinate wrapping — x % 64, y % 32 (or clipping).
3. Bit order — MSB first.
4. Memory loading offset — ROM should be loaded at 0x200.
5. Font set at 0x50, I register etc.

The IBM logo ROM is a well-known test. The typical symptom of "garbled pixels" with direct assignment: since DXYN draws a sprite by setting pixels to 1 instead of XOR, the sprite never erases, and the screen fills up. Actually for IBM logo, the ROM draws the logo by drawing sprites; with assignment, overlapping draws would just fill, but the IBM logo might still look somewhat recognizable... Actually the classic garbled result comes from XOR vs assignment issues combined with VF collision flag — the IBM logo ROM uses collision detection? Hmm.

Let me think about what the IBM logo ROM does. The IBM logo ROM (from the CHIP-8 documentation, "IBM Logo.ch8") displays "IBM" using sprites. It's a simple program that draws sprites at various positions. If DXYN uses direct assignment (pixel = 1), the logo would still appear mostly correct for a single pass... unless the ROM relies on XOR to erase parts. Actually the IBM logo ROM draws each letter as a series of 8x? sprites. Hmm, but the classic garbled output happens when:

- The display is drawn with wrong scaling or the framebuffer indexing is wrong (y*64 + x vs x*32+y).
- The sprite data bit order reversed.
- VF register clobbered by draw (some people set VF incorrectly, or the draw routine overwrites registers).
- Not wrapping coordinates.

Actually, a very common cause of garbled IBM logo: the emulator's DXYN sets pixels rather than XORing, AND the ROM draws the same sprite multiple times with offsets to create the logo — with assignment, overlapping regions become solid, producing a blob. The IBM logo is drawn with many overlapping sprite draws? Let me recall the IBM logo ROM disassembly:

The IBM logo ROM is 134 bytes. It draws the IBM logo using 8x10 sprites? Actually it uses DXYN with N up to 10? No — CHIP-8 DXYN max N is 15. The IBM logo uses sprites of height 10? Hmm, I recall the IBM logo ROM draws letters using multiple draws.

Regardless, the primary fix: DXYN must XOR pixels and set VF when erasing. Also ensure pixel coordinates wrap modulo 64/32.

The user's message is short: "我的 CHIP-8 模拟器跑 IBM logo 只出现乱码像素，绘制指令 DXYN 我用的是直接赋值像素。" — "My CHIP-8 emulator running IBM logo only shows garbled pixels; for the draw instruction DXYN I used direct pixel assignment."

So they've already identified their DXYN uses assignment. The answer: that's the bug — DXYN must be XOR-based with VF collision flag. Explain the semantics:

DXYN:
- Read N bytes starting at I.
- For each byte (row), for each bit (col, MSB first):
  - pixel position: (VX + col) % 64, (VY + row) % 32
  - if sprite bit is 1:
    - if screen pixel is already 1, set VF = 1
    - screen pixel ^= 1
- Drawing is done even when VF gets set.

Why assignment breaks: XOR makes sprites self-erasing and lets ROMs do flicker/erase; with assignment, any sprite drawn over existing pixels can't erase them, and VF collision detection (used by ROMs for logic) never triggers correctly... wait, with assignment you could still detect collision if you check before assigning. But the visible garbling: the IBM logo ROM actually draws the logo, then... hmm, does it? The IBM logo ROM just draws and halts (it has an infinite loop / waits). Actually the IBM logo ROM: it draws the IBM logo and then loops forever (jump to self). So with assignment, the logo should still appear... unless the ROM draws each letter with overlapping sprites where XOR matters.

Let me recall the actual IBM logo ROM behavior. From chip8 test suites discussions: "IBM Logo" ROM displays the IBM logo. The ROM draws sprites at various coordinates. I believe the logo is composed of multiple sprite draws that overlap? If they overlap with XOR, overlapping regions would cancel out — that would create holes, which would be wrong for a logo. So probably they don't overlap.

Hmm, so why garbled with assignment? Other common bugs that garble IBM logo:

1. Loading ROM at wrong offset (not 0x200) or PC starting at wrong place.
2. Framebuffer indexing transposed (display[y][x] vs display[x][y]) — produces garbled/sheared image.
3. Bit order LSB-first — mirrored letters.
4. Coordinate wrap missing — for IBM logo, coordinates are small so wrap rarely matters.
5. VF clobbering: if DXYN always sets VF=0/1 incorrectly and subsequent instructions depend... IBM logo probably doesn't check VF.
6. The 0x00E0 CLS not implemented — screen not cleared between draws; IBM logo draws once though.
7. Sprite height N misdecoded (e.g., using nibble extraction wrong).
8. I register handling wrong.
9. The draw loop iterating bits in wrong direction.

But the user specifically says they use direct assignment. The most likely visible effect: if the ROM draws the logo and the emulator's main loop redraws... Actually wait — many IBM logo ROM versions draw the logo repeatedly? No.

Hmm, actually let me reconsider: the famous IBM logo ROM (ibm-logo.ch8) — I recall its disassembly:

```
0x200: 00E0       CLS
0x202: A2 2A      I = 0x22A  (hmm)
...
```

Let me actually recall from the chip8 archive: IBM Logo.ch8 disassembly (from chip8.gulrak.net or similar):

```
00E0             ; clear
A22A             ; I = 0x22A
6001             ; V0 = 1
6101             ; V1 = 1
D015             ; draw at (0,1) height 5? 
...
```

I don't remember exactly. But there's a known fact: the IBM logo ROM draws the logo using multiple DXYN calls with N=10? No, N max 15, fine.

Actually I found in memory: IBM Logo disassembly:

```
0x200: 00E0  CLS
0x202: A22A  LD I, 0x22A
0x204: 6001  LD V0, 0x01
0x206: 6101  LD V1, 0x01
0x208: D015  DRW V0, V1, 5
0x20A: 7204  ADD V2, 0x04 ...
```

Not sure. The key point stands: the standard answer is XOR semantics.

But wait — with direct assignment, would IBM logo look garbled? If the ROM draws each letter as a single sprite (e.g., 8x10), assignment would render it identically to XOR on a blank screen. The logo would look fine. So garbled output suggests something else too — but the user says "只出现乱码像素" (only garbled pixels appear). Combined with assignment-based drawing, the classic garbling: the ROM may draw the logo by drawing overlapping sprites where XOR creates the letter shapes (e.g., drawing a filled block then XOR-erasing to carve letters). If the IBM logo ROM carves letters via XOR, assignment would produce solid blobs = garbled.

Actually yes! I now recall: the IBM logo ROM draws the logo using 8-wide sprites of height 10, and the letters are formed by multiple draws... Hmm.

Let me just check the actual ROM. I could fetch the IBM logo ROM bytes and disassemble. That would be rigorous. The ROM is widely available. I can search the web for "IBM Logo.ch8 hex bytes" — there's a known hex dump:

The IBM logo ROM hex (134 bytes):
```
00 E0 A2 2A 60 0C 61 08 D0 1F 70 04 A2 39 D0 1F
A2 48 70 08 D0 1F 70 04 A2 57 D0 1F 70 08 A2 66
D0 1F 70 04 A2 75 D0 1F 12 28 FF 00 FF 00 3C 00
3C 00 3C 00 3C 00 FF 00 FF 00 FF 80 FF 80 FF 80
FF 80 3F 80 3F 80 3F 80 3F 80 FF 80 FF 80 FF 80
FF 80 FF 00 FF 00 FF 00 3C 00 3C 00 3C 00 3C 00
FF 00 FF 00 FF 00 FF 00 FF 80 FF 80 FF 80 FF 80
3F 80 3F 80 3F 80 3F 80 FF 80 FF 80 FF 80 FF 80
FF 00 3C 00 3C 00 3C 00 3C 00 FF 00 FF 00
```

Hmm, something like that. The disassembly:

```
0200: 00E0  CLS
0202: A22A  I=0x22A
0204: 600C  V0=12
0206: 6108  V1=8
0208: D01F  draw V0,V1,15   ; wait, F=15 rows
020A: 7004  V0+=4
020C: A239  I=0x239
020E: D01F  draw
0210: A248  I=0x248
0212: 7008  V0+=8
0214: D01F  draw
...
```

So it draws 15-row sprites (8x15) side by side — the letters I, B, M each drawn as sprites, non-overlapping, at x=12,16,24,28,36,40? With V0 starting 12, +4, +8, +4, +8, +4 → x = 12,16,24,28,36,40. Six draws of 8x15 sprites. These are the vertical strokes and the B's bowls etc. They don't overlap.

On a blank screen with assignment, this would render the IBM logo correctly! So garbled output means something else is wrong — OR the user's emulator has other bugs. But hold on — the user says "只出现乱码像素" — maybe their whole screen shows noise, which suggests the framebuffer indexing or the ROM loading is broken, or their draw uses assignment AND their screen isn't cleared, or they draw garbage memory because I is wrong.

Hmm wait, but actually there's a subtlety: with direct assignment (pixel = sprite_bit ? 1 : pixel? or pixel = sprite_bit?), if they do `screen[y][x] = sprite_bit` (assigning 0 too), that's fine on blank screen. If they do `if sprite_bit: screen[y][x] = 1`, also fine on blank screen.

So why garbled? Possibilities:

1. They load the ROM at wrong address or PC starts wrong → executing data as code → garbage draws. But then nothing would look like anything.

2. Their DXYN implementation has a bug beyond assignment: e.g., bit iteration order, or they use `VX + col` without modulo and index out of bounds → wrapping to wrong rows (in C, buffer overflow → garbage). If they index `display[(VY+row)*64 + (VX+col)]` without bounds and the logo is at x=12..47, y=8..22 — within bounds. Fine.

3. Their opcode decoding is wrong: e.g., N extracted incorrectly.

4. Their main loop timing: drawing every cycle vs waiting for timers — IBM logo doesn't care.

5. The classic: they XOR... no they assign.

Hmm, actually wait. Let me reconsider the IBM logo ROM. There are two versions floating around: one that draws and loops forever (jump self), and the original that... The original IBM logo ROM from the "ROMs" folder in many repos: after drawing, it does `1228` (jump 0x228)? In my hex dump above, at 0x226 there's `12 28` = JP 0x228, and 0x228 might be `12 28` again (infinite loop) — the last two bytes "FF 00" hmm.

Actually the hex I recalled ends with "FF 00 FF 00" which is sprite data. The jump at 0x226: `12 28` jumps to 0x228 which is... 0x228 would be within data region? The data starts at 0x22A per `A22A`. So 0x228-0x229 is `12 28`? That would be jump-to-self at 0x228: bytes at 0x228 = "12 28" → JP 228 → infinite loop. Yes! That matches: the last instruction before data is at 0x226? Hmm, let me count: instructions occupy 0x200-0x227ish, data 0x22A-0x285 (134 bytes total = 0x86, so 0x200+0x86 = 0x286 end).

134 bytes: 0x200..0x285. Data from 0x22A to 0x285 = 92 bytes of sprite data. Instructions 0x200..0x229 = 42 bytes = 21 instructions. My recalled listing: CLS, LD I, LD V0, LD V1, DRW, ADD V0, LD I, DRW, LD I, ADD V0, DRW, ADD V0, LD I, DRW, ADD V0, LD I, DRW, JP — that's 18 instructions = 36 bytes → 0x200..0x223, then 0x224: JP 0x224? Hmm, whatever — the exact layout doesn't matter much.

Key insight: with correct XOR and blank screen, IBM logo renders correctly. With assignment, it should ALSO render correctly on a blank screen (since no overlaps). Therefore the user's garbling likely comes from an additional bug — OR their "direct assignment" means something worse, like `screen[y][x] = 1` for every bit regardless of sprite bit (i.e., ignoring the bit test), which would draw solid 8x15 blocks → garbled blobs! That's plausible: "直接赋值像素" could mean they assign the pixel without checking the sprite bit, or they assign color instead of toggling.

Hmm, but more common beginner bug: they do `if (sprite_bit) pixel = 1;` — that's assignment but still renders IBM logo fine. So the garbling must come from elsewhere. But the user attributes it to assignment. As a peer, I should:

1. Confirm DXYN must be XOR + VF collision flag — fix that regardless (it's required for correctness; many ROMs break otherwise).
2. Point out that for IBM logo specifically, assignment vs XOR shouldn't change the image on a cleared screen (no overlapping draws), so if it's garbled, there's likely a second bug. Then list the usual suspects with concrete checks:
   - ROM loaded at 0x200, PC starts 0x200.
   - Bit order MSB-first: `sprite[row] & (0x80 >> col)`.
   - Coordinates: x wraps mod 64, y mod 32; framebuffer indexed [y][x] (y*64+x), 64 wide, 32 tall.
   - N = opcode & 0xF, I points to sprite data.
   - CLS (00E0) implemented and called.
   - VF handling: VF = 0 at start of draw, set to 1 on erase; and make sure drawing still happens when VF set.
   - If using assignment `pixel = 1` only when bit set — fine for IBM; if assigning every bit (including 0s) you'd black out — but garbled suggests noise.

Actually, wait. Let me reconsider: maybe their "直接赋值" is `display[y][x] = chip8_pixel` where they assign the sprite bit including zeros — on a blank screen still fine.

Alternatively their garbling: maybe they render the framebuffer with wrong dimensions (e.g., treating it as 64x32 but indexing [x*64+y]) → sheared diagonal garbage. That's the classic "乱码" look.

Another classic: they update the display only... no.

Another: font not loaded → but IBM logo doesn't use font.

Another: stack/ret issues — IBM logo has no calls.

Another: 0x00E0 clears but they clear to 1? Unlikely.

Another big one: they execute one opcode per frame instead of per cycle — IBM logo still fine (it's just a few instructions then loop).

Another: they decode DXYN as `opcode & 0x000F` for N but use `opcode & 0x0F00` for X... standard.

Hmm, one more classic that garbles IBM logo specifically: the ROM's sprite data region — if their memory is zero-initialized but they load ROM at 0x200 correctly, fine.

Actually — the BIGGEST classic for "IBM logo shows garbage": implementing DXYN with `x` and `y` swapped in the framebuffer, or iterating `for col in 0..8 { pixel = (sprite[row] >> col) & 1 }` (LSB first) → mirrored. Mirrored IBM would still look like letters, just mirrored — "乱码" is more severe.

Given uncertainty, the best response: give the correct DXYN reference implementation (XOR + VF + wrap + MSB-first), explain why assignment breaks CHIP-8 semantics generally (self-erasing sprites, collision flag VF used for logic), and note that for the IBM logo specifically the sprite draws don't overlap, so if it's still garbled after the XOR fix, check the short list (bit order, indexing, ROM load address, N decode). Also offer to look at their code if they share it.

Wait — should I double check the claim "IBM logo draws don't overlap"? Let me verify with the actual ROM. I can fetch the ROM bytes from GitHub (e.g., from a known repo) and disassemble quickly. That would make my answer rigorous. Let me do that: search for ibm logo ch8 raw file.

Known repos: https://github.com/dmatlack/chip8/blob/master/roms/ibm-logo.ch8 ? Or "c8os"? The dmatlack/chip8 repo has roms/... Actually I recall https://github.com/dmatlack/chip8/tree/master/roms contains "ibm-logo.ch8"? There's also the famous "IBM Logo.ch8" in the "chip8 roms" pack. Let me fetch raw bytes via http_request and disassemble with a quick Python script via bash.

Plan:
1. Fetch IBM logo ROM bytes (web).
2. Disassemble to confirm draw coordinates and overlap.
3. Write the answer: correct DXYN semantics + why assignment is wrong + IBM-specific note + checklist.

Actually, can I run bash with python? The environment has bash. I can write a tiny disassembler inline. Let me do it.

Also the user might want code. I'll give a reference DXYN implementation (language-agnostic or Python/C). Since I don't know their language, give compact pseudocode/C-like or Python. Keep it tight.

Let me also reconsider: is it possible that with assignment the IBM logo DOES garble? If the emulator runs the infinite loop `JP 228` repeatedly and 0x228 contains `12 28`... wait if PC=0x228 and bytes at 0x228 are "12 28" → JP 0x228 → infinite loop, no drawing. Fine.

But hmm — what if their emulator doesn't implement CLS and their screen starts as random garbage (uninitialized buffer)? Then assignment would keep the garbage and draw logo on top → "乱码像素" everywhere plus logo. That matches "只出现乱码像素" (only garbled pixels)! If the framebuffer is uninitialized (malloc'd, not zeroed) or they render noise... Actually if buffer uninitialized, XOR vs assignment both keep garbage. CLS would clear it. So check: framebuffer zero-initialized + 00E0 implemented.

Hmm, "只出现乱码像素" could also mean "only garbled pixels appear (instead of the IBM logo)".

Another thought: maybe they draw pixels with assignment `buf[idx] = 1` where idx computed as `y*64+x` but their render loop reads `buf[x*32+y]`... too speculative.

The right move: give the correct DXYN, explain, and ask for their code / offer the checklist. Since this is a conversational debugging question (no code in workspace presumably), I should check if there's a workspace with their emulator code! The environment has a workspace — maybe their project is here. Let me glob for source files first. If their emulator code is in the workspace, I should read it and find the actual bug. That's the senior-engineer move.

Let me start: glob **/*.py, **/*.c, **/*.rs, **/*.js, **/*.cpp, etc. Or just `glob **/*` limited. Let me do a few globs in parallel and also fetch the IBM ROM in parallel.

Actually, let me first check the workspace contents. If empty, answer from knowledge + fetch ROM to verify overlap claim.

Let me do:
- glob "**/*" (might be huge; better targeted: "**/*.py", "**/*.c", "**/*.h", "**/*.rs", "**/*.js", "**/*.ts", "**/*.cpp", "**/*.go", "**/*.java")
- Also check for chip8-related filenames: grep -ri "dxyn" in workspace.

I'll run a few in parallel.

Then, fetch IBM logo ROM from a raw GitHub URL. Candidate URLs:
- https://raw.githubusercontent.com/dmatlack/chip8/master/roms/ibm-logo.ch8 — I think dmatlack/chip8 has roms/ folder with "ibm-logo.ch8"? Not 100% sure of path.
- Alternative: https://github.com/Chromosom3/Chip8 ... unknown.
- Search web if first fails.

Let me try dmatlack first; if 404, web_search.

Then disassemble via bash python one-liner.

Let me also prepare the correct DXYN semantics precisely:

```
DXYN:
  x = V[X] % 64
  y = V[Y] % 32
  V[F] = 0
  for row in 0..N-1:
    byte = memory[I + row]
    for col in 0..7:
      if byte & (0x80 >> col):
        px = (x + col) % 64
        py = (y + row) % 32
        if framebuffer[py][px] == 1:
          V[F] = 1
        framebuffer[py][px] ^= 1
```

Notes:
- Whether x/y wrap up front or per-pixel is a quirk debate; per-pixel modulo is the common safe choice.
- VF must be reset to 0 at start.
- Sprite bits MSB first.
- XOR is essential: sprites erase themselves on redraw (used for movement/flicker), and VF collision drives game logic.

Why assignment garbles things generally: ROMs animate by drawing sprite, then drawing the SAME sprite at the same position to erase (XOR twice = identity), or rely on collision. With assignment, redraws stack instead of toggling → screen fills into blobs. For IBM logo specifically (single pass, non-overlapping), assignment happens to produce the same image, so garbling there points to a second bug — checklist.

Hmm wait, actually now I want to double-check the "non-overlapping" claim with real data. Let me verify via disassembly. If it turns out the IBM logo ROM DOES overlap draws (e.g., the B's holes carved by XOR), then assignment alone fully explains the garbling, and I should say so confidently. This is exactly why I should verify rather than trust memory. My recalled hex shows 6 draws at x=12,16,24,28,36,40 with 8-wide sprites: x ranges 12-19, 16-23 (overlap with previous!), 24-31, 28-35 (overlap), 36-43, 40-47 (overlap). Wait: 12+8=20 > 16 → sprites at x=12 and x=16 OVERLAP in columns 16-19! Hmm interesting. So draws DO overlap horizontally. Whether the overlapping pixels are set in both sprites determines if XOR matters. The IBM logo: "I" is a narrow letter... Actually the logo is drawn as: two vertical bars (serifs?) and the B and M strokes. If adjacent sprites have set bits in overlapping columns at the same rows, XOR would cancel them → with XOR you'd get holes; with assignment you'd get solid. The real IBM logo on CHIP-8 — I've seen screenshots; it looks like the IBM 8-bar-ish logo. Hmm.

Actually wait, I mis-recalled the sequence. Let me not guess — fetch and disassemble. If overlaps exist with both-sprites-set pixels, then assignment fully explains garbling: overlapping regions that should cancel (or one sprite's bits overwriting) produce solid blocks → garbled. Actually with XOR, overlap of two set bits → 0 (hole). Would the real logo have holes? The IBM logo has distinct letters; the draws at x=12 and x=16 overlapping suggests the ROM intentionally uses XOR to combine shapes! E.g., the "I" letter drawn as two sprites that overlap to carve... Hmm, actually maybe the sequence is: draw left part, then draw the next letter part which overlaps the previous letter's right edge to erase overshoot? That's a known trick.

OK — verify empirically. Plan:

1. Parallel: glob workspace for source files; grep for "DXYN"/"0xD" patterns; fetch ROM bytes.
2. Disassemble ROM with python via bash; simulate both XOR and assignment draws to see which produces "IBM" vs garbage. Actually I can fully simulate: implement a tiny CHIP-8 interpreter in Python for just this ROM (it only uses CLS, LD, DRW, ADD Vx, JP, and maybe skip ops) and render both variants as ASCII. That gives definitive evidence: does assignment garble IBM logo? 

That's rigorous and fast. Then my answer: "Yes — assignment is the bug (or: assignment alone shouldn't garble IBM; your real bug is X — check these)". Either way, evidence-based.

Also check workspace for their code — if present, read DXYN and fix directly.

Let me execute:

Step 1 (parallel):
- glob "**/*.py"
- glob "**/*.c"
- glob "**/*.{rs,js,ts,cpp,h,hpp,go,java}" — glob may not support braces; do separate or use bash `ls -R | head`. Simpler: bash `find . -maxdepth 3 -type f | head -50`.
- http_request for ROM.

Actually bash find is one call covering all. But instructions prefer parallel read-only tools. I'll do: bash find, plus http_request ROM fetch, in one block.

For the ROM URL, try: https://raw.githubusercontent.com/dmatlack/chip8/master/roms/ibm-logo.ch8

Hmm, I believe dmatlack/chip8 repo structure: roms/ with subdirs? I recall "roms/ibm-logo.ch8" might not exist; there's "roms/" containing demos... Alternative known mirror: https://raw.githubusercontent.com/Chromosom3/... unknown. Another: the "chip8-test-rom" repos. There's also https://github.com/kripod/chip8-roms — yes! kripod/chip8-roms has "roms/" with categories; IBM logo is under "demos" maybe: https://raw.githubusercontent.com/kripod/chip8-roms/master/roms/demos/IBM%20Logo.ch8 — I think kripod/chip8-roms structure: /roms/demos/IBM Logo.ch8. URL-encode space as %20.

I'll try both URLs in parallel (http_request twice). If both fail, web_search.

Note: http_request returns JSON {status, body,...}; binary .ch8 might come back mangled (body as string with latin-1?). Risky. Better: use bash curl? The bash tool can run curl. `curl -s URL -o /tmp/ibm.ch8 && xxd /tmp/ibm.ch8 | head`. That's cleaner for binary. But does the sandbox have network? http_request is SSRF-safe for public URLs; bash curl might also work. I'll try bash curl first; fallback http_request.

Let me do in one parallel block:
1. bash: `find . -maxdepth 3 -type f -not -path "*/node_modules/*" -not -path "*/.git/*" | head -50` — see workspace.
2. bash: `curl -sL "https://raw.githubusercontent.com/kripod/chip8-roms/master/roms/demos/IBM%20Logo.ch8" -o /tmp/ibm.ch8 && ls -l /tmp/ibm.ch8 && xxd /tmp/ibm.ch8 | head -20` — fetch ROM.

Wait — can I make two bash calls in parallel? Yes, independent. But they might run in same workspace; fine.

Then step 2: disassemble + simulate in python.

Then answer.

Also: should I use explore/plan tools? The developer instructions say: before modifying code, call explore; for multi-step changes call plan. Here, if workspace has their emulator, I'd be modifying code → explore first. If workspace is empty (likely — this is a Q&A), no code modification, just answer. The explore tool says "Record a structured exploration note before editing any code". If I end up just answering, I can skip or do a light explore. I'll first look at the workspace; if there's a CHIP-8 project, I'll explore properly.

Let me start.

Actually also consider: the user's phrasing suggests they already suspect assignment is wrong ("我用的是直接赋值像素" — "I used direct pixel assignment"). They want confirmation + fix. So the core answer: yes, DXYN must XOR. Plus the IBM-specific nuance if verified.

Let me run the tools now.

One more consideration on simulation: the IBM ROM uses opcodes: 00E0, Axxx, 6xkk, 7xkk, DxyN, 1xxx (jump). My mini-interpreter handles those. Render 64x32 as ASCII (#/.). Compare XOR vs assignment (two variants: assign-1-only-when-bit-set, and assign-bit-including-0). Show that XOR → "IBM", assignment → garbage (if overlaps matter) or identical (if not). This determines my message.

Let me also handle: if fetch fails entirely, I can still answer from knowledge but hedge the IBM-specific claim. Better to verify.

Go.Workspace is empty (just AGENTS.md). So this is a pure Q&A — no code to read. The ROM URL 404'd. Let me find the right URL. Try dmatlack repo or search.

Candidates:
- https://raw.githubusercontent.com/dmatlack/chip8/master/roms/ibm-logo.ch8
- kripod/chip8-roms structure: maybe /roms/demos/IBM Logo.ch8 is wrong; could be under different casing. Let me check the repo listing via GitHub API: https://api.github.com/repos/kripod/chip8-roms/git/trees/master?recursive=1 — that returns JSON; grep for IBM.

Let me do that.Empty — maybe the API call failed (rate limit?) or branch is "main". Let me check.GitHub API 被限流了。正在并行尝试已知的原始路径：All 404. Let me use web_search to find the ROM hex dump or a working URL. Search "IBM Logo.ch8 hex dump" or "ibm logo chip8 rom bytes". There are pages that list the hex, e.g., "IBM Logo.ch8: 00 E0 A2 2A ..." on chip8.com or in blog posts. Also "chip8.gulrak.net" has an online disassembler but not the ROM. The "hughsk/chip8-disassembly" ... Let me search.Web search returning nothing. Try a simpler query.Web search is down/empty. Try http_request / web_fetch on known pages:

1. https://github.com/kripod/chip8-roms — HTML page listing. web_fetch it and look for IBM path.
2. Or try the jsDelivr CDN which mirrors GitHub: https://cdn.jsdelivr.net/gh/kripod/chip8-roms@master/ ... need exact path.
3. Try GitHub HTML tree page: https://github.com/kripod/chip8-roms/tree/master/roms — fetch and grep for "IBM".

Let me web_fetch the repo page.The demos dir has Maze, Particle, Sierpinski, Stars, Trip8, Zero Demo — no IBM Logo. Check "programs" dir.找到了：`programs/IBM Logo.ch8`。正在获取并反汇编。DXYN 的正确语义是异或（XOR）加 VF 碰撞标志，这个确实要改。但我把 IBM Logo.ch8（kripod/chip8-roms 版本，132 字节）反汇编后，用赋值和 XOR 两种模式各完整模拟了一遍：六次精灵绘制之间没有任何置位像素重叠，两种模式输出逐像素相同，都能画出正确的 IBM 字样。所以乱码另有原因。

ROM 实际做的事：

```
0200 00E0  CLS
0202 A22A  I = 0x22A
0204 600C  V0 = 12
0206 6108  V1 = 8
0208 D01F  draw(x=12, y=8, 15行)
020A 7009  V0 += 9
020C A239  I = 0x239
020E D01F  draw(x=21)
0210 A248  I = 0x248
0212 7008  V0 += 8
0214 D01F  draw(x=29)
0216 7004  V0 += 4
0218 A257  I = 0x257
021A D01F  draw(x=33)
021C 7008  V0 += 8
021E A266  I = 0x266
0220 D01F  draw(x=41)
0222 7008  V0 += 8
0224 A275  I = 0x275
0226 D01F  draw(x=49)
0228 1228  JP 0228    ; 停机
022A~      6 × 15 字节精灵数据
```

正确的 DXYN 参考实现：

```python
x = V[(op >> 8) & 0xF]
y = V[(op >> 4) & 0xF]
n = op & 0xF
V[0xF] = 0
for row in range(n):
    sprite = memory[I + row]
    for col in range(8):
        if sprite & (0x80 >> col):      # MSB 在前，先做位测试
            px = (x + col) % 64
            py = (y + row) % 32
            if fb[py][px]:
                V[0xF] = 1              # 像素将被擦除 → 碰撞
            fb[py][px] ^= 1             # 翻转；同一精灵画两次即自擦除
```

XOR 是精灵移动和闪烁的基础（重画即擦除），VF 是游戏逻辑的碰撞检测来源，赋值实现两者都拿不到，跑 IBM 之外的 ROM 必坏。

真正的乱码来源，按屏幕症状对号入座：

| 乱码形态 | 原因 |
|---|---|
| 六个 8×15 实心块 | 没做位测试，每个像素无条件写 1 |
| 字母镜像 | 位序反了，必须 `sprite & (0x80 >> col)` |
| 图案沿对角线剪切、错位 | 显存索引转置：64 宽 × 32 高，(x,y) 应存 `fb[y*64 + x]` |
| 满屏随机噪点 | `I = op & 0x0FFF` 掩码错，或 ROM 没加载到 0x200 / PC 起始地址不对，把数据当代码执行 |
| 图案位置漂移 | X/Y 取反了：`X=(op>>8)&0xF`，`Y=(op>>4)&0xF` |
| 精灵高度不对 | `N = op & 0xF`，这个 ROM 里 N=15 |

另外确认 00E0 清屏生效、帧缓冲零初始化。坐标取模在这一条 ROM 上用不上（所有坐标都在界内），其他 ROM 需要。

把你的 DXYN 和主循环代码贴出来，可以直接定位到具体哪一条。