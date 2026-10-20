The user wants to learn and implement a Kafka-like system from scratch in Java, based on the guide "Building Your Own Kafka-like System From Scratch: A Step-by-Step Guide". They want me to:
1. Plan milestones
2. Create a minimal project skeleton

Let me first check the workspace to see what's there. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-distributed-systems-kafka-java-1`. Let me explore what exists.

I should:
1. Look at the workspace contents
2. Maybe search for the guide to understand what steps it covers
3. Plan milestones
4. Create minimal project skeleton

Let me start by exploring the workspace and searching for the guide in parallel.The workspace is empty. The web search found nothing. Let me try another search to find the guide.Interesting - no Java runtime installed. Let me check for other Java installations (e.g., via homebrew, SDKMAN, etc.).

Also, the guide search failed. Let me try a different search. The guide might be from a specific blog. Let me search variations.There are JDKs installed via homebrew: openjdk, openjdk@21, openjdk@27. But they're not linked. `/usr/bin/java` exists but says "Unable to locate a Java Runtime" — that's the stub. Let me check the homebrew JDK paths directly.

Also web search isn't finding the guide. The guide title "Building Your Own Kafka-like System From Scratch: A Step-by-Step Guide" — this might be a specific blog post. Let me try one more search, maybe on GitHub or specific sites. Actually, there's a well-known repo "build-your-own-x" on GitHub. The workspace name is "build-your-own-x-distributed-systems-kafka-java-1" which suggests it's from the build-your-own-x list, distributed systems section, Kafka, Java.

Let me check the homebrew JDKs and try to find the guide.JDK 21 (LTS) 已通过 Homebrew 安装。现在让我查看 build-your-own-x 列表以找到实际的指南链接。找到了指南：`buildthingsuseful/build-your-own-kafka`。我来阅读一下它的 README，以便根据实际内容来规划里程碑。页面抓取返回的内容大多是导航信息。我来获取原始的 README。指南结构已明确。我先检查一下参考仓库的包结构，以便骨架与指南保持一致。GitHub API rate limited. I have enough info from the README though: the guide uses:
- Maven, artifact `simple-kafka-1.0-SNAPSHOT.jar`
- Package `com.simplekafka`
- Classes: `com.simplekafka.broker.SimpleKafkaBroker`, `com.simplekafka.client.SimpleKafkaProducer`, `com.simplekafka.client.SimpleKafkaConsumer`
- Stages: 1. project structure, 2. core protocol layer, 3. Zookeeper integration, 4. storage layer, 5. broker, 6. client library, 7. higher-level producer/consumer APIs, 8. testing
- Broker args: brokerId, host, port, zkPort
- Uses ZooKeeper for coordination

That's enough to plan milestones and create a minimal skeleton. The user asked: "请先帮我规划里程碑并创建最小项目骨架" — plan milestones and create minimal project skeleton.

