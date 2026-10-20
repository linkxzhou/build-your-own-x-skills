The user wants me to convert a tutorial (http://joaoventura.net/blog/2017/python-webserver/) into a Claude Code executable learning task list. This matches the build-your-own-x skill — "build your own web server" category. Let me first read the skill file as instructed.

Let me read the skill first, then fetch the tutorial.该 URL 返回了 404。让我找一下正确的地址，并检查一下 web-server 轨道技能。The web search returned no results. Let me try fetching the URL with https and also check the manifest for a web-server track skill. The URL might be joaoventura.net/blog/2016/python-webserver/ or similar. Let me search the manifest and try a few URL variants.清单文件中将其列为 `web-server-http`。我来检查一下是否有针对该教程的技能，并尝试找到该文章的新位置。有一个与该教程匹配的 `web-server-http` 技能。让我检查一下轨道技能并阅读它。有一个针对该教程的专用技能。让我阅读一下轨道技能及其参考资料。教程 URL 已失效。根据 `tutorial-map.md`，当源内容不可用时，我应该先进行确认。让我尝试使用 Wayback Machine 存档，并阅读该教程技能的概念参考。Wayback 触发了速率限制。让我尝试使用一个明确的时间戳 URL 重试。Wayback is rate-limiting. Let me try the availability API which is lighter, or try a direct wayback URL format. Actually, let me try the wayback availability API:

https://archive.org/wayback/available?url=joaoventura.net/blog/2017/python-webserver/

That's a JSON API, lighter weight.Archive.org 目前限制了此 IP 的访问。让我搜索一下这篇文章的镜像或缓存版本。让我检查一下博客索引，看看文章是否移动了位置。The whole blog seems 404 now. The site may have been restructured or taken down. Let me try the root domain.网站已重构——"blog" 现在变更为 "articles"。让我去那里找找这篇文章。找到了：文章已移动至 `https://joaoventura.net/articles/2017/python-webserver/`。正在获取完整内容。文章内容被截断了。让我获取剩余部分以及包含最终源代码的 gist。提取器在约 10K 字符处被截断。让我通过 `curl` 获取完整的原始 HTML。我已经获取了完整的文章。让我验证一下起始 zip 链接是否仍然有效，然后记录探索结果并规划交付内容。文章已完全恢复，起始 zip 压缩包已失效（404）， gist 依然有效。在编写任务列表之前，先记录探索结果。文章已完整恢复，起始 zip 已失效（404）， gist 依然有效。现在开始编写任务清单。正在验证交付物和工作区状态。The file is written and structured correctly: 6 milestone sections (M0-M5), upstream links present, PROGRESS.md convention, execution protocol. The scratch file .tmp_article.md — I tried to remove it with bash but got permission denied. Let me check if it still exists and remove it via another means. Actually the earlier `cp` created ./.tmp_article.md. The bash rm failed with "permission denied" — odd, but maybe the whole bash command failed. Let me check with glob.任务清单已生成：`python-webserver/TASKS.md`。

转换过程中的三个事实修正：

- 原地址 `joaoventura.net/blog/2017/python-webserver/` 已 404，文章迁移到 `https://joaoventura.net/articles/2017/python-webserver/`，内容已全文核对。
- 教程自带的起始 zip（python-httpserver-base.zip）已失效，清单改为从零创建全部文件。
- 作者的最终代码 gist 仍可用，清单把它定位为“全部完成后的对照材料”，避免提前剧透。

清单结构（6 个里程碑，每个都带可执行验收命令）：

| # | 里程碑 | 验收 |
|---|---|---|
| M0 | 项目骨架 + telnet/curl 观察 HTTP 原文 | 文件就位，能指出请求行/头部/空行/体 |
| M1 | TCP 监听 + 硬编码 200 响应 | `curl -i` 得到 `HTTP/1.0 200 OK` + Hello World，服务端打印原始请求 |
| M2 | 返回 htdocs/index.html | `GET /` 返回 index.html 内容 |
| M3 | 解析请求行，按路径返回文件 | `GET /ipsum.html` 返回 ipsum 页 |
| M4 | FileNotFoundError → 404，服务器不崩 | 不存在路径返回 404，后续请求仍 200 |
| M5 | 拓展（可选）：路径穿越防护、线程并发、POST 回显、与 gist 对照 | 各自独立验收命令 |

清单开头写了给 Claude Code 的执行协议：一次一个里程碑、教学循环（讲概念 → 给骨架 → 学习者写核心 → 跑验收 → 调试 → 复盘）、不提前给完整代码、只用标准库、进度记入 `PROGRESS.md`（文末附模板）。每个里程碑还附了按因排查的常见坑（如 `Address already in use`、favicon 二次请求、空请求导致 `IndexError`）。

开始方式：新会话里让 Claude Code 读 `python-webserver/TASKS.md` 并从 M0 开始即可。