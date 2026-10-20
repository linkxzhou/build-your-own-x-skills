The user wants me to convert the tutorial at https://swtch.com/~rsc/regexp/regexp1.html (Russ Cox's "Regular Expression Matching Can Be Simple And Fast") into a Claude Code executable learning task list.

This matches the build-your-own-x skill — the user wants a hands-on project to learn by rebuilding (a regex engine based on Thompson's construction / NFA simulation). Let me first read the skill file as instructed.

Let me:
1. Read the skill SKILL.md
2. Fetch the tutorial content
3. Then produce a learning task list that Claude Code can execute

Let me start.The skill says I should read the track skill. The topic is "regex engine" — let me check the skills directory for a matching track skill. The skill mentions `skills/<slug>/SKILL.md` and a manifest at `skills/x-skills-manifest.json`. Let me look for a regex track skill.

Also, I should read the rest of the article to build an accurate task list. Let me do both in parallel.There's a `regex-engine-regex-perl` track skill. Let me read it and check for a per-tutorial skill for this specific article, plus get the full article text.The workspace has a per-tutorial skill for exactly this article: `regex-engine-regex-c`. Let me read it, the generic track skill, and its references.The skill's taskify mode is clear: build from the reference map, fetch the source minimally, write `TASKS.md` with per-milestone goal/files/concept/verification, and end with the first runnable checkpoint. I already pulled the article text once; let me extract the technical sections I need, then clean up the temp files (the skill forbids keeping downloads outside the project).I've read the full article. Now let me check the workspace state and the skill's minimal scaffold example, then record the exploration before writing the deliverable.All context is in hand. Writing the deliverable now.Verifying the expected outputs in the task list are actually correct before handing it over:The reference trace exposed a discrepancy: my Python sketch used the wrong decrement semantics, and the top-level `|` emission needs checking against the real source. The article links the full C source — let me verify against it.TASKS.md 中的后缀预期已根据 rsc 的实际算法进行了确认。但我发现了一个测试用例错误：`a(bb)+a` 对比 `abba` —— `abba` 是 a + bb + a，它确实匹配。让我用该文章算法的快速移植版本来验证所有里程碑 3 的预期：我的移植版本中存在一个参数顺序错误（`addstate` 调用）。正在修复：移植版本破坏了 C 语言的指针别名（pointer-aliasing）语义：`list1([s.out])` 复制了值，而 C 语言的 `list1(&s->out)` 持有的是地址。使用可变单元格（mutable cells）进行修复：所有预期结果已验证。TASKS.md 中有两处需要修正：`a(bb)+a` 对比 `abba` 实际上是匹配的（a + bb + a），以及关于计数重复的注释呈现有些笨拙。正在修复这两处：`TASKS.md` 已写入工作区。结构如下：

| 里程碑 | 内容 | 对应文章小节 |
|---|---|---|
| 0 | 环境与骨架 | Introduction |
| 1 | `re2post` 中缀转后缀 | Regular Expressions |
| 2 | Thompson 构造 `post2nfa`（State/Frag/patch） | Converting to NFAs + Compiling to NFA |
| 3 | 多状态 NFA 模拟（clist/nlist/listid 去重） | Simulating the NFA |
| 4 | 复现 `(a?){n}a{n}` 性能对比（自写回溯对照） | Performance |
| 5 | DState 缓存 → 惰性 DFA | Caching the NFA to build a DFA |
| 6 | 选做扩展（字符类、`{n,m}`、Pike VM 子匹配等 8 项） | Real world regular expressions |

每个里程碑含目标、文件、任务分解、验证命令与预期输出、关键概念。所有预期输出都经过验证而非凭印象编写：后缀转换的三个期望值（`abb.+.a.`、`ab.cd.|`、`abc|*.d.`）对照了 rsc 的 `nfa.c` 原始 `re2post` 源码；里程碑 3 的 7 个匹配用例和里程碑 2 的状态数断言用文章算法的忠实移植逐一跑过——期间发现并修正了一处错误（`a(bb)+a` 对 `abba` 实际匹配，负例已换成 `aba`）。

**第一个可运行检查点（里程碑 0）**：

```sh
cc -O2 -o re re.c && ./re 'a' a && echo OK
```

`re.c` 此刻只需 `main` 读两个参数并打印占位输出；命令以 `OK` 结尾即通过，然后对 Claude Code 说"执行里程碑 1"继续。