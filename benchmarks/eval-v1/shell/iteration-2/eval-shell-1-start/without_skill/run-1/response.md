The user wants to write a basic shell in C — the most fundamental first step. This is a classic "build your own shell" exercise. Let me check the workspace first to see what's there, then write a minimal shell.

The most basic step for a shell in C is typically:
1. A REPL loop: print prompt → read line → parse → execute (fork + execvp + wait) → handle builtins (exit, cd)

Let me look at the workspace first.工作区是空的，从零开始。最基本的一步就是一个 REPL 循环：打印提示符 → 读一行 → 解析 → `fork` + `execvp` 执行外部命令 → `waitpid` 等待，外加 `cd` 和 `exit` 两个内建命令（`cd` 必须内建，因为它改变的是 shell 自身的进程状态）。编译零警告，测试全部符合预期（最后 `ls` 报错恰好证明 `cd /` 生效了——相对路径在新目录下找不到文件）。

已创建 `shell.c`，这是最基本的一步：

- **REPL 主循环**：`msh>` 提示符 → `getline` 读行 → `strtok` 按空白分词 → 执行 → 回到提示符
- **外部命令**：`fork()` 出子进程，子进程 `execvp()` 替换自身执行命令，父进程 `waitpid()` 阻塞等待；`execvp` 失败时打印错误并以 127 退出
- **内建命令**：`cd`（必须内建，因为 `chdir` 只影响当前进程，放进子进程毫无意义；无参数时回退到 `$HOME`）和 `exit`；Ctrl+D（EOF）也能干净退出

运行方式：`./msh`，然后可以试 `ls -l`、`echo hi`、`cd /tmp` 等。

这一步跑通后，自然的下一步是：管道 `|`、重定向 `>` `<`、`&` 后台执行、信号处理（Ctrl+C 只杀子进程不杀 shell）。想继续哪个告诉我即可。