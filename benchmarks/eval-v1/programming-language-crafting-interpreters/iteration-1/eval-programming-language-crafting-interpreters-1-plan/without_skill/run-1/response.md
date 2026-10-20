The user wants to learn and implement "Crafting Interpreters" from scratch in Java, and asks me to plan milestones and create a minimal project skeleton. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-programming-language-crafting-interpreters-1`.

Let me first explore the current workspace to see what's there, then plan milestones and create a minimal project skeleton.

Steps:
1. Check workspace contents
2. Plan milestones (following the book structure: Part I Scanner, Part II tree-walking interpreter jlox, Part III bytecode VM clox — but user says Java, so focus on jlox; maybe mention clox is C but they could do it in Java too)
3. Create minimal project skeleton: Gradle or Maven? Minimal — maybe just a simple directory structure with a build.gradle or pom.xml, or even plain javac. Let me keep it minimal: Gradle is standard. Or Maven. Let me check what's in the workspace first.

Let me start by exploring the workspace.The workspace is empty. Java is not installed (or not in PATH). Let me check for common JDK locations on macOS.工作区是空的，机器上还没有 JDK（`/usr/bin/java` 只是 macOS 的安装占位）。我先记录探索结果并制定计划，然后创建骨架。冒烟测试全部符合预期（占位 Scanner 对每个字符报错属设计内，M1 实现后消失）。收尾两处：`.jdk/` 加入 .gitignore，`make test` 在 `test/` 为空时也能跑。里程碑规划与项目骨架已就绪，编译和冒烟测试全部通过。

## 里程碑路线图（详见 README.md）

| 里程碑 | 章节 | 产出 |
|---|---|---|
| M0 ✅ | — | 骨架 + REPL 入口 |
| M1 | 4. Scanning | `Scanner` 词法扫描器 |
| M2 | 5-6 | AST（`Expr`/`Stmt`）+ 递归下降 `Parser` |
| M3 | 7 | 表达式求值 `Interpreter` |
| M4 | 8 | 语句 + `Environment` 变量作用域 |
| M5 | 9 | if/while/for 控制流 |
| M6 | 10-13 | 函数、闭包、解析器、类、继承 → 完整 Lox |
| M7（可选） | 14-28 | clox 字节码 VM（原书用 C，可继续用 Java 练手） |

## 骨架内容

```
Makefile / .gitignore / README.md
src/com/craftinginterpreters/lox/
  Lox.java          # 入口：REPL + runFile + 错误码 64/65/70（已实现，对齐书第 4 章）
  TokenType.java    # 全量 token 类型枚举
  Token.java        # 已实现
  Scanner.java      # 占位：TODO 标注了 4.5-4.7 节的实现点
  Parser.java       # 占位（第 5-6 章）
  Interpreter.java  # 占位（第 7-10 章）
```

零依赖纯 `javac`，命令：`make build` / `make repl` / `make run F=x.lox` / `make test`。

## 环境说明

机器上原本没有 JDK，我下载了 Temurin 17 到项目的 `.jdk/`（已加入 .gitignore）并完成了验证：

```sh
export JAVA_HOME="$PWD/.jdk/jdk-17.0.20.1+1/Contents/Home"
export PATH="$JAVA_HOME/bin:$PATH"
```

冒烟测试结果：用法错误退出码 64、词法错误退出码 65、空脚本退出码 0、REPL 正常交互。占位 Scanner 目前对每个字符报 `Unexpected character` 属预期行为——这就是你的第一个任务：实现 M1，让 `var x = 1;` 扫出正确的 token 流。