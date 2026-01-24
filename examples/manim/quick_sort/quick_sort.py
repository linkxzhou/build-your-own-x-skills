"""
快速排序教学视频 - Manim 动画
一个详细的快速排序算法教学动画

运行方式:
    # 渲染完整视频（低质量预览）
    manim -pql quick_sort.py QuickSortTutorial

    # 高质量渲染
    manim -pqh quick_sort.py QuickSortTutorial

    # 4K 渲染
    manim -pqk quick_sort.py QuickSortTutorial
"""

from manim import *
import numpy as np


# ============ 颜色常量 ============
PIVOT_COLOR = ORANGE
SMALLER_COLOR = BLUE_C
LARGER_COLOR = RED_C
SORTED_COLOR = GREEN
HIGHLIGHT_COLOR = YELLOW
DEFAULT_COLOR = BLUE


class QuickSortTutorial(Scene):
    """
    快速排序完整教学视频
    场景：开场 → 分治思想 → Pivot概念 → 分区详解 → 递归演示 → 完整排序 → 复杂度 → 总结
    """

    def construct(self):
        # 1. 开场引入
        self.intro_scene()

        # 2. 分治思想
        self.divide_conquer_scene()

        # 3. Pivot 概念
        self.pivot_concept_scene()

        # 4. 分区过程详解
        self.partition_scene()

        # 5. 递归演示
        self.recursion_scene()

        # 6. 完整排序演示
        self.full_sort_scene()

        # 7. 复杂度分析
        self.complexity_scene()

        # 8. 总结
        self.summary_scene()

    # ============ 工具方法 ============

    def create_bars(self, values, start_x=-4.5, bar_width=0.5, spacing=0.65,
                    max_height=3.5, y_base=-1.5):
        """创建柱状图"""
        bars = VGroup()
        labels = VGroup()
        max_val = max(values) if values else 1

        for i, val in enumerate(values):
            height = (val / max_val) * max_height
            bar = Rectangle(
                width=bar_width,
                height=height,
                fill_color=DEFAULT_COLOR,
                fill_opacity=0.8,
                stroke_color=WHITE,
                stroke_width=2
            )
            x_pos = start_x + i * spacing
            bar.move_to([x_pos, y_base + height / 2, 0])

            label = Text(str(val), font_size=20, color=WHITE)
            label.next_to(bar, UP, buff=0.1)

            bars.add(bar)
            labels.add(label)

        return bars, labels, values.copy()

    def swap_bars(self, bars, labels, values, i, j, run_time=0.4):
        """交换两个柱子"""
        if i == j:
            return

        pos_i = bars[i].get_center()
        pos_j = bars[j].get_center()

        self.play(
            bars[i].animate.move_to([pos_j[0], pos_i[1], 0]),
            bars[j].animate.move_to([pos_i[0], pos_j[1], 0]),
            labels[i].animate.move_to([pos_j[0], labels[i].get_center()[1], 0]),
            labels[j].animate.move_to([pos_i[0], labels[j].get_center()[1], 0]),
            run_time=run_time
        )

        bars[i], bars[j] = bars[j], bars[i]
        labels[i], labels[j] = labels[j], labels[i]
        values[i], values[j] = values[j], values[i]

    def clear_all(self):
        """清除所有元素"""
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

    # ============ Scene 1: 开场引入 ============

    def intro_scene(self):
        """开场引入"""
        # 主标题
        title = Text("快速排序", font_size=72, color=WHITE)
        subtitle = Text("Quick Sort", font_size=36, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=0.8)
        self.wait(1)

        # 移到顶部
        self.play(
            VGroup(title, subtitle).animate.scale(0.5).to_edge(UP),
            run_time=0.8
        )

        # 展示乱序数组
        values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        bars, labels, vals = self.create_bars(values)

        self.play(FadeIn(bars), FadeIn(labels), run_time=1)

        # 问题
        question = Text("如何高效地将这些数字排序？", font_size=28, color=YELLOW)
        question.to_edge(DOWN, buff=1)
        self.play(Write(question), run_time=1)

        self.wait(1)

        # 暗示
        hint = Text("冒泡排序太慢了... 我们需要更聪明的方法！", font_size=22, color=GRAY)
        hint.next_to(question, DOWN, buff=0.3)
        self.play(FadeIn(hint), run_time=0.8)

        self.wait(1.5)
        self.clear_all()

    # ============ Scene 2: 分治思想 ============

    def divide_conquer_scene(self):
        """分治法介绍"""
        # 标题
        title = Text("核心思想：分治法", font_size=48, color=WHITE)
        english = Text("Divide and Conquer", font_size=28, color=GRAY)
        english.next_to(title, DOWN, buff=0.2)
        title_group = VGroup(title, english).to_edge(UP, buff=0.5)

        self.play(Write(title), FadeIn(english), run_time=1)

        # 三个步骤
        steps = VGroup(
            VGroup(
                Text("1. 分解 (Divide)", font_size=28, color=BLUE),
                Text("把大问题分成小问题", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("2. 解决 (Conquer)", font_size=28, color=GREEN),
                Text("递归解决小问题", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("3. 合并 (Combine)", font_size=28, color=ORANGE),
                Text("组合成最终答案", font_size=20, color=GRAY)
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        steps.next_to(title_group, DOWN, buff=0.6).shift(LEFT * 2)

        for step in steps:
            self.play(FadeIn(step, shift=RIGHT), run_time=0.5)
            self.wait(0.3)

        # 图示
        big = Rectangle(width=4, height=1.2, color=RED, fill_opacity=0.3)
        big.shift(RIGHT * 2.5 + UP * 0.5)
        big_label = Text("大问题", font_size=18).move_to(big)

        self.play(Create(big), Write(big_label), run_time=0.6)

        # 分成小问题
        smalls = VGroup()
        for i, offset in enumerate([-1.2, 0, 1.2]):
            s = Rectangle(width=1.1, height=0.7, color=GREEN, fill_opacity=0.3)
            s.move_to(big.get_center() + DOWN * 1.5 + RIGHT * offset)
            smalls.add(s)

        arrows = VGroup(*[
            Arrow(big.get_bottom(), s.get_top(), buff=0.1, color=YELLOW, stroke_width=2)
            for s in smalls
        ])

        self.play(Create(arrows), run_time=0.5)
        self.play(Create(smalls), run_time=0.6)

        # 要点
        key = Text("快排的精髓：用分区将问题一分为二", font_size=24, color=YELLOW)
        key.to_edge(DOWN, buff=0.6)
        self.play(Write(key), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 3: Pivot 概念 ============

    def pivot_concept_scene(self):
        """Pivot 基准元素概念"""
        title = Text("关键概念：基准元素 (Pivot)", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)

        # 数组
        values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        bars, labels, vals = self.create_bars(values, max_height=3, y_base=-1)
        self.play(FadeIn(bars), FadeIn(labels), run_time=0.6)

        # 索引
        indices = VGroup(*[
            Text(str(i), font_size=14, color=GRAY).next_to(bars[i], DOWN, buff=0.3)
            for i in range(len(vals))
        ])
        self.play(FadeIn(indices), run_time=0.4)

        # 选择 Pivot
        pivot_idx = len(vals) - 1
        pivot_val = vals[pivot_idx]

        pivot_text = Text(f"选择最后一个元素 {pivot_val} 作为 Pivot", font_size=22, color=ORANGE)
        pivot_text.next_to(title, DOWN, buff=0.4)
        self.play(Write(pivot_text), run_time=0.6)

        self.play(
            bars[pivot_idx].animate.set_fill(PIVOT_COLOR),
            Indicate(bars[pivot_idx], color=PIVOT_COLOR),
            run_time=0.6
        )

        # 说明
        explain = VGroup(
            Text("Pivot 的目标:", font_size=20, color=WHITE),
            Text(f"• 找到 {pivot_val} 在排序后的正确位置", font_size=18, color=GRAY),
            Text(f"• 比 {pivot_val} 小的放左边", font_size=18, color=SMALLER_COLOR),
            Text(f"• 比 {pivot_val} 大的放右边", font_size=18, color=LARGER_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        explain.to_edge(LEFT, buff=0.6).shift(DOWN * 0.3)

        for line in explain:
            self.play(FadeIn(line, shift=RIGHT), run_time=0.3)

        self.wait(0.5)

        # 分类展示
        for i in range(len(vals) - 1):
            if vals[i] < pivot_val:
                self.play(bars[i].animate.set_fill(SMALLER_COLOR), run_time=0.15)
            else:
                self.play(bars[i].animate.set_fill(LARGER_COLOR), run_time=0.15)

        # 图例
        legend = VGroup(
            VGroup(
                Rectangle(width=0.4, height=0.4, fill_color=SMALLER_COLOR, fill_opacity=0.8),
                Text(f"< {pivot_val}", font_size=16)
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Rectangle(width=0.4, height=0.4, fill_color=PIVOT_COLOR, fill_opacity=0.8),
                Text("Pivot", font_size=16)
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Rectangle(width=0.4, height=0.4, fill_color=LARGER_COLOR, fill_opacity=0.8),
                Text(f"> {pivot_val}", font_size=16)
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        legend.to_edge(RIGHT, buff=0.5).shift(DOWN * 0.3)
        self.play(FadeIn(legend), run_time=0.5)

        # 类比
        analogy = Text("Pivot 就像裁判，决定每个元素站左边还是右边", font_size=20, color=YELLOW)
        analogy.to_edge(DOWN, buff=0.5)
        self.play(Write(analogy), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 4: 分区过程详解 ============

    def partition_scene(self):
        """分区过程详细演示"""
        title = Text("分区过程详解 (Partition)", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.6)

        # 数组
        values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        bars, labels, vals = self.create_bars(
            values, start_x=-4, bar_width=0.45, spacing=0.6,
            max_height=2.8, y_base=-1
        )
        self.play(FadeIn(bars), FadeIn(labels), run_time=0.5)

        # 索引
        indices = VGroup(*[
            Text(str(i), font_size=12, color=GRAY).next_to(bars[i], DOWN, buff=0.25)
            for i in range(len(vals))
        ])
        self.play(FadeIn(indices), run_time=0.3)

        # Pivot
        pivot_idx = len(vals) - 1
        pivot_val = vals[pivot_idx]
        self.play(bars[pivot_idx].animate.set_fill(PIVOT_COLOR), run_time=0.3)

        pivot_label = Text(f"Pivot = {pivot_val}", font_size=18, color=PIVOT_COLOR)
        pivot_label.next_to(bars[pivot_idx], UP, buff=0.5)
        self.play(FadeIn(pivot_label), run_time=0.3)

        # 伪代码
        code = VGroup(
            Text("partition(arr, low, high):", font_size=14, color=WHITE),
            Text("  pivot = arr[high]", font_size=12, color=GRAY),
            Text("  i = low - 1", font_size=12, color=RED_C),
            Text("  for j = low to high-1:", font_size=12, color=BLUE_C),
            Text("    if arr[j] < pivot:", font_size=12, color=GRAY),
            Text("      i++, swap(arr[i], arr[j])", font_size=12, color=GRAY),
            Text("  swap(arr[i+1], arr[high])", font_size=12, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.06)
        code.to_edge(LEFT, buff=0.3).shift(DOWN * 1.5)
        code_box = SurroundingRectangle(code, color=WHITE, buff=0.1)
        self.play(Create(code_box), Write(code), run_time=1)

        # 指针
        i = -1

        # i 指针（初始在左边界外）
        i_arrow = Arrow(ORIGIN, DOWN * 0.4, color=RED, stroke_width=3)
        i_label = Text("i", font_size=16, color=RED)
        i_arrow.next_to(bars[0], UP, buff=0.7).shift(LEFT * 0.5)
        i_label.next_to(i_arrow, UP, buff=0.08)
        i_group = VGroup(i_arrow, i_label)

        i_info = Text("i = -1", font_size=14, color=RED)
        i_info.to_edge(RIGHT, buff=0.5).shift(UP * 2.5)
        self.play(FadeIn(i_group), FadeIn(i_info), run_time=0.4)

        # j 指针
        j_arrow = Arrow(ORIGIN, DOWN * 0.4, color=BLUE, stroke_width=3)
        j_label = Text("j", font_size=16, color=BLUE)
        j_arrow.next_to(bars[0], UP, buff=0.4)
        j_label.next_to(j_arrow, UP, buff=0.08)
        j_group = VGroup(j_arrow, j_label)
        self.play(FadeIn(j_group), run_time=0.4)

        # 状态文字
        status = Text("", font_size=18)
        status.to_edge(DOWN, buff=0.4)

        # 遍历
        for j in range(len(vals) - 1):
            # 移动 j
            self.play(j_group.animate.next_to(bars[j], UP, buff=0.4), run_time=0.25)

            # 高亮当前
            self.play(bars[j].animate.set_stroke(YELLOW, width=4), run_time=0.15)

            # 比较
            new_status = Text(
                f"arr[{j}]={vals[j]} vs Pivot={pivot_val}",
                font_size=18, color=WHITE
            )
            new_status.to_edge(DOWN, buff=0.4)

            if status.text:
                self.play(Transform(status, new_status), run_time=0.2)
            else:
                status = new_status
                self.play(FadeIn(status), run_time=0.2)

            if vals[j] < pivot_val:
                # 小于 Pivot
                result = Text(f"{vals[j]} < {pivot_val} ✓", font_size=16, color=GREEN)
                result.next_to(status, DOWN, buff=0.1)
                self.play(FadeIn(result), run_time=0.2)

                i += 1
                new_i_info = Text(f"i = {i}", font_size=14, color=RED)
                new_i_info.to_edge(RIGHT, buff=0.5).shift(UP * 2.5)
                self.play(
                    i_group.animate.next_to(bars[i], UP, buff=0.7),
                    Transform(i_info, new_i_info),
                    run_time=0.25
                )

                if i != j:
                    self.swap_bars(bars, labels, vals, i, j, run_time=0.35)

                self.play(
                    bars[i].animate.set_fill(SMALLER_COLOR).set_stroke(WHITE, width=2),
                    run_time=0.15
                )
                self.play(FadeOut(result), run_time=0.1)
            else:
                # 大于等于 Pivot
                result = Text(f"{vals[j]} ≥ {pivot_val} ✗", font_size=16, color=RED_C)
                result.next_to(status, DOWN, buff=0.1)
                self.play(FadeIn(result), run_time=0.2)
                self.play(
                    bars[j].animate.set_fill(LARGER_COLOR).set_stroke(WHITE, width=2),
                    run_time=0.15
                )
                self.play(FadeOut(result), run_time=0.1)

        # 遍历结束
        self.play(FadeOut(status), FadeOut(j_group), run_time=0.3)

        # 将 Pivot 放到正确位置
        final = Text(f"将 Pivot 放到位置 {i + 1}", font_size=20, color=ORANGE)
        final.to_edge(DOWN, buff=0.5)
        self.play(Write(final), run_time=0.6)

        self.swap_bars(bars, labels, vals, i + 1, pivot_idx, run_time=0.5)
        self.play(bars[i + 1].animate.set_fill(SORTED_COLOR), run_time=0.3)

        # 分区标注
        if i + 1 > 0:
            left_brace = Brace(VGroup(*bars[:i + 1]), DOWN, color=SMALLER_COLOR)
            left_text = Text("小于区", font_size=14, color=SMALLER_COLOR)
            left_text.next_to(left_brace, DOWN, buff=0.1)
            self.play(Create(left_brace), FadeIn(left_text), run_time=0.4)

        if i + 2 < len(bars):
            right_brace = Brace(VGroup(*bars[i + 2:]), DOWN, color=LARGER_COLOR)
            right_text = Text("大于区", font_size=14, color=LARGER_COLOR)
            right_text.next_to(right_brace, DOWN, buff=0.1)
            self.play(Create(right_brace), FadeIn(right_text), run_time=0.4)

        conclusion = Text("分区完成！Pivot 已在正确位置", font_size=18, color=YELLOW)
        conclusion.next_to(final, DOWN, buff=0.2)
        self.play(Write(conclusion), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 5: 递归演示 ============

    def recursion_scene(self):
        """递归的魔力"""
        title = Text("递归的魔力", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 分区后结构
        structure = VGroup(
            Text("[小于区]", font_size=26, color=SMALLER_COLOR),
            Text("Pivot", font_size=26, color=SORTED_COLOR),
            Text("[大于区]", font_size=26, color=LARGER_COLOR),
        ).arrange(RIGHT, buff=0.4)
        structure.next_to(title, DOWN, buff=0.5)
        self.play(FadeIn(structure), run_time=0.5)

        # 说明
        explain = VGroup(
            Text("分区后:", font_size=22, color=WHITE),
            Text("• Pivot 已在正确位置 ✓", font_size=18, color=SORTED_COLOR),
            Text("• 对左边子数组递归快排", font_size=18, color=SMALLER_COLOR),
            Text("• 对右边子数组递归快排", font_size=18, color=LARGER_COLOR),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        explain.next_to(structure, DOWN, buff=0.5)

        for line in explain:
            self.play(FadeIn(line, shift=RIGHT), run_time=0.3)

        # 递归树
        tree_title = Text("递归树示意", font_size=20, color=GRAY)
        tree_title.shift(DOWN * 0.8)
        self.play(FadeIn(tree_title), run_time=0.3)

        # Level 0
        root = Rectangle(width=3.5, height=0.5, color=WHITE)
        root.shift(DOWN * 1.4)
        root_text = Text("[5,2,8,1,9,3,7,4,6]", font_size=12)
        root_text.move_to(root)
        self.play(Create(root), Write(root_text), run_time=0.4)

        # Level 1
        left1 = Rectangle(width=1.8, height=0.4, color=SMALLER_COLOR)
        left1.next_to(root, DOWN, buff=0.5).shift(LEFT * 1.3)
        left1_text = Text("[1,2,3,4,5]", font_size=10)
        left1_text.move_to(left1)

        pivot1 = Rectangle(width=0.5, height=0.4, color=SORTED_COLOR)
        pivot1.next_to(root, DOWN, buff=0.5)
        pivot1_text = Text("6", font_size=10)
        pivot1_text.move_to(pivot1)

        right1 = Rectangle(width=1.2, height=0.4, color=LARGER_COLOR)
        right1.next_to(root, DOWN, buff=0.5).shift(RIGHT * 1.3)
        right1_text = Text("[8,9,7]", font_size=10)
        right1_text.move_to(right1)

        lines = VGroup(
            Line(root.get_bottom(), left1.get_top(), color=GRAY),
            Line(root.get_bottom(), pivot1.get_top(), color=GRAY),
            Line(root.get_bottom(), right1.get_top(), color=GRAY),
        )

        self.play(Create(lines), run_time=0.3)
        self.play(
            Create(left1), Write(left1_text),
            Create(pivot1), Write(pivot1_text),
            Create(right1), Write(right1_text),
            run_time=0.5
        )

        # 省略号
        dots = VGroup(
            Text("...", font_size=14, color=GRAY).next_to(left1, DOWN, buff=0.3),
            Text("...", font_size=14, color=GRAY).next_to(right1, DOWN, buff=0.3),
        )
        self.play(FadeIn(dots), run_time=0.3)

        # 终止条件
        base = Text("当子数组长度 ≤ 1 时，已有序，递归结束", font_size=18, color=YELLOW)
        base.to_edge(DOWN, buff=0.5)
        self.play(Write(base), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 6: 完整排序演示 ============

    def full_sort_scene(self):
        """完整快速排序演示"""
        title = Text("完整快速排序演示", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.6)

        values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
        bars, labels, vals = self.create_bars(
            values, start_x=-4, bar_width=0.45, spacing=0.6,
            max_height=2.8, y_base=-1.2
        )
        self.play(FadeIn(bars), FadeIn(labels), run_time=0.5)

        depth_text = Text("递归深度: 0", font_size=16, color=GRAY)
        depth_text.to_edge(RIGHT, buff=0.5).shift(UP * 2.5)
        self.play(FadeIn(depth_text), run_time=0.3)

        def quick_sort_visual(low, high, depth):
            if low >= high:
                return

            # 更新深度
            new_depth = Text(f"递归深度: {depth}", font_size=16, color=GRAY)
            new_depth.to_edge(RIGHT, buff=0.5).shift(UP * 2.5)
            self.play(Transform(depth_text, new_depth), run_time=0.2)

            # 高亮范围
            rect = SurroundingRectangle(
                VGroup(*bars[low:high + 1]), color=YELLOW, buff=0.08
            )
            range_text = Text(f"[{low}:{high}]", font_size=14, color=YELLOW)
            range_text.next_to(rect, UP, buff=0.08)
            self.play(Create(rect), FadeIn(range_text), run_time=0.25)

            # Pivot
            pivot_idx = high
            self.play(bars[pivot_idx].animate.set_fill(PIVOT_COLOR), run_time=0.15)

            # 分区
            i = low - 1
            for j in range(low, high):
                if vals[j] < vals[pivot_idx]:
                    i += 1
                    if i != j:
                        self.swap_bars(bars, labels, vals, i, j, run_time=0.2)
                    self.play(bars[i].animate.set_fill(SMALLER_COLOR), run_time=0.1)
                else:
                    self.play(bars[j].animate.set_fill(LARGER_COLOR), run_time=0.1)

            # Pivot 就位
            final_pos = i + 1
            if final_pos != pivot_idx:
                self.swap_bars(bars, labels, vals, final_pos, pivot_idx, run_time=0.25)
            self.play(bars[final_pos].animate.set_fill(SORTED_COLOR), run_time=0.15)

            self.play(FadeOut(rect), FadeOut(range_text), run_time=0.2)

            # 递归
            quick_sort_visual(low, final_pos - 1, depth + 1)
            quick_sort_visual(final_pos + 1, high, depth + 1)

        quick_sort_visual(0, len(vals) - 1, 0)

        # 全部标记为已排序
        self.play(*[bar.animate.set_fill(SORTED_COLOR) for bar in bars], run_time=0.4)

        complete = Text("排序完成！", font_size=28, color=GREEN)
        complete.next_to(title, DOWN, buff=0.6)
        self.play(Write(complete), run_time=0.5)

        self.wait(2)
        self.clear_all()

    # ============ Scene 7: 复杂度分析 ============

    def complexity_scene(self):
        """时间复杂度分析"""
        title = Text("时间复杂度分析", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 三种情况
        cases = VGroup(
            VGroup(
                Text("最好情况", font_size=24, color=GREEN),
                MathTex(r"O(n \log n)", font_size=28, color=GREEN),
                Text("每次对半分", font_size=16, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("平均情况", font_size=24, color=BLUE),
                MathTex(r"O(n \log n)", font_size=28, color=BLUE),
                Text("随机数据", font_size=16, color=GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("最坏情况", font_size=24, color=RED),
                MathTex(r"O(n^2)", font_size=28, color=RED),
                Text("已排序数组", font_size=16, color=GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1)
        cases.next_to(title, DOWN, buff=0.5)

        for case in cases:
            self.play(FadeIn(case, shift=UP), run_time=0.4)

        # 曲线对比
        axes = Axes(
            x_range=[0, 50, 10],
            y_range=[0, 2500, 500],
            x_length=5.5,
            y_length=2.8,
            axis_config={"include_tip": False},
        )
        axes.shift(DOWN * 1.3)

        x_label = Text("n", font_size=14).next_to(axes, DOWN, buff=0.15)
        y_label = Text("操作数", font_size=14).next_to(axes, LEFT, buff=0.15)
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label), run_time=0.6)

        # O(n²)
        graph_n2 = axes.plot(lambda x: x ** 2, x_range=[0, 50], color=RED)
        label_n2 = MathTex(r"O(n^2)", font_size=18, color=RED)
        label_n2.next_to(graph_n2.get_end(), RIGHT, buff=0.1)

        # O(n log n)
        graph_nlogn = axes.plot(
            lambda x: x * np.log2(x + 1) * 5 if x > 0 else 0,
            x_range=[0, 50], color=GREEN
        )
        label_nlogn = MathTex(r"O(n \log n)", font_size=18, color=GREEN)
        label_nlogn.next_to(graph_nlogn.get_end(), RIGHT, buff=0.1)

        self.play(Create(graph_n2), FadeIn(label_n2), run_time=0.6)
        self.play(Create(graph_nlogn), FadeIn(label_nlogn), run_time=0.6)

        insight = Text("数据量越大，O(n log n) 优势越明显！", font_size=20, color=YELLOW)
        insight.to_edge(DOWN, buff=0.3)
        self.play(Write(insight), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 8: 总结 ============

    def summary_scene(self):
        """总结"""
        title = Text("总结", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 核心三步
        summary = VGroup(
            Text("快速排序三步曲:", font_size=26, color=WHITE),
            VGroup(
                Text("1. 选择 Pivot", font_size=22, color=ORANGE),
                Text("选一个基准元素", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(
                Text("2. 分区 Partition", font_size=22, color=BLUE),
                Text("小的左边，大的右边", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(
                Text("3. 递归", font_size=22, color=GREEN),
                Text("对子数组重复以上步骤", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=0.5).shift(LEFT * 2)

        for item in summary:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.35)

        # 复杂度框
        complexity = VGroup(
            Text("复杂度", font_size=20, color=WHITE),
            Text("时间: O(n log n) 平均", font_size=16, color=GREEN),
            Text("空间: O(log n)", font_size=16, color=BLUE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        complexity.to_edge(RIGHT, buff=1).shift(UP * 0.3)
        box = SurroundingRectangle(complexity, color=WHITE, buff=0.15)
        self.play(Create(box), FadeIn(complexity), run_time=0.5)

        # 核心思想
        key = Text("分治思想是解决复杂问题的钥匙", font_size=22, color=YELLOW)
        key.to_edge(DOWN, buff=1)
        self.play(Write(key), run_time=0.6)

        self.wait(1.5)

        # 感谢
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

        thanks = Text("感谢观看！", font_size=56, color=WHITE)
        self.play(FadeIn(thanks, scale=1.2), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    scene = QuickSortTutorial()
    scene.render()
