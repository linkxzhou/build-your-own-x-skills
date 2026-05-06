# 计算机与数字：二进制的奥秘

这是一个使用 Manim 制作的教学动画，详细介绍计算机如何表示和处理数字。

## 📚 内容概述

本章核心是解释**计算机如何表示和处理数字**。计算机虽然功能强大，但它的"思维"基础异常简单：它只能理解"开"和"关"，即 1 和 0（二进制）。所有的数字，无论是整数还是小数，最终都必须翻译成这种二进制语言才能被存储和计算。

### 场景列表

| 场景 | 文件 | 内容 |
|------|------|------|
| Scene 1 | `scene_01_intro.py` | 开场引入 - 计算机的二进制世界 |
| Scene 2 | `scene_02_number_systems.py` | 进制转换 - 十进制、二进制、十六进制 |
| Scene 3 | `scene_03_integers.py` | 整数的存储 - 精确存储与范围限制 |
| Scene 4 | `scene_04_floats.py` | 浮点数的存储 - IEEE 754 标准 |
| Scene 5 | `scene_05_special_cases.py` | 计算中的奇怪情况 - 误差与特殊值 |
| Scene 6 | `scene_06_summary.py` | 总结与启示 |
| 完整版 | `all_scenes.py` | 整合所有场景的完整视频 |

## 🎯 知识点

### 1. 数字的"语言"：不同的进制
- **十进制**: 我们熟悉的满十进一
- **二进制**: 计算机的母语，只用 0 和 1
- **十六进制**: 程序员的"缩写"，使用 0-9 和 A-F

### 2. 整数存储
- 固定位数存储 (8、16、32、64位)
- 范围限制：n位能存 [0, 2ⁿ-1]
- 溢出问题
- 负数的补码表示

### 3. 浮点数存储 (IEEE 754)
- 符号位 (1位)
- 指数位 (8位)
- 尾数位 (23位)
- 舍入误差的必然性

### 4. 特殊情况
- 舍入误差累积
- NaN (不是一个数字)
- Inf (无穷大)

## 🚀 渲染命令

### 渲染完整视频

```bash
# 预览质量 (快速)
manim -pql all_scenes.py ComputersAndNumbers

# 高质量
manim -pqh all_scenes.py ComputersAndNumbers

# 4K 质量
manim -pqk all_scenes.py ComputersAndNumbers
```

### 渲染单个场景

```bash
# Scene 1: 开场引入
manim -pql scene_01_intro.py Scene01Intro

# Scene 2: 进制转换
manim -pql scene_02_number_systems.py Scene02NumberSystems

# Scene 3: 整数存储
manim -pql scene_03_integers.py Scene03Integers

# Scene 4: 浮点数存储
manim -pql scene_04_floats.py Scene04Floats

# Scene 5: 特殊情况
manim -pql scene_05_special_cases.py Scene05SpecialCases

# Scene 6: 总结
manim -pql scene_06_summary.py Scene06Summary
```

### 渲染参数说明

| 参数 | 说明 |
|------|------|
| `-p` | 渲染完成后自动预览 |
| `-ql` | 低质量 (480p, 15fps) - 快速预览 |
| `-qm` | 中等质量 (720p, 30fps) |
| `-qh` | 高质量 (1080p, 60fps) |
| `-qk` | 4K 质量 (2160p, 60fps) |

## 🎨 配色方案

```python
PRIMARY = "#00D4FF"      # 科技蓝 - 标题、重要元素
SECONDARY = "#FF6B6B"    # 警示红 - 错误、溢出、警告
ACCENT = "#4ECDC4"       # 青绿 - 正确结果、成功状态
BG = "#1a1a2e"           # 深蓝黑 - 科技感背景
TEXT = "#FFFFFF"         # 白色 - 主要文字
GRAY = "#888888"         # 灰色 - 说明文字
BINARY_0 = "#2C3E50"     # 0的颜色
BINARY_1 = "#F39C12"     # 1的颜色
```

## 📁 文件结构

```
computers_and_numbers/
├── README.md                    # 本文件
├── scenes.md                    # 场景规划文档
├── scene_01_intro.py           # Scene 1: 开场引入
├── scene_02_number_systems.py  # Scene 2: 进制转换
├── scene_03_integers.py        # Scene 3: 整数存储
├── scene_04_floats.py          # Scene 4: 浮点数存储
├── scene_05_special_cases.py   # Scene 5: 特殊情况
├── scene_06_summary.py         # Scene 6: 总结
└── all_scenes.py               # 完整视频 (整合所有场景)
```

## 🛠️ 使用的技能

- **manim-composer**: 场景规划和叙事结构
- **manimce-best-practices**: Manim Community Edition 最佳实践

## 📖 参考资料

- [Manim Community 文档](https://docs.manim.community/)
- [IEEE 754 浮点数标准](https://en.wikipedia.org/wiki/IEEE_754)
- [二进制补码](https://en.wikipedia.org/wiki/Two%27s_complement)

## ⚠️ 注意事项

1. **MathTex 中禁止使用中文** - 中文部分使用 `Text`，数学公式使用 `MathTex`，然后用 `VGroup` 组合
2. **布局居中** - 使用 `.set_x(0)` 确保元素水平居中
3. **避免动画重叠** - 每个场景结束时使用 `clear_scene()` 清理元素

## 📝 版本历史

- v1.0.0 - 初始版本，包含完整的六个场景
