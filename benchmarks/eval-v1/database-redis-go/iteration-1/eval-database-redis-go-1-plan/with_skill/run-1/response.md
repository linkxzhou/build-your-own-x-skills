The user wants to learn by building "Build Your Own Redis" from scratch in Go. They want me to:
1. First plan milestones
2. Create a minimal project skeleton

This matches the `build-your-own-x` skill. I must read the SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it, and also find the Redis track skill. The category map was truncated. Let me read more of the SKILL.md and look at the skills directory.用户想要用 Go 实现 Redis。根据分类映射，Redis 对应 `database` 路径。让我找一下该路径的 skill。用户指定的教程「从零构建你自己的 Redis」对应 `database-redis`（build-your-own.org/redis），语言是 Go，还有 `database-redis-go` 可参考。按路由要求，先读 `database` 轨道技能（必读），再读两个教程级技能。`database-redis` 是 C++ 版教程（build-your-own.org/redis），用户指定 Go，所以再读 Go 版教程技能 `database-redis-go` 及其参考资料。技能链已读完：路由 → `database` 轨道 → `database-redis`（你点名的教程，C++ 版）→ `database-redis-go`（Go 版）。现在检查工作区状态和 Go 工具链，并确认上游教程链接。环境确认：Go 1.26.1 可用，工作区为空（只有 `.agents` 和 `AGENTS.md`），有 `nc` 无 `redis-cli`。先看一下 `AGENTS.md` 是否有项目约定。技能链已读完（路由 → `database` 轨道 → `database-redis-go`）。环境：Go 1.26.1（darwin/arm64），工作区为空，有 `nc` 无 `redis-cli`。先记录探索结论，再定计划。计划已定。现在批量创建骨架文件（s1–s3 + README），一处小调整：计划中的 `internal/proto` 改名为 `internal/command`（命令分发表），语义更清晰。构建、vet、测试全绿。最后做 M0 检查的冒烟验证：服务器能启动并监听端口。命令超时——后台 `go run` 的子进程持有输出管道导致挂起。清理残留进程并用重定向重试。端口已被早前那次 `go run` 的残留实例占用——这恰好证明服务器能正常启动监听。清理孤儿进程收尾。里程碑路线图与项目骨架都已就绪，M0 验证通过。

## 里程碑路线图（每个都有可运行检查点）

| # | 里程碑 | 核心概念 | 检查 |
|---|---|---|---|
| M0 ✅ | 项目骨架 | 模块结构、构建/测试流程 | `go build ./... && go test ./...` 全绿 |
| M1 | TCP 服务器 + PING | accept 循环、`\r\n` 分帧 | `printf '*1\r\n$4\r\nPING\r\n' \| nc 127.0.0.1 6380` → `+PONG` |
| M2 | RESP 解析 + GET/SET | RESP2 五种类型、命令分发表 | SET/GET 往返；未知命令回 `-ERR` 且进程不崩 |
| M3 | 并发 | goroutine per conn、数据竞争 | `go test -race ./...`；多客户端无错乱 |
| M4 | 过期 PX/EX/TTL | 惰性 + 定期删除、可注入时间源 | `SET k v PX 100`，200ms 后 GET → `$-1` |
| M5 | 持久化 | AOF vs 快照、重放、损坏尾部 | 重启数据仍在；截断日志仍能启动 |
| M6 | 扩展（选做） | DEL/INCR、B+树存储引擎、SQL 层 | 视所选扩展自定 |

主线教程：[Build Your Own Redis from Scratch](https://build-your-own.org/redis)（C++ 原版，概念通用），Go 跟练参考 [build-redis-from-scratch.dev](https://www.build-redis-from-scratch.dev/)，出自 [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x)。

## 骨架（已创建并验证）

```
cmd/miniredis/main.go    入口：-port 参数（默认 6380），已能启动监听
internal/server/         TCP 接入层：accept 循环已写好，handleConn 留给你（M1）
internal/resp/           RESP 编解码：ParseCommand + 编码辅助 TODO（M2）
internal/command/        命令分发表 Dispatch TODO（M2）
internal/store/          内存 KV：Set/Get TODO（M2），过期结构 TODO（M4）
README.md / PROGRESS.md  路线图 + 进度表（M0 已记录 ✅）
```

验证结果：`go build`、`go vet`、`go test`（4 个包）全绿；二进制启动后 `nc -z` 确认 6380 监听成功。各包测试目前是「骨架自检」（断言占位错误），你实现对应里程碑后把它们改写成真实行为测试。

## 当前位置：M0 完成，从 M1 开始

**概念**（3 句）：Redis 客户端通过 TCP 长连接发送命令，服务器为每个连接循环「读命令 → 执行 → 回复」。RESP 协议里 `PING` 的字节形态是 `*1\r\n$4\r\nPING\r\n`（1 个参数的数组，参数是 4 字节的 bulk string），回复 `+PONG\r\n`。accept 循环我已搭好，你的工作在 `internal/server/server.go:44` 的 `handleConn`。

**你要写的**（TODO 已标在代码里）：
1. 用 `bufio.Reader` 包住 `conn`（RESP 按 `\r\n` 分行，需要按行读）
2. 循环读命令，对端关闭（`io.EOF`）时 return
3. M1 只需认得 `PING` → 回 `+PONG\r\n`，其余回 `-ERR unknown command\r\n`

**检查**：`go run ./cmd/miniredis -port 6380`，另开终端 `printf '*1\r\n$4\r\nPING\r\n' | nc 127.0.0.1 6380`，期望输出 `+PONG`。

写完跑检查，把结果（或卡住的报错）贴给我；卡住时我一次给一个提示。