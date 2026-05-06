"""
数学归纳法 - Scene 6: 算法示例
通过冒泡排序和二分查找展示循环不变量的应用

渲染命令: manim -pqh scene_06_algorithms.py AlgorithmExamples
"""

from manim import *
import numpy as np


# ========== 配色方案 ==========
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    DOMINO_COLOR = "#F39C12" # 多米诺橙
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    INDUCT_COLOR = "#9B59B6" # 归纳步骤紫
    LOOP_COLOR = "#E74C3C"   # 循环红
    CODE_COLOR = "#3498DB"   # 代码蓝
    SORTED_COLOR = "#27AE60" # 已排序绿
    ACTIVE_COLOR = "#F39C12" # 活跃橙
    TARGET_COLOR = "#E91E63" # 目标粉


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


def create_array_element(value, color=Colors.PRIMARY, width=0.7, height=0.7):
    """创建数组元素"""
    box = Square(side_length=width)
    box.set_stroke(color, width=2)
    box.set_fill(color, opacity=0.3)
    
    label = Text(str(value), font_size=20, color=Colors.TEXT)
    label.move_to(box.get_center())
    
    return VGroup(box, label)


def create_array_visualization(values, colors=None):
    """创建数组可视化"""
    if colors is None:
        colors = [Colors.PRIMARY] * len(values)
    
    elements = VGroup()
    for i, (val, col) in enumerate(zip(values, colors)):
        elem = create_array_element(val, col)
        elements.add(elem)
    
    elements.arrange(RIGHT, buff=0.1)
    return elements


