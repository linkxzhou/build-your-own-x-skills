The user wants to build a terminal text editor like kilo in C. This matches the build-your-own-x skill. I should read the SKILL.md first before doing anything else.The SKILL.md was truncated. Let me read the rest of it, and also check the category map for the editor category. The user wants to build a terminal text editor like kilo in C. Let me read the rest of the file.The category is `text-editor`. Now I must read the track skill, and check for a kilo-specific tutorial skill.The track skill output was truncated. Let me read the rest, plus the tutorials reference and the kilo-specific per-tutorial skill.The track skill and kilo per-tutorial skill are loaded. Let me check the workspace state and available toolchain, plus the tutorial map.Workspace is empty, toolchain is ready (cc/clang/make on macOS), and the track + kilo tutorial skills are loaded. Setting up the milestone plan and the starter skeleton.Now create the starter skeleton: kilo.c with the milestone-1 TODOs, a Makefile, and PROGRESS.md. Then give the milestone 1 coaching turn.The skeleton compiles clean, and the pipe test confirms the guard works: with no TTY, `tcgetattr` fails and `die()` exits with `Inappropriate ioctl for device` — exactly what should happen outside a real terminal.

**Where we are:** milestone 1/7 — raw mode.

**The concept.** A terminal starts in *canonical mode*: the OS buffers a whole line, echoes what you type, and only hands your program data when you press Enter. An editor needs every keypress instantly, unechoed, so it flips the tty into *raw mode* via `termios`: save the original settings, clear the right flag bits with `tcsetattr`, and restore the saved settings on exit — otherwise your shell is left with no echo after the program dies.

**What to write next** (TODOs are marked in `kilo.c`):
1. `disableRawMode()` — copy `orig_termios` back with `tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig_termios)`, register it with `atexit()`.
2. In `enableRawMode()`, clear `ECHO | ICANON | ISIG` on the copy, then `tcsetattr` it.
3. Replace the `q` quit with `c == 17` (Ctrl-Q) — control chars are `ctrl` + letter, and Ctrl-Q is ASCII 17.

**How to check it.** Run `./kilo` in a real terminal (Terminal.app/iTerm2 — an IDE output pane is a pipe, as you just saw). Type `asdf`: each key prints its code (`97 ('a')` …). Press Ctrl-Q: it exits and your shell still echoes normally. Then try Enter, Ctrl-C, Esc and note their codes — you'll want them in later milestones.

**Stuck?** First hint: `raw.c_lflag &= ~(ECHO | ICANON);` — the other flags live in `c_iflag`/`c_oflag`, and `VMIN`/`VTIME` in `c_cc` come in the next chapter.

Guide: https://viewsourcecode.org/snaptoken/kilo/ (chapters 1–2 cover this milestone). When the check passes, tell me and we'll log it in `PROGRESS.md` and move to screen drawing.