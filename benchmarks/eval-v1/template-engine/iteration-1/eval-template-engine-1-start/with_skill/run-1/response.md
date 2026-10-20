The user asks in Chinese: "I want to write a Jinja-like template engine in Python, what's the first step?"

This matches the build-your-own-x skill: "an interpreter/compiler/programming language... template engine" — the skill description explicitly mentions "a regex or template engine". Chinese triggers include "从零实现、自己动手写一个 X、手写...解释器...造轮子学原理". So I must read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. I need to see the category map to find the slug for a template engine. Let me read more of the file.模板引擎映射到 `template-engine` 轨道。现在正在读取轨道技能（强制）。The user asked: "我想用 Python 写一个类似 Jinja 的模板引擎，第一步做什么？" (I want to write a Jinja-like template engine in Python, what's the first step?)

Per the track skill:
1. Agree on scope: language (Python — given), target, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide: Python tutorials available:
   - "Approach: Building a toy template engine in Python" (alexmic.net)
   - "A Template Engine" (aosabook.org 500 Lines) — this is the default per the skill: "Default: Python, following the 500 Lines design (compile to a Python function)."
3. Work milestone by milestone.

The skill says default is Python following the 500 Lines design. The user already specified Python and Jinja-like. So scope is mostly settled. I should:
- State where we are (milestone 1/7)
- Explain the concept briefly
- Give a skeleton/TODO, not the full answer
- Give the check command and expected output

The first step: Milestone 1 — variable interpolation: tokenizing {{ }} vs text. render("Hi {{name}}", {name:"A"}) == "Hi A".

Per coaching rules: don't dump full solution. Give skeleton. Ask at most 2 questions — but the user gave language already. I could ask about scope (which features: just {{ }} interpolation first, then {% if %}/{% for %}, filters, inheritance?) — but the milestone table already defines a sensible default scope. The skill says "Ask at most 2 questions, and suggest a default if the learner doesn't care." The user seems eager to start ("第一步做什么？"). I'll propose the default scope and start milestone 1 immediately, maybe with one optional question about whether they want to follow the 500 Lines article closely.

Also should I check the workspace? Let me see what's in the workspace — maybe there's an existing project. Let me glob quickly. Also the skill says record progress in PROGRESS.md when a milestone passes. For now, first step: set up project skeleton + milestone 1.

Let me check the workspace contents first to see if there's existing code.

Also per the system prompt: "Before modifying code, call explore once" — but I'm not modifying code yet; I'm coaching. The user asked "what's the first step?" — I should answer with the coaching format. I don't need to create files yet unless the learner wants. Actually, as a tutor, I could scaffold the project skeleton. But the skill says "Let the learner write the core". The first step is: agree scope, then milestone 1: tokenizer for {{ }}.

Let me check workspace contents to see if there's an existing project directory.

I'll do a quick glob to see what's in the workspace.The workspace only contains the skills directory and AGENTS.md — no existing project. So the learner starts fresh.

Now I'll respond as the tutor per the track skill's output format:

- **Where we are:** milestone 1/7
- **The concept:** short
- **What to write next:** skeleton or TODO list, not the full answer
- **How to check it:** command + expected output
- Stuck? one hint at a time

Also: agree on scope — language is Python (given). Target: Jinja-like subset. Default per skill: follow the 500 Lines design (aosabook "A Template Engine"). I should credit the upstream tutorial with exact link.

The skill says "Ask at most 2 questions, and suggest a default if the learner doesn't care." The user gave language. I can propose the default scope and start milestone 1 right away — the user asked "第一步做什么", so answer directly: 第一步 = milestone 1, variable interpolation tokenizer.

I should give:
1. Scope proposal (default): 支持 {{ }} 插值、HTML 转义、点访问+过滤器、{% if %}/{% for %}、编译为 Python 函数、include/继承。参考 500 Lines 文章。
2. Milestone 1 concept: 模板 = 文本 + {{ }} 标记混合。第一步是把模板字符串切成 token 流（TEXT / VAR），这是所有模板引擎的地基——词法分析（lexing）。
3. Skeleton: project layout + a skeleton of the tokenizer with TODOs, not full solution.
4. Checkpoint: a test render("Hi {{name}}", {name:"A"}) == "Hi A".

Per coaching rules: "Give complete code only for the current milestone, and only when asked, or after the learner has tried." The user asked "第一步做什么" — they want direction, so give skeleton + TODO, let them write the core.

Should I create files in the workspace? The skill says "start milestone 1 in the learner's workspace" after agreeing on scope. But scope agreement — the user hasn't confirmed the scope yet. I think the right move: propose scope briefly, give the milestone-1 skeleton as text (or create the file?). The skill says "Stay in the learner's workspace" — meaning don't install things, work in their workspace. I could create the project skeleton file with TODOs. That's scaffolding, which is allowed ("you scaffold, review and test it"). But "Do not dump a full solution" — a skeleton with TODOs is fine.

Hmm, but should I write files before the learner agrees on scope? The user asked "第一步做什么？" — a question. The best answer: tell them the first step concretely, propose the default scope, and offer the skeleton. I think creating a small skeleton file is helpful and within the tutor role. But the coaching loop says: 1. Explain concept, 2. Show interface or skeleton, 3. Let learner write core. Showing the skeleton can be in the message. Creating the file in workspace makes it concrete and the learner can fill in TODOs.

I'll create the project skeleton: `template_engine/` with `engine.py` containing a skeleton tokenizer + render with TODOs, and a `test_engine.py` with the milestone-1 checkpoint test. Actually, let me keep it minimal: one file `mini_jinja.py` with skeleton + one test file. And PROGRESS.md will be created when milestone passes (skill says record when passed).

Wait — also the system prompt says before modifying code, call `explore` once. I'm creating new files (scaffolding). The explore tool is for recording exploration before editing code. This is a fresh project; there's nothing to explore. But the instruction says "Before modifying code, call explore once to record the files you have read (or intend to read)". I've read the skill files. I could call explore to record this. It's cheap and complies. Then plan? "For any multi-step change (>1 file, >1 logical action, or touching config/tests), call plan" — creating 2 files (engine + test) is a multi-file change. Hmm, but this is a coaching conversation, and the plan tool is for code changes. Creating a skeleton + test is 2 files. To be safe and compliant, I can call explore + plan quickly. But that might be overkill for a tutoring response where the learner writes the code.

Actually, let me think about what's most useful: The user asked "第一步做什么？" The answer should be the coaching response. Creating the skeleton files in the workspace is the scaffold step. I'll do explore (record findings: fresh workspace, skill read, default scope) and plan (3-4 steps: scaffold skeleton, learner fills tokenizer, run checkpoint, record progress). Then create the files. That follows the workflow rules.

Hmm, but plan with seed_todos=true would create todos. That seems reasonable for a multi-milestone project. But the todo list is session-scoped; the project spans many sessions. Still fine.

Actually, let me reconsider: is creating files now premature? The skill workflow step 3: "Agree on scope. Settle the language, the target, the milestone list and how each milestone is checked. Then start milestone 1 in the learner's workspace." The user gave language (Python) and target (Jinja-like). The milestone list is defined by the skill. I can propose the scope and start milestone 1 in the same turn — asking a question and waiting would slow things down; the skill says "suggest a default if the learner doesn't care". The user's question "第一步做什么" signals they want to start. I'll state the scope as a default they can adjust, and scaffold milestone 1.

One question I might ask: 是否要严格跟着 500 Lines 那篇文章走（有 per-tutorial skill），还是按里程碑自由实现？That's 1 question, allowed (at most 2). I'll fold it in as an optional note, defaulting to milestone-driven free implementation with the article as reference.

Let me now write the skeleton. Design for milestone 1 (variable interpolation only):

```python
"""mini_jinja — 一个从零手写的 Jinja 风格模板引擎（教学版）。

里程碑 1：变量插值
    render("Hi {{name}}", {"name": "A"}) == "Hi A"
"""

TEXT, VAR = "text", "var"  # token 类型；里程碑 4 会加 BLOCK


def tokenize(template: str) -> list[tuple[str, str]]:
    """把模板字符串切成 token 流。

    返回 [(kind, value), ...]，kind 是 TEXT 或 VAR。
    例如 "Hi {{name}}" -> [("text", "Hi "), ("var", "name")]

    TODO(你来写):
      1. 用 str.find 或正则找到下一个 "{{"
      2. 它前面的部分是 TEXT token
      3. "{{" 到 "}}" 之间是 VAR token（去掉首尾空白）
      4. 循环直到字符串末尾；没有配对 "}}" 时抛出 TemplateError
    """
    raise NotImplementedError


def render(template: str, context: dict) -> str:
    """渲染模板：把每个 VAR token 换成 context 里的值。"""
    parts = []
    for kind, value in tokenize(template):
        if kind == TEXT:
            parts.append(value)
        else:  # VAR
            # TODO: 从 context 取值；取不到时抛 KeyError 还是渲染成空串？
            parts.append(str(context[value]))
    return "".join(parts)
```

And test file:

```python
from mini_jinja import render

def test_simple_interpolation():
    assert render("Hi {{name}}", {"name": "A"}) == "Hi A"

def test_multiple_and_text_only():
    assert render("{{x}}+{{y}}", {"x": 1, "y": 2}) == "1+2"
    assert render("no tags", {}) == "no tags"

def test_unclosed_tag_raises():
    import pytest
    with pytest.raises(...):
        render("Hi {{name", {})
```

Hmm, for the unclosed tag test, milestone 1 checkpoint per the skill is just render("Hi {{name}}", {name:"A"}) == "Hi A". The unclosed-tag error with line number is milestone 4. I'll keep the test minimal but include a basic unclosed-tag error since the tokenizer TODO mentions it. Actually keep it simple: checkpoint = the one assertion. I'll include 2-3 small tests.

Where to put files? Workspace root. Project dir: `mini_jinja/`? If I make a package dir with engine.py and test file at root... Simpler: create directory `mini_jinja/` containing `engine.py` and `test_engine.py`. Run with `python -m pytest` or plain `python test_engine.py`. To avoid requiring pytest (no installs allowed; pytest may not be present), write tests with plain asserts and a `__main__` runner. Let me check if pytest is available? I shouldn't install anything, but I can check what's available. Actually simpler: plain asserts + main block printing results. Zero dependencies.

Let me decide file layout:

```
mini_jinja/
  engine.py        # 引擎本体（骨架，含 TODO）
  test_engine.py   # 里程碑 1 的检查点测试
```

Run: `cd mini_jinja && python3 test_engine.py` → expected output "Milestone 1 passed: 3/3 tests".

Wait — if engine.py raises NotImplementedError, tests fail. That's the point: learner implements tokenize, then tests pass.

Actually, should render() be complete and only tokenize be TODO? Yes — render is trivial glue; the core learning is the tokenizer. Good.

Now the response format per skill:

- **Where we are:** milestone 1/7
- **The concept:** short (3-6 sentences)
- **What to write next:** skeleton/TODO
- **How to check it:** command + expected output
- Credit upstream tutorial with exact link: http://aosabook.org/en/500L/a-template-engine.html

Also mention scope default (7 milestones) briefly. And one optional question: follow the 500L article closely or free-form? Keep it light.

Tone rules: no filler, lead with answer, no "首先我们需要". Use Chinese since user wrote Chinese. Avoid negation-contrastive phrasing ("不是X而是Y"). Avoid summary stamps. No conditional next-step menus ("如果你想我可以..."). Hmm — the skill says "Then offer the next milestone or a stretch goal" after a milestone passes; that's for later turns. For asking the scope question, I can state it as: "默认按 500 Lines 的设计走；想严格跟原文的话告诉我" — that's a conditional menu-ish? "If you want X, tell me" is a conditional next-step menu. Better: state the default and note the alternative as a parallel positive clause: "默认按里程碑自由实现，参考 500 Lines 的设计；严格跟原文逐段实现也是一种走法，选一个即可。" Hmm that's still menu-ish. The skill instructs to ask at most 2 questions to agree on scope. Asking a question is part of the coaching workflow — I think one short question is fine and required by the skill. I'll phrase: "一个确认：按里程碑自由实现（默认），还是严格跟 500 Lines 原文走？" That's a direct question, allowed by the skill ("Ask at most 2 questions").

Now, tool usage: explore + plan first, then write files. Let me do explore and plan. Actually explore is meant to record files read before editing code. I'll record: read SKILL.md files, fresh workspace, plan to create mini_jinja/engine.py + test_engine.py.

Then plan: goal = scaffold milestone 1 of a Jinja-like template engine in Python. Steps:
1. s1: Create project skeleton mini_jinja/engine.py with tokenize TODO + render glue. verify: file exists, python -c import works.
2. s2: Create checkpoint test test_engine.py (plain asserts). verify: running it fails with NotImplementedError (red).
3. s3: Learner implements tokenize; run checkpoint until green. verify: python3 test_engine.py prints pass.
4. s4: Record milestone in PROGRESS.md. verify: PROGRESS.md contains milestone 1 entry.

Risks: learner may want pytest (not installed — use plain asserts); scope mismatch (Jinja full feature set too big — subset agreed). Rollback: delete mini_jinja/ directory.

seed_todos=true.

Then write the two files. Then respond with the coaching format.

Wait — should I write the files, or show the skeleton in the message and let the learner create them? The skill: "start milestone 1 in the learner's workspace" and "Give an interface or skeleton". Writing the skeleton files into the workspace is scaffolding — good. The learner then fills the TODO. I'll write files.

One more consideration: the system prompt says for multi-step changes call plan with seed_todos. I'll do that. And explore first. Both are quick. Can I call explore and plan in parallel? Plan doesn't depend on explore output. They're independent. But logically explore records what I've read; plan sets up steps. I can call both in one block. Then write files in next block (dependent on nothing, but I want plan/todos set first — actually writes don't depend on plan results). To be safe: call explore + plan together, then write both files together, then maybe run a quick sanity check (python3 -c "import ..." would fail due to NotImplementedError at import? No — NotImplementedError only raised when tokenize called. Import is fine. Test run would fail — that's expected red state. I could run the test to show the learner the starting red state. That's useful: "run it, see it fail with NotImplementedError, then implement". Let me run it to confirm the red state and show expected output.

Actually wait: test_engine.py imports render and calls it → tokenize raises NotImplementedError → test fails with traceback. Expected. I'll run it once to verify the scaffold is wired correctly (error is NotImplementedError from tokenize, meaning glue works).

Let me also double check AGENTS.md at workspace root — it might contain project-specific instructions. I should read it. Let me read it in the same parallel block as explore/plan? Reads are independent. I'll read AGENTS.md first along with explore+plan calls. Hmm, AGENTS.md content might affect how I scaffold. Let me read it in parallel with explore+plan — if it contains relevant constraints I can adjust before writing files (writes happen in the following turn anyway).

Now the engine.py skeleton content. Let me write it carefully, in Chinese comments (user is Chinese-speaking). Keep it a skeleton with TODOs, not the solution.

```python
"""mini_jinja —— 从零手写的 Jinja 风格模板引擎（教学版）。

当前进度：里程碑 1 / 7 —— 变量插值
    render("Hi {{name}}", {"name": "A"}) == "Hi A"

参考：A Template Engine (500 Lines or Less)
http://aosabook.org/en/500L/a-template-engine.html
"""

TEXT = "text"   # 原样输出的文本
VAR = "var"     # {{ ... }} 变量插值
# 里程碑 4 会在这里加 BLOCK（{% if %} / {% for %}）


class TemplateError(Exception):
    """模板语法错误（比如 {{ 没有配对的 }}）。"""


def tokenize(template: str) -> list[tuple[str, str]]:
    """把模板字符串切成 token 流：[(kind, value), ...]。

    例子：
        tokenize("Hi {{name}}!")
        -> [("text", "Hi "), ("var", "name"), ("text", "!")]

    TODO(你来写核心逻辑):
      1. 循环：用 template.find("{{", pos) 找下一个标签起点
      2. 起点之前的片段是 (TEXT, 片段)；找不到 "{{" 时，剩余部分整体是一个 TEXT
      3. "{{" 和 "}}" 之间的内容去掉首尾空白后是 (VAR, 内容)
      4. 找不到配对的 "}}" 时抛 TemplateError
      5. 空模板返回 []
    """
    raise NotImplementedError("里程碑 1：实现 tokenize()")


def render(template: str, context: dict) -> str:
    """渲染模板：TEXT 原样输出，VAR 用 context 里的值替换。"""
    parts = []
    for kind, value in tokenize(template):
        if kind == TEXT:
            parts.append(value)
        else:
            # TODO: 想清楚取不到 key 时的行为——抛 KeyError，还是渲染成空串？
            # Jinja 的默认是“未定义”，这里先选一种并在测试里固定下来。
            parts.append(str(context[value]))
    return "".join(parts)
```

Note: `list[tuple[str, str]]` requires Python 3.9+. Fine.

test_engine.py:

```python
"""里程碑 1 检查点：python3 test_engine.py

全部通过时打印：Milestone 1 passed: 3/3
"""

from engine import render, TemplateError


def test_simple_interpolation():
    assert render("Hi {{name}}", {"name": "A"}) == "Hi A"


def test_multiple_vars_and_plain_text():
    assert render("{{x}} + {{y}}", {"x": 1, "y": 2}) == "1 + 2"
    assert render("no tags here", {}) == "no tags here"
    assert render("", {}) == ""


def test_unclosed_tag_raises():
    try:
        render("Hi {{name", {"name": "A"})
    except TemplateError:
        return
    raise AssertionError("未闭合的 {{ 应该抛 TemplateError")


TESTS = [test_simple_interpolation, test_multiple_vars_and_plain_text, test_unclosed_tag_raises]

if __name__ == "__main__":
    failed = 0
    for t in TESTS:
        try:
            t()
            print(f"PASS {t.__name__}")
        except Exception as e:
            failed += 1
            print(f"FAIL {t.__name__}: {type(e).__name__}: {e}")
    if failed:
        raise SystemExit(f"{failed}/{len(TESTS)} failed")
    print(f"Milestone 1 passed: {len(TESTS)}/{len(TESTS)}")
```

Import: `from engine import render` — works when run from inside mini_jinja dir. Good, zero deps.

Hmm, one design question: should tokenize handle `{{ name }}` with spaces — yes, strip. Covered in TODO.

Now PROGRESS.md — created when milestone passes (step s4), so I don't create it now. Good.

Response structure (Chinese):

**进度：里程碑 1/7 —— 变量插值**

第一步 = 搭骨架 + 写词法分析（tokenizer）。概念 3-6 句：模板引擎的本质是"把混合了占位符的文本翻译成输出"。第一步把模板字符串切成 token 流（TEXT / VAR），这是词法分析；后面所有功能（if/for、过滤器、继承）都建立在 token 流上。Jinja 里 `{{ }}` 是输出表达式，`{% %}` 是语句——里程碑 1 只做前者。

范围（默认，可调）：7 个里程碑——插值 → HTML 转义 → 点访问+过滤器 → if/for → 编译成 Python 函数 → include/继承 → 沙箱（选做）。参考教程：500 Lines "A Template Engine" 链接。

我已在工作区搭好骨架：
- mini_jinja/engine.py — render() 已写好，tokenize() 留了 5 步 TODO 给你
- mini_jinja/test_engine.py — 检查点测试

你要做的：实现 tokenize()。检查命令：`cd mini_jinja && python3 test_engine.py` → 期望输出 `Milestone 1 passed: 3/3`。

卡住了说一声，一次给一个提示。

一个确认：按里程碑自由实现（默认），还是严格跟 500 Lines 原文的结构走？

Wait, the "一个确认" question — the skill says ask at most 2 questions when agreeing on scope. This is fine. But is it a "conditional next-step menu"? It's a scope question required by the coaching workflow, phrased as a direct question. I'll keep it, phrased neutrally.

Also should mention: 当前测试是红的（NotImplementedError），实现后变绿。I'll run the test to confirm and report actual output.

Also credit upstream: include the exact link http://aosabook.org/en/500L/a-template-engine.html — done in engine.py docstring and message.

Now execute: parallel block 1: read AGENTS.md + explore + plan. Then block 2: write engine.py + test_engine.py. Then block 3: bash run test (expect red). Then final message.

Actually — do I need todo_write separately? plan with seed_todos=true populates todos from steps. Good.

Let me write the explore note:

goal: 为"用 Python 从零写 Jinja 风格模板引擎"确定第一步并搭好里程碑 1 的骨架
questions:
- 工作区是否已有相关项目代码？
- template-engine 轨道技能规定的里程碑和检查点是什么？
- 里程碑 1（变量插值）的最小骨架长什么样？
reads: SKILL.md files (already read), AGENTS.md (workspace conventions)
findings:
- 工作区只有技能目录和 AGENTS.md，无既有项目代码（glob 确认）
- 轨道技能 .agents/skills/build-your-own-x/skills/template-engine/SKILL.md:35-45 定义 7 个里程碑，里程碑 1 = 变量插值，检查点 render("Hi {{name}}", {name:"A"}) == "Hi A"
- 默认语言 Python，默认设计参考 500 Lines（aosabook），教程清单在 references/tutorials.md:7-8
unknowns:
- AGENTS.md 是否有额外工作区约定
- 学习者是否想严格跟 500 Lines 原文

plan:
goal: 搭好里程碑 1（变量插值）的可运行骨架，学习者实现 tokenize() 后检查点转绿
assumptions:
- 用户用 Python（已明确），零第三方依赖（标准库 only），避免安装
- 范围取轨道技能默认的 7 里程碑；Jinja 全量特性超出教学范围
steps:
- s1: 创建 mini_jinja/engine.py：TemplateError、tokenize() 骨架（TODO 注释）、render() 胶水。touches: mini_jinja/engine.py。verify: python3 -c "import engine"（在 mini_jinja 下）无语法错误
- s2: 创建 mini_jinja/test_engine.py：3 个纯 assert 测试 + main 运行器。touches: mini_jinja/test_engine.py。verify: python3 test_engine.py 红色失败（NotImplementedError）
- s3: 学习者实现 tokenize()，跑检查点至绿。verify: 输出 Milestone 1 passed: 3/3
- s4: 通过后在 mini_jinja/PROGRESS.md 记录里程碑 1。verify: PROGRESS.md 含里程碑、命令、结果
risks:
- 学习者环境 Python < 3.9（list[tuple] 注解）→ 可改用 typing.List
- pytest 未安装 → 测试用纯 assert + __main__，零依赖
rollback: 删除 mini_jinja/ 目录即可，无外部副作用

Good. Now write files and run.

One more check on the test for unclosed tag: render("Hi {{name", ...) — tokenize should raise TemplateError. In my skeleton, tokenize raises NotImplementedError which is not TemplateError, so test_unclosed_tag_raises raises AssertionError → FAIL. Fine, red state.

Also `from engine import render, TemplateError` — engine.py defines both. Good.

Edge: `render("", {})` → tokenize("") should return [] → render returns "". Good.

Let me also think: should VAR lookup use context[value] directly — if key missing, KeyError propagates. The TODO comment asks the learner to decide. Fine.

Python version check — let me verify python3 exists in the sandbox when I run the test. I'll see from the bash output.

Now, final message formatting: use the skill's output format headers. Keep tight. Chinese. Avoid banned phrasings. Let me draft:

---

**进度：里程碑 1/7 —— 变量插值**

第一步是搭骨架 + 写词法分析（tokenizer）。概念：模板引擎做的事是"把混有占位符的文本翻译成输出"，一切功能都从"把模板切成 token 流"开始——`"Hi {{name}}"` 切成 `[("text","Hi "),("var","name")]`，渲染就是遍历 token、TEXT 原样输出、VAR 查 context 替换。Jinja 的 `{{ }}` 是输出表达式、`{% %}` 是控制语句，里程碑 1 只做前者；if/for 在里程碑 4。

范围（默认，可调）：插值 → HTML 转义 → 点访问+过滤器 → if/for → 编译成 Python 函数 → include/继承 →（选做）沙箱。参考教程：[A Template Engine — 500 Lines or Less](http://aosabook.org/en/500L/a-template-engine.html)。

骨架已建好：
- `mini_jinja/engine.py` — `render()` 胶水已写好，`tokenize()` 留了 5 步 TODO 给你
- `mini_jinja/test_engine.py` — 检查点测试，零依赖

你要写的核心就是 `tokenize()`。检查：

```
cd mini_jinja && python3 test_engine.py
```

现在是红的（NotImplementedError，我刚跑过），实现后应输出 `Milestone 1 passed: 3/3`。卡住说一声，一次给一个提示。

一个确认：按里程碑自由实现（默认），还是严格跟 500 Lines 原文的结构走？

---

Check banned patterns: no "不是...而是", no summary stamps, no conditional menus ("如果你想我可以"). "卡住说一声" is fine. "一个确认：...还是..." is a direct question — acceptable per skill (ask at most 2 questions). Good.

Length is reasonable. Let me execute.AGENTS.md has no extra constraints beyond the skill listing. Now write the two files (s1, s2), then run the test to confirm the red state.The scaffold is wired correctly: all 3 tests fail with NotImplementedError from tokenize, exit code 1. Red state confirmed.

Update todos: s1, s2 completed; s3 in_progress (learner's task). Then final coaching message.**进度：里程碑 1/7 —— 变量插值**

第一步是搭骨架 + 写词法分析（tokenizer）。概念：模板引擎做的事是把混有占位符的文本翻译成输出，一切功能都从“把模板切成 token 流”开始——`"Hi {{name}}"` 切成 `[("text", "Hi "), ("var", "name")]`，渲染就是遍历 token：TEXT 原样输出，VAR 查 context 替换。Jinja 里 `{{ }}` 是输出表达式、`{% %}` 是控制语句，里程碑 1 只做前者，if/for 在里程碑 4。

范围（默认，可调）：插值 → HTML 转义 → 点访问+过滤器 → if/for → 编译成 Python 函数 → include/继承 →（选做）沙箱。参考教程：[A Template Engine — 500 Lines or Less](http://aosabook.org/en/500L/a-template-engine.html)。

骨架已建好，测试我跑过，当前 3/3 红色失败（`NotImplementedError`），接线正确：

- `mini_jinja/engine.py` — `render()` 胶水已写好，`tokenize()` 留了 5 步 TODO 给你
- `mini_jinja/test_engine.py` — 检查点测试，纯标准库，无需安装任何东西

你要写的核心就是 `tokenize()`。检查命令与期望输出：

```
cd mini_jinja && python3 test_engine.py
# Milestone 1 passed: 3/3
```

卡住说一声，一次给一个提示。一个确认：按里程碑自由实现（默认），还是严格跟 500 Lines 原文的结构走？