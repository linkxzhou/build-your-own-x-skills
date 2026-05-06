"""
Scene 4: 子集与幂集
介绍子集概念和幂集定理
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


def create_set_box(width=2, height=1.5, label="S", color=None):
    """创建集合容器"""
    stroke_color = color if color else Colors.PRIMARY
    box = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.2,
        fill_color=Colors.BG,
        fill_opacity=0.3,
        stroke_color=stroke_color,
        stroke_width=2
    )
    
    label_text = MathTex(label, font_size=20, color=stroke_color)
    label_text.next_to(box, UP, buff=0.15)
    
    return VGroup(box, label_text)


class Scene04Subsets(Scene):
    """Scene 4: 子集与幂集"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_subset_definition()
        self.section_subset_examples()
        self.section_power_set()
        self.section_power_set_theorem()
        
        clear_scene(self)
    
    def section_subset_definition(self):
        """子集定义"""
        # 小节标题
        section_title = Text("子集 - 集合的包含关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 定义
        definition = VGroup(
            Text("如果集合 B 中的每个元素都属于集合 A，", font_size=18, color=Colors.GRAY),
            Text("则称 B 是 A 的子集", font_size=18, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        # 符号
        notation = MathTex(r"B \subseteq A", font_size=36, color=Colors.PRIMARY)
        notation.next_to(definition, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(notation))
        self.wait(0.5)
        
        # 可视化：大圆包含小圆
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
        
        visual = VGroup(big_circle, small_circle, label_a, label_b)
        
        self.play(Create(big_circle), FadeIn(label_a))
        self.play(Create(small_circle), FadeIn(label_b))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(notation),
            FadeOut(visual),
            run_time=0.5
        )
    
    def section_subset_examples(self):
        """子集示例"""
        # 小节标题
        section_title = Text("子集的例子", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 示例
        examples = VGroup(
            VGroup(
                MathTex(r"\{1, 2\} \subseteq \{1, 2, 3\}", font_size=24, color=Colors.SECONDARY),
                Text(" ✓", font_size=20, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\{1, 4\} \subseteq \{1, 2, 3\}", font_size=24, color=Colors.ACCENT),
                Text(" ✗  (4 不在右边集合中)", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        examples.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        self.wait(0.5)
        
        # 特殊情况
        special_title = Text("特殊情况:", font_size=20, color=Colors.TEXT)
        special_title.next_to(examples, DOWN, buff=0.5).align_to(examples, LEFT)
        
        special_cases = VGroup(
            VGroup(
                Text("1. ", font_size=18, color=Colors.TEXT),
                Text("空集是任何集合的子集: ", font_size=18, color=Colors.TEXT),
                MathTex(r"\emptyset \subseteq A", font_size=22, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("2. ", font_size=18, color=Colors.TEXT),
                Text("任何集合是自身的子集: ", font_size=18, color=Colors.TEXT),
                MathTex(r"A \subseteq A", font_size=22, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("3. ", font_size=18, color=Colors.TEXT),
                Text("真子集 (不等于自身): ", font_size=18, color=Colors.TEXT),
                MathTex(r"B \subset A", font_size=22, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        special_cases.next_to(special_title, DOWN, buff=0.2).align_to(special_title, LEFT)
        
        self.play(FadeIn(special_title))
        for case in special_cases:
            self.play(FadeIn(case, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(examples),
            FadeOut(special_title),
            FadeOut(special_cases),
            run_time=0.5
        )
    
    def section_power_set(self):
        """幂集概念"""
        # 小节标题
        section_title = Text("幂集 - 所有子集的集合", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("幂集 ", font_size=20, color=Colors.TEXT),
            MathTex(r"\mathcal{P}(A)", font_size=26, color=Colors.PRIMARY),
            Text(" 是集合 A 的所有子集组成的集合", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 示例
        example_label = VGroup(
            Text("例: ", font_size=18, color=Colors.TEXT),
            MathTex(r"A = \{1, 2\}", font_size=24, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        example_label.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_label))
        
        # 所有子集
        subsets_label = Text("A 的所有子集:", font_size=18, color=Colors.TEXT)
        subsets_label.next_to(example_label, DOWN, buff=0.4).align_to(example_label, LEFT)
        
        self.play(FadeIn(subsets_label))
        
        # 逐个显示子集
        subsets = [
            (r"\emptyset", "空集"),
            (r"\{1\}", "只有1"),
            (r"\{2\}", "只有2"),
            (r"\{1, 2\}", "全部"),
        ]
        
        subset_mobjects = VGroup()
        for i, (tex, desc) in enumerate(subsets):
            subset_group = VGroup(
                MathTex(tex, font_size=22, color=Colors.SECONDARY),
                Text(f" ({desc})", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1)
            subset_mobjects.add(subset_group)
        
        subset_mobjects.arrange(RIGHT, buff=0.6)
        subset_mobjects.next_to(subsets_label, DOWN, buff=0.3).set_x(0)
        
        for subset in subset_mobjects:
            self.play(FadeIn(subset, shift=UP * 0.2), run_time=0.4)
            self.wait(0.2)
        
        self.wait(0.5)
        
        # 幂集结果
        power_set_result = MathTex(
            r"\mathcal{P}(A) = \{\emptyset, \{1\}, \{2\}, \{1,2\}\}",
            font_size=26, color=Colors.PRIMARY
        )
        power_set_result.next_to(subset_mobjects, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(power_set_result))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(example_label),
            FadeOut(subsets_label),
            FadeOut(subset_mobjects),
            FadeOut(power_set_result),
            run_time=0.5
        )
    
    def section_power_set_theorem(self):
        """幂集定理"""
        # 小节标题
        section_title = Text("幂集定理", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定理
        theorem = VGroup(
            Text("如果集合 A 有 n 个元素，", font_size=20, color=Colors.TEXT),
            VGroup(
                Text("那么幂集 ", font_size=20, color=Colors.TEXT),
                MathTex(r"\mathcal{P}(A)", font_size=24, color=Colors.PRIMARY),
                Text(" 有 ", font_size=20, color=Colors.TEXT),
                MathTex(r"2^n", font_size=28, color=Colors.ACCENT),
                Text(" 个子集", font_size=20, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15)
        theorem.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(theorem))
        self.wait(0.5)
        
        # 直观解释
        explanation = VGroup(
            Text("直观理解: 对于每个元素，都有两种选择", font_size=18, color=Colors.GRAY),
            Text(""包含" 或 "不包含"", font_size=18, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        explanation.next_to(theorem, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        self.wait(0.5)
        
        # 示例表格
        table_data = [
            ("n = 0", r"\emptyset", r"2^0 = 1"),
            ("n = 1", r"\{a\}", r"2^1 = 2"),
            ("n = 2", r"\{a, b\}", r"2^2 = 4"),
            ("n = 3", r"\{a, b, c\}", r"2^3 = 8"),
        ]
        
        table_rows = VGroup()
        for n_str, set_str, count_str in table_data:
            row = VGroup(
                Text(n_str, font_size=16, color=Colors.TEXT),
                MathTex(set_str, font_size=18, color=Colors.SECONDARY),
                MathTex(count_str, font_size=18, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=1.0)
            table_rows.add(row)
        
        table_rows.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        table_rows.next_to(explanation, DOWN, buff=0.5).set_x(0)
        
        for row in table_rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
        
        self.wait(0.5)
        
        # 公式高亮
        formula_box = SurroundingRectangle(
            MathTex(r"|\mathcal{P}(A)| = 2^{|A|}", font_size=32, color=Colors.PRIMARY),
            color=Colors.PRIMARY,
            buff=0.2
        )
        formula = MathTex(r"|\mathcal{P}(A)| = 2^{|A|}", font_size=32, color=Colors.PRIMARY)
        formula.to_edge(DOWN, buff=0.8).set_x(0)
        formula_box = SurroundingRectangle(formula, color=Colors.PRIMARY, buff=0.2)
        
        self.play(Write(formula), Create(formula_box))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_04_subsets.py Scene04Subsets
    pass
