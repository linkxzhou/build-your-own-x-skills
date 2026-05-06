"""
函数与关系 - Scene 6: 等价关系
介绍等价关系的定义、性质、等价类和应用

渲染命令: manim -pqh scene_06_equivalence.py EquivalenceRelation
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
    FUNCTION_COLOR = "#E74C3C"   # 函数红
    RELATION_COLOR = "#9B59B6"   # 关系紫
    SET_COLOR = "#3498DB"        # 集合蓝
    EQUIV_COLOR = "#2ECC71"      # 等价绿
    REFLEXIVE_COLOR = "#F1C40F"  # 自反黄
    SYMMETRIC_COLOR = "#E74C3C"  # 对称红
    TRANSITIVE_COLOR = "#3498DB" # 传递蓝
    CLASS1_COLOR = "#E74C3C"     # 等价类1
    CLASS2_COLOR = "#3498DB"     # 等价类2
    CLASS3_COLOR = "#2ECC71"     # 等价类3


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


# ========== Scene 6: 等价关系 ==========
class EquivalenceRelation(Scene):
    """等价关系的定义、性质和应用"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.intro()
        self.definition()
        self.examples()
        self.equivalence_classes()
        self.construct_numbers()
        
        clear_scene(self)
    
    def intro(self):
        """引入"""
        section_title = Text("等价关系", font_size=28, color=Colors.EQUIV_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = VGroup(
            Text("在所有关系中，有一类特别重要的关系", font_size=16, color=Colors.GRAY),
            Text("它能把集合划分成若干"等价"的部分", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        
        question = Text(
            '什么样的关系才能表达"等价"的概念？',
            font_size=18, color=Colors.SECONDARY
        )
        question.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(question), run_time=0.5)
    
    def definition(self):
        """等价关系的定义"""
        section_title = Text("等价关系的定义", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 前提
        premise = Text(
            "在集合 S 上的二元关系 R，如果满足以下三条性质：",
            font_size=16, color=Colors.GRAY
        )
        premise.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(premise))
        
        # 三条性质
        properties = VGroup()
        
        # 自反性
        reflexive = VGroup(
            Text("1. 自反性 (Reflexive)", font_size=16, color=Colors.REFLEXIVE_COLOR),
            MathTex(r"\forall s \in S: (s, s) \in R", font_size=20, color=Colors.TEXT),
            Text("每个元素与自己相关", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(reflexive)
        
        # 对称性
        symmetric = VGroup(
            Text("2. 对称性 (Symmetric)", font_size=16, color=Colors.SYMMETRIC_COLOR),
            MathTex(r"(a, b) \in R \Rightarrow (b, a) \in R", font_size=20, color=Colors.TEXT),
            Text("关系是双向的", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(symmetric)
        
        # 传递性
        transitive = VGroup(
            Text("3. 传递性 (Transitive)", font_size=16, color=Colors.TRANSITIVE_COLOR),
            MathTex(r"(a, b) \in R \land (b, c) \in R \Rightarrow (a, c) \in R", font_size=18, color=Colors.TEXT),
            Text('等价关系可以"传递"', font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(transitive)
        
        properties.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        properties.next_to(premise, DOWN, buff=0.3).shift(LEFT * 0.5)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        
        # 结论
        conclusion = VGroup(
            Text("则称 R 是 S 上的", font_size=16, color=Colors.TEXT),
            Text("等价关系", font_size=18, color=Colors.EQUIV_COLOR),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(properties, DOWN, buff=0.4).set_x(0)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.EQUIV_COLOR, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(premise), FadeOut(properties),
            FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    def examples(self):
        """经典例子"""
        section_title = Text("等价关系的例子", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        examples = VGroup()
        
        # 例1：相等关系
        ex1 = VGroup(
            Text("1. 整数的相等关系", font_size=16, color=Colors.PRIMARY),
            Text("a = b", font_size=14, color=Colors.TEXT),
            Text("✓ 自反：a = a", font_size=11, color=Colors.REFLEXIVE_COLOR),
            Text("✓ 对称：a = b → b = a", font_size=11, color=Colors.SYMMETRIC_COLOR),
            Text("✓ 传递：a = b ∧ b = c → a = c", font_size=11, color=Colors.TRANSITIVE_COLOR),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        examples.add(ex1)
        
        # 例2：模n同余
        ex2 = VGroup(
            Text("2. 模 n 同余关系", font_size=16, color=Colors.PRIMARY),
            Text("a ≡ b (mod n)", font_size=14, color=Colors.TEXT),
            Text("即 a 和 b 除以 n 余数相同", font_size=11, color=Colors.GRAY),
            Text("✓ 满足所有三条性质", font_size=11, color=Colors.EQUIV_COLOR),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        examples.add(ex2)
        
        # 例3：三角形相似
        ex3 = VGroup(
            Text("3. 三角形的相似关系", font_size=16, color=Colors.PRIMARY),
            Text("△ABC ∼ △DEF", font_size=14, color=Colors.TEXT),
            Text("✓ 自反：任何三角形与自己相似", font_size=11, color=Colors.REFLEXIVE_COLOR),
            Text("✓ 对称/传递：显然成立", font_size=11, color=Colors.EQUIV_COLOR),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        examples.add(ex3)
        
        examples.arrange(RIGHT, buff=0.5, aligned_edge=UP)
        examples.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=UP * 0.2), run_time=0.5)
        
        # 反例
        counter_title = Text("反例：", font_size=16, color=Colors.ACCENT)
        counter_title.next_to(examples, DOWN, buff=0.4).align_to(examples, LEFT)
        
        counter = VGroup(
            Text('"小于等于" ≤ 不是等价关系', font_size=14, color=Colors.TEXT),
            Text("✗ 不满足对称性：a ≤ b 不能推出 b ≤ a", font_size=12, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        counter.next_to(counter_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(counter_title), FadeIn(counter))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(examples),
            FadeOut(counter_title), FadeOut(counter),
            run_time=0.5
        )
    
    def equivalence_classes(self):
        """等价类"""
        section_title = Text("等价类", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 核心概念
        concept = VGroup(
            Text("等价关系把集合划分成", font_size=16, color=Colors.GRAY),
            Text("互不相交的子集", font_size=18, color=Colors.EQUIV_COLOR),
        ).arrange(RIGHT, buff=0.1)
        concept.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(concept))
        
        definition = VGroup(
            Text("每个子集称为一个", font_size=14, color=Colors.GRAY),
            Text("等价类", font_size=16, color=Colors.EQUIV_COLOR),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(concept, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 可视化：模3同余
        example_title = Text('例：整数的"模3同余"关系', font_size=16, color=Colors.PRIMARY)
        example_title.next_to(definition, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example_title))
        
        # 三个等价类
        # 类0：余数为0
        class0 = VGroup(
            Ellipse(width=2.5, height=1.2, color=Colors.CLASS1_COLOR, stroke_width=2),
        )
        class0[0].set_fill(Colors.CLASS1_COLOR, opacity=0.15)
        class0_elements = Text("..., -6, -3, 0, 3, 6, ...", font_size=12, color=Colors.CLASS1_COLOR)
        class0_elements.move_to(class0[0].get_center())
        class0_label = Text("[0]₃", font_size=14, color=Colors.CLASS1_COLOR)
        class0_label.next_to(class0[0], UP, buff=0.1)
        class0.add(class0_elements, class0_label)
        
        # 类1：余数为1
        class1 = VGroup(
            Ellipse(width=2.5, height=1.2, color=Colors.CLASS2_COLOR, stroke_width=2),
        )
        class1[0].set_fill(Colors.CLASS2_COLOR, opacity=0.15)
        class1_elements = Text("..., -5, -2, 1, 4, 7, ...", font_size=12, color=Colors.CLASS2_COLOR)
        class1_elements.move_to(class1[0].get_center())
        class1_label = Text("[1]₃", font_size=14, color=Colors.CLASS2_COLOR)
        class1_label.next_to(class1[0], UP, buff=0.1)
        class1.add(class1_elements, class1_label)
        
        # 类2：余数为2
        class2 = VGroup(
            Ellipse(width=2.5, height=1.2, color=Colors.CLASS3_COLOR, stroke_width=2),
        )
        class2[0].set_fill(Colors.CLASS3_COLOR, opacity=0.15)
        class2_elements = Text("..., -4, -1, 2, 5, 8, ...", font_size=12, color=Colors.CLASS3_COLOR)
        class2_elements.move_to(class2[0].get_center())
        class2_label = Text("[2]₃", font_size=14, color=Colors.CLASS3_COLOR)
        class2_label.next_to(class2[0], UP, buff=0.1)
        class2.add(class2_elements, class2_label)
        
        classes = VGroup(class0, class1, class2).arrange(RIGHT, buff=0.3)
        classes.next_to(example_title, DOWN, buff=0.3).set_x(0)
        
        for c in classes:
            self.play(FadeIn(c, scale=0.8), run_time=0.5)
        
        # 说明
        note = VGroup(
            Text("• 同一等价类中的元素彼此等价", font_size=12, color=Colors.GRAY),
            Text("• 不同等价类的元素不等价", font_size=12, color=Colors.GRAY),
            Text("• 等价类覆盖整个集合且互不相交", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        note.next_to(classes, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(concept), FadeOut(definition),
            FadeOut(example_title), FadeOut(classes), FadeOut(note),
            run_time=0.5
        )
    
    def construct_numbers(self):
        """用等价关系构建数集"""
        section_title = Text("用等价关系构建数集", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text(
            "等价关系是数学家构造新数集的重要工具",
            font_size=16, color=Colors.GRAY
        )
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 构造整数
        int_title = Text("从自然数构造整数：", font_size=16, color=Colors.PRIMARY)
        int_title.next_to(intro, DOWN, buff=0.4).align_to(intro, LEFT)
        
        int_idea = VGroup(
            Text("用自然数对 (a, b) 表示 a - b", font_size=14, color=Colors.GRAY),
            Text("定义等价关系：(a, b) ∼ (c, d) ⟺ a + d = b + c", font_size=13, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        int_idea.next_to(int_title, DOWN, buff=0.15)
        
        int_example = VGroup(
            Text("例：(5, 3) ∼ (7, 5) ∼ (2, 0)", font_size=12, color=Colors.EQUIV_COLOR),
            Text("它们都表示整数 2", font_size=12, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.3)
        int_example.next_to(int_idea, DOWN, buff=0.1)
        
        self.play(FadeIn(int_title))
        self.play(FadeIn(int_idea))
        self.play(FadeIn(int_example))
        
        # 构造有理数
        rat_title = Text("从整数构造有理数：", font_size=16, color=Colors.SECONDARY)
        rat_title.next_to(int_example, DOWN, buff=0.4).align_to(int_title, LEFT)
        
        rat_idea = VGroup(
            Text("用整数对 (m, n) 表示 m/n (n ≠ 0)", font_size=14, color=Colors.GRAY),
            Text("定义等价关系：(m, n) ∼ (p, q) ⟺ m·q = n·p", font_size=13, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        rat_idea.next_to(rat_title, DOWN, buff=0.15)
        
        rat_example = VGroup(
            Text("例：(1, 2) ∼ (2, 4) ∼ (3, 6)", font_size=12, color=Colors.EQUIV_COLOR),
            Text("它们都表示有理数 1/2", font_size=12, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.3)
        rat_example.next_to(rat_idea, DOWN, buff=0.1)
        
        self.play(FadeIn(rat_title))
        self.play(FadeIn(rat_idea))
        self.play(FadeIn(rat_example))
        
        # 核心思想
        insight = Text(
            "等价类成为新的数学对象！",
            font_size=18, color=Colors.ACCENT
        )
        insight.next_to(rat_example, DOWN, buff=0.4).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.ACCENT, buff=0.1)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(intro),
            FadeOut(int_title), FadeOut(int_idea), FadeOut(int_example),
            FadeOut(rat_title), FadeOut(rat_idea), FadeOut(rat_example),
            FadeOut(insight), FadeOut(insight_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_06_equivalence.py EquivalenceRelation
    pass
