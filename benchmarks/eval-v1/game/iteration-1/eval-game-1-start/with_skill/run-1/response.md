The user wants to build a Snake game in Python to learn game development. This matches the build-your-own-x skill — specifically a game. I should read the skill's SKILL.md first before doing anything else.The file was truncated. Let me read the rest of it to see the category map and find the game slug.贪吃蛇属于 `game` 类别。现在我来读取 track skill —— 这是必须的。The file was truncated. Let me read the rest.现在我来查看一下 Python/pygame 贪吃蛇游戏的教程列表。Let me see the rest of the tutorials file to check for a snake-specific Python tutorial.Python + pygame 是默认的路径，并且有一个针对每个教程的技能。我来读取它以获取具体的细节。Let me read the rest of this skill and the tutorial-map.md.我已经掌握了完整的指导路径。在开始之前，让我先检查一下环境和 workspace。环境检查：Python 3.14.7，尚未安装 pygame，工作区为空。在移交安装命令之前，让我先确认哪个 pygame 包支持 Python 3.14，并记录探索内容。搜索未返回结果。我来尝试使用不同的查询。搜索没有返回结果。我来直接查询 PyPI。pygame-ce 支持 Python 3.14（已在 PyPI 上确认），因此技术栈已确定。我来制定计划并搭建项目框架。现在我来搭建项目框架——包含带有 TODO 的骨架，由你来填充核心代码。预期结果：`game.py` 在导入 pygame 时失败，因为尚未安装。脚手架本身没有问题——我来确认一下纯 Python 部分是否可以正常导入。Scaffold verified. Update todo s1 to completed, s2 in_progress. Then write the coaching turn per the skill's output format:

- Where we are: milestone 1/6
- The concept: game loop, fixed timestep, update/render separation
- What to write next: the 3 TODOs (skeleton already given)
- How to check: command + expected output
- Stuck: one hint at a time

Also give the pip install command (learner runs it themselves). Keep it tight.**进度：Milestone 1 / 6 — 窗口 + 游戏循环**

**概念（30 秒版）**：所有游戏的核心都是同一个循环——每秒重复 60 次「处理输入 → 更新世界状态 → 画一帧」。帧率用 `clock.tick(FPS)` 压住，它返回距上一帧的毫秒数 `dt`，后续所有移动都基于 `dt` 而不是「每帧走一格」，这样换帧率游戏速度不变。update 和 render 分开写，是为了以后能单独测逻辑、单独改画面。

**已搭好的骨架**（在 `snake/game.py`）：

- `Game.__init__`：建窗口、时钟 — 已完成
- `handle_events` / `update` / `render`：**3 个 TODO 留给你**，注释里写了每一步用什么 API
- `run`：循环骨架 — 已完成

**你的任务**：

1. 安装依赖（我按规矩不替你跑安装命令）：
   ```bash
   python3 -m pip install pygame-ce
   ```
   用 pygame-ce 是因为经典 pygame 对 Python 3.14 的轮子更新慢，社区版已官方支持 3.14（PyPI 已确认）。
2. 填完 `snake/game.py` 里的 3 个 TODO（每个 2–4 行，注释里有提示）。
3. 跑检查：
   ```bash
   python3 -m snake.game
   ```
   **通过标准**：窗口打开，左上角 FPS 稳定在 60 附近；按 ESC 或点 X 窗口关闭、终端无任何报错。

卡住了就把报错或你写的代码贴过来，一次给一个提示。跑通后告诉我，我们进 Milestone 2（网格蛇 + 方向键）。