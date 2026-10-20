The user wants me to convert the "Write Yourself a Git" (wyag) tutorial from https://wyag.thb.lt/ into a Claude Code learning task list. Let me first fetch the content of that page to understand what it covers, then create a structured learning task list.

Let me fetch the page first.The workspace is empty. The user wants me to convert the wyag tutorial into a Claude Code learning task list. Let me fetch more of the page content to understand the full structure, then create a structured learning task list (probably as a markdown file, or maybe as a series of tasks).

The user's request: "请基于 https://wyag.thb.lt/ 转换成 Claude Code 学习任务清单。" — Convert the wyag tutorial into a Claude Code learning task list.

This likely means: create a task list (like TASKS.md or a series of prompts) that a user can feed to Claude Code to learn by building wyag step by step. The workspace is empty, so I should create a task list file.

Let me fetch more of the page to get the details of each section. The page was truncated at 30057 chars. Let me fetch more content to understand the details. Actually, I know wyag well — it's a well-known tutorial. But let me get more details to be accurate.

Let me fetch the rest of the page.页面内容已获取（教程结构完整）。现在把 wyag 教程转换为一份可直接在 Claude Code 中逐条执行的学习任务清单，写入工作区。已生成 `WYAG_TASKS.md`，把 wyag 教程的 10 个章节转换成了 10 个可逐条粘贴给 Claude Code 执行的任务（任务 0–9）。

结构设计：

- **每个任务三要素**：教程章节锚点链接（先读原理）→ 可直接粘贴的提示词 → 可复制的验收命令。验收全部采用「wyag 与真实 git 交叉验证」——真实 git 必须能读 wyag 创建的对象/仓库，反之亦然，这是最硬的正确性标准。
- **依赖顺序**：骨架 → init/repo_find → 对象读写 → log/tree/checkout → refs/tag → index/status → add/commit → 端到端验收，与教程章节顺序一致，文末附依赖图。
- **防抄机制**：提示词里明确要求 Claude Code 解释设计原理（如 Merkle DAG、为什么 tree 条目要排序），并附了教程原文中的常见坑清单（tree 的 20 字节二进制 sha、index 的 8 字节对齐、kvlm 的 message 空行等）。
- **测试隔离**：所有验证在 `/tmp/wyag-test` 下进行，避免污染当前工作区。

使用方式：打开 `WYAG_TASKS.md`，按顺序把每个任务的「提示词」块整段发给 Claude Code，跑通验收命令后进入下一个。