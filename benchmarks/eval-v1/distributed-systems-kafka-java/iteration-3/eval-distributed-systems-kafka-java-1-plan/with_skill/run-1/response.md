The user wants to learn by building a Kafka-like system from scratch in Java, based on "Building Your Own Kafka-like System From Scratch: A Step-by-Step Guide". They want me to:
1. Plan milestones
2. Create a minimal project skeleton

First, I should read the build-your-own-x skill since this matches its description exactly (从零实现, 造轮子学原理, hands-on project).

Let me read the skill first.The skill file is truncated. Let me read the rest of it, and also check the skills directory for a kafka-like track skill.Kafka 映射到 `distributed-systems` 轨道。让我读取该轨道技能，并查找是否有匹配该教程的 per-tutorial 技能。存在匹配的 per-tutorial 技能 `distributed-systems-kafka-java`。让我读取轨道技能剩余部分和该教程技能。让我读取教程映射、概念清单和最小骨架指引。技能已读完。现在检查工作区状态和本机 Java 工具链（技能要求：不代装环境，只检测已有工具）。工作区是空的，本机没有 Java 工具链。按技能要求先记录探索笔记，再规划。技能与上下文已确认。现在制定计划并落地骨架。骨架已就位，8 个文件全部在 `my-kafka/` 下，包名与目录一致，`build.sh` 语法检查通过。

**里程碑规划**（详见 `my-kafka/TASKS.md`，进度记 `PROGRESS.md`）：

| # | 里程碑 | 通过标准 |
|---|---|---|
| M0 | 项目骨架 ✅ | 编译运行入口程序 |
| M1 | Append-only log | 追加 1 万条后按 offset 读回正确 payload |
| M2 | Broker API | producer 发送、consumer 从 offset 拉取 |
| M3 | Topics + partitions | 同 key 消息分区内有序 |
| M4 | Consumer groups | 2 消费者分摊 4 分区，重启从提交位点续读 |
| M5 | Replication | kill leader 后 follower 接管，零丢失 |
| M6 | Failure testing | chaos 脚本 + 一致性检查通过 |
| M7 | Stretch: Raft | 3 节点随机 kill 下日志一致 |

**骨架内容**：
- `build.sh` — 纯 javac 构建（本机无 Maven/Gradle 也能跑），源码树保持 Maven 风格，之后迁移只需加一个 `pom.xml`
- `src/main/java/com/example/kafka/Main.java` — 入口，M0 只打印一行
- `src/main/java/com/example/kafka/log/Log.java` — M1 骨架，7 个 TODO（帧编码、段滚动、稀疏索引、按 offset 读），等你来填
- `scratch/` — 实验脚本和日志都放这里，留在项目内

教程原文：https://github.com/buildthingsuseful/build-your-own-kafka

本机没有 JDK，按规则我不代装。请先安装（macOS）：

```bash
brew install openjdk@17
sudo ln -sfn $(brew --prefix)/opt/openjdk@17/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-17.jdk
```

**检查点（M0）**：

```bash
cd my-kafka && ./build.sh && java -cp out com.example.kafka.Main
```

预期输出：

```
build OK -> out/
my-kafka skeleton OK
```

跑通后把结果告诉我，我们进入 M1：先讲段文件与稀疏索引的原理，然后你按 `Log.java` 里的 TODO 逐个填空。