The user wants to learn visual recognition by building license plate recognition in Python. This matches the build-your-own-x skill — "想通过做项目学底层原理" / hands-on project learning. The skill description says: use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills... Chinese triggers include 项目式学习、想通过做项目学底层原理.

The user says "我想用 Python 做车牌识别来学习视觉识别，带我开始" — "I want to do license plate recognition in Python to learn visual recognition, guide me to start."

This matches the skill. I should read the SKILL.md first before doing anything else.The file was truncated. Let me read the rest of the SKILL.md to see the category map and find the right track skill.车牌识别映射到 `visual-recognition-system` 轨道。现在开始读取它。Truncated again. Let me read the rest.The track skill says:
- Python only upstream: licence-plate recognition (scikit-image + ML) — that matches the user's request exactly.
- There may be a per-tutorial skill: `skills/visual-recognition-system-*`. Let me check for it.

The workflow:
1. Agree on scope: language (Python — given), target, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide: the license plate recognition tutorial (scikit-image + ML).
3. Work milestone by milestone.

Let me check if there's a per-tutorial skill for the license plate one.有一个针对每个教程的技能 `visual-recognition-system-python` —— 对应 Python 车牌识别文章。正在读取它。技能链已加载。现在让我检查工作区状态并获取上游教程，以落实里程碑 1。工作区是全新的（仅包含 `.agents` 和 `AGENTS.md`），Python 3.14.7 可用。Medium 文章被 Cloudflare 拦截了 (403)。让我检查一下是否有可访问的镜像，以及它使用了什么数据集，以便我能具体确定范围。技能链已加载（track: `visual-recognition-system` → per-tutorial: `visual-recognition-system-python`）。工作区是空的，Python 3.14.7 可用。Medium 原文有 Cloudflare 付费墙，但 track skill 自带完整的里程碑表，足够带练。先记录探索结论并制定计划：现在我来搭建项目脚手架（s1, s2）——包含骨架、fixture 生成器和检查点。学习者需要编写的核心代码放在 `plate_rec/dataset.py` 中，并带有 3 个 TODO。现在我来验证一下脚手架：检查依赖项是否存在，并对检查点进行空运行。The scaffold works as intended:
- Data generated: 288 char images in 36 classes, 40 plates.
- Checkpoint fails with NotImplementedError (expected — the learner's TODOs are unfilled).

Let me verify the generated images look sane (one char image, one plate image) — quick sanity check of pixel stats.Char image: ink spans rows 4-15, cols 5-13 — centered-ish, 12px tall, 9px wide. Reasonable for a 20x20 glyph. Good enough.

Now update todos (s1, s2 completed; s3 in_progress — it's the learner's task), then write the coaching turn per the skill's output format:
- Where we are: milestone 1/7
- The concept: short
- What to write next: TODOs, not the answer
- How to check: command + expected output
- Stuck: one hint at a time

Also mention: pip install command for them to run (I can't install). PIL/numpy already present in this environment, but scikit-image/scikit-learn not needed until M2/M4. I should still give them the venv + pip command per skill rule 5 ("Print the exact command... let the learner run it").

Keep it tight.项目已搭好，按里程碑推进。跟随的上游教程：[Developing a License Plate Recognition System with Machine Learning in Python](https://medium.com/devcenter/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)（Medium 有付费墙，不影响——里程碑表和检查点都在本地）。

**当前位置：里程碑 1/7 — 数据集 + 加载**

**概念**：识别系统的输入是统一规格的图像张量。三个基本功：灰度化（去掉颜色通道，字符识别只需要形状）、缩放（分类器要求固定尺寸，这里 20x20）、归一化（像素压到 [0,1]，数值稳定）。再加一个 stratified split——按类别分别切分 train/test，保证每个类在两边都有样本，否则稀有类可能整个掉进测试集。

**已就绪**（`plate-rec/`）：
- `scripts/make_synth.py` — 已生成数据：36 类字符图 288 张（`data/chars/<标签>/`，目录名即标签），40 张整牌图（后面里程碑用）
- `scripts/check_m1.py` — 检查点，9 项断言
- `plate_rec/dataset.py` — **你的战场**，3 个 TODO

**环境**（自己跑；本机已有 PIL/numpy，scikit-learn 到里程碑 4 才用得上）：

```bash
cd plate-rec
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

**接下来写什么**（`plate_rec/dataset.py`，每个 TODO 3-6 行）：
1. `load_plate` — 按注释里的 4 步：open → convert("L") → resize((20,20)) → `np.asarray(...)/255.0`
2. `load_dataset` — 遍历 `sorted(data_dir.iterdir())`，子目录名做标签，收集 (X, y)
3. `train_test_split` — 按标签分组，`random.Random(seed)` 组内洗牌，每类前 `ceil(n*ratio)` 个进测试集

**检查**：

```bash
python3 scripts/check_m1.py
```

末行打印 `MILESTONE 1 PASSED` 即过（当前会报 `NotImplementedError: TODO 2`，正常）。过了就记进 `PROGRESS.md`，进里程碑 2（阈值/边缘/形态学）。

卡住就说一声，一次给一个提示。