The user wants me to convert the LLMs-from-scratch tutorial (https://github.com/rasbt/LLMs-from-scratch) into a Claude Code executable learning task list.

First, I should check the skill "build-your-own-x" since this matches — the user wants to learn by building an LLM from scratch, and the skill description mentions "手写...解释器" and "build your own x" triggers, "想通过做项目学底层原理". The LLMs-from-scratch repo is literally about building an LLM (ChatGPT-like) from scratch. The skill says to read SKILL.md before doing anything else.

Let me read the skill first, then explore the repo structure to build the task list.

Plan:
1. Read the skill SKILL.md.
2. Fetch the GitHub repo README to understand the chapter structure.
3. Convert into a Claude Code executable task list — meaning a series of prompts/tasks that can be fed to Claude Code, each with clear deliverables, verification steps, references to the original notebook/chapter.

The output should probably be a markdown file (e.g., a TASKS.md or a series of task files) in the workspace that the user can use with Claude Code. "Claude Code 可执行的学习任务清单" — a learning task list that Claude Code can execute. So I should produce a structured document where each task is a self-contained prompt with: goal, inputs (which chapter/notebook), deliverables (files to create), acceptance criteria (tests), and verification commands.

Let me start by reading the skill.The GitHub page fetch was mostly navigation chrome. I need the actual README content. Let me fetch the raw README instead. Also, the skill says to read the track skill — the category here is "LLM" (build-your-own-x has an "llm" category? Let me check the catalog). The skill mentions `skills/<slug>/SKILL.md`. Let me list the skills directory to find the right track skill (probably `llm` or `neural-network`).

Let me do parallel: glob skills directory, and fetch raw README from GitHub.The README display got cut off at the table of contents. Let me download it locally and check for an LLM track skill in the build-your-own-x skill set.There's an `ai-model-llm-python` track skill. Reading it plus the README's chapter table.The read tool can't read /tmp. Let me move the README into the workspace or just cat it via bash. Let me copy it into workspace temp dir and read. Also read the tutorial-map.md reference of the skill.我已经获取了完整的章节结构。现在让我检查一下工作区，并在编写任务文件之前记录下探索计划。现在我来验证完整的输出：文件列表、每个任务文件中必需的章节标题，以及 README 索引与实际文件之间的一致性。所有检查均已通过：9 个任务文件，每个文件包含全部 5 个必需部分，且 README 索引与文件列表 1:1 匹配。正在清理临时文件并关闭待办事项列表。完成。产出在 `llm-from-scratch/`，共 11 个文件：

```
llm-from-scratch/
├── README.md     # 任务总览、使用方法、学习路径图
├── CLAUDE.md     # 项目级教练守则（Claude Code 启动时自动读取）
└── tasks/        # 9 个任务文件（00-08），每个可直接作为 prompt 喂给 Claude Code
```

**任务清单**（对应上游章节，每个任务含：背景认知 → 交付物 → 验证命令 → 执行指令 → 卡住时对照的上游 notebook 路径）：

| # | 任务 | 验收标准 |
|---|------|---------|
| 00 | 环境搭建 + PyTorch 热身 | softmax/autograd 测试通过 |
| 01 | BPE 分词器 + 滑窗 DataLoader | `y == x 右移一位`、shape 断言 |
| 02 | 注意力三连：简化 → 因果 → 多头 | 因果性测试（改 t 后 token，≤t 输出不变） |
| 03 | GPTModel 124M | 参数量 ≈163M（含 head）、前向 shape 正确 |
| 04 | 训练循环 + 解码 + The Verdict 预训练 | loss 从 ~10.9 降到 <2，生成可读文本 |
| 05 | 加载 OpenAI GPT-2 官方权重 | "Every effort moves you" 续写流畅 |
| 06 | 垃圾短信分类微调 | val 准确率 ≥95% |
| 07 | 指令微调 + Ollama 评估 | Llama3 评分 ≥50 |
| 08 | 进阶（可选）：训练循环增强 + LoRA | LoRA 可训练参数 <5M |

**使用方式**：`cd llm-from-scratch && claude`，然后输入「请阅读 tasks/00-setup.md 并带我完成这个任务」。任务间有依赖（02 依赖 01 的 DataLoader，03 依赖 02 的注意力），按编号顺序推进。`CLAUDE.md` 已写明教学守则：你写核心代码、Claude Code 做脚手架和验收，卡住时对照上游 notebook 定位差异。

设计上做了两个取舍：所有测试用缩小配置（`emb_dim=256, n_layers=2`）保证 CPU 秒级运行；每个任务的验证命令都给出量化预期（loss 区间、准确率、参数量），避免「跑通了但不知道对不对」。