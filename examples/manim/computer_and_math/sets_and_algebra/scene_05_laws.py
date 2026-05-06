"""
Scene 5: 集合定律与德摩根定律
展示集合运算的规律性，重点介绍德摩根定律
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


class VennDiagram:
    """韦恩图辅助类（带全集边界）"""
    
    def __init__(self, center=ORIGIN, radius=0.9, separation=0.7, show_universe=False):
        self.center = center
        self.radius = radius
        self.separation = separation
        
        # 两个圆的圆心
        self.center_a = center + LEFT * separation / 2
        self.center_b = center + RIGHT * separation / 2
        
        # 创建圆
        self.circle_a = Circle(radius=radius)
        self.circle_a.set_stroke(Colors.SET_A, width=2)
        self.circle_a.set_fill(Colors.SET_A, opacity=0.15)
        self.circle_a.move_to(self.center_a)
        
        self.circle_b = Circle(radius=radius)
        self.circle_b.set_stroke(Colors.SET_B, width=2)
        self.circle_b.set_fill(Colors.SET_B, opacity=0.15)
        self.circle_b.move_to(self.center_b)
        
        # 全集边界
        self.universe = None
        if show_universe:
            self.universe = Rectangle(
                width=radius * 4, height=radius * 2.8,
                stroke_color=Colors.GRAY, stroke_width=2
            )
            self.universe.move_to(center)
        
        # 标签
        self.label_a = MathTex("A", font_size=22, color=Colors.SET_A)
        self.label_a.next_to(self.circle_a, UP + LEFT, buff=0.05)
        
        self.label_b = MathTex("B", font_size=22, color=Colors.SET_B)
        self.label_b.next_to(self.circle_b, UP + RIGHT, buff=0.05)
    
    def get_base_group(self):
        """获取基础韦恩图"""
        group = VGroup(self.circle_a, self.circle_b, self.label_a, self.label_b)
        if self.universe:
            group = VGroup(self.universe, self.circle_a, self.circle_b, self.label_a, self.label_b)
        return group
    
    def get_complement_a(self):
        """获取 A 的补集区域"""
        if not self.universe:
            return VGroup()
        diff = Difference(self.universe, self.circle_a)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.GRAY, opacity=0.4)
        return diff
    
    def get_complement_union(self):
        """获取 (A ∪ B)' 区域"""
        if not self.universe:
            return VGroup()
        union = Union(self.circle_a, self.circle_b)
        diff = Difference(self.universe, union)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.ACCENT, opacity=0.5)
        return diff
    
    def get_complement_intersection(self):
        """获取 (A ∩ B)' 区域"""
        if not self.universe:
            return VGroup()
        intersection = Intersection(self.circle_a, self.circle_b)
        diff = Difference(self.universe, intersection)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.SECONDARY, opacity=0.4)
        return diff
    
    def get_complement_a_intersect_complement_b(self):
        """获取 A' ∩ B' 区域"""
        if not self.universe:
            return VGroup()
        union = Union(self.circle_a, self.circle_b)
        diff = Difference(self.universe, union)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.ACCENT, opacity=0.5)
        return diff
    
    def get_complement_a_union_complement_b(self):
        """获取 A' ∪ B' 区域"""
        if not self.universe:
            return VGroup()
        intersection = Intersection(self.circle_a, self.circle_b)
        diff = Difference(self.universe, intersection)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.SECONDARY, opacity=0.4)
        return diff


