The user wants me to convert a tutorial (http://joaoventura.net/blog/2017/python-webserver/) into a Claude Code executable learning task list. Let me first fetch the tutorial to understand its content, then convert it into a task list.

Let me fetch the blog post first.URL 返回 404，搜索正确地址。Archive.org is rate-limiting. Let me try a different approach — maybe Google cache or another mirror. Actually, I know this blog post well: it's João Ventura's "Python Web Server in 100 lines" or similar. Let me search for mirrors of the content.

Actually, let me try the direct site with different paths, or search for the content text.站点结构变了，原 `/blog/` 路径已失效。查 notes/articles 归档。找到了，文章迁移到 `/articles/2017/python-webserver/`。教程全文已拿到（文章已迁移到 `joaoventura.net/articles/2017/python-webserver/`）。内容分 5 步：telnet 体验原始 HTTP → socket 最小服务器 → 返回 index.html → 解析路径返回任意页面 → 404 处理。

先验证教程代码在当前环境可跑通，确保任务清单里的验收命令真实有效。教程代码端到端跑通（200 / 路由 / 404 均正常）。再验证任务 1 要用的原始 HTTP 演示命令在 macOS 上可用（新版 macOS 已移除 telnet，需用 nc 替代）。本地原始 HTTP 收发验证通过（`nc -l` 监听 + 管道发送均可用；telnet 在 macOS 已移除，外网 80 端口原始流量会被沙箱拦截，这两点要写进清单）。再验证清单里要写的验收命令和 T6 加固点是否属实。发现两个关键事实：旧进程没被杀干净（`pkill -f "python3 server.py"` 匹配不到，实际进程名是完整 Python 路径），且空请求确实让服务器崩溃（`IndexError`）。清理后验证 T6 剩余两点。T6 三个缺陷全部实锤：空请求 → `IndexError` 崩溃；`--path-as-is /../server.py` 直接吐出源码；单线程串行。所有验收命令都已在本机验证过。现在写任务清单。完成。产出两个文件：

- **`TASKS.md`** — 6 个可执行学习任务（T1–T6），每个含目标、步骤、已验证的验收命令
- **`tutorial-reference.md`** — 教程全文备份（原文已从 `/blog/` 迁移到 `joaoventura.net/articles/2017/python-webserver/`）

任务结构对应教程的 5 个递进步骤，外加一个进阶任务：

| 任务 | 内容 |
|---|---|
| T1 | 用 `nc` 本机收发原始 HTTP 文本（macOS 无 telnet，沙箱拦外网 80 端口，故改为本机监听） |
| T2 | socket 最小服务器，返回 `Hello World` |
| T3 | 返回 `htdocs/index.html` |
| T4 | 解析请求路径，返回任意页面 |
| T5 | `FileNotFoundError` → 404 |
| T6 | 攻击自己的服务器：空请求崩溃、路径穿越、单线程阻塞，逐一复现并修复 |

清单里的所有验收命令（200 响应、路由、404、三个攻击复现）都在本机 Python 3.14 实测通过，包括确认了教程代码确实会被空请求打出 `IndexError`、`--path-as-is /../server.py` 会泄露源码。两个环境坑也写进了清单：`pkill -f "python3 server.py"` 匹配不到进程（实际进程名是完整框架路径），以及重启前必须先 kill 旧进程否则 `bind` 报 `Address already in use`。