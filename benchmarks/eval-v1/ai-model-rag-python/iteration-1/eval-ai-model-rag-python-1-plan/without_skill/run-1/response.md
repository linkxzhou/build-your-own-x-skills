The user wants to learn and implement "RAG for Document Search" from scratch in Python, and asks me to first plan milestones and create a minimal project skeleton.

Let me first look at the current workspace to understand what's there. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-ai-model-rag-python-1` — this looks like a "build your own X" style project directory.

Let me explore the workspace first, then plan milestones, then create the skeleton.

Steps:
1. Check what's in the workspace (glob, read any existing files).
2. Create a plan (milestones) — the user explicitly asked for milestone planning.
3. Create minimal project skeleton: directory structure, README, requirements, basic modules (ingest, chunk, embed, store, retrieve, answer), maybe a simple CLI, tests.

Since this is a "from scratch" learning project, I should design a minimal RAG pipeline:
- Milestone 0: project skeleton + environment
- Milestone 1: document loading & chunking
- Milestone 2: embeddings (could use a local hash-based embedding for learning, or sentence-transformers / OpenAI)
- Milestone 3: vector store (in-memory / numpy, then maybe sqlite/faiss)
- Milestone 4: retrieval + answer generation (LLM optional, fallback extractive)
- Milestone 5: evaluation & CLI

The user asked to "规划里程碑并创建最小项目骨架" — plan milestones and create minimal skeleton. So I should:
1. Explore workspace.
2. Call `plan` with milestones.
3. Create files: README.md, requirements.txt, rag/ package with modules, tests, maybe a sample docs folder.

Let me start by checking the workspace contents. I'll use glob and bash to list files.

Per instructions: before modifying code, call `explore` once. Then `plan` for multi-step change. Then todo_write, then execute.

Let me do it. First explore the workspace.Empty workspace, Python 3.14.7. Now let me record an exploration note, then plan.

The user wants:
1. Milestone planning for learning RAG from scratch
2. Minimal project skeleton

Design decisions:
- Pure Python first (learning-oriented): use numpy for vectors, avoid heavy deps initially. For embeddings, offer pluggable backends: a deterministic hash-based "toy" embedder (works offline, good for learning) and optionally sentence-transformers/OpenAI.
- Vector store: in-memory numpy with cosine similarity; persist to disk via JSON/npz or sqlite.
- Pipeline modules: loaders (txt/md), chunker (fixed-size with overlap), embedder, store, retriever, generator (extractive fallback + optional LLM), CLI.
- Tests with pytest.
- Sample docs for demo.

Milestones:
- M0: skeleton + env (today)
- M1: ingest — load txt/md, chunk with overlap
- M2: embed — toy hash embedder, cosine similarity
- M3: store — in-memory index + persistence
- M4: retrieve + answer — top-k retrieval, extractive answer (no LLM needed)
- M5: LLM answer generation (optional API)
- M6: eval — small QA set, recall@k

Skeleton files:
```
README.md
requirements.txt
.gitignore
rag/
  __init__.py
  config.py
  loaders.py
  chunker.py
  embedder.py
  store.py
  retriever.py
  generator.py
  pipeline.py
  cli.py
tests/
  test_chunker.py
  test_embedder.py
  test_store.py
docs/
  sample1.md
  sample2.txt
data/  (index storage)
```

Minimal skeleton means I shouldn't implement everything fully — but a skeleton with working stubs and maybe the M1 pieces? The user said "创建最小项目骨架" — create minimal project skeleton. I'll create the structure with clear module stubs (docstrings describing what to implement in each milestone), a runnable CLI skeleton, README with milestones, requirements.txt, and a couple of sample docs. Maybe implement enough that `python -m rag.cli --help` works.

Actually, for a learning project, stubs with TODOs per milestone are ideal. But a completely empty stub is also fine. I'll make the skeleton minimal but coherent: config, module stubs with function signatures + docstrings + TODO markers, CLI that wires them with NotImplementedError-friendly messages, tests that are skipped/pending? Hmm — better: make the skeleton importable and CLI runnable, with each milestone's functions raising NotImplementedError with clear messages. That gives clear learning path.

Actually, let me reconsider: "最小项目骨架" (minimal project skeleton) — structure + stubs + README with milestones. I'll keep it tight.

Let me write the explore note first, then plan, then create files.

Since the workspace is empty, exploration is trivial. I'll still call explore per instructions (before modifying code). Then plan with seed_todos=true.

Let me define the plan:

Goal: Deliver a milestone roadmap + runnable minimal skeleton for a from-scratch RAG document search project in Python.

