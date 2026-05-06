"""
递推与递归 - Scene 7: 递归算法示例
展示阶乘、快速幂、快速排序和汉诺塔等经典递归算法

渲染命令: manim -pqh scene_07_recursion_examples.py RecursionExamples
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
    RECURSIVE_COLOR = "#9B59B6"  # 递归紫
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    CODE_COLOR = "#3498DB"   # 代码蓝
    SORT_COLOR = "#E67E22"   # 排序橙
    HANOI_A = "#E74C3C"      # 汉诺塔A红
    HANOI_B = "#F39C12"      # 汉诺塔B橙
    HANOI_C = "#2ECC71"      # 汉诺塔C绿


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


def create_array_element(value, color=Colors.PRIMARY, size=0.5):
    """创建数组元素"""
    rect = Square(side_length=size)
    rect.set_stroke(color, width=2)
    rect.set_fill(color, opacity=0.3)
    
    label = Text(str(value), font_size=16, color=Colors.TEXT)
    label.move_to(rect.get_center())
    
    return VGroup(rect, label)


def create_disk(width, color):
    """创建汉诺塔圆盘"""
    disk = RoundedRectangle(width=width, height=0.25, corner_radius=0.05)
    disk.set_stroke(color, width=1)
    disk.set_fill(color, opacity=0.8)
    return disk


# ========== Scene 7: 递归算法示例 ==========
class RecursionExamples(Scene):
    """递归算法示例"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.factorial_example()
        self.power_example()
        self.quicksort_example()
        self.hanoi_example()
        
        clear_scene(self)
    
    def factorial_example(self):
        """阶乘示例"""
        section_title = Text("示例一：阶乘", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 数学定义
        math_def = VGroup(
            Text("数学定义：", font_size=18, color=Colors.PRIMARY),
            MathTex(r"n! = n \times (n-1)!", font_size=24, color=Colors.RECURSIVE_COLOR),
            MathTex(r"1! = 1", font_size=20, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        math_def.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(math_def))
        self.wait(0.5)
        
        # 调用栈可视化
        self.play(FadeOut(math_def))
        
        stack_title = Text("计算 4! 的调用过程：", font_size=18, color=Colors.SECONDARY)
        stack_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(stack_title))
        
        # 展开阶段
        expand_title = Text("展开 ↓", font_size=14, color=Colors.RECURSIVE_COLOR)
        expand_title.next_to(stack_title, DOWN, buff=0.3).shift(LEFT * 1.5)
        
        expand_calls = VGroup(
            Text("4! = 4 × 3!", font_size=16, color=Colors.TEXT),
            Text("3! = 3 × 2!", font_size=16, color=Colors.TEXT),
            Text("2! = 2 × 1!", font_size=16, color=Colors.TEXT),
            Text("1! = 1  ✓", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        expand_calls.next_to(expand_title, DOWN, buff=0.15)
        
        self.play(FadeIn(expand_title))
        for call in expand_calls:
            self.play(FadeIn(call, shift=DOWN * 0.1), run_time=0.3)
        
        self.wait(0.5)
        
        # 回归阶段
        return_title = Text("回归 ↑", font_size=14, color=Colors.BASE_COLOR)
        return_title.next_to(expand_title, RIGHT, buff=2.0)
        
        return_calls = VGroup(
            Text("1! = 1", font_size=16, color=Colors.BASE_COLOR),
            Text("2! = 2 × 1 = 2", font_size=16, color=Colors.TEXT),
            Text("3! = 3 × 2 = 6", font_size=16, color=Colors.TEXT),
            Text("4! = 4 × 6 = 24", font_size=16, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        return_calls.next_to(return_title, DOWN, buff=0.15)
        
        self.play(FadeIn(return_title))
        for call in return_calls:
            self.play(FadeIn(call, shift=UP * 0.1), run_time=0.3)
        
        # 结果
        result = VGroup(
            Text("结果：", font_size=18, color=Colors.PRIMARY),
            Text("4! = 24", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        result.next_to(return_calls, DOWN, buff=0.4).set_x(0)
        
        result_box = SurroundingRectangle(result, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(result), Create(result_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(stack_title),
            FadeOut(expand_title), FadeOut(expand_calls),
            FadeOut(return_title), FadeOut(return_calls),
            FadeOut(result), FadeOut(result_box),
            run_time=0.5
        )
    
    def power_example(self):
        """快速幂示例"""
        section_title = Text("示例二：快速幂", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题
        problem = VGroup(
            Text("问题：", font_size=18, color=Colors.PRIMARY),
            Text("计算 b^n", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        problem.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(problem))
        
        # 朴素方法
        naive = VGroup(
            Text("朴素方法：", font_size=16, color=Colors.ACCENT),
            Text("乘 n 次", font_size=14, color=Colors.GRAY),
            Text("时间复杂度 O(n)", font_size=14, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        naive.next_to(problem, DOWN, buff=0.3).align_to(problem, LEFT)
        
        self.play(FadeIn(naive))
        self.wait(0.5)
        
        # 快速幂方法
        fast = VGroup(
            Text("快速幂：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"b^n = (b^{n/2})^2", font_size=20, color=Colors.RECURSIVE_COLOR),
            Text("（n 是偶数时）", font_size=14, color=Colors.GRAY),
            Text("问题规模减半！", font_size=14, color=Colors.SECONDARY),
            Text("时间复杂度 O(log n)", font_size=14, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        fast.next_to(naive, DOWN, buff=0.3).align_to(naive, LEFT)
        
        self.play(FadeIn(fast))
        self.wait(1)
        
        # 示例
        self.play(FadeOut(naive), FadeOut(fast))
        
        example_title = Text("示例：计算 2⁸", font_size=18, color=Colors.SECONDARY)
        example_title.next_to(problem, DOWN, buff=0.4).align_to(problem, LEFT)
        
        self.play(FadeIn(example_title))
        
        steps = VGroup(
            Text("2⁸ = (2⁴)²", font_size=16, color=Colors.TEXT),
            Text("2⁴ = (2²)²", font_size=16, color=Colors.TEXT),
            Text("2² = (2¹)²", font_size=16, color=Colors.TEXT),
            Text("2¹ = 2  (基准)", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        steps.next_to(example_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(0.5)
        
        # 回归
        returns = VGroup(
            Text("2¹ = 2", font_size=16, color=Colors.BASE_COLOR),
            Text("2² = 2² = 4", font_size=16, color=Colors.TEXT),
            Text("2⁴ = 4² = 16", font_size=16, color=Colors.TEXT),
            Text("2⁸ = 16² = 256 ✓", font_size=16, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        returns.next_to(steps, RIGHT, buff=0.8)
        
        for ret in returns:
            self.play(FadeIn(ret, shift=LEFT * 0.1), run_time=0.4)
        
        # 效率对比
        compare = VGroup(
            Text("对比：", font_size=14, color=Colors.GRAY),
            Text("朴素 8 次乘法 vs 快速幂 3 次", font_size=14, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        compare.next_to(returns, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(compare))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(problem),
            FadeOut(example_title), FadeOut(steps), FadeOut(returns),
            FadeOut(compare),
            run_time=0.5
        )
    
    def quicksort_example(self):
        """快速排序示例"""
        section_title = Text("示例三：快速排序", font_size=26, color=Colors.SORT_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 算法步骤
        steps = VGroup(
            Text("① 选择一个基准值 (pivot)", font_size=16, color=Colors.SORT_COLOR),
            Text("② 小于基准的放左边，大于的放右边", font_size=16, color=Colors.TEXT),
            Text("③ 递归排序左右两边", font_size=16, color=Colors.RECURSIVE_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        steps.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for step in steps:
            self.play(FadeIn(step, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(0.5)
        
        # 可视化
        self.play(FadeOut(steps))
        
        demo_title = Text("演示：排序 [3, 1, 4, 1, 5, 9, 2, 6]", font_size=16, color=Colors.SECONDARY)
        demo_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(demo_title))
        
        # 初始数组
        values = [3, 1, 4, 1, 5, 9, 2, 6]
        arr = VGroup()
        for val in values:
            elem = create_array_element(val, Colors.PRIMARY, 0.45)
            arr.add(elem)
        arr.arrange(RIGHT, buff=0.05)
        arr.next_to(demo_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(arr))
        
        # 选择基准（第一个元素）
        pivot_label = Text("基准=3", font_size=12, color=Colors.SORT_COLOR)
        pivot_label.next_to(arr[0], UP, buff=0.1)
        
        self.play(
            arr[0][0].animate.set_stroke(Colors.SORT_COLOR, width=3),
            FadeIn(pivot_label)
        )
        self.wait(0.3)
        
        # 分区结果（简化展示）
        partition_label = Text("分区后：", font_size=14, color=Colors.GRAY)
        partition_label.next_to(arr, DOWN, buff=0.3).align_to(arr, LEFT)
        
        # 小于3的：[1, 1, 2]，等于3的：[3]，大于3的：[4, 5, 9, 6]
        left_vals = [1, 1, 2]
        pivot_val = [3]
        right_vals = [4, 5, 9, 6]
        
        left_arr = VGroup()
        for val in left_vals:
            elem = create_array_element(val, Colors.BASE_COLOR, 0.45)
            left_arr.add(elem)
        left_arr.arrange(RIGHT, buff=0.05)
        
        pivot_elem = create_array_element(3, Colors.SORT_COLOR, 0.45)
        
        right_arr = VGroup()
        for val in right_vals:
            elem = create_array_element(val, Colors.ACCENT, 0.45)
            right_arr.add(elem)
        right_arr.arrange(RIGHT, buff=0.05)
        
        partitioned = VGroup(left_arr, pivot_elem, right_arr).arrange(RIGHT, buff=0.15)
        partitioned.next_to(partition_label, DOWN, buff=0.1).set_x(0)
        
        self.play(
            FadeOut(pivot_label),
            FadeOut(arr),
            FadeIn(partition_label),
            FadeIn(partitioned)
        )
        
        # 标签
        left_label = Text("< 3", font_size=10, color=Colors.BASE_COLOR)
        left_label.next_to(left_arr, DOWN, buff=0.05)
        
        right_label = Text("> 3", font_size=10, color=Colors.ACCENT)
        right_label.next_to(right_arr, DOWN, buff=0.05)
        
        self.play(FadeIn(left_label), FadeIn(right_label))
        self.wait(0.5)
        
        # 递归说明
        recurse = VGroup(
            Text("递归排序左边 →", font_size=12, color=Colors.BASE_COLOR),
            Text("[1, 1, 2]", font_size=12, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        recurse.next_to(partitioned, DOWN, buff=0.4).shift(LEFT * 1)
        
        recurse2 = VGroup(
            Text("递归排序右边 →", font_size=12, color=Colors.ACCENT),
            Text("[4, 5, 6, 9]", font_size=12, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        recurse2.next_to(recurse, DOWN, buff=0.1).align_to(recurse, LEFT)
        
        self.play(FadeIn(recurse), FadeIn(recurse2))
        
        # 最终结果
        final = VGroup(
            Text("最终：", font_size=14, color=Colors.SECONDARY),
            Text("[1, 1, 2, 3, 4, 5, 6, 9]", font_size=14, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        final.next_to(recurse2, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(final))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(demo_title),
            FadeOut(partition_label), FadeOut(partitioned),
            FadeOut(left_label), FadeOut(right_label),
            FadeOut(recurse), FadeOut(recurse2), FadeOut(final),
            run_time=0.5
        )
    
    def hanoi_example(self):
        """汉诺塔示例"""
        section_title = Text("示例四：汉诺塔", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题描述
        problem = VGroup(
            Text("问题：", font_size=16, color=Colors.PRIMARY),
            Text("将 n 个盘子从 A 移到 C", font_size=16, color=Colors.TEXT),
            Text("规则：大盘子不能放在小盘子上", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        problem.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(problem))
        
        # 递归思路
        strategy = VGroup(
            Text("递归分解：", font_size=16, color=Colors.RECURSIVE_COLOR),
            Text("① 移动 n-1 个盘子：A → B", font_size=14, color=Colors.TEXT),
            Text("② 移动最大盘子：A → C", font_size=14, color=Colors.SORT_COLOR),
            Text("③ 移动 n-1 个盘子：B → C", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        strategy.next_to(problem, DOWN, buff=0.3).align_to(problem, LEFT)
        
        for line in strategy:
            self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.3)
        
        self.wait(0.5)
        
        # 简化可视化
        self.play(FadeOut(problem), FadeOut(strategy))
        
        visual_title = Text("3 个盘子的移动过程：", font_size=16, color=Colors.SECONDARY)
        visual_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(visual_title))
        
        # 三个柱子
        poles = VGroup()
        pole_labels = ["A", "B", "C"]
        pole_colors = [Colors.HANOI_A, Colors.HANOI_B, Colors.HANOI_C]
        
        for i, (label, color) in enumerate(zip(pole_labels, pole_colors)):
            pole = Line(ORIGIN, UP * 1.2, color=color, stroke_width=3)
            base = Line(LEFT * 0.5, RIGHT * 0.5, color=color, stroke_width=3)
            pole_text = Text(label, font_size=16, color=color)
            pole_text.next_to(base, DOWN, buff=0.1)
            
            pole_group = VGroup(pole, base, pole_text)
            pole_group.shift(RIGHT * (i - 1) * 2)
            poles.add(pole_group)
        
        poles.next_to(visual_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(poles))
        
        # 创建盘子（在 A 柱）
        disk_widths = [1.0, 0.7, 0.4]
        disk_colors = [Colors.ACCENT, Colors.SORT_COLOR, Colors.SECONDARY]
        
        disks = VGroup()
        for i, (w, c) in enumerate(zip(disk_widths, disk_colors)):
            disk = create_disk(w, c)
            disk.next_to(poles[0][1], UP, buff=0.05 + i * 0.28)
            disks.add(disk)
        
        self.play(FadeIn(disks))
        self.wait(0.5)
        
        # 移动步骤说明
        moves_text = VGroup(
            Text("需要 2³-1 = 7 步", font_size=14, color=Colors.GRAY),
        )
        moves_text.next_to(poles, DOWN, buff=0.4)
        
        self.play(FadeIn(moves_text))
        
        # 递推关系
        recurrence = VGroup(
            Text("递推关系：", font_size=16, color=Colors.RECURSIVE_COLOR),
            MathTex(r"M_n = 2 \times M_{n-1} + 1", font_size=20, color=Colors.RECURSIVE_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        recurrence.next_to(moves_text, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(recurrence))
        self.wait(0.5)
        
        # 解
        solution = VGroup(
            Text("解：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"M_n = 2^n - 1", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        solution.next_to(recurrence, DOWN, buff=0.3)
        
        self.play(FadeIn(solution))
        
        # 64层塔
        legend = VGroup(
            Text("传说：", font_size=14, color=Colors.GRAY),
            Text("64 层塔需要 2⁶⁴-1 ≈ 1844 亿亿步", font_size=14, color=Colors.ACCENT),
            Text("这就是\"世界末日\"的数学依据", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        legend.next_to(solution, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(legend))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(visual_title),
            FadeOut(poles), FadeOut(disks),
            FadeOut(moves_text), FadeOut(recurrence),
            FadeOut(solution), FadeOut(legend),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_07_recursion_examples.py RecursionExamples
    pass
