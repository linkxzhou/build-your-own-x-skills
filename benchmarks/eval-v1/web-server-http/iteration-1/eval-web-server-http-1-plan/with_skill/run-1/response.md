The user wants to learn by building a basic HTTP server from scratch in Python. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.The file was truncated. Let me read the rest of the SKILL.md to see the category map and find the right slug for "web server".主题映射到 `web-server` 跟踪。现在正在读取跟踪技能（在执行其他任何操作前是必需的）。该任务映射到 `web-server` 轨道，而 joaoventura 的 "Building a basic HTTP Server from scratch in Python" 教程几乎完全符合该请求。让我检查一下工作区状态以及该教程的各教程技能。有一个针对每个教程的技能 `web-server-web-python`，很可能对应于 joaoventura 的文章。让我通过 manifest 验证并阅读它。`web-server-http` 是用户提到的确切教程（joaoventura 的 Python HTTP server 文章）。正在读取其各教程的技能。技能链已读完：主题映射到 `web-server` 赛道，且存在与你点名教程一一对应的子技能 `web-server-http`（joaoventura 的文章）。工作区为空（只有 `.agents`），可以从零搭骨架。先记录探索笔记、取上游教程原文对齐里程碑，并拿当前日期。上游原文 404 了。按 tutorial-map 的规则，源不可用时以赛道技能的里程碑表为准；我再确认一下 Wayback Machine 快照是否存在，同时检查本机 Python 版本，然后定计划。Python 3.14.7 与 curl 就绪；上游原文已 404（Wayback 限流），按规则以赛道技能里程碑表为准并在 README 署名原链。开始创建骨架文件。文件就绪，fixture 字节级验证含真实 CRLF。现在做冒烟验证：启动骨架服务器，确认连接被接受、响应为空、进程存活，并语法检查检查脚本。冒烟结果符合设计：连接被接受、响应为空（连接被重置）、服务器打印引导提示后 accept 循环存活。最后在 PROGRESS.md 记录骨架引导条目。骨架就绪，冒烟验证通过。当前进度：**M1 / M7**。

**项目结构**

```
server.py            入口：accept 循环已写好，handle_client 留给你
static/index.html    M3 起对外服务的页面
tests/fixtures/      M2 解析器用的原始请求样本（字节级含 CRLF）
scripts/check_m1.sh  M1 检查点脚本
README.md            里程碑表 M1–M7 + 运行方式
PROGRESS.md          过检记录（已记 M0 骨架引导）
```

**M1 概念（30 秒版）**：HTTP 跑在 TCP 上。服务器做四件事——`socket()` 创建套接字、`bind()` 占住 `127.0.0.1:8080`、`listen()` 开始排队、`accept()` 循环逐个接客。这部分样板已在 `server.py:31-40` 写好；你的工作在 `handle_client`（`server.py:13`）：读请求字节、拼一个硬编码的 HTTP 响应、发回、关闭。HTTP 响应的关键结构是「状态行 + 头 + 空行 + body」，头和 body 之间必须有一个空行（连续两个 `\r\n`）。

**你要写的**：`server.py` 里的 `handle_client`，函数 docstring 里有四步提示。建议先只写 `recv` 并把收到的字节 print 出来，用浏览器或 curl 发一个请求，亲眼看一下原始 HTTP 长什么样，再补发送逻辑。

**检查点**：

```bash
bash scripts/check_m1.sh        # 通过时输出: M1 通过: GET / 返回 HTTP 200
```

卡住时说一声，我一次给一个提示。过检后把结果记进 `PROGRESS.md`，我们进 M2（HTTP 解析）。