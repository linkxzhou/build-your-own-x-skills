# 集合与抽象代数：从基础到无限

本项目使用 Manim 创建教育视频，介绍集合论基础、集合运算、群论入门以及无限的探索。

## 使用的技能

- `manim-composer` - Manim 项目组织和场景规划
- `manimce-best-practices` - Manim Community Edition 最佳实践

## 内容概览

| 场景 | 文件 | 内容 | 时长 |
|------|------|------|------|
| Scene 1 | `scene_01_intro.py` | 开场引入 - 集合的概念 | ~60秒 |
| Scene 2 | `scene_02_representation.py` | 集合的表示方法 | ~90秒 |
| Scene 3 | `scene_03_operations.py` | 集合运算与韦恩图 | ~120秒 |
| Scene 4 | `scene_04_subsets.py` | 子集与幂集 | ~90秒 |
| Scene 5 | `scene_05_laws.py` | 集合定律与德摩根定律 | ~90秒 |
| Scene 6 | `scene_06_groups.py` | 群论入门 | ~120秒 |
| Scene 7 | `scene_07_infinity.py` | 无限的探索 | ~120秒 |
| Scene 8 | `scene_08_summary.py` | 总结与启示 | ~60秒 |
| 完整版 | `all_scenes.py` | 所有场景合并 | ~12-15分钟 |

## 核心概念

### 集合基础
- 集合是确定的、互不相同的元素组成的整体
- 表示方法：列举法 `{1, 2, 3}` 和描述法 `{x | P(x)}`
- 重要数集：N ⊂ Z ⊂ Q ⊂ R ⊂ C

### 集合运算
- **并集** A ∪ B：合并所有元素
- **交集** A ∩ B：提取共有元素
- **差集** A - B：属于A但不属于B
- **对称差** A △ B：只属于其中一个集合

### 幂集定理
- 幂集 P(A) 是集合A的所有子集组成的集合
- n个元素的集合有 2^n 个子集

### 德摩根定律
- (A ∪ B)' = A' ∩ B'
- (A ∩ B)' = A' ∪ B'
- 编程应用：`!(a || b) == (!a && !b)`

### 群论
- 群 (G, ·) 满足四条公理：封闭性、结合律、单位元、逆元
- 例如：整数加法群 (Z, +)，单位元是0，逆元是相反数

### 无限
- 可数无限：可以与N建立一一对应，|N| = |Z| = |Q| = ℵ₀
- 不可数无限：康托尔对角线论证证明 |R| > |N|
- 康托尔定理：|A| < |P(A)|，无限有无穷层级

## 渲染命令

### 单独场景

```bash
# 预览质量 (快速)
manim -pql scene_01_intro.py Scene01Intro
manim -pql scene_02_representation.py Scene02Representation
manim -pql scene_03_operations.py Scene03Operations
manim -pql scene_04_subsets.py Scene04Subsets
manim -pql scene_05_laws.py Scene05Laws
manim -pql scene_06_groups.py Scene06Groups
manim -pql scene_07_infinity.py Scene07Infinity
manim -pql scene_08_summary.py Scene08Summary

# 高质量
manim -pqh scene_01_intro.py Scene01Intro
```

### 完整视频

```bash
# 预览质量
manim -pql all_scenes.py SetsAndAlgebra

# 高质量 (1080p)
manim -pqh all_scenes.py SetsAndAlgebra

# 生产质量 (4K)
manim -pqk all_scenes.py SetsAndAlgebra
```

## 配色方案

| 颜色 | 代码 | 用途 |
|------|------|------|
| 科技蓝 | `#00D4FF` | 主色调、标题、重要元素 |
| 青绿 | `#4ECDC4` | 辅助色、正确结果 |
| 警示红 | `#FF6B6B` | 强调、错误、反例 |
| 集合A | `#E74C3C` | 韦恩图第一个集合 |
| 集合B | `#3498DB` | 韦恩图第二个集合 |
| 交集 | `#9B59B6` | 韦恩图重叠区域 |
| 背景 | `#1a1a2e` | 深蓝黑科技感背景 |
| 文字 | `#FFFFFF` | 主要文字 |
| 灰色 | `#888888` | 说明文字 |

## 项目结构

```
sets_and_algebra/
├── README.md                    # 本文件
├── scenes.md                    # 场景规划文档
├── scene_01_intro.py           # 场景1：开场引入
├── scene_02_representation.py  # 场景2：集合表示
├── scene_03_operations.py      # 场景3：集合运算
├── scene_04_subsets.py         # 场景4：子集与幂集
├── scene_05_laws.py            # 场景5：集合定律
├── scene_06_groups.py          # 场景6：群论入门
├── scene_07_infinity.py        # 场景7：无限探索
├── scene_08_summary.py         # 场景8：总结
└── all_scenes.py               # 完整视频
```

## 依赖

- Python 3.8+
- Manim Community Edition (manim)

```bash
pip install manim
```

## 三个核心启示

1. **集合是编程的基石** - 数组、列表、字典都是集合的变体
2. **抽象是强大的工具** - 群论用同一语言描述时钟、魔方、密码学
3. **理解无限与边界** - 计算机能力有极限，理解可计算性很重要
