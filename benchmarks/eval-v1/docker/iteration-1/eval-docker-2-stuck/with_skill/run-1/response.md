两个原因，通常同时存在：

**1. `unshare(CLONE_NEWPID)` 只对之后 fork 出的子进程生效**

PID namespace 的规则是：调用 unshare 的进程自己留在旧 namespace，新 namespace 只作用于之后创建的子进程。如果你 unshare 后直接 exec 了 `ps`，你其实还在宿主机的 PID ns 里。验证方法：在"容器里"和宿主机分别执行 `readlink /proc/self/ns/pid`，结果一样就是这种情况。修法：unshare 之后必须 fork，子进程才是新 ns 的 PID 1。

**2. `ps` 读的是 /proc，而 /proc 还是宿主机挂载的那份 procfs**

procfs 展示哪个 namespace 的进程，取决于挂载它的进程所在的 PID namespace。你进入新 PID ns 后，/proc 仍然是宿主机（初始 ns）挂载的旧 mount，所以 `ps`、`top` 看到的还是全量宿主机进程。修法：同时创建新的 mount namespace（`CLONE_NEWNS`），在新 ns 里重新挂 proc。

正确写法：

```c
unshare(CLONE_NEWPID | CLONE_NEWNS);   // mount ns 对调用者立即生效
if (fork() == 0) {                     // 子进程才是新 PID ns 的 PID 1
    mount("proc", "/proc", "proc", 0, NULL);
    execvp("sh", (char *[]){"sh", NULL});
}
```

命令行等价物（util-linux 已封装好这套流程）：

```
unshare --pid --fork --mount-proc /bin/sh
```

验证：进去后 `ps aux` 应该只剩 PID 1 自己；`ls /proc | grep -c '^[0-9]'` 只有个位数。

两个附带注意点：

- 重新挂 proc 需要 `CAP_SYS_ADMIN`，所以要在 root 下做。
- 新 ns 里第一个进程就是 PID 1，需要自己收割僵尸进程（安装 SIGCHLD 处理并 `wait()`），否则它的子进程退出后会以僵尸状态留在 ns 里。

补充一点：即使不重挂 /proc，内核侧的隔离（PID 编号、kill 的 pid 解析范围）已经生效，泄漏的只是通过旧 /proc mount 看到的视图——但这个视图足以让 `ps` 显示宿主机全量进程，所以必须处理。