"""
数学归纳法 - Scene 2: 弱归纳法
通过经典求和公式示例展示弱归纳法的完整证明过程

渲染命令: manim -pqh scene_02_weak_induction.py WeakInduction
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
    FORMULA_COLOR = "#E67E22" # 公式橙


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


# ========== Scene 2: 弱归纳法 ==========
class WeakInduction(Scene):
    """弱归纳法及其经典例子"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.weak_induction_intro()
        self.sum_formula_example()
        self.divisibility_example()
        
        clear_scene(self)
    
    def weak_induction_intro(self):
        """弱归纳法介绍"""
        section_title = Text("弱归纳法（普通数学归纳法）", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 步骤框架
        step1_title = VGroup(
            Text("① 基础步骤", font_size=20, color=Colors.BASE_COLOR),
        )
        step1_content = VGroup(
            Text("证明 ", font_size=18, color=Colors.TEXT),
            MathTex(r"P(1)", font_size=24, color=Colors.BASE_COLOR),
            Text(" 成立", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        step1 = VGroup(step1_title, step1_content).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        
        step2_title = VGroup(
            Text("② 归纳步骤", font_size=20, color=Colors.INDUCT_COLOR),
        )
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
        
        # 关键点
        key_point = VGroup(
            Text("关键：", font_size=18, color=Colors.SECONDARY),
            Text('只需要假设"上一步" P(m) 成立', font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(steps, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(steps), FadeOut(key_point),
            run_time=0.5
        )
    
    def sum_formula_example(self):
        """经典例子：求和公式"""
        section_title = Text("经典例子：求和公式", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 命题
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
        
        # ===== 基础步骤 =====
        base_title = VGroup(
            Text("① 基础步骤", font_size=20, color=Colors.BASE_COLOR),
            Text("（n = 1）", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        base_title.next_to(prop_box, DOWN, buff=0.5).align_to(prop_box, LEFT)
        
        self.play(FadeIn(base_title))
        
        # 左边
        base_left = VGroup(
            Text("左边 = ", font_size=16, color=Colors.GRAY),
            MathTex(r"1", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        # 右边
        base_right = VGroup(
            Text("右边 = ", font_size=16, color=Colors.GRAY),
            MathTex(r"\frac{1 \times 2}{2} = 1", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        
        # 结论
        base_conclusion = VGroup(
            Text("左边 = 右边 ", font_size=16, color=Colors.TEXT),
            Text("✓", font_size=20, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        
        base_content = VGroup(base_left, base_right, base_conclusion).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        base_content.next_to(base_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        for item in base_content:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(0.8)
        
        # ===== 归纳步骤 =====
        induct_title = VGroup(
            Text("② 归纳步骤", font_size=20, color=Colors.INDUCT_COLOR),
        ).arrange(RIGHT, buff=0.1)
        induct_title.next_to(base_content, DOWN, buff=0.4).align_to(base_title, LEFT)
        
        self.play(FadeIn(induct_title))
        
        # 归纳假设
        hypothesis = VGroup(
            Text("归纳假设：", font_size=16, color=Colors.GRAY),
            Text("设 ", font_size=16, color=Colors.TEXT),
            MathTex(r"1+2+\cdots+m = \frac{m(m+1)}{2}", font_size=20, color=Colors.INDUCT_COLOR),
        ).arrange(RIGHT, buff=0.08)
        hypothesis.next_to(induct_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(FadeIn(hypothesis))
        self.wait(0.5)
        
        # 目标
        target = VGroup(
            Text("目标：证明 ", font_size=16, color=Colors.TEXT),
            MathTex(r"1+2+\cdots+m+(m+1) = \frac{(m+1)(m+2)}{2}", font_size=18, color=Colors.INDUCT_COLOR),
        ).arrange(RIGHT, buff=0.08)
        target.next_to(hypothesis, DOWN, buff=0.2).align_to(hypothesis, LEFT)
        
        self.play(FadeIn(target))
        self.wait(1)
        
        # 推导过程
        self.play(
            FadeOut(prop_box), FadeOut(prop_group),
            FadeOut(base_title), FadeOut(base_content),
            FadeOut(induct_title), FadeOut(hypothesis), FadeOut(target),
            run_time=0.5
        )
        
        # 详细推导
        derivation_title = Text("推导过程：", font_size=20, color=Colors.INDUCT_COLOR)
        derivation_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(derivation_title))
        
        # 第一步
        step1 = MathTex(
            r"1+2+\cdots+m+(m+1)",
            font_size=24, color=Colors.TEXT
        )
        step1.next_to(derivation_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(step1))
        self.wait(0.3)
        
        # 第二步：使用归纳假设
        step2_label = Text("代入归纳假设", font_size=14, color=Colors.GRAY)
        step2 = MathTex(
            r"= \frac{m(m+1)}{2} + (m+1)",
            font_size=24, color=Colors.TEXT
        )
        step2_group = VGroup(step2_label, step2).arrange(RIGHT, buff=0.2)
        step2_group.next_to(step1, DOWN, buff=0.2).align_to(step1, LEFT)
        
        # 高亮归纳假设部分
        highlight_box = SurroundingRectangle(
            MathTex(r"\frac{m(m+1)}{2}", font_size=24).move_to(step2.get_center() + LEFT * 0.3),
            color=Colors.INDUCT_COLOR, buff=0.05
        )
        
        self.play(FadeIn(step2_group))
        self.wait(0.5)
        
        # 第三步：提取公因子
        step3_label = Text("提取公因子", font_size=14, color=Colors.GRAY)
        step3 = MathTex(
            r"= (m+1) \left( \frac{m}{2} + 1 \right)",
            font_size=24, color=Colors.TEXT
        )
        step3_group = VGroup(step3_label, step3).arrange(RIGHT, buff=0.2)
        step3_group.next_to(step2_group, DOWN, buff=0.2).align_to(step2_group, LEFT)
        
        self.play(FadeIn(step3_group))
        self.wait(0.3)
        
        # 第四步：化简
        step4_label = Text("通分化简", font_size=14, color=Colors.GRAY)
        step4 = MathTex(
            r"= (m+1) \cdot \frac{m+2}{2}",
            font_size=24, color=Colors.TEXT
        )
        step4_group = VGroup(step4_label, step4).arrange(RIGHT, buff=0.2)
        step4_group.next_to(step3_group, DOWN, buff=0.2).align_to(step3_group, LEFT)
        
        self.play(FadeIn(step4_group))
        self.wait(0.3)
        
        # 第五步：结果
        step5_label = Text("得到", font_size=14, color=Colors.GRAY)
        step5 = MathTex(
            r"= \frac{(m+1)(m+2)}{2}",
            font_size=24, color=Colors.INDUCT_COLOR
        )
        step5_group = VGroup(step5_label, step5).arrange(RIGHT, buff=0.2)
        step5_group.next_to(step4_group, DOWN, buff=0.2).align_to(step4_group, LEFT)
        
        self.play(FadeIn(step5_group))
        
        # 结论框
        conclusion = VGroup(
            Text("证毕！", font_size=20, color=Colors.BASE_COLOR),
            Text("P(m+1) 成立 ✓", font_size=18, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        conclusion.next_to(step5_group, DOWN, buff=0.4).set_x(0)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.BASE_COLOR, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(derivation_title),
            FadeOut(step1), FadeOut(step2_group), FadeOut(step3_group),
            FadeOut(step4_group), FadeOut(step5_group),
            FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    def divisibility_example(self):
        """另一个例子：整除性"""
        section_title = Text("另一个例子：整除性", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 命题
        proposition_label = Text("命题 P(n)：", font_size=18, color=Colors.PRIMARY)
        proposition = MathTex(
            r"2^{2n} - 1 \text{ 能被 } 3 \text{ 整除}",
            font_size=26, color=Colors.FORMULA_COLOR
        )
        # 修复：使用 VGroup 组合中文和数学公式
        proposition_fixed = VGroup(
            MathTex(r"2^{2n} - 1", font_size=26, color=Colors.FORMULA_COLOR),
            Text(" 能被 3 整除", font_size=20, color=Colors.FORMULA_COLOR),
        ).arrange(RIGHT, buff=0.1)
        
        prop_group = VGroup(proposition_label, proposition_fixed).arrange(DOWN, buff=0.1)
        prop_group.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        prop_box = SurroundingRectangle(prop_group, color=Colors.FORMULA_COLOR, buff=0.2)
        
        self.play(FadeIn(prop_group), Create(prop_box))
        self.wait(1)
        
        # 简化展示
        proof_title = Text("证明要点：", font_size=18, color=Colors.SECONDARY)
        proof_title.next_to(prop_box, DOWN, buff=0.5).align_to(prop_box, LEFT)
        
        self.play(FadeIn(proof_title))
        
        # 基础步骤
        base = VGroup(
            Text("① 基础步骤 (n=1)：", font_size=16, color=Colors.BASE_COLOR),
            MathTex(r"2^2 - 1 = 3", font_size=22, color=Colors.TEXT),
            Text("，能被3整除 ✓", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        base.next_to(proof_title, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        self.play(FadeIn(base))
        self.wait(0.5)
        
        # 归纳步骤关键
        induct_key = VGroup(
            Text("② 归纳步骤关键：", font_size=16, color=Colors.INDUCT_COLOR),
        )
        induct_key.next_to(base, DOWN, buff=0.3).align_to(base, LEFT)
        
        self.play(FadeIn(induct_key))
        
        # 推导
        induct_formula1 = MathTex(
            r"2^{2(m+1)} - 1 = 2^{2m+2} - 1 = 4 \cdot 2^{2m} - 1",
            font_size=20, color=Colors.TEXT
        )
        induct_formula1.next_to(induct_key, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(FadeIn(induct_formula1))
        self.wait(0.3)
        
        induct_formula2 = MathTex(
            r"= 4(2^{2m} - 1) + 4 - 1 = 4(2^{2m} - 1) + 3",
            font_size=20, color=Colors.TEXT
        )
        induct_formula2.next_to(induct_formula1, DOWN, buff=0.15).align_to(induct_formula1, LEFT)
        
        self.play(FadeIn(induct_formula2))
        self.wait(0.5)
        
        # 解释
        explanation = VGroup(
            Text("由归纳假设，", font_size=16, color=Colors.GRAY),
            MathTex(r"2^{2m}-1", font_size=20, color=Colors.INDUCT_COLOR),
            Text(" 能被3整除", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.08)
        explanation.next_to(induct_formula2, DOWN, buff=0.3).set_x(0)
        
        explanation2 = VGroup(
            Text("所以 ", font_size=16, color=Colors.TEXT),
            MathTex(r"4(2^{2m}-1) + 3", font_size=20, color=Colors.TEXT),
            Text(" 也能被3整除 ✓", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.08)
        explanation2.next_to(explanation, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(explanation))
        self.play(FadeIn(explanation2))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(prop_group), FadeOut(prop_box),
            FadeOut(proof_title), FadeOut(base), FadeOut(induct_key),
            FadeOut(induct_formula1), FadeOut(induct_formula2),
            FadeOut(explanation), FadeOut(explanation2),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_02_weak_induction.py WeakInduction
    pass
