"""
数学归纳法 - Scene 3: 强归纳法
通过鸡块问题展示强归纳法的特点和应用

渲染命令: manim -pqh scene_03_strong_induction.py StrongInduction
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


# ========== Scene 3: 强归纳法 ==========
class StrongInduction(Scene):
    """强归纳法及鸡块问题"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.weak_vs_strong()
        self.chicken_nugget_problem()
        self.application_scenarios()
        
        clear_scene(self)
    
    def weak_vs_strong(self):
        """弱归纳与强归纳的区别"""
        section_title = Text("弱归纳 vs 强归纳", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 弱归纳
        weak_title = Text("弱归纳（普通归纳）", font_size=20, color=Colors.INDUCT_COLOR)
        weak_content = VGroup(
            Text("假设：", font_size=16, color=Colors.GRAY),
            MathTex(r"P(m)", font_size=22, color=Colors.INDUCT_COLOR),
            Text(" 成立（只假设上一步）", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        weak_group = VGroup(weak_title, weak_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        weak_box = SurroundingRectangle(weak_group, color=Colors.INDUCT_COLOR, buff=0.15)
        weak_full = VGroup(weak_group, weak_box)
        
        # 强归纳
        strong_title = Text("强归纳（完全归纳）", font_size=20, color=Colors.STRONG_COLOR)
        strong_content = VGroup(
            Text("假设：", font_size=16, color=Colors.GRAY),
            MathTex(r"P(1), P(2), \ldots, P(m)", font_size=20, color=Colors.STRONG_COLOR),
        ).arrange(RIGHT, buff=0.08)
        strong_content2 = Text("都成立（假设前面所有步）", font_size=16, color=Colors.TEXT)
        
        strong_group = VGroup(strong_title, strong_content, strong_content2).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        strong_box = SurroundingRectangle(strong_group, color=Colors.STRONG_COLOR, buff=0.15)
        strong_full = VGroup(strong_group, strong_box)
        
        # 排列
        comparison = VGroup(weak_full, strong_full).arrange(DOWN, buff=0.5)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(weak_full))
        self.wait(0.8)
        self.play(FadeIn(strong_full))
        self.wait(1)
        
        # 多米诺骨牌类比
        analogy_title = Text("多米诺骨牌类比：", font_size=18, color=Colors.SECONDARY)
        analogy_title.next_to(comparison, DOWN, buff=0.5).align_to(comparison, LEFT)
        
        analogy_content = VGroup(
            Text("一张牌可能需要", font_size=16, color=Colors.GRAY),
            Text("前面多张牌的力量", font_size=16, color=Colors.STRONG_COLOR),
            Text("才能倒下", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        analogy_content.next_to(analogy_title, DOWN, buff=0.15)
        
        self.play(FadeIn(analogy_title), FadeIn(analogy_content))
        
        # 简单动画：多张骨牌一起推
        dominoes = VGroup()
        for i in range(5):
            d = create_domino(height=0.8, width=0.12)
            d.shift(RIGHT * i * 0.4)
            dominoes.add(d)
        
        dominoes.next_to(analogy_content, DOWN, buff=0.4).set_x(0)
        
        # 最后一张骨牌（大一点，需要更多力量）
        big_domino = create_domino(height=1.2, width=0.2, color=Colors.STRONG_COLOR)
        big_domino.next_to(dominoes, RIGHT, buff=0.4)
        
        self.play(FadeIn(dominoes), FadeIn(big_domino))
        
        # 箭头表示多张一起推
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                dominoes[i+1].get_right() + RIGHT * 0.05,
                big_domino.get_left() + LEFT * 0.05 + UP * (0.2 - i * 0.2),
                color=Colors.STRONG_COLOR, stroke_width=2, buff=0
            )
            arrows.add(arrow)
        
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            run_time=0.8
        )
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(comparison),
            FadeOut(analogy_title), FadeOut(analogy_content),
            FadeOut(dominoes), FadeOut(big_domino), FadeOut(arrows),
            run_time=0.5
        )
    
    def chicken_nugget_problem(self):
        """鸡块问题"""
        section_title = Text("鸡块问题（Chicken McNugget Theorem）", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 题目
        problem_title = Text("问题：", font_size=20, color=Colors.PRIMARY)
        problem_title.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT)
        
        problem_content = VGroup(
            Text("餐厅只卖 ", font_size=18, color=Colors.GRAY),
            Text("6块装、9块装、20块装", font_size=18, color=Colors.DOMINO_COLOR),
            Text(" 的鸡块", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        problem_content.next_to(problem_title, DOWN, buff=0.15)
        
        problem_question = Text("从哪个数量开始，所有数量都能买到？", font_size=18, color=Colors.SECONDARY)
        problem_question.next_to(problem_content, DOWN, buff=0.15)
        
        self.play(FadeIn(problem_title))
        self.play(FadeIn(problem_content))
        self.play(FadeIn(problem_question))
        self.wait(1)
        
        # 答案
        answer = VGroup(
            Text("答案：", font_size=18, color=Colors.PRIMARY),
            Text("44块", font_size=24, color=Colors.STRONG_COLOR),
        ).arrange(RIGHT, buff=0.1)
        answer.next_to(problem_question, DOWN, buff=0.4).set_x(0)
        
        answer_box = SurroundingRectangle(answer, color=Colors.STRONG_COLOR, buff=0.15)
        
        self.play(FadeIn(answer), Create(answer_box))
        self.wait(0.8)
        
        # 显示鸡块盒子
        boxes_title = Text("可用盒子：", font_size=16, color=Colors.GRAY)
        boxes_title.next_to(answer_box, DOWN, buff=0.4).align_to(answer_box, LEFT)
        
        box_6 = create_nugget_box(6, Colors.BASE_COLOR)
        box_9 = create_nugget_box(9, Colors.INDUCT_COLOR)
        box_20 = create_nugget_box(20, Colors.STRONG_COLOR)
        
        boxes = VGroup(box_6, box_9, box_20).arrange(RIGHT, buff=0.3)
        boxes.next_to(boxes_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(boxes_title), FadeIn(boxes))
        self.wait(0.5)
        
        # 证明思路
        self.play(
            FadeOut(problem_title), FadeOut(problem_content),
            FadeOut(problem_question), FadeOut(answer), FadeOut(answer_box),
            FadeOut(boxes_title), FadeOut(boxes),
            run_time=0.5
        )
        
        proof_title = Text("证明思路（强归纳法）：", font_size=20, color=Colors.STRONG_COLOR)
        proof_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(proof_title))
        
        # 基础步骤
        base_title = Text("① 基础步骤：验证 44, 45, 46, 47, 48, 49", font_size=18, color=Colors.BASE_COLOR)
        base_title.next_to(proof_title, DOWN, buff=0.3).shift(RIGHT * 0.2)
        
        self.play(FadeIn(base_title))
        
        # 验证表格
        verifications = VGroup()
        verify_data = [
            ("44", "6×4 + 20×1"),
            ("45", "9×5"),
            ("46", "6×1 + 20×2"),
            ("47", "9×3 + 20×1"),
            ("48", "6×8"),
            ("49", "9×1 + 20×2"),
        ]
        
        for val, formula in verify_data:
            row = VGroup(
                Text(val, font_size=14, color=Colors.TEXT),
                Text(" = ", font_size=14, color=Colors.GRAY),
                Text(formula, font_size=14, color=Colors.BASE_COLOR),
            ).arrange(RIGHT, buff=0.1)
            verifications.add(row)
        
        verifications.arrange_in_grid(rows=2, cols=3, buff=(0.4, 0.2))
        verifications.next_to(base_title, DOWN, buff=0.2)
        
        self.play(FadeIn(verifications))
        self.wait(1)
        
        # 归纳步骤
        induct_title = Text("② 归纳步骤：", font_size=18, color=Colors.INDUCT_COLOR)
        induct_title.next_to(verifications, DOWN, buff=0.4).align_to(base_title, LEFT)
        
        self.play(FadeIn(induct_title))
        
        induct_content1 = VGroup(
            Text("设 ", font_size=16, color=Colors.TEXT),
            MathTex(r"n \geq 50", font_size=20, color=Colors.STRONG_COLOR),
            Text("，假设 44 到 n-1 的所有数量都能买到", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        induct_content1.next_to(induct_title, DOWN, buff=0.15).shift(RIGHT * 0.2)
        
        self.play(FadeIn(induct_content1))
        
        induct_content2 = VGroup(
            Text("则 ", font_size=16, color=Colors.TEXT),
            MathTex(r"n-6 \geq 44", font_size=20, color=Colors.TEXT),
            Text("，根据假设 n-6 能买到", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        induct_content2.next_to(induct_content1, DOWN, buff=0.15).align_to(induct_content1, LEFT)
        
        self.play(FadeIn(induct_content2))
        
        induct_conclusion = VGroup(
            Text("所以 ", font_size=16, color=Colors.TEXT),
            MathTex(r"n = (n-6) + 6", font_size=20, color=Colors.STRONG_COLOR),
            Text(" 也能买到 ✓", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.08)
        induct_conclusion.next_to(induct_content2, DOWN, buff=0.15).align_to(induct_content2, LEFT)
        
        self.play(FadeIn(induct_conclusion))
        self.wait(2)
        
        # 可视化：从 n-6 到 n
        visual_title = Text("可视化：", font_size=16, color=Colors.SECONDARY)
        visual_title.next_to(induct_conclusion, DOWN, buff=0.4).align_to(induct_conclusion, LEFT)
        
        n_minus_6_box = RoundedRectangle(height=0.6, width=1.0, corner_radius=0.1)
        n_minus_6_box.set_stroke(Colors.INDUCT_COLOR, width=2)
        n_minus_6_box.set_fill(Colors.INDUCT_COLOR, opacity=0.3)
        n_minus_6_label = Text("n-6", font_size=16, color=Colors.TEXT)
        n_minus_6_label.move_to(n_minus_6_box.get_center())
        n_minus_6 = VGroup(n_minus_6_box, n_minus_6_label)
        
        plus = Text("+", font_size=24, color=Colors.GRAY)
        
        box_6_small = create_nugget_box(6, Colors.BASE_COLOR)
        box_6_small.scale(0.7)
        
        equals = Text("=", font_size=24, color=Colors.GRAY)
        
        n_box = RoundedRectangle(height=0.6, width=0.8, corner_radius=0.1)
        n_box.set_stroke(Colors.STRONG_COLOR, width=2)
        n_box.set_fill(Colors.STRONG_COLOR, opacity=0.3)
        n_label = Text("n", font_size=18, color=Colors.TEXT)
        n_label.move_to(n_box.get_center())
        n_full = VGroup(n_box, n_label)
        
        visual = VGroup(n_minus_6, plus, box_6_small, equals, n_full).arrange(RIGHT, buff=0.2)
        visual.next_to(visual_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(visual_title), FadeIn(visual))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(proof_title),
            FadeOut(base_title), FadeOut(verifications),
            FadeOut(induct_title), FadeOut(induct_content1),
            FadeOut(induct_content2), FadeOut(induct_conclusion),
            FadeOut(visual_title), FadeOut(visual),
            run_time=0.5
        )
    
    def application_scenarios(self):
        """强归纳法的适用场景"""
        section_title = Text("强归纳法的适用场景", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 场景列表
        scenarios = VGroup()
        
        scenario1 = VGroup(
            Text("① 递归定义的问题", font_size=20, color=Colors.STRONG_COLOR),
            Text("如 Fibonacci 数列：F(n) = F(n-1) + F(n-2)", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        scenarios.add(scenario1)
        
        scenario2 = VGroup(
            Text("② 分治算法的正确性证明", font_size=20, color=Colors.STRONG_COLOR),
            Text("如归并排序、快速排序", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        scenarios.add(scenario2)
        
        scenario3 = VGroup(
            Text("③ 数论问题", font_size=20, color=Colors.STRONG_COLOR),
            Text("如算术基本定理（质因数分解）", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        scenarios.add(scenario3)
        
        scenarios.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        scenarios.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for scenario in scenarios:
            self.play(FadeIn(scenario, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.5)
        
        # 关键提示
        tip = VGroup(
            Text("关键提示：", font_size=18, color=Colors.SECONDARY),
            Text("当证明 P(n) 需要用到 P(k)（k < n-1）时，使用强归纳法", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        tip.next_to(scenarios, DOWN, buff=0.5).set_x(0)
        
        tip_box = SurroundingRectangle(tip, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(tip), Create(tip_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(scenarios),
            FadeOut(tip), FadeOut(tip_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_03_strong_induction.py StrongInduction
    pass
