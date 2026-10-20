The user wants me to convert a tutorial from GitHub (build-your-own-kafka) into a Claude Code executable learning task list. Let me first fetch the tutorial to understand its content.

The workspace is named "build-your-own-x-distributed-systems-kafka-java-3", suggesting this is about building your own Kafka in Java.

Let me fetch the GitHub repo first.GitHub 页面返回的多是导航内容，直接抓取 raw README。README 指向一篇 Medium 文章作为详细步骤来源，同时看一下仓库的代码结构。API 限流了，直接浅克隆仓库看结构。仓库结构清楚了。现在读关键源码文件，理解各组件职责，以便任务清单准确对应。Let me read more of the key files to understand the structure. Let me look at the rest of SimpleKafkaBroker, Partition, ZookeeperClient, and the client files. I'll skim them quickly with grep for method signatures to understand the components.I now have a good understanding of the codebase. Let me also check the client files quickly and the controller election logic to make the task list accurate.教程内容已完整掌握：README（8 个阶段 + 测试方法）+ 仓库源码（协议、ZK 集成、存储、Broker、客户端共 9 个 Java 文件）。参考代码已放入 `reference/`。现在生成任务清单。任务清单已生成：`TASKS.md`。参考实现代码已克隆到 `reference/` 供对照。

**转化依据**（已核对教程 README 与仓库全部 9 个源文件）：
- 教程的 8 个阶段（项目骨架 → 协议 → ZooKeeper → 存储 → Broker → 客户端库 → Producer/Consumer → 测试）映射为任务 0–8，每个任务独立可执行。
- 协议常量、字节布局、ZK 节点路径（`/brokers`、`/controller`、`/topics`）、CLI 参数均从参考源码逐一核实，与 README 的测试命令一致（jar 名 `simple-kafka-1.0-SNAPSHOT.jar` 对应 README 的运行命令）。

**清单结构**：每个任务含「提示词」（直接粘贴给 Claude Code）、「验收标准」（要求实际运行命令并贴输出）、「学习点」。关键设计：

- 任务 1–3 各带一个无依赖的自测 main 类（ProtocolTest / ZkTest / PartitionTest），可独立验证后再进入下一阶段。
- 任务 4/5 把 Broker 拆成两步：先跑通请求处理，再做 Controller 选举与故障转移，`ElectionTest` 自动 kill 进程并断言 5 秒内选出新 Controller。
- 任务 8 的 `scripts/e2e.sh` 把分区复制、leader 迁移、持久化变成可重复执行的自动化断言，要求连续跑两遍幂等通过。
- 结尾附 3 道对照思考题（刷盘策略、KRaft 取代 ZK 等），衔接真实 Kafka 的设计差异。

使用方式：按编号开新会话，粘贴对应提示词；规则是先自行实现、卡住才允许查看 `reference/` 对应文件，禁止整文件复制。