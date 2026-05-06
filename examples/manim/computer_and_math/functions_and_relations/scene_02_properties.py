"""
函数与关系 - Scene 2: 函数的特殊性质
介绍单射、满射、双射的概念

渲染命令: manim -pqh scene_02_properties.py FunctionProperties
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
    DOMAIN_COLOR = "#E67E22"     # 定义域橙
    CODOMAIN_COLOR = "#27AE60"   # 值域绿
    ARROW_COLOR = "#F1C40F"      # 箭头黄
    SURJECTIVE_COLOR = "#2ECC71" # 满射绿
    INJECTIVE_COLOR = "#E74C3C"  # 单射红
    BIJECTIVE_COLOR = "#9B59B6"  # 双射紫


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_mapping_arrow(start_pos, end_pos, color=Colors.ARROW_COLOR):
    """创建映射箭头"""
    arrow = Arrow(
        start_pos, end_pos,
        color=color,
        stroke_width=2,
        buff=0.1,
        max_tip_length_to_length_ratio=0.15
    )
    return arrow


def create_property_diagram(s_elems, t_elems, mappings, title_text, title_color, 
                           highlight_targets=None, highlight_sources=None):
    """创建性质演示图
    
    Args:
        s_elems: 定义域元素列表
        t_elems: 值域元素列表
        mappings: 映射列表，每个元素是 (s_index, t_index)
        title_text: 标题文字
        title_color: 标题颜色
        highlight_targets: 需要高亮的值域元素索引列表
        highlight_sources: 需要高亮的定义域元素索引列表
    """
    group = VGroup()
    
    # 定义域椭圆
    s_ellipse = Ellipse(width=1.6, height=2.4)
    s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
    s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
    
    s_texts = VGroup()
    for elem in s_elems:
        t = Text(str(elem), font_size=20, color=Colors.TEXT)
        s_texts.add(t)
    s_texts.arrange(DOWN, buff=0.35)
    s_texts.move_to(s_ellipse.get_center())
    
    # 值域椭圆
    t_ellipse = Ellipse(width=1.6, height=2.4)
    t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
    t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
    t_ellipse.shift(RIGHT * 2.2)
    
    t_texts = VGroup()
    for i, elem in enumerate(t_elems):
        color = title_color if highlight_targets and i in highlight_targets else Colors.TEXT
        t = Text(str(elem), font_size=20, color=color)
        t_texts.add(t)
    t_texts.arrange(DOWN, buff=0.35)
    t_texts.move_to(t_ellipse.get_center())
    
    # 高亮定义域元素
    if highlight_sources:
        for i in highlight_sources:
            s_texts[i].set_color(title_color)
    
    # 标签
    s_label = Text("S", font_size=16, color=Colors.DOMAIN_COLOR)
    s_label.next_to(s_ellipse, UP, buff=0.1)
    
    t_label = Text("T", font_size=16, color=Colors.CODOMAIN_COLOR)
    t_label.next_to(t_ellipse, UP, buff=0.1)
    
    # 箭头
    arrows = VGroup()
    for s_idx, t_idx in mappings:
        arrow = create_mapping_arrow(
            s_texts[s_idx].get_right() + RIGHT * 0.05,
            t_texts[t_idx].get_left() + LEFT * 0.05,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow)
    
    # 标题
    title = Text(title_text, font_size=16, color=title_color)
    
    diagram = VGroup(s_ellipse, s_texts, s_label, t_ellipse, t_texts, t_label, arrows)
    title.next_to(diagram, UP, buff=0.2)
    
    group.add(title, diagram)
    return group


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== Scene 2: 函数的特殊性质 ==========
class FunctionProperties(Scene):
    """介绍单射、满射、双射"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.intro()
        self.surjective()
        self.injective()
        self.bijective()
        self.comparison()
        
        clear_scene(self)
    
    def intro(self):
        """引入"""
        section_title = Text("函数的特殊性质", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = VGroup(
            Text("并非所有函数都一样", font_size=18, color=Colors.GRAY),
            Text("有些函数具有特殊的性质，让它们更有用", font_size=18, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        intro.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intro))
        
        properties = VGroup(
            Text("满射 (Surjective/Onto)", font_size=18, color=Colors.SURJECTIVE_COLOR),
            Text("单射 (Injective/One-to-One)", font_size=18, color=Colors.INJECTIVE_COLOR),
            Text("双射 (Bijective)", font_size=18, color=Colors.BIJECTIVE_COLOR),
        ).arrange(DOWN, buff=0.2)
        properties.next_to(intro, DOWN, buff=0.5).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(properties), run_time=0.5)
    
    def surjective(self):
        """满射"""
        section_title = Text("满射 (Surjective / Onto)", font_size=26, color=Colors.SURJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("定义：", font_size=18, color=Colors.TEXT),
            Text("T 中每个元素都被至少一个 S 元素指向", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 数学表示
        math_def = MathTex(
            r"\forall t \in T, \exists s \in S: f(s) = t",
            font_size=22, color=Colors.TEXT
        )
        math_def.next_to(definition, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(math_def))
        
        # 可视化
        # 满射示例: S = {a, b, c}, T = {1, 2}
        # a→1, b→2, c→2  (所有T元素都被指向)
        surj_example = create_property_diagram(
            ['a', 'b', 'c'], ['1', '2'],
            [(0, 0), (1, 1), (2, 1)],
            "✓ 满射",
            Colors.SURJECTIVE_COLOR,
            highlight_targets=[0, 1]  # 所有T元素都高亮
        )
        
        # 非满射示例: S = {a, b}, T = {1, 2, 3}
        # a→1, b→2  (3没有被指向)
        not_surj_example = create_property_diagram(
            ['a', 'b'], ['1', '2', '3'],
            [(0, 0), (1, 1)],
            "✗ 非满射",
            Colors.ACCENT,
            highlight_targets=[2]  # 3没有被指向
        )
        
        examples = VGroup(surj_example, not_surj_example).arrange(RIGHT, buff=1.0)
        examples.next_to(math_def, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(surj_example), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(not_surj_example), run_time=0.6)
        
        # 类比
        analogy = Text('类比："所有座位都坐满了"', font_size=16, color=Colors.SECONDARY)
        analogy.next_to(examples, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(math_def),
            FadeOut(examples), FadeOut(analogy),
            run_time=0.5
        )
    
    def injective(self):
        """单射"""
        section_title = Text("单射 (Injective / One-to-One)", font_size=26, color=Colors.INJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("定义：", font_size=18, color=Colors.TEXT),
            Text("S 中不同元素对应 T 中不同元素", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 数学表示
        math_def = MathTex(
            r"s_1 \neq s_2 \Rightarrow f(s_1) \neq f(s_2)",
            font_size=22, color=Colors.TEXT
        )
        math_def.next_to(definition, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(math_def))
        
        # 单射示例: S = {a, b}, T = {1, 2, 3}
        # a→1, b→2  (不同元素对应不同值)
        inj_example = create_property_diagram(
            ['a', 'b'], ['1', '2', '3'],
            [(0, 0), (1, 1)],
            "✓ 单射",
            Colors.INJECTIVE_COLOR
        )
        
        # 非单射示例: S = {a, b, c}, T = {1, 2}
        # a→1, b→2, c→2  (b和c对应同一个值)
        not_inj_example = create_property_diagram(
            ['a', 'b', 'c'], ['1', '2'],
            [(0, 0), (1, 1), (2, 1)],
            "✗ 非单射",
            Colors.ACCENT,
            highlight_sources=[1, 2],  # b和c高亮
            highlight_targets=[1]       # 2被重复指向
        )
        
        examples = VGroup(inj_example, not_inj_example).arrange(RIGHT, buff=1.0)
        examples.next_to(math_def, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(inj_example), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(not_inj_example), run_time=0.6)
        
        # 类比
        analogy = Text('类比："没有两人坐同一座位"', font_size=16, color=Colors.SECONDARY)
        analogy.next_to(examples, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(math_def),
            FadeOut(examples), FadeOut(analogy),
            run_time=0.5
        )
    
    def bijective(self):
        """双射"""
        section_title = Text("双射 (Bijection)", font_size=26, color=Colors.BIJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("定义：", font_size=18, color=Colors.TEXT),
            Text("既是满射又是单射", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 说明
        explanation = VGroup(
            Text("• 每个 T 元素都被指向（满射）", font_size=14, color=Colors.SURJECTIVE_COLOR),
            Text("• 每个 T 元素最多被指向一次（单射）", font_size=14, color=Colors.INJECTIVE_COLOR),
            Text("→ 每个 T 元素恰好被指向一次", font_size=14, color=Colors.BIJECTIVE_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanation.next_to(definition, DOWN, buff=0.3).align_to(definition, LEFT)
        
        self.play(FadeIn(explanation))
        
        # 双射示例
        bij_example = create_property_diagram(
            ['a', 'b', 'c'], ['1', '2', '3'],
            [(0, 0), (1, 1), (2, 2)],
            "✓ 双射：完美一一对应",
            Colors.BIJECTIVE_COLOR
        )
        bij_example.next_to(explanation, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(bij_example))
        
        # 重要性质
        property_box = VGroup(
            Text("重要性质：", font_size=16, color=Colors.PRIMARY),
            Text("双射函数存在反函数", font_size=16, color=Colors.TEXT),
            MathTex(r"f^{-1}: T \rightarrow S", font_size=20, color=Colors.BIJECTIVE_COLOR),
        ).arrange(DOWN, buff=0.1)
        property_box.next_to(bij_example, DOWN, buff=0.4).set_x(0)
        
        box = SurroundingRectangle(property_box, color=Colors.BIJECTIVE_COLOR, buff=0.15)
        
        self.play(FadeIn(property_box), Create(box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(explanation),
            FadeOut(bij_example), FadeOut(property_box), FadeOut(box),
            run_time=0.5
        )
    
    def comparison(self):
        """对比总结"""
        section_title = Text("三种性质对比", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建对比卡片
        cards = VGroup()
        
        # 满射卡片
        surj_card = VGroup(
            Text("满射", font_size=18, color=Colors.SURJECTIVE_COLOR),
            Text("T 中每个元素", font_size=12, color=Colors.GRAY),
            Text("都被指向", font_size=12, color=Colors.GRAY),
            MathTex(r"|S| \geq |T|", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        surj_box = SurroundingRectangle(surj_card, color=Colors.SURJECTIVE_COLOR, buff=0.15)
        cards.add(VGroup(surj_box, surj_card))
        
        # 单射卡片
        inj_card = VGroup(
            Text("单射", font_size=18, color=Colors.INJECTIVE_COLOR),
            Text("T 中每个元素", font_size=12, color=Colors.GRAY),
            Text("最多被指向一次", font_size=12, color=Colors.GRAY),
            MathTex(r"|S| \leq |T|", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        inj_box = SurroundingRectangle(inj_card, color=Colors.INJECTIVE_COLOR, buff=0.15)
        cards.add(VGroup(inj_box, inj_card))
        
        # 双射卡片
        bij_card = VGroup(
            Text("双射", font_size=18, color=Colors.BIJECTIVE_COLOR),
            Text("满射 + 单射", font_size=12, color=Colors.GRAY),
            Text("一一对应", font_size=12, color=Colors.GRAY),
            MathTex(r"|S| = |T|", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        bij_box = SurroundingRectangle(bij_card, color=Colors.BIJECTIVE_COLOR, buff=0.15)
        cards.add(VGroup(bij_box, bij_card))
        
        cards.arrange(RIGHT, buff=0.5)
        cards.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
        
        # 箭头表示关系
        arrow1 = Arrow(
            cards[0].get_right() + RIGHT * 0.1,
            cards[2].get_left() + LEFT * 0.1 + UP * 0.3,
            color=Colors.GRAY, stroke_width=2, buff=0.1
        )
        arrow2 = Arrow(
            cards[1].get_right() + RIGHT * 0.1,
            cards[2].get_left() + LEFT * 0.1 + DOWN * 0.3,
            color=Colors.GRAY, stroke_width=2, buff=0.1
        )
        
        plus_sign = MathTex("+", font_size=24, color=Colors.GRAY)
        plus_sign.move_to((cards[2].get_left() + cards[1].get_right()) / 2)
        
        # 集合大小关系总结
        size_summary = Text(
            "集合大小关系决定了可能存在的函数类型",
            font_size=16, color=Colors.SECONDARY
        )
        size_summary.next_to(cards, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(size_summary))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(cards), FadeOut(size_summary),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_02_properties.py FunctionProperties
    pass
