The user wants to build an AR demo in Python + OpenCV that overlays a cube on a marker image. They're asking where to start. The workspace is "build-your-own-x-augmented-reality-1" which suggests this might be related to a "build your own X" tutorial repo about augmented reality. Let me check what's in the workspace first — maybe there's existing material (a guide, README, etc.) that I should ground my answer in.

Let me look at the workspace contents.核心管线就四步，按这个顺序搭：

1. **标记检测** — 用 ArUco 标记（`opencv-contrib-python` 自带，不用自己写检测）
2. **相机内参** — demo 阶段用近似值即可，效果不满意再做棋盘格标定
3. **位姿估计** — `cv2.solvePnP` 把标记 4 个角点的 2D↔3D 对应解成 `rvec/tvec`
4. **投影绘制** — `cv2.projectPoints` 把立方体 8 个顶点投回图像平面，`cv2.line` 连边

环境：

```bash
pip install opencv-contrib-python numpy   # aruco 在 contrib 包里，装 opencv-python 会缺模块
```

先生成一张标记并打印（或直接在手机屏幕上显示）：

```python
import cv2
DICT = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
cv2.imwrite("marker.png", cv2.aruco.generateImageMarker(DICT, 0, 400))
```

主循环骨架（检测 + 位姿 + 画立方体，一步到位）：

```python
import cv2, numpy as np

DICT = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_250)
MARKER_SIZE = 0.05                      # 标记实际边长（米），必须和打印尺寸一致
K = np.float64([[800,0,320],[0,800,240],[0,0,1]])   # 近似内参，demo 够用
DIST = np.zeros(5)

s = MARKER_SIZE / 2
marker_pts = np.float32([[-s,-s,0],[s,-s,0],[s,s,0],[-s,s,0]])   # 标记角点（标记坐标系）
cube = np.float32(                       # 立方体：底面贴标记，向上伸 2 倍边长
    [[x,y,0] for x,y in [(-s,-s),(s,-s),(s,s),(-s,s)]] +
    [[x,y,-2*s] for x,y in [(-s,-s),(s,-s),(s,s),(-s,s)]])
edges = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
         (0,4),(1,5),(2,6),(3,7)]

cap = cv2.VideoCapture(0)
while True:
    ok, frame = cap.read()
    if not ok: break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    corners, ids, _ = cv2.aruco.detectMarkers(gray, DICT)
    if ids is not None:
        cv2.aruco.drawDetectedMarkers(frame, corners, ids)
        for i, cid in enumerate(ids.flatten()):
            if cid != 0: continue
            _, rvec, tvec = cv2.solvePnP(marker_pts, corners[i][0], K, DIST)
            pts, _ = cv2.projectPoints(cube, rvec, tvec, K, DIST)
            pts = pts.reshape(-1, 2).astype(int)
            for a, b in edges:
                cv2.line(frame, tuple(pts[a]), tuple(pts[b]), (0,255,0), 2)
    cv2.imshow("AR cube", frame)
    if cv2.waitKey(1) == 27: break
```

建议的验证顺序：先只跑检测画框 → 加 `cv2.drawFrameAxes(frame, K, DIST, rvec, tvec, 0.03)` 确认位姿方向对 → 再画立方体。如果立方体陷进纸面，把顶点的 z 符号翻过来。

几个常见坑：标记必须贴平（弯折会让位姿抖）；`MARKER_SIZE` 和实际打印尺寸不一致会导致立方体比例错；近似内参会让角度略歪，介意的话拍 15~20 张棋盘格图跑 `cv2.calibrateCamera` 换掉 K 和 DIST。The system is telling me my last reply contained no tool call — I just gave advice in text. The user asked "从哪开始" (where to start), and I gave a plan but didn't actually create anything. The internal stop hook wants me to take one concrete action via a tool call.

The workspace is empty (glob found no matches). The natural concrete action: create the actual working files — the marker generator script and the main AR demo script. That's one logical action (creating the project scaffold). The instruction says "Take exactly ONE concrete action now via a tool call" — so I should emit one tool call. But I can write files... "exactly ONE concrete action" — I'll interpret it as one tool call this turn. Let me write the main demo file first, or maybe both files? It says take exactly ONE concrete action via a tool call. To be safe, one tool call: write the main `ar_cube.py` file. Actually, creating the project with both scripts would be more useful, but the instruction is explicit: "Take exactly ONE concrete action now via a tool call."

Hmm, but multiple tool calls in one response are allowed generally. The stop hook says "Take exactly ONE concrete action now via a tool call." I'll do one write — the main demo script that includes marker generation as a fallback (if marker.png missing, generate it). That makes a single self-contained file, which is actually better design anyway.

Let me write `ar_cube.py` combining marker generation + detection + pose + cube drawing.已创建 `ar_cube.py`，把之前说的四步合并成一个自包含脚本：缺 `marker.png` 时用 `--save-marker` 生成，主循环做检测 → `solvePnP` → `projectPoints` → 画线框。

运行方式：

```bash
pip install opencv-contrib-python numpy
python ar_cube.py --save-marker   # 生成 marker.png，打印或手机显示
python ar_cube.py                 # Esc 退出
```

下一步建议按顺序验证：先确认标记能被检测到（画面上出现绿框），再加 `cv2.drawFrameAxes` 检查位姿轴向，最后看立方体是否贴合纸面——陷进去就把 `CUBE` 顶点的 z 符号翻转。