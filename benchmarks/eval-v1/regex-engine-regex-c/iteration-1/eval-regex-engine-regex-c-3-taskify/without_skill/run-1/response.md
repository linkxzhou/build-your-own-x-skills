The user wants me to convert the tutorial at https://swtch.com/~rsc/regexp/regexp1.html (Russ Cox's "Regular Expression Matching Can Be Simple And Fast") into a Claude Code executable learning task list.

Let me first fetch the article to understand its content, then create a task list that Claude Code can execute — meaning a structured document (like a TASKS.md or LEARNING_PLAN.md) with concrete, verifiable coding tasks based on the tutorial's content.

The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-regex-engine-regex-c-3` — this suggests the user is building their own regex engine, likely in C. Let me check the workspace first and fetch the article in parallel.

Let me start by fetching the article and checking the workspace contents.工作区是空的，文章已取到但被截断。先取全文，确保任务清单覆盖教程所有章节。提取器截断了正文。改用 curl 下载原文到本地再读。The headings got stripped of their text (probably they contain images or the heading text is inside nested tags that got removed). Let me look at the actual content around those lines to identify sections.章节结构已齐。再读实现部分的关键细节（结构体、函数名、文法），确保任务清单引用准确。I now have a complete picture of the article. Let me also check the beginning sections (Regular Expressions, Finite Automata) for the exact syntax covered, and the recursive backtracking section. Let me quickly check lines 108-455 for the key content.I now have the full article content. Let me summarize the article structure:

1. **Introduction** — the two approaches, a?ⁿaⁿ benchmark, Perl vs Thompson NFA
2. **Regular Expressions** — syntax: literals, metacharacters `*+?()|`, escaping, alternation, concatenation, repetition, precedence
3. **Finite Automata** — DFA vs NFA, deterministic vs nondeterministic
4. **Converting Regular Expressions to NFAs** — Thompson's construction: one state per char/metachar, fragment constructions for e1e2, e1|e2, e?, e*, e+
5. **Regular Expression Search Algorithms** — backtracking (recursive, exponential O(2^n)) vs Thompson's simultaneous simulation (O(n²) for a?ⁿaⁿ, O(mn) general)
6. **Implementation** — ANSI C, <400 lines
   - Compiling to NFA: `struct State`, `struct Frag`, `re2post` (infix→postfix with explicit `.` concatenation), `post2nfa`, cases for literal, `.`, `|`, `?`, `*`, `+`
   - Simulating the NFA: `struct List`, `match`, `ismatch`, `addstate` (with listid generation trick, following split arrows), `startlist`, `step`
7. **Performance** — benchmark a?ⁿaⁿ, backtracking O(2ⁿ), Thompson O(n²)/O(mn), PCRE aborts at n=23, Perl memoization incomplete, awk/grep/Tcl build DFAs
8. **Caching the NFA to build a DFA** — `struct DState`, `next[256]`, binary tree lookup with sorted list key, `dstate`, `nextstate`, `startdstate`, on-the-fly DFA construction, cache eviction
9. **Real world regular expressions** — character classes, escape sequences, counted repetition {n,m}, submatch extraction, unanchored matches, non-greedy operators, assertions, backreferences (why they force backtracking), Unicode
10. **History and References** — Rabin/Scott 1959, McNaughton/Yamada, Thompson 1968, QED, ed/grep backtracking, egrep DFA, Rob Pike's sam, Henry Spencer, Tcl
11. **Summary**

Now the user wants: "把这个教程转换成 Claude Code 可执行的学习任务清单" — convert this tutorial into a Claude Code executable learning task list.

"Claude Code 可执行" means the task list should be written so that Claude Code (the CLI agent) can execute each task — i.e., concrete, self-contained, verifiable tasks with clear acceptance criteria, file paths, commands to run. The workspace name suggests "build-your-own-x regex engine regex C" — so the natural output is a TASKS.md (or LEARNING_TASKS.md) file in the workspace that structures a learning path: read sections, implement pieces, test, benchmark.

The workspace is empty. So I should create a task list file. The user speaks Chinese, so the task list should be in Chinese (with code/technical terms in English).

Design considerations for a Claude Code executable task list:
- Each task should be a discrete unit that Claude Code can be given as a prompt (e.g., "Task 1: implement re2post...") with:
  - Goal
  - Background/reference to article section
  - Concrete deliverables (files, functions)
  - Acceptance criteria / verification commands (test cases)
  - Estimated scope
- Tasks should build on each other incrementally: 
  0. Setup project skeleton + test harness
  1. re2post: infix → postfix (shunting-yard), with tests
  2. post2nfa: Thompson construction (State, Frag, patch)
  3. NFA simulation (List, addstate, step, match)
  4. CLI tool + unit tests
  5. Benchmark: a?ⁿaⁿ vs a backtracking implementation (write a naive recursive backtracker to compare) — reproduce the article's graph
  6. DFA cache (DState, dstate, nextstate, startdstate)
  7. Extensions (choose from real-world section): character classes, escapes, counted repetition, unanchored search, submatch extraction (Pike VM is article 2, but the article mentions it)
  8. Write-up: summarize learnings

Also include "reading tasks" — each phase starts with reading a section of the article and answering comprehension questions. Since it's a learning task list, combining reading + implementation + verification is ideal.

Format: a Markdown file, e.g. `TASKS.md` or `LEARNING_PLAN.md`. For Claude Code executability, each task should be copy-pasteable as a prompt. A common pattern: a checklist with `- [ ]` items, each with clear scope and "验收标准" (acceptance criteria) and suggested prompt.

I should keep it focused and practical. Let me write the file in Chinese, with:
- 使用说明 (how to use with Claude Code: feed one task at a time, or use /task commands)
- 任务依赖图
- Phase 0..N tasks, each with: 目标 / 前置 / 参考章节 / 交付物 / 验收标准(可执行命令) / 给 Claude Code 的提示词

Actually, to make it truly "Claude Code 可执行", the best format is: each task is a self-contained prompt block that the user can paste into Claude Code. The prompt includes context, files to create, and acceptance tests. Claude Code can then execute it autonomously.

Let me think about the technical details to get them right:

**re2post**: infix to postfix with `.` as explicit concatenation. Standard shunting-yard. Precedence: `|` (lowest, left-assoc), `.` (implicit, middle), `*+?` (highest, postfix/unary). The article's example: `a(bb)+a` → `abb.+.a.`.

Test cases for re2post:
- `a(bb)+a` → `abb.+.a.`
- `a(b|c)*d` → `abc|*.d.` — let me verify: a, (b|c) → `bc|`, then `*` → `bc|*`, concat with a: `a bc|* .` → `abc|*.`? Hmm wait. Let me carefully derive: infix `a(b|c)*d`. Tokens: a, (, b, |, c, ), *, d. Postfix: a → `a`; (b|c) → `bc|`; `*` applies to (b|c) → `bc|*`; concatenation a·(bc|*) → `abc|*.`; then ·d → `abc|*.d.`. Yes: `abc|*.d.`
- `ab|c` → `ab.c|`? infix ab|c: concat a·b then |c: `ab.` then `|` → `ab.c|`. Yes.
- `a|b|c` → `ab|c|` (left assoc).
- `a**`? Edge case, maybe skip.
- `a+?` — not in scope (non-greedy not supported).

**post2nfa**: as in the article. State struct with c, out, out1, lastlist. Split constant = 256. MatchState = 257. Frag with start + Ptrlist out. Cases: default literal, `.` catenate, `|` alternate, `?` zero-or-one, `*` zero-or-more, `+` one-or-more.

Test: build NFA for `a(bb)+a` and check state count. The article says: exactly one state per character or metacharacter in the regex, excluding parentheses. For `a(bb)+a`: chars a,b,b,+,a = 5 states + 1 match state. Actually each char/metachar creates one state: a(1) b(2) b(3) +(split)(4) a(5), plus matchstate. So post2nfa should create 5 states + match. A test could count states.

**NFA simulation**: List, addstate with listid, startlist, step, ismatch, match. Test cases:
- match("abb.+.a." compiled, "abbbba") == 1
- match("abbbba") full match semantics (anchored, whole string)
- `a?ⁿaⁿ` vs `aⁿ`: e.g. n=3: postfix `a?a?a?aaa.` wait — `a?3a3` = a?a?a?aaa. Postfix: `a?` three times then concat all: a?a?a?aaa → postfix: `a?a?a?aaa...`? Let me derive: tokens a,?,a,?,a,?,a,a,a. Postfix: `a?` `a?` `a?` then concat of all 6: `a?a?a?` then a a a then `.....` (5 dots for 6 items). So postfix = `a?a?a?aaa.....`. Hmm, count: 6 items concatenated need 5 `.`: `a?a?a?aaa` + `.....`. So `a?a?a?aaa.....`. For the test harness, easier to use re2post("a?a?a?aaa").

**Backtracking implementation** for comparison: a simple recursive backtracker on the same postfix or on a parsed AST. The article's point: backtracking is O(2ⁿ) on a?ⁿaⁿ. Task: write `backtrack.c` with recursive matcher, benchmark both, generate CSV/graph. Verification: for n=20ish, NFA finishes in ms, backtracking takes noticeably longer (seconds). Also correctness: both agree on a set of (regex, text) pairs.

**DFA cache**: DState with next[256], left/right tree keyed by sorted list, dstate, nextstate, startdstate, ptrcmp/listcmp. Test: same match results as NFA sim; benchmark shows DFA faster on long inputs (e.g., matching `a?ⁿaⁿ` or repeated matching — DFA cache pays off when matching many strings with same regex, e.g. grep-like usage).

**Extensions** (from real-world section) — pick as optional/stretch tasks:
- E1: character classes `[0-9]`, `.` as any-char (need to change re2post or parse directly)
- E2: escape sequences `\(`, `\\`, `\n`
- E3: counted repetition `{n,m}` expansion
- E4: unanchored search (leftmost-longest) — `.*e.*` trick or explicit
- E5: submatch extraction — Pike VM (points to article 2)
- E6: non-greedy operators — note: doesn't affect whether matches, only submatch boundaries; needs Pike VM

Also a reading-comprehension component: each phase has 2-4 questions from the article (e.g., why does backtracking go exponential? why does Thompson's simulation avoid it? what's the state count bound? why can't DFA-based engines support backreferences?).

Structure of the file:

```markdown
# 学习任务清单：用 C 实现 Thompson NFA 正则引擎
（基于 Russ Cox, "Regular Expression Matching Can Be Simple And Fast"）

## 使用方法（给 Claude Code）
- 逐个任务执行：把「任务提示词」整段粘贴给 Claude Code
- 每个任务有验收标准，执行完必须跑通才算完成
- ...

## 项目结构（最终形态）
regex/
  Makefile
  src/re2post.c ... 
```

Hmm, maybe simpler: single directory with files. Let me design:

```
.
├── Makefile
├── src/
│   ├── regex.c        # State/Frag/post2nfa/NFA 模拟
│   ├── regex.h
│   ├── re2post.c      # infix→postfix（也可并入 regex.c）
│   ├── dfa.c          # DState 缓存（阶段 5）
│   ├── backtrack.c    # 对照用回溯实现（阶段 4）
│   └── main.c         # CLI: regex <regexp> <text...>
├── tests/
│   ├── test_re2post.c
│   ├── test_match.c
│   └── cases.txt
└── bench/
    └── bench.sh / plot
```

Simpler flat layout might be better for a learning project. I'll go with a modest structure.

Task list (each with a paste-ready prompt for Claude Code):

- **T0 环境与骨架**: create Makefile, regex.h stub, main.c CLI that prints "not implemented", test runner script. Verify: `make` compiles, `./regex 'a' abc` runs.
- **T1 阅读 + re2post**: read article sections "Regular Expressions" + "Converting Regular Expressions to NFAs" intro; implement shunting-yard infix→postfix with explicit `.`. Acceptance: unit tests table including `a(bb)+a` → `abb.+.a.`; error on unbalanced parens, dangling operators like `a|`, `*a`? (unary at start invalid), empty.
- **T2 post2nfa Thompson 构造**: implement State/Frag/patch; acceptance: state-count test (one state per char/metachar excluding parens), all fragments patched (no dangling out pointers at end — can assert), `post2nfa("abb.+.a.")` builds and matchstate reachable.
- **T3 NFA 模拟器**: List/addstate/step/match with listid trick. Acceptance: test table of (regex, text, expected) covering `*+?|()`, anchored full-match semantics; e.g. `a(bb)+a` matches `abbbba` but not `abbba`; `a?³a³` matches `aaa`; `(a|b)*abb` matches `babb`... wait full match: `(a|b)*abb` full-matches `aabb`? `(a|b)*abb` against `aabb`: (a|b)* = a, then abb. Yes full match.
- **T4 回溯对照实现 + 基准测试**: implement recursive backtracking matcher (on postfix or AST), verify same results on test table, then benchmark a?ⁿaⁿ for n=2..25 both engines, output CSV, plot or table. Acceptance: NFA time grows ~quadratically, backtracking time doubles per +1 n; document measured numbers in BENCHMARK.md.
- **T5 DFA 缓存**: DState/next[256]/binary tree; acceptance: same match results; benchmark: repeated matching (e.g., match same regex against 10k strings, or long input) shows DFA ≥ NFA sim speedup; verify cache reuse (count dstate allocations — second identical search allocates 0 new DStates).
- **T6 扩展（选做，按文章 Real world 清单）**: escapes + char classes + `{n,m}` expansion + unanchored leftmost-longest search. Each with tests.
- **T7 总结输出**: write SUMMARY.md answering comprehension questions (why exponential vs linear; state bound; why backreferences break DFA; what Pike VM adds), link measurements.

Also include comprehension questions per task (阅读任务). And "给 Claude Code 的执行说明" — how to use: e.g., `claude` then paste task prompt; or use it as a plan file. Maybe also mention that each task prompt is self-contained so it can be run in a fresh session.

I should also embed the key facts from the article into the task prompts so they're self-contained (Claude Code executing the task may not have the article). Include: syntax set (literals, metacharacters `*+?()|`, escaping), precedence (alternation < concatenation < repetition), postfix with explicit `.`, the six compilation cases, State/Frag/List/DState structs, listid trick, benchmark expression a?ⁿaⁿ vs aⁿ, expected complexity O(mn) vs O(2ⁿ).

That makes each prompt executable without re-fetching the article. 

Length: this will be a fairly long file, but that's the deliverable. Keep it tight — maybe ~250-350 lines. Let me be careful to keep each task prompt compact but complete.

Also per instructions: before modifying code, call `explore` once. The workspace is empty (glob returned nothing), and I'm creating a new file. I've done the exploration (fetched article, checked workspace). Let me record an explore note, then plan, then write. Actually the instructions say: "Before modifying code, call `explore` once to record the files you have read (or intend to read)". I've read the article (external) and confirmed empty workspace. I'll call explore + plan, then write the file. Since this is a single-file deliverable, a full plan might be overkill, but the guidance says for multi-step changes call plan. This is one file creation — I'll do explore (consolidate findings) and then write directly. Actually, to be safe and aligned with the workflow, I'll do a quick plan too with seed_todos. Hmm, the todo list for a single write is overkill. The instruction: "For any multi-step change (>1 file, >1 logical action, or touching config/tests), call plan". Creating one markdown file = single logical action. I'll skip plan/todo and just write after explore. That keeps it lean.

One more consideration: the user said "转换成 Claude Code 可执行的学习任务清单" — the deliverable is the task list document itself. I'll write it to `TASKS.md` in the workspace. Maybe name it `LEARNING_TASKS.md`? `TASKS.md` is conventional. I'll go with `TASKS.md`.

Let me now double-check a few technical details for correctness in the prompts:

1. re2post algorithm (from the article's actual source, which I know): it uses nalt/natom counters and paren tracking. I shouldn't paste the article's exact solution code into the task list (that would spoil the learning). Instead give the spec + test vectors. Good — learning task list should specify behavior, not solution. But the article itself contains the full solution for post2nfa/simulation/DFA. The tasks reference article sections where code is given; the learner can choose to transcribe or reimplement. I'll note: "先自己写，再对照原文代码" as a learning suggestion.

2. Test vectors for re2post:
   - `a(bb)+a` → `abb.+.a.` (from article)
   - `a(b|c)*d` → `abc|*.d.` (derived above; let me re-verify: tokens: a ( b | c ) * d. Shunting: output a. `(` push. b output. `|` push. c output. `)` pops `|` → output `bc|`. `*` is postfix unary → output immediately: `bc|*`. d output. Concatenation `.`: when a followed by `(`, natom>1 → emit `.`. Sequence: a, then `.` before (, so output: a b c | * . d . → `abc|*.d.`. ✓.
   - `ab|c` → `ab.c|` ✓ (a b . | c → wait: ab concat → `ab.`, then `|`, then c → `ab.c|`) ✓
   - `(a|b)*abb` → tokens ( a | b ) * a b b. Output: a b | * a b b with dots: after `)` we have `(a|b)` → `ab|`, `*` → `ab|*`, then a → concat dot: `ab|*.a`, b → `ab|*.a.b`, b → `ab|*.a.b.b`. So `ab|*.a.b.b` ✓
   - `a?a?a?aaa` → `a?a?a?aaa.....`? tokens: a ? a ? a ? a a a. Output: a ? → `a?`; then a: concat dot → `a?.a?`... hmm wait. Let me redo. Infix: a? a? a? a a a with implicit concatenation between each. Postfix: `a?` `a?` `a?` `a` `a` `a` then dots between consecutive: 5 dots. So `a?a?a?aaa.....` — count dots: 5. String: `a?a?a?aaa` followed by `.....`. ✓
   - Error cases: `a(` , `a)`, `(a`, `*a`, `a|`, `|a`, empty → return NULL.

3. State count test: for postfix `abb.+.a.` (from `a(bb)+a`): states created: a, b, b, +, a → 5 states + matchstate. Each literal creates 1 state; each of `.|?*+` creates 1 (Split). So state count = number of non-paren chars in infix regex. For `a(bb)+a`: 5. Test: count states in built NFA (walk all states from start, or count via state() calls). Walking requires traversing both out and out1 with visited set — good exercise. Acceptance: count(`a(bb)+a`) == 5 (+1 match), count(`(a|b)*abb`) == 7 (a,b,|,*,a,b,b = 7). ✓ article: "exactly one state per character or metacharacter in the regular expression, excluding parentheses".

4. Match semantics: full-string (anchored) match, like the article's `match(start, s)` returns ismatch(clist) after consuming all of s. Test table:
   - (`abb.+.a.`, "abbbba") → 1; ("abbba") → 0; ("aba") → 0; ("abbbba" prefix "abbba b"?) keep simple.
   - (`a?a?a?aaa.....`, "aaa") → 1
   - (`ab|*.a.b.b` i.e. `(a|b)*abb`, "aabb") → 1; ("abb") → 1; ("abab") → 0
   - (`a*`, "") → 1 (empty string: loop doesn't run, clist=start list; a* start split → addstate follows split to a-state and out1→match? wait: for `a*`, frag: split→(a→back to split), split.out1 dangling patched to matchstate. addstate(start) follows split: adds a-state and matchstate. ismatch → 1. ✓ empty matches a*.)
   - (`a+`, "") → 0. For `a+`: split→a, a.out patched back to split, split.out1 → match. startlist: addstate(split) → follows to a-state and matchstate?? Wait — addstate follows unlabeled arrows recursively: split's out → a (labeled, added), split's out1 → matchstate (added!). Hmm, that would make empty string match a+?! Let me re-check the article's `+` construction:

```
case '+':
	e = pop();
	s = state(Split, e.start, NULL);
	patch(e.out, s);
	push(frag(e.start, list1(&s->out1)));
	break;
```

So split.out = e.start (the a state), split.out1 = dangling (patched to matchstate at end). addstate(split): split is Split → addstate(out=a) adds a; addstate(out1=matchstate) adds matchstate. So initial list contains matchstate → empty string matches a+?!

Hmm wait, that can't be right. Let me re-check addstate: it follows split arrows. For e+ = split(a, matchstate). Initial list after addstate(start=split): visits split → recurses out (a) and out1 (matchstate). Both get added. ismatch → true for empty string. That's wrong semantically!

Hold on — let me recheck the `?` case:
```
case '?':
	e = pop();
	s = state(Split, e.start, NULL);
	push(frag(s, append(e.out, list1(&s->out1))));
	break;
```
For e?: split.out = e.start, split.out1 = dangling. Empty match: addstate(split) → out: e.start (a, added), out1: matchstate (added). ✓ a? matches empty. Correct.

For `+`: same structure — split(e.start, dangling-out1). Empty: split → a added, out1 → matchstate added. Empty matches a+?? That's semantically wrong. Let me recheck the actual article code... From my reading above:

```
One or more:
`
case '+':
	e = pop();
	s = state(Split, e.start, NULL);
	patch(e.out, s);
	push(frag(e.start, list1(&s->out1)));
	break;
`
```

Hmm wait, but actually let me recheck: is it `state(Split, e.start, NULL)`? In the real regexp1.c source (I recall it):

```c
case '+':	/* one or more */
	e = pop();
	s = state(Split, e.start, NULL);
	patch(e.out, s);
	push(frag(e.start, list1(&s->out1)));
	break;
```

Yes that's the actual code. And addstate:

```c
void
addstate(List *l, State *s)
{
	if(s == NULL || s->lastlist == listid)
		return;
	s->lastlist = listid;
	if(s->c == Split){
		/* follow unlabeled arrows */
		addstate(l, s->out);
		addstate(l, s->out1);
		return;
	}
	l->s[l->n++] = s;
}
```

So for `a+`: NFA is split → (a → split), split → matchstate (via out1 patched at end). Start list: addstate(split) → addstate(a) [added], addstate(matchstate) [added]. Empty string: clist contains matchstate → ismatch returns 1. So `a+` matches empty string?!

That contradicts semantics. Wait... let me re-trace. patch(e.out, s): e.out is the dangling out-pointer of the a state (s->out of literal a). It gets patched to s (the split). So a → split. split.out = e.start = a. split.out1 = NULL initially, then frag(e.start, list1(&s->out1)) — the fragment's start is e.start (a), and dangling arrows = [&s->out1]. At the end, patch(e.out, matchstate) sets split.out1 = matchstate.

So the graph: split.out1 → matchstate, split.out → a, a.out → split.

startlist: addstate(split): split is Split → addstate(a), addstate(matchstate). a is literal → added to list. matchstate added to list. So clist = {a, matchstate}. ismatch(clist) → 1. Empty string matches a+.

Hmm, that seems like a bug, but this is the canonical rsc code... Let me think again. Actually wait — I mis-recalled. Let me look at the actual regexp1.c from swtch.com. From memory of the real source:

```c
case '+':	/* one or more */
	e = pop();
	s = state(Split, e.start, NULL);
	patch(e.out, s);
	push(frag(e.start, list1(&s->out1)));
	break;
```

Hmm, and the NFA diagram in the article for e+: "The NFA for e+ also creates a loop, but one that requires passing through e at least once". The diagram: split with one arrow into e, e loops back to split, and split's other arrow goes to... the dangling out. So split.out1 is the dangling arrow (skip path). But then the skip path means empty match!

Wait, no. Let me think about the e+ diagram more carefully. For e+ you need: enter e, after e either loop back or exit. The construction: split state S with S.out → e.start (enter e), e's out patched → S (loop back), S.out1 → dangling (exit). But then from S you can exit without passing e — since S is the start, empty matches. Unless... the fragment's start is e.start (as in the code: push(frag(e.start, ...))), so the NFA's start is a, and S is only reachable after passing through a at least once!

Yes! That's the trick: the fragment returned has start = e.start (a), and the split S is embedded in the loop. The dangling out1 of S becomes the fragment's out. So the NFA for a+: start at a. a → S. S → a (loop) or S → matchstate (exit). Start list = {a} only (addstate(a) — a is a literal, added; no split at start). Empty string: clist={a}, ismatch → 0. ✓ After matching one 'a': step adds S.out... wait step: for state a with c=='a', addstate(nlist, a->out) = addstate(S) → S is split → adds a and matchstate. So after one char, list = {a, matchstate} → match. ✓ 

So the key: for `+`, the split is NOT the fragment start; e.start is. My earlier trace wrongly assumed split was the start. The code `push(frag(e.start, list1(&s->out1)))` — start is e.start. ✓ No bug. Good.

Similarly for `*`: 
```
case '*':
	e = pop();
	s = state(Split, e.start, NULL);
	patch(e.out, s);
	push(frag(s, list1(&s->out1)));
	break;
```
Fragment start = split S. S → e.start or S → dangling(out1→matchstate). Start list: addstate(S) → adds e.start(a) and matchstate. Empty matches a*. ✓

OK so my test expectations hold: `a+` empty → 0, `a*` empty → 1.

5. Backtracking reference implementation: simplest is recursive on the NFA structure (try both split branches with memo off) or on postfix directly. Classic approach: recursive matcher over the NFA graph:

```c
int backtrack(State *s, char *p) {
    if (s == matchstate) return *p == '\0';
    if (s->c == Split)
        return backtracking(s->out, p) || backtracking(s->out1, p);
    if (s->c == *p)  // careful: *p could be '\0'
        return backtracking(s->out, p+1);
    return 0;
}
```
Wait but matchstate check: if s==matchstate, need *p=='\0' for full match. And Split: try out then out1 with same p. Literal: if *p == s->c advance. This gives exponential behavior on a?ⁿaⁿ. ✓ (Note: with this formulation, matchstate reached mid-string fails unless at end — correct for full match.) Edge: *p == '\0' and s->c == 0? c==0 would be literal NUL — not in our alphabet; Split=256, Match=257, so fine.

This is a clean reference backtracker that reuses post2nfa. Good for T4: "reuse the NFA, replace simulation with recursive backtracking" — nicely isolates the algorithm difference, exactly the article's point.

6. Benchmark: n from 2 to 24 (backtracking 2ⁿ steps: n=24 → 16M recursive calls, ~seconds; n=25 → 33M, maybe 10-30s in debug; cap at n=22-25 with a timeout). Output CSV: n, nfa_us, bt_us. Acceptance: bt(n+1)/bt(n) ≈ 2; nfa stays µs–ms. Also mention PCRE aborts at n=23 (article) as trivia. For plotting: generate CSV + optional gnuplot/python matplotlib script; acceptance = CSV exists and trend documented in BENCHMARK.md.

7. DFA cache tests: 
   - Same match results as NFA sim on the full test table.
   - Cache reuse: after first match, run again; count DStates allocated (instrument counter) — second run allocates 0.
   - Speed: matching a long string (e.g., 1MB of 'a' with regex `a*`) — DFA does 1 step/char vs NFA sim's list ops; or repeated matches. Acceptance: measurable speedup documented.

8. Extensions (T6, optional): 
   - E1 escapes: `\(`, `\)`, `\\`, `\+`, `\n`, `\t` — in re2post (treat escaped char as literal token).
   - E2 char classes: `[abc]`, `[a-z]`, `[^abc]`, and `.` = any char (changes the meaning of `.`! The article notes a real implementation uses dot as any-char, so concatenation must become implicit — this forces moving from "explicit dot postfix" to either a different postfix marker or direct parsing. Simplest: keep explicit concat operator but use a different internal char (e.g. 0x08 or a constant CONCAT) and free `.` for any-char.) Good learning note.
   - E3 counted repetition `{n}` `{n,}` `{n,m}`: expand at parse level: e{3} → eee; e{3,5} → eee e? e?; e{3,} → eee e+ (article gives exactly these expansions). ✓
   - E4 unanchored search: leftmost-longest substring; article: unanchored search for e ≈ `.*?e.*` with first .* shortest — but with pure full-match engine, simplest: try match at each start offset (O(n²) worst) — acceptable; leftmost-longest needs submatch tracking → point to Pike VM (article 2). Scope: implement "find leftmost match" (any-length) via start-offset loop; note longest requires article 2 techniques.
   - E5 submatch extraction: Pike VM — mark as advanced, references article 2 (https://swtch.com/~rsc/regexp/regexp2.html), optional.

9. Comprehension questions (阅读任务), from article:
   - Q1: 为什么回溯实现在 a?ⁿaⁿ 上是 O(2ⁿ)？Thompson 模拟为什么是 O(n²)（对固定 regex 是 O(n)）？
   - Q2: Thompson 构造的 NFA 状态数上界是多少？为什么？
   - Q3: addstate 如何用 listid 避免重复添加状态、避免每步 O(n) 查重？
   - Q4: 为什么 DFA 引擎天然无法支持 backreferences？（文章：backreferences 是唯一迫使回溯的特性）
   - Q5: 缓存 DFA 时如何用内存换时间？缓存满了怎么办（文章：可全部丢弃，因为只是 step 的缓存）？
   - Q6: 贪婪/非贪婪影响什么、不影响什么？（不影响是否匹配，只影响子匹配边界）

10. Claude Code usage instructions: 
    - 方式 A：逐任务粘贴「任务提示词」到 claude 会话。
    - 方式 B：一次性把 TASKS.md 交给 Claude Code，让它按顺序执行并自验（每个任务有验收命令）。
    - 每个任务完成后勾选 checkbox。
    - 建议每个任务一个 git commit。

Also include a "全局约定" section: C99/ANSI C, single dir layout, Makefile targets (all, test, bench), test framework = simple assert-based (no deps), full-match semantics, ASCII input.

Now, file naming and structure. I'll write `TASKS.md`. Let me draft it in Chinese, compact but complete. I'll aim for a well-organized doc where each task has: 目标 / 参考 / 交付物 / 验收标准 / 提示词块 (a fenced block the user can paste directly to Claude Code).

Actually, to avoid duplication: make the 提示词块 itself the complete spec (so paste = executable), and keep the surrounding description minimal (one line + checkbox). That reduces redundancy. Structure per task:

```
### T1 · 中缀转后缀 re2post
- [ ] 状态：未开始
**参考**：原文 "Regular Expressions" 与 "Implementation: Compiling to NFA" 开头
**提示词**（整段复制给 Claude Code）：
> ```text
> 在现有项目里实现 re2post...（完整规格+验收）
> ```
```

Hmm, nested code fences in markdown: use ~~~ or 4-backtick outer fence. I'll use four backticks for outer, three for inner. Or simpler: make each prompt a fenced block with ```text and the outer document doesn't need fencing around it. Fine.

Let me also decide the project layout to specify in T0:

```
regex-engine/
├── Makefile
├── src/
│   ├── regex.h      # State/Frag/List/DState 声明与常量
│   ├── regex.c      # post2nfa + NFA 模拟
│   ├── re2post.c    # re2post()
│   ├── dfa.c        # DState 缓存（T5 加入）
│   ├── backtrack.c  # 回溯对照（T4 加入）
│   └── main.c       # CLI
└── tests/
    ├── test_main.c  # 极简断言测试器
    └── testdata.txt # (regex, text, expected) 用例表
```

Makefile targets: `make` (build regex CLI), `make test` (build & run tests), `make bench`.

CLI: `./regex <regexp> <text>` → exit 0 match / 1 no match / 2 error; prints nothing (unix style) or prints "match"/"no match". Keep: exit code semantics for scriptability.

Test vectors table (tests/testdata.txt): I'll embed a concrete table in the task prompt so acceptance is objective:

```
a(bb)+a	abbbba	1
a(bb)+a	abbba	0
a(bb)+a	aba	0
a?a?a?aaa	aaa	1   (infix written as a?a?a?aaa)
(a|b)*abb	aabb	1
(a|b)*abb	abab	0
a*	(empty)	1
a+	(empty)	0
a|b|c	c	1
a|b|c	d	0
(a*)*b	aaab	1
```

Note: empty text representation in the file — use a marker like `-` or just document. I'll say empty line field uses `∅` or specify "空文本用两个连续 tab 或 <empty>"。Simpler: put test cases directly in C arrays in test_main.c instead of a data file. Yes — simpler: test cases as C string array {pattern, text, expected}. Avoid file-format ambiguity.

re2post test vectors (in T1):
- "a(bb)+a" → "abb.+.a."
- "a(b|c)*d" → "abc|*.d."
- "ab|c" → "ab.c|"
- "(a|b)*abb" → "ab|*.a.b.b"
- "a?a?a?aaa" → "a?a?a?aaa....."
- "a**" → "a**"? a** : a then * then *: postfix "a**" ✓ valid input, output "a**".
- errors: "a(", "a)", "(a", "*a", "a|", "|a", "" → NULL

Wait "a**" — is `*` after `*` valid? a** = (a*)* — yes valid regex, postfix "a**". Fine, include.

State-count vectors (T2):
- "a(bb)+a" → 5 NFA states (+1 matchstate)
- "(a|b)*abb" → 7
- "a" → 1
- "a|" → invalid... skip.
- "a**" → 2 (a and one *)

Count method: traverse from start state following out/out1, count unique states excluding matchstate, or instrument state() allocation counter. I'll suggest instrumenting (simpler, exact).

Benchmark specifics (T4): 
- regex: a?ⁿaⁿ (infix `a?a?a?...a` with n ?-groups then n a's, i.e. infix = "a?"*n + "a"*n), text = "a"*n.
- n = 2,4,8,...,24 (or 2..25 step 1). Measure with clock_gettime(CLOCK_MONOTONIC) or gettimeofday; report µs.
- Expected: backtracking roughly doubles each +1 n; NFA grows ~quadratically but stays tiny. Record table in BENCHMARK.md. Stop backtracking at n where runtime > 5s (note it).
- Also correctness cross-check: both engines agree on all test-table cases.

DFA (T5) specifics from article: DState {List l; DState *next[256]; DState *left, *right;}; key = sorted list (qsort by pointer, listcmp); dstate() looks up/inserts in BST; nextstate(d,c) = step + dstate; startdstate. match loops d = d->next[c] ?: nextstate. Acceptance: (1) all test cases pass via DFA path; (2) instrument: second identical match allocates 0 new DStates; (3) bench: e.g. match `a?¹⁰a¹⁰`-style or better: long text — use regex `(a|b)*abb`? Hmm DFA advantage shows on long inputs: text = 100k 'a' + 'b' with regex `a*b`: NFA sim does list ops per char; DFA does array lookup. Measure both, expect DFA faster. Or reuse a?ⁿaⁿ with large n and long text. I'll specify: text = 'a'×100000 + 'b', regex `a*b`, compare NFA sim vs DFA, record µs in BENCHMARK.md; expect DFA ≥ 2× faster (rough). Also memory note: cache can be dropped entirely when full (article point).

T6 extensions with per-item acceptance:
- E1 escapes `\(` `\\` `\n` `\t`: tests: `a\+b` matches "a+b" not "aab"; `\n` matches newline.
- E2 char classes `[abc]`, `[a-z0-9]`, `[^x]`, `.` any-char (note: requires reserving concat operator internally — suggest using a non-printable constant like `\x08` or enum token; article notes real impls build NFA during parsing). Tests: `[0-9]+` full-match "123"; `.` matches "x"; `[^a]` matches "b" not "a".
- E3 counted repetition: e{3} → eee; e{3,5} → eee e? e?; e{3,} → eee e+ (article's exact expansions). Tests: `a{3}` matches "aaa" not "aa"/"aaaa"; `a{2,3}` matches "aa","aaa" not "a"; `a{2,}` matches "aaaa".
- E4 unanchored: CLI flag or new mode: leftmost match. Tests: pattern `b` text "abb" → found at offset 1. Note leftmost-longest needs submatch (article 2). Acceptance: `./regex -f b abb` style or `--find`.
- E5 (stretch) Pike VM submatch: implement per article 2, test `([0-9]+)-([0-9]+)` extraction. Mark optional.

T7 summary: SUMMARY.md with answers to Q1-Q6 + benchmark table + 复盘 (what surprised you). 

Also add "里程碑验收" overall: `make test` all green; `make bench` produces BENCHMARK.md data; CLI usable: `./regex '(a|b)*abb' aabb` → exit 0.

Now the usage instructions for Claude Code at top:

```
## 怎么用（Claude Code）
1. 在项目根目录启动 `claude`
2. 按顺序把每个任务的「提示词」整段粘贴执行；或直接说"执行 TASKS.md 里的下一个任务"
3. 每个任务必须跑通验收命令后才能勾选；建议每任务一个 commit
4. 任务提示词自包含：不依赖会话上下文，新会话也能执行
```

Also a dependency note: T0→T1→T2→T3→T4→T5→(T6 任选)→T7; T4 依赖 T3；T6 各项相互独立。

Length check: this will be ~300 lines. Acceptable for the deliverable.

One more thing: the article URL and section names should be cited so the learner can read along. Include a "阅读地图" table mapping tasks → article sections.

Also mention article's key numbers in prompts where relevant (e.g., "原文实现 <400 行 C").

Let me also double check re2post vector "(a|b)*abb" → "ab|*.a.b.b": tokens: ( a | b ) * a b b. Output: a, b, then `)` emits `|` → "ab|", `*` postfix → "ab|*", then implicit concat before a → ".", "a", concat ".", "b", concat ".", "b" → "ab|*.a.b.b". ✓

And "a(b|c)*d" → "abc|*.d." ✓ derived earlier.

And "a?a?a?aaa" → "a?a?a?aaa.....": tokens a ? a ? a ? a a a; output: a,? → "a?"; then concat dot before next a: "a?.a?"... wait order: after first "a?", next token is 'a' with implicit concat → emit "." then "a", then "?" → "a?.a?"; concat "." + "a" + "?" → "a?.a?.a?"; then a: "." → "a?.a?.a?.a"; a: "." ; a: "." → "a?.a?.a?.a.a.a". Hmm! That gives dots BETWEEN each: "a?.a?.a?.a.a.a" — 5 dots total but interleaved: after each a? group and between the trailing a's. Let me recount: 6 operands (a?, a?, a?, a, a, a) joined by 5 concat dots: "a?" "." "a?" "." "a?"I was in the middle of verifying the re2post test vector for `a?a?a?aaa`. Let me finish that verification and then write the TASKS.md file.

The postfix for `a?a?a?aaa`: 6 operands (a?, a?, a?, a, a, a) joined by 5 concat dots: "a?" "." "a?" "." "a?" "." "a" "." "a" "." "a" → "a?.a?.a?.a.a.a". 

Earlier I wrote "a?a?a?aaa....." which was wrong — the dots are interleaved between operands, not trailing. Correct vector: `a?a?a?aaa` → `a?.a?.a?.a.a.a`.

Let me double check with the shunting-yard logic: tokens: a, ?, a, ?, a, ?, a, a, a with implicit concat between all consecutive pairs where natom > 1.

- 'a': output "a", natom=1
- '?': postfix unary, output "a?", still natom=1
- implicit concat before next 'a': natom>1? natom=1... hmm, actually the article's re2post logic: after `?`, natom stays (the ? applies to the atom). Let me think about the actual algorithm from the article's source:

```c
case '?':
    if(natom == 0) return NULL;
    break;  // falls to emit postfix char, then natom stays? 
```

Actually the real code:
```c
default:
    if(natom > 1){ --natom; strcat(buf, "."); }
    ...
    natom++;
    break;
case '?':
case '*':
case '+':
    if(natom == 0) return NULL;
    strcat(buf, *p);  // emit operator
    break;
```

Hmm, for `?` after an atom: natom was 1 (just the a), `?` emits, natom stays 1. Then next 'a': natom==1, no dot emitted?? That would give "a?a" without dot — wrong!

Wait, let me recall the actual code more carefully. The real re2post from regexp1.c:

```c
char*
re2post(char *re)
{
	int nalt, natom;
	static char buf[8000];
	char *dst;
	struct {
		int nalt;
		int natom;
	} paren[100], *p;
	
	p = paren;
	dst = buf;
	nalt = 0;
	natom = 0;
	if(strlen(re) >= sizeof buf/2)
		return NULL;
	for(; *re; re++){
		switch(*re){
		case '(':
			if(natom > 1){
				--natom;
				*dst++ = '.';
			}
			*p++ = nalt;
			*p++ = natom;
			nalt = 0;
			natom = 0;
			break;
		case '|':
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			nalt++;
			break;
		case ')':
			if(p == paren)
				return NULL;
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			for(;;){
				int c = *--p;
				if(c == '(')
					break;
				*dst++ = c;
			}
			natom++;
			nalt += ... 
```

Hmm, I don't remember it exactly. The key question: after `a?`, is natom still 1 or does `?` not change natom? In the real code:

```c
		case '?':
		case '*':
		case '+':
			if(natom == 0)
				return NULL;
			*dst++ = *re;
			break;
```

So `?` emits but doesn't change natom. After "a?", natom=1. Then next 'a': natom==1, so no dot emitted → "a?a" — that would be WRONG for a?a?a?aaa.

Hmm wait, but actually let me reconsider. For `a?a?a?aaa`, the correct postfix is "a?.a?.a?.a.a.a" (5 dots). If re2post as I recalled doesn't emit dots after `?`, it would produce "a?a?a?aaa" with dots only between the trailing a's: "a?a?a?a.a.a" — that's wrong (it would parse as a? a? a? a.a.a concatenated without dots between the a? groups... actually in postfix without explicit dots between "a?" and "a?", the post2nfa compiler would treat consecutive fragments... no wait, post2nfa only concatenates on '.' — "a?a?a?a.a.a" would leave 4 fragments on the stack at the end → error or wrong result).

So my recollection of the code must be off. Let me think about what the actual code does. Actually I recall the real code has:

```c
		case '?':
		case '*':
		case '+':
			if(natom == 0)
				return NULL;
			*dst++ = *re;
			break;
```

and for default (literal):
```c
		default:
			if(natom > 1){
				--natom;
				*dst++ = '.';
			}
			*dst++ = *re;
			natom++;
			break;
```

With this: "a?a?a?aaa":
- 'a': natom=0→ no dot, emit 'a', natom=1
- '?': emit '?', natom=1
- 'a': natom==1, not >1, no dot, emit 'a', natom=2
- '?': emit '?', natom=2
- 'a': natom>1 → emit '.', natom=1, emit 'a', natom=2
- '?': emit '?', natom=2
- 'a': emit '.', natom=1, emit 'a', natom=2
- 'a': emit '.', natom=1, emit 'a', natom=2
- 'a': emit '.', natom=1, emit 'a', natom=2

Result: "a?" + "a?" + ".a?" + ".a" + ".a" + ".a" = "a?a?.a?.a.a.a"

Hmm that gives "a?a?.a?.a.a.a" — 4 dots. Is that correct postfix for a?a?a?aaa?

Parse: a? a? . a? . a . a . a → ((a?a?)·a?)·a·a·a. Concatenation is associative, so (a?·a?)·a? == a?·(a?·a?) — semantically equivalent! Postfix "a?a?.a?.a.a.a" evaluates: push a?, push a?, '.' pops two → concat. Yes it's valid and equivalent. The dot placement differs from my hand-derived "a?.a?.a?.a.a.a" but both are correct postfix for the same regex (left-assoc vs my right-ish grouping). Both evaluate to the same NFA language.

So which is "the" expected output? It depends on implementation details. For a test vector, I should either use the article's own example (a(bb)+a → abb.+.a.) as the canonical vector, and for others verify semantic equivalence by compiling both and testing matches, rather than exact string equality. That's more robust for a learning task: exact-string tests would over-constrain implementations that group differently.

Hmm, but wait — actually let me re-derive "a(bb)+a" with the algorithm: 
- 'a': emit 'a', natom=1
- '(': natom==1, no dot; push (nalt=0, natom=1); reset nalt=0, natom=0
- 'b': emit 'b', natom=1
- 'b': natom>1? natom==1, no dot; emit 'b', natom=2
- ')': natom>0; while(--natom>0) emit '.' → natom=2→ emit '.', natom=1; pop paren: nalt=0, natom=1; then natom += nalt... the real code: after popping until '(', it does `natom += nalt`? Hmm: after ')', natom should be the group as one atom: natom=1 (from inside) + ... the code sets `natom++`? Let me just trust: after ')', group counts as 1 atom, so natom = paren.natom + max(paren.nalt stuff)... 

Actually the real code for ')':
```c
		case ')':
			if(p == paren)
				return NULL;
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			for(;;){
				int c = *--p;
				if(c == '(')
					break;
				*dst++ = c;
			}
			natom++;
			break;
```

Wait that pops nalt/natom counts... no, the paren stack stores nalt and natom as two ints; the `for(;;)` loop pops the saved nalt (if nalt>0, emits '|') then natom. Hmm, the stack stores pairs; the loop pops until '(' — it pops nalt first: if nalt != 0... Actually the code:

```c
			for(;;){
				int c = *--p;
				if(c == '(')
					break;
				*dst++ = c;
			}
```

Hmm, that pops values and emits them — but nalt/natom are ints, not chars. I'm misremembering. The actual code stores `p->nalt` and `p->natat` as struct and does:

```c
		case ')':
			if(p == paren)
				return NULL;
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			for(; p > paren && *--p != '('; ...)
```

I clearly don't remember it exactly. Doesn't matter — I shouldn't paste the solution anyway. The point for the task list: specify behavior + test vectors, and for vectors beyond the article's own example, verify by semantic equivalence (compile postfix → match tests) OR use exact vectors only where unambiguous.

Let me verify "a(bb)+a" → "abb.+.a." with the algorithm:
- 'a': emit 'a', natom=1
- '(': natom==1 not >1, no dot; save (nalt=0,natom=1); nalt=0,natom=0
- 'b': emit 'b', natom=1
- 'b': natom==1, no dot, emit 'b', natom=2
- ')': while(--natom>0): natom=2 → emit '.', natom=1; restore nalt=0, natom=1; then natom++ → 2? or natom = saved.natom + ... 

For the final output "abb.+.a.": after ')', we have "abb." emitted and the group is one atom (natom=1... but wait the '.' after bb was emitted inside the group). Then '+': emit '+', natom stays. Then 'a': natom>1? If natom==2 (group=1 atom... hmm).

Expected output "abb.+.a.": dots after "bb" (inside group), after '+', and after final 'a'. So: "a" "b" "b" "." "+" "." "a" ".". 

Trace: after ')': emitted "abb." — wait the '.' comes before '+' in output: "abb.+" — the group's internal dot "bb." then '+' → "abb.+", then 'a' with natom>1 → dot then a: "abb.+.a", end: flush remaining natom dots: "abb.+.a.". ✓ consistent with natom=2 after ')'.

OK so the algorithm works; exact vectors depend on associativity choices. Decision for the task list: 
- Use exact-string vectors for the article's own example and simple unambiguous cases (ab|c → ab.c|, a(bb)+a → abb.+.a.).
- For others, verify semantically: re2post output must compile via post2nfa and match the expected (text, expected) pairs. This is the robust approach and I'll note it.

Actually for "ab|c": trace: 'a' emit, natom=1; 'b': natom==1 no dot, emit 'b', natom=2; '|': while(--natom>0) emit '.': natom=2→emit '.', natom=1; nalt=1; 'c': natom==1... wait after '|', natom=0? The '|' case: `while(--natom > 0) *dst++ = '.'; nalt++;` — after loop natom=1? --natom from 2: emits '.', natom becomes 1, loop ends (1>0 false). Hmm then natom=1, nalt=1. Then 'c': natom>1? no, emit 'c', natom=2. End: while(--natom>0) emit '.': emit '.', done. Output: "ab.c|" ✓ matches my vector.

And "a(b|c)*d": 'a' emit natom=1; '(': save(0,1), reset; 'b' emit natom=1; '|': natom==1, while(--natom>0) doesn't run (natom=0 after --? --natom from 1 → 0, 0>0 false, no dot), nalt=1, natom=0? Hmm after the while loop natom=0. Then 'c': emit 'c', natom=1; ')': while(--natom>0): from 1→0, no dot; pop: restore nalt=0,natom=1; emit '|' (nalt=1 → the ')' case pops saved nalt and emits '|'); natom = saved.natom + 1? For output "abc|*.d.": after ')' we need "abc|" and group=1 atom, then '*' → "abc|*", then 'd': natom>1 (a=1 atom + group=1 atom → natom=2) → emit '.', 'd' → "abc|*.d", end flush: '.' → "abc|*.d." ✓.

