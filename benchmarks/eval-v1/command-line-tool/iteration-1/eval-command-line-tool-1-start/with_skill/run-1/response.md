The user wants to build a cowsay-like CLI tool in Rust. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The skill file is truncated. Let me read the rest of it, and also check the category map for the relevant slug. The user wants to write a cowsay-like CLI tool in Rust. Cowsay is a simple CLI tool — it's not exactly in the build-your-own-x catalog categories probably, but it might fall under "misc" or maybe there's a relevant track. Let me read the rest of the SKILL.md file first.cowsay 映射到 `command-line-tool` track。按 skill 要求，先读 track skill。Track skill 已读。按流程先确认环境：查 per-tutorial skill、看工作区现状、确认 Rust 工具链是否就绪。工具链就绪（cargo 1.95.0）。有一个 Rust 专属的 per-tutorial skill，快速看一下它是否覆盖 cowsay 场景。The per-tutorial Rust skill points to https://rust-cli.github.io/book/index.html (Command line apps in Rust). It says to read references/tutorial-map.md for the milestone map before planning detailed work. Let me read that.Track skill 和 Rust per-tutorial skill 都已读，工具链就绪。记录探索结论并制定里程碑计划，同时搭好项目脚手架。脚手架已建好（`cowsay/`，真实 cowsay 未安装，后面用 golden 文件做对照）。我把里程碑 1 的骨架写进 `main.rs`，核心逻辑留给你。**里程碑 1/6 — Hello CLI**（上游教程：[Command line apps in Rust](https://rust-cli.github.io/book/index.html)）

**概念**：CLI 的第一块基石是入口点与退出码。`main` 正常返回即退出码 0；`std::env::args()` 给出命令行参数，第一项是二进制自身路径，所以要 `skip(1)`。版本号用 `env!("CARGO_PKG_VERSION")` 在编译期从 Cargo.toml 读入，避免手写两处。

**你的任务**：打开 `cowsay/src/main.rs`，把 TODO 补上——检测 `--version`（顺手支持 `-V`），命中就打印 `cowsay 0.1.0` 后返回。约 5 行代码。

**检查命令**（通过后我们进里程碑 2）：

```bash
cd cowsay && cargo run -- --version; echo $?
```

期望输出两行：`cowsay 0.1.0` 和 `0`。

卡住了说一声，我一次给一个提示。