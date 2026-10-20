The user says: "My web server can return pages, but the browser keeps spinning and never finishes loading."

This is a debugging question. The user hasn't shown any code. I should check the workspace for their web server code. Let me look at the files in the workspace first.

This matches the build-your-own-x skill? The skill description says: use it whenever someone wants to understand how a tool works by building their own, OR is stuck/debugging midway through their own from-scratch implementation (e.g. 'my own git's hash differs from real git', 'my ray tracer has shadow acne', 'my CHIP-8 draws garbage', 'my toy kernel triple-faults'). The user says "我的 web 服务器能返回页面，但浏览器一直转圈加载不完" — this is likely their own from-scratch web server implementation that's stuck. This matches the skill trigger: "我自己写的 X 出 bug/卡在第 N 步". So I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file and also explore the workspace in parallel. Actually, the instruction says: read that skill's SKILL.md with the read tool BEFORE doing anything else. So first read the SKILL.md. I can also do parallel reads of the workspace to see what's there. But the instruction says read the skill BEFORE doing anything else. To be safe, read SKILL.md first, then explore.

Let me do that.The skill file was truncated. Let me read the rest of it, and also check the workspace for the user's web server code.用户正在调试他们自己的 web 服务器——这对应于 `web-server` 跟踪。根据技能工作流，我必须接下来读取该跟踪技能，并检查工作区中是否存在任何用户代码。No user code files in the workspace (no .py/.js/etc. files). So the user's web server code isn't in this workspace. The user is describing a symptom: server returns pages but browser keeps spinning.

Let me read the rest of the web-server SKILL.md (truncated at line 41).**调试回合**（大概率在里程碑 1–3：TCP listener / 静态文件）。

**概念：** 浏览器判断“响应结束了”只认三样东西之一：`Content-Length`、`Transfer-Encoding: chunked`、或者连接被关闭。手写服务器最典型的坑：响应头里没有 `Content-Length`，发完 body 也没 `close()` socket —— 浏览器只能一直等更多字节，于是转圈到超时。

**最小修复（推荐两个都做）：**

1. 响应头加 `Content-Length: <body 的字节数>`。注意是**字节数**：`len(body.encode('utf-8'))`，含中文时 `len(str)` 会算错，浏览器会永远等差额那几个字节。
2. 加响应头 `Connection: close`，并且在 `send()` 完之后真正调用 `conn.close()`。只发头部、忘了关连接，效果和没发一样。

**先跑这个确认病因：**

```
curl -v --max-time 5 http://localhost:8080/
```

- curl 打印出页面后卡满 5 秒、最后报 `Operation timed out` → 就是上面的 framing 问题，按 1、2 修。
- curl 立刻干净退出 → 页面本身没问题，转圈来自**第二个请求**：浏览器还会要 `/favicon.ico`，或在 keep-alive 连接上发下一个请求，而你的循环正阻塞在旧连接的 `recv()` 上。这种情况把你的 handler 代码贴出来（或放进工作区），我帮你定位到具体那行。

修完后再跑一次上面的 curl：预期看到 `Content-Length: N` 且 curl 在 1 秒内正常退出，浏览器刷新后秒开。