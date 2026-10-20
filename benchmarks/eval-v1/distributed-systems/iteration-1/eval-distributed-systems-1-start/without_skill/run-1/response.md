The user asks in Chinese: "I want to implement a Kafka-like distributed log myself, in Go. What's the first step?" The workspace is named "build-your-own-x-distributed-systems-1", suggesting they're working through a build-your-own-x exercise. Let me check what's in the workspace first — maybe there's existing scaffolding or a README describing the exercise.

This is a question, not a code change request. I should look at the workspace to see if there's context, then give a focused answer. Let me glob the workspace.第一步：先做单机上的 append-only log（WAL）。Kafka 的本质就是「partition = 一个只追加、按 offset 寻址的日志」，分区、复制、消费者组全部建立在这个原语上。这一步不涉及网络和分布式，纯文件 I/O。

目标 API（先只做这两个方法）：

```go
type Log struct{ /* segments, dir */ }

func (l *Log) Append(b []byte) (uint64, error) // 返回分配的 offset
func (l *Log) Read(offset uint64) ([]byte, error)
```

磁盘布局照抄 Kafka 的最小集：

- 每个 segment 两个文件：`<baseOffset>.log`（数据）和 `<baseOffset>.index`（稀疏索引）
- 记录格式用 length-prefix + CRC：`[len uint32][crc32][payload]`，`encoding/binary.BigEndian` 编解码
- 写入用 `os.OpenFile(..., os.O_APPEND|os.O_CREATE|os.O_WRONLY)`，读用 `ReadAt`（pread，天然并发安全）
- 超过阈值（如 1GB）滚动新 segment；索引每 N 条记录或 N 字节记一条 `offset → 文件内位置`

这一步要定的三个语义，后面全依赖它们：

1. offset 是逻辑递增的，跨 segment 连续，重启后必须延续
2. Append 返回成功 = 数据已写入（是否 fsync 由配置决定，先做成每次 `Sync()`，后面再改成可配）
3. Read(offset) 对不存在的 offset 返回明确错误（`ErrOffsetNotFound` 之类）

验证标准：一个测试里并发 Append 1 万条，逐条 Read 校验内容和顺序；杀掉进程重启后，Append 返回的 offset 接着上次的走。

完成后再往上叠：多 partition（每个 partition 一个 `Log` 实例）→ TCP 协议 + producer/consumer → 消费者 offset 持久化 → leader/follower 复制。参考 Travis Jeffery 的 "Building a Distributed Log from Scratch" 系列和 CodeCrafters 的 "Build your own Kafka"（Go track），路线基本就是这个顺序。