The user wants to learn by building an interpreter from scratch in Java, following "Crafting Interpreters" (craftinginterpreters.com). They want:
1. Milestone planning
2. A minimal project skeleton

This matches the `build-your-own-x` skill. I must read the SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also find the relevant track skill. The topic is "interpreter/compiler/programming language" — likely slug `interpreter` or similar. Let me read the rest of SKILL.md and list the skills directory.主题映射到 `programming-language` 轨道。让我阅读该轨道技能，并检查是否有针对 Crafting Interpreters 的特定教程技能。有一个针对 Crafting Interpreters 的特定教程技能。让我把它和轨道技能的其余部分一起阅读。我来阅读一下 crafting-interpreters 技能的其余部分及其 tutorial-map 参考。我来阅读剩余的参考内容：concepts.md 和最小化脚手架指南。技能已读完。按流程先探查工作区与 Java 环境，再记录探索结论、制定计划。`/usr/bin/java` 是 macOS 的占位符，实际没有 JDK。检查一下系统里是否有其他 JDK 安装：环境确认：Homebrew 已装 openjdk@21 和 openjdk@27（`/usr/bin/java` 只是 macOS 占位符）。工作区是空的（只有 AGENTS.md）。记录探索结论并制定计划：Loxy.java 引用了尚不存在的 `Interpreter`（M3 才实现）。按最小骨架原则，先移除该字段，留 TODO：M0 检查点验证——三个命令：REPL 冒烟、脚本模式、错误路径：`java_home` 找不到 Homebrew 的 JDK（未注册到系统位置）。增强 run.sh 的 JDK 探测逻辑，直接探测 Homebrew 路径：检查点 1、2 通过。检查点 3 暴露了 run.sh 只转发 `$1` 的问题，导致 Java 的 usage 分支不可达。改为转发全部参数：三个检查点全部通过。更新 PROGRESS.md 记录 M0：核对发现两处需要修正：README 里程碑表的章节映射有重叠（Ch 9-10 同时出现在 M4 和 M5），且 PROGRESS.md 的日期是猜的。先确认真实日期：里程碑规划与骨架已就绪，M0 检查点全部实测通过。

## 已交付

```
jlox/
├── README.md        # 环境说明 + 里程碑表（M0-M6 + 拉伸目标）
├── PROGRESS.md      # 每个里程碑的验收记录（已记 3 条 M0 检查）
├── run.sh           # JDK 探测（含 Homebrew openjdk@21）+ 编译 + 运行
├── src/.../loxy/Loxy.java   # 入口：脚本/REPL 双模式 + 报错行号框架
└── tests/smoke.lox
```

验证结果：`printf 'var a = 1;\n' | ./run.sh` 进入 REPL；`./run.sh tests/smoke.lox` 正常读入；`./run.sh a b` 输出 `Usage: jlox [script]` 退出码 64。过程中修了两个真实 bug：`java_home` 找不到 Homebrew JDK（改为探测 `/opt/homebrew/opt/openjdk*`），以及 run.sh 只转发 `$1` 导致 usage 分支不可达。

## 里程碑路线（对应原书 Part I，jlox）

| # | 里程碑 | 章节 | 检查点 |
|---|--------|------|--------|
| M0 | 骨架 ✅ | Ch 3 前置 | REPL 可启动 |
| M1 | 词法扫描 Scanner | Ch 4 | token 列表正确；非法字符报错带行号 |
| M2 | Parser → AST | Ch 5-6 | `1 + 2 * 3` 打印 `(+ 1 (* 2 3))` |
| M3 | 表达式求值 | Ch 7 | REPL 算出 `7`；`"a" + 1` 报类型错误 |
| M4 | 语句、变量、作用域 | Ch 8, 11 | 嵌套块 shadowing 正确 |
| M5 | 控制流与函数 | Ch 9-10 | `fib(20)` = 6765；闭包计数器可用 |
| M6 | 测试与加固 | Ch 12-14 | `tests/` 全绿 |
| 拉伸 | 字节码 VM（clox，C） | Part II | `fib(25)` 快于树遍历 |

教程原文：[Crafting Interpreters](http://www.craftinginterpreters.com/)（Bob Nystrom，免费在线）。

## M1 开工：词法扫描

**概念**：Scanner 把字符流切成 token——每个 token 带类型（`VAR`、`IDENTIFIER`、`NUMBER`…）、词素原文、字面值和行号。核心是一个 `scanTokens()` 循环：吃掉空白和注释，按首字符分派（单字符 token 直接产出，`!`/`=` 这类要看下一个字符决定是 `!=` 还是 `!`，即 maximal munch），数字和字符串走各自的子循环。所有错误都通过 `Loxy.error(line, msg)` 上报，扫描器自身只报错不中断。

**你来做**（书 Ch 4 走到 "Lexical Errors" 一节即可）：
1. `TokenType.java` — 先只列 M1 需要的：单字符、一到两字符、字面量、关键字
2. `Token.java` — 四个字段的不可变类
3. `Scanner.java` — `scanTokens()` 主循环 + `identifier()` / `number()` / `string()` 子例程
4. 在 `Loxy.run()` 里接上 `Scanner`，临时打印 token 列表

**检查**：

```bash
printf 'var a = 1;\n' | ./run.sh
# 期望：VAR var null 1 / IDENTIFIER a null 1 / NUMBER 1 1.0 1 / SEMICOLON ; null 1 / EOF  null 1
printf 'var a = "unterminated;\n' | ./run.sh
# 期望：[line 1] Error: Unterminated string.
```

写完贴出你的 token 输出或卡住的代码，我们从真实输出继续。