# ========== Scene 6: 算法示例 ==========
class AlgorithmExamples(Scene):
    """算法正确性证明示例"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.bubble_sort_example()
        self.binary_search_example()
        self.proof_framework()
        
        clear_scene(self)
    
    def bubble_sort_example(self):
        """冒泡排序示例"""
        section_title = Text("算法示例：冒泡排序", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 初始数组
        values = [5, 2, 8, 1, 9]
        array = create_array_visualization(values)
        array.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 索引标签
        indices = VGroup()
        for i in range(len(values)):
            idx = Text(str(i), font_size=12, color=Colors.GRAY)
            idx.next_to(array[i], DOWN, buff=0.1)
            indices.add(idx)
        
        self.play(FadeIn(array), FadeIn(indices))
        self.wait(0.5)
        
        # 不变量说明
        invariant = VGroup(
            Text("循环不变量：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("第 k 轮后，最大的 k 个元素已在正确位置", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        invariant.next_to(indices, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(invariant))
        
        # 动画演示第一轮冒泡
        round_label = Text("第 1 轮：", font_size=16, color=Colors.ACTIVE_COLOR)
        round_label.next_to(invariant, DOWN, buff=0.3).align_to(invariant, LEFT)
        
        self.play(FadeIn(round_label))
        
        # 冒泡过程（简化展示）
        current_values = values.copy()
        
        # 比较 5,2 -> 交换
        self.play(
            array[0][0].animate.set_stroke(Colors.ACTIVE_COLOR, width=3),
            array[1][0].animate.set_stroke(Colors.ACTIVE_COLOR, width=3),
        )
        # 交换动画
        self.play(
            array[0].animate.shift(RIGHT * 0.8),
            array[1].animate.shift(LEFT * 0.8),
            run_time=0.5
        )
        array[0], array[1] = array[1], array[0]
        current_values[0], current_values[1] = current_values[1], current_values[0]
        
        self.play(
            array[0][0].animate.set_stroke(Colors.PRIMARY, width=2),
            array[1][0].animate.set_stroke(Colors.PRIMARY, width=2),
        )
        
        # 跳过中间步骤，直接展示第一轮结束
        self.wait(0.3)
        
        # 第一轮结束状态
        round1_result = VGroup(
            Text("第 1 轮后：", font_size=14, color=Colors.GRAY),
            Text("[2, 5, 1, 8, 9]", font_size=14, color=Colors.TEXT),
            Text("→ 9 已到位", font_size=14, color=Colors.SORTED_COLOR),
        ).arrange(RIGHT, buff=0.1)
        round1_result.next_to(round_label, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        # 标记最后一个元素为已排序
        self.play(
            array[4][0].animate.set_stroke(Colors.SORTED_COLOR, width=3),
            array[4][0].animate.set_fill(Colors.SORTED_COLOR, opacity=0.4),
            FadeIn(round1_result)
        )
        self.wait(0.5)
        
        # 后续轮次简化展示
        rounds_summary = VGroup(
            Text("第 2 轮后：[2, 1, 5, 8, 9] → 8, 9 已到位", font_size=14, color=Colors.GRAY),
            Text("第 3 轮后：[1, 2, 5, 8, 9] → 5, 8, 9 已到位", font_size=14, color=Colors.GRAY),
            Text("...", font_size=14, color=Colors.GRAY),
            Text("最终：[1, 2, 5, 8, 9] ✓ 全部有序", font_size=14, color=Colors.SORTED_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        rounds_summary.next_to(round1_result, DOWN, buff=0.2).align_to(round1_result, LEFT)
        
        self.play(FadeIn(rounds_summary))
        self.wait(1.5)
        
        # 归纳证明结构
        self.play(
            FadeOut(array), FadeOut(indices), FadeOut(round_label),
            FadeOut(round1_result), FadeOut(rounds_summary),
            run_time=0.5
        )
        
        proof_title = Text("归纳证明：", font_size=18, color=Colors.SECONDARY)
        proof_title.next_to(invariant, DOWN, buff=0.4).align_to(invariant, LEFT)
        
        self.play(FadeIn(proof_title))
        
        proof_steps = VGroup(
            VGroup(
                Text("① 初始化：", font_size=16, color=Colors.BASE_COLOR),
                Text("0 轮后，0 个元素已到位（平凡成立）", font_size=14, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("② 保持：", font_size=16, color=Colors.INDUCT_COLOR),
                Text("每轮将未排序部分的最大值冒泡到位", font_size=14, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("③ 终止：", font_size=16, color=Colors.LOOP_COLOR),
                Text("n-1 轮后，所有元素有序", font_size=14, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        proof_steps.next_to(proof_title, DOWN, buff=0.15).shift(RIGHT * 0.2)
        
        for step in proof_steps:
            self.play(FadeIn(step, shift=RIGHT * 0.1), run_time=0.5)
        
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(invariant),
            FadeOut(proof_title), FadeOut(proof_steps),
            run_time=0.5
        )
    
    def binary_search_example(self):
        """二分查找示例"""
        section_title = Text("算法示例：二分查找", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 有序数组
        values = [1, 3, 5, 7, 9, 11, 13, 15]
        array = create_array_visualization(values)
        array.scale(0.8)
        array.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 索引标签
        indices = VGroup()
        for i in range(len(values)):
            idx = Text(str(i), font_size=10, color=Colors.GRAY)
            idx.next_to(array[i], DOWN, buff=0.05)
            indices.add(idx)
        
        self.play(FadeIn(array), FadeIn(indices))
        
        # 目标值
        target_label = VGroup(
            Text("查找目标：", font_size=16, color=Colors.TARGET_COLOR),
            Text("7", font_size=20, color=Colors.TARGET_COLOR),
        ).arrange(RIGHT, buff=0.1)
        target_label.next_to(indices, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(target_label))
        
        # 不变量
        invariant = VGroup(
            Text("循环不变量：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("如果目标存在，一定在 [left, right] 区间内", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        invariant.next_to(target_label, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(invariant))
        self.wait(0.5)
        
        # 搜索演示
        search_title = Text("搜索过程：", font_size=16, color=Colors.SECONDARY)
        search_title.next_to(invariant, DOWN, buff=0.3).align_to(invariant, LEFT)
        
        self.play(FadeIn(search_title))
        
        # 第一步：整个区间
        step1 = VGroup(
            Text("Step 1: left=0, right=7, mid=3", font_size=14, color=Colors.ACTIVE_COLOR),
            Text("  arr[3]=7 = target → 找到！", font_size=14, color=Colors.SORTED_COLOR),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        step1.next_to(search_title, DOWN, buff=0.15).shift(RIGHT * 0.2)
        
        # 高亮区间
        left_brace = Brace(VGroup(array[0], array[7]), DOWN, color=Colors.ACTIVE_COLOR)
        left_brace.shift(DOWN * 0.3)
        
        self.play(Create(left_brace))
        
        # 高亮 mid
        self.play(
            array[3][0].animate.set_stroke(Colors.TARGET_COLOR, width=3),
            array[3][0].animate.set_fill(Colors.TARGET_COLOR, opacity=0.5),
        )
        
        self.play(FadeIn(step1))
        self.wait(1)
        
        # 如果目标是 11，展示多步过程
        self.play(
            FadeOut(step1), FadeOut(left_brace),
            array[3][0].animate.set_stroke(Colors.PRIMARY, width=2),
            array[3][0].animate.set_fill(Colors.PRIMARY, opacity=0.3),
        )
        
        target_label2 = VGroup(
            Text("另一个例子，查找：", font_size=14, color=Colors.TARGET_COLOR),
            Text("11", font_size=18, color=Colors.TARGET_COLOR),
        ).arrange(RIGHT, buff=0.1)
        target_label2.next_to(search_title, DOWN, buff=0.15).shift(RIGHT * 0.2)
        
        self.play(Transform(target_label, target_label2))
        
        # Step 1: mid=3, arr[3]=7 < 11, 右半部分
        step1_new = Text("Step 1: mid=3, arr[3]=7 < 11 → 搜索右半 [4,7]", font_size=14, color=Colors.ACTIVE_COLOR)
        step1_new.next_to(target_label2, DOWN, buff=0.2).align_to(target_label2, LEFT)
        
        # 高亮右半部分
        right_highlight = SurroundingRectangle(
            VGroup(array[4], array[5], array[6], array[7]),
            color=Colors.ACTIVE_COLOR, buff=0.05
        )
        
        self.play(FadeIn(step1_new), Create(right_highlight))
        self.wait(0.5)
        
        # Step 2: mid=5, arr[5]=11 = target
        step2_new = Text("Step 2: mid=5, arr[5]=11 = target → 找到！", font_size=14, color=Colors.SORTED_COLOR)
        step2_new.next_to(step1_new, DOWN, buff=0.1).align_to(step1_new, LEFT)
        
        self.play(
            FadeOut(right_highlight),
            array[5][0].animate.set_stroke(Colors.TARGET_COLOR, width=3),
            array[5][0].animate.set_fill(Colors.TARGET_COLOR, opacity=0.5),
            FadeIn(step2_new)
        )
        self.wait(1)
        
        # 关键点
        key_point = VGroup(
            Text("关键：", font_size=16, color=Colors.SECONDARY),
            Text("每次迭代，搜索区间缩小一半，但不变量始终成立", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(step2_new, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(array), FadeOut(indices),
            FadeOut(target_label), FadeOut(invariant),
            FadeOut(search_title), FadeOut(step1_new), FadeOut(step2_new),
            FadeOut(key_point),
            run_time=0.5
        )
    
    def proof_framework(self):
        """算法正确性证明框架"""
        section_title = Text("算法正确性证明框架", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 框架步骤
        framework = VGroup()
        
        step1 = VGroup(
            Text("1. 确定循环不变量", font_size=20, color=Colors.PRIMARY),
            Text("找到循环中始终保持的性质", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        framework.add(step1)
        
        step2 = VGroup(
            Text("2. 初始化验证", font_size=20, color=Colors.BASE_COLOR),
            Text("循环开始前，不变量成立", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        framework.add(step2)
        
        step3 = VGroup(
            Text("3. 保持性验证", font_size=20, color=Colors.INDUCT_COLOR),
            Text("每次迭代后，不变量仍成立（归纳步骤）", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        framework.add(step3)
        
        step4 = VGroup(
            Text("4. 终止性验证", font_size=20, color=Colors.LOOP_COLOR),
            Text("循环终止 + 不变量 → 算法正确", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        framework.add(step4)
        
        framework.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        framework.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for step in framework:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        # 总结
        summary = VGroup(
            Text("核心思想：", font_size=18, color=Colors.SECONDARY),
            Text("用数学归纳法的思想证明程序的正确性", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        summary.next_to(framework, DOWN, buff=0.6).set_x(0)
        
        summary_box = SurroundingRectangle(summary, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(summary), Create(summary_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(framework),
            FadeOut(summary), FadeOut(summary_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_06_algorithms.py AlgorithmExamples
    pass
