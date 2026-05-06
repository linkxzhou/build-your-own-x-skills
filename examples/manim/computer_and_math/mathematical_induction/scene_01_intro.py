"""
数学归纳法 - Scene 1: 数学归纳法引入
通过多米诺骨牌模型直观展示归纳法的核心思想

渲染命令: manim -pqh scene_01_intro.py InductionIntro
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


def create_domino(height=1.2, width=0.2, color=Colors.DOMINO_COLOR):
    """创建一个多米诺骨牌"""
    domino = Rectangle(height=height, width=width)
    domino.set_stroke(color, width=2)
    domino.set_fill(color, opacity=0.8)
    return domino


# ========== Scene 1: 数学归纳法引入 ==========
class InductionIntro(Scene):
    """数学归纳法的直观介绍"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # 各部分
        self.opening()
        self.domino_model()
        self.math_mapping()
        self.two_steps_summary()
        
        clear_scene(self)
    
    def opening(self):
        """开场动画"""
        main_title = Text("数学归纳法", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("无限问题的有限证明", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        # 核心问题
        question = Text(
            '如何证明一个关于"所有自然数"的结论？',
            font_size=22, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1)
        
        # 难点说明
        challenge = VGroup(
            Text("挑战：", font_size=18, color=Colors.ACCENT),
            Text("自然数有无限多个，无法逐一验证", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        challenge.next_to(question, DOWN, buff=0.4)
        
        self.play(FadeIn(challenge))
        self.wait(1.5)
        
        # 转换到章节标题
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
    
    def domino_model(self):
        """多米诺骨牌模型动画"""
        section_title = Text("多米诺骨牌模型", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建一排多米诺骨牌（站立状态）
        num_dominoes = 8
        dominoes = VGroup()
        
        for i in range(num_dominoes):
            domino = create_domino(height=1.0, width=0.15)
            domino.shift(RIGHT * i * 0.5)
            dominoes.add(domino)
        
        # 加省略号表示无限
        dots = Text("...", font_size=32, color=Colors.DOMINO_COLOR)
        dots.next_to(dominoes, RIGHT, buff=0.3)
        
        domino_group = VGroup(dominoes, dots)
        domino_group.next_to(section_title, DOWN, buff=0.8).set_x(0)
        
        # 地面线
        ground = Line(
            domino_group.get_left() + LEFT * 0.5 + DOWN * 0.5,
            domino_group.get_right() + RIGHT * 0.5 + DOWN * 0.5,
            color=Colors.GRAY, stroke_width=2
        )
        
        self.play(FadeIn(ground))
        
        # 逐个出现骨牌
        for domino in dominoes:
            self.play(FadeIn(domino, shift=UP * 0.3), run_time=0.15)
        self.play(FadeIn(dots))
        self.wait(0.5)
        
        # 目标说明
        goal = Text("目标：证明无限多张骨牌全部倒下", font_size=18, color=Colors.SECONDARY)
        goal.next_to(domino_group, DOWN, buff=0.6)
        
        self.play(FadeIn(goal))
        self.wait(1)
        
        # ===== 基础步骤：推倒第一张骨牌 =====
        base_step = VGroup(
            Text("基础步骤：", font_size=18, color=Colors.BASE_COLOR),
            Text("亲手推倒第一张骨牌", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        base_step.next_to(goal, DOWN, buff=0.5)
        
        self.play(FadeIn(base_step))
        
        # 手指图标（简化为箭头）
        push_arrow = Arrow(
            dominoes[0].get_left() + LEFT * 0.8 + UP * 0.3,
            dominoes[0].get_left() + LEFT * 0.1,
            color=Colors.BASE_COLOR, stroke_width=3
        )
        
        self.play(GrowArrow(push_arrow))
        self.wait(0.3)
        
        # 第一张骨牌倒下（旋转动画）
        self.play(
            Rotate(dominoes[0], angle=-PI/3, about_point=dominoes[0].get_bottom()),
            FadeOut(push_arrow),
            run_time=0.5
        )
        self.wait(0.3)
        
        # ===== 归纳步骤：链式反应 =====
        induct_step = VGroup(
            Text("归纳步骤：", font_size=18, color=Colors.INDUCT_COLOR),
            Text("每张骨牌会推倒下一张", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        induct_step.next_to(base_step, DOWN, buff=0.3)
        
        self.play(FadeIn(induct_step))
        
        # 链式反应动画
        for i in range(1, num_dominoes):
            self.play(
                Rotate(dominoes[i], angle=-PI/3, about_point=dominoes[i].get_bottom()),
                run_time=0.2
            )
        
        self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            Text("结论：", font_size=18, color=Colors.PRIMARY),
            Text("所有骨牌都会倒下！", font_size=18, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(induct_step, DOWN, buff=0.5)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(section_title), FadeOut(domino_group), FadeOut(ground),
            FadeOut(goal), FadeOut(base_step), FadeOut(induct_step),
            FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    def math_mapping(self):
        """映射到数学表达"""
        section_title = Text("映射到数学", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # P(n) 的含义
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
        
        # 例子
        example_title = Text("例如：", font_size=18, color=Colors.SECONDARY)
        example_title.next_to(pn_intro, DOWN, buff=0.5).align_to(pn_intro, LEFT)
        
        example = MathTex(
            r"P(n): 1 + 2 + \cdots + n = \frac{n(n+1)}{2}",
            font_size=26, color=Colors.TEXT
        )
        example.next_to(example_title, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(example_title), FadeIn(example))
        self.wait(1)
        
        # 目标
        goal = VGroup(
            Text("目标：证明 ", font_size=18, color=Colors.GRAY),
            MathTex(r"P(n)", font_size=24, color=Colors.PRIMARY),
            Text(" 对所有自然数 ", font_size=18, color=Colors.GRAY),
            MathTex(r"n \geq 1", font_size=24, color=Colors.PRIMARY),
            Text(" 成立", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        goal.next_to(example, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(goal))
        self.wait(1)
        
        # 骨牌对应关系
        mapping_title = Text("骨牌与数学的对应：", font_size=18, color=Colors.INDUCT_COLOR)
        mapping_title.next_to(goal, DOWN, buff=0.6).align_to(goal, LEFT)
        
        mappings = VGroup(
            VGroup(
                Text("第 n 张骨牌倒下", font_size=16, color=Colors.DOMINO_COLOR),
                MathTex(r"\Leftrightarrow", font_size=22, color=Colors.GRAY),
                MathTex(r"P(n)", font_size=22, color=Colors.PRIMARY),
                Text(" 成立", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("推倒第一张", font_size=16, color=Colors.BASE_COLOR),
                MathTex(r"\Leftrightarrow", font_size=22, color=Colors.GRAY),
                Text("证明 ", font_size=16, color=Colors.TEXT),
                MathTex(r"P(1)", font_size=22, color=Colors.BASE_COLOR),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("一张推倒下一张", font_size=16, color=Colors.INDUCT_COLOR),
                MathTex(r"\Leftrightarrow", font_size=22, color=Colors.GRAY),
                MathTex(r"P(m) \Rightarrow P(m+1)", font_size=22, color=Colors.INDUCT_COLOR),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        mappings.next_to(mapping_title, DOWN, buff=0.2)
        
        self.play(FadeIn(mapping_title))
        
        for mapping in mappings:
            self.play(FadeIn(mapping, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(section_title), FadeOut(pn_intro),
            FadeOut(example_title), FadeOut(example),
            FadeOut(goal), FadeOut(mapping_title), FadeOut(mappings),
            run_time=0.5
        )
    
    def two_steps_summary(self):
        """归纳法两步流程总结"""
        section_title = Text("归纳法的两步流程", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 步骤1：基础步骤
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
        
        # 步骤2：归纳步骤
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
        
        # 排列两个步骤
        steps = VGroup(step1_group, step2_group).arrange(DOWN, buff=0.5)
        steps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(step1_group))
        self.wait(0.8)
        self.play(FadeIn(step2_group))
        self.wait(1)
        
        # 结论箭头
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
        
        # 直觉解释
        intuition = VGroup(
            Text("直觉：", font_size=16, color=Colors.SECONDARY),
            Text("第一张倒了，就一定能推倒第二张；", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        intuition2 = Text("第二张倒了，就一定能推倒第三张……以此类推", font_size=16, color=Colors.GRAY)
        
        intuition_group = VGroup(intuition, intuition2).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        intuition_group.next_to(conclusion_box, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intuition_group))
        self.wait(2)
        
        # 清理
        self.play(
            FadeOut(section_title), FadeOut(steps),
            FadeOut(arrow), FadeOut(conclusion), FadeOut(conclusion_box),
            FadeOut(intuition_group),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_01_intro.py InductionIntro
    pass