Steps:
1. s1: Write README.md with milestone roadmap (M0-M6), learning goals, architecture diagram.
2. s2: Create package skeleton rag/ with module stubs (loaders, chunker, embedder, store, retriever, generator, pipeline, cli, config).
3. s3: Add sample docs + data dir + requirements.txt + .gitignore.
4. s4: Add pytest smoke tests for skeleton (imports, CLI help).
5. s5: Verify: run python -m rag.cli --help and pytest.

Risks: Python 3.14 compatibility with some libs — keep deps minimal (numpy optional? Actually for skeleton, zero hard deps; numpy listed for M2+). Rollback: delete created files (workspace was empty).

Now the skeleton code. Let me design each module:

config.py — dataclass with paths and defaults.

loaders.py — `load_documents(paths) -> list[Document]`; Document dataclass (id, source, text, metadata). M1.

chunker.py — `chunk_document(doc, size, overlap) -> list[Chunk]`; Chunk dataclass (id, doc_id, text, start, end). M1.

embedder.py — `Embedder` protocol + `HashingEmbedder` (M2) + `SentenceTransformerEmbedder` (optional M2+). For skeleton: define interface, stub.

store.py — `VectorStore` with add/search/save/load; numpy cosine. Stub for M3.

retriever.py — `Retriever.search(query, k)` combining embedder+store. M4.

generator.py — `generate(query, chunks)` extractive fallback; LLM optional M5. Stub.

pipeline.py — `build_index(docs_dir)` and `answer(query)` wiring everything. Stub.

cli.py — argparse: `index` and `ask` subcommands; runnable now, prints "not implemented until Mx" for stubs. Actually to make it runnable and verifiable, CLI should work: `--help` works, `index`/`ask` call pipeline which raises NotImplementedError with milestone hint. Hmm, that makes `index` fail. For skeleton that's acceptable and even pedagogically clear. But maybe better: CLI catches NotImplementedError and prints friendly message. Yes.

__init__.py — version, exports.

tests: test_skeleton.py — imports work, chunker raises NotImplementedError, CLI help exits 0. Keep minimal.

requirements.txt: numpy (M2+), pytest (dev). Keep minimal — maybe comment optional extras.

.gitignore: standard python.

docs/sample: two small markdown files about RAG topics so M1 has material.

README.md: milestones table with acceptance criteria per milestone, architecture, how to run, learning path. In Chinese since user speaks Chinese. Yes, respond in Chinese and write README in Chinese.

Let me now write everything. I'll do explore + plan first (parallel? plan depends on nothing from explore since workspace is empty — but instructions say explore before plan; I can call both in same block since they're independent calls... Actually plan should reflect exploration findings. Workspace is empty, confirmed. I'll call explore and plan in one block, then todo_write, then create files.

Wait — the instruction says "Before modifying code, call `explore` once to record the files you have read (or intend to read)". Fine. And plan for multi-step change. Both can go in one message since independent.

Then create files with write calls — multiple writes can be parallel in one block.

Then verify with bash: python -m rag.cli --help && pytest.

Let me draft file contents.

README.md (Chinese):

# RAG for Document Search — 从零实现

学习型项目：用纯 Python 从零实现一个文档检索增强生成（RAG）系统。

## 架构
docs → loaders → chunker → embedder → vector store → retriever → generator → answer

## 里程碑
| 里程碑 | 目标 | 交付物 | 验收标准 |
|---|---|---|---|
| M0 骨架 | 项目结构与环境 | 本骨架 | `python -m rag.cli --help` 可运行，pytest 通过 |
| M1 摄取 | 加载与分块 | loaders.py, chunker.py | txt/md → Document → Chunk（固定长度+重叠），单测覆盖边界 |
| M2 向量化 | 嵌入 | embedder.py | HashingEmbedder 离线可用；余弦相似度正确；可选接 sentence-transformers |
| M3 索引 | 向量库 | store.py | add/search/save/load；top-k 余弦检索；持久化到 data/ |
| M4 检索问答 | 端到端 | retriever.py, generator.py, pipeline.py | `python -m rag.cli ask "问题"` 返回 top-k 证据 + 抽取式答案 |
| M5 生成升级 | LLM 接入（可选） | generator.py | 可插拔 LLM 后端，引用来源 |
| M6 评估 | 质量度量 | eval.py | 小型 QA 集，recall@k / MRR 报告 |

## 快速开始
...

## 目录结构
...

## 学习建议
每个里程碑先写测试再实现；M2 之前零第三方依赖...

Now module stubs. Keep them short with clear signatures and docstrings + TODO(Mx).

