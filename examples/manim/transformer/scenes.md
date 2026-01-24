# Transformer 原理教学视频 - 场景设计

## Overview
- **Topic**: Transformer 架构原理
- **Hook**: "为什么 Transformer 能让机器真正'理解'语言？它的注意力机制有什么魔力？"
- **Target Audience**: 有基本机器学习概念的学习者
- **Estimated Length**: 10-15 分钟
- **Key Insight**: 自注意力机制让模型能够动态地关注输入中最相关的部分

## Narrative Arc
从传统序列模型（RNN）的局限性出发，引出"注意力"的概念。通过可视化展示 Query、Key、Value 的交互过程，揭示自注意力机制如何让每个词都能"看到"整个句子。最后展示完整的 Transformer 架构，让观众理解这一革命性模型的工作原理。

---

## Scene 1: 开场引入 - 语言理解的挑战
**Duration**: ~40 秒
**Purpose**: 引出问题，吸引注意力

### Visual Elements
- 标题动画 "Transformer 原理"
- 一个句子的词语序列
- 词与词之间的依赖关系箭头

### Content
展示一个句子 "The animal didn't cross the street because it was too tired"
提问："这里的 'it' 指的是什么？"
展示人类如何轻松理解，但机器需要"看到"整个句子才能判断

### Narration Notes
语气：好奇、引导思考
"机器如何像人一样理解语言中的长距离依赖？"

### Technical Notes
- Text 创建句子
- Arrow 显示依赖关系
- Indicate 高亮关键词

---

## Scene 2: RNN 的局限性
**Duration**: ~45 秒
**Purpose**: 说明为什么需要新的架构

### Visual Elements
- RNN 链式结构图
- 信息流动动画（逐渐衰减）
- "瓶颈"可视化

### Content
1. 展示 RNN 的顺序处理方式
2. 演示信息随时间步衰减
3. 指出两个问题：
   - 长距离依赖困难
   - 无法并行计算

### Narration Notes
"RNN 像是在玩传话游戏，信息传得越远，丢失得越多"

### Technical Notes
- Rectangle + Arrow 构建 RNN 结构
- 颜色渐变表示信息衰减

---

## Scene 3: 注意力机制的直觉
**Duration**: ~60 秒
**Purpose**: 建立注意力的直观理解

### Visual Elements
- 句子中的词语序列
- 注意力权重热力图
- 动态连接线

### Content
1. 展示"注意力"的比喻：阅读时眼睛会跳到相关的词
2. 对于 "it"，注意力集中在 "animal" 上
3. 不同的词有不同的注意力模式

### Narration Notes
"注意力机制让模型能够'看向'最相关的部分"

### Technical Notes
- 热力图用 Rectangle + opacity
- 连接线用 Line + stroke_width 变化

---

## Scene 4: Query, Key, Value 概念
**Duration**: ~90 秒
**Purpose**: 核心概念详解

### Visual Elements
- 三个向量：Q（蓝色）、K（绿色）、V（橙色）
- 矩阵变换动画
- 查询-匹配过程可视化

### Content
1. 类比：图书馆查询系统
   - Query：你想找什么？
   - Key：每本书的标签
   - Value：书的实际内容
2. 每个词生成自己的 Q、K、V
3. 通过 Q 和 K 的匹配找到相关的 V

### Narration Notes
"Query 问问题，Key 提供索引，Value 给出答案"

### Technical Notes
- 向量用 Arrow 或 Matrix
- 矩阵乘法动画
- 颜色编码：Q=BLUE, K=GREEN, V=ORANGE

---

## Scene 5: 自注意力计算过程
**Duration**: ~120 秒
**Purpose**: 详细演示计算步骤

### Visual Elements
- 输入序列矩阵
- Q、K、V 矩阵
- 注意力分数矩阵
- Softmax 归一化
- 最终输出

