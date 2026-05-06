# 第六章：递推与递归

> 数学中的迭代，编程中的分解术

本项目使用 [Manim](https://www.manim.community/) 动画库创建《编程中的数学》第六章教学视频。

## 📖 内容概述

### 第一部分：递推关系——数学中的"迭代"

| 场景 | 文件 | 内容 |
|------|------|------|
| Scene 1 | `scene_01_intro.py` | 开场与概念引入（俄罗斯套娃比喻） |
| Scene 2 | `scene_02_recurrence_basics.py` | 递推基础（等差/等比/斐波那契数列） |
| Scene 3 | `scene_03_linear_recurrence.py` | 线性递推与伪随机数生成（LCG） |
| Scene 4 | `scene_04_nonlinear_recurrence.py` | 非线性递推（逻辑斯蒂映射、曼德博集） |
| Scene 5 | `scene_05_solving_recurrence.py` | 解递推关系（特征方程法、比内公式） |

### 第二部分：递归——编程中的"问题分解术"

| 场景 | 文件 | 内容 |
|------|------|------|
| Scene 6 | `scene_06_recursion_intro.py` | 递归基础概念（核心要素、无限循环警告） |
| Scene 7 | `scene_07_recursion_examples.py` | 递归算法示例（阶乘、快速幂、快速排序、汉诺塔） |
| Scene 8 | `scene_08_summary.py` | 总结与编程启示 |

### 合并文件

- `all_scenes.py` - 整合所有场景，支持一次性渲染或批量渲染

## 🎨 配色方案

```python
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝 - 主要强调色
    SECONDARY = "#4ECDC4"    # 青绿 - 次要强调色
    ACCENT = "#FF6B6B"       # 警示红 - 警告和重点
    BG = "#1a1a2e"           # 深蓝黑 - 背景
    TEXT = "#FFFFFF"         # 白色 - 文字
    GRAY = "#888888"         # 灰色 - 辅助文字
    RECUR_COLOR = "#F39C12"  # 递推橙 - 递推相关
    RECURSIVE_COLOR = "#9B59B6"  # 递归紫 - 递归相关
    BASE_COLOR = "#2ECC71"   # 基础步骤绿 - 基准情况
    CODE_COLOR = "#3498DB"   # 代码蓝 - 代码相关
    FIBO_COLOR = "#E91E63"   # 斐波那契粉
    CHAOS_COLOR = "#E74C3C"  # 混沌红
    GOLDEN_COLOR = "#FFD700" # 黄金色 - 黄金比例
```

## 🚀 渲染命令

### 单独渲染各场景

```bash
# Scene 1: 开场与概念引入
manim -pqh scene_01_intro.py RecursionIntro

# Scene 2: 递推关系基础
manim -pqh scene_02_recurrence_basics.py RecurrenceBasics

# Scene 3: 线性递推与伪随机数
manim -pqh scene_03_linear_recurrence.py LinearRecurrence

# Scene 4: 非线性递推
manim -pqh scene_04_nonlinear_recurrence.py NonlinearRecurrence

# Scene 5: 解递推关系
manim -pqh scene_05_solving_recurrence.py SolvingRecurrence

# Scene 6: 递归基础概念
manim -pqh scene_06_recursion_intro.py RecursionBasics

# Scene 7: 递归算法示例
manim -pqh scene_07_recursion_examples.py RecursionExamples

# Scene 8: 总结与启示
manim -pqh scene_08_summary.py RecursionSummary
```

### 渲染完整视频

```bash
# 高质量渲染
manim -pqh all_scenes.py RecursionAndRecurrence

# 低质量预览
manim -pql all_scenes.py RecursionAndRecurrence
```

### 渲染选项说明

| 选项 | 说明 |
|------|------|
| `-p` | 渲染后自动播放 |
| `-q l/m/h/k` | 质量：low(480p)/medium(720p)/high(1080p)/4k |
| `-f` | 显示输出文件路径 |
| `--format gif` | 输出 GIF 格式 |

## 📐 核心数学公式

### 递推关系

```
等差数列：aₙ = aₙ₋₁ + d
等比数列：aₙ = r × aₙ₋₁
斐波那契：aₙ = aₙ₋₁ + aₙ₋₂
```

### 线性同余生成器 (LCG)

```
xₙ₊₁ = (a × xₙ + b) mod c
```

### 逻辑斯蒂映射

```
xₙ₊₁ = r × xₙ × (1 - xₙ)
```

### 曼德博集

```
zₙ₊₁ = zₙ² + c
```

### 比内公式（斐波那契直接公式）

```
Fₙ = (φⁿ - ψⁿ) / √5

其中：
φ = (1 + √5) / 2 ≈ 1.618 （黄金比例）
ψ = (1 - √5) / 2 ≈ -0.618
```

### 汉诺塔移动次数

```
Mₙ = 2Mₙ₋₁ + 1
Mₙ = 2ⁿ - 1
```

## 📁 项目结构

```
recursion_and_recurrence/
├── README.md                          # 项目文档
├── scenes.md                          # 场景规划文档
├── scene_01_intro.py                  # 开场与概念引入
├── scene_02_recurrence_basics.py      # 递推关系基础
├── scene_03_linear_recurrence.py      # 线性递推
├── scene_04_nonlinear_recurrence.py   # 非线性递推
├── scene_05_solving_recurrence.py     # 解递推关系
├── scene_06_recursion_intro.py        # 递归基础
├── scene_07_recursion_examples.py     # 递归算法示例
├── scene_08_summary.py                # 总结与启示
└── all_scenes.py                      # 合并文件
```

## 🎯 教学目标

通过本章学习，观众将能够：

1. **理解递推与递归的关系** - 它们是解决问题的两种互补视角
2. **掌握递推关系的基本形式** - 等差、等比、斐波那契数列
3. **了解递推的实际应用** - 伪随机数生成、混沌理论
4. **学会求解递推关系** - 特征方程法和比内公式
5. **掌握递归的核心要素** - 基准情况和递归情况
6. **理解经典递归算法** - 阶乘、快速幂、快速排序、汉诺塔
7. **认识递归效率问题** - 重复计算与优化方法

## 🔧 技术要点

### 动画设计原则

1. **避免动画重叠** - 使用 `self.wait()` 确保动画顺序执行
2. **清理场景** - 使用 `clear_scene()` 函数在场景切换时清除元素
3. **分步展示** - 复杂概念分解为多个小动画
4. **颜色编码** - 使用一致的配色方案区分不同概念

### 手机屏幕优化

- 字体大小适中（标题 26-32，正文 16-20）
- 元素间距合理
- 避免过于密集的布局

## 📚 参考资料

- 《编程中的数学》第六章
- [Manim 官方文档](https://docs.manim.community/)
- 混沌理论与逻辑斯蒂映射
- 斐波那契数列与黄金比例

## 🤝 贡献

欢迎提出改进建议和 Pull Request！

---

*Created with Manim Community Edition*
