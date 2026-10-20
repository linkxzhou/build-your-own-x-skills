The user wants to learn license plate recognition (车牌识别) with Python to learn computer vision. This matches the build-your-own-x skill — "build-your-own-x" skill covers learning by rebuilding real software, and the Chinese triggers include 项目式学习, 从零实现 etc. License plate recognition is a computer vision project. Let me read the skill first.

The skill says: read SKILL.md BEFORE doing anything else. Let me do that.The SKILL.md is truncated. Let me read the rest of it, and also check the skills directory for a matching track. License plate recognition is a computer vision / ML topic. Let me see the category table.The map routes 车牌识别/视觉识别 to the `visual-recognition-system` track. Reading that skill now.该赛道技能要求我确定范围，选择上游指南，并检查学习者的环境。让我检查一下工作区、Python 环境以及针对每个教程的技能。Python 3.14 + numpy 已就绪；cv2/skimage/sklearn/matplotlib 缺失（根据教练规则，你需要自己安装它们）。让我阅读一下车牌教程的各教程技能，以获取针对该文章的详细信息。I have the full picture now. Let me also read the concepts.md reference to have the concept checklist ready for coaching.技能已加载。现在让我获取上游教程，以便基于其实际内容来制定计划。Medium 拦截了直接抓取。让我搜索一下该文章的方法总结，以便准确引用。技能和教程映射已加载。在提出环境配置之前，让我快速确认一下当前的 `scikit-learn`/`scikit-image` 版本是否支持 Python 3.14（当前环境使用的是 3.14.7）。**当前进度：** 准备阶段（0/7），确认两件事后进入里程碑 1。

**核心概念：** 车牌识别是一条流水线——整张照片进来，先**定位**（找到车牌所在的矩形区域），再**分割**（把车牌里的每个字符切开），最后**分类**（认出每个字符）。前三步靠经典图像处理（灰度、边缘、阈值、形态学、连通域），最后一步用机器学习（HOG 特征 + SVM）。一个项目覆盖 CV 和 ML 两块基础。

**跟练教程（upstream）：** [Developing a License Plate Recognition System with Machine Learning in Python](https://medium.com/devcenter/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)。原文在 Medium 上可能要登录，方法我会按里程碑拆解给你。工具链用 scikit-image 替代原文的 OpenCV：依赖更少、API 更适合逐个概念学习。

**里程碑（每个都有可运行的检查点，通过才进入下一个）：**

| # | 里程碑 | 检查点 |
|---|---|---|
| 1 | 数据集与加载 | 脚本加载 N 张图，打印类别统计 |
| 2 | 预处理 | 调试图显示干净的车牌二值图 |
| 3 | 车牌定位 | 10 张测试图画出框，多数 IoU > 0.5 |
| 4 | 字符分割 + SVM 分类 | 报告测试准确率，保存混淆矩阵 |
| 5 | 完整流水线 | `python recognize.py 照片.jpg` 打印车牌号 |
| 6 | 错误分析 | 5 个最差案例 + 原因报告 |
| 7 | 进阶 | 实时摄像头识别，或字符分类器换成 CNN |

**两个问题（都带默认值，直接回“按默认来”也行）：**

1. 识别哪种车牌？默认：**中国蓝牌**（含省份汉字，训练字符用代码合成生成）。
2. 数据来源？默认：字符训练集用 PIL 合成（离线、标签免费、数量随意），定位用的真实照片你提供 10–20 张（手机拍的停车场、路边车辆即可），不够我再给你找公开样例图。

**现在请你在终端跑环境准备**（安装命令由你自己执行）：

```bash
mkdir -p plate-recognition && cd plate-recognition
python3 -m venv .venv
source .venv/bin/activate
pip install scikit-image scikit-learn matplotlib
```

你的 Python 是 3.14，我查过 scikit-image 和 scikit-learn 最新版都支持 3.14，numpy 已经装好。

**本步检查：**

```bash
python -c "import skimage, sklearn, matplotlib; print(skimage.__version__, sklearn.__version__)"
```

预期输出类似 `0.25.2 1.7.1`（版本号可能更新）。跑通后回我两个问题的答案，我们就建项目骨架、写里程碑 1 的加载脚本。