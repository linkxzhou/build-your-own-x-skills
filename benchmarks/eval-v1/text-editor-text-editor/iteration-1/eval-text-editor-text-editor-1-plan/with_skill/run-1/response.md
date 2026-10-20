The user wants to learn and implement "Build Your Own Text Editor" (the famous kilo tutorial by antirez, "Build Your Own Text Editor" by snaptoken) from scratch in C. They want me to:
1. Plan milestones
2. Create a minimal project skeleton

This matches the `build-your-own-x` skill. I must read the SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it.Topic mapped: `text-editor`. Reading the track skill (mandatory).Let me also check the tutorials reference file to pick the exact upstream tutorial link, and check if there's a per-tutorial skill for kilo (text-editor-kilo or similar). Let me look at the skills directory and the tutorials.md.C 语言 + 「Build Your Own Text Editor」对应 snaptoken 的 kilo 教程，存在对应的 per-tutorial skill（`text-editor-text-editor`）。按规则先读 track skill，再读 per-tutorial skill。Skill 已读完。按流程先记录探索，再检查工作区现状和工具链。工作区为空，工具链齐全（cc/gcc/clang/make，macOS）。先确认上游教程的章节结构，保证里程碑映射准确。教程结构确认：7 章（Setup → Raw mode → Raw I/O → Viewer → Editor → Search → Syntax highlighting），与 track skill 的 7 个里程碑一一对应。现在制定计划并落地骨架。里程碑 0 完成。骨架已建好并通过验证：`make` 无警告，`./kilo` 退出码 0。

**当前进度：里程碑 0 / 7**（上游教程：[Build Your Own Text Editor](https://viewsourcecode.org/snaptoken/kilo/)，snaptoken，基于 antirez 的 kilo）

**里程碑规划**（已写入 `README.md`，每步都有可运行检查点）：

| # | 里程碑 | 检查点 |
|---|---|---|
| 0 | 项目骨架 | `make` 无警告，`./kilo` 正常退出 ✅ |
| 1 | Raw mode | 按键打印编码；Ctrl-Q 退出且终端恢复正常 |
| 2 | 屏幕绘制 | 空行显示波浪线；调整窗口后重绘 |
| 3 | 光标移动与滚动 | 打开 1000 行文件能滚到末尾 |
| 4 | 文件 I/O | 编辑 + Ctrl-S 后 `diff` 与期望文件一致 |
| 5 | 编辑功能 | 脚本化按键序列产出期望文件内容 |
| 6 | 搜索 | Ctrl-F 跳转匹配，Esc 恢复原位置 |
| 7 | 进阶 | C 关键字着色；undo 撤销 10 次编辑 |

**创建的文件**：`kilo.c`（带里程碑 1 的 TODO 注释）、`Makefile`（`-Wall -Wextra -std=c99 -pedantic`）、`README.md`、`PROGRESS.md`、`.gitignore`。

**里程碑 1：Raw mode** —— 概念：终端默认处于「规范模式」，内核按行缓冲输入并回显字符，程序要做成编辑器就必须逐键读取、自己控制回显。`termios` API 让你读取并修改终端属性：关掉 `ECHO` 和 `ICANON` 即进入 raw mode，退出前必须恢复原属性，否则终端会坏掉。

`kilo.c` 里的 TODO 已列出步骤：`tcgetattr()` 读属性 → 清 `ECHO | ICANON` → `tcsetattr()` 写回 → 循环读按键，`0x11`（Ctrl-Q）退出 → 恢复属性。在真实终端（Terminal.app / iTerm2）里运行，IDE 输出面板没有 TTY。

**你的检查命令**：

```sh
make && ./kilo
```

预期：敲键盘字符无回显；Ctrl-Q 退出后 `echo` 恢复正常。卡住时把报错或现象贴给我，一次给一条提示。