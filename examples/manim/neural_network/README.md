# 神经网络原理教学视频

使用 ManimCE 创建的神经网络基础原理教学动画。

## 项目结构

```
neural_network/
├── README.md           # 本文档
├── scenes.md           # 场景设计文档
└── neural_network.py   # Manim 动画源码
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
cd /path/to/neural_network

# 低质量快速预览 (推荐调试时使用)
manim -pql neural_network.py NeuralNetworkTutorial

# 中等质量
manim -pqm neural_network.py NeuralNetworkTutorial

# 高质量渲染 (最终输出)
manim -pqh neural_network.py NeuralNetworkTutorial

# 4K 超高清
manim -pqk neural_network.py NeuralNetworkTutorial
```

### 渲染单个场景

```bash
# 感知机场景
manim -pql neural_network.py PerceptronScene

# 激活函数场景
manim -pql neural_network.py ActivationScene

# 反向传播场景
manim -pql neural_network.py BackpropScene
```

## 视频内容

| 序号 | 场景 | 内容 | 时长 |
|------|------|------|------|
| 1 | 开场引入 | 标题、问题引入、大脑类比 | ~40秒 |
| 2 | 生物神经元 | 树突、细胞体、轴突、突触结构 | ~60秒 |
| 3 | 感知机 | 人工神经元、权重、偏置、激活 | ~90秒 |
| 4 | 激活函数 | Step、Sigmoid、Tanh、ReLU 对比 | ~90秒 |
| 5 | 多层网络 | 输入层、隐藏层、输出层结构 | ~120秒 |
| 6 | 前向传播 | 矩阵计算、数值示例 | ~90秒 |
| 7 | 损失函数 | MSE、Cross-Entropy、损失曲面 | ~60秒 |
| 8 | 反向传播 | 链式法则、梯度计算、权重更新 | ~150秒 |
| 9 | 梯度下降 | 下山类比、学习率对比 | ~90秒 |
| 10 | MNIST 案例 | 手写数字识别实例 | ~90秒 |
| 11 | 正则化 | 过拟合、L2、Dropout、Early Stopping | ~60秒 |
| 12 | 总结 | 核心概念回顾、未来展望 | ~45秒 |

**总时长**: 约 12-15 分钟

## 教学特点

### 视觉设计
- **颜色编码**:
  - 🔵 蓝色: 输入层
  - 🟣 紫色: 隐藏层
  - 🟠 橙色: 输出层
  - 🟢 绿色: 正权重
  - 🔴 红色: 负权重
  - 🟡 黄色: 激活状态
  - 🌊 青色: 梯度流

### 核心公式

**感知机**:
$$y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)$$

**激活函数 (Sigmoid)**:
$$\sigma(x) = \frac{1}{1 + e^{-x}}$$

**损失函数 (MSE)**:
$$L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2$$

**反向传播**:
$$\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial w}$$

**梯度下降**:
$$w_{new} = w_{old} - \alpha \cdot \nabla L$$

## 自定义与扩展

### 修改网络结构
在 `create_neural_network()` 方法中调整 `layer_sizes` 参数：
```python
layer_sizes = [4, 8, 8, 4, 2]  # 5层网络
```

### 添加新场景
1. 在 `scenes.md` 中设计场景
2. 在 `neural_network.py` 中实现方法
3. 在 `construct()` 中调用

## 输出文件

渲染完成后，视频文件位于:
```
media/videos/neural_network/
├── 480p15/    # 低质量
├── 720p30/    # 中等质量
├── 1080p60/   # 高质量
└── 2160p60/   # 4K
```

## 参考资源

- [ManimCE 官方文档](https://docs.manim.community/)
- [3Blue1Brown 神经网络系列](https://www.youtube.com/playlist?list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi)
- [Deep Learning Book](https://www.deeplearningbook.org/)

## License

MIT License
