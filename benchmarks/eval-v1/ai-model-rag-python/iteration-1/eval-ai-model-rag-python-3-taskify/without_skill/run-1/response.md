The user wants me to convert the rag-from-scratch tutorial from LangChain into a Claude Code executable learning task list. Let me first understand the current workspace and then fetch the tutorial content.

Let me start by exploring the workspace and fetching the GitHub repo info.GitHub 页面抓取到的主要是导航栏，改用 raw README。README 很短，内容在各 notebook 里。用 GitHub API 拿完整文件树。Now I have a full picture of the tutorial structure. Let me also check the 15_to_18 notebook's remaining cells to be complete.

The tutorial structure:
- Part 1: Overview (basic RAG pipeline)
- Part 2: Indexing (documents, token counting, embeddings, cosine similarity, loaders, splitters, vectorstores)
- Part 3: Retrieval
- Part 4: Generation
- Part 5: Multi Query
- Part 6: RAG-Fusion
- Part 7: Decomposition (answer recursively / individually)
- Part 8: Step Back
- Part 9: HyDE
- Part 10: Logical and Semantic routing
- Part 11: Query structuring for metadata filters
- Part 12: Multi-representation Indexing
- Part 13: RAPTOR
- Part 14: ColBERT
- Part 15: Re-ranking
- Part 16: Impact of long context (probably)
- Part 17/18: probably "Self-RAG" and "Adaptive RAG"? Let me check the 15_to_18 remaining cells.

Let me look at the remaining cells of 15_to_18.The 15_to_18 notebook is a bit sparse — it covers Part 15 (Re-ranking), Part 16 (CRAG - Corrective RAG), Part 17 (Self-RAG, likely missing from this notebook — actually the repo has separate notebooks for self-rag and adaptive RAG? No, the repo only has 5 notebooks. Let me check: the notebook titles say "16 - Retrieval (CRAG)" and "18 - Impact of long context". Part 17 (Self-RAG) might be in the video but the notebook may be minimal. Let me check the actual content of cells 16-18.

Actually, historically the repo had individual notebooks (rag_from_scratch_1.ipynb ... rag_from_scratch_18.ipynb) but they consolidated them. The current notebooks cover:
- 1_to_4: Overview, Indexing, Retrieval, Generation
- 5_to_9: Multi Query, RAG-Fusion, Decomposition, Step Back, HyDE
- 10_and_11: Routing (logical + semantic), Query structuring for metadata filters
- 12_to_14: Multi-representation Indexing, RAPTOR, ColBERT
- 15_to_18: Re-ranking, CRAG, Self-RAG(?), Impact of long context

Let me quickly check cells 16-18 content to see what parts 16/17/18 contain.教程全貌已确认：18 个 Part,分布在 5 个 notebook 中。再确认教程用的语料 URL 和关键依赖，然后写任务清单。教程结构已完全确认。记录探索结论并制定计划。现在编写 TASKS.md。校验通过:Part 1–18 全覆盖,19 个任务(Task 0–18)+ 5 条总验收 = 24 个复选框,数目吻合。修一处自引用问题:总验收里的 grep 计数会把总验收自身的复选框也算进去,改为精确口径。已生成 `TASKS.md`,把 rag-from-scratch 的 18 个 Part 转换为 19 个可执行任务(Task 0–18),教程原 notebook 已克隆到 `.ref_repo/` 供执行时对照。

**清单结构**：

| 阶段 | 任务 | 对应教程 |
|---|---|---|
| 0 | Task 0 环境搭建 | 依赖安装、API key、项目骨架 |
| 1 | Task 1–4 | Part 1–4:最小 RAG 流水线、索引原理、检索、生成 |
| 2 | Task 5–9 | Part 5–9:Multi Query、RAG-Fusion、Decomposition、Step Back、HyDE |
| 3 | Task 10–11 | Part 10–11:逻辑/语义路由、metadata 查询结构化 |
| 4 | Task 12–15 | Part 12–15:Multi-representation、RAPTOR、ColBERT、Re-rank |
| 5 | Task 16–18 | Part 16–18:CRAG、Self-RAG、长上下文对比实验 |

**为 Claude Code 可执行性做的设计**：
- 每个任务固定四段：目标 / 参考(精确到 `.ref_repo` 的 notebook cell 编号)/ 实现要求(指定输出文件 `src/partNN_*.py`)/ 验收标准(可运行的命令或断言，如 `python -m src.part01_basic_rag "What is Task Decomposition?"`)。
- 执行协议写在文件头部：顺序执行、验收全过才勾选 `- [x]`、禁止跳过或放宽验收。
- 教程中纯链接的 Part(13/14/16/17/18)补齐了最小实现要求(如 RAPTOR 简化为 KMeans 聚类+一层摘要、CRAG/Self-RAG 允许用 LCEL 循环模拟 LangGraph),并给无 Cohere key 的场景留了 LLM 重排降级路径。
- 末尾有总验收区(模块覆盖检查、pytest、复选框计数、`reports/summary.md`)和进度表。

在 Claude Code 里直接说「按 TASKS.md 从 Task 0 开始执行」即可开始。