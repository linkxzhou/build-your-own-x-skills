The user asks in Chinese: "I want to use Python + OpenCV to make an AR demo that overlays a cube on a marker image, where do I start?"

This matches the build-your-own-x skill: "build your own... a browser..." — specifically AR overlay cube on marker is like building a mini AR system from scratch. The skill description says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills... It picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution."

The trigger: "想通过做项目学底层原理、推荐一个练手项目" — the user wants to build an AR demo with Python + OpenCV. This is a hands-on project. It's arguably a build-your-own-x category? The categories listed: Git, Redis/databases, shell, Docker/containers, interpreter/compiler, OS, emulator, web server, browser, regex/template engine, game, neural network, blockchain, LLM, malloc, CPU. AR cube overlay isn't exactly in that list... but the skill says "Entry point for learning by rebuilding real software from scratch" and "asks for a hands-on project to learn systems or engineering skills". The user is asking "从哪开始" (where to start) for a hands-on project. Hmm, is this a match? The skill says "names a category from codecrafters-io/build-your-own-x" — AR isn't a category there. But "asks for a hands-on project to learn systems or engineering skills" — the user already has a project in mind (AR cube overlay with OpenCV). 

The instruction says: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it". The match is plausible: it's a hands-on learning project (build your own AR). The skill "picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution." The user already picked topic (AR cube overlay) and language (Python + OpenCV). The skill might still be relevant as an entry point for coaching.

I think the safe move: read the SKILL.md first, then decide. It's cheap. Let me read it.

Then I should coach step by step: explain the pipeline (camera calibration, marker detection, pose estimation, drawing cube), give a minimal roadmap, maybe starter code skeleton. The skill says "coaches step by step instead of dumping a finished solution" — so I should give a roadmap and first steps, maybe a small starter snippet, rather than a full 300-line solution.

Let me read the skill first.The skill file is truncated. Let me read the rest of it, and also check the category map to find the right slug. AR cube overlay with OpenCV — likely "misc" track or maybe "computer-vision"/"graphics"? Let me read the rest of the file.Topic maps to the `augmented-reality` track. Reading the track skill now (mandatory per the router).Truncated again. Let me read the rest of the file (lines 43+).Now read the tutorials reference to pick a guide for Python + OpenCV marker-based AR.The Python tutorial is "Augmented Reality with Python and OpenCV" from bitesofcode. There may be a per-tutorial skill `skills/augmented-reality-*`. Let me check the skills directory for per-tutorial skills.

Also, per the coaching rules:
1. Agree on scope: language (Python + OpenCV — already given), target, checks. Ask at most 2 questions, suggest defaults.
2. Pick a guide — the bitesofcode tutorial.
3. Work milestone by milestone.

Output format per turn:
- Where we are: milestone N/total
- The concept: short
- What to write next: skeleton or TODO list, not full answer
- How to check it: command + expected output
- Stuck? One hint at a time.

Also: "Stay in the workspace. Never install anything yourself." Print pip command for learner. Check what exists in the workspace — maybe check if there's a webcam or test images? I can check the workspace contents quickly. Also check if opencv is already installed? The rule says never run install commands; checking with `python -c "import cv2"` is fine (read-only check). Let me check the workspace and whether cv2/numpy exist.

Let me also check for per-tutorial skills: glob skills/augmented-reality-*/SKILL.md.There's a per-tutorial skill for the Python + OpenCV article. Reading it for article-specific details.路线可以定下来了：Python + OpenCV 标记式 AR，跟着上游教程 [Augmented Reality with Python and OpenCV (bitesofcode)](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/) 做。整体 6 个里程碑，每个都有可运行的检查点：

| # | 里程碑 | 检查点 |
|---|---|---|
| 1 | 图像输入 | 脚本加载并显示标记图 + 场景图（或摄像头帧） |
| 2 | 特征检测 | ORB/SIFT 关键点画在标记图上，数量 > 100 |
| 3 | 特征匹配 | 匹配可视化中绝大多数连线正确 |
| 4 | 单应性/位姿 | 标记轮廓以正确的四边形画到场景图上 |
| 5 | 渲染立方体 | 立方体钉在标记上，图像移动时保持贴合 |
| 6 | 稳定性 | 10 秒片段里叠加层抖动可接受 |

**Milestone 1/6 — 图像输入**

概念：AR 程序本质是一个循环——读帧 → 求标记位姿 → 画 3D → 显示。第一步只搭 I/O 骨架：把“标记图”（参考图）和“包含标记的场景图”读进来并显示。

环境（命令你来跑）：

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install opencv-python numpy
```

现在的 OpenCV（≥4.4）已内置 SIFT，2017 年教程里装 opencv-contrib 的步骤可以跳过。

项目结构：

```
ar-cube/
├── marker.jpg   # 标记图：选纹理丰富的平面图（书封、包装盒面），避开重复图案
├── scene.jpg    # 场景图：把标记图打印出来或显示在屏幕/手机上，从斜角度拍一张
└── ar_demo.py
```

`ar_demo.py` 骨架（核心约 15 行，你自己填）：

```python
import sys
import cv2

def load_image(path):
    # TODO: cv2.imread 读图；返回 None 时打印原因并以非零码退出
    ...

def main():
    marker = load_image(sys.argv[1])
    scene = load_image(sys.argv[2])
    # TODO: cv2.imshow 分别显示两张图，cv2.waitKey(0) 后 destroyAllWindows
    ...

if __name__ == "__main__":
    main()
```

检查点：

```bash
python ar_demo.py marker.jpg scene.jpg
```

预期：弹出两个窗口分别显示两张图，按任意键退出，无 traceback。

标记默认走教程的特征匹配路线（任意有纹理的平面图都能当标记）；ArUco 黑白方块是等价的另一条路线，到第 2–4 步换成 `cv2.aruco` 检测即可，整体流程相同。

一个问题需要你定：后续用摄像头实时画面，还是先只用静态图片？我的默认建议是先静态图片——没摄像头或权限麻烦时全程可跑通，第 5 步把 `cv2.imread` 换成 `cv2.VideoCapture(0)` 就升级成实时 AR。

跑完检查点（或卡住）把输出贴给我；通过后我们记入 `PROGRESS.md`，进入特征检测。