Good, my vectors for a(bb)+a, ab|c, a(b|c)*d are consistent with the standard algorithm. For a?a?a?aaa the standard algorithm gives "a?a?.a?.a.a.a" (left-assoc grouping), while naive hand-derivation gives "a?.a?.a?.a.a.a". Both semantically identical. To avoid over-constraining, I'll use the semantic-verification approach for that one, or just drop it from exact vectors and cover a?ⁿaⁿ in the match tests (where re2post output is verified by matching behavior). I'll include it as a semantic test.

Similarly "(a|b)*abb": trace: '(': natom=0, no dot; save(0,0); reset. 'a': emit, natom=1. '|': natom==1 → no dot, nalt=1, natom=0. 'b': emit, natom=1. ')': while(--natom>0): 1→0 no dot; pop saved nalt=0... wait nalt=1 was set inside group. The ')' case: pops until '(' — the saved struct has nalt=1 (set by '|' inside), natom=0 (saved at '('). Emits '|' for nalt=1. Then natom++ → 1? Output so far "ab|". Then '*': emit → "ab|*", natom stays 1. 'a': natom>1? natom=1... hmm but we need a dot between (a|b)* and a! 

After ')', natom must be 2 for the outer context: saved.natom(0) + 1 (the group) + ... hmm. The ')' case in real code: after popping, `natom += p->nalt`? No... Let me think: the real code after the pop loop does:

