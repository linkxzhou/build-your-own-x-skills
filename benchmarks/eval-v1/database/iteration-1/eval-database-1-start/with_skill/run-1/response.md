The user wants to build a mini Redis in Python from scratch (GET/SET). This matches the build-your-own-x skill. I must read the skill's SKILL.md first before doing anything else.The file was truncated. Let me read the rest of it, and also find the Redis track skill. Let me read more of the SKILL.md and glob for the skills directory.用户希望使用 Python 编写一个迷你 Redis。根据类别映射，Redis 对应 `database` 轨道，并且有一个针对 Python 的特定技能。我先读取这两个文件。现在我来读取 Python 轨道的教程映射和概念参考，并检查工作区状态。工作区是空的，Python 3.14 已准备就绪。让我记录下探索过程，并检查有哪些可用于检查点的客户端工具。`nc` 可用于检查点（没有 `redis-cli`，这没关系）。在创建任何内容之前，让我先检查一下工作区的 `AGENTS.md`。范围已明确：Python 3.14，仅使用标准库，端口 6380，目标是一个基于 RESP 的迷你 Redis，支持 PING/GET/SET。我将遵循 `database` 路径的里程碑表，并标注上游教程。让我来制定计划。脚手架搭建时间。正在创建项目文件。项目已就绪，参考教程是 charlesleifer 的 [Building a Simple Redis Server with Python](http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)，我们按里程碑推进，你写核心代码，我负责脚手架和检查。

## 里程碑 1：TCP 服务器 + PING

**概念（30 秒版）**：Redis 本质是一个 TCP 服务器，客户端连上来发字节流，服务器回字节流。所有通信走 RESP 协议——客户端把 `PING` 编码成 `*1\r\n$4\r\nPING\r\n`（意思是“1 个参数，长度 4，内容 PING”），服务器回 `+PONG\r\n`（`+` 表示简单字符串）。里程碑 1 只做一件事：收到什么连接，就回一个 `+PONG\r\n`，先不解析协议。

**你的任务**：`mini-redis/server.py` 里 `main()` 已经写好了 bind/listen/accept 循环，`handle_connection` 留给你，三行以内：

1. `conn.recv(1024)` 读出客户端发来的字节
2. 回复 `b'+PONG\r\n'`
3. 连接由 `with conn` 自动关闭

**跑起来验证**：

```
cd mini-redis
python3 server.py          # 终端 1
printf '*1\r\n$4\r\nPING\r\n' | nc localhost 6380    # 终端 2，期望输出 +PONG
```

写完把代码贴给我（或直接说“写好了”让我跑检查点）。卡住了就贴报错，我们从真实输出调试。