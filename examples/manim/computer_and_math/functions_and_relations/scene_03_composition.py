"""
函数与关系 - Scene 3: 函数复合
介绍函数复合的概念和性质

渲染命令: manim -pqh scene_03_composition.py FunctionComposition
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
    COMPOSE_COLOR = "#9B59B6"    # 复合紫


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_mapping_arrow(start_pos, end_pos, color=Colors.ARROW_COLOR, curved=False):
    """创建映射箭头"""
    if curved:
        arrow = CurvedArrow(
            start_pos, end_pos,
            color=color,
            stroke_width=2,
        )
    else:
        arrow = Arrow(
            start_pos, end_pos,
            color=color,
            stroke_width=2,
            buff=0.1,
            max_tip_length_to_length_ratio=0.15
        )
    return arrow


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== Scene 3: 函数复合 ==========
class FunctionComposition(Scene):
    """函数复合的概念和性质"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.definition()
        self.visualization()
        self.properties()
        self.programming_analogy()
        
        clear_scene(self)
    
    def definition(self):
        """复合定义"""
        section_title = Text("函数的复合", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 两个函数
        funcs = VGroup(
            VGroup(
                Text("函数 ", font_size=18, color=Colors.GRAY),
                MathTex(r"f: S \rightarrow T", font_size=22, color=Colors.FUNCTION_COLOR),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("函数 ", font_size=18, color=Colors.GRAY),
                MathTex(r"g: T \rightarrow U", font_size=22, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2)
        funcs.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(funcs))
        
        # 复合函数
        compose_def = VGroup(
            Text("复合函数 ", font_size=18, color=Colors.GRAY),
            MathTex(r"(g \circ f): S \rightarrow U", font_size=24, color=Colors.COMPOSE_COLOR),
        ).arrange(RIGHT, buff=0.1)
        compose_def.next_to(funcs, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(compose_def))
        
        # 定义公式
        formula = MathTex(
            r"(g \circ f)(s) = g(f(s))",
            font_size=28, color=Colors.TEXT
        )
        formula.next_to(compose_def, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(formula))
        
        # 理解说明
        explanation = VGroup(
            Text("理解：", font_size=16, color=Colors.PRIMARY),
            Text("先用 f 把 s 变成 f(s)，", font_size=14, color=Colors.GRAY),
            Text("再用 g 把 f(s) 变成 g(f(s))", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanation.next_to(formula, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        
        # 读法注意
        note = VGroup(
            Text("注意：", font_size=14, color=Colors.ACCENT),
            Text("g ∘ f 读作", font_size=14, color=Colors.GRAY),
            Text('"g after f"', font_size=14, color=Colors.SECONDARY),
            Text("（先f后g）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        note.next_to(explanation, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(funcs), FadeOut(compose_def),
            FadeOut(formula), FadeOut(explanation), FadeOut(note),
            run_time=0.5
        )
    
    def visualization(self):
        """可视化"""
        section_title = Text("复合的可视化", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三个集合 S, T, U
        # S = {a, b}
        s_ellipse = Ellipse(width=1.4, height=2.0)
        s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
        s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        s_ellipse.shift(LEFT * 3.5)
        
        s_label = Text("S", font_size=18, color=Colors.DOMAIN_COLOR)
        s_label.next_to(s_ellipse, UP, buff=0.1)
        
        s_elements = VGroup()
        for elem in ['a', 'b']:
            t = Text(elem, font_size=20, color=Colors.TEXT)
            s_elements.add(t)
        s_elements.arrange(DOWN, buff=0.4)
        s_elements.move_to(s_ellipse.get_center())
        
        # T = {1, 2}
        t_ellipse = Ellipse(width=1.4, height=2.0)
        t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
        t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        
        t_label = Text("T", font_size=18, color=Colors.CODOMAIN_COLOR)
        t_label.next_to(t_ellipse, UP, buff=0.1)
        
        t_elements = VGroup()
        for elem in ['1', '2']:
            t = Text(elem, font_size=20, color=Colors.TEXT)
            t_elements.add(t)
        t_elements.arrange(DOWN, buff=0.4)
        t_elements.move_to(t_ellipse.get_center())
        
        # U = {x, y}
        u_ellipse = Ellipse(width=1.4, height=2.0)
        u_ellipse.set_stroke(Colors.SECONDARY, width=2)
        u_ellipse.set_fill(Colors.SECONDARY, opacity=0.1)
        u_ellipse.shift(RIGHT * 3.5)
        
        u_label = Text("U", font_size=18, color=Colors.SECONDARY)
        u_label.next_to(u_ellipse, UP, buff=0.1)
        
        u_elements = VGroup()
        for elem in ['x', 'y']:
            t = Text(elem, font_size=20, color=Colors.TEXT)
            u_elements.add(t)
        u_elements.arrange(DOWN, buff=0.4)
        u_elements.move_to(u_ellipse.get_center())
        
        sets_group = VGroup(
            s_ellipse, s_label, s_elements,
            t_ellipse, t_label, t_elements,
            u_ellipse, u_label, u_elements
        )
        sets_group.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(sets_group))
        
        # 函数标签
        f_label = MathTex(r"f", font_size=22, color=Colors.FUNCTION_COLOR)
        f_label.move_to((s_ellipse.get_center() + t_ellipse.get_center()) / 2 + UP * 1.3)
        
        g_label = MathTex(r"g", font_size=22, color=Colors.SECONDARY)
        g_label.move_to((t_ellipse.get_center() + u_ellipse.get_center()) / 2 + UP * 1.3)
        
        self.play(FadeIn(f_label), FadeIn(g_label))
        
        # f 的箭头: a→1, b→2
        f_arrows = VGroup(
            create_mapping_arrow(
                s_elements[0].get_right() + RIGHT * 0.05,
                t_elements[0].get_left() + LEFT * 0.05,
                Colors.FUNCTION_COLOR
            ),
            create_mapping_arrow(
                s_elements[1].get_right() + RIGHT * 0.05,
                t_elements[1].get_left() + LEFT * 0.05,
                Colors.FUNCTION_COLOR
            ),
        )
        
        self.play(*[GrowArrow(arr) for arr in f_arrows], run_time=0.6)
        
        # g 的箭头: 1→x, 2→y
        g_arrows = VGroup(
            create_mapping_arrow(
                t_elements[0].get_right() + RIGHT * 0.05,
                u_elements[0].get_left() + LEFT * 0.05,
                Colors.SECONDARY
            ),
            create_mapping_arrow(
                t_elements[1].get_right() + RIGHT * 0.05,
                u_elements[1].get_left() + LEFT * 0.05,
                Colors.SECONDARY
            ),
        )
        
        self.play(*[GrowArrow(arr) for arr in g_arrows], run_time=0.6)
        
        # 复合过程动画
        self.wait(0.5)
        
        # 追踪 a 的复合路径
        trace_text = Text("追踪 a:", font_size=14, color=Colors.PRIMARY)
        trace_text.to_edge(LEFT, buff=0.5).shift(DOWN * 2)
        
        self.play(FadeIn(trace_text))
        
        # a → f(a) = 1
        step1 = MathTex(r"a \xrightarrow{f} 1", font_size=18, color=Colors.FUNCTION_COLOR)
        step1.next_to(trace_text, RIGHT, buff=0.3)
        
        # 高亮 a 和 1
        highlight_a = SurroundingRectangle(s_elements[0], color=Colors.PRIMARY, buff=0.05)
        highlight_1 = SurroundingRectangle(t_elements[0], color=Colors.PRIMARY, buff=0.05)
        
        self.play(Create(highlight_a), Write(step1))
        self.play(Transform(highlight_a, highlight_1))
        self.remove(highlight_a)
        self.add(highlight_1)
        
        # 1 → g(1) = x
        step2 = MathTex(r"\xrightarrow{g} x", font_size=18, color=Colors.SECONDARY)
        step2.next_to(step1, RIGHT, buff=0.2)
        
        highlight_x = SurroundingRectangle(u_elements[0], color=Colors.PRIMARY, buff=0.05)
        
        self.play(Write(step2), Transform(highlight_1, highlight_x))
        self.remove(highlight_1)
        
        # 结论
        conclusion = MathTex(
            r"\Rightarrow (g \circ f)(a) = x",
            font_size=18, color=Colors.COMPOSE_COLOR
        )
        conclusion.next_to(step2, RIGHT, buff=0.3)
        
        self.play(Write(conclusion), FadeOut(highlight_x))
        
        # 复合函数的直接箭头（虚线）
        compose_arrows = VGroup(
            DashedLine(
                s_elements[0].get_right() + RIGHT * 0.1,
                u_elements[0].get_left() + LEFT * 0.1,
                color=Colors.COMPOSE_COLOR,
                stroke_width=2
            ),
            DashedLine(
                s_elements[1].get_right() + RIGHT * 0.1,
                u_elements[1].get_left() + LEFT * 0.1,
                color=Colors.COMPOSE_COLOR,
                stroke_width=2
            ),
        )
        
        compose_label = MathTex(r"g \circ f", font_size=18, color=Colors.COMPOSE_COLOR)
        compose_label.move_to((s_ellipse.get_center() + u_ellipse.get_center()) / 2 + DOWN * 1.5)
        
        self.play(
            Create(compose_arrows[0]), Create(compose_arrows[1]),
            FadeIn(compose_label),
            run_time=0.8
        )
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(sets_group),
            FadeOut(f_label), FadeOut(g_label),
            FadeOut(f_arrows), FadeOut(g_arrows),
            FadeOut(trace_text), FadeOut(step1), FadeOut(step2), FadeOut(conclusion),
            FadeOut(compose_arrows), FadeOut(compose_label),
            run_time=0.5
        )
    
    def properties(self):
        """性质"""
        section_title = Text("复合的性质", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 性质1：顺序重要
        prop1_title = Text("1. 顺序重要（一般不满足交换律）", font_size=18, color=Colors.ACCENT)
        prop1_title.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT).shift(LEFT * 1.5)
        
        prop1_formula = MathTex(
            r"g \circ f \neq f \circ g",
            font_size=24, color=Colors.TEXT
        )
        prop1_formula.next_to(prop1_title, DOWN, buff=0.15)
        
        prop1_note = Text("（除非特殊情况）", font_size=14, color=Colors.GRAY)
        prop1_note.next_to(prop1_formula, RIGHT, buff=0.2)
        
        self.play(FadeIn(prop1_title))
        self.play(Write(prop1_formula), FadeIn(prop1_note))
        
        # 性质2：结合律
        prop2_title = Text("2. 满足结合律", font_size=18, color=Colors.SECONDARY)
        prop2_title.next_to(prop1_formula, DOWN, buff=0.4).align_to(prop1_title, LEFT)
        
        prop2_formula = MathTex(
            r"(h \circ g) \circ f = h \circ (g \circ f)",
            font_size=24, color=Colors.TEXT
        )
        prop2_formula.next_to(prop2_title, DOWN, buff=0.15)
        
        self.play(FadeIn(prop2_title))
        self.play(Write(prop2_formula))
        
        # 性质3：保持性质
        prop3_title = Text("3. 性质的保持", font_size=18, color=Colors.PRIMARY)
        prop3_title.next_to(prop2_formula, DOWN, buff=0.4).align_to(prop1_title, LEFT)
        
        prop3_items = VGroup(
            Text("• 两个单射的复合仍是单射", font_size=14, color=Colors.GRAY),
            Text("• 两个满射的复合仍是满射", font_size=14, color=Colors.GRAY),
            Text("• 两个双射的复合仍是双射", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        prop3_items.next_to(prop3_title, DOWN, buff=0.15)
        
        self.play(FadeIn(prop3_title))
        for item in prop3_items:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.3)
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title),
            FadeOut(prop1_title), FadeOut(prop1_formula), FadeOut(prop1_note),
            FadeOut(prop2_title), FadeOut(prop2_formula),
            FadeOut(prop3_title), FadeOut(prop3_items),
            run_time=0.5
        )
    
    def programming_analogy(self):
        """编程类比"""
        section_title = Text("编程中的函数复合", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 代码示例
        code_title = Text("函数调用链：", font_size=16, color=Colors.PRIMARY)
        code_title.next_to(section_title, DOWN, buff=0.4).shift(LEFT * 2)
        
        code = VGroup(
            Text("# Python 示例", font_size=14, color=Colors.GRAY),
            Text("result = g(f(x))", font_size=16, color=Colors.TEXT),
            Text("", font_size=14),
            Text("# 等价于", font_size=14, color=Colors.GRAY),
            Text("temp = f(x)", font_size=16, color=Colors.FUNCTION_COLOR),
            Text("result = g(temp)", font_size=16, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code.next_to(code_title, DOWN, buff=0.2)
        
        self.play(FadeIn(code_title), FadeIn(code))
        
        # 管道操作
        pipe_title = Text("管道模式：", font_size=16, color=Colors.PRIMARY)
        pipe_title.next_to(code, RIGHT, buff=1.5).align_to(code_title, UP)
        
        pipe = VGroup(
            Text("x", font_size=18, color=Colors.DOMAIN_COLOR),
            Text("→", font_size=16, color=Colors.GRAY),
            Text("f", font_size=18, color=Colors.FUNCTION_COLOR),
            Text("→", font_size=16, color=Colors.GRAY),
            Text("g", font_size=18, color=Colors.SECONDARY),
            Text("→", font_size=16, color=Colors.GRAY),
            Text("result", font_size=18, color=Colors.COMPOSE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        pipe.next_to(pipe_title, DOWN, buff=0.3)
        
        self.play(FadeIn(pipe_title), FadeIn(pipe))
        
        # 应用场景
        applications = VGroup(
            Text("应用场景：", font_size=16, color=Colors.PRIMARY),
            Text("• 数据处理管道", font_size=14, color=Colors.GRAY),
            Text("• 中间件链", font_size=14, color=Colors.GRAY),
            Text("• 函数式编程", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        applications.next_to(pipe, DOWN, buff=0.5).align_to(pipe_title, LEFT)
        
        self.play(FadeIn(applications))
        
        # 核心思想
        insight = VGroup(
            Text("核心思想：", font_size=16, color=Colors.ACCENT),
            Text("复杂操作 = 简单操作的组合", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        insight.next_to(code, DOWN, buff=0.8).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title),
            FadeOut(code_title), FadeOut(code),
            FadeOut(pipe_title), FadeOut(pipe),
            FadeOut(applications),
            FadeOut(insight), FadeOut(insight_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_03_composition.py FunctionComposition
    pass
