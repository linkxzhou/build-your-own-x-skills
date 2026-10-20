The user wants me to convert the tutorial at https://www.build-redis-from-scratch.dev/ into a Claude Code executable learning task list. This matches the build-your-own-x skill. Let me first read the skill file.

Let me start by reading the skill, then fetch the tutorial content.The web fetch returned almost nothing (the site is likely a JS-rendered SPA). Let me read the rest of the SKILL.md and check the skills directory for a redis track skill. Also try fetching the tutorial content differently — maybe there's a GitHub repo or the site has an API/JSON content.

Let me:
1. Read the rest of SKILL.md (truncated at line 43).
2. List skills directory for redis-related skills.
3. Try fetching the site with different methods (maybe curl via bash, or check for a sitemap, or the GitHub repo).存在一个 `database` 跟踪技能和针对每个教程的 Redis 技能。让我检查一下其中哪一个引用了此 URL，并阅读该跟踪技能。该教程是 Go 版本的 "Build Your Own Redis from Scratch"，并且有一个针对每个教程的技能 `database-redis-go`。让我阅读一下它及其参考资料。技能框架已加载。现在我需要实际的教程内容——该网站是一个 JS SPA，所以让我尝试用 `curl` 来获取它，并搜索其目录。这是一个 GitBook 站点，重定向至 `/en/introduction`。让我来获取该页面并查找其目录。已找到目录：introduction, first-steps, writing-server, resp-reader, resp-writer, implementing-commands, aof, next。我来获取所有页面并提取文本。我现在已经获取了完整的教程内容。让我检查一下工作区，并在编写任务列表之前记录我的发现。Now let me check the environment for Go and redis-cli availability (read-only checks, no installs), then write the plan and produce the task list file.Now milestone 1 coaching kickoff. Per the skill: explain the concept in 3-6 sentences, show the interface/skeleton, let the learner write the core. I should NOT dump the full solution. Give the skeleton with TODOs and let the learner fill in.

Let me update main.go to a skeleton with TODOs for M1, and present the coaching kickoff in my final message.教程已抓取并转换完成。产出三个文件：

**1. `LEARNING_TASKS.md`** — 核心交付物。8 个章节 → 8 个里程碑（M0–M7），每个含：概念讲解（3-6 句）、带编号的编码任务、可直接粘贴运行的验收命令 + 期望输出、常见坑。章节映射：

| 里程碑 | 教程章节 | 验收 |
|---|---|---|
| M0 环境准备 | First Steps | `go run .` → Hello World |
| M1 TCP 服务器 | Building Server | `printf 'PING\r\n' \| nc localhost 6379` → `+OK` |
| M2 RESP 读取器 | Reading RESP | `resp_test.go` 解析断言 |
| M3 RESP 写入器 | Writing RESP | marshal golden 断言 |
| M4 命令处理器 | Redis Commands | PING/SET/GET/HSET/HGETALL 往返 |
| M5 并发 | Introduction（goroutines） | 双客户端互不阻塞 |
| M6 AOF 持久化 | Data Persistence | 重启后数据仍在 |
| M7 延伸 | Whats Next | 自定义 |

**2. `PROGRESS.md`** — 进度表 + 调试日志，每过验收记一行。

**3. 脚手架** — `go mod init` 完成，`main.go` 已写成 M1 骨架（TODO 注释标出 4 个填空点），`go build` / `go vet` 通过。

环境实测：Go 1.26.1 ✅，端口 6379 空闲 ✅，redis-cli 未安装——所以所有验收命令都给了 `nc` 版本，装了 redis-cli 可直接替换。

**M1 现在开始**。概念：数据库服务器就是一个 TCP 监听器——`net.Listen` 占住端口，`Accept()` 等客户端，`for` 循环里 `conn.Read()` 收字节、`conn.Write()` 发回应。这一步不解析协议，收到什么都回 `+OK\r\n`，先打通链路。

`main.go` 里的 TODO 就是你的作业：listener、accept、读循环、回写四步，骨架和提示都写在注释里。写完跑：

```bash
go run . &
printf 'PING\r\n' | nc localhost 6379   # 期望 +OK
```

卡住或跑通后把输出贴给我，我按 `PROGRESS.md` 记录后进 M2。