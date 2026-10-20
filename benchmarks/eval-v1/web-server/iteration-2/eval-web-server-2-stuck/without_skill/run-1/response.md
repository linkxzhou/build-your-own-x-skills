The user says their web server returns pages but the browser keeps spinning, never finishing loading. This is a classic symptom — usually the server doesn't close the connection properly (missing Content-Length or connection close), or the response is missing a blank line separating headers from body, or the server keeps the connection open without proper keep-alive handling.

Let me explore the workspace first to see what code exists.The workspace is empty. The user says "my web server" — maybe the code is elsewhere, or maybe they haven't shared it. Let me check for hidden files.当前工作目录是空的，我看不到你的服务器代码。请把代码文件放到这个目录，或告诉我代码的路径。

不过这个症状非常典型，大概率是响应没有告诉浏览器“内容到哪里结束”：

1. **缺少 `Content-Length` 且没有关闭连接**（最常见）。HTTP/1.1 默认 keep-alive，浏览器读完 body 后会继续等更多数据，转圈不停。修复方式二选一：
   - 响应头加 `Content-Length: <body字节数>`（注意是字节数，中文等多字节字符要用 `len(body.encode('utf-8'))`）
   - 或加 `Connection: close` 头并在写完响应后调用 `conn.close()`

2. **头部和正文之间少了空行**。headers 结束必须有一个空行 `\r\n\r\n`，少了它浏览器会把 body 当成 header 解析，一直等不到 header 结束。

3. **用 `send()` 而没发完**。TCP 是流式的，`send()` 可能只发了一部分，要循环发送或用 `sendall()`。

一个能正常结束的最小响应长这样：

```python
body = "<h1>Hello</h1>".encode("utf-8")
conn.sendall(
    b"HTTP/1.1 200 OK\r\n"
    b"Content-Type: text/html; charset=utf-8\r\n"
    + f"Content-Length: {len(body)}\r\n".encode()
    + b"Connection: close\r\n"
    + b"\r\n"
    + body
)
conn.close()
```

把你的代码发过来（或放到当前目录），我可以直接定位问题。