config.py:
```python
"""全局配置。"""
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class RagConfig:
    docs_dir: Path = Path("docs")
    index_dir: Path = Path("data")
    chunk_size: int = 400      # 字符数（M1 调参）
    chunk_overlap: int = 50
    top_k: int = 3
    embed_dim: int = 256       # HashingEmbedder 维度（M2）

DEFAULT_CONFIG = RagConfig()
```

loaders.py:
```python
"""M1: 文档加载 — 把 docs/ 下的 txt/md 读成 Document。"""
from dataclasses import dataclass, field
from pathlib import Path

@dataclass
class Document:
    doc_id: str
    source: Path
    text: str
    metadata: dict = field(default_factory=dict)

def load_documents(docs_dir) -> list[Document]:
    """TODO(M1): 遍历 docs_dir 下 *.txt/*.md，按相对路径生成 doc_id，读出全文。"""
    raise NotImplementedError("M1: 在 loaders.py 实现 load_documents()")
```

chunker.py:
```python
"""M1: 分块 — 固定长度 + 重叠滑窗。"""
from dataclasses import dataclass

@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    start: int  # 在原文中的字符偏移
    end: int

def chunk_document(doc, size=400, overlap=50) -> list[Chunk]:
    """TODO(M1): 滑窗切分；保证 chunk_id 稳定（如 f"{doc.doc_id}#c{i}"）。"""
    raise NotImplementedError("M1: 在 chunker.py 实现 chunk_document()")
```

embedder.py:
```python
"""M2: 嵌入 — 把文本映射成定长向量。"""
from typing import Protocol
import numpy as np  # M2 起引入

class Embedder(Protocol):
    dim: int
    def embed(self, texts: list[str]) -> np.ndarray: ...  # shape (n, dim)

class HashingEmbedder:
    """TODO(M2): 词袋 + 哈希到固定维度 + L2 归一化，离线可复现。"""
    def __init__(self, dim: int = 256): ...
    def embed(self, texts): raise NotImplementedError("M2: ...")
```

Hmm, if numpy import at top of embedder.py, then skeleton tests need numpy installed. To keep M0 zero-dependency, put `import numpy as np` inside... Actually Protocol with np.ndarray annotation requires numpy import. I could use `from __future__ import annotations` and TYPE_CHECKING import to avoid runtime dependency. That keeps M0 zero-dep. Good touch for a learning project. Let me do that.

store.py:
```python
"""M3: 向量库 — 内存索引 + 持久化。"""
class VectorStore:
    """TODO(M3): add(chunks, vectors) / search(query_vec, k) / save(dir) / load(dir)。
    检索用余弦相似度；持久化可用 np.savez + json。"""
    def add(self, chunks, vectors): raise NotImplementedError("M3: ...")
    def search(self, query_vec, k): raise NotImplementedError("M3: ...")
    def save(self, index_dir): raise NotImplementedError("M3: ...")
    @classmethod
    def load(cls, index_dir): raise NotImplementedError("M3: ...")
```

retriever.py:
```python
"""M4: 检索 — embedder + store 组合。"""
class Retriever:
    def __init__(self, embedder, store): ...
    def search(self, query: str, k: int = 3): raise NotImplementedError("M4: ...")
```

generator.py:
```python
"""M4/M5: 生成 — 先做抽取式答案，M5 可插拔 LLM。"""
def extractive_answer(query, chunks): raise NotImplementedError("M4: ...")
def llm_answer(query, chunks, backend): raise NotImplementedError("M5: ...")
```

pipeline.py:
```python
"""M4: 端到端编排。"""
def build_index(config): raise NotImplementedError("M4: loaders→chunker→embedder→store→save")
def answer(config, query): raise NotImplementedError("M4: load→retrieve→generate")
```

cli.py — fully working argparse with index/ask subcommands, catching NotImplementedError:

```python
"""命令行入口：python -m rag.cli index|ask"""
import argparse
from .config import DEFAULT_CONFIG
from . import pipeline

def main(argv=None):
    parser = argparse.ArgumentParser(prog="rag", description="RAG for Document Search (从零实现)")
    sub = parser.add_subparsers(dest="command", required=True)
    p_index = sub.add_parser("index", help="构建索引 (M4)")
    p_index.add_argument("--docs", default=str(DEFAULT_CONFIG.docs_dir))
    p_ask = sub.add_parser("ask", help="提问 (M4)")
    p_ask.add_argument("query")
    p_ask.add_argument("-k", type=int, default=DEFAULT_CONFIG.top_k)
    args = parser.parse_args(argv)
    try:
        if args.command == "index":
            pipeline.build_index(...)
        else:
            ...
    except NotImplementedError as e:
        parser.exit(1, f"尚未实现: {e}\n")
```

