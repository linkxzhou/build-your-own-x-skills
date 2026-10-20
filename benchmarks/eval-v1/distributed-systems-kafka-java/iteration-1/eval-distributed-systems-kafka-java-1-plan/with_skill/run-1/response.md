The user wants to learn by building a Kafka-like system from scratch in Java, based on "Building Your Own Kafka-like System From Scratch: A Step-by-Step Guide". They want me to:
1. Plan milestones
2. Create a minimal project skeleton

First, I should read the skill file as instructed: `.agents/skills/build-your-own-x/SKILL.md`. This matches the trigger (从零实现、build your own x、手写 Kafka-like system).

Let me read the skill first.The file was truncated. Let me read the rest of it, and also look for the relevant track skill. The topic is "Kafka-like system" — likely a message queue / event streaming category. Let me check the category map and find the right slug. Let me read more of the SKILL.md and list the skills directory.主题映射到 `distributed-systems` 轨道。让我阅读一下该轨道技能，并检查是否有针对该特定 Kafka 教程的技能。有一个与该教程匹配的特定教程技能：`distributed-systems-kafka-java`。让我阅读一下轨道技能的其余部分和该教程技能。我来阅读一下教程技能的其余部分和教程地图参考。Let me also check the minimal example scaffold guidance and the tutorials.md for the exact upstream link.技能上下文已加载。现在我来检查工作区状态和 Java 工具链的可用性。技能已加载。工作区是空的，并且 `java`/`javac`/`mvn`/`gradle` 都缺失了。在得出 JDK 确实缺失的结论之前，让我先检查一下是否有未链接的安装。Homebrew 中已有 JDK。我来定位一下实际的二进制文件。JDK 21 和 27 已通过 Homebrew 安装（仅 keg-only，未添加到 PATH）——无需安装，只需进行 PATH 导出。Maven/Gradle 缺失，因此骨架将使用纯 `javac`（零依赖，Maven 兼容布局），这非常适合一个仅依赖 JDK 标准库的“从零开始”项目。

让我先记录探索结果和计划。Now execute. First resolve the unknown: the exact JAVA_HOME path for openjdk@21. Homebrew keg: /opt/homebrew/opt/openjdk@21/libexec/openjdk.jdk/Contents/Home. Let me verify that quickly, then write files.

Let me start with todo s1 in progress. Actually I can batch: verify JAVA_HOME path + write README.md and PROGRESS.md in parallel. The write calls are independent of the JAVA_HOME check (README references the export command — I should confirm the path first to put the right command in the README). Let me check the path first, then write files with the correct command.JAVA_HOME 已确认。正在编写 README 和 PROGRESS。我之前在运行检查之前就预先在 `PROGRESS.md` 中填写了 PASS —— 现在将其修正为待处理状态；只有在 `verify.sh` 确实通过后，才会记录该结果。现在我来处理脚本 (s2) 和 Java 源码 (s3) —— 这些是独立的写入操作。验证通过。正在记录里程碑 0 并结束待办事项。里程碑 0 已完成并通过验证。项目在 `minikafka/`，教程出处：[Building Your Own Kafka-like System From Scratch](https://github.com/buildthingsuseful/build-your-own-kafka)（来自 build-your-own-x，Java）。

**里程碑规划**（每个都有可运行的检查点，详见 `minikafka/README.md`）：

| # | 里程碑 | 检查点 |
|---|---|---|
| 0 | 项目骨架 ✅ | `verify.sh` 输出 `VERIFY PASS` |
| 1 | 追加只读日志（segments/offset/index） | 追加 1 万条，读 offset 5000 得到正确 payload |
| 2 | Broker API（TCP/HTTP produce/fetch） | producer 发送，consumer 从指定 offset 拉取 |
| 3 | Topic + 分区（key 哈希、分区内有序） | 同 key 消息在分区内保持顺序的测试 |
| 4 | 消费者组（offset 提交、rebalance） | 2 个消费者分摊 4 个分区，重启后从提交位继续 |
| 5 | 副本（leader/follower、ISR、acks） | 杀掉 leader，follower 接管且已确认消息零丢失 |
| 6 | 故障演练（分区、慢节点、重试） | chaos 脚本 + 一致性检查通过 |
| 7 | 进阶：Raft 元数据/选主 | 3 节点随机 kill 下日志保持一致 |

**骨架内容**：零依赖、纯 `javac` 构建（Maven 兼容布局，以后想加 `pom.xml` 不用挪文件）。`scripts/env.sh` 指向你机器上已装好的 Homebrew openjdk@21——只需 `source`，无需安装任何东西。`src/main/java/minikafka/log/Log.java` 是里程碑 1 的接口桩，注释里写清了要实现的三个方法、建议的磁盘布局和必须保护的不变量。

**下一步是里程碑 1（追加只读日志）**，按惯例由你来写核心代码：

1. 新建 `minikafka/src/main/java/minikafka/log/FileLog.java` 实现 `Log` 接口
2. 先只做单 segment：`append()` 把 payload 追加写入文件并返回 offset，`read(offset)` 用记录长度定界反序列化
3. 跑检查：写个小 main 或测试，追加 1 万条后断言 `read(5000)` 等于第 5000 条 payload

写完（或卡住）随时把代码贴给我，我们从真实输出开始调试。