The user wants to write a simple browser engine in Python, starting from step one. The workspace is named "build-your-own-x-web-browser-1", which suggests this is a "build your own X" style project. Let me first look at what's in the workspace to understand the context — maybe there's a README or existing structure.

Let me explore the workspace first.空工作区，Python 3.14.7。这是经典的 "build your own browser" 项目——第一步是：手写 HTTP 请求获取网页，并把可见文本打印出来（参考 browser.engineering 第 1 章的思路）。我先记录探索结果并制定计划。Now write browser.py. Key design decisions for step 1 (following browser.engineering chapter 1, but slightly enhanced):

1. `request(url)` — hand-written HTTP/1.0 over socket:
   - Parse URL: scheme://host:port/path
   - Default ports: http=80, https=443
   - For https, wrap socket with ssl
   - Send request: `GET /path HTTP/1.0\r\nHost: host\r\nConnection: close\r\n\r\n`
   - Read response until EOF
   - Parse status line, headers, body
   - Handle redirects (301/302/303/307/308) with Location header — browser.engineering does this in chapter 1 actually (exercise), it's useful. Keep max 10 redirects.
   - Handle `Content-Type: text/html` check? Chapter 1 checks it. Let's include a simple check.
   - Handle entity bodies vs connection-close bodies: with HTTP/1.0 + Connection: close, read until EOF is fine. But some servers send Content-Length; reading to EOF works either way when connection closes.

2. `visible_text(body)` — strip tags:
   - Remove `<script>...</script>` and `<style>...</style>` content
   - Replace `<[^>]+>` with space (tags → space to avoid word joining)
   - HTML entity decoding: use `html.unescape` — is that "cheating"? It's stdlib, fine for step 1. Actually browser.engineering chapter 1 doesn't even do entities; but it makes output nicer. Keep it simple: use html.unescape.
   - Collapse whitespace.

3. `wrap(text, width=80)` — simple word wrap using textwrap? textwrap is stdlib and fine. But writing our own is more in the spirit... textwrap.fill is fine, keep code short. Actually let me write a tiny wrap manually — no, textwrap is fine and idiomatic. Hmm, the spirit of "build your own" is about the browser parts (network, rendering), not text utilities. textwrap is acceptable. But to keep it educational and dependency-light, I'll use textwrap.

4. `main()` — argv[1] URL, default scheme http:// if missing, print text.

Also handle `show("url")` function name like the book? The book uses `show(url)`. I'll structure with `request()` and `show()`.

Edge cases:
- URL without scheme → prepend http://
- Headers case-insensitive → lowercase keys
- Status line parse: `HTTP/1.0 200 OK`
- Redirect: only follow for 301/302/303/307/308, Location may be relative → urljoin? Avoid urllib.parse entirely? Parsing URL manually is part of the exercise. For relative Location, simple join: if starts with "/", scheme://host + location. Keep simple.

Let me write the code. Keep it clean, commented in Chinese (user speaks Chinese) — comments in Chinese would be helpful for learning. I'll write concise Chinese comments.

Code:

```python
#!/usr/bin/env python3
"""简易浏览器引擎 · 第 1 步：请求 URL，打印网页可见文本。

用法:
    python3 browser.py <url>

只用标准库 socket/ssl 手写 HTTP/1.0 请求，不用 urllib / requests。
"""

import html
import socket
import ssl
import sys
import textwrap


def parse_url(url):
    """把 URL 拆成 (scheme, host, port, path)。"""
    if "://" not in url:
        url = "http://" + url
    scheme, rest = url.split("://", 1)
    assert scheme in ("http", "https"), f"不支持的协议: {scheme}"
    # path 是第一个 '/' 之后的部分；没有 '/' 说明请求根路径
    if "/" in rest:
        hostport, path = rest.split("/", 1)
        path = "/" + path
    else:
        hostport, path = rest, "/"
    if ":" in hostport:
        host, port = hostport.rsplit(":", 1)
        port = int(port)
    else:
        host, port = hostport, 443 if scheme == "https" else 80
    return scheme, host, port, path


def request(url, max_redirects=10):
    """手写 HTTP/1.0 请求，返回响应体 bytes。跟随重定向。"""
    for _ in range(max_redirects + 1):
        scheme, host, port, path = parse_url(url)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(10)
        s.connect((host, port))
        if scheme == "https":
            ctx = ssl.create_default_context()
            s = ctx.wrap_socket(s, server_hostname=host)
        req = f"GET {path} HTTP/1.0\r\nHost: {host}\r\nConnection: close\r\n\r\n"
        s.send(req.encode("utf-8"))
        # HTTP/1.0 + Connection: close：读到对端关闭即为完整响应
        chunks = []
        while True:
            chunk = s.recv(8192)
            if not chunk:
                break
            chunks.append(chunk)
        s.close()
        response = b"".join(chunks)

        # 拆状态行 / 头部 / 正文
        head, _, body = response.partition(b"\r\n\r\n")
        lines = head.decode("iso-8859-1").split("\r\n")
        version, status, explanation = lines[0].split(" ", 2)
        headers = {}
        for line in lines[1:]:
            k, _, v = line.partition(":")
            headers[k.strip().lower()] = v.strip()

        assert status in ("200", "301", "302", "303", "307", "308"), (status, explanation)
        if status in ("301", "302", "303", "307", "308"):
            location = headers["location"]
            if location.startswith("/"):
                location = f"{scheme}://{host}:{port}{location}"
            url = location
            continue
        return body
    raise RuntimeError("重定向次数过多")
```

