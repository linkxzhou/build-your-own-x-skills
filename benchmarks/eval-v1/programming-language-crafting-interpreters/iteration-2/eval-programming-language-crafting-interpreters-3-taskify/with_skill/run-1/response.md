The user wants me to convert the Crafting Interpreters tutorial (http://www.craftinginterpreters.com/) into an executable learning task list for Claude Code.

First, I should check the skill "build-your-own-x" since this matches its description — someone wants a hands-on project to learn systems skills (building an interpreter from scratch). Let me read that SKILL.md first.

Then I should fetch the table of contents of Crafting Interpreters to build an accurate task list.

Let me start by reading the skill file and fetching the website in parallel.The skill says I should read the track skill for the mapped category. The topic is "interpreter/compiler" — let me check the skills directory for the track skill. The category slug is likely "interpreter" or similar. Let me look at the skills directory.

Also I need the table of contents from contents.html to build the task list.The skills directory only has build-your-own-x — no track skills exist (the router references skills/<slug>/SKILL.md but they don't exist in this workspace). Let me check the manifest mentioned: skills/x-skills-manifest.json. Actually the ls showed only build-your-own-x folder. Let me check inside build-your-own-x folder for skills.

Also I got the TOC mostly. Part III got truncated at chapter 28. I know the book: chapters 28 Methods and Initializers, 29 Superclasses, 30 Optimization, plus Backmatter (Appendix I: Lox on the JVM? Actually backmatter: "Appendix A: Lox Expressions" ... let me recall). The backmatter contains: Appendix 1 "A Bytecode Virtual Machine"? No. Backmatter: "What's next?" Actually the backmatter includes:
- Appendix I: A Compressed History? Hmm.

Let me recall the actual TOC of Crafting Interpreters:

Part I: Welcome
1. Introduction
2. A Map of the Territory
3. The Lox Language

Part II: A Tree-Walk Interpreter
4. Scanning
5. Representing Code
6. Parsing Expressions
7. Evaluating Expressions
8. Statements and State
9. Control Flow
10. Functions
11. Resolving and Binding
12. Classes
13. Inheritance

Part III: A Bytecode Virtual Machine
14. Chunks of Bytecode
15. A Virtual Machine
16. Scanning on Demand
17. Compiling Expressions
18. Types of Values
19. Strings
20. Hash Tables
21. Global Variables
22. Local Variables
23. Jumping Back and Forth
24. Calls and Functions
25. Closures
26. Garbage Collection
27. Classes and Instances
28. Methods and Initializers
29. Superclasses
30. Optimization

Backmatter:
- Appendix I: A Graphical Bytecode Disassembler? No...

Actually the backmatter is:
- Appendix A1: "Lox on the JVM"? Hmm, no. Let me think. The backmatter contains:
  - "Design Note: ..." no those are inline.
  - Backmatter: "Appendix I: A Compressed Lexicon"? 

I remember the backmatter has:
- Appendix I: "A Bytecode Disassembler"? No, that's in chapter 14.

Actually, I believe the backmatter contains:
- Appendix I: "A Compressed History of Lox"? Not sure.

Let me just fetch the rest of contents.html to get the truncated part. The truncation cut off at chapter 28. Let me fetch with more chars or fetch the tail. I'll fetch again with larger maxChars.

Also check the skills folder inside build-your-own-x.Now I have the full TOC. The book has 30 chapters + backmatter. The backmatter includes "Appendix I: A Compressed Lexicon"? Let me recall — the backmatter of Crafting Interpreters contains:
- "Appendix I: A Graphical Grammar of Lox"? Hmm.

Actually I recall the backmatter contains:
- Appendix I: "A Compressed History"? No.

Let me think. The Crafting Interpreters backmatter:
- "Appendix I: A Bytecode Virtual Machine"? No, that's Part III.

I believe the backmatter is:
- Appendix I: "A Compressed Lexicon of Lox"? 

Hmm, actually I'm fairly confident the backmatter contains:
- "Appendix I: A Compressed Lexicon"? No...

Let me just check contents.html tail. The truncated part was after chapter 28: "29. Superclasses, 30. Optimization" then "❧Backmatter" with items. I recall the backmatter has:
- Appendix I: "A Compressed Lexicon"? 

OK let me just fetch contents.html again with a bigger maxChars to see the backmatter section. Actually the first fetch had maxChars 12000 and got truncated at 516 chars remaining. The remaining 516 chars would contain chapters 29, 30 and backmatter. I already know 29 and 30 from the part III page. The backmatter likely includes "Appendix I: A Compressed Lexicon"? I genuinely don't remember. Let me fetch the tail of contents.html.

Actually, I recall now: the backmatter of Crafting Interpreters contains:
- "Appendix I: A Compressed Lexicon"? No. 

I think it's:
- Appendix I: "A Graphical Grammar"? No.

Hmm, I remember there's an appendix about "Lox on the JVM"? No, that's from "Some Notes on Crafting Interpreters"? 

Let me just fetch it. I'll fetch contents.html with maxChars 20000 and look at the end.

Also, the skill directory has many sub-skills. There might be a relevant one for interpreters — let me grep for "craftinginterpreters" or "interpreter" or "lox" in the skills folder.The workspace has a per-tutorial skill for exactly this book: `programming-language-crafting-interpreters`. Per the router, I'll read the track skill first, then the tutorial-specific skill.该技能有一个专门的“将教程转换为任务列表”部分，该部分被截断了。让我阅读其余部分以及 tutorial-map 参考。Now let me read the concepts.md reference too, and the minimal example README for scaffold guidance. Then I'll build the TASKS.md.

The skill says:
1. Build the list from references/tutorial-map.md and references/concepts.md first.
2. Fetch original at most once or twice — I've fetched contents.html and the homepage + part III page (3 fetches, but they were TOC only, fine).
3. Deliver promptly: write the task list (e.g. TASKS.md in the project) with one entry per milestone — goal, files to touch, key concept, and a verification command with expected output.
4. End the reply with the first runnable checkpoint (exact command for milestone 1 and expected output).

Let me read concepts.md and examples/minimal/README.md.I have everything I need. Now let me check the workspace state — is it empty? Let me check what's in the workspace root to decide where to put TASKS.md.

The user's request: "基于 http://www.craftinginterpreters.com/，把这个教程转换成 Claude Code 可执行的学习任务清单。" — Convert the tutorial into a Claude Code executable learning task list.

Per the skill's "Converting the tutorial into a task list" section:
1. Build from tutorial-map.md and concepts.md ✓ (read)
2. Fetch original at most once or twice ✓ (fetched TOC)
3. Deliver promptly: write TASKS.md with one entry per milestone — goal, files to touch, key concept, verification command with expected output.
4. End reply with first runnable checkpoint (exact command for milestone 1 + expected output).

The book structure: 30 chapters in 3 parts. The task list should map chapters to milestones. The book itself uses Java (jlox) for Part II and C (clox) for Part III. The skill defaults to Java.

The book also has an official test suite: https://github.com/munificent/craftinginterpreters/tree/master/test — that's a great verification harness for Claude Code tasks. I can reference it.

Let me design the TASKS.md:

Structure:
- Header: what this is, source, how to use with Claude Code (each task = one Claude Code session/prompt; paste the prompt, let Claude Code implement, run the checkpoint).
- Conventions: repo layout (jlox/ and clox/), progress tracking in PROGRESS.md, the coaching rules (Claude Code scaffolds, learner writes core... actually for "Claude Code 可执行" the tasks should be phrased as prompts/instructions that Claude Code can execute).

Actually "Claude Code 可执行的学习任务清单" means a task list that Claude Code can execute — i.e., each task is written as an actionable instruction with files to touch and a verification command, so the user can feed each task to Claude Code one at a time. The skill says: "write the task list (e.g. TASKS.md in the project) with one entry per milestone — goal, files to touch, key concept, and a verification command with expected output."

So each task entry needs:
- Goal
- Files to touch
- Key concept
- Verification command + expected output

I'll map the 30 chapters into milestones. The book's chapters are already well-sized. I could do one task per chapter, but some chapters are reading-only (1-3 are conceptual). Let me structure:

Phase 0: Setup (repo, toolchain check)
Phase 1 (Part I, ch 1-3): reading + Lox spec — deliverable: README with Lox language summary + test harness decision. Checkpoint: none code, but a written spec. Actually ch3 "The Lox Language" gives the full language spec — task: write docs/lox-spec.md summarizing syntax, and set up the official test suite runner.

Phase 2 (Part II, jlox, ch 4-13): one task per chapter:
- T4 Scanning: Scanner + TokenType + Token. Verify: run scanner on sample, or test suite test/scan? The official test suite has test/scanning? Actually the official repo test dirs: assignments? Let me recall: test/ contains subdirs: benchmark, calls, class, closure, comments, constructor, empty_file? etc. There's no per-chapter mapping, but there is expected output files. For early chapters, simplest verification: a small .lox script + expected stdout, e.g. `java com.craftinginterpreters.lox.Lox test.lox` prints tokens? jlox doesn't print tokens by default. Chapter 4 has a main that prints tokens (Scanner has a main? Actually in ch4, the Scanner class is created and Lox.run uses it; there's a token-printing in the chapter? In ch4 the book writes Scanner and tests it manually; the runPrompt/runFile just scan but don't print. Hmm, actually in ch4 the book does print tokens? Let me recall: In chapter 4, `Lox.java` run() creates Scanner and scans tokens... and the book says "we don't do anything with them yet". There's no token printing. But many readers add a debug print. For verification, better: use the official test suite with a runner, or write small .lox files with expected output once the interpreter can run them.

Practical approach for verification commands:
- jlox: `java -cp jlox com.craftinginterpreters.lox.Lox script.lox` → expected output.
- clox: `./clox script.lox` → expected output.
- Official test suite: `py test.py --interpreter path` (the repo's test.py harness). That requires cloning the book repo for tests. I can include an optional task: clone test suite into test/ and write a small runner. The book's test.py is at github.com/munificent/craftinginterpreters/blob/master/test.py.

For Claude Code executability, each task should have a concrete checkpoint. I'll give per-chapter checkpoints using small .lox snippets with expected output (I can write these accurately from the Lox spec), plus the official test suite as the gold standard at phase ends.

Let me now write the Lox snippets carefully:

Ch4 Scanning checkpoint: token dump. I'll make the task include "add a temporary `--tokens` debug flag that prints scanned tokens" — that's a common exercise and the book's Scanner supports it trivially. Expected output for `var x = 1;`:
```
VAR VAR null
IDENTIFIER x null
EQUAL = null
NUMBER 1 1.0
SEMICOLON ; null
EOF  null
```
Token toString in the book: `String.format("%s %s %s", type, lexeme, literal)` — for NUMBER 1, literal is 1.0 (Java double toString). EOF: lexeme "" → "EOF  null" (two spaces since lexeme empty). This is precise per the book's code. Good.

Ch5 Representing Code: AST classes + Expr printer (RPN/AstPrinter). Checkpoint: `-AstPrinter` prints parenthesized expression: for `1 + 2 * 3` → `(+ 1 (* 2 3))`. The book's AstPrinter prints `(operator left right)`. Input: the book hardcodes an expression in main. Task: make a debug flag that parses? No — parsing is ch6. In ch5 the printer takes a hand-built AST. Checkpoint: unit-test-ish: build `new Expr.Binary(new Expr.Literal(1), "+", new Expr.Binary(new Expr.Literal(2), "*", new Expr.Literal(3)))` → prints `(+ 1 (* 2 3))`. Good.

Ch6 Parsing Expressions: recursive descent parser → Expr. Checkpoint: parse `1 + 2 * 3;` and print via AstPrinter → `(+ 1 (* 2 3))`; `-1 + 2` → `(+ (- 1) 2)`? Unary prints `(- 1)`. Also error case: `1 + ;` → ParseError with message "Expect expression." and exit code 65. The book uses exit code 65 for syntax errors (EX_USAGE? Actually EX_DATAERR=65). In ch6, token() error → ParseError; Lox.error reports; exit code 65 set in runFile? The book sets System.exit(65) in runFile when hadError. Yes: `if (hadError) System.exit(65);`. Good.

Ch7 Evaluating Expressions: Interpreter visitor. Checkpoint: `print 1 + 2 * 3;`? print statement is ch8. In ch7, the book evaluates the expression and... the REPL prints the result: in runPrompt, if parse produced single expression, evaluate and print. Yes! Ch7: "if the user types an expression, evaluate it and print the result" — the book adds that in the REPL: parse expression, interpret, print via AstPrinter? No — it prints the value: `System.out.println(interpreter.evaluate(expression));`? The book: in runPrompt after parsing, checks if single expression statement... Actually the book does this in chapter 7? Let me recall. In ch7 the book has the Interpreter class with visitLiteralExpr etc. And in Lox.run? Hmm, the book in ch7: "we need to hook it up to the main Lox class... if (expression != null) { System.out.println(new Interpreter().evaluate(expression)); }" — something like that in runPrompt only. Yes, ch7 adds expression-mode REPL printing. Checkpoint: REPL `1 + 2 * 3` → `7`; `"a" + "b"` → `ab`? Wait — Lox `+` on strings: ch7 implements binary + for numbers AND strings (concatenation). Yes: "if both strings, concatenate". So `"a" + "b"` → `ab`. And `"a" + 1` → RuntimeError "Operands must be two numbers or two strings." exit 70 (EX_SOFTWARE runtime error code 70). Good.

Ch8 Statements and State: statements, env, var, assignment. Checkpoint script:
```
var a = 1;
print a;      // 1
a = 2;
print a;      // 2
print b;      // Runtime error: Undefined variable 'b'. exit 70
```
Good.

Ch9 Control Flow: if/else, while, for, logical && || (short-circuit). Checkpoint:
```
var i = 0;
while (i < 3) { print i; i = i + 1; }   // 0 1 2
if (i == 3) print "done"; else print "no";  // done
print true and false;  // false
print false or true;   // true
for (var j = 0; j < 2; j = j + 1) print j;  // 0 1
```
Good.

Ch10 Functions: call, return, native clock(). Checkpoint:
```
fun add(a, b) { return a + b; }
print add(1, 2);  // 3
fun fib(n) { if (n < 2) return n; return fib(n-2) + fib(n-1); }
print fib(10);  // 55
print clock;  // <native fn>  (book prints "<native fn>")
```
The book's LoxFunction toString: `<fn add>`; native: `<native fn>`. Good.

Ch11 Resolving and Binding: resolver, max env distance, errors: "Cannot read local variable in its own initializer", "Can't read local variable in its own initializer"? The book: "Error at ...: Can't read local variable in its own initializer."? Let me recall exact message: In Resolver.visitVarExpr: "Can't read local variable in its own initializer."? Hmm. The book's message: `Lox.error(expr.name, "Can't read local variable in its own initializer.");`? I believe it's "Can't read local variable in its own initializer." Also "return" at top level: "Can't return from top-level code." And this at top level: "Can't use 'this' outside of a class." Checkpoint:
```
var a = "outer";
fun f() { print a; var a = "inner"; }
f();  // outer  (resolution: print a binds to global? wait)
```
Hmm — in the book, `print a;` before `var a` in same scope: the resolver marks it declared-not-defined → error "Can't read local variable in its own initializer." Actually that's for reading before declaration in same scope. The classic shadowing example:
```
var a = "global";
fun show() { print a; }
fun set() { a = "assigned"; }
show(); // global
set();
show(); // assigned
```
Hmm that's closure/state. The ch11 key behavior: 
```
var a = "outer";
{
  var a = "inner";
  print a;  // inner
}
print a;  // outer
```
That's ch8 env scoping though. Ch11's distinguishing test: early return binding and "each `a` refers to the right declaration":
```
var a = "one";
fun f() { var a = "two"; fun g() { print a; } g(); }
f();  // two (closure captures resolved env, not dynamic)
```
And the error case:
```
fun f() { var a = a; }  // error: Can't read local variable in its own initializer.
```
Hmm wait, actually the book's exact message — I need to be careful. From the book ch11: 

```java
private void declare(Token name) {
  ...
}
```
and in visitVarStmt... The error in resolveLocal:
```java
if (entry == Boolean.FALSE) {
  Lox.error(expr.name, "Can't read local variable in its own initializer.");
}
```
Hmm, I actually recall it as "Can't read local variable in its own initializer." Let me double check from memory of the test suite: test/variable/uninitialized_early.lox expects "Can't read local variable in its own initializer."? The test suite expected output: "Can't read local variable in its own initializer." I'm fairly confident. Also `return_at_top_level.lox` expects "Can't return from top-level code." And `this` at top: "Can't use 'this' outside of a class."

Since I'm not 100% sure of exact strings, I should phrase expected outputs with the key substring and note "message per book". To be safe, I'll write expected outputs that I'm confident about, and for error messages use the book's wording with a note that exact text follows the book/test suite. Actually the requirement fidelity section says verify named fields... but this is a task list for future execution; the checkpoints will be run then. I'll keep exact strings where confident (they're from the book's code which I know well) and mark the few uncertain ones.

Let me be careful about the ones I state:

- Ch4 token dump format: `type lexeme literal` — confident (Token.toString in ch4: `String.format("%s %s %s", type, lexeme, literal)`).
- NUMBER literal for `1` is `1.0` — confident (Double.toString).
- EOF prints `EOF  null` (empty lexeme → double space) — confident.
- Ch5 AstPrinter: `(+ 1 (* 2 3))` — confident.
- Ch6: `print` not yet; parse error exit 65 — confident. Message "Expect expression."? In primary(): `throw error(peek(), "Expect expression.");` — confident.
- Ch7 REPL: `1 + 2 * 3` → `7`; runtime error exit 70 — confident. Message "Operands must be two numbers or two strings." — confident.
- Ch8: `Undefined variable 'b'.` — confident (RuntimeError: "Undefined variable 'name'."). Exit 70.
- Ch9: outputs as above — confident.
- Ch10: `add(1,2)` → 3; fib(10) → 55; `print clock;` → `<native fn>` — confident. Arity error: "Expected 2 arguments but got 1." — confident.
- Ch11: messages above — mostly confident; I'll use them.
- Ch12 Classes: 
```
class Breakfast { cook() { print "eggs"; } }
Breakfast().cook();  // eggs
```
Wait — method call syntax: `Breakfast().cook();` — Lox allows calling constructor then method. In ch12, `print "Breakfast instance";`... The book example: `class Breakfast { cook() {...} serve(who) {...} }` then `Breakfast().serve("Maude");`? Hmm, actually in ch12 the book does:
```
class Breakfast {
  cook() { print "Eggs a-fry!"; }
  serve(who) { print "Enjoy your breakfast, " + who + "."; }
}
Breakfast().cook();
Breakfast().serve("Maude");
```
Something like that. Fields: `obj.field = value; print obj.field;`. Instance print: `<Breakfast instance>`. Confident: LoxInstance toString: `klass.name + " instance"` → `<Breakfast instance>`.
- Ch13 Inheritance: `class Cruller < Toast {};` super methods:
```
class A { method() { print "A.method"; } }
class B < A { method() { print "B.method"; } test() { super.method(); } }
B().method();  // B.method
B().test();    // A.method
```
Also "Superclass must be a class." error, and "Cannot inherit from itself"? Hmm: "Error at 'superclass': A class can't inherit from itself."? There is a check in resolver for self-inheritance: "A class can't inherit from itself."? I recall test/class/inherit_self.lox expects "A class can't inherit from itself."? Not fully sure; skip or mark.

Part III clox chapters 14-30, one task each:
- T14 Chunks of Bytecode: chunk struct, OpCode enum, addConstant, disassembler. Checkpoint: `make clox && ./clox` no-arg? In ch14 main writes a chunk with OP_RETURN and disassembles to stdout:
```
== test chunk ==
0000 0000 OP_RETURN
```
The book's disassembleChunk prints "== test chunk ==" then offset, line, name. Format: `%04d %04d %s`. For OP_RETURN: `0000 0000 OP_RETURN` then newline. Confident-ish: printf("%04d ", offset); printf("%4d ", line); printf("%s\n", name). So `0000 0000 OP_RETURN`. Good.
- T15 A Virtual Machine: stack, run loop. Checkpoint: constant + arithmetic: the book's main in ch15 pushes constant 1.2, negate, return; debug trace shows stack. I'll define: extend to compile? No — ch15 still hand-written chunk. Checkpoint: disassembly trace with stack effect. Keep simple: run the hand-built chunk, trace prints `== test chunk ==`, `0000 0000 OP_CONSTANT         0 '1.2'`, stack `          [ ]`... The trace format: `%04d %04d %-16s %4d '`... For OP_CONSTANT: `0000 0000 OP_CONSTANT         0 '1.2'`. Stack trace lines: `          [ 1.2 ]`. This is getting too detailed; I'll simplify the expected output to key lines.
- T16 Scanning on Demand: scanner.c. Checkpoint: compile+run a .lox that prints? Not yet — printing is ch21? No wait: print statement in clox comes in ch21? Hmm: ch21 Global Variables adds variable access; print statement is added in ch21? Let me recall: ch17 compiles expressions; ch18 values; ch19 strings; ch20 hash tables; ch21 global variables — and print statement appears in ch21? Actually I think `print` is added in ch21 ("Global Variables") — no wait. Let me think: ch17 compiles arithmetic expressions and the VM executes them, but there's no output yet. The book says in ch17: "we can't print yet". print comes in ch21? Hmm, I believe print statement is implemented in ch21 "Global Variables"? No... Let me think again. 

Chapter 21 "Global Variables": adds OP_DEFINE_GLOBAL, OP_GET_GLOBAL, OP_SET_GLOBAL. And the book says "we'll add print statement"? I recall print being added in ch21: "It's time to add print statements"? Hmm. Actually I'm fairly sure print is added in chapter 21? Let me think about what's in ch21: global variables need a way to observe results → the book adds `print` statement there. Yes — in ch21, the book says something like "we need a way to see results: print statement". Hmm, but I also recall print in ch21 being described as "the print statement we've been missing". I'm fairly confident print lands in ch21.

Wait, actually — I now recall ch21 starts with "variable declarations... print". Let me check: In ch21 the book writes: "We can finally print! ... print statement". I'll go with ch21 for print. Hmm, but there's risk. Alternative: I could verify by fetching chapter 21. The skill says fetch at most once or twice (README/TOC only) — I've done 3 fetches already. I'll rely on memory but phrase checkpoints to be robust: for ch17-20, checkpoints use the debug trace/disassembler rather than program output; from ch21 on, use .lox scripts with print.

Actually, let me reconsider: I'm quite sure that in ch17 (Compiling Expressions), the book notes "our VM can't print yet" and tests via the disassembler/trace. And print statement: chapter 21 "Global Variables" — the book: "print statements... we've needed a way to observe". Hmm, I genuinely believe print is ch21. Let me also recall ch23 Jumping Back and Forth adds while/for; ch24 calls; ch25 closures; ch26 GC; ch27 classes; ch28 methods+init; ch29 super; ch30 optimization (NaN boxing / constant folding? ch30 covers "constant folding" and "jump threading"? The book's ch30: optimizations — constant folding, and... it covers "Constant Folding" and "Jump Threading"? I recall ch30 has sections: "Constant Folding", "Jump Threading"? Hmm, actually ch30 sections: "Measuring", "Optimizing Compilers"? The main optimization implemented: constant folding in the compiler, and "jump threading"? I recall the chapter implements constant folding and discusses others. Also "NaN boxing" is in ch28? No — NaN boxing is in ch30? Hmm. Value representation: ch18 uses tagged union; ch28? No. NaN boxing is section in ch30? I believe ch30 "Optimization" includes: constant folding, jump threading? and "NaN boxing" is actually in chapter 28? No...

Let me recall the actual ch30 contents: "30. Optimization" — sections: "Measuring" (benchmarking), "Faster Hash Table Probing"? Hmm no. I remember: ch30 covers constant folding, and "jump threading", and "NaN boxing"? I think NaN boxing is indeed in ch30 under "Value Representation"? Hmm, no — I'm now fairly sure NaN boxing is in ch30? Let me think about the book's index: "NaN boxing" appears in chapter 30? ... I recall reading ch30: it has "Constant Folding", "Jump Threading", "Desugaring"? 

OK — risk management: for ch30 I'll phrase the task as "constant folding + benchmark with the book's test suite benchmarks" without asserting the exact list of techniques. Actually I do remember now: Chapter 30 sections are: "Measuring", "Faster Hash Tables"? no... The chapter implements: constant folding (in compiler), and "jump threading"? and "NaN boxing"? I'm going to check quickly — one more fetch of chapter 30's TOC-level info is justified? The skill says fetch at most once or twice for README/TOC. I've fetched 3 pages. I'll avoid more fetches and phrase ch30 generically: "constant folding and other optimizations from the chapter; benchmark before/after with test/benchmark/*.lox". That's safe.

Similarly ch26 GC: mark-sweep, addObject? Checkpoint: stress GC with DEBUG_STRESS_GC, run a script allocating strings; also `--gc`? The book uses `#define DEBUG_STRESS_GC` and `DEBUG_LOG_GC`. Checkpoint: run fib or string alloc with stress GC and see "GC" logs, no crash. Fine.

Ch20 Hash Tables: tombstones, resize. Checkpoint: unit-ish test via a small C test or run script after ch21? Hash table alone has no observable output; checkpoint: temporary test main that inserts/finds/deletes keys and prints results. Fine — I'll phrase "add a temporary test main".

Ch22 Local Variables: slots, OP_GET_LOCAL/SET_LOCAL. Checkpoint:
```
var a = "global";
{ var a = "outer"; { var a = "inner"; print a; } print a; } print a;
// inner outer global
```
Good.

Ch23: while/for loops:
```
var i = 0; while (i < 3) { print i; i = i + 1; }  // 0 1 2
for (var i = 0; i < 3; i = i + 1) print i;  // 0 1 2
```
Good.

Ch24 Calls and Functions: call frames, stack, native clock, recursion fib(15)? Checkpoint:
```
fun fib(n) { if (n < 2) return n; return fib(n - 2) + fib(n - 1); }
print fib(10);  // 55
```
Stack overflow error: "Stack overflow." — confident.

Ch25 Closures: upvalues, open/closed:
```
fun makeCounter() { var i = 0; fun count() { i = i + 1; print i; } return count; }
var c = makeCounter(); c(); c();  // 1 2
```
Good. Also loop-variable capture semantics (each iteration fresh binding).

Ch27 Classes and Instances: class decl, instances, fields, OP_CLASS, OP_GET_PROPERTY/SET_PROPERTY? Properties are ch27 (fields), methods ch28. Checkpoint:
```
class Pair {}
var p = Pair();
p.first = 1; p.second = 2;
print p.first + p.second;  // 3
```
Good. Error: "Only instances have fields." — confident.

Ch28 Methods and Initializers: methods, this, init:
```
class Scone { topping(first, second) { print "scone with " + first + " and " + second; } }
Scone().topping("berries", "cream");
class Person { init(name) { this.name = name; } greet() { print "hi " + this.name; } }
Person("Bob").greet();  // hi Bob
```
Errors: "Only instances have methods.", "Can only use 'this' inside a class method."? Hmm — resolver error: "Can't use 'this' outside of a class." (ch11 already). init return error: "Cannot return a value from an initializer." — confident-ish. And "Can't use 'this' in a static context"? skip.

Ch29 Superclasses: OP_INHERIT, OP_GET_SUPER, OP_SET_SUPER? (set_super exists for fields on super? yes OP_SET_SUPER exists). Checkpoint:
```
class A { method() { print "A.method"; } }
class B < A { method() { print "B.method"; } test() { super.method(); } }
B().test();  // A.method
```
Errors: "Superclass must be a class." — confident.

Ch30 Optimization: constant folding; benchmark suite; compare runtime before/after. Checkpoint: run test/benchmark/*.lox? The book repo has test/benchmark/ with e.g. equality.lox? There are benchmarks in the repo? I recall test/benchmark exists? Hmm — the book mentions benchmarks in ch30 ("I generated some benchmarks"). The repo has test/benchmark/*.lox? I believe yes: test/benchmark/ contains files like `string_concat.lox`? Not sure of names. I'll phrase: "use the benchmark scripts from the book's repo test/benchmark/ (or write your own) and record times in PROGRESS.md".

Official test suite: test.py runner: `python3 test.py --interpreter <path>`? The book's test.py usage: `py test.py` expects clox/jlox built in the repo? The harness: `python3 test.py --interpreter path/to/clox`? I recall: `py test.py` runs against `clox` binary in repo root by default; options: `--interpreter`. Hmm. The README of the repo: "To run the test suite: py test.py"? I'll phrase: clone the repo, then `python3 test.py --interpreter ./clox` (and note: check `python3 test.py --help` for flags). Safe.

Now — how to structure TASKS.md for Claude Code executability. Each task should be a self-contained prompt the user can paste into Claude Code, or that Claude Code can pick up sequentially. Good format:

```
## T04 — Scanning (jlox)
- 章节: ch4 https://www.craftinginterpreters.com/scanning.html
- 目标: ...
- 概念: ...
- 涉及文件: jlox/src/com/craftinginterpreters/lox/{Token,Scanner,TokenType}.java
- 验收: command + expected
- 完成后: 在 PROGRESS.md 记录
```

Plus a "如何使用" section: one task per session; paste the task block as the prompt; Claude Code should implement + run the checkpoint; if checkpoint fails, debug; mark done in PROGRESS.md. Also coaching guardrails from the skill: Claude Code scaffolds but the learner writes core code? The skill's operating principles say learning-by-building, don't dump full solutions. Since the user asked for a task list Claude Code can execute, I'll include a "协作模式" note: two modes — 教练模式 (Claude explains + you write code) vs 代写模式 (Claude implements). Default per skill: coach mode, learner writes core. I'll encode that as instructions in TASKS.md header so each session follows it.

Also include the skill's rule: record progress in PROGRESS.md after each milestone.

Language choice: The book uses Java (jlox) then C (clox). The skill defaults to Java. I'll default to the book's own stack (Java + C) and note alternatives (e.g., do Part II in another language) as an option the user can pick at T00.

Repo layout:
```
crafting-interpreters/
├── jlox/          # Part II: Java tree-walk interpreter
│   └── src/com/craftinginterpreters/lox/
├── clox/          # Part III: C bytecode VM
│   ├── Makefile
│   └── *.c/h
├── test/          # .lox scripts + expected outputs (from book repo or self-written)
├── docs/lox-spec.md
└── PROGRESS.md
```

Build commands: jlox — javac + java, or a simple script. Keep dependency-free: `javac -d jlox/bin jlox/src/com/craftinginterpreters/lox/*.java` then `java -cp jlox/bin com.craftinginterpreters.lox.Lox`. clox: Makefile with `gcc -std=c11 -Wall -Wextra -o clox *.c` (book uses cc). Checkpoint T00: toolchain check `javac -version && gcc --version`.

Now the task list. Let me enumerate tasks:

Phase 0:
- T00 环境与骨架: check javac/gcc, create repo layout, jlox main that prints usage / reads file, Makefile for clox later. Checkpoint: `java -cp jlox/bin com.craftinginterpreters.lox.Lox` prints "Usage: jlox [script]" exit 64. The book: `System.err.println("Usage: jlox [script]"); System.exit(64);` — confident (EX_USAGE=64).

Phase I (reading):
- T01 ch1-2 阅读地图: read ch1 Introduction, ch2 A Map of the Territory; deliverable: docs/notes — write 10-line summary: scanner→parser→AST→interpreter vs bytecode VM; scavenger? Keep: docs/roadmap.md with the pipeline diagram in text. Checkpoint: file exists with the 5 pipeline stages listed. Light task.
- T02 ch3 Lox 语言规格: read ch3; write docs/lox-spec.md: types (number/string/bool/nil), expressions, statements, functions, classes; copy 3 example programs. Checkpoint: docs/lox-spec.md contains keywords list (and, or, fun, var, class, super, this, print, return, while, for, if, else, true, false, nil). Also set up test harness: clone book repo test suite? I'll put test harness setup here: `git clone --depth 1 https://github.com/munificent/craftinginterpreters book-tests` into project dir (allowed: inside project). Then `python3 book-tests/test.py --help` works. Hmm — cloning the whole repo includes book source; fine, depth 1. Or just copy test/ dir. Keep simple: clone into `book-tests/` (gitignored later). Checkpoint: `ls book-tests/test | head` shows test dirs.

Phase II (jlox, ch4-13): T04..T13 as above.

Phase III (clox, ch14-30): T14..T30.

Backmatter:
- T31 附录: Lox grammar appendix — cross-check docs/lox-spec.md against Appendix I grammar; write docs/grammar.md with full productions. Checkpoint: grammar covers all statements/expressions incl. sugar.
- T32 (optional) 毕业项目: extend Lox with a feature of your choice (e.g., arrays/lists, string interpolation, switch? book suggests: "lists", "maps"? The book's challenges suggest adding features). Deliverable: one feature end-to-end in clox with tests. Checkpoint: new test passes.

Also a final task: run full official test suite for jlox and clox, record pass counts in PROGRESS.md. The book's test suite covers both interpreters (same .lox files with expected outputs). jlox passes most but not all (some tests rely on clox-specific behavior? mostly both). Note: some tests expect specific error messages that differ between jlox/clox? The suite is shared and both pass nearly all. I'll phrase: run suite, record pass/fail, fix regressions.

Number of tasks: T00, T01, T02, T04-T13 (10), T14-T30 (17), T31, T32, T33(final suite). That's ~33 entries. That's a lot of writing but it's the deliverable. Keep each entry compact (5-6 lines).

Per the skill: "one entry per milestone — goal, files to touch, key concept, and a verification command with expected output." I'll follow exactly that schema, in Chinese (user speaks Chinese), with commands in English.

Also per skill step 4: "End the reply with the first runnable checkpoint (the exact command to run for milestone 1 and what the user should see)."

Now — should I call plan/explore tools? The developer instructions: "Before modifying code, call explore once..." — I'm creating a new TASKS.md file (a doc, but still a file write). "For any multi-step change (>1 file...)" — this is a single file write. The explore tool: "Record a structured exploration note before editing any code". Writing TASKS.md is not code editing per se, but to be safe and compliant, I'll do a quick explore call consolidating findings, then write the file. Actually the instruction says call explore once before modifying code — I've done the reading; a single explore call to consolidate is cheap and compliant. Then write TASKS.md. A plan call for a single-file write is overkill; the skill's workflow (convert → write TASKS.md → end with checkpoint) is already prescribed. I'll skip `plan` (single logical action, one file) but do `explore` to record findings. Hmm, the instruction says explore is for "before editing any code" — TASKS.md is a markdown deliverable, not code. I'll still do one lightweight explore to be safe since it's the prescribed flow and costs little.

Actually, let me reconsider: the guidance says "Before modifying code, call `explore` once to record the files you have read (or intend to read), what you already confirmed, and what is still unknown." I'll do it — it also helps the session record the skill workflow.

Where to put TASKS.md? Workspace root. Let me check what's in the workspace root first — quick ls. I'll combine with the explore call? explore doesn't read files. Let me do bash ls + explore in parallel, then write.

Now let me draft the TASKS.md content carefully.

Key exact strings I'll use (from the book, high confidence):

jlox:
- Usage: `Usage: jlox [script]` exit 64.
- Token dump: `type lexeme literal`, e.g. for `var x = 1;`:
  ```
  VAR VAR null
  IDENTIFIER x null
  EQUAL = null
  NUMBER 1 1.0
  SEMICOLON ; null
  EOF  null
  ```
  (EOF line has two spaces: "EOF" + " " + "" + " " + "null" → "EOF  null"). I'll note the double space.
- AstPrinter: `(+ 1 (* 2 3))`.
- Parse error: `Error: Expect expression.`? The book's Lox.error prints `[line N] Error message`. For parse errors via `error(token, message)`: if token.type == EOF → "Error at end: Expect expression." else "Error at 'X': Expect expression." For `1 + ;` → `Error at ';' : Expect expression.`? The format: `"[line " + line + "] Error" + where + ": " + message` where where = " at ';'". So output: `[line 1] Error at ';': Expect expression.` Hmm — for `;` token, where is " at ';'". So `[line 1] Error at ';': Expect expression.` I'll use that. Exit 65.
- REPL: `1 + 2 * 3` → `7`; `"a" + "b"` → `ab`; `"a" + 1` → `[line 1] Error: Operands must be two numbers or two strings.` exit 70. Runtime error format: `"[line " + line + "] Error: " + message`? In ch7 the book prints runtime errors as `[line N] Error: message`? RuntimeError has token; Lox.runtimeError prints `[line N] Error: message`? The book: `System.err.println(message + "\n[line " + error.token.line + "]");`? Hmm. In ch7: 
  ```java
  private static void runtimeError(RuntimeError error) {
    System.err.println(error.getMessage() + "\n[line " + error.token.line + "]");
    hadRuntimeError = true;
  }
  ```
  So output is message then newline then `[line 1]`. So `Operands must be two numbers or two strings.\n[line 1]`. I'll write expected as two lines. Later (ch8+) runtimeError changes? In ch8 it stays similar. OK I'll present expected output as the message + `[line 1]` line, noting format per book.
  
  Hmm wait, in later chapters (ch10+) runtimeError prints `[line N] Error` prefix? Let me recall ch10: `System.err.println(error.getMessage() + "\n[line " + error.token.line + "]");` — I think it stays. Fine.

- Ch8: 
  ```
  var a = 1;
  print a;   // 1
  a = 2;
  print a;   // 2
  print b;   // Undefined variable 'b'. + [line 5]
  ```
- Ch9: while/if/for/logical outputs as above.
- Ch10: add(1,2)=3, fib(10)=55, `print clock;` → `<native fn>`, arity error `Expected 2 arguments but got 1.`.
- Ch11: 
  ```
  var a = "outer";
  fun f() { print a; var a = "inner"; print a; }
  f();
  ```
  Hmm — `print a` before `var a` in function scope: resolver sees `a` declared later in same scope → error "Can't read local variable in its own initializer."? Wait no: the resolver's declare() adds the var to scope only AFTER... In the book, visitVarStmt: resolve(r.stmt.initializer) happens BEFORE declare(name). So `print a;` (a statement before var) — when resolving `print a`, is `a` in scopes? The `var a` statement hasn't been declared yet when resolving earlier statements, so `print a` resolves to the GLOBAL a → prints "outer". Then `var a = "inner"` shadows. So output: `outer\ninner`. That's the book's ch11 example exactly (the "closure captures variable at resolution" demo). Good — I'll use that as the checkpoint: f() prints outer then inner.
  Plus error case: `{ var a = a; }`? Hmm — `var a = a;` at top level: initializer resolved before declare → resolves to global a → OK at top level. Inside a block: `{ var a = a; }` — same: resolve initializer first, `a` not yet declared → resolves to global. So when does "Can't read local variable in its own initializer." trigger? `var a = a` where... hmm, actually the book's check: in resolveLocal, if scopes.peek().get(name.lexeme) == Boolean.FALSE → error. FALSE is set by declare() (declared but not defined). declare() is called after resolving initializer. So `var a = a;` inside a function: resolve initializer `a` → not in scope map yet → global. Then declare sets FALSE, then define sets TRUE. So the error triggers for... `fun f() { print a; var a = "inner"; }`? Resolving `print a`: scopes contains? `var a` statement comes after, so when resolving `print a`, declare hasn't run → `a` resolves to global. Hmm, so when does FALSE ever get read? 

  Ah — I remember: the book's resolver declares function parameters and... the FALSE case: `class` inheritance? No. Let me think: declare() sets FALSE, define() sets TRUE. Between declare and define, the only resolution that happens is the initializer itself — but resolve(initializer) happens BEFORE declare. So FALSE is never observed?? No wait — for `var a = <expr>`, order in visitVarStmt: `resolve(stmt.initializer); declare(stmt.name); define(...)`. So initializer resolved before declare. FALSE never read for var. But for FUNCTION declarations: visitFunctionStmt: declare(name) FIRST, then resolve function body (parameters declared, body resolved), then define. So inside the function body, references to the function name itself see FALSE → but that's allowed (recursion) — resolveLocal skips FALSE? No: resolveLocal errors on FALSE... but for functions the book handles it: in resolveLocal, `if (entry == Boolean.FALSE) error "Can't read local variable in its own initializer."` — hmm, but then recursion `fun f() { f(); }` would error? No — because `f` inside the body: resolveLocal walks scopes from innermost; the function's own name is in the ENCLOSING scope (declared in the scope where fun stmt appears), and it's FALSE while resolving the body... That would error on recursion!

  Let me recall the actual book code (ch11):
  ```java
  private void resolveLocal(Expr expr, Token name) {
    for (int i = scopes.size() - 1; i >= 0; i--) {
      if (scopes.get(i).containsKey(name.lexeme)) {
        if (scopes.get(i).get(name.lexeme) == Boolean.FALSE) {
          Lox.error(name, "Can't read local variable in its own initializer.");
        }
        interpreter.resolve(expr, scopes.size() - 1 - i);
        return;
      }
    }
  }
  ```
  And visitFunctionStmt:
  ```java
  declare(stmt.name);
  resolveFunction(stmt.function, Type.FUNCTION);
  define(stmt.name);
  ```
  Hmm — so `fun f() { var f = 3; f(); }`? Inner `var f` shadows. Recursion: `fun f() { f(); }` — resolving `f()` inside body: innermost scopes are the function body scope (params), then the scope containing `f` with FALSE → error?! That can't be right; the book supports recursion (ch10 fib recursion works, and ch11 must preserve it).

  Resolution: I misremember. The book's declare/define FALSE trick: declare() only adds if... and in resolveLocal the FALSE check exists, and for functions the book declares AFTER? Let me recall ch11 text: "we declare the function's name before resolving its body so recursion works"... and the FALSE check: "if we're trying to read a variable whose value is false, it's in the middle of its own initialization → error". And recursion works because... hmm, in visitFunctionStmt the order is declare → resolve body → define. The function name is FALSE during body resolution. `f()` inside body → resolveLocal finds `f` with FALSE → error "Can't read local variable in its own initializer."?? But recursion demonstrably works in jlox ch11 (fib example in later chapters uses recursion and resolver).

  Wait — maybe declare() for functions... Let me recall the actual code from the book (I've read it):

  ```java
  @Override
  public Void visitFunctionStmt(Stmt.Function stmt) {
    declare(stmt.name);
    resolveFunction(stmt.function, FunctionType.FUNCTION);
    define(stmt.name);
    return null;
  }
  ```
  and
  ```java
  private void declare(Token name) {
    if (scopes.isEmpty()) return;
    Scope scope = scopes.peek();
    if (scope.containsKey(name.lexeme)) Lox.error(name, "Already a variable with this name in this scope.");
    scope.put(name.lexeme, false);
  }
  private void define(Token name) { if (scopes.isEmpty()) return; scopes.peek().put(name.lexeme, true); }
  ```
  and resolveLocal with the FALSE check as above. Then `fun f() { f(); }`: resolving the call's callee `f`: scopes = [global(f→false), bodyScope]. Innermost bodyScope doesn't contain f; next scope global contains f→FALSE → error?! 

  Hmm, but wait — the FALSE check message is "Can't read local variable in its own initializer." For a function name that would be wrong. Let me reconsider: maybe the FALSE check only applies... Actually! I remember now: the book's resolveLocal FALSE check exists, and recursion works because the function name is declared in the scope ENCLOSING the body, and when resolving the body, the name IS found with FALSE → the book handles this: in resolveFunction, the book... hmm.

  Let me look at it from the test suite angle: test/function/recursion? The suite has test/closure? There's definitely recursion working. So the book's code must allow it. Resolution: I think declare() is called AFTER resolving for varI was in the middle of reasoning through the resolver's FALSE-check semantics for the ch11 checkpoint. Let me settle that quickly, then write TASKS.md.

The book's ch11 code (I recall it now correctly):

```java
@Override
public Void visitVarStmt(Stmt.Var stmt) {
  declare(stmt.name);
  if (stmt.initializer != null) {
    resolve(stmt.initializer);
  }
  define(stmt.name);
  return null;
}
```

Wait — actually the book changed the order in ch11: declare FIRST, then resolve initializer, then define. That's exactly what makes "Can't read local variable in its own initializer." reachable: `var a = a;` inside a block/function → resolving initializer `a` finds `a` with FALSE → error. And for functions, declare() is called before resolving the body, but resolveLocal's FALSE check... recursion: `fun f() { f(); }` — resolving `f` inside the body: the function name is in the enclosing scope with FALSE → would error?

No — I remember the book's actual resolveLocal:

```java
private void resolveLocal(Expr expr, Token name) {
  for (int i = scopes.size() - 1; i >= 0; i--) {
    if (scopes.get(i).containsKey(name.lexeme)) {
      if (scopes.get(i).get(name.lexeme) == Boolean.FALSE) {
        Lox.error(name, "Can't read local variable in its own initializer.");
      }
      interpreter.resolve(expr, scopes.size() - 1 - i);
      return;
    }
  }
}
```

And recursion works because... hmm. Actually I now recall the book's text in ch11: "we declare the function's name before resolving its body" — and the FALSE check would fire for direct recursion. But the book explicitly handles this: in visitFunctionStmt, the book does NOT declare before? Let me recall the actual text: "After declare() returns, we resolve the function's body... A function declaration declares its own name so that recursion works" — and the FALSE state: "we use false to mean 'declared but not yet defined'... if we read a variable in that state, it's an error: reading a variable in its own initializer."

And for recursion: `fun isEven(n) { ... isOdd(...) }` mutual recursion works because the name is defined by the time the body RUNS, but resolution happens while FALSE... The check would fire. Unless — the book's declare() for functions... 

OK, I've spent enough on this. The exact behavior: I'm confident about these test-suite-backed facts:
- `var a = a;` (local) → error "Can't read local variable in its own initializer." — this is the documented purpose of the FALSE check (test/variable/uninitialized_early? or similar).
- Recursion works in jlox ch11+ (fib examples throughout the book).

Both are true simultaneously, so the book's code must handle it. The resolution (which I now genuinely recall): in ch11, visitVarStmt order is declare → resolve initializer → define, and the FALSE check fires for `var a = a;`. For functions, the book declares the name before resolving the body, and resolveLocal's FALSE check... the book's text says: "we declare the function's name before we resolve its body so that recursion works" — and the FALSE check is bypassed because... 

AH WAIT. I remember now! The book's resolveLocal FALSE check message and the recursion case: the book's declare() puts FALSE, and for functions the body resolution finds the name with FALSE — but the book's text in ch11 says: "Since we declare the function's name before resolving its body, references to the function's own name inside its body resolve correctly" — and the FALSE check: "the only way to hit that error is `var a = a;`"... 

Hmm, no. Actually — I finally recall the real detail: the book's declare() is:

```java
private void declare(Token name) {
  if (scopes.isEmpty()) return;
  Map<String, Boolean> scope = scopes.peek();
  scope.put(name.lexeme, false);
}
```

and visitFunctionStmt:

```java
declare(stmt.name);
resolveFunction(stmt.function, FunctionType.FUNCTION);
define(stmt.name);
```

and resolveLocal has the FALSE check. So `fun f() { f(); }` → resolving `f` in body: found FALSE → error "Can't read local variable in its own initializer."?? That contradicts recursion working.

Let me just test my memory against the known test suite: test/function/recursion? Hmm, I don't remember such a test. But fib recursion in ch10 (before resolver) works. In ch11+, does the book still show recursion? Ch13+ examples use recursion? The clox chapters definitely have recursion (ch24 calls, fib). jlox with resolver: the book's ch11 text explicitly says: "we declare the function's name before resolving its body. That lets references to the function's own name inside its body resolve to the function itself — recursion!" And the FALSE check: "if we try to read a variable that's declared but not defined, it must be in its own initializer" — for FUNCTIONS, reading the name while FALSE is FINE (recursion), so... the book must special-case it.

I recall the actual book code now with certainty — resolveLocal:

```java
if (scopes.get(i).get(name.lexeme) == Boolean.FALSE) {
  Lox.error(name, "Can't read local variable in its own initializer.");
}
```

Hmm, and the book's ch11 text: "we report an error if the variable is read while it's in this half-initialized state" — and then: "This is a bit strict... `var a = a;`". And for functions: the book's declare-before-resolve means the function name is FALSE during body resolution, so `fun f() { f(); }` WOULD error... unless the book's text says otherwise.

You know what — I've hit the limit of reliable memory on this micro-detail. The task list doesn't need to resolve it. For T11's checkpoint I'll use behaviors I'm 100% sure of:
1. Shadowing/closure resolution: `var a = "outer"; fun f() { print a; var a = "inner"; print a; } f();` → prints `outer` then `inner` (this is literally the book's ch11 example demonstrating resolution to the right declaration).
2. Early return error: `return 1;` at top level → "Can't return from top-level code." (confident, test suite has return_at_top_level.lox).
3. `this` outside class → "Can't use 'this' outside of a class." (confident).
4. Duplicate declaration in same scope → "Already a variable with this name in this scope." (confident).

And I'll mention `var a = a;` in a block → "Can't read local variable in its own initializer." with a "(以书/测试套件实际输出为准)" hedge. Actually — the test suite file test/variable/uninitialized_early.lox? I'm fairly confident the message string is right; the trigger is `var a = a;` in a local scope. I'll include it but mark the whole error-message set with a note: "错误文案以书内实现与官方测试套件 expected 输出为准". That's honest and keeps the task list executable (Claude Code will run and see).

Similarly for ch13 self-inheritance: "A class can't inherit from itself." — I'll include with the same hedge note. Actually I'm quite confident about "Superclass must be a class." (ch13 runtime check) and the resolver's self-inheritance check exists. Fine.

One more thing to verify from memory: print statement in clox — which chapter? I reasoned ch21. Let me double-check by recalling ch21 "Global Variables" content: OP_DEFINE_GLOBAL, OP_GET_GLOBAL, OP_SET_GLOBAL... and the chapter opens with "we can't write useful programs yet because we can't observe anything — time to add print"? Hmm, actually I now recall ch21's opening: "Our VM can barely do anything... In this chapter we add global variables AND the print statement"? 

I genuinely believe print is ch21 — the book says something like "we'll add the print statement here because without output, variables are pointless". Hmm, but wait — I also have a memory of ch17 ending with "we can't print yet, but the debug trace shows the stack". And ch18/19/20 have no print. So print must come at ch21 (first chapter where programs can do something observable: globals). Yes — ch21. I'm confident enough; and the task list's ch17-20 checkpoints use the disassembler/trace, which is correct regardless.

Also ch15 checkpoint: the book's main in ch15 pushes constant 1.2, negates it, returns. Trace output:
```
== test chunk ==
0000 0000 OP_CONSTANT         0 '1.2'
0002 0000 | OP_NEGATE
0003 0000 | OP_RETURN
```
Wait — the trace format: `disassembleInstruction` prints `%04d %04d ` then the name padded to 16, then for OP_CONSTANT the constant index and value. The `|` for same line. Stack trace after each instruction: `          [ ]` / `          [ 1.2 ]` / `          [ -1.2 ]`. The book's printf for stack: `printf("          [ ");` then values `printf("%g", value)` → `1.2`, `-1.2`. So expected:
```
== test chunk ==
0000 0000 OP_CONSTANT         0 '1.2'
          [ 1.2 ]
0002 0000 | OP_NEGATE
          [ -1.2 ]
0003 0000 | OP_RETURN
          [ ]
```
Hmm, the constant value format: `printf("'%g'", constant)`? In disassembleInstruction: `printf("%4d '", index); printValue(constant); printf("'\n");` → `   0 '1.2'`. So line: `0000 0000 OP_CONSTANT         0 '1.2'`. Close enough — I'll present it with a hedge "格式细节以书内 disassembleChunk 输出为准" and show the key lines. Actually for executability, exact expected output matters. I'll show my best reconstruction and add the hedge note once globally in the header: "预期输出按书中实现重建；若与实际运行有细微格式差异（空格/换行），以实际实现为准，判定标准是语义一致。" That's a reasonable, honest global note.

Ch14 checkpoint: main writes chunk with OP_RETURN, disassembles:
```
== test chunk ==
0000 0000 OP_RETURN
```
Confident.

Now the jlox build/run commands. Keep zero-dependency:
- Build: `javac -d jlox/out $(find jlox/src -name '*.java')`
- Run: `java -cp jlox/out com.craftinginterpreters.lox.Lox script.lox`
- REPL: `java -cp jlox/out com.craftinginterpreters.lox.Lox`

clox:
- `make -C clox` (Makefile: `cc -std=c11 -Wall -Wextra -g -o clox *.c`? book uses `cc -g -O3`? ch14 Makefile: `CFLAGS = -Wall -Wextra -std=c11 -g`? The book's Makefile: `cc -c -Wall -Wextra -std=c11 -g *.c`? I'll just specify a Makefile with `cc -std=c11 -Wall -Wextra -g -O2 -o clox *.c` — implementation detail for the task.)
- Run: `./clox/clox script.lox`

Test suite (T02 setup + T33 final):
- `git clone --depth 1 https://github.com/munificent/craftinginterpreters book-tests`
- `python3 book-tests/test.py --interpreter "java -cp jlox/out com.craftinginterpreters.lox.Lox"`? The harness's --interpreter flag: I recall `py test.py --interpreter <cmd>` exists? The book's test.py: usage `py test.py` and it looks for `clox` or `jlox`? I recall options: `--interpreter` (path to interpreter binary). Hmm. To be safe: "运行 `python3 book-tests/test.py --help` 查看参数，用 `--interpreter` 指向你的解释器（jlox 需要一个可执行包装脚本）"。For jlox, a wrapper script `bin/jlox`:
  ```sh
  #!/bin/sh
  exec java -cp "$(dirname "$0")/../jlox/out" com.craftinginterpreters.lox.Lox "$@"
  ```
  That's a nice touch — include in T00 or T02.

Now the header of TASKS.md — how to use with Claude Code:
- 每个任务一个会话/一次提交；把任务块直接作为 prompt 粘贴给 Claude Code。
- 协作模式开关：`模式: 教练`（默认，Claude 讲概念+给骨架，核心代码自己写）或 `模式: 代写`（Claude 直接实现并跑验收）。Per the skill's coaching rules, default coach mode.
- 每个任务完成后：跑验收命令 → 通过后在 PROGRESS.md 追加一行（任务号、验收命令、结果、日期）→ git commit。
- 卡住时：把报错原文贴给 Claude Code，要求"最小修复"。
- 全局约定：错误信息文案以书内实现/官方测试套件为准；预期输出为语义判定。

Also include the milestone table mapping chapters → tasks at a glance (progress overview with checkboxes).

Structure of TASKS.md:

```markdown
# Crafting Interpreters — Claude Code 学习任务清单

来源: http://www.craftinginterpreters.com/ (Robert Nystrom, 免费在线全文)
产出: jlox (Java 树遍历解释器, Part II) + clox (C 字节码虚拟机, Part III)

## 使用方法 (给 Claude Code 的全局指令)
...

## 里程碑总览
| 任务 | 章节 | 里程碑 | 验收 |
...

## Phase 0 — 准备
### T00 ...
## Phase I — 阅读 (ch1-3)
### T01, T02
## Phase II — jlox (ch4-13)
### T04..T13
## Phase III — clox (ch14-30)
### T14..T30
## 收尾
### T31, T32, T33
```

Each task block format (per skill: goal, files to touch, key concept, verification command with expected output):

```markdown
### T04 · Scanning — 词法扫描器
- 阅读: https://www.craftinginterpreters.com/scanning.html
- 目标: ...
- 概念: ...
- 文件: ...
- 验收: `cmd` → expected
```

Prompt-ability: I'll add a line at top: "把单个任务块（含标题）整段粘贴给 Claude Code 即可执行". 

Now write all 30+ task entries. Keep each tight. Let me draft the content now. I need to be careful with lengths — the previous answer got truncated, so I should write the file in maybe 2-3 write/edit calls? The write tool takes full content — one big write could hit output limits again. The file will be ~400-500 lines. That's roughly 15-20KB. Should be fine in one write call, but to be safe I'll split: write Phase 0-II first, then append Phase III + 收尾 via edit. Actually edit requires exact old_text match — I can end the first write with a marker line and replace it. Or use bash heredoc append. Simpler: two writes — first write full file part 1 with a trailing marker `<!-- PART2 -->`, then edit replacing the marker with part 2. Let me do that.

Also: the explore call before writing. Let me do explore + ls in parallel now, then write.

Actually — do I still need the ls? I know the workspace has .agents/. A quick ls confirms no existing TASKS.md or project. Combine: bash `ls -la` + explore in one block.

Then: write TASKS.md (part 1), edit (append part 2), then final reply ending with the first runnable checkpoint per the skill.

Let me now compose the actual content.

---

Part 1 content:

# Crafting Interpreters · Claude Code 学习任务清单

- 教程: http://www.craftinginterpreters.com/ — Robert Nystrom，全文免费在线
- 最终产出: 两个完整的 Lox 解释器
  - `jlox/` — Java 树遍历解释器（Part II, ch4–13）
  - `clox/` — C 字节码虚拟机（Part III, ch14–30）
- 用法: 每个任务 = 一次 Claude Code 会话。把任务块整段粘贴为 prompt。完成后跑验收命令，通过则记入 PROGRESS.md 并 git commit。

## 全局约定（每个会话都生效，可随任务块一起粘贴）

1. 模式默认为"教练"：Claude Code 先用 3–6 句讲清本任务核心概念，给出类/函数骨架，核心逻辑由学习者编写；学习者明确说"代写"时才由 Claude Code 实现。
2. 不一次性给出整本书的代码；只做当前任务，保持已有代码不动。
3. 每个任务以验收命令通过为完成标准；失败时从真实报错出发做最小修复。
4. 错误信息文案（如 `Undefined variable 'b'.`）以书中实现与官方测试套件的 expected 输出为准；预期输出中的空格/换行等格式细节以实际运行为准，判定看语义。
5. 完成后在 PROGRESS.md 追加一行：`Txx | 验收命令 | 结果 | 日期`，然后 commit。
6. 不安装全局工具链；需要依赖时打印命令让学习者自己执行。

## 目录结构

```
crafting-interpreters/
├── jlox/src/com/craftinginterpreters/lox/   # Java 源码
├── jlox/out/                                # javac 输出 (gitignore)
├── bin/jlox                                 # 可执行包装脚本（跑官方测试套件用）
├── clox/                                    # C 源码 + Makefile
├── docs/                                    # lox-spec.md, roadmap.md, grammar.md
├── book-tests/                              # 官方测试套件 clone (gitignore)
├── test/                                    # 自写 .lox 冒烟脚本
└── PROGRESS.md
```

## 里程碑总览

| 任务 | 章节 | 里程碑 | 一句话验收 |
|---|---|---|---|
| T00 | — | 工具链 + 项目骨架 | `jlox` 无参运行打印 Usage，退出码 64 |
| T01 | 1–2 | 阅读导论，写管线笔记 | docs/roadmap.md 列出 5 阶段管线 |
| T02 | 3 | Lox 语言规格 + 测试套件 | docs/lox-spec.md 含全部关键字；book-tests 可用 |
| T04 | 4 | Scanner | `--tokens` 输出 token 流 |
| T05 | 5 | AST + AstPrinter | `(+ 1 (* 2 3))` |
| T06 | 6 | 递归下降 Parser | 解析成功/报错退出码 65 |
| T07 | 7 | 表达式求值 | REPL `1 + 2 * 3` → 7 |
| T08 | 8 | 语句 + 环境 | var/print/赋值/未定义变量报错 |
| T09 | 9 | 控制流 | if/while/for/短路逻辑 |
| T10 | 10 | 函数 | fib(10) → 55 |
| T11 | 11 | Resolver | 闭包绑定正确 + 静态作用域报错 |
| T12 | 12 | 类 | 字段 + `<X instance>` |
| T13 | 13 | 继承 | super 调用 |
| T14 | 14 | 字节码块 + 反汇编器 | `OP_RETURN` 反汇编输出 |
| T15 | 15 | VM 主循环 | 跟踪栈变化 |
| T16 | 16 | 按需扫描 | clox 读 .lox 源码产出 token |
| T17 | 17 | 表达式编译 | 编译 `1*2+3` 产出正确字节码 |
| T18 | 18 | 值类型 | 布尔/nil/比较指令 |
| T19 | 19 | 字符串 | 拼接 + 字符串驻留 |
| T20 | 20 | 哈希表 | 插入/查找/删除/tombstone |
| T21 | 21 | 全局变量 + print | 第一个可见输出 `print 1;` |
| T22 | 22 | 局部变量 | 槽位指令 + 嵌套作用域 |
| T23 | 23 | 跳转 | while/for 循环 |
| T24 | 24 | 调用 | CallFrame + 递归 + clock |
| T25 | 25 | 闭包 | Upvalue 捕获 |
| T26 | 26 | GC | 标记-清除 + 压力测试 |
| T27 | 27 | 类与实例 | 字段读写 |
| T28 | 28 | 方法与 init | this + 构造器 |
| T29 | 29 | 超类 | OP_INHERIT/GET_SUPER |
| T30 | 30 | 优化 | 常量折叠 + 基准对比 |
| T31 | 附录 | 语法总表 | docs/grammar.md 对照附录 I |
| T32 | — | 全量测试 | 官方套件通过率记录 |
| T33 | — | 毕业项目 | 自选扩展特性端到端 |

---

## Phase 0 — 准备

### T00 · 工具链与项目骨架
- 目标: 建立仓库结构，jlox 入口能跑起来。
- 概念: REPL vs 脚本模式；退出码约定（64 用法错误 / 65 语法错误 / 70 运行时错误）。
- 文件: `jlox/src/com/craftinginterpreters/lox/Lox.java`、`bin/jlox`、`.gitignore`、`PROGRESS.md`
- 步骤:
  1. 确认工具链: `javac -version`（≥11 即可）、`cc --version` 或 `gcc --version`、`python3 --version`。
  2. 建目录结构；写 `Lox.java`：无参 → stderr 打印 `Usage: jlox [script]` 退出 64；文件参数 → 读入内容（暂存为字符串）；多参 → 退出 64。
  3. 写 `bin/jlox` 包装脚本（供官方测试套件调用）。
- 验收:
  ```
  $ javac -d jlox/out $(find jlox/src -name '*.java')
  $ java -cp jlox/out com.craftinginterpreters.lox.Lox
  Usage: jlox [script]
  $ echo $?
  64
  ```

## Phase I — 阅读（ch1–3）

### T01 · 导论与地图（ch1–2）
- 阅读: introduction.html, a-map-of-the-territory.html
- 目标: 建立"解释器管线"心智模型。
- 文件: `docs/roadmap.md`
- 要点: scanner → parser → (AST | bytecode) → interpreter/VM；tree-walk vs bytecode 两条路线的取舍；编译期/运行期划分。
- 验收: `docs/roadmap.md` 存在且按顺序列出 5 个管线阶段，并用 3–5 句话对比 jlox 与 clox 路线。

### T02 · Lox 语言规格 + 测试套件（ch3）
- 阅读: the-lox-language.html
- 目标: 把语言规格落成文档；接入官方测试套件。
- 文件: `docs/lox-spec.md`、`book-tests/`（clone）
- 步骤:
  1. `docs/lox-spec.md`：数据类型（number/string/bool/nil）、动态类型、表达式与语句、函数/闭包、类/继承，附 2–3 个书内示例程序。
  2. 列出全部保留字: and class else false fun for if nil or print return super this true var while。
  3. `git clone --depth 1 https://github.com/munificent/craftinginterpreters book-tests`
- 验收:
  ```
  $ grep -c 'and\|class\|fun\|print' docs/lox-spec.md   # ≥ 4
  $ ls book-tests/test | head
  assignment  blocks  bool  ...（测试目录列表）
  ```

---

## Phase II — jlox：树遍历解释器（ch4–13）

### T04 · Scanning（ch4）
- 阅读: scanning.html
- 目标: 手写词法扫描器，源码 → Token 流。
- 概念: lexeme vs token；最大匹配；行号跟踪；错误恢复（继续扫描）。
- 文件: `TokenType.java`（枚举）、`Token.java`、`Scanner.java`；`Lox.java` 加 `--tokens` 调试开关。
- 验收:
  ```
  $ java -cp jlox/out com.craftinginterpreters.lox.Lox --tokens test/tokens.lox
  VAR VAR null
  IDENTIFIER x null
  EQUAL = null
  NUMBER 1 1.0
  SEMICOLON ; null
  EOF  null
  ```
  其中 `test/tokens.lox` 内容为 `var x = 1;`；EOF 行 lexeme 为空所以是两个空格。另测: `@` → `[line 1] Error: Unexpected character.`（文案以书为准）。

### T05 · Representing Code（ch5）
- 阅读: representing-code.html
- 目标: 定义 Expr AST 类族 + AstPrinter（前缀括号打印）。
- 概念: 用 Visitor 模式绕开 Java 无 union 类型；元编程生成样板（书用脚本，手写亦可）。
- 文件: `Expr.java`（Literal/Unary/Binary/Grouping + Visitor）、`AstPrinter.java`
- 验收: 在 main 或临时测试中构造 `1 + 2 * 3` 的 AST 并打印:
  ```
  (+ 1 (* 2 3))
  ```

### T06 · Parsing Expressions（ch6）
- 阅读: parsing-expressions.html
- 目标: 递归下降解析器，Token 流 → Expr。
- 概念: 文法优先级链（expression→equality→comparison→term→factor→unary→primary）；左结合用循环、右结合用递归；ParseError 同步恢复。
- 文件: `Parser.java`
- 验收:
  ```
  $ java -cp jlox/out com.craftinginterpreters.lox.Lox --ast '1 + 2 * 3;'
  (+ 1 (* 2 3))
  $ java -cp jlox/out com.craftinginterpreters.lox.Lox --ast '1 + ;'
  [line 1] Error at ';': Expect expression.
  $ echo $?
  65
  ```
  （`--ast` 为调试开关：解析后用 AstPrinter 打印。）

### T07 · Evaluating Expressions（ch7）
- 阅读: evaluating-expressions.html
- 目标: 树遍历求值器；REPL 支持表达式回显。
- 概念: Java 的 Number/Boolean/String 装箱对应 Lox 动态类型；真值规则（nil/false 为假）；`+` 数字相加、字符串拼接；运行时错误 RuntimeError。
- 文件: `Interpreter.java`；`Lox.java` REPL 中表达式回显。
- 验收:
  ```
  $ java -cp jlox/out com.craftinginterpreters.lox.Lox
  > 1 + 2 * 3
  7
  > "a" + "b"
  ab
  > "a" + 1
  Operands must be two numbers or two strings.
  [line 1]
  ```
  （运行时错误后进程退出码 70。）

### T08 · Statements and State（ch8）
- 阅读: statements-and-state.html
- 目标: 语句层（print/var/表达式语句/块）+ Environment 链。
- 概念: 声明 vs 定义 vs 赋值；环境链实现块级作用域与遮蔽；`print` 是语句不是函数。
- 文件: `Stmt.java`、`Environment.java`；`Parser.java`/`Interpreter.java` 扩展。
- 验收: `test/state.lox`:
  ```
  var a = 1;
  print a;
  a = 2;
  print a;
  { var a = "inner"; print a; }
  print a;
  print b;
  ```
  → 输出 `1 2 inner 2`，最后 `[line 7]` 附近报 `Undefined variable 'b'.`，退出码 70。

### T09 · Control Flow（ch9）
- 阅读: control-flow.html
- 目标: if/else、while、for（语法糖）、and/or 短路。
- 概念: for 循环在 Parser 层脱糖为 while；短路求值在 Interpreter 层直接返回操作数。
- 文件: `Parser.java`、`Interpreter.java`、`AstPrinter.java`（如需）
- 验收: `test/control.lox`:
  ```
  var i = 0;
  while (i < 3) { print i; i = i + 1; }
  for (var j = 0; j < 2; j = j + 1) print j;
  if (i == 3) print "done"; else print "no";
  print true and false;
  print false or "fallback";
  ```
  → `0 1 2 0 1 done false fallback`

### T10 · Functions（ch10）
- 阅读: functions.html
- 目标: 函数声明/调用/return + 原生函数 clock()。
- 概念: 调用 = 新环境 + 执行体；return 用异常 unwind；参数个数校验（arity）。
- 文件: `Stmt.Function`、`Expr.Call`、`LoxFunction.java`、`LoxCallable.java`、`Lox.java`（clock）
- 验收: `test/fn.lox`:
  ```
  fun add(a, b) { return a + b; }
  print add(1, 2);
  fun fib(n) { if (n < 2) return n; return fib(n - 2) + fib(n - 1); }
  print fib(10);
  print clock;
  add(1);
  ```
  → `3 55 <native fn>`，最后报 `Expected 2 arguments but got 1.` 退出码 70。

### T11 · Resolving and Binding（ch11）
- 阅读: resolving-and-binding.html
- 目标: Resolver 静态分析 pass，给每个变量标注作用域距离。
- 概念: 语义分析在解释前一次性完成；距离 = 从当前环境向外走几层；静态作用域错误提前报。
- 文件: `Resolver.java`；`Expr.Variable/Assignment` 加 distance 字段；`Interpreter` 按 distance 直接寻址。
- 验收: `test/resolve.lox`:
  ```
  var a = "outer";
  fun f() { print a; var a = "inner"; print a; }
  f();
  ```
  → `outer` `inner`（第一个 a 在解析期绑定到全局）。
  错误用例（各自单独运行，文案以书为准）:
  - 顶层 `return 1;` → `Can't return from top-level code.`
  - 顶层 `this;` → `Can't use 'this' outside of a class.`
  - 块内 `var a = a;` → `Can't read local variable in its own initializer.`
  - 同块重复 `var a = 1; var a = 2;` → `Already a variable with this name in this scope.`

### T12 · Classes（ch12）
- 阅读: classes.html
- 目标: 类声明、实例化、字段读写、方法调用。
- 概念: 实例 = 属性袋；方法存在类上，调用时绑定实例；`<X instance>` 打印格式。
- 文件: `LoxClass.java`、`LoxInstance.java`；`Expr.Get/Set`、`Stmt.Class`
- 验收: `test/class.lox`:
  ```
  class Breakfast {
    cook() { print "eggs"; }
  }
  var b = Breakfast();
  b.cook();
  b.kind = "soft";
  print b.kind;
  print b;
  print b.nothing;
  ```
  → `eggs soft <Breakfast instance>`，最后 `Undefined property 'nothing'.` 退出码 70。

### T13 · Inheritance（ch13）
- 阅读: inheritance.html
- 目标: 单继承 + super 方法调用。
- 概念: `<` 继承语法；方法查找沿父类链；super 绑定到"定义该方法时所在的类"的父类。
- 文件: `Stmt.Class` 加 superclass、`Expr.Super`、`LoxClass`/`LoxInstance` 扩展、Resolver
- 验收: `test/inherit.lox`:
  ```
  class A { method() { print "A.method"; } }
  class B < A {
    method() { print "B.method"; }
    test() { super.method(); }
  }
  B().method();
  B().test();
  class C < 3 {}
  ```
  → `B.method A.method`，最后 `Superclass must be a class.` 退出码 70。

<!-- PART2 -->

Part 2 content:

## Phase III — clox：字节码虚拟机（ch14–30）

约定: clox 全程 C11 + Makefile，`make -C clox` 产出 `clox/clox`。调试开关在 `common.h`: `DEBUG_TRACE_EXECUTION`、`DEBUG_PRINT_CODE`、`DEBUG_STRESS_GC`、`DEBUG_LOG_GC`。

### T14 · Chunks of Bytecode（ch14）
- 阅读: chunks-of-bytecode.html
- 目标: 字节码块数据结构 + 反汇编器。
- 概念: 指令 = 单字节 opcode（+操作数）；动态数组；行号与指令分离存储。
- 文件: `clox/common.h`、`memory.c/h`、`chunk.c/h`、`debug.c/h`、`main.c`、`Makefile`
- 验收: main 手工构造含 OP_RETURN 的 chunk 并反汇编:
  ```
  $ make -C clox && ./clox/clox
  == test chunk ==
  0000 0000 OP_RETURN
  ```

### T15 · A Virtual Machine（ch15）
- 阅读: a-virtual-machine.html
- 目标: 栈式 VM 主循环。
- 概念: 栈机；computed goto / switch dispatch；`#define DEBUG_TRACE_EXECUTION` 逐指令跟踪。
- 文件: `vm.c/h`
- 验收: main 构造 `OP_CONSTANT 1.2; OP_NEGATE; OP_RETURN`，开跟踪运行:
  ```
  == test chunk ==
  0000 0000 OP_CONSTANT         0 '1.2'
            [ 1.2 ]
  0002 0000 | OP_NEGATE
            [ -1.2 ]
  0003 0000 | OP_RETURN
            [ ]
  ```
  （格式细节以实际 disassembleInstruction 输出为准。）

### T16 · Scanning on Demand（ch16）
- 阅读: scanning-on-demand.html
- 目标: C 版扫描器，VM 直接读 .lox 源文件。
- 概念: 手写状态机扫描；字符串扫描按需推进（不预切 token）。
- 文件: `scanner.c/h`、`vm.c`（runFile/runPrompt 骨架）
- 验收: `./clox/clox test/tokens.lox` 能完整扫描不报错（暂无输出，错误路径: `Error at '1': Expect expression.` 之类由后续章节完善——本任务验收标准: 合法文件静默通过、非法字符报 `[line N] Error: Unexpected character.`）。

### T17 · Compiling Expressions（ch17）
- 阅读: compiling-expressions.html
- 目标: 单遍编译器: 表达式 → 字节码（Pratt 风格优先级爬升）。
- 概念: 边解析边发码；`#define DEBUG_PRINT_CODE` 反汇编编译产物；编译期常量表。
- 文件: `compiler.c/h`
- 验收: `./clox/clox --debug-print-code`（或开宏）编译 `1 * 2 + 3;`:
  ```
  == <script>
  0000    1 OP_CONSTANT         1 '2'
  ...
  ```
  关键判定: 常量 2、1 先入表，乘法在加法之前发码（优先级正确）。

### T18 · Types of Values（ch18）
- 阅读: types-of-values.html
- 目标: tagged union Value + 布尔/nil/比较指令。
- 概念: tag + as 联合体；falsy = nil/false；`==` 跨类型语义。
- 文件: `value.c/h`、`compiler.c`、`vm.c`（OP_NIL/TRUE/FALSE/NOT/EQUAL/LESS/GREATER）
- 验收: 临时 main 或跟踪输出验证 `!true; false == nil; 1 < 2;` 各产出正确字节码与栈效果（本阶段仍无 print，看跟踪）。

### T19 · Strings（ch19）
- 阅读: strings.html
- 目标: 字符串值 + `+` 拼接 + 字符串驻留。
- 概念: Obj 头 + 堆分配；驻留使 `==` 退化为指针比较；拼接结果入表。
- 文件: `object.c/h`、`memory.c`（reallocate）、`vm.c`（OP_ADD 字符串分支）
- 验收: 跟踪运行 `"a" + "bc";`，确认结果字符串 `"abc"` 入常量表且指针比较成立。

### T20 · Hash Tables（ch20）
- 阅读: hash-tables.html
- 目标: 开放寻址哈希表（线性探测 + tombstone）。
- 概念: FNV-1a 哈希；负载因子 0.75 扩容；tombstone 与删除语义。
- 文件: `table.c/h`
- 验收: 临时测试 main: 插入 3 键、删 1、再查全部、扩容后重查 → 全部断言通过（打印 `table ok`）。

### T21 · Global Variables（ch21）
- 阅读: global-variables.html
- 目标: 全局变量指令 + print 语句 —— clox 第一次有可见输出。
- 概念: 全局存哈希表（按名查找），局部存栈槽（按序号查找）——为 T22 铺垫。
- 文件: `compiler.c`（var/print 语句、OP_DEFINE_GLOBAL/GET_GLOBAL/SET_GLOBAL）、`vm.c`
- 验收:
  ```
  $ ./clox/clox test/state.lox
  1
  2
  inner
  2
  [line 7] Error
  Undefined variable 'b'.
  ```
  （错误输出格式以实际实现为准；退出码 70。）

### T22 · Local Variables（ch22）
- 阅读: local-variables.html
- 目标: 栈槽局部变量 + 作用域深度计数。
- 概念: 编译期记录 slot 下标；OP_GET_LOCAL/SET_LOCAL；块退出回退 stackTop。
- 文件: `compiler.c`（Local 数组、scopeDepth）
- 验收: `./clox/clox test/nested.lox`:
  ```
  var a = "global";
  { var a = "outer"; { var a = "inner"; print a; } print a; }
  print a;
  ```
  → `inner outer global`

### T23 · Jumping Back and Forth（ch23）
- 阅读: jumping-back-and-forth.html
- 目标: if/else、while、for 的跳转指令实现。
- 概念: OP_JUMP/JUMP_IF_FALSE（回填 patch）、OP_LOOP 反向跳转；and/or 短路。
- 文件: `compiler.c`、`vm.c`
- 验收: `./clox/clox test/control.lox` → `0 1 2 0 1 done false fallback`（与 T09 同一脚本）。

### T24 · Calls and Functions（ch24）
- 阅读: calls-and-functions.html
- 目标: 函数编译进常量、CallFrame、原生函数。
- 概念: frame = ip + 窗口化栈；OP_CALL；递归；栈溢出检测。
- 文件: `object.c/h`（ObjFunction）、`compiler.c`、`vm.c`
- 验收: `./clox/clox test/fn.lox` → `3 55 <native fn>` + arity 错误 `Expected 2 arguments but got 1.`；另测深递归报 `Stack overflow.`。

### T25 · Closures（ch25）
- 阅读: closures.html
- 目标: Upvalue 捕获（open/closed）。
- 概念: 局部变量逃逸出栈 → 堆上 ObjUpvalue；OP_CLOSURE/GET_UPVALUE/SET_UPVALUE/CLOSE_UPVALUE；循环变量每轮新绑定。
- 文件: `object.c/h`（ObjClosure/ObjUpvalue）、`compiler.c`、`vm.c`
- 验收: `./clox/clox test/closure.lox`:
  ```
  fun makeCounter() {
    var i = 0;
    fun count() { i = i + 1; print i; }
    return count;
  }
  var c = makeCounter();
  c(); c();
  ```
  → `1 2`

### T26 · Garbage Collection（ch26）
- 阅读: garbage-collection.html
- 目标: 标记-清除 GC。
- 概念: 三色标记（灰/白工作列表）；roots = 栈/frames/开放 upvalue/全局表/临时保护；`DEBUG_STRESS_GC`。
- 文件: `memory.c`（markObjects/sweep）、`object.c`（blacken）、`vm.c`
- 验收: 开 `DEBUG_STRESS_GC` + `DEBUG_LOG_GC` 跑 `test/closure.lox` 与 fib：日志显示 `-- gc begin`/`-- gc end`，程序输出不变，无崩溃（valgrind 无 invalid read 更佳）。

### T27 · Classes and Instances（ch27）
- 阅读: classes-and-instances.html
- 目标: 类声明、实例化、字段。
- 概念: 类也是 Obj；字段存实例的哈希表；OP_CLASS/GET_PROPERTY/SET_PROPERTY。
- 文件: `object.c/h`（ObjClass/ObjInstance）、`compiler.c`、`vm.c`
- 验收: `./clox/clox test/class.lox` → `eggs soft <Breakfast instance>` + `Undefined property 'nothing'.`

### T28 · Methods and Initializers（ch28）
- 阅读: methods-and-initializers.html
- 目标: 方法表、this、init。
- 概念: 方法绑定 = 闭包捕获接收者；OP_METHOD/OP_INVOKE（内联方法调用快路径）；init 特殊返回规则。
- 文件: `object.c/h`（ObjBoundMethod）、`compiler.c`、`vm.c`
- 验收: `./clox/clox test/method.lox`:
  ```
  class Person {
    init(name) { this.name = name; }
    greet() { print "hi " + this.name; }
  }
  Person("Bob").greet();
  ```
  → `hi Bob`；另测 init 中 `return 1;` → `Cannot return a value from an initializer.`

### T29 · Superclasses（ch29）
- 阅读: superclasses.html
- 目标: 继承 + super 调用。
- 概念: OP_INHERIT 复制方法表；OP_GET_SUPER 沿父类链查找；super 静态绑定到词法外围类。
- 文件: `compiler.c`、`vm.c`、`object.c`
- 验收: `./clox/clox test/inherit.lox` → `B.method A.method` + `Superclass must be a class.`

### T30 · Optimization（ch30）
- 阅读: optimization.html
- 目标: 常量折叠等优化 + 基准测量。
- 概念: 编译期折叠字面量表达式；基准驱动优化（先测量再动手）。
- 文件: `compiler.c`（折叠）、`docs/benchmark.md`（记录）
- 验收: 用 `book-tests/test/benchmark/`（或自写）脚本对比 T30 前后运行时间，结果记入 `docs/benchmark.md`；官方测试套件全量回归通过。

## 收尾

### T31 · 语法总表（附录 I、II）
- 阅读: appendix I (Lox Grammar), appendix II (Generated Syntax Tree ClassesI need to finish the TASKS.md file. I was drafting content but I haven't actually written anything to disk yet — my previous two responses were truncated while drafting in my head/output. Let me check: did I actually call the write tool? No — I never emitted a tool call; the content was all in the response text. So TASKS.md does not exist yet.

Let me verify the workspace state first, then write the file in chunks (to avoid truncation): write part 1, then append via edit with a marker, then part 3.

Plan:
1. bash ls to confirm workspace state (quick).
2. write TASKS.md part 1 (header + overview + Phase 0 + Phase I + Phase II tasks T00-T13) ending with marker `<!-- PART2 -->`.
3. edit to replace marker with Phase III (T14-T30) + 收尾 (T31-T33) + 使用说明 ending.
4. Final reply: brief summary + first runnable checkpoint per the skill.

Keep each write reasonably sized. Let me compose carefully but compactly.

Actually, to minimize risk of truncation, I'll do the ls + first write in one response (parallel calls are fine — but write depends on nothing from ls; the ls is just informational. If TASKS.md existed I'd want to know first... risk is low; workspace only has .agents. I'll still do ls first alone quickly? That costs a round trip. I'll combine: bash ls + write part1 in same block — if ls revealed an existing TASKS.md I'd have overwritten it, but it's a fresh workspace, acceptable. Actually the earlier `find .agents/skills` output showed only skill files; root likely empty. Go parallel.

Part 1 content — header, conventions, layout, overview table, Phase 0 (T00), Phase I (T01, T02), Phase II (T04–T13). That's the biggest chunk. Let me keep task entries tight: 目标/概念/文件/验收.

Then part 2: Phase III T14–T21.
Then part 3: T22–T30 + 收尾 T31–T33.

Three chunks, each moderate. Use marker comments `<!-- PART2 -->` and `<!-- PART3 -->`.

Let me write the content now. Keep it in Chinese, commands in English.Part 1 written. Now appending Phase III (T14–T21).Now the final chunk: T22–T30, 收尾 T31–T33, and the progress-tracking note.Verifying the file integrity and coverage:`TASKS.md` 已生成（491 行，33 个任务块，覆盖 ch1–30 + 附录）。结构：

- **T00–T02** 准备与阅读：工具链、项目骨架、Lox 语言规格、接入官方测试套件
- **T04–T13** jlox（Java 树遍历解释器）：Scanner → AST → Parser → 求值 → 语句/环境 → 控制流 → 函数 → Resolver → 类 → 继承
- **T14–T30** clox（C 字节码 VM）：chunk/反汇编 → VM 循环 → 扫描 → 编译 → 值/字符串/哈希表 → 全局/局部变量 → 跳转 → 调用 → 闭包 → GC → 类/方法/super → 优化
- **T31–T33** 收尾：语法总表校对、官方测试套件全量回归、自选毕业项目

每个任务块含：目标、核心概念、涉及文件、验收命令与预期输出，可直接整段粘贴给 Claude Code 执行。文件头部有全局约定（默认教练模式：Claude 讲概念、给骨架，核心代码自己写；每任务通过验收后记入 `PROGRESS.md` 并 commit；错误文案以书内实现与官方测试套件为准）。任务号与章节号对齐（ch3 并入 T02，故无 T03）。

第一个可运行检查点（T00）：

```
$ javac -d jlox/out $(find jlox/src -name '*.java')
$ java -cp jlox/out com.craftinginterpreters.lox.Lox
Usage: jlox [script]
$ echo $?
64
```

看到 `Usage: jlox [script]` 且退出码为 64，T00 即通过，可以开始 T04（Scanner）。