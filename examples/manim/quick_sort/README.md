# 快速排序教学视频

基于 Manim 的快速排序算法教学动画，详细展示快排的核心思想和实现过程。

## 项目结构

```
quick_sort/
├── README.md           # 本文档
├── scenes.md           # 场景设计文档
└── quick_sort.py       # Manim 动画源码
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
cd /path/to/quick_sort

# 低质量预览（快速渲染）
manim -pql quick_sort.py QuickSortTutorial

# 中等质量
manim -pqm quick_sort.py QuickSortTutorial

# 高质量渲染
manim -pqh quick_sort.py QuickSortTutorial

# 4K 渲染
manim -pqk quick_sort.py QuickSortTutorial
```

### 参数说明

| 参数 | 说明 |
|------|------|
| `-p` | 渲染完成后自动播放 |
| `-q` | 质量等级：`l`(低), `m`(中), `h`(高), `k`(4K) |
| `-l` | 等同于 `-ql` |

## 视频内容

共 8 个场景，时长约 8-10 分钟：

| 场景 | 内容 | 时长 |
|------|------|------|
| 1. 开场引入 | 标题、问题提出 | ~30秒 |
| 2. 分治思想 | Divide & Conquer 介绍 | ~45秒 |
| 3. Pivot 概念 | 基准元素的作用 | ~60秒 |
| 4. 分区详解 | Partition 过程 + 伪代码 | ~120秒 |
| 5. 递归演示 | 递归树、终止条件 | ~60秒 |
| 6. 完整排序 | 从头到尾排序演示 | ~90秒 |
| 7. 复杂度分析 | O(n²) vs O(n log n) | ~60秒 |
| 8. 总结 | 核心三步回顾 | ~30秒 |

## 教学特点

### 可视化设计
- **柱状图**：直观展示数组元素
- **颜色编码**：
  - 🔵 蓝色：默认/小于 Pivot
  - 🟠 橙色：Pivot
  - 🔴 红色：大于 Pivot
  - 🟢 绿色：已排序
  - 🟡 黄色：当前操作

### 动画特点
- 指针动画同步显示 i 和 j 的移动
- 伪代码与动画同步
- 交换操作有明确的视觉反馈
- 递归过程可视化

## 输出文件

渲染完成后，视频文件位于：
```
media/videos/quick_sort/[质量]/QuickSortTutorial.mp4
```

## 自定义修改

### 修改数据
在 `quick_sort.py` 中找到：
```python
values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
```
替换为你想要的数组。

### 调整速度
修改 `run_time` 参数控制动画速度。

### 修改颜色
在文件顶部的颜色常量区域修改：
```python
PIVOT_COLOR = ORANGE
SMALLER_COLOR = BLUE_C
LARGER_COLOR = RED_C
SORTED_COLOR = GREEN
```

## 相关资源

- [Manim 官方文档](https://docs.manim.community/)
- [快速排序 - Wikipedia](https://zh.wikipedia.org/wiki/快速排序)

## 许可证

MIT License