Wait — status line split: `HTTP/1.0 200 OK` — some servers send just `HTTP/1.0 200` without explanation. `split(" ", 2)` fails if only 2 parts. Use partition: `version, _, rest = lines[0].partition(" ")` then `status, _, explanation = rest.partition(" ")`. Safer.

Also content-type check: if headers.get("content-type","").startswith("text/html") — chapter 1 asserts it. For robustness, warn instead of assert? Keep assert-like check but allow missing content-type. I'll do: ctype = headers.get("content-type", "text/html") — hmm, simpler: only check if present and not html → error. Let me include it as a gentle check in show().

visible_text:

```python
def visible_text(body):
    """从 HTML 中提取可见文本：去掉 script/style、剥掉标签、解码实体。"""
    text = body.decode("utf-8", errors="replace")
    # <script>/<style> 的内容对读者不可见，整块删掉
    for tag in ("script", "style"):
        text = re.sub(rf"<{tag}\b[^>]*>.*?</{tag}\s*>", " ", text, flags=re.S | re.I)
    # 标签换成空格，避免相邻文字粘连
    text = re.sub(r"<[^>]+>", " ", text)
    # 解码 &amp; &lt; 等实体
    text = html.unescape(text)
    # 压缩空白
    return " ".join(text.split())
```

Need `import re`.

wrap + main:

```python
def show(url):
    body = request(url)
    text = visible_text(body)
    print(textwrap.fill(text, width=80))


def main():
    if len(sys.argv) != 2:
        print(f"用法: python3 {sys.argv[0]} <url>", file=sys.stderr)
        sys.exit(2)
    show(sys.argv[1])


if __name__ == "__main__":
    main()
```

That's clean. Now test.html with entities, script, style, headings.

Then run local server test and real-site tests. Let me write files and run tests in parallel where possible. Write both files first, then run tests.Now test: start local http.server, run browser.py against it, and test real sites. Start server in background, run tests, kill server.本地测试通过：实体已解码、script/style 内容被剔除、标签剥离后文字无粘连。再验证真实站点的 http / https / 重定向三条路径。All three paths work. Let me update todos and give a concise summary with next steps.第一步完成，`browser.py` 已可用：

```
python3 browser.py example.com
```

**实现内容**（约 100 行，仅标准库，参考 browser.engineering 第 1 章）：

- `parse_url()` — 手工拆解 URL 为 `(scheme, host, port, path)`，无 scheme 自动补 `http://`
- `request()` — 用 `socket` 手写 `GET ... HTTP/1.0` + `Host` + `Connection: close`；https 用 `ssl` 包一层；读到对端关闭即得完整响应；解析状态行/头部/正文，301/302/303/307/308 跟随 `Location`（最多 10 次）
- `visible_text()` — 删除 `<script>`/`<style>` 整块内容 → 标签替换为空格（防粘连）→ `html.unescape` 解码实体 → 压缩空白
- `show()` — `textwrap.fill` 按 80 列换行输出

**验证结果**：
- 本地 `test.html`（含实体、script、style）：实体正确解码为 `& < > '`，脚本和样式内容未泄漏，标签间文字无粘连
- 真实站点：`https://example.com`、无 scheme 的 `example.com`、`http://example.com` 重定向三条路径均输出正常

**已知限制**（后续步骤解决）：不支持 gzip/chunked 编码、不解析相对链接、无缓存。

下一步是第 2 章：给文字加上字号和字体（`<h1>`/`<b>`/`<i>` 区分），把“打印文本”升级为 Tkinter 窗口里的排版显示。