The user is asking about the build-your-own-x skill, specifically the build-your-own-shell track, and whether they can do it on Windows without WSL. I should read the skill's SKILL.md first, as instructed by the project notes, since the task matches the skill description ("asks which build-your-own project to start with" / "stuck" / wants to do a track).

Let me read the SKILL.md and see what it says about the shell track, then answer the Windows question.The file was truncated. Let me read the rest of the SKILL.md, and also look at the shell track skill. Let me find the skills directory structure.The track skill is `skills/shell/SKILL.md`. Reading it plus the tutorial list to check platform assumptions.Let me read the rest of the shell SKILL.md (it was truncated at line 43).The track skill assumes Unix (`skills/shell/SKILL.md:26` says "Unix-like OS assumed. On Windows, use WSL"), so let me verify how portable the two non-C tutorials actually are before recommending a Windows-native path.The Rust tutorial uses `std::process::Command`, which is cross-platform. Let me check the per-tutorial coaching skills for Rust and Go to see what they assume.Yes — with one caveat at the end of the track. I read the track skill (`skills/shell/SKILL.md`); it assumes Unix ("On Windows, use WSL"), but that assumption really only bites in two places, and the rest of the track runs fine natively on Windows.

**What works natively (milestones 1–6 of 7)**

REPL loop, spawning programs, built-ins, quoting/env expansion, redirection, and pipes all map cleanly to cross-platform std APIs — `std::process::Command` in Rust or `os/exec` in Go handle spawn, wait, `Stdio` redirection and piped processes identically on Windows. I verified the Rust tutorial (Josh McGuigan, [build-your-own-shell-rust](https://www.joshmcguigan.com/blog/build-your-own-shell-rust/)) uses exactly those APIs, so you can follow it verbatim on Windows. The Go tutorial's original link (sj14.gitlab.io) now 404s, which makes Rust the better-supported choice here.

**What you lose**

- **Milestone 7 (signals + jobs):** Windows has no POSIX signals or process groups. Ctrl-C becomes a console control event, and killing a child tree needs Job Objects or `taskkill /T`. Doable, but it turns into a Windows-API exercise instead of a signals one.
- **The fork/exec mental model:** the C tutorials (brennan.io etc.) are built on `fork`/`execvp`/`waitpid`/`dup2`, and MSVC has no `fork`. If that low-level process model is your actual goal, the cleanest no-WSL path is Docker Desktop: edit on Windows, compile and test inside a Linux container (`docker run --rm -it -v ${PWD}:/work gcc bash`). That gives you the real Unix syscalls with a one-command setup.

**My recommendation:** Windows-native Rust track, milestones 1–6 as written, milestone 7 either skipped or done as a Windows-API stretch. You still learn parsing, process lifecycle, I/O plumbing and job control concepts — only the raw syscall layer differs.

Two scoping questions before milestone 1: are you comfortable in Rust (or would you rather use Go/Python), and is your goal the shell itself or specifically the fork/exec internals?

**Check your toolchain** (run in PowerShell, install from [rustup.rs](https://rustup.rs) if missing):

```
cargo --version
```

Expected: `cargo 1.xx.x (xxxxxxx 20xx-xx-xx)`. Once that prints, we start milestone 1: a REPL that reads a line, splits it, and exits on `exit` or Ctrl-D.