Hmm, keep it simple. config from args — fine, minimal.

__init__.py:
```python
"""RAG for Document Search — 从零实现的学习型项目。"""
__version__ = "0.1.0"
```

tests/test_skeleton.py:
```python
"""M0 冒烟测试：骨架可导入、CLI 可运行、未实现模块按预期抛错。"""
import subprocess, sys
import pytest
from rag import chunker, loaders

def test_modules_importable():
    import rag, rag.cli, rag.pipeline, rag.store, rag.embedder, rag.retriever, rag.generator
    ...

def test_m1_stubs_raise_not_implemented():
    with pytest.raises(NotImplementedError):
        chunker.chunk_document(...)

def test_cli_help():
    r = subprocess.run([sys.executable, "-m", "rag.cli", "--help"], capture_output=True, text=True)
    assert r.returncode == 0 and "ask" in r.stdout
```

Wait — chunk_document signature: chunk_document(doc, size, overlap). Passing a Document is fine since it raises before using it. Actually it raises immediately, so any args work. But to be clean, construct a Document.

requirements.txt:
```
# M0: 零第三方依赖即可运行骨架与测试
# M2 起需要:
numpy>=1.26
# 可选 (M2 进阶 / M5):
# sentence-transformers
# openai
# 开发:
pytest>=8
```

Hmm, pytest in requirements.txt or separate? Keep one file with comments, simple for learning.

.gitignore: __pycache__/, *.pyc, .pytest_cache/, data/, .venv/

docs samples: two short markdown files in Chinese about RAG concepts — good retrieval targets for later milestones. e.g. docs/rag_basics.md (什么是RAG, 分块, 嵌入, 向量检索), docs/pitfalls.md (常见坑: 分块太大、重叠、归一化、评估). Keep each ~15-30 lines.

data/.gitkeep — index output dir. Actually .gitignore ignores data/, but keep dir with .gitkeep. Fine.

Now milestone plan via `plan` tool:

goal: 交付 RAG 文档检索项目的里程碑路线图与可运行的最小 Python 骨架
steps:
- s1: 写 README.md（里程碑 M0–M6、架构、验收标准） touches README.md verify: 阅读检查里程碑表完整
- s2: 创建 rag/ 包骨架（config/loaders/chunker/embedder/store/retriever/generator/pipeline/cli） verify: python -c "import rag.cli"
- s3: 添加 docs 样例、requirements.txt、.gitignore、data/ 目录 verify: ls
- s4: 添加 M0 冒烟测试 verify: pytest 通过
- s5: 端到端验证 CLI 与测试 verify: python -m rag.cli --help && pytest -q

assumptions: 工作区为空目录；Python 3.14；M0 骨架零第三方依赖；里程碑按 M1 摄取→M2 嵌入→M3 索引→M4 检索问答→M5 LLM→M6 评估 递进
risks: Python 3.14 较新，后续安装 numpy/sentence-transformers 可能有兼容问题 → 骨架期零依赖规避；中文分块按字符切分在 M1 再细化
rollback: 工作区原本为空，删除新增文件即可完全回滚

seed_todos: true

Then todo_write is seeded by plan (seed_todos=true populates). Then I execute writes.

Order of my responses:
1. explore + plan (parallel, one block)
2. todo_write (mark s1 in_progress) — actually plan with seed_todos=true populates todos; I then update statuses as I go. I can do writes in parallel batches and update todo after.