```c
			natom++;
```

Hmm if natom was 1 (from 'b' inside... no wait, inside ')' handling: while(--natom>0) reduced inner natom to 1). Then after pop, natom++ → 2? That gives natom=2 in outer context: group(1) + previous 'a' before '(' (saved natom=1) = 2. ✓ Then 'a': natom>1 → emit '.', emit 'a', natom=2. 'b': natom>1 → emit '.', emit 'b', natom=2. 'b': emit '.', emit 'b', natom=2. End: while(--natom>0): emit '.'. Output: "ab|" + "*" + ".a" + ".b" + ".b" + "." = "ab|*.a.b.b." 

Hmm! That has a TRAILING dot: "ab|*.a.b.b." — but my earlier vector was "ab|*.a.b.b" without trailing dot. Which is right? The end-of-string flush: the real code after the loop:

```c
	while(p > paren){
		*dst++ = ')';
		...
	}
	for(...){ while(--natom > 0) *dst++ = '.'; ... }
```

Actually the real ending:
```c
	for(; p > paren; p--){
		*dst++ = '|';
		...
	}
```

I recall the ending emits the remaining '|'s and then:
```c
	while(--natom > 0)
		*dst++ = '.';
```

Hmm wait, but for "a(bb)+a" the expected output "abb.+.a." — trace the end: after final 'a', natom=2 (group+ +1... let me recount: after ')': natom=2? For a(bb)+a: saved at '(' was natom=1 (the leading 'a'). After ')': inner natom reduced to 1, then natom++ → 2? Then '+': emit, natom=2. 'a': natom>1 → emit '.', emit 'a', natom=2. End flush: while(--natom>0): emit '.'. Output: "abb" + "." (from inner) + "+" + ".a" + "." = "abb.+.a." ✓ — yes trailing dot present! "abb.+.a." ends with '.'. ✓ matches article.

So "(a|b)*abb" → "ab|*.a.b.b." WITH trailing dot. My earlier vector "ab|*.a.b.b" was missing the trailing dot. Let me recount: after ')': natom=2 (saved 0 + group 1... hmm wait saved natom at '(' was 0 since nothing before '('; after ')': inner reduced to 1, natom++ → 2? That would mean 2 atoms in outer context but there's nothing before the group... 

Hmm, this is where I need to be careful. Let me re-examine: the ')' case:

```c
		case ')':
			if(p == paren)
				return NULL;
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			for(;;){
				int c = *--p;
				if(c == '(')
					break;
				*dst++ = c;
			}
			natom++;
			break;
```

Wait, this pops chars from the paren stack and emits them — but the stack stores nalt/natom ints... I think the actual implementation stores the nalt count as... you know what, I remember now: the paren stack in the real code stores nalt and natom, and the ')' case does:

```c
			while(--natom > 0)
				*dst++ = '.';
			for(; p > paren; p -= 2){
				*dst++ = '|';  // no...
```

I genuinely don't remember the exact code. Let me just reason from first principles about what the correct postfix is, since that's what matters for the task list:

"(a|b)*abb" correct postfix: the regex is ((a|b)*)·a·b·b. Postfix: "ab|" "*" → "ab|*", then concat with a: "ab|*.a", concat b: "ab|*.a.b", concat b: "ab|*.a.b.b". That's 3 dots after the group. Total output: "ab|*.a.b.b" — NO trailing dot, because there are exactly 4 operands ((a|b)*, a, b, b) joined by 3 dots.

But the algorithm trace suggested a trailing dot. Which is correct? For "a(bb)+a" = a·(bb)+·a: 3 operands joined by 2 dots: "a" "bb." "+" "a" → "abb.+.a." — the article's own expected output. Count dots: "bb." (inner), ".a" wait: "abb.+.a." = a b b . + . a . — that's THREE dots for... operands: a, (bb)+, a → 2 concat dots needed. But output has 3 dots?! "abb.+.a." — dots: after bb, after +, after final a. Hmm, 3 dots.

Wait: "abb.+.a." parses as: a, b, b → "bb." concats b·b. Then "+": (bb)+. Then ".": concat a·(bb)+. Then "a": literal a. Then ".": concat (a·(bb)+)·a. So dots: 1 inside group (b·b), 1 between a and (bb)+, 1 between (a(bb)+) and a. Total 3 dots, 4 operands (a, b, b, a) — wait operands at top level: a, (bb)+, a = 3 top-level operands → 2 top-level dots; plus 1 dot inside the group = 3 total. ✓ Consistent.

Now "(a|b)*abb": operands: a, b (inside group, joined by | not .), then *, then a, b, b. Top-level: (a|b)*, a, b, b → 3 dots. Inside group: 0 dots (alternation). Total 3 dots: "ab|*" + ".a" + ".b" + ".b" = "ab|*.a.b.b" — no trailing dot. 

But the algorithm's end-flush `while(--natom > 0) *dst++ = '.'` — for "a(bb)+a" the trailing dot came from end-flush with natom=2 (a·(bb)+ already dotted when 'a' was seen, then final flush dots the last two). Let me re-trace "a(bb)+a" end: after final 'a': emitted "abb.+.a", natom=2 (the a and (bb)+... no wait. Hmm: after ')': natom = saved(1) + 1 = 2? Then '+': emit, natom=2. 'a': natom>1 → emit '.', natom-- →1, emit 'a', natom++ → 2. End: while(--natom>0): emit '.'. → "abb.+.a." ✓ 3 dots total: inner 1, before-a 1, end-flush 1. ✓

"(a|b)*abb" end: after ')': natom = saved(0) + 1 = 1. '*': emit, natom=1. 'a': natom==1, NO dot?! emit 'a', natom=2. 'b': emit '.', emit 'b', natom=2. 'b': emit '.', emit 'b', natom=2. End: emit '.'. Output: "ab|*" + "a" + ".b" + ".b" + "." = "ab|*a.b.b." — WRONG! Missing dot between * and a, spurious trailing dot.

So either my recollection of the algorithm is wrong, or... hmm. Wait — maybe after ')', natom should be saved.natom + 1 where the ++ accounts for the group as one atom, but ALSO the group's nalt... For "(a|b)*abb": saved at '(': nalt=0, natom=0. Inside: 'a' → natom=1; '|' → nalt=1, natom=0 (after while(--natom>0) from 1 → 0); 'b' → natom=1; ')': while(--natom>0): 1→0, no dot; pop: restore nalt=1, natom=0; emit '|' (for nalt=1); natom = restored.natom + 1 = 0+1 = 1? Hmm but the group is ONE atom, and there were 0 atoms before it → natom=1. Then '*': emit, natom=1. 'a': natom==1 → no dot → WRONG as shown.

Unless... the '|' case sets natom=0 but the ')' case does `natom += p->nalt`... no. Hmm, wait — maybe I have the '|' case wrong. Real '|' case:

```c
		case '|':
			if(natom == 0)
				return NULL;
			while(--natom > 0)
				*dst++ = '.';
			nalt++;
			break;
```

After '|': natom=1? --natom from 1 → 0, loop doesn't emit, natom=0. nalt=1. Then 'b': natom==0... default case: if(natom > 1) — no; emit 'b'; natom++ → 1. ')': while(--natom>0): 1→0 no emit; pop saved (nalt=0, natom=0); emit nalt '|'s? The pop loop emits... 

