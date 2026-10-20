The user wants to learn by building a basic HTTP server from scratch in Python. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.The file is truncated. Let me read the rest of it.主题映射到 `web-server` 轨道。现在开始读取轨道技能（强制要求）。The track skill isn't at `.agents/skills/web-server/SKILL.md`. Let me find where skills live.Now let me read the tutorials reference to pick a Python tutorial with its exact link.The learner wants Python, "用 Python 从零构建基础 HTTP Server" — this maps exactly to "Building a basic HTTP Server from scratch in Python" by João Ventura: http://joaoventura.net/blog/2017/python-webserver/

Let me check if there's a per-tutorial skill for it: `skills/web-server-*`. From the glob output earlier I saw various per-tutorial skills. Let me check for web-server-* ones.`web-server-web-python` 很可能涵盖了 João Ventura 的文章。让我确认一下。这个单教程技能对应的是 AOSA 文章。用户请求中提到了“基础 HTTP Server”，这与 João Ventura 的文章相符。我来检查一下 manifest，看看哪个 slug 对应哪个 URL。Exact match found: `web-server-http` — "用 Python 从零构建基础 HTTP Server" (João Ventura's article). Reading that per-tutorial skill now.技能链已读完：入口 → `web-server` 轨道 → 精确匹配的教程技能 `web-server-http`（João Ventura《Building a basic HTTP Server from scratch in Python》）。先确认工作区状态和 Python 环境。工作区是空的，Python 3.14.7 和 curl 都可用。记录探索结论并制定计划。现在验证骨架确实能启动并监听 8080（后台起 3 秒再杀掉）：里程碑规划与骨架已就绪，位于 `my-http-server/`。上游教程：[Building a basic HTTP Server from scratch in Python](http://joaoventura.net/blog/2017/python-webserver/)（João Ventura），M1–M3 对应教程正文，M4–M6 是进阶扩展。

**当前进度：M1 / 7 — TCP listener**

**概念（3 句话）**：HTTP 跑在 TCP 之上。服务器先 `socket()` 创建套接字，`bind()` 占住 `localhost:8080`，`listen()` 排队等待，然后 `accept()` 阻塞直到有客户端连入——每次 accept 返回一个专门服务这条连接的新 socket。HTTP 响应的最小形态就是一段字节：状态行 + 头 + 空行（`\r\n\r\n`）+ body。

**骨架里已备好**：`server.py`（bind/listen/accept 循环已写好，留了 TODO a/b/c 给你）、`TASKS.md`（7 个里程碑各带检查命令）、`PROGRESS.md`、`tests/smoke_test.py`、`www/` 和 `scratch/`。已验证骨架能启动并监听 8080。

**你接下来写**（`server.py` 的 TODO 处，约 3 行）：
1. `client_socket.recv(1024)` 收请求，打印出来看看真实的 HTTP 请求长什么样
2. `client_socket.sendall(RESPONSE)` 回硬编码响应
3. `client_socket.close()`

**检查点**（通过后在 `PROGRESS.md` 记一行，然后我们进 M2）：

```bash
python3 server.py        # 终端 1
curl -v localhost:8080   # 终端 2
```

预期：`HTTP/1.1 200 OK`，body 为 `Hello, World!`；服务器终端打印 `Connection from ...`。