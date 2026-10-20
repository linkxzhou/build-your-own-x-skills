The user wants to learn visual recognition by building license plate recognition (车牌识别) in Python. This matches the build-your-own-x skill — specifically "build your own X" for learning by rebuilding real software. The skill description says: use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems skills... Chinese triggers include 项目式学习, 从零实现 etc.

The user says "我想用 Python 做车牌识别来学习视觉识别，带我开始" — "I want to do license plate recognition in Python to learn visual recognition, guide me to start."

This is a hands-on learning project request. I should read the skill first: .agents/skills/build-your-own-x/SKILL.md before doing anything else.

Let me read the skill.The skill file was truncated. Let me read the rest of it, and also check the skills directory for a matching track. License plate recognition is a computer vision / ML topic. Let me see what track skills exist.该路由将车牌识别映射到 `visual-recognition-system` 轨道。正在读取该轨道技能（根据路由器，这是必需的）：The track skill is truncated. Let me read the rest of it, and also the tutorials.md reference file.轨道技能已加载。让我检查一下车牌教程的各教程技能，并查看工作区状态：工作区是空的——一个全新的开始。学习者选择了车牌识别 + Python，这与 `visual-recognition-system-python` 每个教程的技能相匹配。现在开始阅读它：Let me also read the concepts.md reference and the minimal example README to understand the scaffold guidance.技能已加载：我将指导你完成一个 7 个里程碑的车牌识别构建，使用上游教程 [Developing a License Plate Recognition System with Machine Learning in Python](https://medium.com/devcenter/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)。首先，让我检查一下这台机器上有什么可用资源（Python 版本、CV 库、中文字体），以便骨架能符合实际情况：环境检查：Python 3.14，`numpy` + `Pillow` 已就绪；`opencv` / `scikit-learn` / `matplotlib` 缺失（你需要自行安装 —— 我会在下文提供具体命令）。让我验证一下用于合成中文车牌的 CJK 字体，并记录探索结果：PingFang 是一个受保护的系统字体，但 Arial Unicode.ttf（包含 CJK 字符）是可读的。正在验证 PIL 是否可以渲染汉字：字体和渲染已确认。现在开始制定计划：现在正在构建脚手架（s1–s3）：现在是合成车牌生成器（基础设施 — 学习者只需阅读，无需编写）：现在进行里程碑 1 的检查点以及学习者的骨架：刚才的草稿有误——现在重新编写实际的检查点：现在验证基础设施是否正常工作：生成数据集，并确认检查点处于正确的红色状态：生成器中的一个 bug：`random.Random` 缺少 `.normal` 方法（那是 numpy 的方法）。最小化修复方案 — 从种子随机数生成器中派生出一个 numpy 生成器：数据集已构建（360个场景），检查点已连接并处于红色状态。对真实数据进行快速合理性检查：Everything checks out: plate average RGB (65, 103, 185) is blue-ish as expected, labels match filenames, boxes are within the 640×360 scene.

Update todos: s1, s2, s3 completed; s4 in_progress (learner's turn). s5 pending.

Then write the coaching reply per the track skill's output format:
- Where we are: milestone 1/7
- The concept: short
- What to write next: TODO list (the 3 TODOs in dataset.py)
- How to check it: command + expected output — must end with this

Keep it tight. Also mention the one bug I fixed (transparency) and the install command for later milestones (already in README, brief mention).**Where we are:** milestone 1/7 — dataset + loading. Project scaffold is in `plate-rec/`, dataset is generated, checkpoint is wired and currently red.

**The concept.** Every recognition system starts with data plumbing: images on disk → numeric arrays a model can consume. Three decisions matter here: grayscale (color adds little for plate text, and cuts memory 3×), float32 normalized to [0, 1] (stable for later math), and a fixed shape (360, 640) so samples stack into one tensor `X (N, 360, 640)`. Labels come from the filename (`琼DB4332_0000.png` → `琼DB4332`) plus a `labels.csv` with ground-truth boxes we'll use in milestone 3. The data is synthetic — PIL-rendered blue plates with seeded noise, blur and brightness jitter — so every image ships with perfect ground truth and runs are reproducible. One bug fixed along the way: `random.Random` has no `.normal` (that's numpy); the generator now seeds a `np.random.default_rng` from it.

**What to write next** — implement the three TODOs in `plate-rec/src/dataset.py` (the only file you touch; `src/generator.py` is infrastructure):

1. `load_image(path)` — `Image.open(...).convert("L")` → `np.asarray(..., dtype=np.float32) / 255.0`
2. `load_split(name)` — read `data/<name>/labels.csv`, call `load_image` per row, `np.stack` the images, return `(X, y)` with labels from the CSV
3. `class_counts(y)` — count each of the 7 characters per label; total over a split must equal `7 × N`

**How to check it:**

    cd plate-rec
    python3 scripts/check_dataset.py

Expected when done:

    MILESTONE 1 CHECK — dataset + loading
      [PASS] load_image runs
      [PASS] returns numpy array
      [PASS] grayscale (2 dims)
      [PASS] shape (360, 640)
      [PASS] dtype float32
      [PASS] range [0, 1]
      [PASS] load_split('train') runs
      [PASS] 240 samples
      ...
    MILESTONE 1 CHECK PASSED — dataset + loading done.

Right now it exits with `NotImplementedError` — that's the red state. From milestone 2 you'll need OpenCV/scikit-learn/matplotlib; install them yourself when we get there: `python3 -m pip install opencv-python scikit-learn matplotlib`.