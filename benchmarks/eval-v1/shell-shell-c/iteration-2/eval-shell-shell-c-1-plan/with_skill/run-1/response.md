The user wants to learn and implement "Build your own Shell" in C from scratch. They want me to first plan milestones and create a minimal project skeleton.

According to the instructions, I should read the build-your-own-x skill first since this matches its description exactly.The skill file was truncated. Let me read the rest of it.主题映射到 `shell` 轨道。正在读取轨道技能（强制）。轨道技能位于 `.agents/skills/build-your-own-x/skills/shell/SKILL.md`。正在读取它，以及 C 语言特定的教程技能。两个文件都被截断了。让我读取剩余部分以及参考文件。用户命名的教程「让我们构建一个 Shell！」映射到 `shell-shell-c` 技能 (kamalmarhubi/shell-workshop)。正在读取其剩余的参考资料。技能已加载。现在检查工作区状态和可用工具链，并获取一次上游 README 以对齐里程碑（技能允许只读 README 一到两次）。工作区是空的，工具链已就绪 (Apple clang 21 + GNU Make, macOS)。GitHub 页面返回的大多是页面外壳；我正在获取原始 README 以获取实际的研讨会步骤列表（在技能的一次性获取预算内）。工作区根目录下有一个 `AGENTS.md` 文件——在搭建骨架之前，我先阅读一下它。`AGENTS.md` 只是技能加载说明。所有上下文已收集完毕 —— 正在记录探索笔记和行动计划。检查点通过：构建零警告，回显正确，`exit` 干净退出（退出码 0）。创建 PROGRESS.md。里程碑规划与骨架已就绪。当前进度：**M1 / 7**。

**产出文件**

- `TASKS.md` — 7 个里程碑（REPL → fork/exec → 内建命令 → 引号与变量 → 重定向 → 管道 → 信号与作业），每个都带目标、关键概念和通过后才放行的检查点
- `myshell/` — 最小骨架：`Makefile`（`cc -Wall -Wextra -g -std=c11`）、`src/main.c`（仅 M1 的回显 REPL，后续里程碑只留 TODO 注释）、`README.md`、`.gitignore`
- `PROGRESS.md` — 进度表，M1 已记录骨架验证结果

**本里程碑的概念**：shell 的骨架是 REPL——打印提示符、`getline()` 读一行、处理、循环。`getline` 传 `NULL`/0 进去会自动 malloc 扩容，返回 `-1` 表示 EOF（Ctrl-D）。此刻它只是个「更个性化的 cat」，这正是上游练习 1 的起点。

**你的第一步**：给 shell 起名——上游作者说这是最重要的一步。改 `myshell/src/main.c:21` 的 `PROMPT` 宏（他用的是 `heee> `），顺手 `git init` 并做第一次提交。

**检查点**（改完名字后跑）：

```sh
make -C myshell
printf 'hi\nls\nexit\n' | ./myshell/myshell; echo $?
# 期望: 三行提示符各跟 hi、ls，然后退出码 0；交互模式下按 Ctrl-D 也应干净退出
```

通过后告诉我，我们进 M2：`fork` + `execvp` + `waitpid`，以及为什么直接调 `execvp` 会让你的 shell 自己消失。