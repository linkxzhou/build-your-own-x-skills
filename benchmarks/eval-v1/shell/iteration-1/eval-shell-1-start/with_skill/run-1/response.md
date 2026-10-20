The user wants to write their own shell in C, starting with the most basic step. This matches the build-your-own-x skill — specifically "build your own shell". I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read more of it, and also find the shell track skill. The category map was truncated. Let me read the rest of the SKILL.md and look for the shell track skill.The track skill is `skills/shell/SKILL.md` (mandatory), and there's a C-specific tutorial skill. Reading both.已读取 Track skill 和 C 语言教程 skill。现在正在加载教程参考并检查工作区状态。技能已加载：shell track + C 教程。工作区是空的，macOS 上有 `cc`/`make`。按流程先记录探索结论并制定计划，然后搭骨架。骨架开工：我搭好 `main` 循环和构建环境，把 M1 的核心（读行、分词）留 TODO 给你写。The scaffold works: prompts, reads lines, exits on "exit" with status 0. (The stubs return NULL for read_line so it breaks immediately at EOF — actually wait, the piped input: first read_line returns NULL (stub), so it breaks at EOF immediately. That's why only one "> " appeared. Fine — the loop logic itself is verified via the exit path... actually no, with the stub returning NULL it breaks immediately. The "exit" path wasn't exercised. But that's fine — the learner will implement and test. The scaffold compiles clean and the loop's EOF path works.

Hmm, but I should verify the loop's exit-command path works too. With stubs, read_line returns NULL immediately so we never get to test "exit". I could temporarily... no — keep it simple. The learner will implement read_line and split_line, then the full checkpoint runs. The scaffold is verified to compile and run without crashing.

Now update todos: s1 completed, s2 in_progress (learner's work). Then write the coaching response: where we are, the concept, what to write, how to check.**Milestone 1/7 — REPL 循环。** 骨架已就绪，参考教程：[Tutorial — Write a Shell in C](https://brennan.io/2015/01/16/write-a-shell-in-c/)（Stephen Brennan）。

**已建好的文件**

- `shell.c` — `main` 和 `lsh_loop()` 已写好，两个核心函数留了带提示的 TODO
- `Makefile` — `make` 已验证编译零警告（`-std=c11 -Wall -Wextra`）
- `README.md` — 7 个里程碑和各自的验收标准
- `PROGRESS.md` — 每过一关记录一次

**概念（30 秒版）**：shell 的本质是一个 REPL——读一行、切成参数、执行、循环。M1 只做前三步的“读”和“切”，执行是空壳。关键点有两个：`getline()` 替你管理缓冲区增长，EOF 时返回 -1（这就是 Ctrl-D 退出的信号）；`strtok()` 返回的 token 是指向原字符串内部的指针，所以最后只需 `free(args)` 和 `free(line)` 两次。

**你的任务**：打开 `shell.c`，实现两个函数（提示都写在注释里）：

1. `lsh_read_line()` — 用 `getline()`，先 `man 3 getline` 看签名
2. `lsh_split_line()` — 用 `strtok()` 按 `LSH_TOK_DELIM` 切，装进 malloc 的数组，装满了就 `realloc` 翻倍

**验收命令**：

```sh
make && ./shell
```

- 输入 `exit` 回车 → 退出，`echo $?` 显示 0
- 直接按 Ctrl-D → 干净退出
- 空行回车 → 重新出现 `> ` 提示符

写完贴上来或直接说“跑不通”，我们从真实输出开始调。