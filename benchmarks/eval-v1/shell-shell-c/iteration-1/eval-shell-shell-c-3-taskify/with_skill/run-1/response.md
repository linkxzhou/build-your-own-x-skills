The user wants me to convert the shell-workshop tutorial from kamalmarhubi/shell-workshop into a Claude Code executable learning task list. Let me first check the skill that matches — "build-your-own-x" — since this is about learning by building (a shell). The skill says to read SKILL.md before doing anything else.

Let me read the skill first, then fetch the GitHub repo content.The GitHub page fetch was mostly navigation chrome. I need the actual README content. Let me fetch the raw README from raw.githubusercontent.com. Also, I should read the rest of the SKILL.md (it was truncated) and check the shell track skill.

Let me:
1. Read the rest of the SKILL.md (truncated at line 43).
2. Fetch raw README of shell-workshop.
3. Check the skills directory for a shell track skill.README 被截断了。让我获取完整的 README 并检查 shell track skill。README 一直被截断。我将通过 `curl` 下载它，并读取必需的 shell track skill。README 已下载（共 233 行）。我来读取一下，并检查一下仓库结构。The read tool can't read /tmp (outside workspace). Let me move the README into the workspace, e.g. `.agents/tmp/` or just workspace root. Also GitHub API rate limited. Let me copy the file into workspace and read it. For the repo tree, I can try fetching the GitHub HTML page for the file listing, or use codeload to download the tarball.The read tool truncated. Let me read the rest in chunks.我已经获取了完整的教程。现在让我检查一下练习所依赖的骨架代码（`shell.c`、`utils.h`、`utils.c`、`Makefile`），因为任务列表需要引用实际的接口。仓库中的 `shell.c` 是一个完整的参考解决方案——这对任务设计很重要（学习者需要自己构建 `shell.c`，并将仓库中的版本作为最终检查的参考）。让我确认一下 `utils.c` 实际上解析了什么（它是否处理 `|` 和重定向？），因为练习是围绕它构建的。现在我来读取 `utils.c` 以准确了解解析器处理的内容——这决定了重定向任务是否需要解析器扩展。我已经准备好所需的一切：完整的教程文本、骨架 API（`utils.h`）以及一个关键发现——仓库中的 `shell.c` 是一个完整的参考解决方案，因此学习者必须从头开始编写自己的 `shell.c`。现在我来编写任务列表文件。清理完成。现在我来编写任务列表文件。现在我来对照教程核对文件，并修复我发现的两个问题：(a) 任务 0 的 `make` 在 `shell.c` 为空时会失败（没有 `main` 函数），(b) 最终验收的 `git` 操作步骤过于复杂。另外，还要补充说明上游的 `job-control` 部分是 `TODO`。任务清单已生成：`shell-workshop-tasks.md`。改编自上游教程 https://github.com/kamalmarhubi/shell-workshop （Kamal Marhubi, Strange Loop 2014 "Let's build a shell!"），全部 8 个 Exercise 和 "What next" 拓展都已覆盖。

**结构**：任务 0（环境）→ 任务 1–8（主线：REPL 回显 → 直接 exec 亲眼看进程被替换 → fork/exec → wait → cd 内建 → 抽出 `fork_and_exec_with_io` → 两段管道 → 任意长度管道）→ 拓展 S1–S8（重定向、`2>&1`、环境变量、export、信号、glob、后台执行）→ 最终与参考答案对拍。

改编时基于仓库实际代码做的三个关键决策：

1. **仓库自带的 `shell.c` 是完整参考答案**（REPL + 多段管道全都有），任务 0 第一步就是把它改名藏起来，自己从空文件写起，全部做完后再编译它对拍验收。
2. **`utils.c` 的 `parse_command` 只按空白切分**，不认识 `>` `<`，所以拓展任务 S1 明确要求扩展解析，验收命令 `echo hi > /tmp/f` 才能成立。
3. 上游教程的 Exercise 编号本身跳过了 5（4 直接到 6），任务 5 标题里注明了这一点，避免对教程时困惑；"Other directions" 第 7 条 job control 上游就是 TODO，无内容可改编，已注明未列入。

每个任务都带：概念（≤6 句）、步骤、可真实运行的验收命令、git commit 提交点。文件末尾附了 Claude Code 会话开场模板和三条硬规则（只改 `shell.c`、验收必须贴真实输出、卡住先提示后给码），可以直接贴进项目 `CLAUDE.md`。

使用方式：新开会话，输入 `读取 shell-workshop-tasks.md 的任务 N` 加上文件里的开场模板，一次会话推一个任务。