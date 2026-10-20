The user wants to learn and implement "RAG for Document Search" from scratch in Python. They want me to first plan milestones and create a minimal project skeleton.

This matches the build-your-own-x skill — "从零实现" (build from scratch), and RAG is a category (build an LLM / RAG). I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it, and also look for the skills directory to find the RAG/LLM track skill.RAG 映射到 `ai-model` 轨道，并且有一个针对每个教程的技能 `ai-model-rag-python`。根据工作流程，先读取轨道技能，然后读取教程技能。两个技能已加载。现在正在读取剩余的轨道技能以及两个参考文件（教程列表 + 里程碑映射）。I've read the track skill, the per-tutorial skill, and the tutorial map. There's also a `references/concepts.md` mentioned. Let me read that too since it's referenced. Also, I should check the workspace state — is it empty? Let me check what's in the workspace root.

Then per the workflow:
1. Establish context: empty directory? Check.
2. Plan milestones — the track skill gives the RAG milestone table: chunking → embeddings → retrieval → generation, with checkpoints.
3. Create minimal project skeleton.

The track skill says: "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care." The user already specified Python and RAG for Document Search. So I can proceed with defaults and note assumptions.

Also important coaching rules:
- Never dump the whole project. Give full code only for the current milestone.
- Never install anything myself — print pip commands for the learner.
- Record milestones in PROGRESS.md.
- Milestone 1 = skeleton: files, entry point, README, runnable hello-world command.

So my task now: plan milestones (the milestone list) and create the minimal project skeleton (milestone 1). The skeleton should be minimal: package layout, README, PROGRESS.md, a CLI entry point that runs, maybe a tests/ dir with a trivial test. Keep it runnable without third-party deps (stdlib only) so the learner can run it immediately, and print the pip install command for later milestones.

Let me read concepts.md and check the workspace.工作区是空的（只有 `.agents/` 和 `AGENTS.md`），Python 3.14.7 可用 —— 所以这是一个从零开始的开始：里程碑 1 是骨架。技能文件已全部读取。在编写任何代码之前，先记录探索笔记。技能和上下文已加载。现在我来编写行动计划。计划已确定。正在编写骨架文件（PROGRESS.md 紧随验证之后，以便它能记录实际输出）。骨架文件已写入。正在运行验证：CLI 帮助、stub 行为以及测试套件。所有检查均已通过。正在记录 `PROGRESS.md` 中的里程碑 1，并附上实际输出。里程碑 1/7 完成，骨架已验证：`--help` 正常、4 个测试全绿、占位子命令按预期退出码 2。

**里程碑路线**（完整表格在 `README.md`，进度在 `PROGRESS.md`）：

1. ✅ 项目骨架 — CLI + 测试闭环
2. 核心数据模型 — `Document` / `Chunk`
3. 输入层 — 加载 + 重叠分块
4. 核心引擎 — 嵌入（哈希基线起步）+ 余弦 top-k 索引
5. 端到端 — `ask` 命令，检索 + 抽取式回答 + 引用
6. 评估 — recall@k，向量检索 vs 关键词基线
7. 扩展 — BM25 混合、重排、真实嵌入/LLM API

M1–M3 零依赖纯标准库；M4 起需要 `pip install numpy`（到时你自己执行）。

**下一步：里程碑 2，核心数据模型。** 概念：整条 RAG 流水线只传递两种对象——`Document`（从磁盘读入的原始文件）和 `Chunk`（被嵌入、被索引的最小检索单元）。关键不变量：chunk 必须能追溯回它的来源文档（`doc_id` + `ordinal`），这样 M5 的回答才能给出引用；`chunk_id` 稳定且可读，方便调试和去重。

接口骨架（`ragsearch/models.py`，核心由你来写）：

```python
from dataclasses import dataclass

@dataclass
class Document:
    doc_id: str
    text: str
    source: str   # 来源文件路径

@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    ordinal: int  # 文档内序号，从 0 开始
    text: str

# 不变量（在 __post_init__ 里校验）：
# 1. text 非空（strip 后）
# 2. ordinal >= 0
# 3. chunk_id 推荐格式 f"{doc_id}#{ordinal}"
```

写完后建 `tests/test_models.py`：合法构造、空文本抛 `ValueError`、负 `ordinal` 抛 `ValueError`。检查命令：`python3 -m unittest tests.test_models -v`，全绿即进入 M3。卡住了说一声，我一次给一个提示。