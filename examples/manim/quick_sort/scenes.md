# 快速排序教学视频 - 场景设计

## Overview
- **Topic**: 快速排序 (Quick Sort) 算法
- **Hook**: "为什么快速排序是实践中最常用的排序算法？它的秘密是什么？"
- **Target Audience**: 有基本编程概念的学生/初学者
- **Estimated Length**: 8-10 分钟
- **Key Insight**: 分治思想 + 巧妙的分区策略 = 平均 O(n log n) 的高效排序

## Narrative Arc
从一个混乱的数组开始，提出"如何高效排序"的问题。通过分治法的思想引入，展示 Pivot（基准元素）的作用，详细演示分区过程，最后通过递归完成整个排序。让观众理解"化大为小"的智慧。

---

## Scene 1: 开场引入
**Duration**: ~30 秒
**Purpose**: 吸引注意力，提出问题

### Visual Elements
- 一组乱序的数字柱状图
- 标题动画
- 问号效果

### Content
展示一组乱序数据 [5, 2, 8, 1, 9, 3, 7, 4, 6]，提问："如何高效地把这些数字排好序？"

### Narration Notes
语气：好奇、引导思考
"今天我们来学习一个非常巧妙的算法——快速排序"

### Technical Notes
- Rectangle 创建柱状图
- Text 显示标题
- FadeIn/Write 动画

---

## Scene 2: 分治思想介绍
**Duration**: ~45 秒
**Purpose**: 建立核心概念

### Visual Elements
- "分治法" 大标题
- 三步骤图解：分解 → 解决 → 合并
- 箭头连接动画

### Content
介绍分治法核心：把大问题分成小问题，小问题更容易解决。

### Narration Notes
"快速排序的核心是分治法——Divide and Conquer"

### Technical Notes
- VGroup 组织步骤
- Arrow 表示关系
- Transform 动画

---

## Scene 3: Pivot 概念
**Duration**: ~60 秒
**Purpose**: 介绍基准元素

### Visual Elements
- 数组柱状图
- Pivot 高亮（橙色）
- 小于/大于分区示意

### Content
1. 选择最后一个元素作为 Pivot
2. 解释 Pivot 的目标：找到它在排序后的正确位置
3. 比 Pivot 小的放左边，大的放右边

### Narration Notes
"Pivot 就像裁判，决定每个元素站左边还是右边"

### Technical Notes
- Indicate() 高亮
- 颜色编码：ORANGE=Pivot, BLUE=小于, RED=大于

---

## Scene 4: 分区过程详解
**Duration**: ~120 秒
**Purpose**: 核心算法演示

### Visual Elements
- 数组 [5, 2, 8, 1, 9, 3, 7, 4, 6]
- 两个指针：i（红色）和 j（蓝色）
- 伪代码同步显示
- 交换动画

### Content
逐步演示分区过程：
1. i = -1 表示小于区边界
2. j 遍历每个元素
3. 若 arr[j] < pivot: i++, 交换
4. 最后将 Pivot 放到正确位置

### Narration Notes
耐心解释每一步，强调为什么要交换

### Technical Notes
- Arrow 指针
- swap_bars 动画
- 伪代码框

---

## Scene 5: 递归魔力
**Duration**: ~60 秒
**Purpose**: 展示递归完成排序

### Visual Elements
- 分区后的数组
- 递归树示意图
- 逐层展开动画

### Content
1. Pivot 已就位
2. 对左子数组递归快排
3. 对右子数组递归快排
4. 终止条件：数组长度 ≤ 1

### Narration Notes
"递归的美妙：同样的策略不断重复"

### Technical Notes
- 递归树用 Line + Text
- SurroundingRectangle 框子数组

---

## Scene 6: 完整演示
**Duration**: ~90 秒
**Purpose**: 从头到尾看一遍

### Visual Elements
- 完整数组
- 递归层级指示
- 已排序元素标记（绿色）

### Content
以适中速度演示完整的快速排序过程

### Narration Notes
简洁旁白，让动画说话

### Technical Notes
- 递归函数可视化
- 颜色过渡动画

---

## Scene 7: 复杂度分析
**Duration**: ~60 秒
**Purpose**: 理解效率

### Visual Elements
- O(n²) vs O(n log n) 曲线对比
- 最好/平均/最坏情况表格

### Content
- 最好：每次对半分 → O(n log n)
- 平均：O(n log n)
- 最坏：已排序数组 → O(n²)

### Narration Notes
"在大多数情况下，快速排序真的很快！"

### Technical Notes
- Axes + Plot 绘图
- Table 或 VGroup 表格

---

## Scene 8: 总结
**Duration**: ~30 秒
**Purpose**: 回顾要点

### Visual Elements
- 三步总结：选 Pivot → 分区 → 递归
- 复杂度框
- 感谢语

### Content
回顾快排核心三步，强调分治思想的价值

### Narration Notes
"分治思想是解决复杂问题的钥匙"

---

## Color Palette
- Primary: BLUE (#58C4DD) - 默认元素、小于区
- Secondary: GREEN (#83C167) - 已排序元素
- Accent: ORANGE (#FFA500) - Pivot
- Highlight: YELLOW (#FFFF00) - 当前操作
- Warning: RED (#FF6666) - 大于区、指针
- Background: #1C1C1C

## Mathematical Content
- 时间复杂度：O(n log n) 平均，O(n²) 最坏
- 空间复杂度：O(log n) 递归栈
- 递推公式：T(n) = 2T(n/2) + O(n)

## Implementation Order
1. quick_sort.py - 主场景文件
2. 分场景测试
3. 完整渲染