class Scene05Laws(Scene):
    """Scene 5: 集合定律与德摩根定律"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_basic_laws()
        self.section_complement()
        self.section_de_morgan()
        self.section_logic_connection()
        
        clear_scene(self)
    
    def section_basic_laws(self):
        """基本定律"""
        # 小节标题
        section_title = Text("集合的基本定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定律表
        laws = [
            ("交换律", r"A \cup B = B \cup A", r"A \cap B = B \cap A"),
            ("结合律", r"(A \cup B) \cup C = A \cup (B \cup C)", r"(A \cap B) \cap C = A \cap (B \cap C)"),
            ("分配律", r"A \cap (B \cup C) = (A \cap B) \cup (A \cap C)", r"A \cup (B \cap C) = (A \cup B) \cap (A \cup C)"),
        ]
        
        table_header = VGroup(
            Text("定律", font_size=16, color=Colors.GRAY),
            Text("并集形式", font_size=16, color=Colors.PRIMARY),
            Text("交集形式", font_size=16, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=1.5)
        table_header.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(table_header))
        
        table_rows = VGroup()
        for name, union_form, inter_form in laws:
            row = VGroup(
                Text(name, font_size=14, color=Colors.TEXT),
                MathTex(union_form, font_size=16, color=Colors.PRIMARY),
                MathTex(inter_form, font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.5)
            table_rows.add(row)
        
        table_rows.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        table_rows.next_to(table_header, DOWN, buff=0.4).set_x(0)
        
        for row in table_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.2)
        
        # 幂等律和吸收律
        more_laws = VGroup(
            VGroup(
                Text("幂等律: ", font_size=14, color=Colors.TEXT),
                MathTex(r"A \cup A = A", font_size=18, color=Colors.PRIMARY),
                Text(", ", font_size=14, color=Colors.TEXT),
                MathTex(r"A \cap A = A", font_size=18, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("同一律: ", font_size=14, color=Colors.TEXT),
                MathTex(r"A \cup \emptyset = A", font_size=18, color=Colors.PRIMARY),
                Text(", ", font_size=14, color=Colors.TEXT),
                MathTex(r"A \cap U = A", font_size=18, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        more_laws.next_to(table_rows, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(more_laws))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(table_header),
            FadeOut(table_rows),
            FadeOut(more_laws),
            run_time=0.5
        )
    
    def section_complement(self):
        """补集概念"""
        # 小节标题
        section_title = Text("补集", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("相对于全集 U，不属于 A 的元素组成 A 的补集", font_size=18, color=Colors.GRAY),
            MathTex(r"A' = \bar{A} = U - A = \{x \mid x \in U \land x \notin A\}", font_size=22, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.2)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 韦恩图展示补集
        venn = VennDiagram(center=DOWN * 1.2, radius=0.9, show_universe=True)
        
        # 只显示一个圆和全集
        single_circle = Circle(radius=0.9)
        single_circle.set_stroke(Colors.SET_A, width=2)
        single_circle.set_fill(Colors.SET_A, opacity=0.3)
        single_circle.move_to(DOWN * 1.2)
        
        universe = Rectangle(width=3.6, height=2.5, stroke_color=Colors.GRAY, stroke_width=2)
        universe.move_to(DOWN * 1.2)
        
        label_a = MathTex("A", font_size=22, color=Colors.SET_A)
        label_a.move_to(single_circle.get_center())
        
        label_u = MathTex("U", font_size=22, color=Colors.GRAY)
        label_u.next_to(universe, UP + RIGHT, buff=0.1)
        
        self.play(Create(universe), FadeIn(label_u))
        self.play(Create(single_circle), FadeIn(label_a))
        
        # 高亮补集
        complement = Difference(universe, single_circle)
        complement.set_stroke(width=0)
        complement.set_fill(Colors.ACCENT, opacity=0.4)
        
        complement_label = MathTex(r"A'", font_size=22, color=Colors.ACCENT)
        complement_label.next_to(universe, DOWN + LEFT, buff=-0.5)
        
        self.play(FadeIn(complement), FadeIn(complement_label))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(universe),
            FadeOut(single_circle),
            FadeOut(label_a),
            FadeOut(label_u),
            FadeOut(complement),
            FadeOut(complement_label),
            run_time=0.5
        )
    
    def section_de_morgan(self):
        """德摩根定律"""
        # 小节标题
        section_title = Text("德摩根定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 两条定律
        law1 = MathTex(r"(A \cup B)' = A' \cap B'", font_size=32, color=Colors.PRIMARY)
        law2 = MathTex(r"(A \cap B)' = A' \cup B'", font_size=32, color=Colors.SECONDARY)
        
        laws = VGroup(law1, law2).arrange(DOWN, buff=0.4)
        laws.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(law1), run_time=0.8)
        self.wait(0.3)
        self.play(Write(law2), run_time=0.8)
        self.wait(0.5)
        
        # 直观解释
        explanation = VGroup(
            Text('"并集的补" = "各自补集的交"', font_size=16, color=Colors.GRAY),
            Text('"交集的补" = "各自补集的并"', font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        explanation.next_to(laws, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        self.wait(0.5)
        
        # 韦恩图验证第一条定律
        verify_title = Text("验证第一条定律:", font_size=16, color=Colors.TEXT)
        verify_title.next_to(explanation, DOWN, buff=0.4).align_to(explanation, LEFT)
        
        self.play(FadeIn(verify_title))
        
        # 左边：(A ∪ B)'
        venn_left = VennDiagram(center=DOWN * 2.5 + LEFT * 2.5, radius=0.6, separation=0.5, show_universe=True)
        base_left = venn_left.get_base_group()
        
        left_label = MathTex(r"(A \cup B)'", font_size=18, color=Colors.ACCENT)
        left_label.next_to(base_left, DOWN, buff=0.2)
        
        self.play(FadeIn(base_left), FadeIn(left_label))
        
        # 高亮 (A ∪ B)'
        highlight_left = venn_left.get_complement_union()
        self.play(FadeIn(highlight_left))
        
        # 右边：A' ∩ B'
        venn_right = VennDiagram(center=DOWN * 2.5 + RIGHT * 2.5, radius=0.6, separation=0.5, show_universe=True)
        base_right = venn_right.get_base_group()
        
        right_label = MathTex(r"A' \cap B'", font_size=18, color=Colors.ACCENT)
        right_label.next_to(base_right, DOWN, buff=0.2)
        
        self.play(FadeIn(base_right), FadeIn(right_label))
        
        # 高亮 A' ∩ B'
        highlight_right = venn_right.get_complement_a_intersect_complement_b()
        self.play(FadeIn(highlight_right))
        
        # 等号
        equals = MathTex("=", font_size=36, color=Colors.TEXT)
        equals.move_to(DOWN * 2.5)
        
        self.play(Write(equals))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(laws),
            FadeOut(explanation),
            FadeOut(verify_title),
            FadeOut(base_left),
            FadeOut(left_label),
            FadeOut(highlight_left),
            FadeOut(base_right),
            FadeOut(right_label),
            FadeOut(highlight_right),
            FadeOut(equals),
            run_time=0.5
        )
    
    def section_logic_connection(self):
        """与逻辑运算的联系"""
        # 小节标题
        section_title = Text("与逻辑运算的联系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 对照表
        correspondence = VGroup(
            VGroup(
                Text("集合运算", font_size=16, color=Colors.PRIMARY),
                Text("逻辑运算", font_size=16, color=Colors.SECONDARY),
                Text("布尔代数", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=1.5),
            VGroup(
                MathTex(r"A \cup B", font_size=20, color=Colors.PRIMARY),
                MathTex(r"p \lor q", font_size=20, color=Colors.SECONDARY),
                Text("OR", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=1.8),
            VGroup(
                MathTex(r"A \cap B", font_size=20, color=Colors.PRIMARY),
                MathTex(r"p \land q", font_size=20, color=Colors.SECONDARY),
                Text("AND", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=1.8),
            VGroup(
                MathTex(r"A'", font_size=20, color=Colors.PRIMARY),
                MathTex(r"\neg p", font_size=20, color=Colors.SECONDARY),
                Text("NOT", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=2.0),
        ).arrange(DOWN, buff=0.35)
        correspondence.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for row in correspondence:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(0.5)
        
        # 德摩根定律在编程中的应用
        programming = VGroup(
            Text("编程中的德摩根定律:", font_size=18, color=Colors.TEXT),
            VGroup(
                MathTex(r"\neg(p \lor q) = \neg p \land \neg q", font_size=22, color=Colors.PRIMARY),
                Text("  →  ", font_size=16, color=Colors.GRAY),
                Text("!(a || b) == (!a && !b)", font_size=14, color=Colors.SECONDARY, font="Courier New"),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\neg(p \land q) = \neg p \lor \neg q", font_size=22, color=Colors.PRIMARY),
                Text("  →  ", font_size=16, color=Colors.GRAY),
                Text("!(a && b) == (!a || !b)", font_size=14, color=Colors.SECONDARY, font="Courier New"),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        programming.next_to(correspondence, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(programming))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_05_laws.py Scene05Laws
    pass
