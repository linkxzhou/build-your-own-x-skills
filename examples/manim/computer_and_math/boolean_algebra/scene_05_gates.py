"""
Scene 5: 布尔函数与逻辑门
从数学走向电路，介绍布尔函数和逻辑门
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    ZERO = "#2C3E50"         # 0的颜色
    ONE = "#F39C12"          # 1的颜色
    AND_COLOR = "#E74C3C"    # AND颜色
    OR_COLOR = "#3498DB"     # OR颜色
    NOT_COLOR = "#9B59B6"    # NOT颜色
    XOR_COLOR = "#2ECC71"    # XOR颜色
    NAND_COLOR = "#E91E63"   # NAND颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_and_gate(size=1.0):
    """创建AND门符号"""
    gate = VGroup()
    
    # 主体 - 左边矩形 + 右边半圆
    body = VGroup()
    rect = Rectangle(width=0.6 * size, height=0.6 * size)
    rect.set_stroke(Colors.AND_COLOR, width=2)
    rect.shift(LEFT * 0.15 * size)
    
    arc = Arc(radius=0.3 * size, start_angle=-PI/2, angle=PI)
    arc.set_stroke(Colors.AND_COLOR, width=2)
    arc.shift(RIGHT * 0.15 * size)
    
    body.add(rect, arc)
    
    # 输入线
    in1 = Line(LEFT * 0.8 * size + UP * 0.15 * size, 
               LEFT * 0.45 * size + UP * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    in2 = Line(LEFT * 0.8 * size + DOWN * 0.15 * size,
               LEFT * 0.45 * size + DOWN * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    
    # 输出线
    out = Line(RIGHT * 0.45 * size, RIGHT * 0.8 * size,
               stroke_width=2, color=Colors.AND_COLOR)
    
    gate.add(body, in1, in2, out)
    return gate


def create_or_gate(size=1.0):
    """创建OR门符号"""
    gate = VGroup()
    
    # 简化的OR门形状
    points = [
        LEFT * 0.4 * size + UP * 0.3 * size,
        RIGHT * 0.1 * size + UP * 0.3 * size,
        RIGHT * 0.4 * size,
        RIGHT * 0.1 * size + DOWN * 0.3 * size,
        LEFT * 0.4 * size + DOWN * 0.3 * size,
    ]
    
    # 上曲线
    top_line = Line(points[0], points[1], stroke_width=2, color=Colors.OR_COLOR)
    # 右上弧
    top_arc = ArcBetweenPoints(points[1], points[2], angle=-0.5)
    top_arc.set_stroke(Colors.OR_COLOR, width=2)
    # 右下弧
    bottom_arc = ArcBetweenPoints(points[2], points[3], angle=-0.5)
    bottom_arc.set_stroke(Colors.OR_COLOR, width=2)
    # 下曲线
    bottom_line = Line(points[3], points[4], stroke_width=2, color=Colors.OR_COLOR)
    # 左弧
    left_arc = ArcBetweenPoints(points[4], points[0], angle=-0.3)
    left_arc.set_stroke(Colors.OR_COLOR, width=2)
    
    body = VGroup(top_line, top_arc, bottom_arc, bottom_line, left_arc)
    
    # 输入线
    in1 = Line(LEFT * 0.8 * size + UP * 0.15 * size,
               LEFT * 0.3 * size + UP * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    in2 = Line(LEFT * 0.8 * size + DOWN * 0.15 * size,
               LEFT * 0.3 * size + DOWN * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    
    # 输出线
    out = Line(RIGHT * 0.4 * size, RIGHT * 0.8 * size,
               stroke_width=2, color=Colors.OR_COLOR)
    
    gate.add(body, in1, in2, out)
    return gate


def create_not_gate(size=1.0):
    """创建NOT门符号（三角形+小圆）"""
    gate = VGroup()
    
    # 三角形
    triangle = Triangle()
    triangle.set_height(0.5 * size)
    triangle.set_width(0.4 * size)
    triangle.rotate(-PI/2)
    triangle.set_stroke(Colors.NOT_COLOR, width=2)
    triangle.set_fill(Colors.BG, opacity=1)
    
    # 输出端小圆（表示取反）
    circle = Circle(radius=0.06 * size)
    circle.set_stroke(Colors.NOT_COLOR, width=2)
    circle.next_to(triangle, RIGHT, buff=0.02 * size)
    
    body = VGroup(triangle, circle)
    
    # 输入线
    inp = Line(LEFT * 0.6 * size, LEFT * 0.2 * size,
               stroke_width=2, color=Colors.PRIMARY)
    
    # 输出线
    out = Line(RIGHT * 0.28 * size, RIGHT * 0.6 * size,
               stroke_width=2, color=Colors.NOT_COLOR)
    
    gate.add(body, inp, out)
    return gate


def create_nand_gate(size=1.0):
    """创建NAND门符号（AND + 小圆）"""
    gate = VGroup()
    
    # AND门主体
    rect = Rectangle(width=0.5 * size, height=0.5 * size)
    rect.set_stroke(Colors.NAND_COLOR, width=2)
    rect.shift(LEFT * 0.1 * size)
    
    arc = Arc(radius=0.25 * size, start_angle=-PI/2, angle=PI)
    arc.set_stroke(Colors.NAND_COLOR, width=2)
    arc.shift(RIGHT * 0.15 * size)
    
    # 输出端小圆
    circle = Circle(radius=0.05 * size)
    circle.set_stroke(Colors.NAND_COLOR, width=2)
    circle.move_to(RIGHT * 0.45 * size)
    
    body = VGroup(rect, arc, circle)
    
    # 输入线
    in1 = Line(LEFT * 0.7 * size + UP * 0.12 * size,
               LEFT * 0.35 * size + UP * 0.12 * size,
               stroke_width=2, color=Colors.PRIMARY)
    in2 = Line(LEFT * 0.7 * size + DOWN * 0.12 * size,
               LEFT * 0.35 * size + DOWN * 0.12 * size,
               stroke_width=2, color=Colors.PRIMARY)
    
    # 输出线
    out = Line(RIGHT * 0.5 * size, RIGHT * 0.7 * size,
               stroke_width=2, color=Colors.NAND_COLOR)
    
    gate.add(body, in1, in2, out)
    return gate


def create_xor_gate(size=1.0):
    """创建XOR门符号"""
    gate = VGroup()
    
    # 类似OR门但前面多一条弧
    points = [
        LEFT * 0.4 * size + UP * 0.3 * size,
        RIGHT * 0.1 * size + UP * 0.3 * size,
        RIGHT * 0.4 * size,
        RIGHT * 0.1 * size + DOWN * 0.3 * size,
        LEFT * 0.4 * size + DOWN * 0.3 * size,
    ]
    
    top_line = Line(points[0], points[1], stroke_width=2, color=Colors.XOR_COLOR)
    top_arc = ArcBetweenPoints(points[1], points[2], angle=-0.5)
    top_arc.set_stroke(Colors.XOR_COLOR, width=2)
    bottom_arc = ArcBetweenPoints(points[2], points[3], angle=-0.5)
    bottom_arc.set_stroke(Colors.XOR_COLOR, width=2)
    bottom_line = Line(points[3], points[4], stroke_width=2, color=Colors.XOR_COLOR)
    left_arc = ArcBetweenPoints(points[4], points[0], angle=-0.3)
    left_arc.set_stroke(Colors.XOR_COLOR, width=2)
    
    # XOR特有的前置弧
    extra_arc = ArcBetweenPoints(
        LEFT * 0.5 * size + DOWN * 0.3 * size,
        LEFT * 0.5 * size + UP * 0.3 * size,
        angle=-0.3
    )
    extra_arc.set_stroke(Colors.XOR_COLOR, width=2)
    
    body = VGroup(top_line, top_arc, bottom_arc, bottom_line, left_arc, extra_arc)
    
    # 输入输出线
    in1 = Line(LEFT * 0.8 * size + UP * 0.15 * size,
               LEFT * 0.35 * size + UP * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    in2 = Line(LEFT * 0.8 * size + DOWN * 0.15 * size,
               LEFT * 0.35 * size + DOWN * 0.15 * size,
               stroke_width=2, color=Colors.PRIMARY)
    out = Line(RIGHT * 0.4 * size, RIGHT * 0.8 * size,
               stroke_width=2, color=Colors.XOR_COLOR)
    
    gate.add(body, in1, in2, out)
    return gate


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene05Gates(Scene):
    """Scene 5: 布尔函数与逻辑门"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_boolean_functions()
        self.section_basic_gates()
        self.section_derived_gates()
        self.section_nand_universal()
        
        clear_scene(self)
    
    def section_boolean_functions(self):
        """布尔函数介绍"""
        section_title = Text("布尔函数", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("定义: 输入输出都是布尔值的函数", font_size=16, color=Colors.GRAY),
            MathTex(r"f: \{0,1\}^n \rightarrow \{0,1\}", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 示例
        example_title = Text("示例:", font_size=16, color=Colors.TEXT)
        example_title.next_to(definition, DOWN, buff=0.4).align_to(definition, LEFT).shift(LEFT * 1)
        
        self.play(FadeIn(example_title))
        
        example = MathTex(
            r"f(x, y) = x \land (x \lor \neg y)",
            font_size=22, color=Colors.PRIMARY
        )
        example.next_to(example_title, DOWN, buff=0.2)
        
        self.play(Write(example))
        
        # 函数数量
        count_info = VGroup(
            Text("n 变量布尔函数的数量:", font_size=14, color=Colors.TEXT),
            MathTex(r"2^{2^n}", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        count_info.next_to(example, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(count_info))
        
        # 具体数字
        counts = VGroup(
            VGroup(
                Text("n=1:", font_size=14, color=Colors.GRAY),
                MathTex(r"2^2 = 4", font_size=16, color=Colors.TEXT),
                Text("种", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("n=2:", font_size=14, color=Colors.GRAY),
                MathTex(r"2^4 = 16", font_size=16, color=Colors.TEXT),
                Text("种", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("n=3:", font_size=14, color=Colors.GRAY),
                MathTex(r"2^8 = 256", font_size=16, color=Colors.TEXT),
                Text("种", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(RIGHT, buff=0.5)
        counts.next_to(count_info, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(counts))
        
        # 提示
        hint = Text("每种布尔函数都可以用逻辑门电路来实现！", font_size=16, color=Colors.PRIMARY)
        hint.next_to(counts, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(hint, shift=UP * 0.1))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, definition, example_title, example,
            count_info, counts, hint
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_basic_gates(self):
        """基本逻辑门"""
        section_title = Text("基本逻辑门", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("逻辑门是实现布尔运算的电子电路", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 三种基本门
        gates_title = Text("三种基本门:", font_size=16, color=Colors.TEXT)
        gates_title.next_to(intro, DOWN, buff=0.4).align_to(intro, LEFT).shift(LEFT * 2.5)
        
        self.play(FadeIn(gates_title))
        
        # AND门
        and_group = VGroup()
        and_gate = create_and_gate(size=0.9)
        and_label = Text("AND门", font_size=14, color=Colors.AND_COLOR)
        and_formula = MathTex(r"Y = A \land B", font_size=16, color=Colors.TEXT)
        and_truth = Text("全1出1", font_size=12, color=Colors.GRAY)
        
        and_info = VGroup(and_label, and_formula, and_truth).arrange(DOWN, buff=0.1)
        and_group.add(and_gate, and_info)
        and_group.arrange(DOWN, buff=0.2)
        
        # OR门
        or_group = VGroup()
        or_gate = create_or_gate(size=0.9)
        or_label = Text("OR门", font_size=14, color=Colors.OR_COLOR)
        or_formula = MathTex(r"Y = A \lor B", font_size=16, color=Colors.TEXT)
        or_truth = Text("有1出1", font_size=12, color=Colors.GRAY)
        
        or_info = VGroup(or_label, or_formula, or_truth).arrange(DOWN, buff=0.1)
        or_group.add(or_gate, or_info)
        or_group.arrange(DOWN, buff=0.2)
        
        # NOT门
        not_group = VGroup()
        not_gate = create_not_gate(size=0.9)
        not_label = Text("NOT门", font_size=14, color=Colors.NOT_COLOR)
        not_formula = MathTex(r"Y = \neg A", font_size=16, color=Colors.TEXT)
        not_truth = Text("取反", font_size=12, color=Colors.GRAY)
        
        not_info = VGroup(not_label, not_formula, not_truth).arrange(DOWN, buff=0.1)
        not_group.add(not_gate, not_info)
        not_group.arrange(DOWN, buff=0.2)
        
        gates = VGroup(and_group, or_group, not_group).arrange(RIGHT, buff=0.8)
        gates.next_to(gates_title, DOWN, buff=0.3).set_x(0)
        
        for gate in gates:
            self.play(FadeIn(gate, shift=UP * 0.2), run_time=0.5)
        
        # 关键信息
        key_info = Text("任何布尔函数都可以用这三种门组合实现", font_size=14, color=Colors.PRIMARY)
        key_info.next_to(gates, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_info))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(section_title, intro, gates_title, gates, key_info)
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_derived_gates(self):
        """派生逻辑门"""
        section_title = Text("派生逻辑门", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("由基本门组合而成的常用门", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # NAND门
        nand_group = VGroup()
        nand_gate = create_nand_gate(size=0.85)
        nand_label = Text("NAND门", font_size=14, color=Colors.NAND_COLOR)
        nand_formula = MathTex(r"Y = \neg(A \land B)", font_size=16, color=Colors.TEXT)
        nand_truth = Text("非全1", font_size=12, color=Colors.GRAY)
        
        nand_info = VGroup(nand_label, nand_formula, nand_truth).arrange(DOWN, buff=0.1)
        nand_group.add(nand_gate, nand_info)
        nand_group.arrange(DOWN, buff=0.2)
        
        # NOR门
        nor_group = VGroup()
        nor_label = Text("NOR门", font_size=14, color=Colors.NOT_COLOR)
        nor_formula = MathTex(r"Y = \neg(A \lor B)", font_size=16, color=Colors.TEXT)
        nor_truth = Text("全0出1", font_size=12, color=Colors.GRAY)
        
        # 简化的NOR门示意
        nor_symbol = VGroup(
            Text("NOR", font_size=16, color=Colors.NOT_COLOR),
        )
        nor_box = SurroundingRectangle(nor_symbol, color=Colors.NOT_COLOR, buff=0.15)
        nor_gate = VGroup(nor_box, nor_symbol)
        
        nor_info = VGroup(nor_label, nor_formula, nor_truth).arrange(DOWN, buff=0.1)
        nor_group.add(nor_gate, nor_info)
        nor_group.arrange(DOWN, buff=0.2)
        
        # XOR门
        xor_group = VGroup()
        xor_gate = create_xor_gate(size=0.85)
        xor_label = Text("XOR门", font_size=14, color=Colors.XOR_COLOR)
        xor_formula = MathTex(r"Y = A \oplus B", font_size=16, color=Colors.TEXT)
        xor_truth = Text("不同出1", font_size=12, color=Colors.GRAY)
        
        xor_info = VGroup(xor_label, xor_formula, xor_truth).arrange(DOWN, buff=0.1)
        xor_group.add(xor_gate, xor_info)
        xor_group.arrange(DOWN, buff=0.2)
        
        # XNOR门
        xnor_group = VGroup()
        xnor_label = Text("XNOR门", font_size=14, color=Colors.SECONDARY)
        xnor_formula = MathTex(r"Y = \neg(A \oplus B)", font_size=16, color=Colors.TEXT)
        xnor_truth = Text("相同出1", font_size=12, color=Colors.GRAY)
        
        xnor_symbol = VGroup(
            Text("XNOR", font_size=16, color=Colors.SECONDARY),
        )
        xnor_box = SurroundingRectangle(xnor_symbol, color=Colors.SECONDARY, buff=0.15)
        xnor_gate = VGroup(xnor_box, xnor_symbol)
        
        xnor_info = VGroup(xnor_label, xnor_formula, xnor_truth).arrange(DOWN, buff=0.1)
        xnor_group.add(xnor_gate, xnor_info)
        xnor_group.arrange(DOWN, buff=0.2)
        
        # 排列
        gates = VGroup(nand_group, nor_group, xor_group, xnor_group).arrange(RIGHT, buff=0.6)
        gates.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        for gate in gates:
            self.play(FadeIn(gate, shift=UP * 0.2), run_time=0.4)
        
        # XOR的特殊意义
        xor_note = VGroup(
            Text("XOR特别重要：", font_size=14, color=Colors.XOR_COLOR),
            Text("• 模2加法", font_size=12, color=Colors.GRAY),
            Text("• 加法器的核心", font_size=12, color=Colors.GRAY),
            Text("• 密码学常用", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        xor_note.next_to(gates, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(xor_note))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(section_title, intro, gates, xor_note)
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_nand_universal(self):
        """NAND门的万能性"""
        section_title = Text("NAND门的万能性", font_size=24, color=Colors.NAND_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 核心信息
        core_info = Text("只用NAND门就能构建所有其他逻辑门！", font_size=18, color=Colors.PRIMARY)
        core_info.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(core_info))
        self.wait(0.5)
        
        # 构建NOT
        not_title = Text("用NAND构建NOT:", font_size=14, color=Colors.TEXT)
        not_title.next_to(core_info, DOWN, buff=0.5).align_to(core_info, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(not_title))
        
        not_formula = MathTex(
            r"\neg A = A \uparrow A",
            font_size=20, color=Colors.NOT_COLOR
        )
        not_desc = Text("(将两个输入都接同一个信号)", font_size=12, color=Colors.GRAY)
        not_group = VGroup(not_formula, not_desc).arrange(DOWN, buff=0.1)
        not_group.next_to(not_title, DOWN, buff=0.2)
        
        self.play(FadeIn(not_group))
        
        # 构建AND
        and_title = Text("用NAND构建AND:", font_size=14, color=Colors.TEXT)
        and_title.next_to(not_group, DOWN, buff=0.35).align_to(not_title, LEFT)
        
        self.play(FadeIn(and_title))
        
        and_formula = MathTex(
            r"A \land B = (A \uparrow B) \uparrow (A \uparrow B)",
            font_size=20, color=Colors.AND_COLOR
        )
        and_desc = Text("(NAND后再NAND自己)", font_size=12, color=Colors.GRAY)
        and_group = VGroup(and_formula, and_desc).arrange(DOWN, buff=0.1)
        and_group.next_to(and_title, DOWN, buff=0.2)
        
        self.play(FadeIn(and_group))
        
        # 构建OR
        or_title = Text("用NAND构建OR:", font_size=14, color=Colors.TEXT)
        or_title.next_to(and_group, DOWN, buff=0.35).align_to(not_title, LEFT)
        
        self.play(FadeIn(or_title))
        
        or_formula = MathTex(
            r"A \lor B = (A \uparrow A) \uparrow (B \uparrow B)",
            font_size=20, color=Colors.OR_COLOR
        )
        or_desc = Text("(德摩根定律的应用)", font_size=12, color=Colors.GRAY)
        or_group = VGroup(or_formula, or_desc).arrange(DOWN, buff=0.1)
        or_group.next_to(or_title, DOWN, buff=0.2)
        
        self.play(FadeIn(or_group))
        
        self.wait(0.5)
        
        # 实际意义
        significance = VGroup(
            Text("实际意义:", font_size=14, color=Colors.PRIMARY),
            Text("• 简化芯片制造工艺", font_size=12, color=Colors.GRAY),
            Text("• 只需一种基本单元", font_size=12, color=Colors.GRAY),
            Text("• NAND闪存由此得名", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        significance.next_to(not_title, RIGHT, buff=1.5)
        
        sig_box = SurroundingRectangle(significance, color=Colors.NAND_COLOR, buff=0.15)
        
        self.play(FadeIn(significance), Create(sig_box))
        
        # 强调
        emphasis = Text('"一种门统治一切"', font_size=18, color=Colors.SECONDARY)
        emphasis.next_to(or_group, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(emphasis, scale=0.9))
        
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_05_gates.py Scene05Gates
    pass
