The user says: "My web server can return pages, but the browser keeps spinning and never finishes loading."

This is a debugging question. The user hasn't shared any code. This matches the build-your-own-x skill? The skill description says: "Use it whenever someone wants to understand how a tool works by building their own, ... OR is stuck/debugging midway through their own from-scratch implementation (e.g. 'my own git's hash differs from real git', ... 'my web server ...')". The user says "我的 web 服务器" — "my web server" — this could be their own from-scratch implementation (like a hand-written web server, 造轮子). The trigger includes "我自己写的 X 出 bug/卡在第 N 步". The user's phrasing "我的 web 服务器能返回页面，但浏览器一直转圈加载不完" strongly suggests they wrote their own web server (a build-your-own-x project) and it's buggy.

So per instructions: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it."

I should read the skill file first. Let me do that.

Also, I should check the workspace for their code — maybe there's a project in the workspace. Let me read the SKILL.md first, then explore the workspace.

Let me start by reading the skill.The skill says: read the track skill. The topic is a web server. Let me find the web-server track skill. Let me look for `skills/web-server*/SKILL.md` or similar. The glob output was truncated. Let me glob specifically.

Also the user's issue: browser keeps spinning — likely their own hand-written web server. The track skill for web server would be something like `skills/web-server/SKILL.md`. Let me find it.The track skill is `skills/web-server/SKILL.md`. Read it. Also, since the user is debugging, I should check their workspace for their server code. The glob earlier showed only skill files — the workspace seems to contain only `.agents/skills/...`. Let me check whether there's any user code in the workspace (e.g., server.py, etc.). The first glob `**/*` returned only skill files (truncated). Let me glob for common code files excluding .agents.

Let me read the track skill and search for user code in parallel.The workspace has no user code — only AGENTS.md and the skills. So the user's server code isn't in the workspace. The user is describing a bug in their own web server ("我的 web 服务器能返回页面，但浏览器一直转圈加载不完").

Per the track skill: "Debugging turns count too. When the learner is stuck mid-way, still read the track skill first, give the minimal fix, and end with a runnable check (command + expected output)."

I've read the track skill (mostly — it was truncated at line 42; let me read the rest to be thorough, lines 42-60ish). Let me read the remainder of the SKILL.md.

Then I should coach: the classic causes of "browser keeps spinning" with a hand-written HTTP server:

1. **Missing `Connection: close` + not closing the socket / keep-alive mishandling**: If the server doesn't send `Content-Length` and doesn't close the connection, the browser doesn't know when the body ends → keeps waiting → spinner forever. This is THE classic cause. HTTP/1.1 defaults to persistent connections; without Content-Length or chunked encoding, the client can't determine the end of the response body. Fix: send `Content-Length` header, or send `Connection: close` and close the socket after the response.

2. **Not closing the connection after response** (in HTTP/1.0 style servers): if you never `close()` the socket, curl/browser hangs.

3. **Not reading the request body fully before responding** — if the client sends a body (e.g., POST) and the server responds without draining the socket, the client may stall.

4. **Content-Length mismatch**: if Content-Length says N bytes but you send fewer, browser waits for the rest → spinner.

5. **favicon.ico request hanging**: browser requests /favicon.ico; if the server blocks on that request (e.g., single-threaded accept loop stuck, or handler crashes without response), the page may appear loaded but spinner continues. Actually if the server is single-threaded and blocks, subsequent requests hang. But the page itself returned. The spinner often keeps spinning because of a pending subresource request (favicon, CSS, JS, images) that never completes — e.g., the HTML references a resource and the server hangs on the second request (single-threaded server that doesn't handle concurrent requests, or crashed handler that never responds).

6. **Response not ending with proper CRLF / blank line**: headers must end with `\r\n\r\n`. If you use `\n\n` some browsers tolerate, but if missing entirely, browser waits.

7. **Chunked encoding done wrong**.

The most common for hand-rolled servers: missing Content-Length and/or never closing the socket.

Per the skill's coaching rules: give the minimal fix, end with a runnable check (command + expected output). Don't dump a full solution. Ask for their code? The skill says debugging turns: give minimal fix. But we don't have their code. We can give the diagnosis checklist and the most likely fix with a tiny code snippet for the current milestone, plus a runnable check with curl.

The user wrote in Chinese, so respond in Chinese.

Also per skill: "Credit the upstream tutorial you are following, using its exact link." For debugging, maybe reference the lsbaws tutorial (Ruslan Spivak's "Let's Build A Web Server") — the per-tutorial skill web-server-web-ruslanspivak-lsbaws-part1. Let me check the tutorials.md for the exact link to credit. Let me read the rest of the track SKILL.md (lines 42+) and tutorials.md.

Also, I should ask them to share their handler code OR paste it into the workspace. But the skill says give minimal fix. Best approach: explain the likely cause (response framing: Content-Length / Connection: close / socket close), give a minimal fix pattern, and a runnable check:

```
curl -v http://localhost:8080/
```
Expected: `Content-Length: N` present, and curl exits immediately (no hang). Also `curl -v --raw` or use `curl -H 'Connection: keep-alive'`.

Also a check for the "second request hangs" case: `curl -v http://localhost:8080/favicon.ico`.

Let me read the rest of the track skill and the tutorials reference to get the exact upstream link.**调试回合（响应收尾，milestone 1–3 最常见的坑）**

浏览器转圈的直接原因：它判定不了“响应已经结束”，于是一直等剩余字节。HTTP 里响应的结束只有两种合法信号——`Content-Length` 数够了，或者连接被关闭。手写服务器几乎总是栽在这两处之一：

1. **没发 `Content-Length`，也没发 `Connection: close`，发完也不 `close()` socket。** HTTP/1.1 默认 keep-alive，浏览器只能傻等下一段数据。
2. **`Content-Length` 数错了。** 最隐蔽的一种：页面里有中文时，`len(body)` 数的是字符数，实际要发的是字节数——每个汉字 3 字节，长度偏小，浏览器就永远差几个字节。必须 `len(body.encode('utf-8'))`。
3. **页面显示完了但圈还在转。** 这说明主文档到了，是某个子资源请求（`/favicon.ico`、CSS、JS）挂住了——单线程 accept 循环被第一个连接占死，或某个 handler 崩了却没回任何响应。

最小修复（Python 示意，Node/Go 同理，就这三件事）：

```python
body = html.encode("utf-8")                      # 先编码成字节
header = (
    "HTTP/1.1 200 OK\r\n"
    "Content-Type: text/html; charset=utf-8\r\n"
    f"Content-Length: {len(body)}\r\n"           # 字节数，不是字符数
    "Connection: close\r\n"
    "\r\n"                                       # 头部必须以空行 \r\n 结束
).encode("utf-8")
conn.sendall(header + body)
conn.close()                                     # 发完就关
```

概念出处可对照 [Let's Build A Web Server (Ruslan Spivak)](https://ruslanspivak.com/lsbaws-part1/) 第 1 部分的响应格式一节。

**怎么检查（跑完把结果对上来）：**

```bash
curl -v http://localhost:8080/
```

期望看到这三行，且 curl **立即退出**（挂起即命中原因 1/2）：

```
< HTTP/1.1 200 OK
< Content-Length: 137
< Connection: close
* Closing connection 0
```

curl 正常退出但浏览器仍转圈的话，再跑第二条，专测子资源/并发：

```bash
curl -v --max-time 3 http://localhost:8080/favicon.ico
```

期望 3 秒内返回（404 也算通过）；超时说明服务器卡在并发或某个 handler 上。两条都对不上时，把你发送响应的那段代码贴出来，我按你的实现给最小改动。