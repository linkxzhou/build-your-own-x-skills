"""
递推与递归 - Scene 2: 递推关系基础
介绍等差数列、等比数列和斐波那契数列

渲染命令: manim -pqh scene_02_recurrence_basics.py RecurrenceBasics
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
    RECUR_COLOR = "#F39C12"  # 递推橙
    RECURSIVE_COLOR = "#9B59B6"  # 递归紫
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    CODE_COLOR = "#3498DB"   # 代码蓝
    FIBO_COLOR = "#E91E63"   # 斐波那契粉
    ARITH_COLOR = "#3498DB"  # 等差蓝
    GEOM_COLOR = "#E67E22"   # 等比橙


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


def create_sequence_element(value, color=Colors.PRIMARY, size=0.6):
    """创建数列元素"""
    circle = Circle(radius=size/2)
    circle.set_stroke(color, width=2)
    circle.set_fill(color, opacity=0.3)
    
    label = Text(str(value), font_size=18, color=Colors.TEXT)
    label.move_to(circle.get_center())
    
    return VGroup(circle, label)


# ========== Scene 2: 递推关系基础 ==========
class RecurrenceBasics(Scene):
    """递推关系基础知识"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.what_is_recurrence()
        self.arithmetic_sequence()
        self.geometric_sequence()
        self.fibonacci_sequence()
        
        clear_scene(self)
    
    def what_is_recurrence(self):
        """什么是递推关系"""
        section_title = Text("什么是递推关系？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("递推关系：", font_size=20, color=Colors.RECUR_COLOR),
            Text("用数列中前面的项来定义当前项的规则", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        definition_box = SurroundingRectangle(definition, color=Colors.RECUR_COLOR, buff=0.15)
        
        self.play(FadeIn(definition), Create(definition_box))
        self.wait(1)
        
        # 类比
        analogy = VGroup(
            Text("类比：", font_size=18, color=Colors.SECONDARY),
            Text("数列接龙游戏", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        analogy.next_to(definition_box, DOWN, buff=0.4)
        
        self.play(FadeIn(analogy))
        self.wait(0.5)
        
        # 需要的两个要素
        elements_title = Text("需要两个要素：", font_size=18, color=Colors.PRIMARY)
        elements_title.next_to(analogy, DOWN, buff=0.4).align_to(analogy, LEFT)
        
        self.play(FadeIn(elements_title))
        
        elem1 = VGroup(
            Text("① 初始值", font_size=16, color=Colors.BASE_COLOR),
            Text("（开头的数）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        
        elem2 = VGroup(
            Text("② 递推规则", font_size=16, color=Colors.RECUR_COLOR),
            Text("（怎么从前推到后）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        
        elements = VGroup(elem1, elem2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        elements.next_to(elements_title, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        for elem in elements:
            self.play(FadeIn(elem, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(1)
        
        # 示例预告
        preview = Text(
            "接下来看三个经典例子...",
            font_size=16, color=Colors.GRAY
        )
        preview.next_to(elements, DOWN, buff=0.5)
        
        self.play(FadeIn(preview))
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(definition_box),
            FadeOut(analogy), FadeOut(elements_title), FadeOut(elements),
            FadeOut(preview),
            run_time=0.5
        )
    
    def arithmetic_sequence(self):
        """等差数列"""
        section_title = Text("例子一：等差数列", font_size=26, color=Colors.ARITH_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 规则
        rule_title = Text("递推规则：", font_size=18, color=Colors.TEXT)
        rule_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        rule = MathTex(r"a_n = a_{n-1} + d", font_size=28, color=Colors.ARITH_COLOR)
        rule.next_to(rule_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(rule_title), FadeIn(rule))
        
        # 示例
        example_title = Text("示例（d=1）：", font_size=16, color=Colors.GRAY)
        example_title.next_to(rule_title, DOWN, buff=0.4).align_to(rule_title, LEFT)
        
        self.play(FadeIn(example_title))
        
        # 数列动画
        nums = VGroup()
        arrows = VGroup()
        values = [1, 2, 3, 4, 5]
        
        for i, val in enumerate(values):
            elem = create_sequence_element(val, Colors.ARITH_COLOR)
            elem.shift(RIGHT * i * 1.0)
            nums.add(elem)
            
            if i > 0:
                arrow = Arrow(
                    nums[i-1].get_right() + RIGHT * 0.05,
                    elem.get_left() + LEFT * 0.05,
                    buff=0.02, color=Colors.GRAY, stroke_width=2, max_tip_length_to_length_ratio=0.2
                )
                # +1 标签
                plus_label = Text("+1", font_size=12, color=Colors.ARITH_COLOR)
                plus_label.next_to(arrow, UP, buff=0.02)
                arrows.add(VGroup(arrow, plus_label))
        
        dots = Text("...", font_size=28, color=Colors.ARITH_COLOR)
        dots.next_to(nums, RIGHT, buff=0.3)
        
        seq_group = VGroup(nums, arrows, dots)
        seq_group.next_to(example_title, DOWN, buff=0.3).set_x(0)
        
        # 逐个出现
        for i, num in enumerate(nums):
            if i == 0:
                self.play(FadeIn(num, scale=0.5), run_time=0.3)
            else:
                self.play(
                    FadeIn(arrows[i-1]),
                    FadeIn(num, scale=0.5),
                    run_time=0.3
                )
        self.play(FadeIn(dots))
        
        # 特点
        feature = VGroup(
            Text("特点：", font_size=16, color=Colors.SECONDARY),
            Text("相邻两项的差是常数", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        feature.next_to(seq_group, DOWN, buff=0.4)
        
        self.play(FadeIn(feature))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(rule_title), FadeOut(rule),
            FadeOut(example_title), FadeOut(seq_group), FadeOut(feature),
            run_time=0.5
        )
    
    def geometric_sequence(self):
        """等比数列"""
        section_title = Text("例子二：等比数列", font_size=26, color=Colors.GEOM_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 规则
        rule_title = Text("递推规则：", font_size=18, color=Colors.TEXT)
        rule_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        rule = MathTex(r"a_n = r \times a_{n-1}", font_size=28, color=Colors.GEOM_COLOR)
        rule.next_to(rule_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(rule_title), FadeIn(rule))
        
        # 示例
        example_title = Text("示例（r=2）：", font_size=16, color=Colors.GRAY)
        example_title.next_to(rule_title, DOWN, buff=0.4).align_to(rule_title, LEFT)
        
        self.play(FadeIn(example_title))
        
        # 数列动画（用柱状图表示指数增长）
        values = [1, 2, 4, 8, 16]
        max_val = max(values)
        
        bars = VGroup()
        labels = VGroup()
        
        for i, val in enumerate(values):
            bar_height = (val / max_val) * 2.0
            bar = Rectangle(width=0.5, height=bar_height)
            bar.set_stroke(Colors.GEOM_COLOR, width=2)
            bar.set_fill(Colors.GEOM_COLOR, opacity=0.6)
            bar.shift(RIGHT * i * 0.8)
            bar.align_to(ORIGIN, DOWN)
            bars.add(bar)
            
            label = Text(str(val), font_size=14, color=Colors.TEXT)
            label.next_to(bar, UP, buff=0.1)
            labels.add(label)
        
        dots = Text("...", font_size=28, color=Colors.GEOM_COLOR)
        
        chart = VGroup(bars, labels)
        chart.next_to(example_title, DOWN, buff=0.4).set_x(0)
        dots.next_to(chart, RIGHT, buff=0.2)
        
        # 动画
        for i in range(len(bars)):
            self.play(
                GrowFromEdge(bars[i], DOWN),
                FadeIn(labels[i]),
                run_time=0.4
            )
        self.play(FadeIn(dots))
        
        # ×2 标注
        multiply_labels = VGroup()
        for i in range(len(bars) - 1):
            mult = Text("×2", font_size=12, color=Colors.GEOM_COLOR)
            mult.move_to((bars[i].get_center() + bars[i+1].get_center()) / 2 + UP * 0.3)
            multiply_labels.add(mult)
        
        self.play(FadeIn(multiply_labels))
        
        # 特点
        feature = VGroup(
            Text("特点：", font_size=16, color=Colors.SECONDARY),
            Text("相邻两项的比是常数，指数增长", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        feature.next_to(chart, DOWN, buff=0.5)
        
        self.play(FadeIn(feature))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(rule_title), FadeOut(rule),
            FadeOut(example_title), FadeOut(chart), FadeOut(dots),
            FadeOut(multiply_labels), FadeOut(feature),
            run_time=0.5
        )
    
    def fibonacci_sequence(self):
        """斐波那契数列"""
        section_title = Text("例子三：斐波那契数列", font_size=26, color=Colors.FIBO_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 规则
        rule_title = Text("递推规则：", font_size=18, color=Colors.TEXT)
        rule_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        rule = MathTex(r"a_n = a_{n-1} + a_{n-2}", font_size=28, color=Colors.FIBO_COLOR)
        rule.next_to(rule_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(rule_title), FadeIn(rule))
        
        # 初始值
        init = VGroup(
            Text("初始值：", font_size=16, color=Colors.GRAY),
            MathTex(r"a_1 = 1, a_2 = 1", font_size=22, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        init.next_to(rule_title, DOWN, buff=0.3).align_to(rule_title, LEFT)
        
        self.play(FadeIn(init))
        
        # 数列
        fib_values = [1, 1, 2, 3, 5, 8, 13]
        
        nums = VGroup()
        for i, val in enumerate(fib_values):
            elem = create_sequence_element(val, Colors.FIBO_COLOR, size=0.55)
            elem.shift(RIGHT * i * 0.85)
            nums.add(elem)
        
        dots = Text("...", font_size=24, color=Colors.FIBO_COLOR)
        dots.next_to(nums, RIGHT, buff=0.2)
        
        seq_group = VGroup(nums, dots)
        seq_group.next_to(init, DOWN, buff=0.4).set_x(0)
        
        # 逐个出现并展示加法关系
        self.play(FadeIn(nums[0], scale=0.5), FadeIn(nums[1], scale=0.5), run_time=0.4)
        
        for i in range(2, len(fib_values)):
            # 高亮前两个
            highlight1 = SurroundingRectangle(nums[i-2], color=Colors.SECONDARY, buff=0.05)
            highlight2 = SurroundingRectangle(nums[i-1], color=Colors.SECONDARY, buff=0.05)
            
            # 加号
            plus = Text("+", font_size=16, color=Colors.SECONDARY)
            plus.move_to((nums[i-2].get_center() + nums[i-1].get_center()) / 2 + DOWN * 0.6)
            
            # 等于
            equals = Text("=", font_size=16, color=Colors.SECONDARY)
            equals.next_to(plus, RIGHT, buff=0.3)
            
            # 结果
            result = Text(str(fib_values[i]), font_size=16, color=Colors.FIBO_COLOR)
            result.next_to(equals, RIGHT, buff=0.1)
            
            calc = VGroup(plus, equals, result)
            
            self.play(
                Create(highlight1), Create(highlight2),
                FadeIn(calc),
                run_time=0.3
            )
            self.play(
                FadeIn(nums[i], scale=0.5),
                FadeOut(highlight1), FadeOut(highlight2), FadeOut(calc),
                run_time=0.3
            )
        
        self.play(FadeIn(dots))
        self.wait(0.5)
        
        # 解释
        explain = VGroup(
            Text("规则：", font_size=16, color=Colors.SECONDARY),
            Text("当前项 = 前两项之和", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explain.next_to(seq_group, DOWN, buff=0.4)
        
        self.play(FadeIn(explain))
        
        # 黄金比例关联
        golden = VGroup(
            Text("趣闻：", font_size=14, color=Colors.GRAY),
            Text("相邻两项的比趋近于黄金比例 φ ≈ 1.618", font_size=14, color=Colors.RECUR_COLOR),
        ).arrange(RIGHT, buff=0.1)
        golden.next_to(explain, DOWN, buff=0.3)
        
        self.play(FadeIn(golden))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(rule_title), FadeOut(rule),
            FadeOut(init), FadeOut(seq_group), FadeOut(explain), FadeOut(golden),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_02_recurrence_basics.py RecurrenceBasics
    pass
