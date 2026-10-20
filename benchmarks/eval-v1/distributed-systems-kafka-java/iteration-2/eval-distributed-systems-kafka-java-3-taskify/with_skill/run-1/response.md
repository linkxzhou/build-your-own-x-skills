The user wants me to convert a tutorial from GitHub (build-your-own-kafka) into a Claude Code executable learning task list. Let me first fetch the repository to understand what the tutorial contains.

Let me start by fetching the GitHub repo to see what it's about.这项任务符合 `build-your-own-x` 技能。让我加载它，并同时获取实际的教程内容。该技能指向一个轨道技能。让我阅读 SKILL.md 的其余部分，检查是否存在 Kafka 相关的轨道技能，并获取详细的 Medium 文章。有一个完全匹配的教程技能 `distributed-systems-kafka-java`。根据技能工作流，我将首先阅读轨道技能，然后阅读教程技能。让我阅读教程技能的其余部分及其参考文件。技能的转换工作流（`distributed-systems-kafka-java/SKILL.md:67-74`）要求以离线参考为事实来源，README 只补充缺失细节（已获取一次，拿到了 stage 结构和运行命令）。还差轨道技能里程碑表的第 6-8 行，补齐后即可写任务清单。参考资料齐了：教程 8 个 stage、运行命令、5 组核心概念，加上轨道技能的检查点标准。按技能的转换流程写 `TASKS.md`（每个任务含目标、概念、涉及文件、Claude Code 提示词、验证命令与期望输出），并附 `PROGRESS.md` 供逐项打卡。验证产物一致性：jar 名、类名、测试名在 TASKS.md 与 PROGRESS.md 之间必须完全一致，且教程原始命令逐字保留。已生成两份文件：

- **`TASKS.md`** — 9 个任务（T1–T8 对应教程 Stage 1–8，T9 为可选拉伸），每项含目标、涉及文件、核心概念、一段可直接粘贴给 Claude Code 的提示词、验证命令与期望输出。教练模式约定写在文件开头：Claude 讲概念、给骨架，核心逻辑由你写，通过验证才进下一关。
- **`PROGRESS.md`** — 打卡表，每关通过后由 Claude Code 记录命令与结果。

任务与教程的对应关系：T1 骨架 → T2 二进制协议 → T3 ZooKeeper/controller 选举 → T4 日志分段与索引 → T5 broker 复制与故障转移 → T6 元数据发现 → T7 高层 Producer/Consumer → T8 端到端验收 + 杀 leader/杀 controller 演练。教程的 5 组「Testing 要点」在文末有概念对照表，全部落到具体任务。jar 名、类名、测试名已与教程原始命令逐字核对一致。

第一个可运行检查点（T1，在项目目录执行）：

```shell
mvn clean package
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.Main
```

看到 `BUILD SUCCESS` 且第二条命令打印骨架启动信息，T1 即通过，把结果记入 `PROGRESS.md` 后进入 T2。