### Content
完整演示自注意力计算：
1. 输入 X 通过三个权重矩阵得到 Q、K、V
2. 计算注意力分数：Q × K^T
3. 缩放：除以 √d_k
4. Softmax 归一化
5. 加权求和：Attention × V

### Narration Notes
逐步解释每个步骤的意义，强调"为什么要缩放"

### Technical Notes
- Matrix 显示矩阵
- MathTex 显示公式
- Transform 动画展示计算过程

---

## Scene 6: 多头注意力
**Duration**: ~60 秒
**Purpose**: 解释多头机制的意义

### Visual Elements
- 多个平行的注意力"头"
- 不同颜色表示不同头
- 合并过程

### Content
1. 单头注意力的局限：只能关注一种关系
2. 多头：同时关注不同类型的关系
   - 语法关系
   - 语义关系
   - 位置关系
3. 最后拼接并投影

### Narration Notes
"多头注意力就像多个专家同时分析，各司其职"

### Technical Notes
- 多个并行的注意力模块
- Concatenate 动画

---

## Scene 7: 位置编码
**Duration**: ~45 秒
**Purpose**: 解释为什么需要位置信息

### Visual Elements
- 打乱顺序的句子
- 正弦/余弦波形
- 位置编码向量

### Content
1. 问题：自注意力没有位置概念
2. "猫吃鱼" vs "鱼吃猫" 对注意力来说一样
3. 解决：添加位置编码
4. 使用正弦余弦函数生成位置向量

### Narration Notes
"位置编码给每个词一个'坐标'，告诉模型它在哪里"

### Technical Notes
- 正弦波用 ParametricFunction
- 位置向量可视化

---

## Scene 8: 完整 Transformer 架构
**Duration**: ~90 秒
**Purpose**: 展示整体结构

### Visual Elements
- 编码器-解码器结构
- 各层组件
- 数据流动动画

### Content
1. 编码器结构：
   - 多头自注意力
   - 前馈网络
   - 残差连接 + 层归一化
2. 解码器结构：
   - Masked 自注意力
   - 编码器-解码器注意力
   - 前馈网络
3. 堆叠多层

### Narration Notes
"编码器理解输入，解码器生成输出"

### Technical Notes
- 模块化设计
- 箭头显示数据流
- 渐进式展开

---

## Scene 9: Transformer 的优势
**Duration**: ~45 秒
**Purpose**: 总结优点

### Visual Elements
- 对比表格
- 并行计算示意
- 长距离依赖可视化

### Content
1. 并行计算：所有位置同时处理
2. 长距离依赖：任意两个位置直接连接
3. 可解释性：注意力权重可视化

### Narration Notes
"这就是 Transformer 革命性的原因"

### Technical Notes
- Table 或 VGroup 对比
- 并行箭头动画

---

## Scene 10: 总结与应用
**Duration**: ~40 秒
**Purpose**: 回顾要点，展望应用

### Visual Elements
- 核心概念回顾
- 应用案例（GPT、BERT 等）
- 感谢语

### Content
1. 核心回顾：
   - 自注意力：让每个词看到全局
   - Q、K、V：查询-匹配-取值
   - 多头：多角度分析
2. 应用：GPT、BERT、Vision Transformer

### Narration Notes
"Transformer 开启了 AI 的新时代"

---

## Color Palette
- Primary: BLUE (#58C4DD) - Query、主要元素
- Secondary: GREEN (#83C167) - Key
- Accent: ORANGE (#FFA500) - Value
- Highlight: YELLOW (#FFFF00) - 重点标注
- Attention: RED_C - 注意力权重
- Background: #1C1C1C

## Mathematical Content
- 自注意力公式：$\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$
- 多头注意力：$\text{MultiHead}(Q,K,V) = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O$
- 位置编码：$PE_{(pos,2i)} = \sin(pos/10000^{2i/d})$

## Implementation Order
1. transformer.py - 主场景文件
2. 分场景测试
3. 完整渲染