Let me be efficient: after plan, do all file writes in one big parallel block (they're independent), then run verification bash, then update todos to completed, then final summary.

Actually todo_write to mark progress: I'll set all items, first in_progress, then after writes+verify mark all completed. Two todo_write calls total. Fine.

Let me write the actual content now carefully.

README.md — comprehensive but not bloated. Chinese.

Let me draft:

```markdown
# RAG for Document Search — 从零实现（Python）

学习型项目：不依赖现成 RAG 框架，用纯 Python 逐层实现「文档 → 索引 → 检索 → 回答」的完整链路。

## 架构总览

```
docs/ ──▶ loaders ──▶ chunker ──▶ embedder ──▶ VectorStore ──▶ Retriever ──▶ Generator ──▶ 答案+引用
 (M1)      (M1)        (M2)         (M3)          (M4)          (M4/M5)
```

## 里程碑路线图

| # | 里程碑 | 核心文件 | 要做的事 | 验收标准 |
|---|--------|----------|----------|----------|
| M0 | 项目骨架 | 全部 | 结构、配置、CLI、测试脚手架 | `python -m rag.cli --help` 可运行；`pytest` 通过 |
| M1 | 摄取与分块 | `loaders.py` `chunker.py` | 读 txt/md → `Document`；固定长度+重叠滑窗 → `Chunk` | 单测覆盖：空文档、短于 chunk_size、重叠正确、偏移量对得上原文 |
| M2 | 向量化 | `embedder.py` | `HashingEmbedder`（词袋哈希 + L2 归一化，离线可复现）；余弦相似度 | 相同文本相似度≈1；语义相近文本得分高于无关文本；可选：接 sentence-transformers 对比 |
| M3 | 向量索引 | `store.py` | `add / search / save / load`，top-k 余弦检索，持久化到 `data/` | 重建进程后 `load` 检索结果一致；top-k 有序 |
| M4 | 端到端检索问答 | `retriever.py` `generator.py` `pipeline.py` | `index` 与 `ask` 两条命令打通；抽取式答案 + 引用来源 | `python -m rag.cli ask "什么是RAG"` 返回带来源的证据片段 |
| M5 | 生成升级（可选） | `generator.py` | 可插拔 LLM 后端（OpenAI 兼容接口），答案基于检索证据并标注引用 | 无 API key 时自动回退抽取式答案 |
| M6 | 评估 | `eval.py` | 小型 QA 评测集；recall@k、MRR | 产出评估报告，能对比不同 chunk_size/top_k |

## 快速开始

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

python -m rag.cli --help          # M0：骨架可运行
pytest -q                          # M0：冒烟测试
```

## 目录结构

```
rag/
  config.py      # 全局配置（chunk 大小、top_k 等）
  loaders.py     # M1 文档加载
  chunker.py     # M1 分块
  embedder.py    # M2 嵌入
  store.py       # M3 向量库
  retriever.py   # M4 检索
  generator.py   # M4/M5 答案生成
  pipeline.py    # M4 端到端编排
  cli.py         # 命令行入口
tests/           # 每个里程碑先补测试再实现
docs/            # 示例文档（也是检索语料）
data/            # 索引持久化目录（gitignore）
```

## 学习约定

- 每个里程碑：先读模块里的 `TODO(Mx)` 注释 → 写测试 → 实现 → 全量 pytest 通过后进入下一关。
- M2 之前保持零第三方依赖；`numpy` 从 M2 引入。
- 所有函数带类型标注；`Chunk.start/end` 必须能对回原文，方便调试与引用定位。
```

Wait — architecture diagram line: loaders (M1), chunker (M1), embedder (M2), VectorStore (M3), Retriever (M4), Generator (M4/M5). Let me fix the annotation line:

```
docs/ ─▶ loaders ─▶ chunker ─▶ embedder ─▶ VectorStore ─▶ Retriever ─▶ Generator ─▶ 答案+引用
        (M1)       (M1)       (M2)        (M3)          (M4)        (M4/M5)
```

Alignment roughly. Fine.

Note: nested code block inside markdown — I'm writing via write tool so no issue.

cli.py full:

```python
"""命令行入口。

用法:
    python -m rag.cli index [--docs docs]
    python -m rag.cli ask "什么是 RAG?" [-k 3]
"""
from __future__ import annotations

import argparse
from pathlib import Path

from . import pipeline
from .config import DEFAULT_CONFIG


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="rag", description="RAG for Document Search — 从零实现",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    p_index = sub.add_parser("index", help="构建向量索引 (M4 打通)")
    p_index.add_argument("--docs", type=Path, default=DEFAULT_CONFIG.docs_dir)

    p_ask = sub.add_parser("ask", help="检索并回答 (M4 打通)")
    p_ask.add_argument("query")
    p_ask.add_argument("-k", type=int, default=DEFAULT_CONFIG.top_k)

    args = parser.parse_args(argv)

    try:
        if args.command == "index":
            pipeline.build_index(docs_dir=args.docs)
        else:
            pipeline.answer(query=args.query, top_k=args.k)
    except NotImplementedError as exc:
        parser.exit(2, f"[未实现] {exc}\n按 README 里程碑顺序实现对应模块后再试。\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

pipeline.py:

```python
"""M4: 端到端编排 — 把 M1–M3 的零件串成两条命令。"""
from __future__ import annotations

from pathlib import Path

from .config import DEFAULT_CONFIG


def build_index(docs_dir: Path = DEFAULT_CONFIG.docs_dir) -> None:
    """TODO(M4): loaders.load_documents → chunker.chunk_document
    → embedder.HashingEmbedder.embed → store.VectorStore.add/save。"""
    raise NotImplementedError("M4: 在 pipeline.py 实现 build_index()")


def answer(query: str, top_k: int = DEFAULT_CONFIG.top_k) -> None:
    """TODO(M4): store.VectorStore.load → retriever.Retriever.search
    → generator.extractive_answer，打印答案与引用来源。"""
    raise NotImplementedError("M4: 在 pipeline.py 实现 answer()")
```

Hmm, pipeline imports config DEFAULT_CONFIG as default arg — fine.

embedder.py with TYPE_CHECKING:

```python
"""M2: 嵌入 — 把文本映射成定长向量，相似文本 → 相似向量。"""
from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

if TYPE_CHECKING:  # M2 安装 numpy 前保持零依赖
    import numpy as np


class Embedder(Protocol):
    dim: int

    def embed(self, texts: list[str]) -> "np.ndarray":
        """返回 shape (len(texts), dim) 的 L2 归一化矩阵。"""
        ...


class HashingEmbedder:
    """TODO(M2): 词袋 + 哈希到固定维度 + L2 归一化。

    实现提示:
      - 对每个 token 计算 hash(token) % dim，正负号可用第二个 hash 决定;
      - 累加词频后做 L2 归一化，使余弦相似度 = 点积;
      - 纯 Python + numpy 即可，离线可复现，适合理解检索原理。
    """

    def __init__(self, dim: int = 256) -> None:
        self.dim = dim

    def embed(self, texts: list[str]) -> "np.ndarray":
        raise NotImplementedError("M2: 在 embedder.py 实现 HashingEmbedder.embed()")
```

store.py:

```python
"""M3: 向量库 — 内存索引 + 磁盘持久化。"""
from __future__ import annotations

from typing import TYPE_CHECKING

from .chunker import Chunk

if TYPE_CHECKING:
    import numpy as np


class VectorStore:
    """TODO(M3): 向量 + 元数据的内存索引，np.savez + json 持久化。

    需要实现:
      add(chunks, vectors)      追加向量与对应 Chunk
      search(query_vec, k)      余弦相似度 top-k，返回 [(Chunk, score)]
      save(index_dir) / load(index_dir)
    """

    def add(self, chunks: list[Chunk], vectors: "np.ndarray") -> None:
        raise NotImplementedError("M3: 在 store.py 实现 VectorStore.add()")

    def search(self, query_vec: "np.ndarray", k: int = 3) -> list[tuple[Chunk, float]]:
        raise NotImplementedError("M3: 在 store.py 实现 VectorStore.search()")

    def save(self, index_dir) -> None:
        raise NotImplementedError("M3: 在 store.py 实现 VectorStore.save()")

    @classmethod
    def load(cls, index_dir) -> "VectorStore":
        raise NotImplementedError("M3: 在 store.py 实现 VectorStore.load()")
```

retriever.py:

```python
"""M4: 检索 — 组合 Embedder 与 VectorStore。"""
from __future__ import annotations

from .embedder import Embedder
from .store import VectorStore


class Retriever:
    def __init__(self, embedder: Embedder, store: VectorStore) -> None:
        self.embedder = embedder
        self.store = store

    def search(self, query: str, k: int = 3) -> list:
        """TODO(M4): query → 向量 → store.search，返回 [(Chunk, score)]。"""
        raise NotImplementedError("M4: 在 retriever.py 实现 Retriever.search()")
```

generator.py:

```python
"""M4/M5: 答案生成 — 先抽取式，后可插拔 LLM。"""
from __future__ import annotations


def extractive_answer(query: str, hits: list) -> str:
    """TODO(M4): 不依赖 LLM，从 top-k 片段中抽取最相关句子作为答案。"""
    raise NotImplementedError("M4: 在 generator.py 实现 extractive_answer()")


def llm_answer(query: str, hits: list, backend) -> str:
    """TODO(M5): 把检索片段作为上下文交给 LLM，要求答案标注引用来源。"""
    raise NotImplementedError("M5: 在 generator.py 实现 llm_answer()")
```

loaders.py:

```python
"""M1: 文档加载 — 把 docs/ 下的 txt/md 读成 Document。"""
from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class Document:
    doc_id: str
    source: Path
    text: str
    metadata: dict = field(default_factory=dict)


def load_documents(docs_dir: Path) -> list[Document]:
    """TODO(M1): 递归遍历 docs_dir 下的 *.txt / *.md。

    要求:
      - doc_id 用相对路径字符串，保证稳定可复现;
      - 按 UTF-8 读取，跳过无法解码的文件并记录警告;
      - metadata 至少包含 source 与文件大小。
    """
    raise NotImplementedError("M1: 在 loaders.py 实现 load_documents()")
```

chunker.py:

```python
"""M1: 分块 — 固定长度 + 重叠的滑动窗口。"""
from __future__ import annotations

from dataclasses import dataclass

from .loaders import Document


@dataclass
class Chunk:
    chunk_id: str
    doc_id: str
    text: str
    start: int  # 在原文中的字符偏移（含）
    end: int    # 不含


def chunk_document(doc: Document, size: int = 400, overlap: int = 50) -> list[Chunk]:
    """TODO(M1): 滑窗切分。

    要求:
      - chunk_id 形如 f"{doc.doc_id}#c{i}"，顺序稳定;
      - 0 < overlap < size，相邻块重叠 overlap 个字符;
      - 短于 size 的文档返回单个 Chunk;
      - start/end 必须满足 doc.text[start:end] == chunk.text。
    """
    raise NotImplementedError("M1: 在 chunker.py 实现 chunk_document()")
```

config.py:

```python
"""全局配置 — 所有可调参数集中在这里，方便 M6 做对比实验。"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass
class RagConfig:
    docs_dir: Path = Path("docs")
    index_dir: Path = Path("data")
    chunk_size: int = 400      # 字符
    chunk_overlap: int = 50
    top_k: int = 3
    embed_dim: int = 256       # HashingEmbedder 维度


DEFAULT_CONFIG = RagConfig()
```

__init__.py:

```python
"""RAG for Document Search — 从零实现的学习型项目。"""

__version__ = "0.1.0"
```

tests/test_skeleton.py:

```python
"""M0 冒烟测试 — 骨架可导入、CLI 可运行、各里程碑桩函数按预期抛错。"""
from __future__ import annotations

import subprocess
import sys

import pytest

from rag import chunker, loaders, pipeline


def test_all_modules_importable():
    import rag
    from rag import cli, config, embedder, generator, retriever, store  # noqa: F401

    assert rag.__version__


def test_m1_stub_raises():
    doc = loaders.Document(doc_id="d", source="d.md", text="hello")
    with pytest.raises(NotImplementedError):
        chunker.chunk_document(doc)


def test_m4_stub_raises():
    with pytest.raises(NotImplementedError):
        pipeline.answer(query="test")


def test_cli_help_runs():
    result = subprocess.run(
        [sys.executable, "-m", "rag.cli", "--help"],
        capture_output=True, text=True,
    )
    assert result.returncode == 0
    assert "ask" in result.stdout and "index" in result.stdout
```

Wait: loaders.Document source field is Path typed but passing str is fine at runtime.

test_cli_help_runs runs subprocess with cwd = workspace root — pytest run from root, subprocess inherits cwd, so `python -m rag.cli` finds rag package. Good.

requirements.txt:

```
# M0–M1: 零第三方依赖（标准库即可运行骨架与测试）
# M2 起需要:
numpy>=1.26
# 可选（M2 进阶 / M5）:
# sentence-transformers>=3
# openai>=1.40
# 开发 / 测试:
pytest>=8
```

.gitignore:

```
__pycache__/
*.py[cod]
.pytest_cache/
.venv/
data/
.DS_Store
```

docs/rag_basics.md — sample corpus:

```markdown
# RAG 基础概念

## 什么是 RAG
RAG（Retrieval-Augmented Generation，检索增强生成）先从文档库中检索与问题相关的片段，再把片段作为上下文交给生成模型，让答案基于真实资料而不是模型记忆。

## 为什么需要 RAG
大模型的训练数据有截止时间，也记不住私有文档。RAG 把"知识"放在可随时更新的索引里，模型只负责阅读和总结，能显著减少幻觉。

## 典型流程
1. 摄取：加载 txt/markdown/pdf 等文档。
2. 分块：把长文档切成固定长度、带重叠的小片段。
3. 嵌入：用向量模型把每个片段映射成一个定长向量。
4. 索引：把向量与元数据存进向量库。
5. 检索：把用户问题也变成向量，取余弦相似度最高的 top-k 片段。
6. 生成：把片段和问题一起交给模型，生成带引用的答案。
```

docs/chunking_tips.md:

```markdown
# 分块与检索的常见坑

## 分块太大
块太大会稀释主题，检索命中后噪声多、答案不准。常见起点是 300–500 字符，再按效果调整。

## 分块太小
块太小会丢上下文，"它""该方案"这类指代悬空。解决办法是保留 10%–20% 的重叠，或在块首带上文档标题。

## 忘记归一化
用余弦相似度时，向量必须做 L2 归一化，否则点积会偏向长文本。

## 没有评估
至少准备 10–20 条"问题 → 应命中文档"的评测集，用 recall@k 衡量检索质量，否则调参全靠感觉。
```

data/.gitkeep — empty file. write tool with empty content? content "" should work.

Now — one concern: `from .chunker import Chunk` in store.py, and chunker imports from loaders — all fine, no cycles.

cli.py: `parser.exit(2, ...)` — exits with SystemExit(2) after printing message. In test we only test --help, fine.

Also `sub.add_subparsers(dest="command", required=True)` — Python 3.7+ ok.

Python 3.14: `list[str] | None` fine with __future__ annotations anyway.

Now the plan tool call. Then writes. Then verify: `python3 -m rag.cli --help && python3 -m pytest -q` — pytest may not be installed. Check: run `python3 -m pytest -q` and if missing, pip install pytest? Installing into user env — it's a local reversible action, fine. Or use venv? Creating .venv is good practice but adds time; the README suggests venv. For verification, I can just try pytest; if not installed, `python3 -m pip install -q pytest` (user site). Hmm, on macOS with Python 3.14, pip install may need --user or --break-system-packages if homebrew. Let me just try and see. Alternatively verify with unittest? The skeleton tests use pytest. I could write tests compatible with both? Simpler: try pytest, install if needed.

Actually, to keep zero-friction, I could write the smoke test using plain `unittest` so it runs with stdlib only. That aligns with "M0 零依赖". But pytest is nicer for the learning path and README says pytest. Compromise: keep pytest tests, and in verification install pytest if missing. Let me check if pytest exists first in the verify step: `python3 -c "import pytest"`.

Let me also double check `python3 -m rag.cli --help` works from workspace root — yes since rag/ is in cwd.

One more thing: the user asked "请先帮我规划里程碑并创建最小项目骨架" — so final response should present the milestone plan concisely + what was created + how to start. Keep it tight.

Also should I create a goal? "Create a goal only when explicitly requested" — user didn't ask. Skip.

Let me execute: explore + plan in one block now.Now execute: write all files in parallel. All writes are independent. Let me write README.md, rag/* files, docs, requirements, .gitignore, data/.gitkeep, tests.

I'll do them all in one block.All files written. Now verify the skeleton runs.Everything verified:
- `python3 -m rag.cli --help` works, shows index/ask subcommands
- `ask` on stub exits with code 2 and friendly "not implemented" message pointing to milestone
- pytest: 4 passed

Let me update the todo list to completed, then give the final summary. Also verify the file tree quickly? The writes all succeeded and tests pass (which import all modules). Good enough.

Update todos: all 5 completed.里程碑规划与骨架已就绪，验证通过（`--help` 正常、pytest 4 passed）。

## 里程碑路线图（详见 README.md）

| # | 里程碑 | 核心文件 | 验收标准 |
|---|--------|----------|----------|
| M0 | 项目骨架 | 全部 | CLI 可运行、pytest 通过 ✅ 已完成 |
| M1 | 摄取与分块 | `loaders.py` `chunker.py` | txt/md → Document → 带重叠滑窗的 Chunk，偏移可对回原文 |
| M2 | 向量化 | `embedder.py` | HashingEmbedder（词袋哈希 + L2 归一化，离线可复现） |
| M3 | 向量索引 | `store.py` | add/search/save/load，top-k 余弦检索，持久化到 `data/` |
| M4 | 端到端问答 | `retriever.py` `generator.py` `pipeline.py` | `ask "什么是RAG"` 返回带引用的抽取式答案 |
| M5 | LLM 生成（可选） | `generator.py` | 可插拔 LLM 后端，无 key 时回退抽取式 |
| M6 | 评估 | `eval.py` | QA 评测集 + recall@k / MRR，对比 chunk_size / top_k |

## 骨架结构

```
rag/            config / loaders / chunker / embedder / store / retriever / generator / pipeline / cli
tests/          M0 冒烟测试（可导入、CLI、桩函数抛错）
docs/           两篇示例文档，同时是后续检索语料
data/           索引持久化目录（已 gitignore）
```

设计要点：每个模块留了 `TODO(Mx)` 桩函数 + 实现提示，未实现时 CLI 会提示该做哪个里程碑；M0–M1 零第三方依赖，`numpy` 从 M2 才引入。

下一步从 M1 开始：实现 `rag/loaders.py` 的 `load_documents()` 和 `rag/chunker.py` 的 `chunk_document()`，按惯例先在 `tests/` 补测试再写实现。