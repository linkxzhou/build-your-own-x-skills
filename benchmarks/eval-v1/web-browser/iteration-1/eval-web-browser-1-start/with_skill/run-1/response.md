The user wants to build a simple browser engine in Python, starting from step one. This matches the build-your-own-x skill — specifically "browser" category. I must read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also find the browser track skill. The category map was truncated. Let me read more of the SKILL.md and look for the browser skill.主题映射到 `web-browser` 轨道，并且有一个与 Python 匹配的 `web-browser-browser-python` 教程技能。现在开始读取这两个文件。两个文件都被截断了。让我阅读剩余的部分和参考文件。环境检查：工作区状态、Python 版本、Tk 可用性（里程碑 2 需要）、网络可达性。环境确认：空工作区、Python 3.14.7、网络可用（example.org 返回 200）。有一个环境限制要先说：这台机器的 Python 缺少 `_tkinter`，里程碑 2 的窗口绘制会用到，届时你需要自己运行安装命令（macOS：`brew install python-tk@3.14`），里程碑 1 用不到，先不阻塞。

按 build-your-own-x 的 web-browser 轨道，Python 跟随 **Browser Engineering** 教程（https://browser.engineering ，第 1 章：https://browser.engineering/http.html ）。路线共 7 个里程碑，每个都有可运行的检查点：

1. Fetch：URL 解析 + socket 发 HTTP GET → `browser http://example.org` 打印 HTML
2. 文本渲染：去标签 + Tk 窗口 + 滚动
3. HTML 解析器：tokenizer + DOM 树
4. CSS + 样式：选择器、优先级、继承
5. 布局：block/inline、折行、盒模型
6. 绘制 + 链接：display list、点击跳转、后退
7. 扩展：嵌入 JS（DukPy）或表单`browser.py` 骨架已就位。当前进度：里程碑 1/7。

**概念（3 句）**：浏览器拿到 URL 后做的第一件事是发起 HTTP 请求。URL 本身是个可解析的结构：`scheme://host:port/path`，scheme 决定默认端口和是否加密。HTTP/1.1 请求就是一段按 `\r\n` 分行的纯文本——请求行、若干头部、空行——服务器回的响应也是同样的格式，头部之后的剩余字节就是 body。

**你来写**：`browser.py` 里的两个 TODO——`URL.__init__` 拆出 scheme/host/port/path，`URL.request()` 用 `socket.create_connection` 建连接、拼请求、按行读响应、返回 body。建议先读一遍教程第 1 章：https://browser.engineering/http.html

**检查**：

```
python3 browser.py http://example.org
```

预期输出一段以 `<html>` 开头、含 "Example Domain" 的 HTML。

卡住了说一声，一次给一个提示。写完贴输出（或报错），我来 review，过了就记进 `PROGRESS.md` 进 M2。