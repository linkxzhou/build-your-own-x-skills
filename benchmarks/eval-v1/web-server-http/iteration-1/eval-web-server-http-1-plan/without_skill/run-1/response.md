The user wants to learn and implement "building a basic HTTP server from scratch in Python" and asks me to:
1. Plan milestones
2. Create a minimal project skeleton

Let me first look at the current workspace to understand what's there. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-web-server-http-1` — this looks like it's based on the "Build Your Own X" style challenge (codecrafters-style "Build Your Own Web Server" HTTP/1).

Let me explore the workspace first, then create a plan with milestones, then create the minimal project skeleton.

Per my instructions: Before modifying code, call `explore` once to record files read/intended. For multi-step change, call `plan`. Then `todo_write`, then execute.

Let me start by exploring the workspace structure.工作区是空的，Python 3.14.7 可用。先记录探索结论并制定计划。计划已定，开始创建骨架文件。骨架已建好，进行端到端验证。测试通过，但收尾时 `accept()` 因监听 socket 被关闭抛了线程异常噪音。给 `serve_forever` 加上优雅退出（这也正是 M5 要学的「优雅关闭」雏形）：命令组合方式有误（`&` 把整条链都放进了后台，`wait` 挂住）。拆开执行：端到端验证通过（HTTP 200 + Hello, World!），但后台进程可能残留，清理确认一下：里程碑规划与项目骨架已交付，测试全绿、curl 验证返回 200。

**里程碑路线图**（详见 `README.md`）：

| 里程碑 | 内容 | 验收 |
|---|---|---|
| M0 | TCP 监听 + 硬编码 200 响应（已随骨架完成） | `curl` 返回 Hello, World! |
| M1 | Echo 服务器：理解请求是字节流、`\r\n\r\n` 定界 | 响应体回显原始请求 |
| M2 | 请求解析：`parse_request` → Request 对象，非法请求 400 | 响应体返回 JSON 化的 method/path/headers |
| M3 | 路由与静态文件、路径穿越防御 | `GET /` 返回 HTML，`/../` 攻击被拒 |
| M4 | Response 封装与错误处理（400/404/405/500） | `DELETE /` 返回 405 |
| M5 | 并发：每连接一线程/线程池 | 两个终端同时 curl 互不阻塞 |
| M6 | keep-alive、HEAD、访问日志与压测 | curl 显示 `Re-using existing connection` |

**骨架结构**：

```
├── README.md            # 路线图 + 每步的验收命令
├── server/
│   ├── config.py        # HOST/PORT 集中配置
│   ├── tcp.py           # M0 实现：accept 循环 + 硬编码响应，TODO(M1) 已标注
│   └── __main__.py      # python3 -m server 启动入口
├── static/index.html    # M3 用
└── tests/test_smoke.py  # 裸 socket 冒烟测试（真实连接，不 mock）
```

设计要点：`tcp.py` 里 `TODO(M1)`/`TODO(M5)` 标出了你接下来动手的位置；测试用 `port=0` 临时端口避免冲突；`serve_forever` 已处理监听 socket 关闭时的优雅退出（M5 会正式展开这个话题）。

现在就可以开始 M1：运行 `python3 -m server`，然后把 `server/tcp.py:20` 的 `handle_connection` 改成 echo —— 用 `conn.recv(4096)` 读出请求字节并原样回显，改完跑 `python3 -m unittest discover -s tests -v` 验证。