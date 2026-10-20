The user says: "我的编辑器退出后终端不回显了，必须 reset 才能用。" (After my editor exits, the terminal doesn't echo anymore, I have to run `reset` to use it.)

This is a classic terminal state problem — the editor (or some program) crashed or exited without restoring terminal settings (specifically ECHO flag via termios). Common causes:
1. The editor crashed (segfault) and didn't restore termios.
2. The editor was killed with SIGKILL (kill -9), so no cleanup handlers ran.
3. The editor didn't properly save/restore terminal state (bug in the editor).
4. Using `stty sane` instead of `reset` is a lighter fix.
5. If it's their own editor (this workspace context suggests maybe they're building an editor — the build-your-own-x skill mentions editors/interpreters), the fix is to ensure terminal state restoration on exit, including signal handlers for SIGINT/SIGTERM/SIGHUP, and handling abnormal exits.

Wait — the context: there's a skill "build-your-own-x" which includes building editors. The user might be building their own text editor (like the kilo tutorial) and after exiting their editor, the terminal doesn't echo. That's a very common issue in the kilo tutorial — the `disableRawMode` uses `atexit`, but if the program crashes (e.g., segfault due to a bug), the atexit handler doesn't run, leaving the terminal in raw mode with ECHO off.

The user's message is ambiguous: it could be a general question ("my editor breaks my terminal") or they're developing their own editor. Given the workspace context and the skill available, I should check the workspace for files first. Let me look at what's in the workspace.

Actually, the skill instructions say: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else". The user's problem — "my editor exits and terminal doesn't echo" — could match "build-your-own-x" if they're building their own editor. But it could also just be a general terminal troubleshooting question about vim/nano/etc.

Let me first check the workspace to see if there's an editor project. If there is, this is likely about their own editor code. If not, it's a general question.

Let me glob the workspace.

The skill trigger: "Use it whenever someone wants to understand how a tool works by building their own... asks for a hands-on project..." — the user here has a problem with an editor. If they're building their own editor (kilo-style), the skill would apply for coaching. Let me check the workspace first.

Plan:
1. Glob workspace for files (e.g., *.c, *.py, editor-related).
2. If there's an editor project, read the relevant code (raw mode enable/disable, atexit, signal handling).
3. Diagnose: likely missing terminal state restore on abnormal exit, or raw mode not restored, or they enabled raw mode but crash before restore.
4. Provide fix: atexit + signal handlers, or tcgetattr save/restore, and immediate workaround `stty sane`.

Let me start with glob and maybe grep.The workspace only contains the skills directory and AGENTS.md. There's no user editor project. So the user is asking a general question: "After my editor exits, the terminal doesn't echo, I have to run reset."

Hmm, but wait — is the user building their own editor? The workspace has no project files. The user's question is a troubleshooting question. It could be:
1. They use vim/nano/less and after exit the terminal is broken.
2. They're developing their own editor (maybe elsewhere) and it breaks the terminal.

Given the skill available (build-your-own-x with a text-editor skill), and the AGENTS.md context, the user might be in the middle of building their own editor and hit this classic problem. But there's no code in the workspace. The question reads like a general troubleshooting question: "我的编辑器退出后终端不回显了，必须 reset 才能用。"

Should I read the skill? The skill trigger says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills..." The user hasn't asked to build anything; they have a broken terminal. However, if they're building their own editor, the text-editor skill would be relevant. The skill description for text-editor-text-editor-cpp likely covers raw mode and terminal state restoration.

Let me read the text-editor skill's SKILL.md and concepts to see if it covers this exact issue — it likely does (kilo tutorial covers "terminal state restoration" and the common pitfall of terminal left in raw mode after crash). Actually, the instruction says to read the SKILL.md BEFORE doing anything else when the task matches. The task: "my editor exits and terminal doesn't echo" — this is a debugging question about terminal raw mode. If the user is building their own editor, this matches the text-editor skill's domain.

Given ambiguity, the safest path: read the text-editor SKILL.md (cheap) to see if it has guidance on this exact problem, then answer. The answer itself is well-known:

**Diagnosis**: The editor put the terminal into raw mode (disabled ECHO via termios/tcsetattr) and exited without restoring it. This happens when:
- The editor crashed (segfault) — atexit handlers don't run on abnormal termination.
- The editor was killed with SIGKILL (kill -9) — no handler can catch it.
- The editor has a bug: enables raw mode but the restore path is missing or fails.

**Immediate fix**: `stty sane` (lighter than `reset`; reset also fixes character set/scroll regions). Or `reset`. Or open a new shell. Also `tput rmcup`/`printf '\e[?1049l\e[?25h'` for alternate screen/cursor issues.

