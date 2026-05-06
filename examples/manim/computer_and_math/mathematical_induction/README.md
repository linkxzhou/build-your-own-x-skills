# 数学归纳法 - Manim 动画项目

本项目是《编程中的数学》系列第五章的可视化教程，使用 Manim 动画库创建，介绍数学归纳法这个强大的证明和推理方法，以及它在编程中的重要应用。

## 📁 项目结构

```
mathematical_induction/
├── README.md                    # 项目说明文档
├── scenes.md                    # 场景规划文档
├── scene_01_intro.py            # Scene 1: 数学归纳法引入（多米诺骨牌模型）
├── scene_02_weak_induction.py   # Scene 2: 弱归纳法（求和公式示例）
├── scene_03_strong_induction.py # Scene 3: 强归纳法（鸡块问题）
├── scene_04_pitfalls.py         # Scene 4: 归纳法的陷阱
├── scene_05_loop_invariant.py   # Scene 5: 循环不变量
├── scene_06_algorithms.py       # Scene 6: 算法示例
├── scene_07_summary.py          # Scene 7: 总结与启示
└── all_scenes.py                # 完整视频合并文件
```

## 🎬 场景概览

### Scene 1: 数学归纳法引入
- **多米诺骨牌模型**：直观展示归纳法的核心思想
- 基础步骤：推倒第一张骨牌
- 归纳步骤：每张骨牌推倒下一张
- 映射到数学表达 P(n)

### Scene 2: 弱归纳法
- 弱归纳法的标准步骤
- **经典例子**：求和公式 1+2+...+n = n(n+1)/2
- 完整的证明推导过程

### Scene 3: 强归纳法
- 弱归纳 vs 强归纳的区别
- **鸡块问题**：6块、9块、20块装，从44开始所有数量都能买到
- 强归纳法的适用场景

### Scene 4: 归纳法的陷阱
- **陷阱一**：忘记基础步骤（前n个偶数和是奇数？）
- **陷阱二**：逆转蕴含方向
- **陷阱三**："所有马都同色"诡辩

### Scene 5: 循环不变量
- 循环不变量的定义
- **三步证明法**：初始化、保持、终止
- 求和循环示例动态演示

### Scene 6: 算法示例
- **冒泡排序**：不变量 - 第k轮后最大的k个元素已到位
- **二分查找**：不变量 - 目标一定在当前区间内
- 算法正确性证明框架

### Scene 7: 总结与启示
- 知识回顾
- **编程启示**：递归与归纳、循环不变量、代码正确性
- 结语：从"能用"到"正确"

## 🎨 配色方案

```python
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑背景
    DOMINO_COLOR = "#F39C12" # 多米诺橙
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    INDUCT_COLOR = "#9B59B6" # 归纳步骤紫
    LOOP_COLOR = "#E74C3C"   # 循环红
    CODE_COLOR = "#3498DB"   # 代码蓝
    STRONG_COLOR = "#E91E63" # 强归纳粉
```

## 🚀 渲染命令

### 渲染单独场景

```bash
# Scene 1: 数学归纳法引入
manim -pqh scene_01_intro.py InductionIntro

# Scene 2: 弱归纳法
manim -pqh scene_02_weak_induction.py WeakInduction

# Scene 3: 强归纳法
manim -pqh scene_03_strong_induction.py StrongInduction

# Scene 4: 归纳法的陷阱
manim -pqh scene_04_pitfalls.py InductionPitfalls

# Scene 5: 循环不变量
manim -pqh scene_05_loop_invariant.py LoopInvariant

# Scene 6: 算法示例
manim -pqh scene_06_algorithms.py AlgorithmExamples

# Scene 7: 总结与启示
manim -pqh scene_07_summary.py InductionSummary
```

### 渲染完整视频

```bash
manim -pqh all_scenes.py MathematicalInduction
```

### 渲染选项说明

- `-p`: 渲染后自动预览
- `-q`: 质量设置
  - `-ql`: 低质量（480p，快速预览）
  - `-qm`: 中等质量（720p）
  - `-qh`: 高质量（1080p）
  - `-qk`: 4K质量
- `-h`: 高质量的简写

## 📱 屏幕适配

本项目针对竖屏/手机屏幕优化：
- 字体大小适当放大
- 元素垂直排列为主
- 标题：28-32pt
- 正文：16-20pt
- 适当留白

## 🛠️ 环境要求

- Python 3.8+
- Manim Community Edition
- LaTeX 发行版（如 TeX Live 或 MiKTeX）

### 安装 Manim

```bash
pip install manim
```

## 📝 注意事项

1. **中文字体**：确保系统安装了中文字体，Manim 的 Text 类会自动使用
2. **LaTeX 中文**：避免在 MathTex 中使用 `\text{中文}`，会导致编译错误
3. **动画时长**：注意控制每个场景的时长，避免过长
4. **元素重叠**：使用 `clear_scene()` 清理场景，避免动画重叠

## 🔗 相关资源

- [Manim Community 文档](https://docs.manim.community/)
- [《编程中的数学》系列](../)

## 📖 内容大纲

### 核心概念

1. **数学归纳法**
   - 基础步骤（Base Case）：证明 P(1) 成立
   - 归纳步骤（Inductive Step）：P(m) → P(m+1)

2. **弱归纳 vs 强归纳**
   - 弱归纳：只假设 P(m)
   - 强归纳：假设 P(1), P(2), ..., P(m)

3. **循环不变量**
   - 初始化：循环前成立
   - 保持：每次迭代后仍成立
   - 终止：循环结束时目标达成

### 编程启示

- 递归与归纳是"双胞胎"
- 循环不变量提升代码质量
- 从"大概能运行"到"逻辑保证正确"

## 📅 版本历史

- v1.0.0 (2026-01-31): 初始版本，完成所有7个场景
