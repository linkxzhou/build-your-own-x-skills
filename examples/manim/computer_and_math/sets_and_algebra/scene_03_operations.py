"""
Scene 3: 集合运算与韦恩图
可视化并集、交集、差集、对称差
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
    """韦恩图辅助类"""
    
    def __init__(self, center=ORIGIN, radius=1.2, separation=0.8):
        self.center = center
        self.radius = radius
        self.separation = separation
        
        # 两个圆的圆心
        self.center_a = center + LEFT * separation / 2
        self.center_b = center + RIGHT * separation / 2
        
        # 创建圆
        self.circle_a = Circle(radius=radius)
        self.circle_a.set_stroke(Colors.SET_A, width=3)
        self.circle_a.set_fill(Colors.SET_A, opacity=0.2)
        self.circle_a.move_to(self.center_a)
        
        self.circle_b = Circle(radius=radius)
        self.circle_b.set_stroke(Colors.SET_B, width=3)
        self.circle_b.set_fill(Colors.SET_B, opacity=0.2)
        self.circle_b.move_to(self.center_b)
        
        # 标签
        self.label_a = MathTex("A", font_size=28, color=Colors.SET_A)
        self.label_a.next_to(self.circle_a, UP + LEFT, buff=0.1)
        
        self.label_b = MathTex("B", font_size=28, color=Colors.SET_B)
        self.label_b.next_to(self.circle_b, UP + RIGHT, buff=0.1)
    
    def get_base_group(self):
        """获取基础韦恩图"""
        return VGroup(self.circle_a, self.circle_b, self.label_a, self.label_b)
    
    def get_intersection_region(self):
        """获取交集区域"""
        intersection = Intersection(self.circle_a, self.circle_b)
        intersection.set_stroke(width=0)
        intersection.set_fill(Colors.INTERSECTION, opacity=0.6)
        return intersection
    
    def get_union_region(self):
        """获取并集区域"""
        union = Union(self.circle_a, self.circle_b)
        union.set_stroke(Colors.PRIMARY, width=3)
        union.set_fill(Colors.PRIMARY, opacity=0.4)
        return union
    
    def get_difference_a_b(self):
        """获取 A - B 区域"""
        diff = Difference(self.circle_a, self.circle_b)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.SET_A, opacity=0.6)
        return diff
    
    def get_difference_b_a(self):
        """获取 B - A 区域"""
        diff = Difference(self.circle_b, self.circle_a)
        diff.set_stroke(width=0)
        diff.set_fill(Colors.SET_B, opacity=0.6)
        return diff
    
    def get_symmetric_difference(self):
        """获取对称差区域"""
        diff_a = Difference(self.circle_a, self.circle_b)
        diff_a.set_stroke(width=0)
        diff_a.set_fill(Colors.SET_A, opacity=0.5)
        
        diff_b = Difference(self.circle_b, self.circle_a)
        diff_b.set_stroke(width=0)
        diff_b.set_fill(Colors.SET_B, opacity=0.5)
        
        return VGroup(diff_a, diff_b)


class Scene03Operations(Scene):
    """Scene 3: 集合运算与韦恩图"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_intro_venn()
        self.section_union()
        self.section_intersection()
        self.section_difference()
        self.section_symmetric_difference()
        
        clear_scene(self)
    
    def section_intro_venn(self):
        """介绍韦恩图"""
        # 小节标题
        section_title = Text("韦恩图 - 可视化集合关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 创建示例集合
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
        self.wait(0.5)
        
        # 创建韦恩图
        venn = VennDiagram(center=DOWN * 1.5, radius=1.3, separation=1.0)
        base = venn.get_base_group()
        
        self.play(Create(base), run_time=1)
        
        # 在圆内标注元素
        elem_a_only = MathTex(r"1, 2", font_size=18, color=Colors.TEXT)
        elem_a_only.move_to(venn.center_a + LEFT * 0.4)
        
        elem_common = MathTex(r"3, 4", font_size=18, color=Colors.TEXT)
        elem_common.move_to(venn.center)
        
        elem_b_only = MathTex(r"5, 6", font_size=18, color=Colors.TEXT)
        elem_b_only.move_to(venn.center_b + RIGHT * 0.4)
        
        self.play(
            FadeIn(elem_a_only),
            FadeIn(elem_common),
            FadeIn(elem_b_only),
        )
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(example_sets),
            FadeOut(base),
            FadeOut(elem_a_only),
            FadeOut(elem_common),
            FadeOut(elem_b_only),
            run_time=0.5
        )
    
    def section_union(self):
        """并集运算"""
        # 小节标题
        section_title = VGroup(
            Text("并集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A \cup B", font_size=30, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = Text('"合并所有元素"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 创建韦恩图
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        # 先显示基础图
        self.play(FadeIn(base))
        self.wait(0.3)
        
        # 高亮并集区域
        union = venn.get_union_region()
        self.play(FadeIn(union), run_time=0.8)
        
        # 公式和结果
        formula = VGroup(
            MathTex(r"A \cup B", font_size=28, color=Colors.PRIMARY),
            MathTex(r"= \{x \mid x \in A \lor x \in B\}", font_size=22, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.2)
        formula.next_to(base, RIGHT, buff=0.8).shift(UP * 0.3)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} \cup \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{1,2,3,4,5,6\}", font_size=24, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.15)
        example.next_to(formula, DOWN, buff=0.4)
        
        self.play(FadeIn(formula))
        self.play(FadeIn(example))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(base),
            FadeOut(union),
            FadeOut(formula),
            FadeOut(example),
            run_time=0.5
        )
    
    def section_intersection(self):
        """交集运算"""
        # 小节标题
        section_title = VGroup(
            Text("交集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A \cap B", font_size=30, color=Colors.INTERSECTION),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = Text('"提取共有元素"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 创建韦恩图
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        self.wait(0.3)
        
        # 高亮交集区域
        intersection = venn.get_intersection_region()
        self.play(FadeIn(intersection), run_time=0.8)
        
        # 公式和结果
        formula = VGroup(
            MathTex(r"A \cap B", font_size=28, color=Colors.INTERSECTION),
            MathTex(r"= \{x \mid x \in A \land x \in B\}", font_size=22, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.2)
        formula.next_to(base, RIGHT, buff=0.8).shift(UP * 0.3)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} \cap \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{3,4\}", font_size=24, color=Colors.INTERSECTION),
        ).arrange(DOWN, buff=0.15)
        example.next_to(formula, DOWN, buff=0.4)
        
        self.play(FadeIn(formula))
        self.play(FadeIn(example))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(base),
            FadeOut(intersection),
            FadeOut(formula),
            FadeOut(example),
            run_time=0.5
        )
    
    def section_difference(self):
        """差集运算"""
        # 小节标题
        section_title = VGroup(
            Text("差集 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A - B", font_size=30, color=Colors.SET_A),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = Text('"属于A但不属于B"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 创建韦恩图
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        self.wait(0.3)
        
        # 高亮 A - B 区域
        diff = venn.get_difference_a_b()
        self.play(FadeIn(diff), run_time=0.8)
        
        # 公式和结果
        formula = VGroup(
            MathTex(r"A - B", font_size=28, color=Colors.SET_A),
            MathTex(r"= \{x \mid x \in A \land x \notin B\}", font_size=22, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.2)
        formula.next_to(base, RIGHT, buff=0.8).shift(UP * 0.3)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} - \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{1,2\}", font_size=24, color=Colors.SET_A),
        ).arrange(DOWN, buff=0.15)
        example.next_to(formula, DOWN, buff=0.4)
        
        self.play(FadeIn(formula))
        self.play(FadeIn(example))
        self.wait(1)
        
        # 注意: B - A 不同
        note = VGroup(
            Text("注意: ", font_size=16, color=Colors.ACCENT),
            MathTex(r"B - A = \{5, 6\}", font_size=20, color=Colors.SET_B),
            Text(" ≠ A - B", font_size=16, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        note.next_to(example, DOWN, buff=0.3)
        
        self.play(FadeIn(note))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(base),
            FadeOut(diff),
            FadeOut(formula),
            FadeOut(example),
            FadeOut(note),
            run_time=0.5
        )
    
    def section_symmetric_difference(self):
        """对称差运算"""
        # 小节标题
        section_title = VGroup(
            Text("对称差 ", font_size=26, color=Colors.TEXT),
            MathTex(r"A \triangle B", font_size=30, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = Text('"只属于其中一个集合"', font_size=20, color=Colors.GRAY)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 创建韦恩图
        venn = VennDiagram(center=DOWN * 0.8 + LEFT * 2, radius=1.0, separation=0.8)
        base = venn.get_base_group()
        
        self.play(FadeIn(base))
        self.wait(0.3)
        
        # 高亮对称差区域
        sym_diff = venn.get_symmetric_difference()
        self.play(FadeIn(sym_diff), run_time=0.8)
        
        # 公式和结果
        formula = VGroup(
            MathTex(r"A \triangle B", font_size=28, color=Colors.SECONDARY),
            MathTex(r"= (A - B) \cup (B - A)", font_size=22, color=Colors.GRAY),
            MathTex(r"= (A \cup B) - (A \cap B)", font_size=22, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        formula.next_to(base, RIGHT, buff=0.8).shift(UP * 0.3)
        
        example = VGroup(
            MathTex(r"\{1,2,3,4\} \triangle \{3,4,5,6\}", font_size=22, color=Colors.TEXT),
            MathTex(r"= \{1,2,5,6\}", font_size=24, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.15)
        example.next_to(formula, DOWN, buff=0.3)
        
        self.play(FadeIn(formula))
        self.play(FadeIn(example))
        
        # XOR 类比
        xor_note = VGroup(
            Text("程序员视角: ", font_size=16, color=Colors.PRIMARY),
            Text("类似于 XOR (异或) 运算", font_size=16, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        xor_note.next_to(example, DOWN, buff=0.3)
        
        self.play(FadeIn(xor_note))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_03_operations.py Scene03Operations
    pass