So my deliverables:
1. Milestone plan (mapped to the guide's stages 1-7 + testing)
2. Minimal project skeleton: Maven pom.xml, directory structure, package structure with stub classes (protocol, zookeeper, storage, broker, client), a README documenting milestones, .gitignore.

Since no Maven installed, I should note that. I can still create the skeleton. Should I install maven? The user asked for skeleton creation; compiling would be nice to verify. Maven isn't installed. Options: use brew install maven (takes time, modifies system — that's a system-level install; it's reasonably safe but let me consider). Actually, I could verify compilation with javac directly using the JDK 21. The skeleton with stubs can be compiled with javac to verify syntax. That's a good verification without installing Maven.

Actually, let me think about whether to install maven via brew. The user will need Maven eventually (guide says `mvn clean package`). Installing via brew is a system change — moderately reversible (brew uninstall). I'd rather ask or just note it. Hmm, "Executing actions with care" — installing a package via brew is common but takes time. Let me first create the skeleton, verify with javac, and tell the user to `brew install maven` (or I can offer). Actually the instruction says don't stage next-step menus. I can just note: Maven 未安装，运行 `brew install maven` 后即可 `mvn clean package`. That's naming the next action directly, which is fine.

Alternatively, I could install maven myself. It's a local dev tool install, fairly standard. But it can take a while and download a lot. I'll leave it to the user, or actually... let me just try installing it quickly? Hmm. The user asked to "create minimal project skeleton" — verification via javac is enough. I'll note the maven install command.

Now the plan. Per my instructions: explore → plan → todo_write → execute → verify. I've explored (workspace empty, guide found, JDK available). Let me call `explore` to record findings, then `plan`, then create files.

Milestone plan (mapped to guide stages):

- M0 (Stage 1): 项目骨架 — Maven 项目、包结构、协议常量、可编译运行
- M1 (Stage 2): 核心协议层 — 二进制协议：消息格式、请求/响应编解码 (ProtocolConstants, Message, Request/Response codecs)
- M2 (Stage 3): ZooKeeper 集成 — broker 注册、controller 选举、元数据存储 (ZooKeeperClient, /brokers, /controller, /topics)
- M3 (Stage 4): 存储层 — Log segment、索引、offset 管理 (Log, LogSegment, OffsetIndex)
- M4 (Stage 5): Broker — 网络层 (SocketServer)、请求处理、分区/副本管理、leader/follower 同步、controller 故障转移
- M5 (Stage 6): 客户端库 — 连接管理、协议封装、元数据发现
- M6 (Stage 7): 高层 Producer/Consumer API — SimpleKafkaProducer (round-robin 分区), SimpleKafkaConsumer (poll, offset commit)
- M7 (Stage 8): 端到端测试 — 3 broker 集群、produce/consume、kill leader 验证 failover

Skeleton structure:

```
simple-kafka/
├── pom.xml
├── .gitignore
├── README.md            (里程碑计划 + 运行说明)
├── docs/
│   └── MILESTONES.md    (详细里程碑)
└── src/
    ├── main/java/com/simplekafka/
    │   ├── common/          (协议常量、消息模型)
    │   │   ├── ProtocolConstants.java
    │   │   └── Message.java
    │   ├── protocol/        (编解码器)
    │   │   ├── MessageCodec.java
    │   │   ├── RequestDecoder.java / ...
    │   ├── zookeeper/       (ZK 集成)
    │   │   └── ZooKeeperClient.java
    │   ├── storage/         (存储层)
    │   │   ├── Log.java
    │   │   ├── LogSegment.java
    │   │   └── OffsetIndex.java
    │   ├── broker/          (broker)
    │   │   ├── SimpleKafkaBroker.java
    │   │   ├── BrokerServer.java / SocketServer
    │   │   ├── Partition.java
    │   │   ├── ReplicaManager.java
    │   │   └── Controller.java
    │   └── client/          (客户端)
    │       ├── SimpleKafkaProducer.java
    │       ├── SimpleKafkaConsumer.java
    │       └── NetworkClient.java
    └── test/java/com/simplekafka/...
```

Dependencies: ZooKeeper client (org.apache.zookeeper:zookeeper:3.8.x). For minimal skeleton, stubs only — classes compile, main methods print usage. Keep stubs minimal but meaningful: each class with TODO comments pointing to milestone.

Wait — should the skeleton include the zookeeper dependency? The guide uses ZooKeeper. Adding the dependency in pom now is fine (it's needed at M2). For skeleton, include it so pom is stable. zookeeper 3.9.x has log4j deps issues; use zookeeper 3.8.4 with slf4j. Actually org.apache.zookeeper:zookeeper:3.8.4 pulls in slf4j-api, logback? It has slf4j-api and requires a binding; add slf4j-simple to avoid warnings. Keep it simple.

Also JUnit 5 for tests.

Java version: 21 (LTS, installed). pom: maven.compiler.release 21.

For the skeleton classes, minimal but compilable:

- `ProtocolConstants.java`: magic byte, request/response type constants, op codes.
- `Message.java`: topic, partition, offset, key, value, timestamp, crc. With encode/decode? That's M1 — keep as model with fields + toString, TODO for codec.
- `MessageCodec.java`: static encode/decode stubs throwing UnsupportedOperationException? Hmm, stubs that throw are fine for skeleton, but maybe better to leave TODO comments with empty bodies? For a "minimal skeleton", I'd make classes with fields/constructor and TODO markers. Compilable.

Actually, let me make the skeleton genuinely runnable in a trivial sense: SimpleKafkaBroker main parses args (brokerId host port zkPort) and prints "starting..." with TODO. Producer/Consumer main parse args similarly. That matches the guide's CLI contract so the user can run them from day one.

Also a test: simple test that ProtocolConstants values are as expected, or Message model test — to verify `mvn test` works. But without maven installed I can't run it. I can compile with javac (need junit? no — skip test compile with javac, just compile main sources).

Let me also write README.md with milestones and quick start, and docs/MILESTONES.md with detailed milestone breakdown including acceptance criteria per milestone.

Also .gitignore: target/, .idea, *.iml, .DS_Store.

Should I git init? The workspace is empty (no .git). Creating a git repo is reasonable for a from-scratch project. Let me check if git is available and init + initial commit? Committing is a local reversible action. I'd say init the repo and make an initial commit — helpful. Actually, let me be careful: user may want their own git history. A minimal skeleton with git init is standard. I'll do git init and one initial commit, mentioning it. Hmm, or leave git init but no commit? I'll do init + commit; it's local and reversible.

Actually wait — is the workspace itself meant to be the project root? Workspace: /Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-distributed-systems-kafka-java-1 — empty. Yes, use workspace root as project root.

Let me now:
1. explore (record findings)
2. plan (with seed_todos)
3. create files
4. verify with javac compile
5. git init + commit
6. summarize milestones in chat

For the pom, artifactId simple-kafka, version 1.0-SNAPSHOT (matches guide's jar name simple-kafka-1.0-SNAPSHOT.jar), groupId com.simplekafka.

Final name in build: simple-kafka-1.0-SNAPSHOT.jar — default jar naming is ${artifactId}-${version}.jar = simple-kafka-1.0-SNAPSHOT.jar. Good.

ZooKeeper dependency: org.apache.zookeeper:zookeeper:3.8.4, with exclusions for log4j? zookeeper 3.8 depends on slf4j-api, logback? Let me recall: zookeeper 3.8.x has dependencies: slf4j-api, logback-classic? Actually zookeeper 3.8.4 pom includes io.dropwizard.metrics, logback... I think zookeeper 3.8 uses logback 1.2.13? Hmm. To be safe add exclusion of log4j and log4j-core? ZooKeeper 3.8 moved to logback. There's a known issue: zookeeper 3.8 depends on ch.qos.logback. Fine either way — it'll resolve. Add slf4j-simple? If logback comes transitively, slf4j-simple conflicts (multiple bindings warning, still works). Keep pom minimal: zookeeper + junit. If there are warnings, fine.

Actually for a skeleton, maybe I shouldn't even add zookeeper yet — M2 needs it. But adding now avoids pom churn. I'll add it now with a comment.

Netty: zookeeper client needs netty for some transports but 3.8 default NIO works without netty? The zookeeper jar has NIO client. Fine.

Let me write the files now.

pom.xml:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.simplekafka</groupId>
  <artifactId>simple-kafka</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>simple-kafka</name>
  <description>A Kafka-like distributed messaging system built from scratch (learning project)</description>

  <properties>
    <maven.compiler.release>21</maven.compiler.release>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <zookeeper.version>3.8.4</zookeeper.version>
    <junit.version>5.10.2</junit.version>
  </properties>

  <dependencies>
    <dependency>
      <groupId>org.apache.zookeeper</groupId>
      <artifactId>zookeeper</artifactId>
      <version>${zookeeper.version}</version>
      <exclusions>
        <exclusion>
          <groupId>org.slf4j</groupId>
          <artifactId>slf4j-log4j12</artifactId>
        </exclusion>
        <exclusion>
          <groupId>log4j</groupId>
          <artifactId>log4j</artifactId>
        </exclusion>
      </exclusions>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-simple</artifactId>
      <version>2.0.13</version>
    </dependency>
    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>${junit.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.2.5</version>
      </plugin>
    </plugins>
  </build>
</project>
```

Hmm, zookeeper 3.8.4 exclusions: slf4j-log4j12 doesn't exist in 3.8 (that was 3.4/3.5). Harmless to exclude. Actually exclusions of non-existent deps are fine.

Wait, zookeeper 3.8.4 — does it exist? ZooKeeper releases: 3.8.0...3.8.4 (yes, 3.8.4 released April 2024). 3.9.x also exists. OK.

slf4j-simple 2.0.13 exists. zookeeper 3.8.4 uses slf4j-api 2.0.x? It uses slf4j-api 1.7.30? Hmm, zookeeper 3.8 uses slf4j 1.7. slf4j-simple 2.0 with slf4j-api 1.7 → binding mismatch (slf4j 2 bindings use ServiceLoader; slf4j-api 1.7 uses StaticLoggerBinder). If zookeeper pulls slf4j-api 1.7.30 and I add slf4j-simple 2.0.13, the binding won't be picked up by 1.7 API → "Failed to load class StaticLoggerBinder" warning, NOP logger. To be safe, use slf4j-simple 1.7.36 which works with both 1.7 API (StaticLoggerBinder present in 1.7.36) — yes slf4j-simple 1.7.36 works with slf4j-api 1.7. And if maven resolves slf4j-api to 2.0 (nearest wins — my direct slf4j-simple 1.7.36 depends on slf4j-api 1.7.36), fine.

Actually simpler: don't add slf4j binding at all; zookeeper 3.8.4 transitively includes logback-classic? Let me think... zookeeper 3.8.0 pom: dependencies include org.slf4j:slf4j-api:1.7.30, ch.qos.logback:logback-classic? I believe zookeeper 3.8 does include logback-classic 1.2.x as runtime dep. Hmm, not 100% sure. If no binding, we get a warning but code works. For skeleton, warnings are acceptable but ugly. I'll add slf4j-simple 1.7.36 — safe with 1.7 API. If zookeeper brings logback too, multiple bindings → SLF4J picks one with a warning. Meh.

Alternative: exclude nothing, add slf4j-simple 1.7.36. Good enough for a learning project.

Actually, let me reconsider: maybe keep the pom truly minimal for the skeleton — just junit — and add zookeeper at M2. The user said "最小项目骨架" (minimal project skeleton). Minimal = junit only? But then pom changes at M2. I think including zookeeper now with a comment "used from M2 (Stage 3)" is helpful and stable. I'll include it.

Hmm, but "minimal" — I'll include it; it's one dependency and the guide's stage 3 needs it immediately.

Now the Java stubs. Package com.simplekafka with subpackages: common, protocol, zookeeper, storage, broker, client.

Files:

1. common/ProtocolConstants.java
```java
package com.simplekafka.common;

/**
 * M1 (Stage 2): 核心协议层 —— 二进制协议常量。
 */
public final class ProtocolConstants {
    private ProtocolConstants() {}

    /** 协议魔数，用于快速校验报文 */
    public static final int MAGIC_BYTE = 0x5AF4; // "SimpleKafka"

    // ---- 请求类型 ----
    public static final byte REQ_PRODUCE = 0;
    public static final byte REQ_FETCH = 1;
    public static final byte REQ_METADATA = 2;
    public static final byte REQ_CREATE_TOPIC = 3;
    public static final byte REQ_JOIN_GROUP = 4; // follower 副本同步/注册

    // ---- 响应类型 ----
    public static final byte RESP_PRODUCE = 100;
    ...
}
```

Hmm, keep it small: magic, request types, error codes.

2. common/Message.java — model with fields: topic, partition, offset, timestamp, key, value; constructor, getters, toString. TODO: crc + codec in M1.

3. protocol/MessageCodec.java — static encode(Message)/decode(byte[]) stubs with TODO, throwing UnsupportedOperationException("M1").

Hmm — throwing stubs means the classes compile but fail at runtime; that's the point of a skeleton. OK.

Actually, maybe better: leave them as TODO with `throw new UnsupportedOperationException("TODO(M1): ...")`. Clear contract.

4. protocol/RequestCodec.java + ResponseCodec? Keep one file protocol/Codecs? Minimal: MessageCodec only, plus a note. I'll add RequestDecoder/ResponseEncoder? Too much. Minimal skeleton: protocol/MessageCodec.java and protocol/RequestType.java? RequestType already in constants. Just MessageCodec.

5. zookeeper/ZooKeeperClient.java — wrapper holding ZooKeeper handle, TODO methods: registerBroker, electController, createTopicAssignment, watchBrokers. Constructor takes connectString. Stub with TODOs.

6. storage/LogSegment.java, storage/Log.java, storage/OffsetIndex.java — stubs. Log with baseDir, topicPartition; append(Message) TODO; read(offset, maxBytes) TODO.

7. broker/SimpleKafkaBroker.java — main class matching guide CLI: args brokerId host port zkPort. Fields, start() TODO, main parses args and prints startup plan. Make it actually construct the object and print "TODO(M4)". Runnable without crashing? If start() throws UnsupportedOperation, running it crashes. Better: main parses args, prints config, and logs "skeleton: broker logic lands in M4". That way `java -cp ... SimpleKafkaBroker 1 localhost 9091 2181` works today.

8. broker/Partition.java, broker/ReplicaManager.java, broker/Controller.java — stubs (M4).

9. client/NetworkClient.java — connection wrapper stub (M6).
10. client/SimpleKafkaProducer.java — main: args host port topic; sends a few messages TODO (M5/M7). Print skeleton message.
11. client/SimpleKafkaConsumer.java — main: args host port topic partition; TODO.

12. test: com/simplekafka/common/MessageTest.java — construct Message, assert getters. Trivial but proves mvn test wiring. And maybe ProtocolConstantsTest. One test file is enough.

13. README.md — project intro, milestones table, quick start (mvn, zk, broker/producer/consumer commands from the guide), JDK note (brew install maven; JDK21 via homebrew path).

14. docs/MILESTONES.md — detailed milestone plan M0-M7 with goals, tasks, acceptance criteria, mapped to guide stages 1-8.

15. .gitignore.

Also maybe scripts/? Not needed.

Let me also think about whether to set JAVA_HOME for javac verification: /opt/homebrew/opt/openjdk@21. javac compile all main sources to a temp dir:

```
JAVA_HOME=/opt/homebrew/opt/openjdk@21
$JAVA_HOME/bin/javac -d /tmp/sk-build $(find src/main/java -name '*.java')
```

That verifies compilation. Tests need junit jar — skip; or download junit? Skip, note that mvn test will verify.

Git init + commit: do it.

Now milestone plan content. Map guide stages to milestones with acceptance criteria:

- M0 骨架 (Stage 1): Maven 项目 + 包结构 + 可编译 + CLI 可运行。验收: mvn clean package 成功；三个 main 类按指南命令可运行。
- M1 协议层 (Stage 2): Message 二进制格式 (magic, crc32, timestamp, key, value, 长度前缀帧)；Request/Response 编解码。验收: codec 单元测试 round-trip；损坏数据 CRC 校验失败。
- M2 ZooKeeper 集成 (Stage 3): broker 注册 (/brokers/ids/{id})、controller 选举 (/controller ephemeral)、topic 分区分配元数据 (/brokers/topics/{topic})、watch 机制。验收: 启动 3 broker，ZK 中可见注册信息；杀掉 controller 后新 controller 产生。
- M3 存储层 (Stage 4): LogSegment (追加写 .log)、OffsetIndex (稀疏索引 offset→position)、Log (segment 滚动、按 offset 读)。验收: 单元测试 append/read round-trip、重启后恢复 offset、索引查找。
- M4 Broker (Stage 5): SocketServer (NIO 或线程池)、请求分发、Partition/ReplicaManager、leader/follower 复制、controller 故障转移。验收: 3 broker 集群创建 topic 分区副本分布；kill leader 后 follower 接管，已确认消息不丢。
- M5 客户端库 (Stage 6): NetworkClient (连接池、请求/响应关联、metadata 发现)、协议封装。验收: 客户端通过 metadata 找到分区 leader 并直连。
- M6 高层 API (Stage 7): Producer (分区选择 round-robin、acks、批量/重试可选)、Consumer (poll、offset 提交、从指定 offset 消费)。验收: produce N 条 → consume 恰好 N 条且有序。
- M7 端到端测试 (Stage 8): 集成测试脚本/测试类：3 broker + zk，produce/consume，failover 场景。验收: 指南"Testing the System"全流程跑通。

Order note: guide's stage order is protocol → zookeeper → storage → broker → client. I'll follow the guide's order exactly (user wants to follow the guide). Good.

Now, per instructions, I should call explore first to record findings, then plan. Let me do explore + plan. Actually explore is meant to be called before editing code, recording files read or planned. I've read: workspace (empty), guide README (via curl), JDK check. Let me record that.

Then plan with seed_todos=true, then execute: write files, verify javac, git init/commit.

Let me write all the file contents carefully.

Message.java:

```java
package com.simplekafka.common;

import java.util.Arrays;

/**
 * 系统中的基本消息单元（M1 将为其实现二进制编解码）。
 */
public class Message {
    private final String topic;
    private final int partition;
    private long offset = -1;          // 由 broker 存储层分配
    private final long timestamp;
    private final byte[] key;          // 可为 null
    private final byte[] value;

    public Message(String topic, int partition, long timestamp, byte[] key, byte[] value) {...}

    getters...

    @Override public String toString() ...
}
```

Keep it compact.

MessageCodec stub:

```java
package com.simplekafka.protocol;

import com.simplekafka.common.Message;

/**
 * M1 (Stage 2): 消息的二进制编解码。
 *
 * 目标帧格式（长度前缀帧）:
 * [4B frameLength][2B magic][4B crc32][8B timestamp][4B keyLen][key][4B valueLen][value]
 * topic/partition/offset 属于请求头或存储元数据，不进入消息帧。
 */
public final class MessageCodec {
    private MessageCodec() {}

    public static byte[] encode(Message message) {
        throw new UnsupportedOperationException("TODO(M1): 实现消息编码");
    }

    public static Message decode(byte[] frame) {
        throw new UnsupportedOperationException("TODO(M1): 实现消息解码");
    }
}
```

ZooKeeperClient stub:

```java
package com.simplekafka.zookeeper;

import org.apache.zookeeper.ZooKeeper;

import java.io.IOException;

/**
 * M2 (Stage 3): ZooKeeper 集成。
 *
 * 元数据布局（参考 Kafka 旧版 ZK 协议）:
 *   /simplekafka/brokers/ids/{brokerId}        -> ephemeral，broker 注册
 *   /simplekafka/controller                    -> ephemeral，controller 选举
 *   /simplekafka/topics/{topic}                -> persistent，分区副本分配
 */
public class ZooKeeperClient {
    private final ZooKeeper zk;

    public ZooKeeperClient(String connectString, int sessionTimeoutMs) throws IOException {
        // TODO(M2): 创建 ZooKeeper 会话，处理连接建立前的同步等待
        this.zk = new ZooKeeper(connectString, sessionTimeoutMs, event -> {});
    }

    /** TODO(M2): broker 启动时注册 ephemeral 节点 /brokers/ids/{id} */
    public void registerBroker(int brokerId, String host, int port) {
        throw new UnsupportedOperationException("TODO(M2)");
    }
    ...
}
```

Hmm, creating ZooKeeper in constructor with empty watcher is fine.

Storage stubs:

LogSegment:
```java
package com.simplekafka.storage;

import java.io.File;

/**
 * M3 (Stage 4): 单个日志段文件 (.log) 及其配套索引 (.index)。
 */
public class LogSegment {
    private final File logFile;
    private final File indexFile;
    private final long baseOffset;

    public LogSegment(File dir, long baseOffset) {
        this.logFile = new File(dir, baseOffset + ".log");
        this.indexFile = new File(dir, baseOffset + ".index");
        this.baseOffset = baseOffset;
    }

    /** TODO(M3): 追加一条消息，返回分配给它的 offset */
    public long append(byte[] frame) { throw new UnsupportedOperationException("TODO(M3)"); }

    /** TODO(M3): 从指定文件位置读取一帧 */
    public byte[] readAt(long position) { throw new UnsupportedOperationException("TODO(M3)"); }
    ...
}
```

Log:
```java
public class Log {
    // TODO(M3): segment 滚动（按大小）、nextOffset 恢复、read(offset)
}
```

OffsetIndex:
```java
public class OffsetIndex {
    // TODO(M3): 稀疏索引，相对 offset -> 物理位置，二分查找
}
```

Maybe make these classes with fields + TODO methods minimal. Keep each small.

Broker:

SimpleKafkaBroker:
```java
package com.simplekafka.broker;

import java.util.logging.Logger; // or System.out

/**
 * M4 (Stage 5): broker 主入口。
 *
 * 用法（与指南一致）:
 *   java -cp simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.broker.SimpleKafkaBroker <brokerId> <host> <port> <zkPort>
 */
public class SimpleKafkaBroker {
    private final int brokerId;
    private final String host;
    private final int port;
    private final int zkPort;

    public SimpleKafkaBroker(int brokerId, String host, int port, int zkPort) {...}

    public void start() {
        // TODO(M2): 向 ZooKeeper 注册自己
        // TODO(M4): 启动 SocketServer、加载/创建 Log、参与 controller 选举、副本同步
        System.out.printf("[broker-%d] skeleton 启动于 %s:%d (zk:%d) —— broker 逻辑在 M4 实现%n", ...);
    }

    public static void main(String[] args) {
        if (args.length != 4) { System.err.println("Usage: SimpleKafkaBroker <brokerId> <host> <port> <zkPort>"); System.exit(1); }
        new SimpleKafkaBroker(Integer.parseInt(args[0]), args[1], Integer.parseInt(args[2]), Integer.parseInt(args[3])).start();
    }
}
```

Should start() block? In real broker it blocks forever. For skeleton, print and return. Fine.

Also stub: broker/SocketServer.java? Add as TODO class with comment. Minimal: I'll include SocketServer, Partition, ReplicaManager, Controller as tiny stubs with TODO comments. Hmm, "Don't create files unless absolutely necessary" — but a skeleton's purpose is the structure; the guide's stages reference these components. I think 4 tiny stubs are justified as the skeleton IS the deliverable. Keep each ≤ 20 lines.

Actually, let me trim: broker package gets SimpleKafkaBroker (functional CLI) + Controller + Partition + ReplicaManager + SocketServer stubs. client gets NetworkClient stub + Producer/Consumer CLIs. That's reasonable.

Producer:
```java
package com.simplekafka.client;

/**
 * M5/M6 (Stage 6/7): 客户端库与高层 Producer API。
 *
 * 用法（与指南一致）:
 *   java -cp simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.client.SimpleKafkaProducer <host> <port> <topic>
 */
public class SimpleKafkaProducer {
    public static void main(String[] args) {
        if (args.length != 3) { usage; exit; }
        String host = args[0]; int port = ...; String topic = args[2];
        // TODO(M6): 循环发送消息到 topic（round-robin 选分区）
        System.out.printf("[producer] skeleton: host=%s port=%d topic=%s —— 发送逻辑在 M6 实现%n", ...);
    }
}
```

Consumer similar with partition arg.

NetworkClient stub:
```java
/**
 * M5 (Stage 6): 客户端网络层 —— 连接管理、请求/响应关联、metadata 发现。
 */
public class NetworkClient {
    // TODO(M5): connect/send/recv，按 correlationId 关联响应
}
```

Hmm, an empty class with only comments compiles fine.

Test file:

```java
package com.simplekafka.common;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class MessageTest {
    @Test
    void shouldCarryTopicKeyAndValue() {
        Message m = new Message("test-topic", 0, 42L, "k".getBytes(), "v".getBytes());
        assertEquals("test-topic", m.topic());
        assertEquals(0, m.partition());
        assertEquals(42L, m.timestamp());
        assertArrayEquals("k".getBytes(), m.key());
        assertArrayEquals("v".getBytes(), m.value());
        assertEquals(-1, m.offset());
    }
}
```

Use record-like accessors? I'll write a plain class with getX() or record-style topic()? Java 21 — could use a record! Message as record with offset mutable? offset is assigned by broker later. Could do record Message(String topic, int partition, long timestamp, byte[] key, byte[] value) and offset handled separately... Simpler: plain class with getters named topic(), partition() etc. (record-style). Or just use a record and keep offset out of the message (offset assigned by storage layer, returned from append). Actually that's cleaner design: Message = immutable payload; broker assigns offset. The guide likely has offset in message. For skeleton, record with offset included as mutable field is awkward. I'll do a plain class with standard getters (getTopic() etc.) — most tutorial-friendly. Hmm, records are idiomatic modern Java. But offset assignment... I'll keep plain class with getters getTopic(), getOffset() with setter setOffset(long) package-private? Public setter is fine for learning code.

Decision: plain class, fields, constructor(topic, partition, timestamp, key, value), getters, setOffset, toString, equals/hashCode skip (arrays). Keep simple.

README.md content:

# SimpleKafka — 从零实现 Kafka-like 系统（Java 学习项目）

基于指南: Building Your Own Kafka-like System From Scratch (buildthingsuseful/build-your-own-kafka)

## 里程碑 (docs/MILESTONES.md 有详细验收标准)

| 里程碑 | 对应指南 | 内容 | 状态 |
|---|---|---|---|
| M0 | Stage 1 | 项目骨架 | ✅ |
| M1 | Stage 2 | 核心协议层 | ⬜ |
| M2 | Stage 3 | ZooKeeper 集成 | ⬜ |
| M3 | Stage 4 | 存储层 | ⬜ |
| M4 | Stage 5 | Broker | ⬜ |
| M5 | Stage 6 | 客户端库 | ⬜ |
| M6 | Stage 7 | 高层 Producer/Consumer API | ⬜ |
| M7 | Stage 8 | 端到端测试 | ⬜ |

## 环境要求
- JDK 21（本机已有 /opt/homebrew/opt/openjdk@21）
- Maven: `brew install maven`
- ZooKeeper: `brew install zookeeper`（M2 起需要）

## 快速开始
mvn clean package
...guide commands...

## 目录结构
...

docs/MILESTONES.md: detailed per-milestone: 目标 / 关键任务 / 验收标准 / 对应指南章节.

Now execution order:
1. explore call
2. plan call (seed_todos=true)
3. write files (parallel writes in batches)
4. javac verify
5. git init + commit
6. final summary

Let me be careful with the write tool: it overwrites; fine for new files.

One more consideration: should README be in Chinese? User speaks Chinese; guide is English. I'll write README/MILESTONES in Chinese with English terms. Good.

Also note: the guide's medium article is paywalled possibly; mention repo link. Fine.

Let me now write everything. I'll do explore + plan in one message? explore then plan — plan depends on nothing from explore's output, but instructions say explore before plan. They're independent calls; I can batch them. Actually plan should reflect exploration findings — I already know them. Batch both in one response to save time. Hmm, the guidance: "If you intend to call multiple tools and there are no dependencies between the calls, make all of the independent calls in the same block." explore and plan are independent given I've done the research. I'll batch them.

Then todo_write is seeded by plan (seed_todos=true), so no separate todo_write needed initially.

File writing: many files. I can batch multiple write calls per response. Let me group: batch 1: pom.xml, .gitignore, README.md, docs/MILESTONES.md. batch 2: common (2), protocol (1). batch 3: zookeeper (1), storage (3). batch 4: broker (5), client (3), test (1). Then verify.

Actually I can put more writes per batch — they're independent. Maybe 6-8 per response.

Let me draft all file contents now.

pom.xml — final:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>com.simplekafka</groupId>
  <artifactId>simple-kafka</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>jar</packaging>

  <name>simple-kafka</name>
  <description>从零实现的 Kafka-like 分布式消息系统（学习项目，跟随 build-your-own-kafka 指南）</description>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.release>21</maven.compiler.release>
    <zookeeper.version>3.8.4</zookeeper.version>
    <slf4j.version>1.7.36</slf4j.version>
    <junit.version>5.10.2</junit.version>
  </properties>

  <dependencies>
    <!-- M2 (Stage 3) 起使用：broker 注册、controller 选举、元数据存储 -->
    <dependency>
      <groupId>org.apache.zookeeper</groupId>
      <artifactId>zookeeper</artifactId>
      <version>${zookeeper.version}</version>
    </dependency>
    <dependency>
      <groupId>org.slf4j</groupId>
      <artifactId>slf4j-simple</artifactId>
      <version>${slf4j.version}</version>
    </dependency>

    <dependency>
      <groupId>org.junit.jupiter</groupId>
      <artifactId>junit-jupiter</artifactId>
      <version>${junit.version}</version>
      <scope>test</scope>
    </dependency>
  </dependencies>

  <build>
    <plugins>
      <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-surefire-plugin</artifactId>
        <version>3.2.5</version>
      </plugin>
    </plugins>
  </build>
</project>
```

zookeeper 3.8.4 transitively brings slf4j-api 1.7.30; slf4j-simple 1.7.36 works. OK.

.gitignore:

```
target/
*.class
*.log
.idea/
*.iml
.vscode/
.DS_Store
/tmp/
```

Hmm /tmp/ maybe not needed. Keep simple.

Now README.md:

```markdown
# SimpleKafka — 从零实现 Kafka-like 系统（Java）

跟随指南 [Building Your Own Kafka-like System From Scratch: A Step-by-Step Guide](https://github.com/buildthingsuseful/build-your-own-kafka)（配套 [Medium 文章](https://medium.com/@buildthingsuseful/building-your-own-kafka-like-system-from-scratch-a-step-by-step-guide-d3c5f0a303c0)），用 Java 从零实现一个简化版 Kafka，理解分布式消息系统的核心设计。

## 里程碑

详细目标与验收标准见 [docs/MILESTONES.md](docs/MILESTONES.md)。

| 里程碑 | 指南阶段 | 内容 | 状态 |
|---|---|---|---|
| M0 | Stage 1 | Maven 项目骨架、包结构、CLI 入口 | ✅ |
| M1 | Stage 2 | 核心协议层：消息帧格式、CRC、编解码 | ⬜ |
| M2 | Stage 3 | ZooKeeper 集成：broker 注册、controller 选举、元数据 | ⬜ |
| M3 | Stage 4 | 存储层：LogSegment、稀疏索引、offset 管理 | ⬜ |
| M4 | Stage 5 | Broker：网络层、分区/副本、leader 选举与复制 | ⬜ |
| M5 | Stage 6 | 客户端库：连接管理、metadata 发现 | ⬜ |
| M6 | Stage 7 | 高层 Producer / Consumer API | ⬜ |
| M7 | Stage 8 | 端到端测试：3 broker 集群 + failover | ⬜ |

## 环境要求

- JDK 21（本机已装 Homebrew openjdk@21，未 link 时用 `export JAVA_HOME=/opt/homebrew/opt/openjdk@21`）
- Maven：`brew install maven`
- ZooKeeper（M2 起）：`brew install zookeeper`

## 快速开始

```shell
mvn clean package

# 1. 启动 ZooKeeper
zkServer start

# 2. 启动 3 个 broker
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.broker.SimpleKafkaBroker 1 localhost 9091 2181
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.broker.SimpleKafkaBroker 2 localhost 9092 2181
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.broker.SimpleKafkaBroker 3 localhost 9093 2181

# 3. 生产 / 消费
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.client.SimpleKafkaProducer localhost 9091 test-topic
java -cp target/simple-kafka-1.0-SNAPSHOT.jar com.simplekafka.client.SimpleKafkaConsumer localhost 9091 test-topic 0
```

> 当前为 M0 骨架：CLI 可运行并打印参数，broker/producer/consumer 的实际逻辑随里程碑逐步填充。

## 目录结构

```
src/main/java/com/simplekafka/
├── common/      协议常量、消息模型          (M1)
├── protocol/    二进制编解码               (M1)
├── zookeeper/   ZK 注册/选举/元数据        (M2)
├── storage/     LogSegment / 索引 / Log    (M3)
├── broker/      SocketServer / Partition / ReplicaManager / Controller (M4)
└── client/      NetworkClient / Producer / Consumer (M5-M6)
```
```

docs/MILESTONES.md — detailed:

```markdown
# 里程碑计划

对应指南的 Stage 1-8。每个里程碑：目标 → 关键任务 → 验收标准。完成一个再进入下一个。

## M0 项目骨架（Stage 1）✅
- 目标：可编译、可运行的 Maven 项目，包结构对应后续各组件。
- 任务：pom.xml（JDK 21、zookeeper、junit 依赖）；common/protocol/zookeeper/storage/broker/client 六个包；三个 CLI 入口（broker/producer/consumer）参数解析与指南一致。
- 验收：`mvn clean package` 成功；`java -cp ... SimpleKafkaBroker 1 localhost 9091 2181` 等命令可运行。

## M1 核心协议层（Stage 2）
- 目标：定义客户端↔broker、leader↔follower 共用的二进制协议。
- 任务：
  - 消息帧格式：`[4B 帧长][2B magic][4B CRC32][8B timestamp][4B keyLen][key][4B valueLen][value]`
  - MessageCodec.encode/decode（round-trip）
  - 请求/响应类型与错误码（PRODUCE/FETCH/METADATA/CREATE_TOPIC）
- 验收：编解码单元测试通过；CRC 校验能发现损坏帧。

## M2 ZooKeeper 集成（Stage 3）
- 目标：用 ZK 完成 broker 注册、controller 选举、元数据存储。
- 任务：
  - `/simplekafka/brokers/ids/{id}`（ephemeral）注册 broker
  - `/simplekafka/controller`（ephemeral）选举 controller
  - `/simplekafka/topics/{topic}` 存分区副本分配
  - watcher：broker 上/下线、controller 失效感知
- 验收：3 个 broker 启动后 ZK 中可见注册节点；kill controller 后剩余 broker 中选出新 controller。

## M3 存储层（Stage 4）
- 目标：Kafka 式顺序追加日志。
- 任务：
  - LogSegment：`.log` 追加写 + `.index` 稀疏索引（相对 offset → 文件位置）
  - Log：segment 按大小滚动、nextOffset 维护、按 offset 二分定位 segment 再读
  - 重启恢复：扫描 segment 恢复 nextOffset 与索引
- 验收：单元测试 append→read round-trip；重启后 offset 连续；索引查找命中正确位置。

## M4 Broker（Stage 5）
- 目标：完整 broker：网络、请求处理、分区副本、复制与故障转移。
- 任务：
  - SocketServer（ServerSocket + 线程池即可）+ 请求分发
  - Partition：leader/follower 角色；follower 从 leader 拉 取并写入本地 Log
  - Controller：从 ZK 读取分配、处理 broker 上下线、触发 leader 选举
  - 高水位（HW）与已确认消息语义
- 验收：创建 topic 后分区副本分布在 3 个 broker；kill leader，follower 接管且已确认消息不丢。

## M5 客户端库（Stage 6）
- 目标：客户端公共网络层。
- 任务：NetworkClient（连接管理、correlationId 关联请求/响应、METADATA 发现分区 leader）。
- 验收：producer/consumer 通过 metadata 拿到 leader 地址并直连成功。

## M6 高层 API（Stage 7）
- 目标：好用的 Producer / Consumer。
- 任务：
  - Producer：round-robin 选分区、acks 确认、失败重试
  - Consumer：poll 循环、按 offset 消费、offset 提交（存 ZK 或本地）
- 验收：produce N 条消息，consumer 恰好按序读到 N 条。

## M7 端到端测试（Stage 8）
- 目标：跑通指南 "Testing the System" 全流程。
- 任务：脚本/集成测试拉起 zk + 3 broker；produce/consume；kill leader 验证 failover；观察分区分布与复制。
- 验收：README 快速开始命令全部按预期工作。
```

Now Java files. Let me write them carefully so javac passes.

common/ProtocolConstants.java:

```java
package com.simplekafka.common;

/**
 * M1（Stage 2）：核心协议常量。
 */
public final class ProtocolConstants {

    privateI was in the middle of writing the skeleton. My previous response got truncated mid-way through drafting file contents (I was drafting in my head, hadn't actually made tool calls yet — actually looking back, my last visible action was drafting text in the response itself, which got cut). I need to continue: record explore/plan, then write all files, verify with javac, git init + commit, and summarize.

Let me now actually execute. First explore + plan calls, then write files in batches.

Let me be efficient: call explore and plan in one block, then write files.

Actually since my previous turn was truncated mid-drafting, I should just proceed with tool calls now. Let me do explore + plan together.Now write files. Batch 1: pom.xml, .gitignore, README.md, docs/MILESTONES.md.Batch 2: common、protocol、zookeeper、storage 包桩代码。Batch 3: broker、client 包与测试。验证：下载 zookeeper/slf4j jar 到临时目录，用 openjdk@21 全量编译并冒烟运行三个 main。编译通过；无参 broker 正确打印 usage 并 exit(1)（`set -e` 中断了后续冒烟）。继续冒烟带参运行。三个 CLI 冒烟通过。最后 git init + 初始提交。骨架已就绪并验证通过。指南已定位为 [buildthingsuseful/build-your-own-kafka](https://github.com/buildthingsuseful/build-your-own-kafka)（build-your-own-x 列表的 Java/Distributed Systems 条目），里程碑完全对齐它的 Stage 1-8：

| 里程碑 | 指南阶段 | 内容 |
|---|---|---|
| M0 ✅ | Stage 1 | 项目骨架 |
| M1 | Stage 2 | 协议层：消息帧 `[帧长][magic][CRC32][ts][key][value]`、请求/响应编解码 |
| M2 | Stage 3 | ZooKeeper：broker 注册、controller 选举、topic 分配元数据 |
| M3 | Stage 4 | 存储层：LogSegment + 稀疏索引 + segment 滚动/恢复 |
| M4 | Stage 5 | Broker：SocketServer、Partition/ReplicaManager、复制与 failover |
| M5 | Stage 6 | 客户端库：NetworkClient、metadata 发现 leader |
| M6 | Stage 7 | 高层 Producer（round-robin/acks）/ Consumer（poll/offset 提交） |
| M7 | Stage 8 | 端到端：3 broker 集群 + kill leader 验证 |

详细任务与验收标准在 `docs/MILESTONES.md`。

**已创建**（git 初始提交 `3f86596`）：
- `pom.xml`：JDK 21、zookeeper 3.8.4、slf4j、JUnit 5，产物名与指南一致（`simple-kafka-1.0-SNAPSHOT.jar`）
- 六个包的桩代码：`common`（协议常量、Message）、`protocol`、`zookeeper`、`storage`、`broker`、`client`，每个待实现点标了 `TODO(Mx)`
- 三个 CLI 入口参数解析与指南完全一致，`MessageTest` 验证测试接线

**验证结果**：openjdk@21 全量编译通过；`SimpleKafkaBroker 1 localhost 9091 2181`、Producer、Consumer 冒烟输出正常，错误参数正确打印 usage 退出。

下一步：`brew install maven` 后跑 `mvn clean package` 确认 Maven 构建与测试，然后从 M1（`MessageCodec` 编解码 + CRC 单元测试）开始实现。