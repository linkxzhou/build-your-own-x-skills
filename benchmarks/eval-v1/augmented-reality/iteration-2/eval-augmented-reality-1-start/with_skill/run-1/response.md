The user asks in Chinese: "I want to use Python + OpenCV to make an AR demo that overlays a cube on a marker image, where do I start?"

This matches the build-your-own-x skill trigger: "从零实现、自己动手写一个 X" — building an AR demo from scratch with OpenCV. The skill description says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems skills..." This is a hands-on project to learn computer vision skills — overlaying a cube on a marker image is a classic AR from-scratch project. The skill says to read SKILL.md BEFORE doing anything else.

So I should read the skill file first.The file was truncated. Let me read the rest of it.该主题映射到 `augmented-reality` 路径。正在读取路径技能。The glob output is truncated. Let me search specifically for augmented-reality skills.轨道技能和 Python+OpenCV 教程技能均已存在。正在并行读取这两个技能。轨道技能的里程碑表格被截断了。我正在读取剩余部分以及 Python+OpenCV 的教程地图。我正在读取轨道教程列表，以获取准确的 Python+OpenCV 指南链接。I have everything I need. The user's request maps exactly to the Python + OpenCV track, and the upstream tutorial is "Augmented Reality with Python and OpenCV" (bitesofcode, part 1). The per-tutorial skill `augmented-reality-python-opencv` matches.

Now, per the coaching rules:
- Agree on scope: language is already decided (Python + OpenCV). Target: marker-based AR overlaying a cube. I should ask at most 2 questions, and suggest a default if the learner doesn't care. Key question: webcam available or static test images? That determines milestone 1's shape.
- Work milestone by milestone. Don't dump the whole project. Give skeleton for milestone 1, not full solution.
- Every reply ends with "How to check it": command + expected output.
- Never install anything myself — print the pip command for the learner.
- Credit the upstream tutorial with its exact link.
- Record milestones in PROGRESS.md when passed.

The user asked "从哪开始?" (where do I start?). So my answer should:
1. State the track and the upstream tutorial link.
2. Give the milestone list (7 milestones from the track skill, possibly merged).
3. Ask the 1-2 scoping questions (webcam vs static images; OpenCV installed?).
4. Give milestone 1 skeleton + checkpoint command.
5. Print the pip install command for them to run themselves.

Also per the skill: "Stay in the learner's workspace" — I should check what's in the workspace. Let me check what exists in the workspace first (empty dir? existing project?). The workflow says "Identify whether the user is starting from an empty directory, continuing a partial implementation, or debugging a failing project."

Let me check the workspace contents quickly. Also check if Python/OpenCV are available — but I must not install anything. Checking what's already there is fine and encouraged ("prefer the tools that are already there", "check what exists").

Let me run a quick bash to list the workspace and check python/opencv availability.从零开始做一个标记式 AR，路线已经定好：**Python + OpenCV 轨道**，跟着这篇上游教程走：[Augmented Reality with Python and OpenCV](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)（bitesofcode, Part 1）。你负责写代码，我负责拆里程碑、给骨架、陪你调试。

**当前位置：里程碑 1/6 —— 图像输入**

整条路线（每个里程碑都有可运行的检查点，通过才进下一个）：

1. **图像输入** — 加载标记图 + 场景图（或摄像头帧）
2. **特征检测** — ORB/SIFT 关键点，标记图上关键点数 > 100
3. **特征匹配** — BFMatcher + Lowe ratio test，画出匹配线
4. **单应矩阵 / 位姿** — RANSAC 求 homography，把标记轮廓画成正确的四边形
5. **渲染立方体** — 用位姿把 3D 立方体投影叠加到标记上
6. **稳定性** — 帧间平滑，叠加物不抖

**先做两件事（你自己跑，我不代装）：**

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install opencv-python numpy
```

注意：你机器上是 Python 3.14，如果 `pip install opencv-python` 报找不到 wheel，就换 Python 3.12/3.13 建 venv。

**里程碑 1 的骨架**（新建 `ar_cube.py`，核心留给你写）：

```python
# ar_cube.py — 里程碑 1：输入层
import cv2

MARKER_PATH = "marker.jpg"   # 标记图：一块平面、纹理丰富的图（书封面、杂志封面都行）
SCENE_PATH  = "scene.jpg"    # 场景图：这张标记图出现在某个场景里的照片

def load_images():
    marker = cv2.imread(MARKER_PATH, cv2.IMREAD_GRAYSCALE)
    scene  = cv2.imread(SCENE_PATH,  cv2.IMREAD_GRAYSCALE)
    # TODO 1: imread 读不到文件时静默返回 None，加断言防后面莫名崩溃
    return marker, scene

if __name__ == "__main__":
    marker, scene = load_images()
    # TODO 2: 打印两张图的 shape
    # TODO 3: 用 cv2.imshow 各开一个窗口显示，cv2.waitKey(0) 后销毁
```

两个问题（都有默认值，不回复就按默认走）：

1. 有摄像头吗？默认先用静态图片做完 1–5，第 6 步再切摄像头——静态图好调试。
2. 标记图选好了吗？默认随便找一本书封面拍两张照片：一张正面特写当 `marker.jpg`，一张斜着放进场景当 `scene.jpg`。

**检查点**：`python ar_cube.py` 应打印两个尺寸（如 `(480, 640)`），并弹出两个灰度图窗口。跑通后把结果告诉我，我们进里程碑 2。The system says my last reply contained no tool call — commands in code fences are display-only. I need to take one concrete action via a tool call. The natural next step: create the milestone 1 skeleton file `ar_cube.py` in the workspace, per the coaching skill (scaffold, learner writes core). That's one concrete action.

The skill says stay in the learner's workspace, keep scratch files inside the project. Creating `ar_cube.py` with the skeleton and TODOs is exactly the scaffold step. I should not dump the full solution — skeleton with TODOs is fine.

Let me write the file.骨架已落盘：`ar_cube.py`（里程碑 1/6，图像输入）。三个 TODO 留给你：断言防 None、打印 shape、imshow 显示两图。

接下来你做两件事：

1. 装依赖（你自己跑）：
   ```bash
   python3 -m venv .venv && source .venv/bin/activate
   pip install opencv-python numpy
   ```
   Python 3.14 若报找不到 opencv wheel，换 3.12/3.13 建 venv。
2. 补完三个 TODO，并准备两张图：`marker.jpg`（书封面正面特写）和 `scene.jpg`（同一封面斜放在场景里的照片）。

**检查点**：`python ar_cube.py` → 打印两个尺寸（如 `(480, 640)`），弹出两个灰度窗口。跑通后把输出贴给我，进里程碑 2（ORB 特征检测）。