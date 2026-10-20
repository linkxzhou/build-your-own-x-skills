The user wants me to convert the rag-from-scratch tutorial from langchain-ai into a Claude Code executable learning task list. This matches the build-your-own-x skill — "想通过做项目学底层原理" / hands-on project learning. Let me first read the skill file as instructed.

Let me start by reading the SKILL.md.Let me read the rest of the SKILL.md file.该请求对应到 `ai-model` 赛道（RAG 已明确列出）。让我阅读一下赛道技能，并检查是否有针对 rag-from-scratch 的特定教程技能。有一个针对每个教程的技能 `ai-model-rag-python`。让我检查一下它是否与 rag-from-scratch 相匹配，并阅读它。这是一个精确的匹配 —— 该技能的源 URL 正是 rag-from-scratch。让我阅读一下它的参考文件。该技能的源 URL 与请求完全匹配。现在让我获取实际的 rag-from-scratch README 以获取准确的 notebook 列表，并检查工作区状态。GitHub 页面抓取到的内容大多是导航栏。我来获取原始的 README 以获取准确的 notebook 列表。README 很简短——内容在 notebooks 中。我来通过 GitHub API 列出仓库结构。该仓库包含 5 个合并的 notebook（视频 1–18）。我来从每个 notebook 中提取 markdown 标题，以构建准确的任务列表。我已经掌握了完整的教程结构。让我检查一下工作区的 `AGENTS.md` 以了解项目规范，然后整理我的探索笔记。我已经准备好了所需的一切：完整的教程结构（5 个 notebook 中的 18 个部分）、技术栈以及匹配的技能。让我记录一下探索结果并制定计划。现在进行交叉检查：TASKS.md 中必须出现所有 18 个部分名称，且每个任务都必须包含验证命令。所有检查均已通过：20 个任务（任务 0 + 任务 1–19）中的 18 个部分名称均完全匹配，每个任务都有一个验证块，安装命令仅标记为学习者运行，上游链接已署名，并且 PROGRESS.md 跟踪了所有 7 个里程碑组。已生成两个文件：

- **`TASKS.md`** — 把上游 5 个 notebook 的 18 个 Part 转成 20 个任务（任务 0 环境骨架 + 任务 1–19），按 6 个里程碑分组。每个任务含：目标、对应 notebook 参考位置、要写的 `src/` 模块、pytest 验证命令、通过标准。任务 2/8/11/14/15/18/19 还要求把基线指标记入 `PROGRESS.md`，形成可对比的学习曲线。
- **`PROGRESS.md`** — 里程碑总览表、基线指标记录表、完成日志模板。

关键设计决策：

1. **实现形态**：notebook 只作参考资料，代码落在 `src/` 模块 + `tests/`，每个任务以 `pytest` 收尾——这比 notebook 形式更适合 Claude Code 逐任务执行和回归验证。
2. **后端可切换**：任务 0 的 `src/config.py` 支持 OpenAI（与上游一致）或 Ollama（llama3 + nomic-embed-text，免费本地跑），后续所有任务不感知后端。
3. **教学约定**（写入 TASKS.md 使用规则，遵循 build-your-own-x 技能）：一次一个任务、概念讲解→骨架→学习者写核心→跑验证的循环、安装命令由学习者执行、完整代码仅在学习者尝试后按当前任务给出。
4. **语料固定**为上游默认的 Lilian Weng agent 博客，保证跨任务的检索指标可比。

开始学习时发这句即可：「继续 RAG 任务清单：读 TASKS.md 和 PROGRESS.md，找到第一个未完成任务，按教学循环开始。」