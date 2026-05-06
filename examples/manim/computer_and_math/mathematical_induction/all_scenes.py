"""
数学归纳法 - 完整视频
包含所有场景的合并文件

渲染命令: manim -pqh all_scenes.py MathematicalInduction
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
    STRONG_COLOR = "#E91E63" # 强归纳粉
    WARNING_COLOR = "#F39C12" # 警告橙
    INVARIANT_COLOR = "#9B59B6" # 不变量紫
    FORMULA_COLOR = "#E67E22" # 公式橙
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


def create_domino(height=1.0, width=0.15, color=Colors.DOMINO_COLOR):
    """创建一个多米诺骨牌"""
    domino = Rectangle(height=height, width=width)
    domino.set_stroke(color, width=2)
    domino.set_fill(color, opacity=0.8)
    return domino


def create_nugget_box(count, color=Colors.DOMINO_COLOR):
    """创建鸡块盒子"""
    box = RoundedRectangle(height=0.8, width=1.2, corner_radius=0.1)
    box.set_stroke(color, width=2)
    box.set_fill(color, opacity=0.3)
    
    label = Text(str(count), font_size=22, color=Colors.TEXT)
    label.move_to(box.get_center())
    
    return VGroup(box, label)


def create_horse(color=Colors.DOMINO_COLOR, scale=1.0):
    """创建简化的马图标"""
    body = Ellipse(width=0.8, height=0.4)
    body.set_stroke(color, width=2)
    body.set_fill(color, opacity=0.6)
    
    head = Circle(radius=0.15)
    head.set_stroke(color, width=2)
    head.set_fill(color, opacity=0.6)
    head.next_to(body, RIGHT, buff=-0.1).shift(UP * 0.1)
    
    horse = VGroup(body, head)
    horse.scale(scale)
    return horse


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


# ========== 完整视频场景 ==========
class MathematicalInduction(Scene):
    """数学归纳法 - 完整视频"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题（贯穿全片）
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # ===== Scene 1: 数学归纳法引入 =====
        self.scene1_intro()
        
        # ===== Scene 2: 弱归纳法 =====
        self.scene2_weak_induction()
        
        # ===== Scene 3: 强归纳法 =====
        self.scene3_strong_induction()
        
        # ===== Scene 4: 归纳法的陷阱 =====
        self.scene4_pitfalls()
        
        # ===== Scene 5: 循环不变量 =====
        self.scene5_loop_invariant()
        
        # ===== Scene 6: 算法示例 =====
        self.scene6_algorithms()
        
        # ===== Scene 7: 总结与启示 =====
        self.scene7_summary()
    
    # ==================== Scene 1: 数学归纳法引入 ====================
    def scene1_intro(self):
        """Scene 1: 数学归纳法引入"""
        self.scene1_opening()
        self.scene1_domino_model()
        self.scene1_math_mapping()
        self.scene1_two_steps_summary()
        clear_scene(self)
    
    def scene1_opening(self):
        """开场动画"""
        main_title = Text("数学归纳法", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("无限问题的有限证明", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        question = Text(
            '如何证明一个关于"所有自然数"的结论？',
            font_size=22, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1)
        
        challenge = VGroup(
            Text("挑战：", font_size=18, color=Colors.ACCENT),
            Text("自然数有无限多个，无法逐一验证", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        challenge.next_to(question, DOWN, buff=0.4)
        
        self.play(FadeIn(challenge))
        self.wait(1.5)
        
        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            FadeOut(challenge),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def scene1_domino_model(self):
        """多米诺骨牌模型动画"""
        section_title = Text("多米诺骨牌模型", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        num_dominoes = 8
        dominoes = VGroup()
        
        for i in range(num_dominoes):
            domino = create_domino(height=1.0, width=0.15)
            domino.shift(RIGHT * i * 0.5)
            dominoes.add(domino)
        
        dots = Text("...", font_size=32, color=Colors.DOMINO_COLOR)
        dots.next_to(dominoes, RIGHT, buff=0.3)
        
        domino_group = VGroup(dominoes, dots)
        domino_group.next_to(section_title, DOWN, buff=0.8).set_x(0)
        
        ground = Line(
            domino_group.get_left() + LEFT * 0.5 + DOWN * 0.5,
            domino_group.get_right() + RIGHT * 0.5 + DOWN * 0.5,
            color=Colors.GRAY, stroke_width=2
        )
        
        self.play(FadeIn(ground))
        
        for domino in dominoes:
            self.play(FadeIn(domino, shift=UP * 0.3), run_time=0.15)
        self.play(FadeIn(dots))
        self.wait(0.5)
        
        goal = Text("目标：证明无限多张骨牌全部倒下", font_size=18, color=Colors.SECONDARY)
        goal.next_to(domino_group, DOWN, buff=0.6)
        
        self.play(FadeIn(goal))
        self.wait(1)
        
        base_step = VGroup(
            Text("基础步骤：", font_size=18, color=Colors.BASE_COLOR),
            Text("亲手推倒第一张骨牌", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        base_step.next_to(goal, DOWN, buff=0.5)
        
        self.play(FadeIn(base_step))
        
        push_arrow = Arrow(
            dominoes[0].get_left() + LEFT * 0.8 + UP * 0.3,
            dominoes[0].get_left() + LEFT * 0.1,
            color=Colors.BASE_COLOR, stroke_width=3
        )
        
        self.play(GrowArrow(push_arrow))
        self.wait(0.3)
        
        self.play(
            Rotate(dominoes[0], angle=-PI/3, about_point=dominoes[0].get_bottom()),
            FadeOut(push_arrow),
            run_time=0.5
        )
        self.wait(0.3)
        
        induct_step = VGroup(
            Text("归纳步骤：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("每张骨牌会推倒下一张", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        induct_step.next_to(base_step, DOWN, buff=0.3)
        
        self.play(FadeIn(induct_step))
        
        for i in range(1, num_dominoes):
            self.play(
                Rotate(dominoes[i], angle=-PI/3, about_point=dominoes[i].get_bottom()),
                run_time=0.2
            )
        
        self.wait(0.5)
        
        conclusion = VGroup(
            Text("结论：", font_size=18, color=Colors.PRIMARY),
            Text("所有骨牌都会倒下！", font_size=18, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(induct_step, DOWN, buff=0.5)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(domino_group), FadeOut(ground),
            FadeOut(goal), FadeOut(base_step), FadeOut(induct_step),
            FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    def scene1_math_mapping(self):
        """映射到数学表达"""
        section_title = Text("映射到数学", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        pn_intro = VGroup(
            Text("设 ", font_size=20, color=Colors.GRAY),
            MathTex(r"P(n)", font_size=28, color=Colors.PRIMARY),
            Text(" 表示关于自然数 ", font_size=20, color=Colors.GRAY),
            MathTex(r"n", font_size=28, color=Colors.PRIMARY),
            Text(" 的一个命题", font_size=20, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        pn_intro.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(pn_intro))
        self.wait(0.5)
        
        example_title = Text("例如：", font_size=18, color=Colors.SECONDARY)
        example_title.next_to(pn_intro, DOWN, buff=0.5).align_to(pn_intro, LEFT)
        
        example = MathTex(
            r"P(n): 1 + 2 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=26, color=Colors.TEXT
        )
        example.next_to(example_title, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(example_title), FadeIn(example))
        self.wait(1)
        
        goal = VGroup(
            Text("目标：证明 ", font_size=18, color=Colors.GRAY),
            MathTex(r"P(n)", font_size=24, color=Colors.PRIMARY),
            Text(" 对所有自然数 ", font_size=18, color=Colors.GRAY),
            MathTex(r"n \geq 1", font_size=24, color=Colors.PRIMARY),
            Text(" 成立", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        goal.next_to(example, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(goal))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(pn_intro),
            FadeOut(example_title), FadeOut(example),
            FadeOut(goal),
            run_time=0.5
        )
    
    def scene1_two_steps_summary(self):
        """归纳法两步流程总结"""
        section_title = Text("归纳法的两步流程", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        step1_title = VGroup(
            Text("步骤一：", font_size=20, color=Colors.BASE_COLOR),
            Text("基础步骤 (Base Case)", font_size=20, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        
        step1_content = VGroup(
            Text("证明 ", font_size=18, color=Colors.TEXT),
            MathTex(r"P(1)", font_size=24, color=Colors.BASE_COLOR),
            Text(" 成立", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        step1 = VGroup(step1_title, step1_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        step1_box = SurroundingRectangle(step1, color=Colors.BASE_COLOR, buff=0.2)
        step1_group = VGroup(step1, step1_box)
        
        step2_title = VGroup(
            Text("步骤二：", font_size=20, color=Colors.INDUCT_COLOR),
            Text("归纳步骤 (Inductive Step)", font_size=20, color=Colors.INDUCT_COLOR),
        ).arrange(RIGHT, buff=0.1)
        
        step2_content1 = VGroup(
            Text("归纳假设：假设 ", font_size=16, color=Colors.GRAY),
            MathTex(r"P(m)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 成立", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        
        step2_content2 = VGroup(
            Text("推进：证明 ", font_size=16, color=Colors.TEXT),
            MathTex(r"P(m+1)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 也成立", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        step2 = VGroup(step2_title, step2_content1, step2_content2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        step2_box = SurroundingRectangle(step2, color=Colors.INDUCT_COLOR, buff=0.2)
        step2_group = VGroup(step2, step2_box)
        
        steps = VGroup(step1_group, step2_group).arrange(DOWN, buff=0.5)
        steps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(step1_group))
        self.wait(0.8)
        self.play(FadeIn(step2_group))
        self.wait(1)
        
        arrow = Arrow(
            steps.get_bottom() + DOWN * 0.3,
            steps.get_bottom() + DOWN * 0.9,
            color=Colors.PRIMARY, stroke_width=3
        )
        
        conclusion = VGroup(
            MathTex(r"P(n)", font_size=24, color=Colors.PRIMARY),
            Text(" 对所有 ", font_size=18, color=Colors.TEXT),
            MathTex(r"n \geq 1", font_size=24, color=Colors.PRIMARY),
            Text(" 成立", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        conclusion.next_to(arrow, DOWN, buff=0.2)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.PRIMARY, buff=0.15)
        
        self.play(GrowArrow(arrow))
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(steps),
            FadeOut(arrow), FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    # ==================== Scene 2: 弱归纳法 ====================
    def scene2_weak_induction(self):
        """Scene 2: 弱归纳法"""
        self.scene2_intro()
        self.scene2_sum_formula()
        clear_scene(self)
    
    def scene2_intro(self):
        """弱归纳法介绍"""
        section_title = Text("弱归纳法（普通数学归纳法）", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        step1_title = Text("① 基础步骤", font_size=20, color=Colors.BASE_COLOR)
        step1_content = VGroup(
            Text("证明 ", font_size=18, color=Colors.TEXT),
            MathTex(r"P(1)", font_size=24, color=Colors.BASE_COLOR),
            Text(" 成立", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        step1 = VGroup(step1_title, step1_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        step2_title = Text("② 归纳步骤", font_size=20, color=Colors.INDUCT_COLOR)
        step2_content1 = VGroup(
            Text("归纳假设：假设 ", font_size=16, color=Colors.GRAY),
            MathTex(r"P(m)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 成立", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        step2_content2 = VGroup(
            Text("目标：证明 ", font_size=16, color=Colors.TEXT),
            MathTex(r"P(m+1)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 成立", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        step2 = VGroup(step2_title, step2_content1, step2_content2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        steps = VGroup(step1, step2).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        steps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(step1, shift=RIGHT * 0.2))
        self.wait(0.5)
        self.play(FadeIn(step2, shift=RIGHT * 0.2))
        self.wait(1)
        
        key_point = VGroup(
            Text("关键：", font_size=18, color=Colors.SECONDARY),
            Text('只需要假设"上一步" P(m) 成立', font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(steps, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(steps), FadeOut(key_point), run_time=0.5)
    
    def scene2_sum_formula(self):
        """经典例子：求和公式"""
        section_title = Text("经典例子：求和公式", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        proposition_label = Text("命题 P(n)：", font_size=18, color=Colors.PRIMARY)
        proposition = MathTex(
            r"1 + 2 + 3 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=28, color=Colors.FORMULA_COLOR
        )
        
        prop_group = VGroup(proposition_label, proposition).arrange(DOWN, buff=0.1)
        prop_group.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        prop_box = SurroundingRectangle(prop_group, color=Colors.FORMULA_COLOR, buff=0.2)
        
        self.play(FadeIn(prop_group), Create(prop_box))
        self.wait(1)
        
        base_title = VGroup(
            Text("① 基础步骤", font_size=20, color=Colors.BASE_COLOR),
            Text("（n = 1）", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        base_title.next_to(prop_box, DOWN, buff=0.5).align_to(prop_box, LEFT)
        
        self.play(FadeIn(base_title))
        
        base_left = VGroup(
            Text("左边 = ", font_size=16, color=Colors.GRAY),
            MathTex(r"1", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        base_right = VGroup(
            Text("右边 = ", font_size=16, color=Colors.GRAY),
            MathTex(r"\frac{1 \times 2}{2} = 1", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        base_conclusion = VGroup(
            Text("左边 = 右边 ", font_size=16, color=Colors.TEXT),
            Text("✓", font_size=20, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        
        base_content = VGroup(base_left, base_right, base_conclusion).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        base_content.next_to(base_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        for item in base_content:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(0.8)
        
        induct_title = Text("② 归纳步骤", font_size=20, color=Colors.INDUCT_COLOR)
        induct_title.next_to(base_content, DOWN, buff=0.4).align_to(base_title, LEFT)
        
        self.play(FadeIn(induct_title))
        
        hypothesis = VGroup(
            Text("归纳假设：设 ", font_size=16, color=Colors.GRAY),
            MathTex(r"1+2+\cdots+m = \frac{m(m+1)}{2}", font_size=20, color=Colors.INDUCT_COLOR),
        ).arrange(RIGHT, buff=0.08)
        hypothesis.next_to(induct_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(FadeIn(hypothesis))
        
        conclusion = VGroup(
            Text("证毕！P(m+1) 成立 ✓", font_size=18, color=Colors.BASE_COLOR),
        )
        conclusion.next_to(hypothesis, DOWN, buff=0.4).set_x(0)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.BASE_COLOR, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(prop_group), FadeOut(prop_box),
            FadeOut(base_title), FadeOut(base_content),
            FadeOut(induct_title), FadeOut(hypothesis),
            FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    # ==================== Scene 3: 强归纳法 ====================
    def scene3_strong_induction(self):
        """Scene 3: 强归纳法"""
        self.scene3_comparison()
        self.scene3_chicken_nugget()
        clear_scene(self)
    
    def scene3_comparison(self):
        """弱归纳与强归纳的区别"""
        section_title = Text("弱归纳 vs 强归纳", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        weak_title = Text("弱归纳（普通归纳）", font_size=20, color=Colors.INDUCT_COLOR)
        weak_content = VGroup(
            Text("假设：", font_size=16, color=Colors.GRAY),
            MathTex(r"P(m)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 成立（只假设上一步）", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        weak_group = VGroup(weak_title, weak_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        weak_box = SurroundingRectangle(weak_group, color=Colors.INDUCT_COLOR, buff=0.15)
        weak_full = VGroup(weak_group, weak_box)
        
        strong_title = Text("强归纳（完全归纳）", font_size=20, color=Colors.STRONG_COLOR)
        strong_content = VGroup(
            Text("假设：", font_size=16, color=Colors.GRAY),
            MathTex(r"P(1), P(2), \ldots, P(m)", font_size=20, color=Colors.STRONG_COLOR),
        ).arrange(RIGHT, buff=0.08)
        strong_content2 = Text("都成立（假设前面所有步）", font_size=16, color=Colors.TEXT)
        
        strong_group = VGroup(strong_title, strong_content, strong_content2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        strong_box = SurroundingRectangle(strong_group, color=Colors.STRONG_COLOR, buff=0.15)
        strong_full = VGroup(strong_group, strong_box)
        
        comparison = VGroup(weak_full, strong_full).arrange(DOWN, buff=0.5)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(weak_full))
        self.wait(0.8)
        self.play(FadeIn(strong_full))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(comparison), run_time=0.5)
    
    def scene3_chicken_nugget(self):
        """鸡块问题"""
        section_title = Text("鸡块问题", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        problem_content = VGroup(
            Text("餐厅只卖 ", font_size=18, color=Colors.GRAY),
            Text("6块装、9块装、20块装", font_size=18, color=Colors.DOMINO_COLOR),
            Text(" 的鸡块", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        problem_content.next_to(section_title, DOWN, buff=0.4)
        
        problem_question = Text("从哪个数量开始，所有数量都能买到？", font_size=18, color=Colors.SECONDARY)
        problem_question.next_to(problem_content, DOWN, buff=0.15)
        
        self.play(FadeIn(problem_content), FadeIn(problem_question))
        self.wait(1)
        
        answer = VGroup(
            Text("答案：", font_size=18, color=Colors.PRIMARY),
            Text("44块", font_size=24, color=Colors.STRONG_COLOR),
        ).arrange(RIGHT, buff=0.1)
        answer.next_to(problem_question, DOWN, buff=0.4).set_x(0)
        
        answer_box = SurroundingRectangle(answer, color=Colors.STRONG_COLOR, buff=0.15)
        
        self.play(FadeIn(answer), Create(answer_box))
        self.wait(1)
        
        proof_hint = VGroup(
            Text("证明思路：", font_size=16, color=Colors.SECONDARY),
            Text("基础：验证 44-49", font_size=14, color=Colors.BASE_COLOR),
            Text("归纳：若能买 n-6，则能买 n", font_size=14, color=Colors.INDUCT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        proof_hint.next_to(answer_box, DOWN, buff=0.4)
        
        self.play(FadeIn(proof_hint))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(problem_content), FadeOut(problem_question),
            FadeOut(answer), FadeOut(answer_box), FadeOut(proof_hint),
            run_time=0.5
        )
    
    # ==================== Scene 4: 归纳法的陷阱 ====================
    def scene4_pitfalls(self):
        """Scene 4: 归纳法的陷阱"""
        self.scene4_intro()
        self.scene4_no_base()
        self.scene4_all_horses()
        clear_scene(self)
    
    def scene4_intro(self):
        """陷阱介绍"""
        section_title = Text("归纳法的常见陷阱", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        warning = VGroup(
            Text("⚠️ 警告", font_size=24, color=Colors.WARNING_COLOR),
            Text("归纳法虽然强大，但使用不当会导致荒谬的结论", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2)
        warning.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(warning))
        self.wait(1.5)
        
        pitfalls = VGroup(
            Text("① 忘记基础步骤", font_size=18, color=Colors.ACCENT),
            Text("② 逆转蕴含方向", font_size=18, color=Colors.ACCENT),
            Text("③ 归纳步骤有漏洞", font_size=18, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        pitfalls.next_to(warning, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(pitfalls))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(warning), FadeOut(pitfalls), run_time=0.5)
    
    def scene4_no_base(self):
        """陷阱一：忘记基础步骤"""
        section_title = Text("陷阱一：忘记基础步骤", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        fake_claim = VGroup(
            Text('错误"证明"：', font_size=18, color=Colors.ACCENT),
            Text("前 n 个正偶数的和是奇数", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        fake_claim.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(fake_claim))
        
        but = Text("但 n=1 时，2 是偶数！基础步骤失败！", font_size=18, color=Colors.ACCENT)
        but.next_to(fake_claim, DOWN, buff=0.5)
        
        self.play(FadeIn(but))
        
        warning_box = VGroup(
            Text("教训：", font_size=18, color=Colors.WARNING_COLOR),
            Text('没有正确的基础步骤，整个"证明"建立在虚假之上', font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        warning_box.next_to(but, DOWN, buff=0.4).set_x(0)
        
        warning_border = SurroundingRectangle(warning_box, color=Colors.WARNING_COLOR, buff=0.15)
        
        self.play(FadeIn(warning_box), Create(warning_border))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(fake_claim), FadeOut(but),
            FadeOut(warning_box), FadeOut(warning_border),
            run_time=0.5
        )
    
    def scene4_all_horses(self):
        """陷阱三：所有马都同色"""
        section_title = Text('陷阱三："所有马都同色"', font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        claim = VGroup(
            Text("著名诡辩：", font_size=18, color=Colors.WARNING_COLOR),
            Text('"证明"任意 n 匹马都是同一颜色', font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        claim.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(claim))
        
        error_explain = VGroup(
            Text("问题：P(1)→P(2) 时", font_size=16, color=Colors.ACCENT),
            Text('两匹马的集合没有"公共马"！', font_size=16, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.1)
        error_explain.next_to(claim, DOWN, buff=0.5)
        
        self.play(FadeIn(error_explain))
        
        lesson = VGroup(
            Text("教训：归纳步骤必须对", font_size=16, color=Colors.TEXT),
            Text("所有 m", font_size=16, color=Colors.INDUCT_COLOR),
            Text(" 都成立", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        lesson.next_to(error_explain, DOWN, buff=0.4).set_x(0)
        
        lesson_box = SurroundingRectangle(lesson, color=Colors.WARNING_COLOR, buff=0.15)
        
        self.play(FadeIn(lesson), Create(lesson_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(claim),
            FadeOut(error_explain), FadeOut(lesson), FadeOut(lesson_box),
            run_time=0.5
        )
    
    # ==================== Scene 5: 循环不变量 ====================
    def scene5_loop_invariant(self):
        """Scene 5: 循环不变量"""
        self.scene5_intro()
        self.scene5_three_steps()
        clear_scene(self)
    
    def scene5_intro(self):
        """循环不变量介绍"""
        section_title = Text("循环不变量", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        question = VGroup(
            Text("问题：", font_size=20, color=Colors.PRIMARY),
            Text("如何保证循环代码是正确的？", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        question.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(question))
        
        definition = VGroup(
            Text("循环不变量：", font_size=18, color=Colors.INVARIANT_COLOR),
            Text("在循环执行过程中始终保持为真的条件", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(question, DOWN, buff=0.5).set_x(0)
        
        definition_box = SurroundingRectangle(definition, color=Colors.INVARIANT_COLOR, buff=0.15)
        
        self.play(FadeIn(definition), Create(definition_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(question),
            FadeOut(definition), FadeOut(definition_box),
            run_time=0.5
        )
    
    def scene5_three_steps(self):
        """三步证明法"""
        section_title = Text("三步证明法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        step1 = VGroup(
            Text("① 初始化", font_size=20, color=Colors.BASE_COLOR),
            Text("（基础步骤）", font_size=16, color=Colors.GRAY),
            Text("循环开始前，不变量成立", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        step2 = VGroup(
            Text("② 保持", font_size=20, color=Colors.INDUCT_COLOR),
            Text("（归纳步骤）", font_size=16, color=Colors.GRAY),
            Text("每次迭代后，不变量仍成立", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        step3 = VGroup(
            Text("③ 终止", font_size=20, color=Colors.LOOP_COLOR),
            Text("（结论）", font_size=16, color=Colors.GRAY),
            Text("循环结束时，目标达成", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        steps = VGroup(step1, step2, step3).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        steps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for step in [step1, step2, step3]:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(steps), run_time=0.5)
    
    # ==================== Scene 6: 算法示例 ====================
    def scene6_algorithms(self):
        """Scene 6: 算法示例"""
        self.scene6_bubble_sort()
        self.scene6_binary_search()
        clear_scene(self)
    
    def scene6_bubble_sort(self):
        """冒泡排序示例"""
        section_title = Text("算法示例：冒泡排序", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        invariant = VGroup(
            Text("循环不变量：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("第 k 轮后，最大的 k 个元素已在正确位置", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        invariant.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(invariant))
        
        proof = VGroup(
            Text("① 初始化：0 轮后，0 个元素已到位 ✓", font_size=14, color=Colors.BASE_COLOR),
            Text("② 保持：每轮将最大值冒泡到位 ✓", font_size=14, color=Colors.INDUCT_COLOR),
            Text("③ 终止：n-1 轮后，所有元素有序 ✓", font_size=14, color=Colors.LOOP_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        proof.next_to(invariant, DOWN, buff=0.5)
        
        for line in proof:
            self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.5)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(invariant), FadeOut(proof), run_time=0.5)
    
    def scene6_binary_search(self):
        """二分查找示例"""
        section_title = Text("算法示例：二分查找", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        invariant = VGroup(
            Text("循环不变量：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("如果目标存在，一定在 [left, right] 区间内", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        invariant.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(invariant))
        
        key_point = VGroup(
            Text("关键：", font_size=16, color=Colors.SECONDARY),
            Text("每次迭代，搜索区间缩小一半，但不变量始终成立", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(invariant, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(invariant), FadeOut(key_point), run_time=0.5)
    
    # ==================== Scene 7: 总结与启示 ====================
    def scene7_summary(self):
        """Scene 7: 总结与启示"""
        self.scene7_review()
        self.scene7_insights()
        self.scene7_closing()
        clear_scene(self)
    
    def scene7_review(self):
        """知识回顾"""
        section_title = Text("知识回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        points = VGroup(
            Text("① 归纳法核心：基础步骤 + 归纳步骤", font_size=16, color=Colors.PRIMARY),
            Text("② 弱归纳 vs 强归纳", font_size=16, color=Colors.PRIMARY),
            Text("③ 常见陷阱：忘基础、逆方向、有漏洞", font_size=16, color=Colors.PRIMARY),
            Text("④ 循环不变量：初始化 → 保持 → 终止", font_size=16, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        points.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(points), run_time=0.5)
    
    def scene7_insights(self):
        """编程启示"""
        section_title = Text("编程启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        insights = VGroup(
            Text('① 递归与归纳是"双胞胎"', font_size=18, color=Colors.SECONDARY),
            Text("② 循环不变量提升代码质量", font_size=18, color=Colors.SECONDARY),
            Text('③ 从"大概能运行"到"逻辑保证正确"', font_size=18, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        insights.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for insight in insights:
            self.play(FadeIn(insight, shift=RIGHT * 0.2), run_time=0.6)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(insights), run_time=0.5)
    
    def scene7_closing(self):
        """结语"""
        core_message = VGroup(
            Text("数学归纳法", font_size=32, color=Colors.PRIMARY),
            Text("开启算法正确性证明的钥匙", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.3)
        core_message.set_x(0).set_y(0)
        
        self.play(FadeIn(core_message[0], scale=0.8))
        self.play(FadeIn(core_message[1], shift=UP * 0.2))
        self.wait(0.8)
        
        summary = VGroup(
            Text("无限问题", font_size=18, color=Colors.GRAY),
            Text("→ 归纳法 →", font_size=18, color=Colors.INDUCT_COLOR),
            Text("有限证明", font_size=18, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        summary.next_to(core_message, DOWN, buff=0.5)
        
        self.play(FadeIn(summary))
        self.wait(0.5)
        
        domino_row = VGroup()
        for i in range(7):
            domino = Rectangle(height=0.8, width=0.12)
            domino.set_stroke(Colors.DOMINO_COLOR, width=2)
            domino.set_fill(Colors.DOMINO_COLOR, opacity=0.7)
            domino.shift(RIGHT * i * 0.35)
            domino_row.add(domino)
        
        dots = Text("...", font_size=24, color=Colors.DOMINO_COLOR)
        dots.next_to(domino_row, RIGHT, buff=0.2)
        
        domino_group = VGroup(domino_row, dots)
        domino_group.next_to(summary, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(domino_group))
        
        for domino in domino_row:
            self.play(
                Rotate(domino, angle=-PI/3, about_point=domino.get_bottom()),
                run_time=0.15
            )
        
        self.wait(0.5)
        
        final_words = VGroup(
            Text("掌握归纳法，", font_size=20, color=Colors.TEXT),
            Text('让你的代码从"能用"升级为"正确"', font_size=20, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        final_words.next_to(domino_group, DOWN, buff=0.5).set_x(0)
        
        final_box = SurroundingRectangle(final_words, color=Colors.SECONDARY, buff=0.2)
        
        self.play(FadeIn(final_words), Create(final_box))
        self.wait(2)
        
        self.play(
            FadeOut(core_message), FadeOut(summary),
            FadeOut(domino_group), FadeOut(final_words), FadeOut(final_box),
            run_time=0.8
        )
        
        thanks = Text("感谢观看", font_size=40, color=Colors.PRIMARY)
        thanks.set_x(0).set_y(0)
        
        self.play(FadeIn(thanks, scale=0.5))
        self.wait(2)
        
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    # 渲染命令: manim -pqh all_scenes.py MathematicalInduction
    pass
