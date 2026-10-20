The user has a text editor project (build-your-own-x-text-editor-2) and reports that after exiting the editor, the terminal doesn't echo anymore and needs `reset`. This is a classic raw-mode terminal restoration bug — the editor likely enables raw mode but fails to disable it on exit (missing atexit handler, panic path, or not restoring on all exit paths).

Let me explore the workspace first to see what files exist.工作区目前是空的，我看不到你的编辑器源码。先说结论：这个症状（退出后终端不回显、换行不显示、必须 `reset`）几乎总是**raw mode 没有在所有退出路径上恢复**造成的——`tcsetattr` 恢复正常模式的代码只在正常退出时执行了，某条路径（报错提前 return、panic、Ctrl-C 信号杀掉进程）绕过了它。

常见漏掉的路径：

1. **错误提前退出**：`enableRawMode()` 成功后，后面任何 `return` / `exit(1)` / `die()` 都必须先恢复终端。
2. **panic / 崩溃**：Rust 里 panic 默认 unwind，但 Drop guard 之外的手动 `std::process::exit` 会跳过 Drop；C 里 `abort()` 直接跳过 `atexit`。
3. **信号**：SIGINT/SIGTERM 默认行为是直接终止进程，恢复代码根本没机会跑。
4. **Ctrl-D / EOF 读到 0 字节**的分支。

标准修法是把恢复挂在“必然执行”的位置：

- C：`atexit(disableRawMode)` + 捕获 SIGINT/SIGTERM 后 `exit()`（让 atexit 兜底）
- Rust：Drop guard（RAII）+ `panic::set_hook` 里恢复，或用 `crossterm` 时确保 `disable_raw_mode()` 在所有分支前执行
- Go：`defer term.Restore()` 放在 main 最顶部

把你的编辑器源码放进这个工作区（或告诉我路径），我帮你定位具体是哪条退出路径漏了恢复。