The user wants to build a Snake game in Python to learn game development, and wants me to guide them through it. This is a teaching/interactive task. Let me check the workspace first to see what's there, then set up a plan.

The user says "带我开始" — guide me to start. So I should be interactive: explain the approach, maybe start with a minimal version and let them learn step by step. But I'm an agent — I should probably scaffold the first version and explain the concepts, then iterate with them.

Let me first look at the workspace to see if it's empty or has existing files.

Since this is a multi-step task (creating a game project), I should use explore/plan. But first, a quick look at the directory.

Let me check what's in the workspace, check Python availability, and whether pygame is installed.

Approach: Use pygame (standard for learning game dev). Plan:
1. Check environment (python version, pygame installed)
2. Create snake.py with a minimal but complete version: grid, snake movement, food, score, game over, restart
3. Explain the game loop concepts (init → events → update → draw → tick)
4. Run it to verify it launches (can't really run a GUI game headless, but can at least check syntax / run with a dummy video driver for a few frames)

Actually, for teaching purposes, maybe better to build it incrementally with the user. But the user said "带我开始" — start with them. I'll create a first working version with clear structure and comments in Chinese, explain the core concepts, and tell them how to run it and what to try next.

Let me check the environment first.空目录、Python 3.14、还没装 pygame。我先装环境，再带你写第一版。逻辑验证通过：向右走 12 步后撞墙死亡，符合预期。再快速验证吃食物变长：第一版完成，逻辑已通过冒烟测试（撞墙、吃食物变长、自撞判定都正确）。

## 运行

```bash
.venv/bin/python snake.py
```

方向键控制，撞墙或撞自己结束（分数打印在终端）。

## 游戏开发最核心的概念：游戏循环

看 `snake.py:96` 的 `main()`，所有游戏（从贪吃蛇到 3A 大作）都是这个结构，每秒重复 FPS 次：

```
1. 处理输入  → 读键盘/鼠标事件，改变"意图"（direction）
2. 更新状态  → 游戏世界往前推一步（step()：蛇移动、判定死亡）
3. 绘制      → 把当前状态画成一帧（draw()）
4. tick      → clock.tick(FPS) 控制节奏，太快就等
```

贪吃蛇的特殊之处：它是一个**离散**游戏——蛇按“步”移动而不是按像素，所以 FPS=8 意味着蛇每秒走 8 格。大多数游戏是连续的（按像素/物理移动），但循环结构完全一样。

另一个值得看的点：`step()` 里蛇用**列表当队列**——新头 `insert(0, ...)` 进队首，没吃到食物就 `pop()` 掉尾巴，吃到就不 pop（这就是“变长”的全部秘密），`snake.py:33`。

## 你现在的练习（按顺序做，每个都是真实改动）

1. **调手感**：把 `FPS` 改成 12、`CELL` 改成 32，感受参数对游戏的影响
2. **死亡后重开**：死亡时别退出，在屏幕上显示 "Game Over - Press R to restart"，按 R 重置所有状态（提示：把 `main` 里的初始化代码抽成 `reset()` 函数）
3. **穿墙模式**：改 `step()` 里的撞墙判定，让蛇从左边出去、右边回来（模运算 `% COLS`）

做完第 2 个你就理解“状态重置”，做完第 3 个你就理解“坐标环绕”。改完随时贴代码或报错给我，我帮你 review。