**If it's their own editor, the durable fix**:
1. Save original termios with `tcgetattr(STDIN_FILENO, &orig)` before enabling raw mode.
2. Register restore with `atexit()`.
3. Install handlers for SIGINT, SIGTERM, SIGHUP, SIGSEGV (best-effort), SIGTSTP, SIGCONT (re-apply raw mode after SIGCONT since the shell's TTY driver may reset... actually on SIGTSTP the shell restores the terminal; on SIGCONT you need to re-enable raw mode).
4. On crash: a SIGSEGV handler that restores termios then re-raises is best-effort but risky; the robust approach is to run the editor logic in a child process and have the parent restore the terminal when the child dies (like how some editors/pagers do it), or just accept `stty sane`.
5. Also handle EIO: when the terminal is in raw mode and the process is backgrounded, reads fail with EIO.

Also mention: if using Python `tty.setraw()` / `termios`, use try/finally. If using curses, `curses.endwin()` in finally, or use `curses.wrapper`.

Also the classic kilo tutorial issue: `enableRawMode` with `atexit(disableRawMode)` — if the program segfaults (e.g., in editorRefreshScreen due to a bug), atexit doesn't run → terminal stuck in raw mode → no echo. Fix: fix the segfault, and add signal handlers.

Let me check the skill to align with its guidance. The skill instruction says to read SKILL.md before doing anything else when the task matches. I already did glob/ls (fine, read-only). Let me read the text-editor SKILL.md and its concepts.md to see if there's specific guidance on terminal restoration.

Actually, wait. Is the user building their own editor? There's no evidence in the workspace. The question is phrased as a user of an editor: "我的编辑器退出后" — "after my editor exits". Could be vim. But in this workspace context (build-your-own-x skills installed), it's plausible they're building one. The phrase "必须 reset 才能用" suggests they know the reset workaround.

I think the best answer covers both: explain the mechanism (raw mode / ECHO flag not restored), give the quick fix (stty sane), and give the durable fix depending on whether it's vim/nano (check TERM, stty settings, or a shell hook) or their own editor (atexit + signal handlers + try/finally).

Let me read the text-editor skill quickly to see if it has a section on this — it would help me give consistent guidance and maybe reference the skill's concepts. It's cheap to read.终端回显设置属于 tty 设备本身，进程退出时内核不会帮你恢复。编辑器启动时用 `tcsetattr` 关掉了 `ECHO`（raw mode 的一部分），只要它**异常退出**，恢复代码没跑到，你回到的 shell 就继承了一个不回显的终端。

**立刻修复**：`stty sane`。它只恢复行规程设置（echo、icanon、isig 等），比 `reset` 轻（reset 还会重置字符映射、滚动区域）。如果只是丢了回显，`stty echo` 也够。事后可以 `stty -a` 确认，坏掉时通常能看到 `-echo -icanon -isig`。

**判断是哪种情况**：

- 编辑器退出后 `echo $?` 是 139 → 段错误，`atexit` 注册的恢复函数不会执行。
- 被 `kill -9` 杀掉 → SIGKILL 不可捕获，进程内任何方案都救不了。
- 正常退出也坏 → 恢复路径本身有 bug（比如某条错误分支直接 `exit` 绕过了恢复）。

**根治（如果是你自己在写的编辑器）**，四个要点：

1. 开 raw mode 前先 `tcgetattr` 保存原始设置。
2. `atexit` 恢复，覆盖正常退出。
3. 给 SIGINT/SIGTERM/SIGHUP/SIGQUIT/SIGTSTP 装处理器：先恢复终端，再恢复默认处理并 re-raise（保留 Ctrl-C 返回 130 这类语义）。
4. SIGCONT 时重新进入 raw mode——Ctrl-Z 挂起再恢复后，shell 可能已经重置过终端。

```c
static struct termios orig;

static void disableRawMode(void) { tcsetattr(STDIN_FILENO, TCSAFLUSH, &orig); }

static void onSignal(int sig) {
    disableRawMode();
    signal(sig, SIG_DFL);
    raise(sig);
}

void enableRawMode(void) {
    struct termios raw;
    tcgetattr(STDIN_FILENO, &orig);
    atexit(disableRawMode);
    signal(SIGINT, onSignal); signal(SIGTERM, onSignal);
    signal(SIGHUP, onSignal); signal(SIGQUIT, onSignal);
    signal(SIGTSTP, onSignal);              /* 挂起前恢复 */
    signal(SIGCONT, enableRawMode);         /* 恢复后重开 */

    raw = orig;
    raw.c_lflag &= ~(ECHO | ICANON | ISIG | IEXTEN);
    raw.c_iflag &= ~(IXON | ICRNL | BRKINT | INPCK | ISTRIP);
    raw.c_oflag &= ~(OPOST);
    raw.c_cflag |= CS8;
    raw.c_cc[VMIN] = 0; raw.c_cc[VTIME] = 1;
    tcsetattr(STDIN_FILENO, TCSAFLUSH, &raw);
}
```

SIGSEGV 也可以装 best-effort 处理器（恢复后 re-raise），实践中通常有效但不可靠。真正稳的模式是父子进程：父进程持有 tty，编辑器逻辑跑在子进程里，父进程 `waitpid` 后无条件恢复终端——子进程哪怕被 `kill -9` 或段错误，终端也能复原。

其他语言的等价写法：Python 用 `try/finally` 包住 `termios.tcsetattr`（curses 就用 `curses.wrapper`）；Rust 写一个实现 `Drop` 的 guard。

如果是现成的 vim/less 出这个问题，基本只有崩溃或被 SIGKILL 一种解释，`dmesg` 里能看到对应的 segfault 记录；正常退出还坏的话，检查 shell rc 里有没有动过 `stty`。