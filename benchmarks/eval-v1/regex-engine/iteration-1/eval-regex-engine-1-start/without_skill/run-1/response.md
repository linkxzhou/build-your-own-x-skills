The user wants to write a regex engine in Python, starting from the simplest possible version. Let me look at the workspace first to see what's there — the directory name suggests this is a "build-your-own-x regex engine" project. Let me check what files exist.

The user speaks Chinese, so I should respond in Chinese.

Let me explore the workspace first.工作区是空的，Python 3.14.7 可用。我先记录探索结论并制定计划，然后动手写第一版。工作区是空的，直接从零开始。先写 v0 引擎和测试。两个失败用例其实是我的预期写错了——`search` 是子串匹配：`a*b` 在 `aaaxb` 末尾的 `b` 处（零个 a）命中，`a*a` 在 `aaab` 的 `aaa` 处命中。引擎行为与标准库一致，修正测试预期并补上锚定版本：v0 完成，35 个用例全部通过，且与标准库 `re.search` 对拍一致。

**两个文件**
- `regex.py` — 引擎本体，三个函数约 40 行：
  - `search` (regex.py:10)：逐起点尝试，处理 `^` 锚点
  - `_match_here` (regex.py:23)：模式剩余部分能否从文本开头匹配，处理 `$`、`.`、字面量
  - `_match_star` (regex.py:38)：`c*` 先试匹配 0 次，失败则多消耗一个字符重试——回溯就藏在这一行里
- `test_regex.py` — 无依赖测试，覆盖字面量、锚点、点号、星号、回溯和空串边界

**这个设计的两个关键点**
1. `search` 里循环到 `len(text) + 1`，允许在文本末尾匹配，这样 `a$` 和空模式才正确。
2. `_match_star` 先试 0 次再递增，天然产生回溯语义：`a*ab` 匹配 `aaab` 时，`*` 会自动让出字符。

**已知局限**（留给后续版本）：切片传参是 O(n²) 拷贝；`*` 前面只能跟单字符；没有 `+`、`?`、字符类、分组。

下一步自然的扩展顺序是 `?` 和 `+`（改 `_match_here` 几行即可）→ 字符类 `[abc]` → 捕获分组（这时值得从“返回布尔”升级为“返回匹配位置”）。