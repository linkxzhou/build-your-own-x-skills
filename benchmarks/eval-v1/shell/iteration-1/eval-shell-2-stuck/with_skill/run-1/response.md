`wc` never sees EOF, so it blocks in `read()` forever and your `waitpid` never returns. A pipe reader gets EOF only when **every** write end is closed — and after two forks there are up to four processes holding those descriptors: the parent and both children each inherit both `fds[0]` and `fds[1]`.

The usual culprit: the parent closes nothing (or closes only one end) after forking. The parent's open `fds[1]` keeps the pipe alive even though `ls` exited, so `wc -l` waits indefinitely and prints nothing.

Rule: after `dup2`, every process must close both raw pipe fds — including the parent, after both forks.

```c
int fds[2];
pipe(fds);

pid_t p1 = fork();
if (p1 == 0) {                      /* ls */
    dup2(fds[1], STDOUT_FILENO);
    close(fds[0]);                  /* ls must not hold the read end */
    close(fds[1]);                  /* dup2'd copy is enough */
    execvp("ls", argv1);
}

pid_t p2 = fork();
if (p2 == 0) {                      /* wc */
    dup2(fds[0], STDIN_FILENO);
    close(fds[0]);
    close(fds[1]);                  /* <-- the one people forget */
    execvp("wc", argv2);
}

close(fds[0]);                      /* parent closes BOTH, after both forks */
close(fds[1]);

waitpid(p1, &st1, 0);
waitpid(p2, &st2, 0);
```

Two related traps worth checking while you're in there:

- **Closing before the second fork** gives the opposite symptom: `wc` inherits a closed stdin and prints `0` immediately.
- **`ls` keeping `fds[0]` open** doesn't cause this hang, but it breaks SIGPIPE: if `wc` dies early, `ls` blocks instead of getting `EPIPE` on write. Close it.

To confirm who's holding the write end on a live hang: `ls -l /proc/$(pgrep -f wc)/fd` — you'll see the pipe fd, then check which other PID shares it (`lsof | grep pipe`). Check `dup2`/`execvp` return values too; a failed `execvp` with an unclosed write end produces exactly this hang.