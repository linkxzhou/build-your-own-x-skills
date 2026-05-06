"""
集合与抽象代数：从基础到无限
完整视频 - 包含所有场景

渲染命令:
- 预览质量: manim -pql all_scenes.py SetsAndAlgebra
- 高质量: manim -pqh all_scenes.py SetsAndAlgebra
- 生产质量: manim -pqk all_scenes.py SetsAndAlgebra

预计时长: 12-15 分钟
"""

from manim import *


# ============================================================
# 配色方案
# ============================================================
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


# ============================================================
# 工具函数
# ============================================================
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_element_circle(value, color=Colors.PRIMARY, radius=0.3):
    """创建一个元素圆圈"""
    circle = Circle(radius=radius)
    circle.set_fill(color, opacity=0.7)
    circle.set_stroke(Colors.TEXT, width=2)
    
    text = Text(str(value), font_size=int(radius * 60), color=Colors.TEXT)
    text.move_to(circle.get_center())
    
    return VGroup(circle, text)


def create_set_box(width=4, height=2.5, label="S", color=None):
    """创建集合容器"""
    stroke_color = color if color else Colors.PRIMARY
    box = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.3,
        fill_color=Colors.BG,
        fill_opacity=0.3,
        stroke_color=stroke_color,
        stroke_width=3
    )
    
    label_text = MathTex(label, font_size=28, color=stroke_color)
    label_text.next_to(box, UP, buff=0.2)
    
    return VGroup(box, label_text)


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
    
    num_circle = Circle(radius=0.2)
    num_circle.set_fill(Colors.PRIMARY, opacity=0.8)
    num_circle.set_stroke(width=0)
    num_text = Text(str(number), font_size=16, color=Colors.BG)
    num_text.move_to(num_circle.get_center())
    num_group = VGroup(num_circle, num_text)
    num_group.move_to(card.get_left() + RIGHT * 0.4)
    
    name_text = Text(name, font_size=16, color=Colors.TEXT)
    name_text.next_to(num_group, RIGHT, buff=0.2)
    
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.next_to(name_text, DOWN, buff=0.1).align_to(name_text, LEFT)
    
    formula_tex = MathTex(formula, font_size=20, color=Colors.SECONDARY)
    formula_tex.move_to(card.get_right() + LEFT * 1.2)
    
    return VGroup(card, num_group, name_text, desc_text, formula_tex)


def create_insight_card(icon, title, description, color, width=5, height=1.4):
    """创建启示卡片"""
    card = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.15,
        fill_color=Colors.BG,
        fill_opacity=0.5,
        stroke_color=color,
        stroke_width=2
    )
    
    icon_text = Text(icon, font_size=28)
    icon_text.move_to(card.get_left() + RIGHT * 0.5)
    
    title_text = Text(title, font_size=16, color=color)
    title_text.next_to(icon_text, RIGHT, buff=0.3)
    
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.next_to(title_text, DOWN, buff=0.1).align_to(title_text, LEFT)
    
    return VGroup(card, icon_text, title_text, desc_text)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ============================================================