OK here's the thing — I recall the actual paren stack stores nalt and natom, and ')' does:

```c
			for(; p > paren; p -= 2){
				*dst++ = '|';   // ??? no
```

Honestly, the exact code doesn't matter for the task list. What matters: the CORRECT postfix for "(a|b)*abb" is "ab|*.a.b.b" (3 dots, no trailing). Any correct re2post must produce semantically valid postfix; exact string may vary only in associativity of consecutive concats, but dot COUNT between distinct top-level atoms is fixed. The trailing-dot question: "a(bb)+a" → "abb.+.a." has its final dot as a genuine concat (a·((bb)+)·a needs 2 top-level dots: one before 'a' after +, one at end). ✓. For "(a|b)*abb": 3 top-level dots all between atoms: *.a, a.b, b.b → "ab|*.a.b.b", no trailing. ✓.

So the correct vectors:
- "a(bb)+a" → "abb.+.a." (article's own)
- "ab|c" → "ab.c|"
- "a(b|c)*d" → "abc|*.d."
- "(a|b)*abb" → "ab|*.a.b.b"
- "a?a?a?aaa" → "a?.a?.a?.a.a.a" OR "a?a?.a?.a.a.a" (associativity-dependent — use semantic check)
- "a**" → "a**"
- "ab" → "ab."

Hmm wait, "ab|c" → "ab.c|": operands a·b, c joined by |: postfix "ab." then "|" then "c" → "ab.c|" ✓ no trailing.

And my earlier claim "(a|b)*abb → ab|*.a.b.b" ✓ (I had it right the first time; the algorithm-trace confusion was due to misremembered code details — the real code must handle it correctly since the article's example works).

Actually hold on, let me recheck "a(b|c)*d" → "abc|*.d.": operands: a, (b|c)*, d → 2 dots: "a" "bc|" "*" ".d" end-flush "." → "abc|*.d." ✓ 2 dots: between a and group (emitted when 'd' seen? no wait). Trace: "abc|*" then 'd': natom=2 (a + group) → emit '.', emit 'd' → "abc|*.d", end: natom=2 → emit '.' → "abc|*.d." ✓.

Good. Now for the task list I'll provide exact vectors for the unambiguous ones and note that a?a?a?aaa may legitimately produce either grouping — verify semantically (compile + match) instead of string-compare. Actually simpler: I'll give exact expected outputs for all five but add a note: "若你的实现产生语义等价但结合顺序不同的后缀（如 a?a?a?aaa 的两种分组），以语义验证为准". Hmm, for a?a?a?aaa: "a?.a?.a?.a.a.a" vs "a?a?.a?.a.a.a" — both valid. I'll mark that one as semantic-check-only.

Wait, actually, is "a?a?.a?.a.a.a" really what the standard algorithm produces? From my trace above with the real algorithm: 'a' emit natom=1; '?' emit natom=1; 'a': natom==1 no dot, emit, natom=2; '?' emit natom=2; 'a': natom>1 → dot, natom=1, emit, natom=2; '?' emit; 'a': dot, emit, natom=2; 'a': dot, emit; 'a': dot, emit; end: dot. → "a?" "a?" ".a?" ".a" ".a" ".a" "." = "a?a?.a?.a.a.a." — with trailing dot! 5 dots: between a?·a?, a?·a?, a·a, a·a, and end-flush. Operands: a?,a?,a?,a,a,a = 6 operands → 5 dots ✓. "a?a?.a?.a.a.a." — count dots: after 2nd a?, after 3rd a?, between a·a, between a·a, trailing = 5 ✓. And "a?.a?.a?.a.a.a" also 5 dots ✓. Both valid, different grouping. Confirmed: use semantic check for this one.

Hmm wait, "a?a?.a?.a.a.a." has a trailing dot — is trailing dot valid postfix? "a?a?.a?.a.a.a." evaluates: a? a? . → (a?a?); a? . → ((a?a?)a?); a . a . a . → ... final '.' concats last two. Yes valid.

OK. Now let me also reconsider: should the task list even include exact re2post vectors beyond the article's? Yes — tests make it Claude-Code-executable. I'll include: ab → ab., a(bb)+a → abb.+.a., ab|c → ab.c|, a(b|c)*d → abc|*.d., (a|b)*abb → ab|*.a.b.b, a** → a**, plus error cases, plus semantic note for a?a?a?aaa.

Hmm, one concern: is "(a|b)*abb → ab|*.a.b.b" truly what a correct implementation produces, or could a correct impl produce "ab|*a.b.b." (my broken trace)? The broken trace came from misremembered code. A CORRECT re2post must emit the dot between (a|b)* and a — any implementation that doesn't is buggy (postfix "ab|*a.b.b." would parse as (a|b)* · a · b · b? Let me check: "ab|*a.b.b.": a, b, | → ab|; * → ab|*; a → push a (no dot!); '.' → pops ab|* and a → concat ✓; b; '.' → concat; b; '.' → concat. Wait — "ab|*a.b.b." = a b | * a . b . b . — the '.' after 'a' pops TWO fragments: (a|b)* and a → concat. So it IS correct! The dot placement differs: "ab|*.a.b.b" emits dot before 'a' (when 'a' is read), "ab|*a.b.b." emits dot after 'a' (at end-flush... no wait).

Hmm: "ab|*a.b.b." — sequence: a, b, |, *, a, ., b, ., b, . — that's 3 dots: after first a (post-*)... positions: between * and a? No: "ab|*a.b.b." = a·b·|·*·a·.·b·.·b·. The first '.' comes after 'a' (the one following *). Evaluating: stack [a], [b] → '|' → [ab|] → '*' → [ab|*] → 'a' → [ab|*, a] → '.' → pop two, concat → [ab|*·a] → 'b' → [.., b] → '.' → concat → 'b' → '.' → concat. Final: (a|b)*·a·b·b ✓ CORRECT.

And "ab|*.a.b.b" = a,b,|,*,.,a,.,b,.,b: [a],[b]→|→[ab|]→*→[ab|*]→'.'→pop ONE? NO — '.' pops TWO: but stack has only ONE fragment [ab|*]! '.' would underflow! 

WAIT. That's wrong! In postfix with explicit '.', '.' is BINARY — pops two fragments. "ab|*.a.b.b": after "ab|*" stack=[ab|*]; next char '.' → pop pop → UNDERFLOW. So "ab|*.a.b.b" is INVALID postfix!!

Hmm!! But earlier I derived "(a|b)*abb → ab|*.a.b.b" by hand... Let me redo carefully. (a|b)*abb = ((a|b)*)·a·b·b. Postfix notation: operands in order: (a|b)*, a, b, b with binary concat between consecutive: 
- (a|b)* → "ab|*"
- concat with a: need "ab|*" "a" "." → "ab|*a."
- concat with b: "ab|*a." "b" "." → "ab|*a.b."
- concat with b: "ab|*a.b." "b" "." → "ab|*a.b.b."

So correct postfix = "ab|*a.b.b." — WITH the dot AFTER each operand pair, i.e. "ab|*a.b.b." (trailing dot). My "ab|*.a.b.b" was WRONG (dot before operand = invalid, underflow).

Let me recheck "a(b|c)*d" → I claimed "abc|*.d.": a, bc|, *, ., d, . — after "abc|*" stack=[a·(bc|*)]? NO: trace "abc|*.d.": 'a'→[a]; 'b'→[a,b]; 'c'→[a,b,c]; '|'→pop b,c → [a, bc|]; '*'→ [a, bc|*]; '.'→ pop bc|*, a → [a·(bc|*)]; 'd'→ [a·(bc|*), d]; '.'→ [a·(bc|*)·d] ✓ VALID. So "abc|*.d." is correct — dot after the * group, before d... the '.' here comes after '*' and pops a + (bc|*). ✓.

And "(a|b)*abb": by same pattern: "ab|*" then '.' pops... wait in "abc|*.d." the '.' after '*' pops a and (bc|*) — the 'a' was still on the stack from the beginning. For "(a|b)*abb": 'a'→[a]; '('... group: 'a','b','|' → [a, ab|]; ')' — wait postfix has no parens: tokens a, (, a, |, b, ), *, a, b, b. Postfix emission: a [from group] b | → "ab|", * → "ab|*", then outer: the leading 'a' is still pending on the OUTPUT string: full output = "a" + "ab|*" + then concat a·(ab|*) needs '.' → "aab|*." hmm wait no!

Ugh, I conflated. "(a|b)*abb" — the regex is (a|b)* followed by abb. There's NO leading 'a' outside the group. Tokens: ( a | b ) * a b b. Postfix: group emits "ab|", then '*' → "ab|*", then 'a' → "ab|*a", 'b' → "ab|*ab", 'b' → "ab|*abb", then dots: concat (a|b)*·a: after both are in output... in postfix, dots must be placed to form: ((ab|*)·a)·b)·b: "ab|*" "a" "." "b" "." "b" "." → "ab|*a.b.b." ✓ (as I corrected). 

And "a(bb)+a": tokens a ( b b ) + a. Postfix: "a" + "bb" + "." (inner concat) + "+" → "abb.+", then 'a' → "abb.+a", then outer dots: a·((bb)+)·a: "a" "bb.+" "." "a" "." → "abb.+.a." ✓ — the article's example, dot between + and a comes when? Output "abb.+.a.": a,b,b,.,+,.,a,. — the second '.' is between '+' and 'a' in the string but semantically it's the concat operator applied after reading 'a'. ✓ consistent.

So corrected vectors:
- "a(bb)+a" → "abb.+.a." ✓ (article)
- "ab|c" → "ab.c|" ✓ (trace: a,b,.,c,| → [ab], [c] → | ✓)
- "a(b|c)*d" → "abc|*.d." ✓
- "(a|b)*abb" → "ab|*a.b.b." (corrected! trailing dot)
- "ab" → "ab."
- "a**" → "a**"
- "a?a?a?aaa" → standard-algorithm output "a?a?.a?.a.a.a." hmm let me recheck with correct understanding: tokens a ? a ? a ? a a a. Emission with dots-as-you-go (dot emitted BEFORE the next operand when natom>1): 
  - 'a': out="a", natom=1
  - '?': out="a?", natom=1
  - 'a': natom==1 → no dot; out="a?a", natom=2
  - '?': out="a?a?", natom=2
  - 'a': natom>1 → out="a?a?.", natom=1, out+="a" → "a?a?.a", natom=2
  - '?': out="a?a?.a?", natom=2
  - 'a': dot → "a?a?.a?.", emit 'a' → "a?a?.a?.a", natom=2
  - 'a': dot → "a?a?.a?.a.", emit → "a?a?.a?.a.a", natom=2
  - 'a': dot → "a?a?.a?.a.a.", emit → "a?a?.a?.a.a.a", natom=2
  - end: while(--natom>0): emit '.' → "a?a?.a?.a.a.a."
  Result: "a?a?.a?.a.a.a." — 5 dots ✓ valid? Trace: a?→[a?]; a?→[a?,a?]; '.'→[a?a?]; a?→[..,a?]; '.'→[(a?a?)a?]; a→[..,a]; '.'→[..·a]; a→[..,a]; '.'→; a→[..,a]; '.'→ final concat ✓ VALID.
  
  Alternative grouping "a?.a?.a?.a.a.a" (dot-before style): a?→[a?]; '.'→UNDERFLOW! Invalid! So dot-before-each-operand style is INVALID postfix; the dot must come AFTER both operands. So "a?.a?.a?.a.a.a" is INVALID. Only "a?a?.a?.a.a.a." style (or equivalent valid orderings) work. 

Hmm wait, but that contradicts... "a?.a?.a?.a.a.a": first char 'a' → [a]; second char '.' → pops... only one element → underflow. YES invalid. Good catch. So the ONLY reasonable outputs are dot-after-pair style. Then associativity: "a?a?.a?.a.a.a." (left-assoc, standard) vs could a correct impl produce "a?.a?a?.a.a.a."? That would need dot after 2nd a? pairing 1st+2nd... "a?" "a?" "." — same thing. The variation is only in WHERE among the trailing a's dots go, but all correct impls emit dot when natom>1 at next-operand time + end flush → deterministic: "a?a?.a?.a.a.a.". Hmm, but an impl could also emit dot AFTER reading the operand (post-emit): 'a' emit, then if prev-natom>1 emit '.'... that gives "a?a.a?.a.a.a."? Let me not go down this hole. 

Decision: provide exact vectors for the 4 clean ones (a(bb)+a, ab|c, a(b|c)*d, ab, a**) and for a?a?a?aaa + (a|b)*abb use SEMANTIC verification (post2nfa + match tests) with a note that exact dot placement may vary by implementation but must be valid postfix (never underflow, single fragment left). Actually — for (a|b)*abb, "ab|*a.b.b." is what the standard algorithm produces; I'll give it as the expected vector but add the semantic-check note. Hmm, risk: if I state a wrong exact vector, the learner/Claude Code chases a ghost. The article's own vector "a(bb)+a → abb.+.a." is authoritative. For others, semantic verification is the robust choice. I'll do: exact vectors only for the article's example + trivially unambiguous ones where I've verified by hand-trace of valid postfix:

Verified valid-by-trace:
- "ab" → "ab." ✓
- "a**" → "a**" ✓ (a,*,* — each * unary pops 1)
- "ab|c" → "ab.c|" ✓
- "a(bb)+a" → "abb.+.a." ✓ (article)
- "a(b|c)*d" → "abc|*.d." ✓ (traced valid)
- "(a|b)*abb" → "ab|*a.b.b." ✓ (traced valid)
- "a?a?a?aaa" → "a?a?.a?.a.a.a." ✓ (traced valid) — I'll include it with a note.

Error cases: "a(", "a)", "(a", ")(", "*a", "a|", "|a", "" → NULL. Check "*a": '*' with natom==0 → NULL ✓. "a|": '|' ok (natom=1), end: nalt=1 pending, natom=1 → end flush... the real code at end: while(p>paren) emit ')' handling... for "a|": after loop, natom=1, nalt=1, stack empty. End code: `while(--natom > 0)` no emit; but nalt=1 unemitted → the end code: `if(nalt...)`? The real end:
```c
	while(p > paren){ ... }
	for(... nalt ...) 
```
Hmm, real code end:
```c
	for(; p > paren; p--){
		*dst++ = ')';
		...
	}
```
No. The actual ending of re2post:
```c
	while(p > paren){
		*dst++ = ')';
		...
	}
```
I really don't remember. Semantically "a|" is invalid (dangling alternation) → must return NULL. A correct impl detects it (natom==0 check somewhere or nalt pending with single operand). I'll list it as an error case requirement without prescribing mechanism. ✓

Also empty string "" → NULL (or error). ✓

Now match test vectors (full-string semantics), using INFIX patterns (tests compile via re2post→post2nfa):
- ("a(bb)+a", "abbbba") → 1 ✓ (a·(bb)+·a: abbbba = a bbbb a ✓)
- ("a(bb)+a", "abbba") → 0 (bb+ needs even b's ≥2: abbba has 3 b's → 0 ✓)
- ("a(bb)+a", "aba") → 0
- ("a?a?a?aaa", "aaa") → 1
- ("a?a?a?aaa", "aa") → 0 (full match: min length 3 ✓)
- ("(a|b)*abb", "aabb") → 1
- ("(a|b)*abb", "abb") → 1
- ("(a|b)*abb", "abab") → 0 (must end in abb: abab ends ab+b? "abab" ends "bab"... last three "bab" ≠ abb → 0 ✓)
- ("a*", "") → 1
- ("a+", "") → 0
- ("a|b|c", "c") → 1; ("a|b|c", "d") → 0
- ("(a*)*b", "aaab") → 1 (stress: nested stars, tests addstate dedup/listid)
- ("(a*)*", "") → 1 (empty-body star, classic edge: NFA for (a*)* — start split loops; must terminate! addstate with lastlist prevents infiniteI need to continue from where I left off. I was verifying test vectors for the match tests, specifically the edge case ("(a*)*", "") — empty-body star. Let me finish that verification briefly and then write the TASKS.md file.

The key concern: (a*)* NFA — start split state loops. addstate with lastlist prevents infinite recursion since it marks states as visited per list generation. So ("(a*)*", "") → 1 and it terminates. Good.

Now I have all the verified content. Time to write the TASKS.md file. Let me compose it now — in Chinese, with self-contained task prompts that Claude Code can execute, including:

- Usage instructions for Claude Code
- Reading map (tasks → article sections)
- Global conventions (project layout, Makefile targets, CLI semantics, full-match semantics)
- T0–T7 tasks with: goal, reference section, deliverables, acceptance criteria, paste-ready prompt
- Verified test vectors (from my analysis):
  - re2post: "a(bb)+a" → "abb.+.a." (article's own), "ab" → "ab.", "a**" → "a**", "ab|c" → "ab.c|", "a(b|c)*d" → "abc|*.d.", "(a|b)*abb" → "ab|*a.b.b.", "a?a?a?aaa" → "a?a?.a?.a.a.a." (with semantic-check note), error cases → NULL
  - match: the table I verified
  - state counts: a(bb)+a → 5 states + matchstate, (a|b)*abb → 7, a → 1, a** → 2
- Benchmark spec: a?ⁿaⁿ vs aⁿ, n=2..25, backtracking doubles per n, NFA ~quadratic
- DFA cache spec with cache-reuse instrumentation
- Extensions E1–E5
- Summary task with comprehension questions

Let me write the file now. Keep it tight but complete. I'll write it in one `write` call.

Structure:

```markdown
# 学习任务清单：用 C 实现 Thompson NFA 正则引擎

基于 Russ Cox《Regular Expression Matching Can Be Simple And Fast》(https://swtch.com/~rsc/regexp/regexp1.html)

## 使用方法（Claude Code）
...

## 阅读地图
| 任务 | 原文章节 |

## 全局约定
...

## 任务总览（依赖关系）
T0 → T1 → T2 → T3 → T4 → T5 → T6(选) → T7

---

### T0 ...
- [ ] 未完成
**提示词**：
```text
...
```
```

For nested code fences: the prompts are fenced with ```text inside the markdown. That's fine since the outer document isn't fenced.

Let me draft the content carefully but compactly. Each prompt block should be self-contained: context, files, spec, test vectors, acceptance commands.

T0 prompt: create skeleton — Makefile (all/test/bench/clean), src/regex.h with constants (Split=256, Match=257), src/main.c CLI stub (exit 2 "not implemented"), tests/test_main.c minimal assert framework. Acceptance: make && make test passes (tests skip unimplemented), ./regex a abc exits 2.

Actually simpler: T0 creates Makefile + directory layout + CLI that takes (regexp, text) args and a trivial test runner. Keep it minimal.

T1 prompt: re2post. Spec: infix → postfix, explicit '.' concat, precedence | < concat < *+?, parens, escaping NOT yet (T6). Return NULL on invalid input. Test vectors (exact): the 7 vectors + errors. Note on a?a?a?aaa: exact vector given but allow semantic equivalence if grouping differs — actually I traced "a?a?.a?.a.a.a." as the standard output; I'll give it as expected but add note: "若你的实现输出语义等价的后缀（结合顺序不同），以 T3 的 match 语义测试为准". Files: src/re2post.c, tests/test_re2post.c. Acceptance: make test green.

T2 prompt: post2nfa Thompson construction. State/Frag/Ptrlist/patch. Cases: literal, '.', '|', '?', '*', '+'. Key detail: '+' 的 fragment start 是 e.start（split 在环内），'*' 的 fragment start 是 split。Instrument state counter. Acceptance: state counts (a(bb)+a → 5, (a|b)*abb → 7, a → 1, a** → 2, each +1 matchstate), all dangling pointers patched (assert e.out empty / single fragment at end), invalid postfix (e.g. "a..", "..", "|") → NULL.

Wait — post2nfa input is postfix; invalid postfix like "a.." would underflow stack → return NULL. Good test.

T3 prompt: NFA simulation. List/addstate(listid)/startlist/step/ismatch/match. Full-string match semantics. Test table (the verified vectors). Acceptance: make test green including edge cases (a* vs "", a+ vs "", (a*)* vs "", nested stars terminate).

T4 prompt: backtracking reference + benchmark. backtrack.c: recursive on same NFA (Split → try out then out1; literal → advance; matchstate → *p=='\0'). Cross-check on test table. bench: a?ⁿaⁿ vs aⁿ, n=2..25, µs, CSV + BENCHMARK.md table. Acceptance: both engines agree on all cases; backtracking time ~doubles per +1 n; NFA stays sub-ms through n=25; document. Also note PCRE aborts at n=23 (article trivia).

T5 prompt: DFA cache. DState{List l; next[256]; left,right}, BST keyed by sorted list (ptrcmp/listcmp), dstate/nextstate/startdstate. Instrument dstate allocation count. Acceptance: same test table via DFA; second identical match allocates 0 new DStates; bench: text='a'×100000+'b' with regex a*b — DFA vs NFA sim timing recorded; note cache-eviction option (article: cache is disposable).

T6 prompt (optional, pick subsets): E1 escapes, E2 char classes + dot-any (reserve concat as internal constant), E3 {n,m} expansion (article's exact expansions), E4 unanchored leftmost search. Each with tests. Mark E5 (Pike VM submatch, article 2) as stretch.

T7 prompt: SUMMARY.md — answers to 6 comprehension questions + benchmark table + 复盘.

Also a final "里程碑" checklist.

Length: aim ~250 lines. Write it now.

One more check on the "(a|b)*abb" vector "ab|*a.b.b." — trace validity: a→[a]; b→[a,b]; |→[ab|]; *→[ab|*]; a→[ab|*,a]; .→[ab|*·a]; b→[..,b]; .→[..·b]; b→[..,b]; .→[final] ✓ valid, single fragment. ✓

And "a(b|c)*d" → "abc|*.d.": a→[a]; b→[a,b]; c→[a,b,c]; |→[a,bc|]; *→[a,bc|*]; .→[a·bc|*]; d→[..,d]; .→[final] ✓.

"a?a?.a?.a.a.a.": a→[a]; ?→[a?]; a→[a?,a]; ?→[a?,a?]; .→[a?a?]; a→[..,a]; ?→[..,a?]; .→[(a?a?)a?]; a; .; a; .; a; . → ✓ valid.

"ab.c|": a→[a]; b→[a,b]; .→[ab]; c→[ab,c]; |→[ab|c] ✓.

"abb.+.a.": a,b→[a,b]; b→[a,b,b]; .→[a,bb]; +→[a,bb+]; a→[a,bb+,a]; .→[a·bb+]; .→[final] ✓.

"ab.": a,b,. → [ab] ✓. "a**": a,*→[a*],*→[a*] ✓.

All vectors verified. State counts: a(bb)+a: chars/metachars excluding parens: a,b,b,+,a = 5 ✓. (a|b)*abb: a,b,|,*,a,b,b = 7 ✓. a** = a,*,* = 2... wait a** infix is a then * then *: 1 literal + 2 operators = 3 states! Let me recount: "a**" = a, *, * → 3 states (1 for 'a', 1 for first *, 1 for second *). Earlier I said 2 — wrong. Each char OR metachar creates exactly one state: a(1) *(2) *(3) = 3. Fix: a** → 3 states.

Match vectors final check:
- ("a(bb)+a","abbbba")→1: a + (bb)+ = bbbb + a ✓
- ("a(bb)+a","abbba")→0 ✓ (odd b count)
- ("a(bb)+a","aba")→0 ✓
- ("a?a?a?aaa","aaa")→1 ✓ (all ? take zero)
- ("a?a?a?aaa","aa")→0 ✓ (min 3)
- ("(a|b)*abb","aabb")→1 ✓
- ("(a|b)*abb","abb")→1 ✓
- ("(a|b)*abb","abab")→0 ✓
- ("a*","")→1 ✓
- ("a+","")→0 ✓
- ("a|b|c","c")→1 ✓
- ("a|b|c","d")→0 ✓
- ("(a*)*b","aaab")→1 ✓
- ("(a*)*","")→1 ✓ (terminates via lastlist dedup)
- ("a**","aaa")→1 ✓ (a** = (a*)*)

Good. Now write TASKS.md.The file is written. I spotted an error in the milestone section — the exit codes are swapped. Fixing:That edit was a no-op — let me verify the actual file content around the milestone section:Line 288 is already correct (`aabb` matches → 0, `abab` doesn't → 1, per the convention 匹配=0/不匹配=1). My edit was a no-op on identical text, so the file stands. Final consistency check of the whole file:TASKS.md 已完成并自验。交付内容：

**文件**：`TASKS.md`（291 行）——把 Russ Cox 文章的脉络转成 8 个可执行任务，每个任务带一段自包含的「提示词」代码块，直接粘贴给 Claude Code 即可执行，无需会话上下文。

**任务链**（依赖顺序）：
- **T0** 骨架与 CLI（Makefile、退出码约定 0/1/2）
- **T1** `re2post` 中缀→后缀（含 7 个精确测试向量 + 8 个非法输入）
- **T2** Thompson 构造 `post2nfa`（State/Frag/patch，六种编译分支，状态数断言）
- **T3** NFA 多状态模拟（listid 去重、15 条语义测试表，含 `(a*)*` 空串终止等边界）
- **T4** 回溯对照实现 + `a?ⁿaⁿ` 基准（n=2..25，复现 O(2ⁿ) vs O(mn)）
- **T5** DState 缓存构造 DFA（二叉树查找、缓存复用断言、长文本加速比）
- **T6** 选做扩展 E1–E5（转义、字符类、`{n,m}` 展开、非锚定、Pike VM）
- **T7** SUMMARY.md 六道思考题复盘

**关键设计**：
- 提示词只给规格和测试向量，不给答案代码——写完再对照原文复盘
- 所有测试向量经过手工验证（后缀表达式栈求值无下溢、状态数符合文章“每字符/元字符一状态”结论、`+` 与 `*` 片段起点差异决定空串语义）
- 每个任务有可执行的验收命令（`make test` / `make bench` / CLI 退出码），勾选前必须跑通
- 附阅读地图（任务↔原文章节）和里程碑总验收清单

使用方式：在目录里启动 `claude`，逐段粘贴提示词，或直接说「执行 TASKS.md 里的下一个未勾选任务」。