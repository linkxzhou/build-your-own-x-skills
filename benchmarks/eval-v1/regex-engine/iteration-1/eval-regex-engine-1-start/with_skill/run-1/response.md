The user wants to write their own regex engine in Python, starting from the simplest. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.The skill file is truncated. Let me read the rest of it, and also find the regex track skill.主题映射到 `regex-engine` 轨道，并且有一个针对 Python 的教程技能。正在读取这两个文件。正在读取 track skill 的剩余部分、Python 教程映射，并检查工作区状态。工作区是空的，Python 3.14 已准备就绪。让我从轨道的参考列表中获取上游教程链接。技能链已读完：主题映射到 `regex-engine` 轨道，Python 有对应教程（build-your-own.org 的 Backtracking/NFA/DFA）。轨道规则明确：里程碑制、你写核心代码、每个里程碑有可运行检查点、不一次性倒完整方案。先记录探索结论并立计划，然后搭好里程碑 1 的脚手架。Now create the three files. Let me write them carefully.

regex.py — search given, match_here TODO with docstring pinning the four cases in order.

test_regex.py — 24 cases, cross-checked against re.search, plain runner.

PROGRESS.md — milestone log.

Let me write the files now.运行未实现状态的检查点，验证测试框架本身工作正常。测试框架验证通过：0/24、exit=1、无 BAD-CASE（24 个硬编码期望全部与 `re.search` 一致）。更新进度后交接。**里程碑 1/7 — 字面量 + `.` `^` `$`**，脚手架已就绪（`regex-lab/`）。

**概念**：匹配器是两个互相递归的函数。`search` 负责在文本每个起点尝试（已给你写好）；`match_here` 回答"模式是否从这里开始匹配"——每次只消费模式的一个元素，然后递归处理剩余部分。`^` 只是让 `search` 跳过扫描，`$` 只是模式末尾的一个特殊判断，两者都不需要循环。

**你来写**：`regex-lab/regex.py` 里的 `match_here`，删掉 `NOT_IMPLEMENTED` 那行。函数 docstring 里按顺序列了四个分支：

1. 模式耗尽 → 匹配当且仅当文本也耗尽
2. 模式只剩 `$` → 匹配当且仅当文本耗尽
3. 首字符匹配（相等或 `.`）且文本非空 → 递归 `(pattern[1:], text[1:])`
4. 其余 → False

**检查**：`cd regex-lab && python3 test_regex.py`，期望 `24/24 cases passing`。测试表已逐条和 Python `re.search` 交叉核对过，若有 `BAD-CASE` 输出说明测试表本身有问题，直接告诉我。

卡住时说一声，一次给一个提示。完成后我会把结果记进 `PROGRESS.md`，然后进入里程碑 2（`*` `+` `?` 和回溯）。