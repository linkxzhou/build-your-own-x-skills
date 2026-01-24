# Transformer 原理教学视频

基于 Manim 的 Transformer 架构原理教学动画，详细展示注意力机制的工作原理。

## 项目结构

```
transformer/
├── README.md           # 本文档
├── scenes.md           # 场景设计文档
└── transformer.py      # Manim 动画源码
```

## 环境要求

- Python 3.8+
- Manim Community Edition

### 安装 Manim

```bash
pip install manim
```

macOS 还需要安装依赖：
```bash
brew install py3cairo ffmpeg pango scipy
```

## 运行方式

```bash
cd /path/to/transformer

# 低质量预览（快速渲染）
manim -pql transformer.py TransformerTutorial

# 中等质量
manim -pqm transformer.py TransformerTutorial

# 高质量渲染
manim -pqh transformer.py TransformerTutorial

# 4K 渲染
manim -pqk transformer.py TransformerTutorial
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `-p` | 渲染完成后自动播放 |
| `-q` | 质量等级：`l`(低), `m`(中), `h`(高), `k`(4K) |

## 视频内容

共 10 个场景，时长约 10-15 分钟：

| 场景 | 内容 | 时长 |
|------|------|------|
| 1. 开场引入 | 语言理解的挑战 | ~40秒 |
| 2. RNN 局限 | 传统模型的问题 | ~45秒 |
| 3. 注意力直觉 | 注意力机制概念 | ~60秒 |
| 4. QKV 概念 | Query, Key, Value | ~90秒 |
| 5. 自注意力 | 计算过程详解 | ~120秒 |
| 6. 多头注意力 | Multi-Head 机制 | ~60秒 |
| 7. 位置编码 | 正弦/余弦编码 | ~45秒 |
| 8. 完整架构 | Encoder-Decoder | ~90秒 |
| 9. 优势总结 | 为什么成功 | ~45秒 |
| 10. 总结 | 核心回顾 | ~40秒 |

## 核心概念

### 自注意力 (Self-Attention)
让序列中的每个位置都能"看到"整个序列，动态计算相关性。

### Query, Key, Value
- **Query (Q)**: 当前位置想要查询什么
- **Key (K)**: 其他位置的"标签"
- **Value (V)**: 其他位置的实际内容

### 注意力公式
$$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$

### 多头注意力
同时从多个角度分析关系：
$$\text{MultiHead} = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O$$

## 颜色编码

| 颜色 | 含义 |
|------|------|
| 🔵 蓝色 | Query / 编码器 |
| 🟢 绿色 | Key / 解码器 |
| 🟠 橙色 | Value / Cross Attention |
| 🟡 黄色 | 重点标注 |
| 🔴 红色 | 注意力权重 |

## 输出文件

渲染完成后，视频文件位于：
```
media/videos/transformer/[质量]/TransformerTutorial.mp4
```

## 自定义修改

### 修改示例句子
在 `intro_scene()` 中修改：
```python
sentence = Text("Your sentence here", ...)
```

### 调整动画速度
修改各场景中的 `run_time` 参数。

### 修改颜色主题
在文件顶部的颜色常量区域修改：
```python
QUERY_COLOR = BLUE
KEY_COLOR = GREEN
VALUE_COLOR = ORANGE
```

## 知识点参考

- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - 原始论文
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/) - 图解教程
- [Transformer 详解](https://zhuanlan.zhihu.com/p/338817680) - 中文解读

## 许可证

MIT License
