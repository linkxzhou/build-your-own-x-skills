The user wants to learn and implement "Let's build a shell!" (让我们构建一个 Shell！) from scratch in C. They want me to first plan milestones and create a minimal project skeleton.

This is likely referring to the "build-your-own-x" repository's shell tutorial — the workspace name is "build-your-own-x-shell-shell-c-1", which suggests this is from the build-your-own-x list. The famous one is "Let's build a shell!" by Yehuda Katz & Tom Dale? Actually, the well-known one in build-your-own-x for shells in C is "Let's build a shell!" — there's a tutorial by "Yehuda Katz"? Let me think. In build-your-own-x/README under "Build your own Shell":
- "C: Let's build a shell!" by Yehuda Katz and Tom Dale? Hmm, actually I recall "Let's build a shell!" is by "Yehuda Katz"? No...

The build-your-own-x repo lists:
- C: Let's build a shell! — https://github.com/kamalmarhubi/shell-workshop (by Kamal Marhubi)
- C: Let's build a shell! — by Yehuda Katz? 

Actually I remember: "Let's build a shell!" workshop by Kamal Marhubi and Jorge Aparicio? The repo is kamalmarhubi/shell-workshop. There's also "Write a Shell in C" by Stephen Brennan (Brennan.io tutorial "Tutorial - Write a Shell in C").

The workspace name "build-your-own-x-shell-shell-c-1" suggests the first C shell entry in build-your-own-x, which is "Let's build a shell!" by Kamal Marhubi (shell-workshop). That tutorial has steps: it's a workshop with exercises — parsing, forking, executing, builtins like cd, exit, PATH lookup, etc.

The user asks in Chinese: "我想从零开始用 C 学习并实现「让我们构建一个 Shell！」，请先帮我规划里程碑并创建最小项目骨架。" — "I want to learn and implement 'Let's build a shell!' from scratch in C. Please first help me plan milestones and create a minimal project skeleton."

So the task: plan milestones (roadmap) and create a minimal project skeleton (directory structure, Makefile, main.c stub, README with milestones, maybe tests).

Per my instructions: I should explore the workspace first, then plan, then execute. Let me check what's in the workspace.

I should:
1. Explore workspace (glob to see existing files).
2. Maybe fetch the tutorial to align milestones with it (web_fetch the shell-workshop repo README). That would help make milestones faithful to the tutorial. The build-your-own-x entry: "C: Let's build a shell!" links to https://github.com/kamalmarhubi/shell-workshop. Let me verify via web search or fetch.

3. Create plan with milestones.
4. Create skeleton: Makefile, src/main.c, include/, tests/, README.md with milestone plan, .gitignore.

Since this is a multi-step change, I should call explore once, then plan, then todo_write, then execute.

Let me start by checking the workspace contents and fetching the tutorial info in parallel.

Let me do: glob '**/*' to see workspace, and web_fetch the GitHub repo README.

Actually the user said "从零开始" (from scratch), so the workspace is probably empty. Let me check.

Plan for skeleton:
- README.md — milestones (里程碑) mapped to tutorial steps
- Makefile — build with gcc/clang, -Wall -Wextra -std=c11, debug target
- src/main.c — minimal REPL skeleton (read line, print, loop) with TODOs
- src/ maybe split later; keep minimal: main.c only
- include/shell.h maybe minimal
- tests/ — a simple smoke test script (test.sh) that pipes commands
- .gitignore

Milestones based on "Let's build a shell!" (kamalmarhubi/shell-workshop):
The workshop has exercises:
1. Print a prompt and read a line
2. Parse the line into words (split on whitespace)
3. Fork and exec (run commands with execvp)
4. Wait for child
5. Builtins: exit, cd
6. PATH lookup (execvp does it, but workshop does manual PATH search)
7. Signals? Maybe not.

Actually the shell-workshop README: "Let's build a shell!" — exercises:
- Exercise 1: Print a prompt
- Exercise 2: Read a line of input
- Exercise 3: Parse the input
- Exercise 4: Execute the command (fork/exec)
- Exercise 5: cd builtin
- Exercise 6: exit builtin
- Exercise 7: PATH lookup

I'm not 100% sure of the exact exercise list. Let me fetch the repo to be faithful. I'll do web_fetch on https://github.com/kamalmarhubi/shell-workshop.

Let me first glob the workspace and fetch the tutorial in parallel.

Then create plan, todos, and files.

Language: respond in Chinese since user wrote in Chinese.

Let me start.The GitHub page fetch got mostly navigation chrome. The repo is "kamalmarhubi/shell-workshop: Materials from my Strange Loop 2014 workshop, Let's Build a Shell!" — confirmed. Let me fetch the raw README to get the exercise structure so milestones align with the tutorial.README 被截断了。让我获取完整的练习列表。The output got truncated at 8900 chars. Let me get the rest of the README — the sections after "4. Forking a new process". Let me use grep on the downloaded content to extract headings and exercise markers.Now I have the full exercise structure of "Let's build a shell!" (Strange Loop 2014 workshop by Kamal Marhubi):

- §0 Getting started (skeleton code + utility functions)
- §1 Exercise 1: prompt + read line, echo it back (glorified cat)
- §2 System calls (execve/execvp background)
- §3 Exercise 2: execute command with args (parse_command provided)
- §4 Forking a new process (Exercise 3 implied: fork before exec)
- §5 Waiting for children — Exercise 4: wait
- §5 Builtins — Exercise 6: cd builtin (there's probably Exercise 5: exit builtin, let me check lines 96-146)
- §6 Pipelines — Exercise 7: fork_and_exec_with_io, Exercise 8: 2-element pipes
- §7 What next — natural progressions & other directions

Let me read the middle part (lines 75-215) to see exercises 3, 5, and the "what next" list so my milestone plan is faithful.Let me see the rest (pipelines section and what next).教程结构已确认。工作区为空。让我记录探索结果并制定计划。计划已设定。现在开始编写所有骨架文件。所有文件已写入。现在我来验证构建和测试。构建成功，冒烟测试通过，回显功能正常。最后一步：执行 `git init` 并进行初始提交（对应教程第 0 步）。骨架已就绪并验证通过（`make` 零警告、`make test` 绿、已提交 `c4a6f2e`）。

**里程碑**（完整表格在 `README.md`，与教程练习一一对应）：

| 里程碑 | 练习 | 核心 API |
|---|---|---|
| M0 ✅ | §0 骨架 | — |
| M1 ✅ | Ex1 提示符+读入+回显 | `getline` |
| M2 | Ex2 直接执行命令 | `execvp` |
| M3 | Ex3 fork 后再 exec | `fork` |
| M4 | Ex4 等待子进程 | `wait` |
| M5 | Ex6 内建 `exit`/`cd` | `chdir` |
| M6 | Ex7+8 两段管道 | `pipe`/`dup2` |
| M7 选做 | §7 长管道/重定向/`$VAR` | `open`/`getenv` |

**骨架内容**：
- `src/main.c` — M1 回显 REPL 已实现，`TODO(M2)`~`TODO(M6)` 注释标出每个里程碑的落点，动手时照着做即可
- `include/parse.h` + `src/parse.c` — 教程 Rule 0 视为"给定代码"的解析工具（`parse_command`/`parse_line`），M2 起使用
- `Makefile`（`make` / `run` / `test` / `clean`）、`tests/smoke.sh`（M1 用例，随里程碑追加）

一个刻意保留的教学点：M2 直接 `execvp` 会让 shell 自己被替换退出——这是教程安排的顿悟时刻，M3 的 `fork` 就是为了解决它。下一步打开 `src/main.c:37`，从 M2 开始实现。