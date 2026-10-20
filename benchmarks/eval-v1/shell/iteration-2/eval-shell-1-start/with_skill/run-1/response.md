The user wants to start writing their own shell in C, doing the most basic step first. This matches the build-your-own-x skill — specifically "build your own shell". I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of the SKILL.md.Topic is `shell`. Reading the track skill now — it's mandatory.Track skill is at `skills/shell/SKILL.md`, and there's a C-specific tutorial skill. Reading both.Let me read the rest of the shell track skill (it was truncated at line 43ish), and also the tutorials.md reference to pick a C tutorial. The C-specific per-tutorial skill points to kamalmarhubi/shell-workshop. The classic C tutorial is Stephen Brennan's "Tutorial - Write a Shell in C" (https://brennan.io/2015/01/16/write-a-shell-in-c/).

Let me read the remaining part of the shell track skill and the tutorials reference.技能已加载。按流程先看一下工作区现状和可用的编译工具。工作区是空的，Apple clang 已就绪，无需安装任何东西。按教程路线：Brennan 的《Tutorial - Write a Shell in C》，第 1 个里程碑是 REPL 循环。先记录探索结论并立计划，然后搭骨架。现在搭骨架：`mysh/main.c`（接口完整、核心留 TODO）、`Makefile`、`PROGRESS.md`。**进度：里程碑 1/7 — REPL 循环**（教程：[Tutorial - Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)）

**概念**：shell 的本质是一个死循环——打印提示符、读一行、切分成词、执行、释放内存、再来。今天只做前三步加 `exit`，真正执行程序（fork/exec）是里程碑 2。

**已就位**：`mysh/main.c`（能编译、能跑，核心留了 3 个 TODO）、`mysh/Makefile`、`mysh/PROGRESS.md`（里程碑表）。

**你来写的部分**（都在 `mysh/main.c`）：

1. `read_line()` — 读一行，返回去掉 `\n` 的堆上字符串；EOF 时返回 NULL。两条路任选：`getline()`（man 3 getline，它替你分配缓冲区）或 `getchar()` 循环 + `realloc` 手动扩容。
2. `split_line()` — 用 `strtok(line, " \t\r\n")` 切词，返回 NULL 结尾的 `char **`。注意 `strtok` 会往 `line` 里写 `\0`，所以参数是 `char *` 而非 `const char *`。
3. TODO 3 处 — 把 `argc` 数出来（遍历到 NULL 为止）。

**检查命令**（写完后跑）：

```
make -C mysh && printf 'hi  world\nexit\n' | ./mysh/mysh
```

预期输出：

```
> argc=2: [hi] [world]
> 
```

交互模式下按 Ctrl-D 也应干净退出。卡住了说一声，一次给一个提示。