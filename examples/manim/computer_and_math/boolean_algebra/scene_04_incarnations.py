"""
Scene 4: 三个分身实例
展示布尔代数在集合论、命题逻辑、模2算术中的三个具体实例
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
    SET_COLOR = "#E67E22"    # 集合颜色
    LOGIC_COLOR = "#1ABC9C"  # 逻辑颜色
    Z2_COLOR = "#F39C12"     # Z2颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_incarnation_card(title, color, content_items, width=3.5, height=3.0):
    """创建分身卡片"""
    card = VGroup()
    
    # 背景框
    bg = RoundedRectangle(
        corner_radius=0.15,
        width=width,
        height=height,
        fill_color=Colors.BG,
        fill_opacity=0.95,
        stroke_color=color,
        stroke_width=3
    )
    
    # 标题
    title_text = Text(title, font_size=18, color=color)
    title_text.move_to(bg.get_top() + DOWN * 0.3)
    
    # 分隔线
    sep_line = Line(
        bg.get_left() + RIGHT * 0.2 + DOWN * 0.5,
        bg.get_right() + LEFT * 0.2 + DOWN * 0.5,
        color=color,
        stroke_width=1
    )
    
    # 内容
    content = VGroup()
    for item in content_items:
        if isinstance(item, tuple):
            # (label, value) 格式
            label = Text(item[0], font_size=12, color=Colors.GRAY)
            value = MathTex(item[1], font_size=18, color=Colors.TEXT)
            row = VGroup(label, value).arrange(RIGHT, buff=0.1)
        else:
            row = Text(item, font_size=14, color=Colors.TEXT)
        content.add(row)
    
    content.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
    content.move_to(bg.get_center() + DOWN * 0.2)
    
    card.add(bg, title_text, sep_line, content)
    return card


def create_venn_intersection():
    """创建交集韦恩图"""
    venn = VGroup()
    
    circle_a = Circle(radius=0.5, color=Colors.OR_COLOR, stroke_width=2)
    circle_a.shift(LEFT * 0.25)
    
    circle_b = Circle(radius=0.5, color=Colors.AND_COLOR, stroke_width=2)
    circle_b.shift(RIGHT * 0.25)
    
    # 交集区域
    intersection = Intersection(circle_a, circle_b, fill_color=Colors.SECONDARY, fill_opacity=0.5)
    
    label_a = Text("A", font_size=12, color=Colors.OR_COLOR)
    label_a.move_to(circle_a.get_center() + LEFT * 0.3)
    
    label_b = Text("B", font_size=12, color=Colors.AND_COLOR)
    label_b.move_to(circle_b.get_center() + RIGHT * 0.3)
    
    venn.add(circle_a, circle_b, intersection, label_a, label_b)
    return venn


def create_venn_union():
    """创建并集韦恩图"""
    venn = VGroup()
    
    circle_a = Circle(radius=0.5, stroke_width=2)
    circle_a.set_stroke(Colors.OR_COLOR)
    circle_a.set_fill(Colors.OR_COLOR, opacity=0.3)
    circle_a.shift(LEFT * 0.25)
    
    circle_b = Circle(radius=0.5, stroke_width=2)
    circle_b.set_stroke(Colors.AND_COLOR)
    circle_b.set_fill(Colors.AND_COLOR, opacity=0.3)
    circle_b.shift(RIGHT * 0.25)
    
    label_a = Text("A", font_size=12, color=Colors.OR_COLOR)
    label_a.move_to(circle_a.get_center() + LEFT * 0.3)
    
    label_b = Text("B", font_size=12, color=Colors.AND_COLOR)
    label_b.move_to(circle_b.get_center() + RIGHT * 0.3)
    
    venn.add(circle_a, circle_b, label_a, label_b)
    return venn


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene04Incarnations(Scene):
    """Scene 4: 三个分身实例"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_intro()
        self.section_set_theory()
        self.section_propositional_logic()
        self.section_z2_arithmetic()
        self.section_comparison()
        
        clear_scene(self)
    
    def section_intro(self):
        """引入：布尔代数的三个分身"""
        section_title = Text("布尔代数的三个分身", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 引言
        intro = VGroup(
            Text("同一套抽象结构，在不同领域有不同的具体实现。", font_size=16, color=Colors.GRAY),
            Text("它们遵循相同的运算规则，却有各自的应用场景。", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        intro.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intro))
        self.wait(1)
        
        # 三个分身预览
        preview = VGroup(
            VGroup(
                Circle(radius=0.3, color=Colors.SET_COLOR, stroke_width=2),
                Text("集合论", font_size=14, color=Colors.SET_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Circle(radius=0.3, color=Colors.LOGIC_COLOR, stroke_width=2),
                Text("命题逻辑", font_size=14, color=Colors.LOGIC_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Circle(radius=0.3, color=Colors.Z2_COLOR, stroke_width=2),
                Text("模2算术", font_size=14, color=Colors.Z2_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.0)
        preview.next_to(intro, DOWN, buff=0.6).set_x(0)
        
        for item in preview:
            self.play(FadeIn(item, scale=0.8), run_time=0.4)
        
        self.wait(1.5)
        
        # 清除
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(preview), run_time=0.5)
    
    def section_set_theory(self):
        """分身一：集合论"""
        section_title = Text("分身一：集合论", font_size=24, color=Colors.SET_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 介绍
        intro = Text("在幂集 P(U) 上的布尔代数", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 对应关系表
        mapping_title = Text("运算对应：", font_size=16, color=Colors.TEXT)
        mapping_title.next_to(intro, DOWN, buff=0.4).align_to(intro, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(mapping_title))
        
        mappings = VGroup(
            VGroup(
                MathTex(r"\land", font_size=24, color=Colors.AND_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                MathTex(r"\cap", font_size=24, color=Colors.SET_COLOR),
                Text("(交集)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\lor", font_size=24, color=Colors.OR_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                MathTex(r"\cup", font_size=24, color=Colors.SET_COLOR),
                Text("(并集)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\neg", font_size=24, color=Colors.NOT_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                MathTex(r"\overline{A}", font_size=24, color=Colors.SET_COLOR),
                Text("(补集)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.2)
        mappings.next_to(mapping_title, DOWN, buff=0.2)
        
        for m in mappings:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.3)
        
        # 特殊元素
        special_title = Text("特殊元素：", font_size=16, color=Colors.TEXT)
        special_title.next_to(mappings, DOWN, buff=0.4).align_to(mapping_title, LEFT)
        
        specials = VGroup(
            VGroup(
                Text("0", font_size=18, color=Colors.ZERO),
                MathTex(r"\longleftrightarrow", font_size=16, color=Colors.GRAY),
                MathTex(r"\emptyset", font_size=20, color=Colors.SET_COLOR),
                Text("(空集)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("1", font_size=18, color=Colors.ONE),
                MathTex(r"\longleftrightarrow", font_size=16, color=Colors.GRAY),
                MathTex(r"U", font_size=20, color=Colors.SET_COLOR),
                Text("(全集)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.15)
        specials.next_to(special_title, DOWN, buff=0.2)
        
        self.play(FadeIn(special_title), FadeIn(specials))
        
        # 韦恩图示例
        venn_title = Text("韦恩图验证交换律：", font_size=14, color=Colors.TEXT)
        venn_title.next_to(mapping_title, RIGHT, buff=1.5)
        
        self.play(FadeIn(venn_title))
        
        # 创建简单的韦恩图
        venn1 = VGroup()
        c1_a = Circle(radius=0.4, stroke_color=Colors.OR_COLOR, stroke_width=2)
        c1_a.set_fill(Colors.OR_COLOR, opacity=0.3)
        c1_a.shift(LEFT * 0.2)
        
        c1_b = Circle(radius=0.4, stroke_color=Colors.AND_COLOR, stroke_width=2)
        c1_b.set_fill(Colors.AND_COLOR, opacity=0.3)
        c1_b.shift(RIGHT * 0.2)
        
        l1_a = Text("A", font_size=10, color=Colors.OR_COLOR).move_to(c1_a.get_left() + LEFT * 0.15)
        l1_b = Text("B", font_size=10, color=Colors.AND_COLOR).move_to(c1_b.get_right() + RIGHT * 0.15)
        
        venn1.add(c1_a, c1_b, l1_a, l1_b)
        
        label1 = MathTex(r"A \cap B", font_size=16, color=Colors.SET_COLOR)
        venn1_group = VGroup(venn1, label1).arrange(DOWN, buff=0.15)
        venn1_group.next_to(venn_title, DOWN, buff=0.2)
        
        venn2 = VGroup()
        c2_a = Circle(radius=0.4, stroke_color=Colors.AND_COLOR, stroke_width=2)
        c2_a.set_fill(Colors.AND_COLOR, opacity=0.3)
        c2_a.shift(LEFT * 0.2)
        
        c2_b = Circle(radius=0.4, stroke_color=Colors.OR_COLOR, stroke_width=2)
        c2_b.set_fill(Colors.OR_COLOR, opacity=0.3)
        c2_b.shift(RIGHT * 0.2)
        
        l2_a = Text("B", font_size=10, color=Colors.AND_COLOR).move_to(c2_a.get_left() + LEFT * 0.15)
        l2_b = Text("A", font_size=10, color=Colors.OR_COLOR).move_to(c2_b.get_right() + RIGHT * 0.15)
        
        venn2.add(c2_a, c2_b, l2_a, l2_b)
        
        label2 = MathTex(r"B \cap A", font_size=16, color=Colors.SET_COLOR)
        venn2_group = VGroup(venn2, label2).arrange(DOWN, buff=0.15)
        
        equal_sign = MathTex(r"=", font_size=24, color=Colors.SECONDARY)
        
        venn_demo = VGroup(venn1_group, equal_sign, venn2_group).arrange(RIGHT, buff=0.3)
        venn_demo.next_to(venn_title, DOWN, buff=0.2)
        
        self.play(FadeIn(venn_demo))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, intro, mapping_title, mappings,
            special_title, specials, venn_title, venn_demo
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_propositional_logic(self):
        """分身二：命题逻辑"""
        section_title = Text("分身二：命题逻辑", font_size=24, color=Colors.LOGIC_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 介绍
        intro = Text("在 {真, 假} 上的布尔代数", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 对应关系
        mapping_title = Text("运算对应：", font_size=16, color=Colors.TEXT)
        mapping_title.next_to(intro, DOWN, buff=0.4).align_to(intro, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(mapping_title))
        
        mappings = VGroup(
            VGroup(
                MathTex(r"\land", font_size=24, color=Colors.AND_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                Text('逻辑"且"', font_size=16, color=Colors.LOGIC_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\lor", font_size=24, color=Colors.OR_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                Text('逻辑"或"', font_size=16, color=Colors.LOGIC_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                MathTex(r"\neg", font_size=24, color=Colors.NOT_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                Text('逻辑"非"', font_size=16, color=Colors.LOGIC_COLOR),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.2)
        mappings.next_to(mapping_title, DOWN, buff=0.2)
        
        for m in mappings:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.3)
        
        # 特殊元素
        special_title = Text("特殊元素：", font_size=16, color=Colors.TEXT)
        special_title.next_to(mappings, DOWN, buff=0.35).align_to(mapping_title, LEFT)
        
        specials = VGroup(
            VGroup(
                Text("0", font_size=18, color=Colors.ZERO),
                MathTex(r"\longleftrightarrow", font_size=16, color=Colors.GRAY),
                Text("F (False)", font_size=16, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("1", font_size=18, color=Colors.ONE),
                MathTex(r"\longleftrightarrow", font_size=16, color=Colors.GRAY),
                Text("T (True)", font_size=16, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.15)
        specials.next_to(special_title, DOWN, buff=0.2)
        
        self.play(FadeIn(special_title), FadeIn(specials))
        
        # 编程应用
        code_title = Text("编程中的应用：", font_size=16, color=Colors.TEXT)
        code_title.next_to(mapping_title, RIGHT, buff=2.0)
        
        self.play(FadeIn(code_title))
        
        code_examples = VGroup(
            Text("if (a && b)", font_size=14, color=Colors.AND_COLOR),
            Text("    // a AND b", font_size=12, color=Colors.GRAY),
            Text("if (a || b)", font_size=14, color=Colors.OR_COLOR),
            Text("    // a OR b", font_size=12, color=Colors.GRAY),
            Text("if (!a)", font_size=14, color=Colors.NOT_COLOR),
            Text("    // NOT a", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        code_examples.next_to(code_title, DOWN, buff=0.2)
        
        code_box = SurroundingRectangle(code_examples, color=Colors.LOGIC_COLOR, buff=0.15)
        
        self.play(FadeIn(code_examples), Create(code_box))
        
        # 组合条件
        combo_text = Text("组合条件判断", font_size=12, color=Colors.GRAY)
        combo_text.next_to(code_box, DOWN, buff=0.15)
        
        self.play(FadeIn(combo_text))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, intro, mapping_title, mappings,
            special_title, specials, code_title, code_examples,
            code_box, combo_text
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_z2_arithmetic(self):
        """分身三：模2整数算术"""
        section_title = Text("分身三：模2整数算术 (ℤ₂)", font_size=24, color=Colors.Z2_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 介绍
        intro = Text("在 {0, 1} 上的运算 —— 数字电路的数学模型", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 运算对应
        mapping_title = Text("运算对应：", font_size=16, color=Colors.TEXT)
        mapping_title.next_to(intro, DOWN, buff=0.4).align_to(intro, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(mapping_title))
        
        mappings = VGroup(
            VGroup(
                MathTex(r"\land", font_size=24, color=Colors.AND_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                Text("乘法 (×)", font_size=16, color=Colors.Z2_COLOR),
                MathTex(r"(1 \times 1 = 1)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                Text("XOR", font_size=18, color=Colors.XOR_COLOR),
                MathTex(r"\longleftrightarrow", font_size=20, color=Colors.GRAY),
                Text("加法 (+)", font_size=16, color=Colors.Z2_COLOR),
                MathTex(r"(1 + 1 = 0)", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.25)
        mappings.next_to(mapping_title, DOWN, buff=0.2)
        
        for m in mappings:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.4)
        
        # 运算表
        table_title = Text("ℤ₂ 运算表：", font_size=16, color=Colors.TEXT)
        table_title.next_to(mappings, DOWN, buff=0.4).align_to(mapping_title, LEFT)
        
        self.play(FadeIn(table_title))
        
        # 乘法表
        mul_title = Text("乘法 (AND)", font_size=14, color=Colors.AND_COLOR)
        mul_table = VGroup(
            VGroup(
                Text("×", font_size=12, color=Colors.GRAY),
                Text("0", font_size=12, color=Colors.ZERO),
                Text("1", font_size=12, color=Colors.ONE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("0", font_size=12, color=Colors.ZERO),
                Text("0", font_size=12, color=Colors.ZERO),
                Text("0", font_size=12, color=Colors.ZERO),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("1", font_size=12, color=Colors.ONE),
                Text("0", font_size=12, color=Colors.ZERO),
                Text("1", font_size=12, color=Colors.ONE),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.15)
        
        mul_group = VGroup(mul_title, mul_table).arrange(DOWN, buff=0.15)
        mul_box = SurroundingRectangle(mul_group, color=Colors.AND_COLOR, buff=0.1)
        
        # 加法表
        add_title = Text("加法 (XOR)", font_size=14, color=Colors.XOR_COLOR)
        add_table = VGroup(
            VGroup(
                Text("+", font_size=12, color=Colors.GRAY),
                Text("0", font_size=12, color=Colors.ZERO),
                Text("1", font_size=12, color=Colors.ONE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("0", font_size=12, color=Colors.ZERO),
                Text("0", font_size=12, color=Colors.ZERO),
                Text("1", font_size=12, color=Colors.ONE),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("1", font_size=12, color=Colors.ONE),
                Text("1", font_size=12, color=Colors.ONE),
                Text("0", font_size=12, color=Colors.ZERO),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.15)
        
        add_group = VGroup(add_title, add_table).arrange(DOWN, buff=0.15)
        add_box = SurroundingRectangle(add_group, color=Colors.XOR_COLOR, buff=0.1)
        
        tables = VGroup(
            VGroup(mul_box, mul_group),
            VGroup(add_box, add_group)
        ).arrange(RIGHT, buff=0.5)
        tables.next_to(table_title, DOWN, buff=0.2)
        
        self.play(FadeIn(tables))
        
        # 关键点：1+1=0
        key_point = VGroup(
            Text("关键特性：", font_size=14, color=Colors.TEXT),
            MathTex(r"1 + 1 = 0", font_size=20, color=Colors.XOR_COLOR),
            Text("(模2: 进位被丢弃)", font_size=12, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.2)
        key_point.next_to(tables, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(key_point))
        
        # 应用说明
        app_note = Text("这正是数字电路中二进制运算的数学基础！", font_size=14, color=Colors.PRIMARY)
        app_note.next_to(key_point, DOWN, buff=0.25).set_x(0)
        
        self.play(FadeIn(app_note, shift=UP * 0.1))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, intro, mapping_title, mappings,
            table_title, tables, key_point, app_note
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_comparison(self):
        """三个分身对比总结"""
        section_title = Text("三个分身的统一性", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建对比表
        # 表头
        header = VGroup(
            Text("", font_size=14),  # 空白
            Text("集合论", font_size=14, color=Colors.SET_COLOR),
            Text("命题逻辑", font_size=14, color=Colors.LOGIC_COLOR),
            Text("ℤ₂", font_size=14, color=Colors.Z2_COLOR),
        ).arrange(RIGHT, buff=0.7)
        header.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(header))
        
        # 数据行
        rows_data = [
            ("元素", ["P(U)", "{T, F}", "{0, 1}"]),
            ("AND", ["∩", "且", "×"]),
            ("OR", ["∪", "或", "XOR作为加法"]),
            ("NOT", ["补集", "非", "1-x"]),
            ("0", ["∅", "F", "0"]),
            ("1", ["U", "T", "1"]),
        ]
        
        rows = VGroup()
        for label, values in rows_data:
            row = VGroup(
                Text(label, font_size=12, color=Colors.GRAY),
                Text(values[0], font_size=12, color=Colors.SET_COLOR),
                Text(values[1], font_size=12, color=Colors.LOGIC_COLOR),
                Text(values[2], font_size=12, color=Colors.Z2_COLOR),
            ).arrange(RIGHT, buff=0.7)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(header, DOWN, buff=0.2)
        
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.25)
        
        self.wait(0.5)
        
        # 核心信息
        core_message = VGroup(
            Text("核心洞见：", font_size=16, color=Colors.PRIMARY),
            Text("虽然表面不同，但它们遵循", font_size=14, color=Colors.TEXT),
            Text("完全相同的代数规则！", font_size=16, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        core_message.next_to(rows, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(core_message, shift=UP * 0.2))
        
        # 强调框
        emphasis_box = SurroundingRectangle(core_message, color=Colors.PRIMARY, buff=0.15)
        self.play(Create(emphasis_box))
        
        # 应用提示
        hint = Text("这就是抽象代数的威力 —— 一套理论，多种应用", font_size=14, color=Colors.GRAY)
        hint.next_to(emphasis_box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(hint))
        
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_04_incarnations.py Scene04Incarnations
    pass
