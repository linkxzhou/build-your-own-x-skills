"""
递推与递归 - Scene 6: 递归基础概念
介绍递归的核心要素和基本思想

渲染命令: manim -pqh scene_06_recursion_intro.py RecursionBasics
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


def create_matryoshka(size, color, opacity=0.7):
    """创建俄罗斯套娃形状"""
    body = Ellipse(width=size * 0.8, height=size)
    body.set_stroke(color, width=2)
    body.set_fill(color, opacity=opacity)
    
    head = Circle(radius=size * 0.25)
    head.set_stroke(color, width=2)
    head.set_fill(color, opacity=opacity)
    head.next_to(body, UP, buff=-size * 0.15)
    
    return VGroup(body, head)


# ========== Scene 6: 递归基础概念 ==========
class RecursionBasics(Scene):
    """递归基础概念"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.from_recurrence_to_recursion()
        self.two_core_elements()
        self.infinite_loop_warning()
        self.fun_examples()
        
        clear_scene(self)
    
    def from_recurrence_to_recursion(self):
        """从递推到递归"""
        section_title = Text("从递推到递归", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 对比
        comparison = VGroup(
            VGroup(
                Text("递推", font_size=22, color=Colors.RECUR_COLOR),
                Text("从前到后的生成", font_size=16, color=Colors.TEXT),
                Text("数学视角", font_size=14, color=Colors.GRAY),
                MathTex(r"a_1 \to a_2 \to a_3 \to \cdots", font_size=18, color=Colors.RECUR_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("递归", font_size=22, color=Colors.RECURSIVE_COLOR),
                Text("从大到小的拆解与合并", font_size=16, color=Colors.TEXT),
                Text("编程视角", font_size=14, color=Colors.GRAY),
                MathTex(r"f(n) \to f(n-1) \to \cdots \to f(1)", font_size=18, color=Colors.RECURSIVE_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.0)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 框
        box1 = SurroundingRectangle(comparison[0], color=Colors.RECUR_COLOR, buff=0.2)
        box2 = SurroundingRectangle(comparison[1], color=Colors.RECURSIVE_COLOR, buff=0.2)
        
        self.play(
            FadeIn(comparison[0]), Create(box1),
            run_time=0.8
        )
        self.wait(0.5)
        self.play(
            FadeIn(comparison[1]), Create(box2),
            run_time=0.8
        )
        self.wait(1)
        
        # 核心定义
        definition = VGroup(
            Text("递归：", font_size=18, color=Colors.PRIMARY),
            Text("函数调用自身来解决问题", font_size=18, color=Colors.RECURSIVE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(comparison, DOWN, buff=0.5)
        
        def_box = SurroundingRectangle(definition, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(definition), Create(def_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(comparison),
            FadeOut(box1), FadeOut(box2),
            FadeOut(definition), FadeOut(def_box),
            run_time=0.5
        )
    
    def two_core_elements(self):
        """两个核心要素"""
        section_title = Text("递归的两个核心要素", font_size=26, color=Colors.RECURSIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 要素一：基准情况
        elem1_title = Text("① 基准情况 (Base Case)", font_size=20, color=Colors.BASE_COLOR)
        elem1_content = VGroup(
            Text("最简单的问题，可以直接解决", font_size=16, color=Colors.TEXT),
            Text("递归的终点", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        elem1 = VGroup(elem1_title, elem1_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        elem1_box = SurroundingRectangle(elem1, color=Colors.BASE_COLOR, buff=0.15)
        elem1_group = VGroup(elem1, elem1_box)
        
        # 要素二：递归情况
        elem2_title = Text("② 递归情况 (Recursive Case)", font_size=20, color=Colors.RECURSIVE_COLOR)
        elem2_content = VGroup(
            Text("把问题分解为更小的子问题", font_size=16, color=Colors.TEXT),
            Text("子问题结构相同但规模更小", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        elem2 = VGroup(elem2_title, elem2_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        elem2_box = SurroundingRectangle(elem2, color=Colors.RECURSIVE_COLOR, buff=0.15)
        elem2_group = VGroup(elem2, elem2_box)
        
        elements = VGroup(elem1_group, elem2_group).arrange(DOWN, buff=0.4)
        elements.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(elem1_group, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(elem2_group, shift=RIGHT * 0.2))
        self.wait(1)
        
        # 代码示例
        self.play(FadeOut(elements))
        
        code_title = Text("伪代码示例：", font_size=18, color=Colors.CODE_COLOR)
        code_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(code_title))
        
        # 代码块
        code_lines = VGroup(
            Text("def solve(problem):", font_size=14, color=Colors.CODE_COLOR),
            Text("    if is_simple(problem):", font_size=14, color=Colors.BASE_COLOR),
            Text("        return direct_answer  # 基准情况", font_size=14, color=Colors.GRAY),
            Text("    else:", font_size=14, color=Colors.RECURSIVE_COLOR),
            Text("        smaller = make_smaller(problem)", font_size=14, color=Colors.TEXT),
            Text("        return combine(solve(smaller))  # 递归", font_size=14, color=Colors.RECURSIVE_COLOR),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        
        code_bg = RoundedRectangle(
            width=code_lines.width + 0.4,
            height=code_lines.height + 0.3,
            corner_radius=0.1
        )
        code_bg.set_stroke(Colors.CODE_COLOR, width=1)
        code_bg.set_fill("#0a0a1a", opacity=0.9)
        code_bg.move_to(code_lines.get_center())
        
        code_block = VGroup(code_bg, code_lines)
        code_block.next_to(code_title, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(code_block))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(code_title), FadeOut(code_block),
            run_time=0.5
        )
    
    def infinite_loop_warning(self):
        """无限循环警告"""
        section_title = Text("⚠️ 没有基准情况会怎样？", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 警告
        warning = VGroup(
            Text("无限循环！", font_size=24, color=Colors.ACCENT),
            Text("程序永远不会停止", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        warning.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(warning, scale=0.8))
        self.wait(0.5)
        
        # 可视化无限调用
        call_title = Text("函数调用栈爆炸：", font_size=16, color=Colors.GRAY)
        call_title.next_to(warning, DOWN, buff=0.4).align_to(warning, LEFT)
        
        self.play(FadeIn(call_title))
        
        # 堆栈动画
        stack_items = VGroup()
        for i in range(6):
            item = VGroup(
                Rectangle(width=2.5, height=0.4, color=Colors.ACCENT, stroke_width=1),
                Text(f"solve({5-i})", font_size=12, color=Colors.TEXT),
            )
            item[1].move_to(item[0].get_center())
            stack_items.add(item)
        
        stack_items.arrange(DOWN, buff=0.05)
        stack_items.next_to(call_title, DOWN, buff=0.2)
        
        # 逐个添加
        for item in stack_items:
            self.play(FadeIn(item, shift=DOWN * 0.2), run_time=0.2)
        
        # 省略号和崩溃
        dots = Text("...", font_size=24, color=Colors.ACCENT)
        dots.next_to(stack_items, DOWN, buff=0.1)
        
        crash = Text("💥 Stack Overflow!", font_size=18, color=Colors.ACCENT)
        crash.next_to(dots, DOWN, buff=0.2)
        
        self.play(FadeIn(dots), FadeIn(crash))
        self.wait(1)
        
        # 教训
        lesson = VGroup(
            Text("教训：", font_size=18, color=Colors.SECONDARY),
            Text("必须有基准情况来终止递归！", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        lesson.next_to(crash, DOWN, buff=0.4)
        
        lesson_box = SurroundingRectangle(lesson, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(lesson), Create(lesson_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(warning),
            FadeOut(call_title), FadeOut(stack_items),
            FadeOut(dots), FadeOut(crash),
            FadeOut(lesson), FadeOut(lesson_box),
            run_time=0.5
        )
    
    def fun_examples(self):
        """趣味例子"""
        section_title = Text("趣味递归例子", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # GNU
        gnu_title = Text('① GNU = "GNU\'s Not Unix"', font_size=18, color=Colors.RECURSIVE_COLOR)
        gnu_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        gnu_explain = VGroup(
            Text("GNU 的定义中包含 GNU 本身", font_size=14, color=Colors.GRAY),
            Text("（没有基准情况的递归定义）", font_size=14, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        gnu_explain.next_to(gnu_title, DOWN, buff=0.15).shift(RIGHT * 0.3)
        
        self.play(FadeIn(gnu_title))
        self.play(FadeIn(gnu_explain))
        self.wait(0.8)
        
        # 俄罗斯套娃
        matry_title = Text("② 俄罗斯套娃", font_size=18, color=Colors.RECURSIVE_COLOR)
        matry_title.next_to(gnu_explain, DOWN, buff=0.4).align_to(gnu_title, LEFT)
        
        self.play(FadeIn(matry_title))
        
        # 套娃动画
        colors = [Colors.ACCENT, Colors.RECURSIVE_COLOR, Colors.PRIMARY, Colors.SECONDARY, Colors.BASE_COLOR]
        sizes = [1.2, 0.95, 0.7, 0.5, 0.35]
        
        dolls = VGroup()
        for size, color in zip(sizes, colors):
            doll = create_matryoshka(size, color)
            dolls.add(doll)
        
        dolls.arrange(RIGHT, buff=0.2)
        dolls.next_to(matry_title, DOWN, buff=0.2).set_x(0)
        dolls.scale(0.7)
        
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dolls], lag_ratio=0.2),
            run_time=1
        )
        
        matry_explain = VGroup(
            Text("打开大娃娃 → 发现小娃娃", font_size=14, color=Colors.GRAY),
            Text("直到最小的娃娃（基准情况）", font_size=14, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        matry_explain.next_to(dolls, DOWN, buff=0.2)
        
        self.play(FadeIn(matry_explain))
        self.wait(1)
        
        # 乌龟塔
        turtle_title = Text("③ 乌龟塔悖论", font_size=18, color=Colors.RECURSIVE_COLOR)
        turtle_title.next_to(matry_explain, DOWN, buff=0.4).align_to(matry_title, LEFT)
        
        self.play(FadeIn(turtle_title))
        
        turtle_story = VGroup(
            Text('"地球站在一只大乌龟背上"', font_size=14, color=Colors.GRAY),
            Text('"大乌龟站在更大的乌龟背上"', font_size=14, color=Colors.GRAY),
            Text('"一直都是乌龟！"', font_size=14, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        turtle_story.next_to(turtle_title, DOWN, buff=0.15).shift(RIGHT * 0.3)
        
        self.play(FadeIn(turtle_story))
        
        no_base = Text("（没有基准情况的无限递归）", font_size=12, color=Colors.ACCENT)
        no_base.next_to(turtle_story, DOWN, buff=0.1)
        
        self.play(FadeIn(no_base))
        self.wait(2)
        
        self.play(
            FadeOut(section_title),
            FadeOut(gnu_title), FadeOut(gnu_explain),
            FadeOut(matry_title), FadeOut(dolls), FadeOut(matry_explain),
            FadeOut(turtle_title), FadeOut(turtle_story), FadeOut(no_base),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_06_recursion_intro.py RecursionBasics
    pass