# 韦恩图辅助类
# ============================================================
class VennDiagram:
    """韦恩图辅助类"""
    
    def __init__(self, center=ORIGIN, radius=1.2, separation=0.8, show_universe=False):
        self.center = center
        self.radius = radius
        self.separation = separation
        
        self.center_a = center + LEFT * separation / 2
        self.center_b = center + RIGHT * separation / 2
        
        self.circle_a = Circle(radius=radius)
        self.circle_a.set_stroke(Colors.SET_A, width=3)
        self.circle_a.set_fill(Colors.SET_A, opacity=0.2)
        self.circle_a.move_to(self.center_a)
        
        self.circle_b = Circle(radius=radius)
        self.circle_b.set_stroke(Colors.SET_B, width=3)
        self.circle_b.set_fill(Colors.SET_B, opacity=0.2)
        self.circle_b.move_to(self.center_b)
        
        self.universe = None
        if show_universe:
            self.universe = Rectangle(
                width=radius * 4, height=radius * 2.8,
                stroke_color=Colors.GRAY, stroke_width=2
            )
            self.universe.move_to(center)
        
        self.label_a = MathTex("A", font_size=28, color=Colors.SET_A)
        self.label_a.next_to(self.circle_a, UP + LEFT, buff=0.1)
        
        self.label_b = MathTex("B", font_size=28, color=Colors.SET_B)
        self.label_b.next_to(self.circle_b, UP + RIGHT, buff=0.1)
    
    def get_base_group(self):
        group = VGroup(self.circle_a, self.circle_b, self.label_a, self.label_b)
        if self.universe:
            group = VGroup(self.universe, self.circle_a, self.circle_b, self.label_a, self.label_b)
        return group
    
    def get_intersection_region(self):
        intersection = Intersection(self.circle_a, self.circle_b)
        intersection.set_stroke(width=0)
        intersection.set_fill(Colors.INTERSECTION, opacity=0.6)
        return intersection
    
    def get_union_region(self):
        union = Union(self.circle_a, self.circle_b)
        union.set_stroke(Colors.PRIMARY, width=3)
        union.set_fill(Colors.PRIMARY, opacity=0.4)
        return union
    
    def get_difference_a_b(self):
        diff = Difference(self.circle_a, self.circle_b)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.SET_A, opacity=0.6)
        return diff
    
    def get_symmetric_difference(self):
        diff_a = Difference(self.circle_a, self.circle_b)
        diff_a.set_stroke(width=0)
        diff_a.set_fill(Colors.SET_A, opacity=0.5)
        
        diff_b = Difference(self.circle_b, self.circle_a)
        diff_b.set_stroke(width=0)
        diff_b.set_fill(Colors.SET_B, opacity=0.5)
        
        return VGroup(diff_a, diff_b)
    
    def get_complement_union(self):
        if not self.universe:
            return VGroup()
        union = Union(self.circle_a, self.circle_b)
        diff = Difference(self.universe, union)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.ACCENT, opacity=0.5)
        return diff
    
    def get_complement_a_intersect_complement_b(self):
        if not self.universe:
            return VGroup()
        union = Union(self.circle_a, self.circle_b)
        diff = Difference(self.universe, union)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.ACCENT, opacity=0.5)
        return diff


