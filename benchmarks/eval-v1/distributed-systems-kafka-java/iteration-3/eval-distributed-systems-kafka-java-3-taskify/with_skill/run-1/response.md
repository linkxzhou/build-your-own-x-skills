The user wants me to convert a tutorial (build-your-own-kafka from GitHub) into a Claude Code executable learning task list. Let me first check the skill that matches this — "build-your-own-x" skill is explicitly for this kind of task. Let me read the SKILL.md first.

Then I need to fetch the GitHub repo to understand the tutorial structure.

Let me start by reading the skill file and fetching the repo in parallel.The GitHub page fetch got mostly navigation chrome. Let me read the rest of the SKILL.md first, and also check the skills directory for a kafka-related track skill. The skill mentions `skills/<slug>/SKILL.md` — for Kafka it would likely be "message-broker" or similar. Let me check the manifest and the skills directory.

Also I need to get the actual tutorial content. The repo is "buildthingsuseful/build-your-own-kafka". Let me fetch the README raw.README 已拿到：Java + Maven，7 个阶段构建 SimpleKafka。按 skill 路由，kafka → `distributed-systems` track skill（必读）。同时查一下有没有针对该教程的 per-tutorial skill，并抓取仓库实际代码结构。存在针对该教程的专属 skill：`distributed-systems-kafka-java`。读取它，同时重试仓库文件列表（API 返回为空，可能分支名不同）。读取 per-tutorial skill 的剩余部分和它引用的 `references/tutorial-map.md`，同时重试仓库文件树。GitHub API 限流，但 skill 明确规定：任务清单以离线 references 为准，README 已抓取一次足够。读取两个 reference 文件。材料齐了。补读 track skill 被截断的里程碑表，并检查工作区现状（concepts.md 要求先检查项目是否为空）。材料齐了：教程 README（7 阶段 + 测试）、track skill 里程碑表、per-tutorial skill 的转换规则（§5：以离线 references 为准，交付 `TASKS.md`，每项含目标/文件/概念/验证命令，回复以第一个可运行检查点结尾）。工作区为空目录，本机缺 Java/Maven（需作为 M0 前置任务，安装命令由学习者自己执行）。记录探索结论并制定计划。写入 TASKS.md 与 PROGRESS.md。已交付两个文件：

- **`TASKS.md`** — 9 个里程碑（M0–M8），每项含目标、涉及文件、核心概念、给 Claude Code 的任务、验证命令与期望输出。教程的 7 个 Stage 映射为：Stage 1→M0，Stage 2→M1，Stage 3→M2，Stage 4→M3，Stage 5→M4+M6（复制/故障转移单独成里程碑，配 track skill 的 kill-leader 检查点），Stage 6+7→M5，Stage 8→M7，另加可选 M8（Raft 延伸）。
- **`PROGRESS.md`** — 逐里程碑勾选表，验证通过才推进。

使用方式：在项目根目录对 Claude Code 说「按 TASKS.md 执行 M<n>」。每个里程碑按「讲概念 → 给骨架 → 你写核心 → 跑验证 → 复盘」的节奏进行；安装类命令由你自己执行。

一个环境事实：本机当前没有 Java 和 Maven，所以 M0 的安装命令需要你先跑。

**检查点（M0）**——执行安装后验证：

```shell
# 安装（macOS/Homebrew，自行执行）：
brew install openjdk@17 maven zookeeper

# 验证：
mvn -version
# 期望输出：Apache Maven 3.x.x，Java version: 17
```