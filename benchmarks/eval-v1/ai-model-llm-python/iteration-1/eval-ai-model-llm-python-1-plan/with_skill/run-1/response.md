The user wants to learn and implement an LLM from scratch in Python. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also find the LLM track skill.The track is `ai-model`, and there's a matching per-tutorial skill `ai-model-llm-python`. Reading the track skill first, as required.Truncated again. Let me read the rest of the track skill, and also the per-tutorial skill `ai-model-llm-python/SKILL.md` since the user explicitly wants Python + LLM.Let me read the rest of the per-tutorial skill and the tutorial-map.md and concepts.md references.Now let me read the concepts.md and the minimal example README to understand the scaffold guidance.技能已加载：track `ai-model` + per-tutorial `ai-model-llm-python`（上游教程：rasbt/LLMs-from-scratch）。先检查工作区和运行环境。环境确认：Python 3.14.7，无 torch，工作区为空。按流程先记录探索结论，并查证 torch 对 Python 3.14 的支持情况（这决定环境准备指令怎么写）。搜索无结果，直接查 PyPI 的 torch wheel 列表。torch 2.14.1 有 cp314 wheel（含 macOS arm64），Python 3.14 可直接装。信息齐了，制定计划并落地骨架。Both checkpoints pass:
- `python3 -m minillm info` → exit 0, prints env report
- `python3 -m unittest discover -s tests -v` → 3 tests OK

PROGRESS.md already records M0 as PASS with these commands. The record matches reality. Let me verify the PROGRESS.md content is accurate — it says "torch 未安装（M2 前安装即可）" which matches the actual output. Good.

Now s4 complete. s5: hand over with torch install command and M1 kickoff brief.

Per the skill: never install anything myself; print the exact command. Also credit upstream tutorial with exact link (done in README).

Final message should include:
- Where we are: M0 done, milestone table
- What was created
- The torch install command for the learner to run
- M1 kickoff: concept brief + what to write + how to check

Keep it tight. The milestone table is in README, so I don't need to repeat the whole table — but the user asked "先帮我规划里程碑" so the milestone plan should be visible in my response. I'll give a compact version of the milestone list and point to README for the full checkpoint table. Actually the README has the full table; my response should summarize the roadmap briefly and give the M1 kickoff.

Per output style: lead with the answer, no filler, no summary-stamp closings, no conditional next-step menus. End with M1 kickoff as the concrete next action.M0 完成：骨架已建好并通过验证。项目跟随 [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch)（build-your-own-x · AI Model · Python 轨道）。

## 里程碑路线图（M0–M7）

| # | 里程碑 | 通过标准 |
|---|---|---|
| M0 | 项目骨架 | CLI 可运行、测试全绿 ✅ |
| M1 | 数据 + 字符级分词器 | encode→decode 完全还原，报告词表大小 |
| M2 | bigram 基线模型 | 记录基线 val loss（后续都要打败它） |
| M3 | 自注意力 + Transformer block | 形状测试通过；单 batch 过拟合到接近 0 |
| M4 | 训练循环 + checkpoint | val loss 优于基线；重载 checkpoint loss 一致 |
| M5 | 采样（temperature / top-k） | 生成文本可读、贴近语料风格 |
| M6 | 评估（perplexity） | 指标表：各里程碑 vs 基线 |
| M7 | 进阶（KV cache / BPE） | 可测量的加速或质量提升 |

完整 checkpoint 表在 `README.md`，进度记录在 `PROGRESS.md`。

## 已创建

```
minillm/            tokenizer.py  data.py  model.py  train.py  sample.py  __main__.py
tests/test_skeleton.py
README.md  PROGRESS.md  requirements.txt  .gitignore
```

验证结果：`python3 -m minillm info` 退出码 0；`python3 -m unittest discover -s tests -v` 3 个测试全部通过。骨架零第三方依赖即可运行。

## 你来跑：安装 torch（M2 前需要，M1 用标准库即可）

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

已确认 PyPI 上有 torch 2.14.1 的 cp314 wheel，你的 Python 3.14.7 可直接安装。

## M1 开工：字符级分词器

**概念**：模型只认整数。分词器把文本映射成 token id 序列——字符级方案就是建一张「字符 → id」表，encode 查表、decode 反查。词表大小 = 语料中不同字符的个数。

**你写什么**（骨架已留 TODO）：
1. `minillm/tokenizer.py` — `CharTokenizer.from_text`（排序建表保证可复现）、`encode`、`decode`
2. `minillm/data.py` — `load_corpus`、`train_val_split`（9:1 按顺序切，不打乱）

**怎么验证**：写完后跑 `python3 -m unittest discover -s tests -v`，我会先给你一个 round-trip 测试：`decode(encode(text)) == text` 对任意语料内文本成立，且词表大小符合预期。卡住了说一声，一次给一个提示。