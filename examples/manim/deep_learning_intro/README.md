# 给高中生的深度学习入门手册 - 教学视频

使用 ManimCE 创建的深度学习科普教学动画，面向高中生群体，以生动的比喻和动画展示深度学习的核心概念。

## 使用的技能 (Skills)

- **manim-composer**: Manim 动画编排与场景设计
- **manimce-best-practices**: ManimCE 最佳实践

## 项目结构

```
deep_learning_intro/
├── README.md                              # 本文档
├── scenes.md                              # 场景设计文档
├── scene_01_intro.py                      # 场景1: 开场引入
├── scene_02_ml_basics.py                  # 场景2: 机器学习基础
├── scene_03_overfitting.py                # 场景3: 过拟合与数据集划分
├── scene_04_gpu_tensor.py                 # 场景4: GPU与张量
├── scene_05_loss_gradient.py              # 场景5: 损失函数与梯度下降
├── scene_06_backprop_depth.py             # 场景6: 反向传播与深度价值
├── scene_07_building_blocks.py            # 场景7: 神经网络积木库
├── scene_08_architectures.py              # 场景8: 经典架构
├── scene_09_applications.py               # 场景9: 应用场景
├── scene_10_future.py                     # 场景10: 挑战与未来
└── all_scenes.py                          # 完整视频（所有场景）
```

## 环境要求

- Python 3.8+
- ManimCE (社区版)

### 安装 Manim

```bash
pip install manim
```

## 运行方式

```bash
cd /path/to/deep_learning_intro

# 低质量快速预览 (推荐调试时使用)
manim -pql all_scenes.py DeepLearningIntro

# 中等质量
manim -pqm all_scenes.py DeepLearningIntro

# 高质量渲染 (最终输出)
manim -pqh all_scenes.py DeepLearningIntro

# 4K 超高清
manim -pqk all_scenes.py DeepLearningIntro
```

### 渲染单个场景

```bash
# 开场引入
manim -pql scene_01_intro.py IntroScene

# 机器学习基础
manim -pql scene_02_ml_basics.py MLBasicsScene

# 过拟合
manim -pql scene_03_overfitting.py OverfittingScene

# GPU与张量
manim -pql scene_04_gpu_tensor.py GPUTensorScene

# 损失与梯度
manim -pql scene_05_loss_gradient.py LossGradientScene

# 反向传播
manim -pql scene_06_backprop_depth.py BackpropDepthScene

# 积木库
manim -pql scene_07_building_blocks.py BuildingBlocksScene

# 经典架构
manim -pql scene_08_architectures.py ArchitecturesScene

# 应用场景
manim -pql scene_09_applications.py ApplicationsScene

# 挑战与未来
manim -pql scene_10_future.py FutureScene
```

## 视频内容

| 序号 | 场景 | 内容 | 时长 |
|------|------|------|------|
| 1 | 开场引入 | AI应用展示、深度学习概念、小狗训练类比 | ~60秒 |
| 2 | 机器学习基础 | 训练集、模型、参数、损失的可视化 | ~90秒 |
| 3 | 过拟合与数据集 | 死记硬背类比、训练/验证/测试集划分 | ~90秒 |
| 4 | GPU与张量 | 硬件加速、张量维度可视化 | ~90秒 |
| 5 | 损失与梯度下降 | 损失函数、下山类比、学习率 | ~120秒 |
| 6 | 反向传播与深度 | 链式法则、梯度流动、多层协作 | ~150秒 |
| 7 | 积木库 | 线性层、卷积、激活、池化、Dropout等 | ~180秒 |
| 8 | 经典架构 | MLP、CNN、ResNet、Transformer | ~150秒 |
| 9 | 应用场景 | 图像分类、目标检测、文本生成、图像生成 | ~120秒 |
| 10 | 挑战与未来 | 提示工程、量化、适配器、总结 | ~90秒 |

**总时长**: 约 18-22 分钟

## 教学特点

### 视觉设计风格
- **科技感配色**: 深色背景 + 霓虹渐变色
- **流畅动画**: 平滑过渡、粒子效果
- **数据可视化**: 张量、梯度流、网络结构

### 颜色编码
- 🔵 `#00D4FF` (青色): 输入、数据
- 🟢 `#00FF88` (绿色): 正确、优化方向
- 🟡 `#FFD700` (金色): 重点、激活
- 🟣 `#8B5CF6` (紫色): 神经网络、模型
- 🔴 `#FF6B6B` (红色): 错误、损失
- ⚪ `#FFFFFF` (白色): 文字、边框

### 核心概念与公式

**感知机**:
$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$$

**损失函数 (MSE)**:
$$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**交叉熵损失**:
$$L = -\sum_{i=1}^{n}y_i\log(\hat{y}_i)$$

**梯度下降**:
$$w_{new} = w_{old} - \alpha \cdot \nabla L$$

**反向传播 (链式法则)**:
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial w}$$

**注意力机制**:
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

## 生活化比喻

| 概念 | 比喻 |
|------|------|
| 深度学习 | 训练小狗：演示+奖励 |
| 过拟合 | 死记硬背答案的学生 |
| 训练/验证/测试集 | 课本/模拟考/高考 |
| GPU | 游戏显卡被AI借用 |
| 张量 | 从数字到表格到立方体 |
| 梯度下降 | 闭眼在山上找最低点 |
| Dropout | 不能只靠少数人 |
| 跳跃连接 | 梯度的高速公路 |
| 注意力机制 | 读书时关联相关知识 |

## 输出文件

渲染完成后，视频文件位于:
```
media/videos/all_scenes/
├── 480p15/    # 低质量
├── 720p30/    # 中等质量
├── 1080p60/   # 高质量
└── 2160p60/   # 4K
```

## 扩展与自定义

### 修改动画速度
在各场景文件中调整 `run_time` 参数:
```python
self.play(animation, run_time=1.5)  # 调整为1.5秒
```

### 添加新场景
1. 在 `scenes.md` 中设计场景内容
2. 创建新的 `scene_xx_name.py` 文件
3. 在 `all_scenes.py` 中导入并调用

## 参考资源

- 📖 [The Little Book of Deep Learning](https://fleuret.org/public/lbdl.pdf)
- 🎬 [3Blue1Brown 神经网络系列](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- 📚 [Deep Learning Book](https://www.deeplearningbook.org/)
- 🔧 [ManimCE 官方文档](https://docs.manim.community/)

## License

MIT License
