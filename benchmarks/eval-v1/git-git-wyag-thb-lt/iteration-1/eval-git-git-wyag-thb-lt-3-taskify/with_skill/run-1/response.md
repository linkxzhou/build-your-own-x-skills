The user wants me to convert the "Write yourself a Git!" tutorial (wyag.thb.lt) into a Claude Code learning task list. This matches the build-your-own-x skill — the user wants a hands-on project to learn by rebuilding Git from scratch. Let me first read the skill file as instructed.

The trigger: "请基于 https://wyag.thb.lt/ 转换成 Claude Code 学习任务清单" — they want to learn by building their own Git. This is clearly the build-your-own-x skill territory. Let me read the SKILL.md first.Let me read the rest of the SKILL.md file to see the category map and find the git slug.主题是 Git，slug 是 `git`。用户指定了 wyag 教程，所以我来检查一下 track skill 和 per-tutorial skill。The skills are nested under `.agents/skills/build-your-own-x/skills/`. Let me read the git track skill and check for a wyag-specific skill.有一个 wyag 专用的技能。让我来阅读它。它引用了 `references/tutorial-map.md`。我来找一下并阅读它。我已经掌握了完整的技能上下文。现在让我获取实际的 wyag 教程结构，以便任务列表能够忠实地映射到其各个章节。我已经获取了完整的 wyag 目录。让我检查一下该技能附带的最小示例，然后编写任务列表。我已经准备好所需的一切：路由技能、git 跟踪技能、wyag 特定技能，以及 wyag 的实际目录（10 个章节，命令：`init`、`hash-object`、`cat-file`、`log`、`ls-tree`、`checkout`、`show-ref`、`tag`、`rev-parse`、`ls-files`、`check-ignore`、`status`、`rm`、`add`、`commit`）。现在我将编写任务列表文件。文件已写入。我来确认一下它是否完整且格式正确。任务清单已生成：`wyag-claude-code-tasks.md`（184 行）。

**结构**：把 wyag 教程的 10 章压缩成 8 个 Milestone（0–7）+ 1 个选做进阶项，每个 Milestone 都带目标、核心概念、子任务 checklist 和可与真 git 对照的验收命令：

| Milestone | 教程章节 | 命令 | 验收锚点 |
|---|---|---|---|
| 0 骨架 | §1–2 | argparse 分发 | `--help` 可用 |
| 1 init | §3 | `init` | 真 git 认识你建的仓库 |
| 2 对象 | §4 | `hash-object` / `cat-file` | sha 与 `git hash-object` 完全一致 |
| 3 log | §5 | `log` | sha 序列与 `git log` 一致 |
| 4 树/检出 | §6 | `ls-tree` / `checkout` | `diff -r` 两工作区一致 |
| 5 引用 | §7 | `show-ref` / `tag` / `rev-parse` | `git show v1.0` 能解析你的 tag |
| 6 索引只读 | §8 | `ls-files` / `check-ignore` / `status` | 与 `git status --porcelain` 一致 |
| 7 暂存提交 | §9 | `rm` / `add` / `commit` | 全程用 wyag 提交，`git fsck` 干净 |

**设计要点**：

- 文件开头有一段可直接粘贴给 Claude Code 的「全局规则」：一次只做一个 Milestone、先讲概念再给骨架、核心逻辑留给你写、每个 Milestone 结束必须跑验收并记录到 `PROGRESS.md`。这是防止 Claude Code 直接把整个 wyag 抄给你的关键约束。
- 每个 Milestone 附标准开场 prompt，新会话直接复制即可续接进度。
- 验收全部以真 git 为对照标准（sha 相等、`git fsck` 干净、`--porcelain` 输出一致），这是这类项目最可靠的正确性检查。
- 语言默认 Python 3 标准库（wyag 原文即 Python，零依赖）；结尾附 5 道自查题，覆盖对象寻址、tree 排序、index stat 字段、分支 vs 标签的存储差异等教程核心概念。

教程原文：https://wyag.thb.lt/ （Stephen Dolan, CC BY-NC-SA）。下一步从 Milestone 0 开始：建目录、把清单文件放进去、开一个 Claude Code 会话贴入全局规则。