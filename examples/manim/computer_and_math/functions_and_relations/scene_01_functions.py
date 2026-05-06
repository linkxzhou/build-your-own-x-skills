"""
函数与关系 - Scene 1: 函数——集合之间的映射
从函数的严格定义出发，展示函数作为集合映射的本质

渲染命令: manim -pqh scene_01_functions.py FunctionsIntro
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


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_set_ellipse(elements, label, color, width=2.5, height=3.0):
    """创建集合椭圆（包含元素）"""
    ellipse = Ellipse(width=width, height=height)
    ellipse.set_stroke(color, width=3)
    ellipse.set_fill(color, opacity=0.1)
    
    label_text = Text(label, font_size=20, color=color)
    label_text.next_to(ellipse, UP, buff=0.2)
    
    # 排列元素
    element_mobjects = VGroup()
    for i, elem in enumerate(elements):
        elem_text = Text(str(elem), font_size=24, color=Colors.TEXT)
        element_mobjects.add(elem_text)
    
    # 垂直排列元素
    if len(elements) > 0:
        spacing = min(0.7, (height - 0.6) / len(elements))
        element_mobjects.arrange(DOWN, buff=spacing)
        element_mobjects.move_to(ellipse.get_center())
    
    return VGroup(ellipse, label_text, element_mobjects)


def create_mapping_arrow(start_pos, end_pos, color=Colors.ARROW_COLOR):
    """创建映射箭头"""
    arrow = Arrow(
        start_pos, end_pos,
        color=color,
        stroke_width=2,
        buff=0.15,
        max_tip_length_to_length_ratio=0.15
    )
    return arrow


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== Scene 1: 函数——集合之间的映射 ==========
class FunctionsIntro(Scene):
    """函数作为集合映射的介绍"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # 各部分
        self.opening()
        self.definition()
        self.arrow_diagram()
        self.valid_vs_invalid()
        self.key_understanding()
        
        clear_scene(self)
    
    def opening(self):
        """开场动画"""
        main_title = Text("函数与关系", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("从映射到抽象", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        # 引出问题
        question = Text(
            "函数不只是 y = f(x)，它是一种更一般的概念",
            font_size=22, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        # 转换到章节标题
        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def definition(self):
        """函数的严格定义"""
        section_title = Text("函数的严格定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义文字
        def_line1 = VGroup(
            Text("给定两个集合 ", font_size=18, color=Colors.GRAY),
            Text("S", font_size=20, color=Colors.DOMAIN_COLOR),
            Text("（定义域）和 ", font_size=18, color=Colors.GRAY),
            Text("T", font_size=20, color=Colors.CODOMAIN_COLOR),
            Text("（值域）", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.05)
        
        def_line2 = VGroup(
            Text("函数 ", font_size=18, color=Colors.GRAY),
            MathTex(r"f: S \rightarrow T", font_size=24, color=Colors.FUNCTION_COLOR),
            Text(" 是有序对 ", font_size=18, color=Colors.GRAY),
            MathTex(r"(s, t)", font_size=22, color=Colors.TEXT),
            Text(" 的集合", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.05)
        
        definition = VGroup(def_line1, def_line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(1)
        
        # 关键约束
        constraint_title = Text("关键约束：", font_size=18, color=Colors.ACCENT)
        constraint_title.next_to(definition, DOWN, buff=0.4).align_to(definition, LEFT)
        
        constraint = VGroup(
            Text("S 中的每个元素都必须出现", font_size=16, color=Colors.TEXT),
            Text("一次且仅出现一次", font_size=16, color=Colors.ACCENT),
            Text("作为有序对的第一个元素", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.05)
        constraint.next_to(constraint_title, DOWN, buff=0.1)
        
        self.play(FadeIn(constraint_title), FadeIn(constraint))
        
        # 类比
        analogy = VGroup(
            Text("类比：给 S 中的每个元素分配一个 T 中的", font_size=16, color=Colors.GRAY),
            Text('"伴侣"', font_size=16, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.05)
        analogy.next_to(constraint, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(constraint_title), FadeOut(constraint),
            FadeOut(analogy),
            run_time=0.5
        )
    
    def arrow_diagram(self):
        """箭头图可视化"""
        section_title = Text("函数的可视化：箭头图", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建两个集合
        # 集合 S = {a, b, c}
        s_ellipse = Ellipse(width=2.0, height=2.8)
        s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=3)
        s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        s_ellipse.shift(LEFT * 2.5)
        
        s_label = Text("S", font_size=22, color=Colors.DOMAIN_COLOR)
        s_label.next_to(s_ellipse, UP, buff=0.15)
        
        s_elements = VGroup()
        for i, elem in enumerate(['a', 'b', 'c']):
            elem_text = Text(elem, font_size=22, color=Colors.TEXT)
            s_elements.add(elem_text)
        s_elements.arrange(DOWN, buff=0.4)
        s_elements.move_to(s_ellipse.get_center())
        
        # 集合 T = {1, 2, 3}
        t_ellipse = Ellipse(width=2.0, height=2.8)
        t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=3)
        t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        t_ellipse.shift(RIGHT * 2.5)
        
        t_label = Text("T", font_size=22, color=Colors.CODOMAIN_COLOR)
        t_label.next_to(t_ellipse, UP, buff=0.15)
        
        t_elements = VGroup()
        for i, elem in enumerate(['1', '2', '3']):
            elem_text = Text(elem, font_size=22, color=Colors.TEXT)
            t_elements.add(elem_text)
        t_elements.arrange(DOWN, buff=0.4)
        t_elements.move_to(t_ellipse.get_center())
        
        sets_group = VGroup(s_ellipse, s_label, s_elements, t_ellipse, t_label, t_elements)
        sets_group.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeIn(s_ellipse), FadeIn(s_label), FadeIn(s_elements),
            FadeIn(t_ellipse), FadeIn(t_label), FadeIn(t_elements),
            run_time=0.8
        )
        
        # 函数标记
        func_label = MathTex(r"f: S \rightarrow T", font_size=24, color=Colors.FUNCTION_COLOR)
        func_label.move_to((s_ellipse.get_center() + t_ellipse.get_center()) / 2 + UP * 1.8)
        
        self.play(FadeIn(func_label))
        
        # 绘制映射箭头: a→1, b→2, c→2
        arrows = VGroup()
        
        # a → 1
        arrow1 = create_mapping_arrow(
            s_elements[0].get_right() + RIGHT * 0.1,
            t_elements[0].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow1)
        
        # b → 2
        arrow2 = create_mapping_arrow(
            s_elements[1].get_right() + RIGHT * 0.1,
            t_elements[1].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow2)
        
        # c → 2
        arrow3 = create_mapping_arrow(
            s_elements[2].get_right() + RIGHT * 0.1,
            t_elements[1].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow3)
        
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=0.4)
        
        # 说明
        explanation = VGroup(
            Text("f(a) = 1", font_size=16, color=Colors.GRAY),
            Text("f(b) = 2", font_size=16, color=Colors.GRAY),
            Text("f(c) = 2", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanation.to_edge(RIGHT, buff=0.8).shift(DOWN * 0.5)
        
        self.play(FadeIn(explanation))
        
        # 注意点
        note = Text("注意：b 和 c 都对应 2，这是允许的！", font_size=16, color=Colors.SECONDARY)
        note.next_to(sets_group, DOWN, buff=0.5).set_x(0)
        
        highlight = SurroundingRectangle(
            VGroup(arrow2, arrow3, t_elements[1]),
            color=Colors.SECONDARY, buff=0.1
        )
        
        self.play(FadeIn(note), Create(highlight))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(sets_group),
            FadeOut(func_label), FadeOut(arrows),
            FadeOut(explanation), FadeOut(note), FadeOut(highlight),
            run_time=0.5
        )
    
    def valid_vs_invalid(self):
        """合法与非法映射对比"""
        section_title = Text("合法映射 vs 非法映射", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # ===== 合法映射 =====
        valid_title = Text("✓ 合法函数", font_size=18, color=Colors.CODOMAIN_COLOR)
        
        # 小集合
        vs_ellipse = Ellipse(width=1.4, height=2.0)
        vs_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
        vs_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        
        vs_elements = VGroup()
        for elem in ['a', 'b']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            vs_elements.add(elem_text)
        vs_elements.arrange(DOWN, buff=0.3)
        vs_elements.move_to(vs_ellipse.get_center())
        
        vt_ellipse = Ellipse(width=1.4, height=2.0)
        vt_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
        vt_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        vt_ellipse.shift(RIGHT * 2.0)
        
        vt_elements = VGroup()
        for elem in ['1', '2']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            vt_elements.add(elem_text)
        vt_elements.arrange(DOWN, buff=0.3)
        vt_elements.move_to(vt_ellipse.get_center())
        
        valid_arrows = VGroup(
            create_mapping_arrow(vs_elements[0].get_right() + RIGHT * 0.05,
                                vt_elements[0].get_left() + LEFT * 0.05, Colors.ARROW_COLOR),
            create_mapping_arrow(vs_elements[1].get_right() + RIGHT * 0.05,
                                vt_elements[1].get_left() + LEFT * 0.05, Colors.ARROW_COLOR),
        )
        
        valid_group = VGroup(vs_ellipse, vs_elements, vt_ellipse, vt_elements, valid_arrows)
        valid_title.next_to(valid_group, UP, buff=0.2)
        valid_full = VGroup(valid_title, valid_group)
        
        valid_reason = Text("每个定义域元素恰好对应一个值", font_size=12, color=Colors.GRAY)
        valid_reason.next_to(valid_group, DOWN, buff=0.15)
        
        # ===== 非法映射1: 一个元素对应多个 =====
        invalid1_title = Text("✗ 非法：一对多", font_size=18, color=Colors.ACCENT)
        
        i1s_ellipse = Ellipse(width=1.4, height=2.0)
        i1s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
        i1s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        
        i1s_elements = VGroup()
        for elem in ['a', 'b']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            i1s_elements.add(elem_text)
        i1s_elements.arrange(DOWN, buff=0.3)
        i1s_elements.move_to(i1s_ellipse.get_center())
        
        i1t_ellipse = Ellipse(width=1.4, height=2.0)
        i1t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
        i1t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        i1t_ellipse.shift(RIGHT * 2.0)
        
        i1t_elements = VGroup()
        for elem in ['1', '2']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            i1t_elements.add(elem_text)
        i1t_elements.arrange(DOWN, buff=0.3)
        i1t_elements.move_to(i1t_ellipse.get_center())
        
        # a 对应 1 和 2
        invalid1_arrows = VGroup(
            create_mapping_arrow(i1s_elements[0].get_right() + RIGHT * 0.05,
                                i1t_elements[0].get_left() + LEFT * 0.05, Colors.ACCENT),
            create_mapping_arrow(i1s_elements[0].get_right() + RIGHT * 0.05,
                                i1t_elements[1].get_left() + LEFT * 0.05, Colors.ACCENT),
            create_mapping_arrow(i1s_elements[1].get_right() + RIGHT * 0.05,
                                i1t_elements[1].get_left() + LEFT * 0.05, Colors.ARROW_COLOR),
        )
        
        invalid1_group = VGroup(i1s_ellipse, i1s_elements, i1t_ellipse, i1t_elements, invalid1_arrows)
        invalid1_title.next_to(invalid1_group, UP, buff=0.2)
        invalid1_full = VGroup(invalid1_title, invalid1_group)
        
        invalid1_reason = Text("a 对应了两个值", font_size=12, color=Colors.ACCENT)
        invalid1_reason.next_to(invalid1_group, DOWN, buff=0.15)
        
        # ===== 非法映射2: 有元素无对应 =====
        invalid2_title = Text("✗ 非法：有遗漏", font_size=18, color=Colors.ACCENT)
        
        i2s_ellipse = Ellipse(width=1.4, height=2.0)
        i2s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
        i2s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        
        i2s_elements = VGroup()
        for elem in ['a', 'b']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            i2s_elements.add(elem_text)
        i2s_elements.arrange(DOWN, buff=0.3)
        i2s_elements.move_to(i2s_ellipse.get_center())
        
        i2t_ellipse = Ellipse(width=1.4, height=2.0)
        i2t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
        i2t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        i2t_ellipse.shift(RIGHT * 2.0)
        
        i2t_elements = VGroup()
        for elem in ['1', '2']:
            elem_text = Text(elem, font_size=18, color=Colors.TEXT)
            i2t_elements.add(elem_text)
        i2t_elements.arrange(DOWN, buff=0.3)
        i2t_elements.move_to(i2t_ellipse.get_center())
        
        # b 没有对应
        invalid2_arrows = VGroup(
            create_mapping_arrow(i2s_elements[0].get_right() + RIGHT * 0.05,
                                i2t_elements[0].get_left() + LEFT * 0.05, Colors.ARROW_COLOR),
        )
        
        # b 上加问号
        question_mark = Text("?", font_size=20, color=Colors.ACCENT)
        question_mark.next_to(i2s_elements[1], RIGHT, buff=0.3)
        
        invalid2_group = VGroup(i2s_ellipse, i2s_elements, i2t_ellipse, i2t_elements, invalid2_arrows, question_mark)
        invalid2_title.next_to(invalid2_group, UP, buff=0.2)
        invalid2_full = VGroup(invalid2_title, invalid2_group)
        
        invalid2_reason = Text("b 没有对应值", font_size=12, color=Colors.ACCENT)
        invalid2_reason.next_to(invalid2_group, DOWN, buff=0.15)
        
        # 排列三组
        all_groups = VGroup(
            VGroup(valid_full, valid_reason),
            VGroup(invalid1_full, invalid1_reason),
            VGroup(invalid2_full, invalid2_reason)
        ).arrange(RIGHT, buff=0.6)
        all_groups.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(all_groups[0]), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(all_groups[1]), run_time=0.6)
        self.wait(0.5)
        self.play(FadeIn(all_groups[2]), run_time=0.6)
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(all_groups), run_time=0.5)
    
    def key_understanding(self):
        """关键理解"""
        section_title = Text("关键理解", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 两条规则
        rules = VGroup()
        
        rule1 = VGroup(
            Text("✓ 允许：", font_size=18, color=Colors.CODOMAIN_COLOR),
            Text("S 中不同元素可以对应 T 中同一元素", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        rule1_ex = Text("（多人可坐同一座位）", font_size=14, color=Colors.GRAY)
        rule1_ex.next_to(rule1, DOWN, buff=0.1, aligned_edge=LEFT)
        rules.add(VGroup(rule1, rule1_ex))
        
        rule2 = VGroup(
            Text("✗ 禁止：", font_size=18, color=Colors.ACCENT),
            Text("S 中一个元素对应 T 中多个元素", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        rule2_ex = Text("（一人不能同时坐多个座位）", font_size=14, color=Colors.GRAY)
        rule2_ex.next_to(rule2, DOWN, buff=0.1, aligned_edge=LEFT)
        rules.add(VGroup(rule2, rule2_ex))
        
        rules.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        rules.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for rule in rules:
            self.play(FadeIn(rule, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.5)
        
        # 核心思想
        core = VGroup(
            Text("函数的本质：", font_size=18, color=Colors.PRIMARY),
            Text("为定义域中的每个元素分配唯一的值域元素", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        core.next_to(rules, DOWN, buff=0.6).set_x(0)
        
        core_box = SurroundingRectangle(core, color=Colors.PRIMARY, buff=0.2)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(rules),
            FadeOut(core), FadeOut(core_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_01_functions.py FunctionsIntro
    pass