# ============================================================
# 主场景类
# ============================================================
class SetsAndAlgebra(Scene):
    """集合与抽象代数 - 完整视频"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # Scene 1: 开场引入
        self.scene_01_intro()
        
        # Scene 2: 集合的表示方法
        self.scene_02_representation()
        
        # Scene 3: 集合运算与韦恩图
        self.scene_03_operations()
        
        # Scene 4: 子集与幂集
        self.scene_04_subsets()
        
        # Scene 5: 集合定律与德摩根定律
        self.scene_05_laws()
        
        # Scene 6: 群论入门
        self.scene_06_groups()
        
        # Scene 7: 无限的探索
        self.scene_07_infinity()
        
        # Scene 8: 总结与启示
        self.scene_08_summary()
    
    # ========================================================
    # Scene 1: 开场引入
    # ========================================================
    def scene_01_intro(self):
        # 开场标题
        main_title = Text("集合与抽象代数", font_size=48, color=Colors.PRIMARY)
        subtitle = Text("从基础到无限", font_size=28, color=Colors.GRAY)
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        self.play(
            FadeOut(subtitle),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
        
        # 集合概念介绍
        section_title = Text("集合 - 万物的基础", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        metaphor = Text("你可以把集合想象成一个'收纳盒'", font_size=22, color=Colors.GRAY)
        metaphor.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(metaphor))
        
        box = create_set_box(width=5, height=3, label="S")
        box.next_to(metaphor, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(box), run_time=0.8)
        
        elements = [1, 2, 5]
        element_circles = VGroup()
        final_positions = [
            box[0].get_center() + LEFT * 1.2,
            box[0].get_center(),
            box[0].get_center() + RIGHT * 1.2,
        ]
        
        for i, val in enumerate(elements):
            elem = create_element_circle(val, color=Colors.SECONDARY)
            elem.move_to(box[0].get_top() + UP * 1.5)
            element_circles.add(elem)
        
        for i, (elem, pos) in enumerate(zip(element_circles, final_positions)):
            self.play(elem.animate.move_to(pos), run_time=0.5)
        
        self.wait(0.5)
        
        properties = VGroup(
            Text("• 确定的元素", font_size=18, color=Colors.TEXT),
            Text("• 互不相同", font_size=18, color=Colors.TEXT),
            Text("• 可以是数字、字母、甚至其他集合", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        properties.next_to(box, DOWN, buff=0.4).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.3)
        
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(metaphor), FadeOut(box),
            FadeOut(element_circles), FadeOut(properties),
            run_time=0.5
        )
        
        # 数学符号表示
        section_title = Text("数学符号表示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        notation_intro = Text("用花括号 { } 包围元素:", font_size=20, color=Colors.GRAY)
        notation_intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(notation_intro))
        
        set_expr = MathTex(r"S = \{1, 2, 5\}", font_size=36, color=Colors.PRIMARY)
        set_expr.next_to(notation_intro, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(set_expr), run_time=1)
        
        cardinality_text = VGroup(
            Text("基数 (元素个数): ", font_size=20, color=Colors.TEXT),
            MathTex(r"|S| = 3", font_size=28, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        cardinality_text.next_to(set_expr, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(cardinality_text))
        
        element_notation = VGroup(
            Text("元素属于集合: ", font_size=20, color=Colors.TEXT),
            MathTex(r"1 \in S", font_size=28, color=Colors.SECONDARY),
            Text(", ", font_size=20, color=Colors.TEXT),
            MathTex(r"4 \notin S", font_size=28, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        element_notation.next_to(cardinality_text, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(element_notation))
        
        key_point = VGroup(
            Text("集合中", font_size=20, color=Colors.TEXT),
            Text("元素无序", font_size=20, color=Colors.SECONDARY),
            Text("且", font_size=20, color=Colors.TEXT),
            Text("不重复", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(element_notation, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        
        equivalence = MathTex(
            r"\{1, 2, 5\} = \{5, 1, 2\} = \{1, 1, 2, 5\}",
            font_size=24, color=Colors.GRAY
        )
        equivalence.next_to(key_point, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(equivalence))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 2: 集合的表示方法
    # ========================================================
    def scene_02_representation(self):
        # 列举法
        section_title = Text("列举法 - 逐一列出元素", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        desc = Text("直接写出集合中的所有元素", font_size=20, color=Colors.GRAY)
        desc.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(desc))
        
        examples = VGroup(
            VGroup(
                Text("数字集合: ", font_size=18, color=Colors.TEXT),
                MathTex(r"A = \{1, 2, 3, 4, 5\}", font_size=28, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("字母集合: ", font_size=18, color=Colors.TEXT),
                MathTex(r"B = \{a, b, c\}", font_size=28, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        examples.next_to(desc, DOWN, buff=0.5).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(desc), FadeOut(examples), run_time=0.5)
        
        # 描述法
        section_title = Text("描述法 - 用条件定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        format_text = VGroup(
            Text("格式: ", font_size=18, color=Colors.TEXT),
            MathTex(r"\{x \mid P(x)\}", font_size=32, color=Colors.PRIMARY),
            Text(' 读作 "满足条件 P(x) 的所有 x"', font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.15)
        format_text.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(format_text))
        
        example_set = MathTex(
            r"A = \{x \mid x \in \mathbb{Z}^+, x < 20, x \text{ mod } 2 = 0\}",
            font_size=24, color=Colors.SECONDARY
        )
        example_set.next_to(format_text, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(example_set), run_time=1)
        
        example_result = VGroup(
            Text("= ", font_size=18, color=Colors.TEXT),
            MathTex(r"\{2, 4, 6, 8, 10, 12, 14, 16, 18\}", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        example_result.next_to(example_set, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(example_result))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(format_text),
            FadeOut(example_set), FadeOut(example_result),
            run_time=0.5
        )
        
        # 重要数集
        section_title = Text("重要数集", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        sets_data = [
            ("C", "复数", 5.5, 3.0, "#9B59B6"),
            ("R", "实数", 4.4, 2.4, "#E74C3C"),
            ("Q", "有理数", 3.3, 1.8, "#F39C12"),
            ("Z", "整数", 2.2, 1.2, "#3498DB"),
            ("N", "自然数", 1.1, 0.6, "#2ECC71"),
        ]
        
        ellipses = VGroup()
        labels = VGroup()
        center = DOWN * 0.8
        
        for symbol, name, width, height, color in sets_data:
            ellipse = Ellipse(width=width, height=height)
            ellipse.set_stroke(color, width=2)
            ellipse.set_fill(color, opacity=0.1)
            ellipse.move_to(center)
            ellipses.add(ellipse)
            
            label = MathTex(r"\mathbb{" + symbol + "}", font_size=24, color=color)
            label.next_to(ellipse, RIGHT, buff=0.15)
            labels.add(label)
        
        for ellipse, label in zip(ellipses, labels):
            self.play(Create(ellipse), FadeIn(label), run_time=0.5)
        
        inclusion = MathTex(
            r"\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}",
            font_size=28, color=Colors.PRIMARY
        )
        inclusion.to_edge(DOWN, buff=0.8).set_x(0)
        
        self.play(Write(inclusion))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 3: 集合运算与韦恩图
    # ========================================================
    def scene_03_operations(self):
        # 介绍韦恩图
        section_title = Text("韦恩图 - 可视化集合关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        example_sets = VGroup(
            VGroup(
                MathTex("A", font_size=24, color=Colors.SET_A),
                MathTex(r"= \{1, 2, 3, 4\}", font_size=24, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex("B", font_size=24, color=Colors.SET_B),
                MathTex(r"= \{3, 4, 5, 6\}", font_size=24, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        example_sets.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example_sets))
        
        venn = VennDiagram(center=DOWN * 1.5, radius=1.3, separation=1.0)
        base = venn.get_base_group()
        
        self.play(Create(base), run_time=1)
        
        elem_a_only = MathTex(r"1, 2", font_size=18, color=Colors.TEXT)
        elem_a_only.move_to(venn.center_a + LEFT * 0.4)
        
        elem_common = MathTex(r"3, 4", font_size=18, color=Colors.TEXT)
        elem_common.move_to(venn.center)
        
        elem_b_only = MathTex(r"5, 6", font_size=18, color=Colors.TEXT)
        elem_b_only.move_to(venn.center_b + RIGHT * 0.4)
        
        self.play(FadeIn(elem_a_only), FadeIn(elem_common), FadeIn(elem_b_only))
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(example_sets), FadeOut(base),
            FadeOut(elem_a_only), FadeOut(elem_common), FadeOut(elem_b_only),
            run_time=0.5
        )
        
        # 并集
        section_title = VGroup(
            Text("并集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A \cup B", font_size=30, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = Text('"合并所有元素"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        
        union = venn.get_union_region()
        self.play(FadeIn(union), run_time=0.8)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} \cup \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{1,2,3,4,5,6\}", font_size=24, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.15)
        example.next_to(base, RIGHT, buff=0.8)
        
        self.play(FadeIn(example))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(base), FadeOut(union), FadeOut(example),
            run_time=0.5
        )
        
        # 交集
        section_title = VGroup(
            Text("交集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A \cap B", font_size=30, color=Colors.INTERSECTION),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = Text('"提取共有元素"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        
        intersection = venn.get_intersection_region()
        self.play(FadeIn(intersection), run_time=0.8)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} \cap \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{3,4\}", font_size=24, color=Colors.INTERSECTION),
        ).arrange(DOWN, buff=0.15)
        example.next_to(base, RIGHT, buff=0.8)
        
        self.play(FadeIn(example))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(base), FadeOut(intersection), FadeOut(example),
            run_time=0.5
        )
        
        # 差集
        section_title = VGroup(
            Text("差集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A - B", font_size=30, color=Colors.SET_A),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = Text('"属于A但不属于B"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        
        diff = venn.get_difference_a_b()
        self.play(FadeIn(diff), run_time=0.8)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} - \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{1,2\}", font_size=24, color=Colors.SET_A),
        ).arrange(DOWN, buff=0.15)
        example.next_to(base, RIGHT, buff=0.8)
        
        self.play(FadeIn(example))
        self.wait(1.5)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 4: 子集与幂集
    # ========================================================
    def scene_04_subsets(self):
        # 子集定义
        section_title = Text("子集 - 集合的包含关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("如果集合 B 中的每个元素都属于集合 A，", font_size=18, color=Colors.GRAY),
            Text("则称 B 是 A 的子集", font_size=18, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        notation = MathTex(r"B \subseteq A", font_size=36, color=Colors.PRIMARY)
        notation.next_to(definition, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(notation))
        
        big_circle = Circle(radius=1.5)
        big_circle.set_stroke(Colors.SET_A, width=3)
        big_circle.set_fill(Colors.SET_A, opacity=0.15)
        big_circle.move_to(DOWN * 1.2)
        
        small_circle = Circle(radius=0.7)
        small_circle.set_stroke(Colors.SET_B, width=3)
        small_circle.set_fill(Colors.SET_B, opacity=0.3)
        small_circle.move_to(DOWN * 1.2 + LEFT * 0.3)
        
        label_a = MathTex("A", font_size=24, color=Colors.SET_A)
        label_a.next_to(big_circle, UP + RIGHT, buff=0.1)
        
        label_b = MathTex("B", font_size=24, color=Colors.SET_B)
        label_b.move_to(small_circle.get_center())
        
        self.play(Create(big_circle), FadeIn(label_a))
        self.play(Create(small_circle), FadeIn(label_b))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(notation),
            FadeOut(big_circle), FadeOut(small_circle),
            FadeOut(label_a), FadeOut(label_b),
            run_time=0.5
        )
        
        # 幂集
        section_title = Text("幂集 - 所有子集的集合", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("幂集 ", font_size=20, color=Colors.TEXT),
            MathTex(r"\mathcal{P}(A)", font_size=26, color=Colors.PRIMARY),
            Text(" 是集合 A 的所有子集组成的集合", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        example_label = VGroup(
            Text("例: ", font_size=18, color=Colors.TEXT),
            MathTex(r"A = \{1, 2\}", font_size=24, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        example_label.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_label))
        
        power_set_result = MathTex(
            r"\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{1,2\}\}",
            font_size=26, color=Colors.PRIMARY
        )
        power_set_result.next_to(example_label, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(power_set_result))
        
        theorem = VGroup(
            Text("幂集定理: n 个元素 → ", font_size=18, color=Colors.TEXT),
            MathTex(r"2^n", font_size=28, color=Colors.ACCENT),
            Text(" 个子集", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        theorem.next_to(power_set_result, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(theorem))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 5: 集合定律与德摩根定律
    # ========================================================
    def scene_05_laws(self):
        # 基本定律
        section_title = Text("集合的基本定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        laws = VGroup(
            VGroup(
                Text("交换律: ", font_size=16, color=Colors.TEXT),
                MathTex(r"A \cup B = B \cup A", font_size=20, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("结合律: ", font_size=16, color=Colors.TEXT),
                MathTex(r"(A \cup B) \cup C = A \cup (B \cup C)", font_size=20, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("分配律: ", font_size=16, color=Colors.TEXT),
                MathTex(r"A \cap (B \cup C) = (A \cap B) \cup (A \cap C)", font_size=18, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        laws.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for law in laws:
            self.play(FadeIn(law, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(laws), run_time=0.5)
        
        # 德摩根定律
        section_title = Text("德摩根定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        law1 = MathTex(r"(A \cup B)' = A' \cap B'", font_size=32, color=Colors.PRIMARY)
        law2 = MathTex(r"(A \cap B)' = A' \cup B'", font_size=32, color=Colors.SECONDARY)
        
        laws = VGroup(law1, law2).arrange(DOWN, buff=0.4)
        laws.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(law1), run_time=0.8)
        self.play(Write(law2), run_time=0.8)
        
        explanation = VGroup(
            Text('"并集的补" = "各自补集的交"', font_size=16, color=Colors.GRAY),
            Text('"交集的补" = "各自补集的并"', font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        explanation.next_to(laws, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        
        # 编程应用
        programming = VGroup(
            Text("编程中:", font_size=16, color=Colors.PRIMARY),
            Text("!(a || b) == (!a && !b)", font_size=14, color=Colors.SECONDARY, font="Courier New"),
        ).arrange(RIGHT, buff=0.2)
        programming.next_to(explanation, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(programming))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 6: 群论入门
    # ========================================================
    def scene_06_groups(self):
        # 什么是群
        section_title = Text("什么是群？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("群 (Group) 是一个代数结构，由", font_size=18, color=Colors.GRAY),
            Text("一个集合 G 和一个二元运算 · 组成", font_size=18, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        notation = MathTex(r"(G, \cdot)", font_size=48, color=Colors.PRIMARY)
        notation.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(notation))
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(notation), run_time=0.5)
        
        # 四条公理
        section_title = Text("群的四条公理", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        axioms = [
            (1, "封闭性", "运算结果仍在集合内", r"a \cdot b \in G"),
            (2, "结合律", "运算顺序可以调整", r"(a \cdot b) \cdot c = a \cdot (b \cdot c)"),
            (3, "单位元", '存在一个"不变"元素', r"\exists e: e \cdot a = a"),
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
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(cards), run_time=0.5)
        
        # 整数加法群
        section_title = VGroup(
            Text("例子: 整数加法群 ", font_size=26, color=Colors.TEXT),
            MathTex(r"(\mathbb{Z}, +)", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        number_line = NumberLine(
            x_range=[-5, 5, 1],
            length=10,
            include_numbers=True,
            include_tip=True,
            color=Colors.GRAY
        )
        number_line.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(Create(number_line))
        
        verifications = VGroup(
            VGroup(
                Text("单位元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"e = 0", font_size=18, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("逆元: ", font_size=14, color=Colors.TEXT),
                MathTex(r"a^{-1} = -a", font_size=18, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        verifications.next_to(number_line, DOWN, buff=0.5).set_x(0)
        
        for ver in verifications:
            self.play(FadeIn(ver, shift=RIGHT * 0.2), run_time=0.5)
        
        zero_highlight = Circle(radius=0.2, color=Colors.PRIMARY, stroke_width=3)
        zero_highlight.move_to(number_line.n2p(0))
        
        self.play(Create(zero_highlight))
        
        conclusion = VGroup(
            MathTex(r"(\mathbb{Z}, +)", font_size=28, color=Colors.PRIMARY),
            Text(" 是一个群！", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.to_edge(DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(conclusion))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 7: 无限的探索
    # ========================================================
    def scene_07_infinity(self):
        # 无限的引入
        section_title = Text("无限 - 没有尽头的世界", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        question = Text('无限有多"大"？所有无限都一样大吗？', font_size=20, color=Colors.GRAY)
        question.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question))
        
        infinity_types = VGroup(
            VGroup(
                Text("可数无限", font_size=20, color=Colors.PRIMARY),
                Text("(Countably Infinite)", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("不可数无限", font_size=20, color=Colors.ACCENT),
                Text("(Uncountably Infinite)", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=2.0)
        infinity_types.next_to(question, DOWN, buff=0.6).set_x(0)
        
        box1 = SurroundingRectangle(infinity_types[0], color=Colors.PRIMARY, buff=0.2)
        box2 = SurroundingRectangle(infinity_types[1], color=Colors.ACCENT, buff=0.2)
        
        self.play(FadeIn(infinity_types[0]), Create(box1))
        self.play(FadeIn(infinity_types[1]), Create(box2))
        
        discovery = VGroup(
            Text("惊人发现: ", font_size=18, color=Colors.SECONDARY),
            Text('有些无限比另一些无限"更大"！', font_size=18, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        discovery.next_to(infinity_types, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(discovery))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(question),
            FadeOut(infinity_types), FadeOut(box1), FadeOut(box2),
            FadeOut(discovery),
            run_time=0.5
        )
        
        # 可数无限
        section_title = Text("可数无限", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("如果一个集合可以与自然数", font_size=18, color=Colors.GRAY),
            MathTex(r"\mathbb{N}", font_size=22, color=Colors.PRIMARY),
            Text("建立一一对应，则称为可数无限", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        conclusion = VGroup(
            Text("所以 ", font_size=16, color=Colors.TEXT),
            MathTex(r"|\mathbb{Z}| = |\mathbb{N}| = \aleph_0", font_size=22, color=Colors.PRIMARY),
            Text(" (阿列夫零)", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(conclusion))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(conclusion), run_time=0.5)
        
        # 康托尔对角线论证
        section_title = Text("康托尔对角线论证", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = VGroup(
            Text("实数", font_size=18, color=Colors.TEXT),
            MathTex(r"\mathbb{R}", font_size=22, color=Colors.ACCENT),
            Text(" 能与自然数一一对应吗？", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        
        contradiction = VGroup(
            Text("通过对角线论证，可以构造出", font_size=16, color=Colors.TEXT),
            Text("不在列表中", font_size=16, color=Colors.ACCENT),
            Text("的新数！", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.05)
        contradiction.next_to(intro, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(contradiction))
        
        conclusion = VGroup(
            Text("结论: ", font_size=16, color=Colors.TEXT),
            MathTex(r"|\mathbb{R}| > |\mathbb{N}|", font_size=22, color=Colors.PRIMARY),
            Text(" 实数是不可数的！", font_size=16, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(contradiction, DOWN, buff=0.5).set_x(0)
        
        box = SurroundingRectangle(conclusion, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(box))
        self.wait(2)
        
        clear_scene(self)
        self.add(self.chapter_title)
    
    # ========================================================
    # Scene 8: 总结与启示
    # ========================================================
    def scene_08_summary(self):
        # 知识体系回顾
        section_title = Text("知识体系回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        path_text = VGroup(
            Text("学习路径: ", font_size=18, color=Colors.TEXT),
            Text("集合 → 运算 → 定律 → 群论 → 无限", font_size=18, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        path_text.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(path_text))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(path_text), run_time=0.5)
        
        # 三个核心启示
        section_title = Text("三个核心启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        insights = [
            ("🧱", "集合是编程的基石", "数组、列表、字典都是集合的变体", Colors.PRIMARY),
            ("🔮", "抽象是强大的工具", "群论用同一语言描述时钟、魔方、密码学", Colors.SECONDARY),
            ("♾️", "理解无限与边界", "计算机能力有极限，理解可计算性很重要", Colors.ACCENT),
        ]
        
        cards = VGroup()
        for icon, title, desc, color in insights:
            card = create_insight_card(icon, title, desc, color, width=5.5, height=1.2)
            cards.add(card)
        
        cards.arrange(DOWN, buff=0.25)
        cards.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.6)
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(cards), run_time=0.5)
        
        # 结束
        closing_text = VGroup(
            Text("集合与抽象代数", font_size=28, color=Colors.PRIMARY),
            Text("不仅是数学工具", font_size=22, color=Colors.TEXT),
            VGroup(
                Text("更是", font_size=22, color=Colors.TEXT),
                Text("逻辑与抽象思维", font_size=22, color=Colors.SECONDARY),
                Text("的核心锻炼", font_size=22, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3)
        closing_text.set_x(0)
        
        for line in closing_text:
            self.play(FadeIn(line, shift=UP * 0.3), run_time=0.6)
        
        self.wait(1)
        
        self.play(FadeOut(self.chapter_title), closing_text.animate.scale(0.8).shift(UP * 0.5), run_time=0.8)
        
        thanks = Text("感谢观看", font_size=36, color=Colors.PRIMARY)
        thanks.set_x(0)
        
        self.play(FadeOut(closing_text), FadeIn(thanks, scale=1.2), run_time=1)
        self.wait(2)
        
        self.play(FadeOut(thanks), run_time=1)


if __name__ == "__main__":
    pass
