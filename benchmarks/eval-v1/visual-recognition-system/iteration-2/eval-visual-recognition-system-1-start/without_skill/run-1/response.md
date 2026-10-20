The user wants to learn visual recognition by building a license plate recognition system in Python. The workspace is named "build-your-own-x-visual-recognition-system-1" which suggests this is a learning project. Let me first explore the workspace to see what's there.

The user says "带我开始" (guide me to start). So this is a teaching/mentoring task. Let me check the workspace first.空目录、Python 3.14 就绪。车牌识别是学视觉识别的经典项目，因为它完整覆盖一条视觉流水线：**定位目标 → 分割 → 识别**。我先给你路线图，然后带你把环境搭起来、跑通第一课。

## 学习路线（经典 CV 起步，后期升级深度学习）

1. **造数据**：用 PIL 生成带标注的合成车牌图（自己造数据 = 免费拿到 ground truth，难度可控）
2. **车牌定位**：灰度 → 边缘 → 形态学 → 轮廓筛选（宽高比 ~3.14:1）
3. **字符分割**：二值化 + 连通域分析
4. **字符识别**：先模板匹配（理解原理），再换小 CNN（理解深度学习）
5. **升级**：换成 YOLO 检测 + CRNN 识别的现代方案，对比手工特征和端到端的差异

每一步你都能**看见中间图像**，这是学视觉最重要的环节。

先搭环境：环境就绪（cv2 5.0 / numpy 2.5 / pillow 13）。开始**第 1 课：造数据**——自己生成车牌图，图片内容本身就是标注，后面每一步都能拿它对答案。先确认系统里有哪些可用的字体：字体齐全（Arial Bold 画字母数字，Arial Unicode 画省份汉字）。写第 1 课的代码：read 工具读不了图片内容，用 ASCII 预览验证一下车牌画得对不对：车牌渲染正确（能看到 7 个槽位的白色字符）。加一个简短的 README 记录路线图和进度：**第 1 课完成。** 你现在有：

- `plate_rec/gen_data.py` — 数据生成器，核心是 `draw_plate()`：蓝底画布 → 7 个槽位逐字符绘制 → `textbbox` 居中
- `plate_rec/data/plates/` — 20 张 440x140 车牌图 + `labels.txt` 标注
- `README.md` — 六课路线图，进度实时更新

**动手练习（第 2 课前建议做）：**
1. 打开 `plate_rec/data/plates/plate_0000.png` 肉眼看看，对照 `labels.txt` 第一行
2. 改 `gen_data.py` 里的 `PLATE_W/PLATE_H` 或字体大小，重新生成，观察变化
3. 思考一个问题：如果识别程序拿到这张图，第一步该做什么？（答案：先找到"车牌在哪"——这就是第 2 课的定位问题）

**第 2 课预告（车牌定位）**：把彩色图转灰度 → Canny 边缘 → 形态学闭运算把字符连成块 → `findContours` 找轮廓 → 用宽高比 ≈ 3.14 和面积过滤出车牌矩形。你随时说"继续"，我们就开始写 `locate.py`。