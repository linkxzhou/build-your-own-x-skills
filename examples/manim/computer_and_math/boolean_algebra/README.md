# 布尔代数：真与假的数学

本项目使用 Manim 动画库制作关于布尔代数的教学视频，详细讲解布尔代数的基本概念、运算法则、实际应用以及如何用逻辑门构建计算机加法器。

## 概述

- **主题**: 布尔代数——现代计算机科学的逻辑基石
- **预计时长**: 约 15-18 分钟
- **目标受众**: 编程初学者、计算机科学入门者、对数字电路感兴趣的学习者
- **核心洞见**: 布尔代数是连接抽象数学与物理电路的桥梁

## 场景结构

| 场景 | 文件 | 内容 | 时长 |
|------|------|------|------|
| Scene 1 | `scene_01_intro.py` | 布尔代数引入：开关比喻、基本概念、历史背景 | ~90秒 |
| Scene 2 | `scene_02_operations.py` | 三种基本运算：AND、OR、NOT及真值表 | ~120秒 |
| Scene 3 | `scene_03_laws.py` | 核心定律：交换律、结合律、分配律、德摩根定律 | ~120秒 |
| Scene 4 | `scene_04_incarnations.py` | 三个分身：集合论、命题逻辑、模2算术 | ~150秒 |
| Scene 5 | `scene_05_gates.py` | 布尔函数与逻辑门：基本门、派生门、NAND万能性 | ~150秒 |
| Scene 6 | `scene_06_adder.py` | 二进制加法器：半加器、全加器、多位加法器 | ~150秒 |
| Scene 7 | `scene_07_summary.py` | 总结与启示：知识金字塔、核心启示 | ~60秒 |

## 渲染命令

### 渲染完整视频
```bash
# 高质量渲染
manim -pqh all_scenes.py BooleanAlgebra

# 快速预览
manim -pql all_scenes.py BooleanAlgebra
```

### 渲染单个场景
```bash
# 以 Scene 1 为例
manim -pql scene_01_intro.py Scene01Intro

# 高质量渲染
manim -pqh scene_01_intro.py Scene01Intro
```

## 配色方案

| 颜色 | 色值 | 用途 |
|------|------|------|
| 科技蓝 | `#00D4FF` | 主色调、标题、重要元素 |
| 青绿 | `#4ECDC4` | 辅色、正确结果 |
| 警示红 | `#FF6B6B` | 强调、错误、反例 |
| 深蓝灰 | `#2C3E50` | 0值、假状态 |
| 金橙 | `#F39C12` | 1值、真状态 |
| 红色 | `#E74C3C` | AND运算 |
| 蓝色 | `#3498DB` | OR运算 |
| 紫色 | `#9B59B6` | NOT运算 |
| 绿色 | `#2ECC71` | XOR运算 |
| 深蓝黑 | `#1a1a2e` | 背景色 |

## 知识要点

### 1. 布尔代数基础
- 两个核心元素：0（假）和 1（真）
- 开关比喻：开=1=真，关=0=假
- 乔治·布尔 1854年创立

### 2. 三种基本运算
- **AND (∧)**: 全真才真，类比串联开关
- **OR (∨)**: 有真即真，类比并联开关
- **NOT (¬)**: 取反，真变假、假变真

### 3. 核心定律
- 交换律：a ∨ b = b ∨ a
- 结合律：a ∨ (b ∨ c) = (a ∨ b) ∨ c
- 分配律：a ∧ (b ∨ c) = (a ∧ b) ∨ (a ∧ c)
- 同一律：a ∨ 0 = a, a ∧ 1 = a
- 互补律：a ∨ ¬a = 1, a ∧ ¬a = 0
- 德摩根定律：¬(a ∧ b) = ¬a ∨ ¬b

### 4. 三个分身
- **集合论**: ∩=AND, ∪=OR, 补集=NOT
- **命题逻辑**: 且、或、非
- **模2算术**: 乘法=AND, 加法(XOR)

### 5. 逻辑门
- 基本门：AND、OR、NOT
- 派生门：NAND、NOR、XOR、XNOR
- NAND门的万能性：可构建所有其他门

### 6. 二进制加法器
- 半加器：S = A XOR B, C = A AND B
- 全加器：两个半加器 + 一个OR门
- 多位加法器：全加器级联

## 使用的技能

- manim-composer
- manimce-best-practices

## 项目结构

```
boolean_algebra/
├── README.md                 # 本文件
├── scenes.md                 # 场景规划文档
├── all_scenes.py             # 完整视频（所有场景合并）
├── scene_01_intro.py         # Scene 1: 布尔代数引入
├── scene_02_operations.py    # Scene 2: 三种基本运算
├── scene_03_laws.py          # Scene 3: 核心定律
├── scene_04_incarnations.py  # Scene 4: 三个分身实例
├── scene_05_gates.py         # Scene 5: 布尔函数与逻辑门
├── scene_06_adder.py         # Scene 6: 二进制加法器
└── scene_07_summary.py       # Scene 7: 总结与启示
```

## 依赖

- Python 3.8+
- Manim Community Edition

## 安装

```bash
pip install manim
```

## 许可

教育用途
