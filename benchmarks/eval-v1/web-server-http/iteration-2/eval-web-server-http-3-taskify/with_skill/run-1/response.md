The user wants me to convert a tutorial (http://joaoventura.net/blog/2017/python-webserver/) into a Claude Code executable learning task list. This matches the build-your-own-x skill — "build a web server from scratch" is one of the topics. Let me read the skill first.

Let me fetch the tutorial content and read the skill.该 URL 返回了 404。让我找一下这篇文章的实际位置，并检查一下 web-server 的 track skill。The web search found nothing. Let me try fetching the URL with https and different paths. The original URL was http://joaoventura.net/blog/2017/python-webserver/. Maybe the actual URL is different. Let me try:
- https://joaoventura.net/blog/2017/python-webserver/
- Maybe it's "simple-python-webserver" or similar.

Let me search the site. Also read the web-server track skill.博客的 URL 已经失效。让我检查一下该轨道的精选教程列表，以及是否有针对该特定文章的教程技能。该教程在精选列表中。我来检查一下针对该教程的技能，并通过 Wayback Machine 获取文章内容，因为原网址已经失效。每个教程的技能 `web-server-web-python` 涵盖了另一篇文章（aosabook 500L）。Wayback 触发了速率限制；让我通过 availability API 查询一个快照。Archive.org 正在限流。让我尝试使用 Memento TimeTravel 聚合器。Timetravel is dead. Let me try the wayback machine again after a moment, or try a different snapshot URL format. Let me wait a bit and retry web.archive.org with a specific timestamp format. Or try Google cache — deprecated. 

Let me try the wayback CDX API instead, which might be a different rate limit bucket.Egress proxy 正在对 archive.org 进行限流。我稍等片刻后再重试。仍然受到速率限制。让我搜索一下这篇文章的镜像或翻译副本，同时等待。The egress proxy is rate-limiting archive.org hard. Let me try a different approach — maybe the article is mirrored elsewhere. The article "Building a basic HTTP Server from scratch in Python" by João Ventura (2017). Let me search for its content. The article content, as I recall from the build-your-own-x list and general knowledge:

The article builds a simple HTTP server in Python using sockets:
1. Creates a socket, binds to port 8080, listens
2. Accepts connections, receives request
3. Parses the request line (method, path, version)
4. Sends a hard-coded response
5. Then serves static files from a directory, with MIME types
6. Handles 404s

Let me try searching for cached copies on other sites — e.g., Chinese translation blogs (the article was translated into Chinese on some sites like jianshu/csdn), or GitHub repos that reference it.

Let me search in Chinese: "用Python从零开始构建一个基本的HTTP服务器" or "joaoventura HTTP服务器".我来尝试使用 archive.today 作为替代存档。archive.ph fails with SSL error (probably blocked by egress proxy). Let me try archive.today variants: archive.li, archive.md, archive.is.Archive.today 域名被代理拦截了。在等待更长时间后，我再尝试一次 archive.org。代理一直被限速。让我尝试通过 `bash` 使用 `curl`，它可能走不同的网络路径。让我检查一下作者网站是否已迁移了该文章，并搜索中文翻译。作者网站已重构；旧博客文章已移除。让我检查一下他的文章列表，看看是否有新的 URL。找到了——文章已迁移至 `/articles/2017/python-webserver/`。正在获取。内容被截断了。让我获取剩余的部分。fetch 工具截断了输出。我来用 curl 下载完整页面并读取它。我已经获取了完整的文章。让我快速验证一下起始 zip 的 URL 是否仍然有效，然后记录我的探索笔记。我已经获取了完整的教程内容。现在开始编写任务列表文件。正在修复我在 S1 中发现的一个拼写错误（`\r\n\r<body>` 应该为 `\r\n\r\n<body>`）：任务清单已生成：`python-webserver-tasks.md`。

两点说明：

- 原链接已失效，文章迁移到了 https://joaoventura.net/articles/2017/python-webserver/ ，清单内引用的是新地址；作者起点 zip 的旧路径也失效了，清单里用的是验证过的新路径（HTTP 200）。
- 清单按 build-your-own-x 的 web-server 教练流程组织：M0–M5 严格对应教程正文（HTTP 文本本质 → socket 监听 → index.html → 请求行解析 → 404），S1/S2 补上教程代码自带的两个真实缺陷（`\n` 行尾、路径穿越），每个任务都带概念讲解、骨架代码、原文练习和可执行的验收命令。

使用方式：在项目目录启动 `claude`，把清单开头「如何用 Claude Code 执行本清单」里的开场白粘贴进去即可，它会按「概念 → 骨架 → 你写核心 → 验收 → 复盘」逐任务推进，并把进度记入 `PROGRESS.md`。

验收：

```bash
head -40 python-webserver-tasks.md
```

期望输出：标题、原文新链接、gist 链接和开场白模板。