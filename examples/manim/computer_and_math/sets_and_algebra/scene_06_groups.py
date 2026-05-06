"""
Scene 6: 群论入门
介绍群的四条公理和常见例子
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    SET_A = "#E74C3C"        # 集合A颜色
    SET_B = "#3498DB"        # 集合B颜色
    INTERSECTION = "#9B59B6" # 交集颜色
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


def create_axiom_card(number, name, description, formula, width=6, height=1.2):
    """创建公理卡片"""
    card = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.15,
        fill_color=Colors.BG,
        fill_opacity=0.5,
        stroke_color=Colors.PRIMARY,
        stroke_width=2
    )
    
    # 编号
    num_circle = Circle(radius=0.2)
    num_circle.set_fill(Colors.PRIMARY, opacity=0.8)
    num_circle.set_stroke(width=0)
    num_text = Text(str(number), font_size=16, color=Colors.BG)
    num_text.move_to(num_circle.get_center())
    num_group = VGroup(num_circle, num_text)
    num_group.move_to(card.get_left() + RIGHT * 0.4)
    
    # 名称
    name_text = Text(name, font_size=16, color=Colors.TEXT)
    name_text.next_to(num_group, RIGHT, buff=0.2)
    
    # 描述
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.next_to(name_text, DOWN, buff=0.1).align_to(name_text, LEFT)
    
    # 公式
    formula_tex = MathTex(formula, font_size=20, color=Colors.SECONDARY)
    formula_tex.move_to(card.get_right() + LEFT * 1.2)
    
    return VGroup(card, num_group, name_text, desc_text, formula_tex)


class Scene06Groups(Scene):
    """Scene 6: 群论入门"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_what_is_group()
        self.section_four_axioms()
        self.section_integer_group()
        self.section_non_group_example()
        self.section_applications()
        
        clear_scene(self)
    
    def section_what_is_group(self):
        """什么是群"""
        # 小节标题
        section_title = Text("什么是群？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("群 (Group) 是一个代数结构，由", font_size=18, color=Colors.GRAY),
            Text("一个集合 G 和一个二元运算 · 组成", font_size=18, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 符号表示
        notation = MathTex(r"(G, \cdot)", font_size=48, color=Colors.PRIMARY)
        notation.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(notation))
        self.wait(0.5)
        
        # 解释各部分
        explanations = VGroup(
            VGroup(
                MathTex("G", font_size=24, color=Colors.SET_A),
                Text(" - 一个非空集合", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\cdot", font_size=24, color=Colors.SET_B),
                Text(" - 一个二元运算 (如 +, ×, ∘)", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        explanations.next_to(notation, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(explanations))
        
        # 关键点
        key_point = VGroup(
            Text("关键: ", font_size=16, color=Colors.ACCENT),
            Text("必须满足四条公理！", font_size=16, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(explanations, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(notation),
            FadeOut(explanations),
            FadeOut(key_point),
            run_time=0.5
        )
    
    def section_four_axioms(self):
        """四条公理"""
        # 小节标题
        section_title = Text("群的四条公理", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建四张公理卡片
        axioms = [
            (1, "封闭性", "运算结果仍在集合内", r"a \cdot b \in G"),
            (2, "结合律", "运算顺序可以调整", r"(a \cdot b) \cdot c = a \cdot (b \cdot c)"),
            (3, "单位元", '存在一个"不变"元素', r"\exists e: e \cdot a = a \cdot e = a"),
            (4, "逆元", '每个元素有"反"元素', r"\forall a, \exists a^{-1}: a \cdot a^{-1} = e"),
        ]
        
        cards = VGroup()
        for num, name, desc, formula in axioms:
            card = create_axiom_card(num, name, desc, formula, width=5.5, height=1.0)
            cards.add(card)
        
        cards.arrange(DOWN, buff=0.2)
        cards.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.5)
            self.wait(0.2)
        
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(cards),
            run_time=0.5
        )
    
    def section_integer_group(self):
        """整数加法群"""
        # 小节标题
        section_title = VGroup(
            Text("例子: 整数加法群 ", font_size=26, color=Colors.TEXT),
            MathTex(r"(\mathbb{Z}, +)", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 数轴可视化
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_numbers=True,
            include_tip=True,
            color=Colors.GRAY
        )
        number_line.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(Create(number_line))
        self.wait(0.3)
        
        # 验证四条公理
        verifications = VGroup(
            VGroup(
                Text("封闭性: ", font_size=14, color=Colors.TEXT),
                MathTex(r"3 + 5 = 8 \in \mathbb{Z}", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("结合律: ", font_size=14, color=Colors.TEXT),
                MathTex(r"(1+2)+3 = 1+(2+3) = 6", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("单位元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"e = 0", font_size=18, color=Colors.PRIMARY),
                Text(", ", font_size=14, color=Colors.TEXT),
                MathTex(r"a + 0 = a", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("逆元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"a^{-1} = -a", font_size=18, color=Colors.PRIMARY),
                Text(", ", font_size=14, color=Colors.TEXT),
                MathTex(r"3 + (-3) = 0", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        verifications.next_to(number_line, DOWN, buff=0.5).set_x(0)
        
        for ver in verifications:
            self.play(FadeIn(ver, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        
        # 高亮 0 作为单位元
        zero_highlight = Circle(radius=0.2, color=Colors.PRIMARY, stroke_width=3)
        zero_highlight.move_to(number_line.n2p(0))
        
        self.play(Create(zero_highlight))
        self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            MathTex(r"(\mathbb{Z}, +)", font_size=28, color=Colors.PRIMARY),
            Text(" 是一个群！", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.to_edge(DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(conclusion))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(number_line),
            FadeOut(zero_highlight),
            FadeOut(verifications),
            FadeOut(conclusion),
            run_time=0.5
        )
    
    def section_non_group_example(self):
        """反例：自然数加法"""
        # 小节标题
        section_title = VGroup(
            Text("反例: 自然数加法 ", font_size=26, color=Colors.TEXT),
            MathTex(r"(\mathbb{N}, +)", font_size=28, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 为什么不是群
        explanation = Text("为什么自然数加法不是群？", font_size=20, color=Colors.GRAY)
        explanation.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        
        # 检查公理
        checks = VGroup(
            VGroup(
                Text("封闭性: ", font_size=14, color=Colors.TEXT),
                MathTex(r"3 + 5 = 8 \in \mathbb{N}", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("结合律: ", font_size=14, color=Colors.TEXT),
                MathTex(r"(1+2)+3 = 1+(2+3)", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("单位元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"e = 0", font_size=18, color=Colors.SECONDARY),
                Text(" ✓", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("逆元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"5^{-1} = -5 \notin \mathbb{N}", font_size=18, color=Colors.ACCENT),
                Text(" ✗", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        checks.next_to(explanation, DOWN, buff=0.4).set_x(0)
        
        for i, check in enumerate(checks):
            self.play(FadeIn(check, shift=RIGHT * 0.2), run_time=0.4)
            if i == 3:  # 最后一条，强调
                self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            Text("自然数中", font_size=18, color=Colors.TEXT),
            Text("没有负数", font_size=18, color=Colors.ACCENT),
            Text("，无法满足逆元公理！", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(checks, DOWN, buff=0.5).set_x(0)
        
        box = SurroundingRectangle(conclusion, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(box))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(explanation),
            FadeOut(checks),
            FadeOut(conclusion),
            FadeOut(box),
            run_time=0.5
        )
    
    def section_applications(self):
        """群的应用"""
        # 小节标题
        section_title = Text("群的应用", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 应用示例
        applications = VGroup(
            VGroup(
                Text("🕐", font_size=24),
                Text(" 时钟算术: ", font_size=16, color=Colors.TEXT),
                MathTex(r"(\mathbb{Z}_{12}, +)", font_size=20, color=Colors.PRIMARY),
                Text(" - 模12加法群", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("🎲", font_size=24),
                Text(" 魔方变换: ", font_size=16, color=Colors.TEXT),
                Text("旋转操作构成一个群", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("🔐", font_size=24),
                Text(" 密码学: ", font_size=16, color=Colors.TEXT),
                Text("RSA、椭圆曲线密码基于群论", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("⚛️", font_size=24),
                Text(" 物理学: ", font_size=16, color=Colors.TEXT),
                Text("对称性与守恒定律", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        applications.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for app in applications:
            self.play(FadeIn(app, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        
        # 洞见
        insight = VGroup(
            Text("抽象代数的威力:", font_size=18, color=Colors.PRIMARY),
            Text("用统一的语言描述不同领域的结构", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        insight.to_edge(DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(insight))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_06_groups.py Scene06Groups
    pass
