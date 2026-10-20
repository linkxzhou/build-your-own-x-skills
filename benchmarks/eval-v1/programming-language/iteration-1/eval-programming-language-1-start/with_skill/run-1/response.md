The user wants to write their own small language interpreter in Python, from step one, guided. This matches the build-your-own-x skill — specifically the interpreter/programming language category. I must read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read more of it, and also find the interpreter track skill. The category map was truncated. Let me read the rest of the SKILL.md and look for the skills directory.主题已映射到 `programming-language` 轨道。让我阅读一下该轨道技能——这是必须的。Let me read the rest of the track skill (truncated at line 709 chars). Let me read from line 33 onwards.轨道技能已读。按流程：先选定上游教程并确认工作区状态，然后定范围、搭好里程碑 1 的骨架。工作区是空的，Python 3.14 可用。按流程先记录探索结论、定计划，然后搭里程碑 1 的骨架。骨架就绪。现在创建 4 个文件：`tiny/lexer.py`（数据模型齐全，核心循环留给你）、`tests/test_lexer.py`（6 个检查点）、`PROGRESS.md`、`tiny/__init__.py`。验证骨架本身能跑：骨架跑通，TODO 状态正确显示。修一下计数显示（TODO 中断时剩余用例应显示为待做，而非失败）：Skeleton verified. Now write the coaching response following the track skill's output format:
- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton/TODO list, not the full answer
- How to check it: command + expected output
- Stuck? one hint at a time

Also update todo s1 completed, s2 in_progress. Then final message.**进度：里程碑 1/7 — Tokenizer。** 骨架已就绪，核心循环留给你写。

**概念（3 句）**：解释器的第一站是词法分析——把原始字符串切成 Token 流，Token 是语言里最小的有意义单位（数字、标识符、`+`、`;`）。每个 Token 带类型、值和行列号，行列号是后面所有报错信息的来源。Tokenizer 逐字符扫描：数字聚成一整个、字母聚成单词再查关键字表，不认识的字符当场报错。之后的解析器和求值器只看 Token，永远不碰原始文本。

**已建好的文件**：
- `tiny/lexer.py` — `TokenType`、`Token`、`LexError` 全部就绪，`tokenize()` 在 `tiny/lexer.py:36` 留了 TODO，6 种情况都列好了
- `tests/test_lexer.py` — 6 个检查点测试
- `PROGRESS.md` — 里程碑表，每过一关我帮你记录

**你写什么**：`tiny/lexer.py:36` 的主循环。结构是 `while i < n`，每轮按 TODO 里的 6 种情况分发；扫数字/标识符时用内层循环连续吃字符，记得先记起始行列号。参考教程：[Let's Build A Simple Interpreter, Part 1](https://ruslanspivak.com/lsbasi-part1/)（Ruslan Spivak）。

**怎么验证**：
```
python3 tests/test_lexer.py        # 目标: 6/6 通过
echo 'let x = 1 + 2;' | python3 -m tiny.lexer
```
第二条的期望输出：
```
LET('let')@1:1
IDENT('x')@1:5
ASSIGN('=')@1:7
NUMBER('1')@1:9
PLUS('+')@1:11
NUMBER('2')@1:13
SEMI(';')@1:14
EOF('')@1:15
```

卡住就说，一次给一个提示。写完把测试输出贴给我，我帮你 review。