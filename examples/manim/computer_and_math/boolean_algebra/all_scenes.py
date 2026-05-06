"""
布尔代数：真与假的数学
完整视频 - 所有场景合并

渲染命令: manim -pqh all_scenes.py BooleanAlgebra
预览命令: manim -pql all_scenes.py BooleanAlgebra
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
    ZERO = "#2C3E50"         # 0的颜色（深蓝灰）
    ONE = "#F39C12"          # 1的颜色（金橙）
    AND_COLOR = "#E74C3C"    # AND颜色
    OR_COLOR = "#3498DB"     # OR颜色
    NOT_COLOR = "#9B59B6"    # NOT颜色
    XOR_COLOR = "#2ECC71"    # XOR颜色
    NAND_COLOR = "#E91E63"   # NAND颜色
    CARRY = "#FF9800"        # 进位颜色
    SUM = "#00BCD4"          # 和颜色
    SET_COLOR = "#E67E22"    # 集合颜色
    LOGIC_COLOR = "#1ABC9C"  # 逻辑颜色
    Z2_COLOR = "#F39C12"     # Z2颜色


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_switch(is_on=False, size=1.0):
    """创建一个开关"""
    base = RoundedRectangle(
        width=size * 1.5, height=size * 0.8,
        corner_radius=size * 0.4,
        fill_color=Colors.ONE if is_on else Colors.ZERO,
        fill_opacity=0.8,
        stroke_color=Colors.PRIMARY,
        stroke_width=2
    )
    
    knob = Circle(radius=size * 0.3)
    knob.set_fill(Colors.TEXT, opacity=1)
    knob.set_stroke(Colors.PRIMARY, width=2)
    
    if is_on:
        knob.move_to(base.get_center() + RIGHT * size * 0.35)
    else:
        knob.move_to(base.get_center() + LEFT * size * 0.35)
    
    return VGroup(base, knob)


def create_lightbulb(is_on=False, size=1.0):
    """创建一个灯泡"""
    bulb = Circle(radius=size * 0.4)
    bulb.set_stroke(Colors.PRIMARY, width=2)
    if is_on:
        bulb.set_fill(Colors.ONE, opacity=0.9)
    else:
        bulb.set_fill(Colors.ZERO, opacity=0.5)
    
    base_rect = Rectangle(width=size * 0.3, height=size * 0.2)
    base_rect.set_stroke(Colors.PRIMARY, width=2)
    base_rect.set_fill(Colors.GRAY, opacity=0.5)
    base_rect.next_to(bulb, DOWN, buff=0)
    
    rays = VGroup()
    if is_on:
        for angle in range(0, 360, 45):
            ray = Line(
                bulb.get_center() + size * 0.5 * np.array([np.cos(angle * DEGREES), np.sin(angle * DEGREES), 0]),
                bulb.get_center() + size * 0.7 * np.array([np.cos(angle * DEGREES), np.sin(angle * DEGREES), 0]),
                color=Colors.ONE,
                stroke_width=2
            )
            rays.add(ray)
    
    return VGroup(bulb, base_rect, rays)


def create_bit_display(value, size=0.8):
    """创建一个比特显示"""
    color = Colors.ONE if value == 1 else Colors.ZERO
    
    rect = RoundedRectangle(
        width=size, height=size,
        corner_radius=size * 0.1,
        fill_color=color,
        fill_opacity=0.8,
        stroke_color=Colors.PRIMARY,
        stroke_width=2
    )
    
    text = Text(str(value), font_size=int(size * 40), color=Colors.TEXT)
    text.move_to(rect.get_center())
    
    return VGroup(rect, text)


def create_bit_cell(value, size=0.4):
    """创建一个比特单元格"""
    color = Colors.ONE if value == 1 else Colors.ZERO
    
    rect = Square(side_length=size)
    rect.set_fill(color, opacity=0.8)
    rect.set_stroke(Colors.PRIMARY, width=2)
    
    text = Text(str(value), font_size=int(size * 40), color=Colors.TEXT)
    text.move_to(rect.get_center())
    
    return VGroup(rect, text)


def create_truth_table_header(inputs, output, op_color):
    """创建真值表表头"""
    header = VGroup()
    
    for inp in inputs:
        cell = Text(inp, font_size=18, color=Colors.TEXT)
        header.add(cell)
    
    out_cell = Text(output, font_size=18, color=op_color)
    header.add(out_cell)
    
    header.arrange(RIGHT, buff=0.8)
    return header


def create_truth_table_row(values, result, result_color):
    """创建真值表行"""
    row = VGroup()
    
    for val in values:
        cell = create_bit_cell(val, size=0.45)
        row.add(cell)
    
    result_cell = create_bit_cell(result, size=0.45)
    result_cell[0].set_stroke(result_color, width=3)
    row.add(result_cell)
    
    row.arrange(RIGHT, buff=0.6)
    return row


def create_gate_box(name, color, size=0.8):
    """创建简化的门符号盒子"""
    box = VGroup()
    
    rect = RoundedRectangle(
        corner_radius=0.05,
        width=size,
        height=size * 0.6,
        fill_color=Colors.BG,
        fill_opacity=0.9,
        stroke_color=color,
        stroke_width=2
    )
    
    label = Text(name, font_size=int(size * 15), color=color)
    label.move_to(rect.get_center())
    
    box.add(rect, label)
    return box


def create_law_card(name, formula, description, color, width=3.2, height=1.4):
    """创建定律卡片"""
    card = VGroup()
    
    bg = RoundedRectangle(
        corner_radius=0.1,
        width=width,
        height=height,
        fill_color=Colors.BG,
        fill_opacity=0.9,
        stroke_color=color,
        stroke_width=2
    )
    
    name_text = Text(name, font_size=16, color=color)
    name_text.move_to(bg.get_top() + DOWN * 0.25)
    
    formula_text = MathTex(formula, font_size=22, color=Colors.TEXT)
    formula_text.move_to(bg.get_center() + DOWN * 0.05)
    
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.move_to(bg.get_bottom() + UP * 0.25)
    
    card.add(bg, name_text, formula_text, desc_text)
    return card


def create_pyramid_layer(text, width, color, height=0.5):
    """创建金字塔层"""
    layer = VGroup()
    
    trapezoid = Polygon(
        LEFT * width/2 + UP * height/2,
        RIGHT * width/2 + UP * height/2,
        RIGHT * (width/2 - 0.3) + DOWN * height/2,
        LEFT * (width/2 - 0.3) + DOWN * height/2,
        fill_color=color,
        fill_opacity=0.3,
        stroke_color=color,
        stroke_width=2
    )
    
    label = Text(text, font_size=14, color=Colors.TEXT)
    label.move_to(trapezoid.get_center())
    
    layer.add(trapezoid, label)
    return layer


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== 主场景类 ==========
class BooleanAlgebra(Scene):
    """布尔代数：完整视频"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题（全程显示）
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # ===== Scene 1: 布尔代数引入 =====
        self.scene1_opening()
        self.scene1_switch_metaphor()
        self.scene1_definition()
        self.scene1_history()
        
        # ===== Scene 2: 三种基本运算 =====
        self.scene2_and_operation()
        self.scene2_or_operation()
        self.scene2_not_operation()
        self.scene2_summary()
        
        # ===== Scene 3: 核心定律 =====
        self.scene3_intro()
        self.scene3_basic_laws()
        self.scene3_identity_complement()
        self.scene3_demorgan()
        
        # ===== Scene 4: 三个分身实例 =====
        self.scene4_intro()
        self.scene4_set_theory()
        self.scene4_propositional_logic()
        self.scene4_z2_arithmetic()
        self.scene4_comparison()
        
        # ===== Scene 5: 布尔函数与逻辑门 =====
        self.scene5_boolean_functions()
        self.scene5_basic_gates()
        self.scene5_nand_universal()
        
        # ===== Scene 6: 二进制加法器 =====
        self.scene6_intro()
        self.scene6_half_adder()
        self.scene6_full_adder()
        self.scene6_ripple_adder()
        
        # ===== Scene 7: 总结与启示 =====
        self.scene7_knowledge_pyramid()
        self.scene7_three_insights()
        self.scene7_finale()
        
        clear_scene(self)
    
    # ========== Scene 1: 布尔代数引入 ==========
    def scene1_opening(self):
        """开场动画"""
        main_title = Text("布尔代数", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("真与假的数学", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        question = Text(
            "计算机如何用 0 和 1 理解整个世界？",
            font_size=24, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def scene1_switch_metaphor(self):
        """开关比喻"""
        section_title = Text('"开关数学"', font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # OFF 状态
        switch_off = create_switch(is_on=False, size=0.8)
        bulb_off = create_lightbulb(is_on=False, size=0.8)
        zero_bit = create_bit_display(0, size=0.7)
        false_text = Text("假 (False)", font_size=18, color=Colors.ZERO)
        
        off_group = VGroup(switch_off, bulb_off, zero_bit, false_text).arrange(RIGHT, buff=0.6)
        off_group.next_to(section_title, DOWN, buff=0.8).shift(LEFT * 0.5)
        
        off_label = Text("关 (OFF)", font_size=16, color=Colors.GRAY)
        off_label.next_to(off_group, LEFT, buff=0.3)
        
        # ON 状态
        switch_on = create_switch(is_on=True, size=0.8)
        bulb_on = create_lightbulb(is_on=True, size=0.8)
        one_bit = create_bit_display(1, size=0.7)
        true_text = Text("真 (True)", font_size=18, color=Colors.ONE)
        
        on_group = VGroup(switch_on, bulb_on, one_bit, true_text).arrange(RIGHT, buff=0.6)
        on_group.next_to(off_group, DOWN, buff=0.6)
        
        on_label = Text("开 (ON)", font_size=16, color=Colors.GRAY)
        on_label.next_to(on_group, LEFT, buff=0.3)
        
        self.play(FadeIn(off_label))
        self.play(FadeIn(switch_off), FadeIn(bulb_off), run_time=0.6)
        self.play(FadeIn(zero_bit), FadeIn(false_text), run_time=0.5)
        
        self.wait(0.5)
        
        self.play(FadeIn(on_label))
        self.play(FadeIn(switch_on), FadeIn(bulb_on), run_time=0.6)
        self.play(FadeIn(one_bit), FadeIn(true_text), run_time=0.5)
        
        equiv = VGroup(
            Text("开 = 1 = 真", font_size=20, color=Colors.ONE),
            Text("关 = 0 = 假", font_size=20, color=Colors.ZERO),
        ).arrange(DOWN, buff=0.2)
        equiv.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)
        
        box = SurroundingRectangle(equiv, color=Colors.PRIMARY, buff=0.2)
        
        self.play(FadeIn(equiv), Create(box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title),
            FadeOut(off_group), FadeOut(off_label),
            FadeOut(on_group), FadeOut(on_label),
            FadeOut(equiv), FadeOut(box),
            run_time=0.5
        )
    
    def scene1_definition(self):
        """布尔代数定义"""
        section_title = Text("什么是布尔代数？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("布尔代数是一套关于", font_size=20, color=Colors.GRAY),
            Text('"真与假"', font_size=22, color=Colors.PRIMARY),
            Text("的数学体系", font_size=20, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(definition))
        
        elements_title = Text("核心元素:", font_size=18, color=Colors.TEXT)
        elements_title.next_to(definition, DOWN, buff=0.5).align_to(definition, LEFT)
        
        elements = VGroup(
            VGroup(
                create_bit_display(0, size=0.6),
                Text(" 代表 假/关/空", font_size=16, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                create_bit_display(1, size=0.6),
                Text(" 代表 真/开/全", font_size=16, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=1.0)
        elements.next_to(elements_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(elements_title))
        self.play(FadeIn(elements))
        
        ops_title = Text("三种基本运算:", font_size=18, color=Colors.TEXT)
        ops_title.next_to(elements, DOWN, buff=0.5).align_to(elements_title, LEFT)
        
        ops = VGroup(
            VGroup(
                Text("AND (与)", font_size=16, color=Colors.AND_COLOR),
                MathTex(r"\land", font_size=24, color=Colors.AND_COLOR),
                Text('"而且"', font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("OR (或)", font_size=16, color=Colors.OR_COLOR),
                MathTex(r"\lor", font_size=24, color=Colors.OR_COLOR),
                Text('"或者"', font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("NOT (非)", font_size=16, color=Colors.NOT_COLOR),
                MathTex(r"\neg", font_size=24, color=Colors.NOT_COLOR),
                Text('"取反"', font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(RIGHT, buff=0.8)
        ops.next_to(ops_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(ops_title))
        for op in ops:
            self.play(FadeIn(op, shift=UP * 0.1), run_time=0.4)
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(elements_title), FadeOut(elements),
            FadeOut(ops_title), FadeOut(ops),
            run_time=0.5
        )
    
    def scene1_history(self):
        """历史背景"""
        section_title = Text("历史背景", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        boole_name = Text("乔治·布尔 (George Boole)", font_size=24, color=Colors.PRIMARY)
        boole_name.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(boole_name))
        
        year = Text("1854年", font_size=20, color=Colors.ONE)
        year.next_to(boole_name, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(year))
        
        book = VGroup(
            Text("发表《思维规律的研究》", font_size=18, color=Colors.GRAY),
            Text("(The Laws of Thought)", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        book.next_to(year, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(book))
        
        significance = VGroup(
            Text("首次将逻辑推理数学化", font_size=18, color=Colors.TEXT),
            Text("为现代计算机科学奠定基础", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2)
        significance.next_to(book, DOWN, buff=0.5).set_x(0)
        
        for line in significance:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.5)
        
        timeline = VGroup(
            VGroup(
                Text("1854", font_size=14, color=Colors.PRIMARY),
                Text("布尔代数诞生", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
            Text("→", font_size=20, color=Colors.GRAY),
            VGroup(
                Text("1937", font_size=14, color=Colors.PRIMARY),
                Text("香农应用于电路", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
            Text("→", font_size=20, color=Colors.GRAY),
            VGroup(
                Text("今天", font_size=14, color=Colors.PRIMARY),
                Text("数十亿晶体管", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.4)
        timeline.to_edge(DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(timeline))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(boole_name),
            FadeOut(year), FadeOut(book),
            FadeOut(significance), FadeOut(timeline),
            run_time=0.5
        )
    
    # ========== Scene 2: 三种基本运算 ==========
    def scene2_and_operation(self):
        """AND运算"""
        section_title = VGroup(
            Text("AND 运算 (与)", font_size=26, color=Colors.AND_COLOR),
            MathTex(r"\land", font_size=32, color=Colors.AND_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"而且" - 全真才真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        header = create_truth_table_header(["A", "B"], "A ∧ B", Colors.AND_COLOR)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1)
        
        self.play(FadeIn(header))
        
        and_data = [([0, 0], 0), ([0, 1], 0), ([1, 0], 0), ([1, 1], 1)]
        
        rows = VGroup()
        for values, result in and_data:
            row = create_truth_table_row(values, result, Colors.AND_COLOR)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(header, DOWN, buff=0.2)
        
        highlight = None
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
            if i == 3:
                highlight = SurroundingRectangle(row, color=Colors.AND_COLOR, buff=0.05)
                self.play(Create(highlight), run_time=0.3)
        
        analogy_title = Text("类比: 串联开关", font_size=16, color=Colors.TEXT)
        analogy_title.next_to(truth_table_title, RIGHT, buff=2.5)
        
        self.play(FadeIn(analogy_title))
        
        analogy_desc = Text("两个开关都闭合，灯才亮", font_size=14, color=Colors.GRAY)
        analogy_desc.next_to(analogy_title, DOWN, buff=0.2)
        
        self.play(FadeIn(analogy_desc))
        
        circuits = VGroup(
            Text("S1=1, S2=1 → 亮", font_size=14, color=Colors.ONE),
            Text("其他情况 → 灭", font_size=14, color=Colors.ZERO),
        ).arrange(DOWN, buff=0.2)
        circuits.next_to(analogy_desc, DOWN, buff=0.3)
        
        self.play(FadeIn(circuits))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(highlight),
            FadeOut(analogy_title), FadeOut(analogy_desc),
            FadeOut(circuits),
            run_time=0.5
        )
    
    def scene2_or_operation(self):
        """OR运算"""
        section_title = VGroup(
            Text("OR 运算 (或)", font_size=26, color=Colors.OR_COLOR),
            MathTex(r"\lor", font_size=32, color=Colors.OR_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"或者" - 有真即真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        header = create_truth_table_header(["A", "B"], "A ∨ B", Colors.OR_COLOR)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1)
        
        self.play(FadeIn(header))
        
        or_data = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 1)]
        
        rows = VGroup()
        highlights = VGroup()
        for i, (values, result) in enumerate(or_data):
            row = create_truth_table_row(values, result, Colors.OR_COLOR)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(header, DOWN, buff=0.2)
        
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
            if i > 0:
                highlight = SurroundingRectangle(row, color=Colors.OR_COLOR, buff=0.05)
                highlights.add(highlight)
                self.play(Create(highlight), run_time=0.2)
        
        analogy_title = Text("类比: 并联开关", font_size=16, color=Colors.TEXT)
        analogy_title.next_to(truth_table_title, RIGHT, buff=2.5)
        
        self.play(FadeIn(analogy_title))
        
        analogy_desc = Text("任一开关闭合，灯就亮", font_size=14, color=Colors.GRAY)
        analogy_desc.next_to(analogy_title, DOWN, buff=0.2)
        
        self.play(FadeIn(analogy_desc))
        
        circuits = VGroup(
            Text("任一S=1 → 亮", font_size=14, color=Colors.ONE),
            Text("全部S=0 → 灭", font_size=14, color=Colors.ZERO),
        ).arrange(DOWN, buff=0.2)
        circuits.next_to(analogy_desc, DOWN, buff=0.3)
        
        self.play(FadeIn(circuits))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(highlights),
            FadeOut(analogy_title), FadeOut(analogy_desc),
            FadeOut(circuits),
            run_time=0.5
        )
    
    def scene2_not_operation(self):
        """NOT运算"""
        section_title = VGroup(
            Text("NOT 运算 (非)", font_size=26, color=Colors.NOT_COLOR),
            MathTex(r"\neg", font_size=32, color=Colors.NOT_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"取反" - 真变假，假变真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        header = VGroup(
            Text("A", font_size=18, color=Colors.TEXT),
            Text("¬A", font_size=18, color=Colors.NOT_COLOR),
        ).arrange(RIGHT, buff=1.0)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1.5)
        
        self.play(FadeIn(header))
        
        not_data = [(0, 1), (1, 0)]
        
        rows = VGroup()
        for value, result in not_data:
            row = VGroup(
                create_bit_cell(value, size=0.5),
                create_bit_cell(result, size=0.5),
            ).arrange(RIGHT, buff=0.8)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.2)
        rows.next_to(header, DOWN, buff=0.2)
        
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.4)
        
        flip_title = Text("取反可视化:", font_size=16, color=Colors.TEXT)
        flip_title.next_to(truth_table_title, RIGHT, buff=2.5)
        
        self.play(FadeIn(flip_title))
        
        bit_0 = create_bit_cell(0, size=0.7)
        bit_0.next_to(flip_title, DOWN, buff=0.5)
        
        self.play(FadeIn(bit_0))
        
        arrow = MathTex(r"\xrightarrow{\neg}", font_size=24, color=Colors.NOT_COLOR)
        arrow.next_to(bit_0, RIGHT, buff=0.3)
        
        bit_1_copy = create_bit_cell(1, size=0.7)
        bit_1_copy.next_to(arrow, RIGHT, buff=0.3)
        
        self.play(FadeIn(arrow), FadeIn(bit_1_copy))
        
        arrow2 = MathTex(r"\xrightarrow{\neg}", font_size=24, color=Colors.NOT_COLOR)
        arrow2.next_to(bit_1_copy, RIGHT, buff=0.3)
        
        bit_0_result = create_bit_cell(0, size=0.7)
        bit_0_result.next_to(arrow2, RIGHT, buff=0.3)
        
        self.play(FadeIn(arrow2), FadeIn(bit_0_result))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(flip_title),
            FadeOut(bit_0), FadeOut(arrow), FadeOut(bit_1_copy),
            FadeOut(arrow2), FadeOut(bit_0_result),
            run_time=0.5
        )
    
    def scene2_summary(self):
        """运算总结"""
        section_title = Text("三种运算总结", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        cards = VGroup()
        
        and_card = VGroup(
            Text("AND (∧)", font_size=20, color=Colors.AND_COLOR),
            Text("全真才真", font_size=14, color=Colors.GRAY),
            MathTex(r"1 \land 1 = 1", font_size=18, color=Colors.TEXT),
            Text("其余为 0", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        and_box = SurroundingRectangle(and_card, color=Colors.AND_COLOR, buff=0.2)
        cards.add(VGroup(and_box, and_card))
        
        or_card = VGroup(
            Text("OR (∨)", font_size=20, color=Colors.OR_COLOR),
            Text("有真即真", font_size=14, color=Colors.GRAY),
            MathTex(r"0 \lor 0 = 0", font_size=18, color=Colors.TEXT),
            Text("其余为 1", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        or_box = SurroundingRectangle(or_card, color=Colors.OR_COLOR, buff=0.2)
        cards.add(VGroup(or_box, or_card))
        
        not_card = VGroup(
            Text("NOT (¬)", font_size=20, color=Colors.NOT_COLOR),
            Text("取反", font_size=14, color=Colors.GRAY),
            MathTex(r"\neg 0 = 1", font_size=18, color=Colors.TEXT),
            MathTex(r"\neg 1 = 0", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15)
        not_box = SurroundingRectangle(not_card, color=Colors.NOT_COLOR, buff=0.2)
        cards.add(VGroup(not_box, not_card))
        
        cards.arrange(RIGHT, buff=0.5)
        cards.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
        
        key_point = Text("所有复杂逻辑都可以用这三种运算组合而成！", font_size=18, color=Colors.PRIMARY)
        key_point.next_to(cards, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(cards), FadeOut(key_point), run_time=0.5)
    
    # ========== Scene 3: 核心定律 ==========
    def scene3_intro(self):
        """引入"""
        section_title = Text("布尔代数的核心定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = VGroup(
            Text("就像普通代数有加法、乘法的运算规则一样，", font_size=16, color=Colors.GRAY),
            Text("布尔代数也有自己的一套定律体系。", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        intro.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intro))
        
        hint = Text("这些定律是简化逻辑表达式的有力工具！", font_size=16, color=Colors.PRIMARY)
        hint.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(hint, scale=0.9))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(hint), run_time=0.5)
    
    def scene3_basic_laws(self):
        """基本定律"""
        section_title = Text("基本定律", font_size=22, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title))
        
        # 交换律
        commutative_title = Text("交换律 (Commutative)", font_size=18, color=Colors.PRIMARY)
        commutative_title.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(commutative_title))
        
        comm_formulas = VGroup(
            MathTex(r"a \lor b = b \lor a", font_size=22, color=Colors.OR_COLOR),
            MathTex(r"a \land b = b \land a", font_size=22, color=Colors.AND_COLOR),
        ).arrange(RIGHT, buff=0.8)
        comm_formulas.next_to(commutative_title, DOWN, buff=0.2)
        
        self.play(Write(comm_formulas))
        
        # 结合律
        associative_title = Text("结合律 (Associative)", font_size=18, color=Colors.PRIMARY)
        associative_title.next_to(comm_formulas, DOWN, buff=0.3).align_to(commutative_title, LEFT)
        
        self.play(FadeIn(associative_title))
        
        assoc_formulas = VGroup(
            MathTex(r"a \lor (b \lor c) = (a \lor b) \lor c", font_size=20, color=Colors.OR_COLOR),
            MathTex(r"a \land (b \land c) = (a \land b) \land c", font_size=20, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.1)
        assoc_formulas.next_to(associative_title, DOWN, buff=0.15)
        
        self.play(Write(assoc_formulas))
        
        # 分配律
        distributive_title = Text("分配律 (Distributive)", font_size=18, color=Colors.PRIMARY)
        distributive_title.next_to(assoc_formulas, DOWN, buff=0.3).align_to(commutative_title, LEFT)
        
        self.play(FadeIn(distributive_title))
        
        dist_formulas = VGroup(
            MathTex(r"a \land (b \lor c) = (a \land b) \lor (a \land c)", font_size=20, color=Colors.AND_COLOR),
            MathTex(r"a \lor (b \land c) = (a \lor b) \land (a \lor c)", font_size=20, color=Colors.OR_COLOR),
        ).arrange(DOWN, buff=0.1)
        dist_formulas.next_to(distributive_title, DOWN, buff=0.15)
        
        dist_desc = Text("注意：第二条在普通代数中不成立！", font_size=14, color=Colors.ACCENT)
        dist_desc.next_to(dist_formulas, DOWN, buff=0.1)
        
        self.play(Write(dist_formulas))
        self.play(FadeIn(dist_desc))
        
        highlight = SurroundingRectangle(dist_formulas[1], color=Colors.ACCENT, buff=0.1)
        self.play(Create(highlight), run_time=0.5)
        
        self.wait(2)
        
        all_elements = VGroup(
            section_title, commutative_title, comm_formulas,
            associative_title, assoc_formulas,
            distributive_title, dist_formulas, dist_desc, highlight
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def scene3_identity_complement(self):
        """同一律和互补律"""
        section_title = Text("特殊定律", font_size=22, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title))
        
        # 同一律
        identity_title = Text("同一律", font_size=16, color=Colors.PRIMARY)
        identity_formulas = VGroup(
            MathTex(r"a \lor 0 = a", font_size=20, color=Colors.OR_COLOR),
            MathTex(r"a \land 1 = a", font_size=20, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.1)
        left_col = VGroup(identity_title, identity_formulas).arrange(DOWN, buff=0.15)
        
        # 零一律
        zero_one_title = Text("零一律", font_size=16, color=Colors.PRIMARY)
        zero_one_formulas = VGroup(
            MathTex(r"a \lor 1 = 1", font_size=20, color=Colors.OR_COLOR),
            MathTex(r"a \land 0 = 0", font_size=20, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.1)
        middle_col = VGroup(zero_one_title, zero_one_formulas).arrange(DOWN, buff=0.15)
        
        # 互补律
        complement_title = Text("互补律", font_size=16, color=Colors.PRIMARY)
        complement_formulas = VGroup(
            MathTex(r"a \lor \neg a = 1", font_size=20, color=Colors.NOT_COLOR),
            MathTex(r"a \land \neg a = 0", font_size=20, color=Colors.NOT_COLOR),
        ).arrange(DOWN, buff=0.1)
        right_col = VGroup(complement_title, complement_formulas).arrange(DOWN, buff=0.15)
        
        all_cols = VGroup(left_col, middle_col, right_col).arrange(RIGHT, buff=0.8)
        all_cols.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(left_col, shift=UP * 0.2))
        self.play(FadeIn(middle_col, shift=UP * 0.2))
        self.play(FadeIn(right_col, shift=UP * 0.2))
        
        # 双重否定
        double_neg = VGroup(
            Text("双重否定律:", font_size=16, color=Colors.SECONDARY),
            MathTex(r"\neg(\neg a) = a", font_size=22, color=Colors.NOT_COLOR),
        ).arrange(RIGHT, buff=0.2)
        double_neg.next_to(all_cols, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(double_neg))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(all_cols), FadeOut(double_neg), run_time=0.5)
    
    def scene3_demorgan(self):
        """德摩根定律"""
        section_title = Text("德摩根定律 (De Morgan)", font_size=24, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text('"翻转"的艺术 —— 最重要的布尔代数定律之一', font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        law1 = MathTex(r"\neg(a \land b) = \neg a \lor \neg b", font_size=28, color=Colors.TEXT)
        law1_desc = Text('"非全真" = "存在假"', font_size=14, color=Colors.GRAY)
        law1_box = VGroup(law1, law1_desc).arrange(DOWN, buff=0.1)
        
        law2 = MathTex(r"\neg(a \lor b) = \neg a \land \neg b", font_size=28, color=Colors.TEXT)
        law2_desc = Text('"非存在真" = "全为假"', font_size=14, color=Colors.GRAY)
        law2_box = VGroup(law2, law2_desc).arrange(DOWN, buff=0.1)
        
        laws = VGroup(law1_box, law2_box).arrange(DOWN, buff=0.3)
        laws.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(law1), FadeIn(law1_desc))
        self.play(Write(law2), FadeIn(law2_desc))
        
        mnemonic = VGroup(
            Text("记忆口诀：", font_size=14, color=Colors.PRIMARY),
            Text("长杠变短杠，开口换方向", font_size=16, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        mnemonic.next_to(laws, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(mnemonic))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(laws), FadeOut(mnemonic), run_time=0.5)
    
    # ========== Scene 4: 三个分身实例 ==========
    def scene4_intro(self):
        """引入"""
        section_title = Text("布尔代数的三个分身", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("同一套抽象结构，在不同领域有不同的具体实现", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        
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
        preview.next_to(intro, DOWN, buff=0.5).set_x(0)
        
        for item in preview:
            self.play(FadeIn(item, scale=0.8), run_time=0.4)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(preview), run_time=0.5)
    
    def scene4_set_theory(self):
        """集合论分身"""
        section_title = Text("分身一：集合论", font_size=24, color=Colors.SET_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        mappings = VGroup(
            VGroup(
                MathTex(r"\land", font_size=22, color=Colors.AND_COLOR),
                Text("↔", font_size=16, color=Colors.GRAY),
                MathTex(r"\cap", font_size=22, color=Colors.SET_COLOR),
                Text("(交集)", font_size=12, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"\lor", font_size=22, color=Colors.OR_COLOR),
                Text("↔", font_size=16, color=Colors.GRAY),
                MathTex(r"\cup", font_size=22, color=Colors.SET_COLOR),
                Text("(并集)", font_size=12, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.15),
            VGroup(
                MathTex(r"\neg", font_size=22, color=Colors.NOT_COLOR),
                Text("↔", font_size=16, color=Colors.GRAY),
                Text("补集", font_size=16, color=Colors.SET_COLOR),
            ).arrange(RIGHT, buff=0.15),
        ).arrange(DOWN, buff=0.2)
        mappings.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for m in mappings:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.3)
        
        specials = VGroup(
            Text("0 ↔ ∅ (空集)", font_size=14, color=Colors.GRAY),
            Text("1 ↔ U (全集)", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.5)
        specials.next_to(mappings, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(specials))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(mappings), FadeOut(specials), run_time=0.5)
    
    def scene4_propositional_logic(self):
        """命题逻辑分身"""
        section_title = Text("分身二：命题逻辑", font_size=24, color=Colors.LOGIC_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        mappings = VGroup(
            Text('∧ ↔ 逻辑"且"', font_size=16, color=Colors.AND_COLOR),
            Text('∨ ↔ 逻辑"或"', font_size=16, color=Colors.OR_COLOR),
            Text('¬ ↔ 逻辑"非"', font_size=16, color=Colors.NOT_COLOR),
        ).arrange(DOWN, buff=0.2)
        mappings.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(mappings))
        
        code_title = Text("编程中:", font_size=14, color=Colors.TEXT)
        code_title.next_to(mappings, DOWN, buff=0.4).set_x(0)
        
        code = VGroup(
            Text("if (a && b) // AND", font_size=12, color=Colors.AND_COLOR),
            Text("if (a || b) // OR", font_size=12, color=Colors.OR_COLOR),
            Text("if (!a)     // NOT", font_size=12, color=Colors.NOT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code.next_to(code_title, DOWN, buff=0.2)
        
        self.play(FadeIn(code_title), FadeIn(code))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(mappings), FadeOut(code_title), FadeOut(code), run_time=0.5)
    
    def scene4_z2_arithmetic(self):
        """模2算术分身"""
        section_title = Text("分身三：模2整数算术 (ℤ₂)", font_size=24, color=Colors.Z2_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("在 {0, 1} 上的运算 —— 数字电路的数学模型", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        mappings = VGroup(
            Text("∧ ↔ 乘法 (1 × 1 = 1)", font_size=16, color=Colors.AND_COLOR),
            Text("XOR ↔ 加法 (1 + 1 = 0)", font_size=16, color=Colors.XOR_COLOR),
        ).arrange(DOWN, buff=0.2)
        mappings.next_to(intro, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(mappings))
        
        key_point = Text("关键特性: 1 + 1 = 0 (模2: 进位被丢弃)", font_size=14, color=Colors.PRIMARY)
        key_point.next_to(mappings, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(mappings), FadeOut(key_point), run_time=0.5)
    
    def scene4_comparison(self):
        """对比总结"""
        section_title = Text("三个分身的统一性", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        core_message = VGroup(
            Text("虽然表面不同，但它们遵循", font_size=16, color=Colors.TEXT),
            Text("完全相同的代数规则！", font_size=18, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        core_message.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(core_message, shift=UP * 0.2))
        
        emphasis_box = SurroundingRectangle(core_message, color=Colors.PRIMARY, buff=0.15)
        self.play(Create(emphasis_box))
        
        hint = Text("这就是抽象代数的威力 —— 一套理论，多种应用", font_size=14, color=Colors.GRAY)
        hint.next_to(emphasis_box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(hint))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(core_message), FadeOut(emphasis_box), FadeOut(hint), run_time=0.5)
    
    # ========== Scene 5: 布尔函数与逻辑门 ==========
    def scene5_boolean_functions(self):
        """布尔函数"""
        section_title = Text("布尔函数", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("定义: 输入输出都是布尔值的函数", font_size=16, color=Colors.GRAY),
            MathTex(r"f: \{0,1\}^n \rightarrow \{0,1\}", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        
        count_info = VGroup(
            Text("n 变量布尔函数数量:", font_size=14, color=Colors.TEXT),
            MathTex(r"2^{2^n}", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        count_info.next_to(definition, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(count_info))
        
        hint = Text("每种布尔函数都可以用逻辑门电路来实现！", font_size=16, color=Colors.PRIMARY)
        hint.next_to(count_info, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(hint, shift=UP * 0.1))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(count_info), FadeOut(hint), run_time=0.5)
    
    def scene5_basic_gates(self):
        """基本逻辑门"""
        section_title = Text("基本逻辑门", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("逻辑门是实现布尔运算的电子电路", font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        gates = VGroup()
        
        and_group = VGroup(
            create_gate_box("AND", Colors.AND_COLOR, size=0.7),
            Text("全1出1", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        or_group = VGroup(
            create_gate_box("OR", Colors.OR_COLOR, size=0.7),
            Text("有1出1", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        not_group = VGroup(
            create_gate_box("NOT", Colors.NOT_COLOR, size=0.7),
            Text("取反", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        xor_group = VGroup(
            create_gate_box("XOR", Colors.XOR_COLOR, size=0.7),
            Text("不同出1", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        gates.add(and_group, or_group, not_group, xor_group)
        gates.arrange(RIGHT, buff=0.6)
        gates.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        for gate in gates:
            self.play(FadeIn(gate, shift=UP * 0.2), run_time=0.4)
        
        key_info = Text("任何布尔函数都可以用这些门组合实现", font_size=14, color=Colors.PRIMARY)
        key_info.next_to(gates, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_info))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(gates), FadeOut(key_info), run_time=0.5)
    
    def scene5_nand_universal(self):
        """NAND门万能性"""
        section_title = Text("NAND门的万能性", font_size=24, color=Colors.NAND_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        core_info = Text("只用NAND门就能构建所有其他逻辑门！", font_size=18, color=Colors.PRIMARY)
        core_info.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(core_info))
        
        constructions = VGroup(
            VGroup(
                Text("NOT:", font_size=14, color=Colors.NOT_COLOR),
                MathTex(r"\neg A = A \uparrow A", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("AND:", font_size=14, color=Colors.AND_COLOR),
                MathTex(r"A \land B = (A \uparrow B) \uparrow (A \uparrow B)", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("OR:", font_size=14, color=Colors.OR_COLOR),
                MathTex(r"A \lor B = (A \uparrow A) \uparrow (B \uparrow B)", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.2)
        constructions.next_to(core_info, DOWN, buff=0.4).set_x(0)
        
        for c in constructions:
            self.play(FadeIn(c), run_time=0.4)
        
        emphasis = Text('"一种门统治一切"', font_size=18, color=Colors.SECONDARY)
        emphasis.next_to(constructions, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(emphasis, scale=0.9))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(core_info), FadeOut(constructions), FadeOut(emphasis), run_time=0.5)
    
    # ========== Scene 6: 二进制加法器 ==========
    def scene6_intro(self):
        """引入"""
        section_title = Text("从逻辑到计算", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        question = Text("核心问题：如何用逻辑门实现加法？", font_size=18, color=Colors.PRIMARY)
        question.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(question))
        
        observation = VGroup(
            Text("观察一位二进制加法:", font_size=14, color=Colors.TEXT),
            Text("• Sum = A XOR B", font_size=14, color=Colors.SUM),
            Text("• Carry = A AND B", font_size=14, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        observation.next_to(question, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(observation))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(question), FadeOut(observation), run_time=0.5)
    
    def scene6_half_adder(self):
        """半加器"""
        section_title = Text("半加器 (Half Adder)", font_size=24, color=Colors.SUM)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("功能: 计算两个1位二进制数的和", font_size=14, color=Colors.GRAY),
            Text("输入: A, B", font_size=14, color=Colors.PRIMARY),
            Text("输出: Sum (S), Carry (C)", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).shift(LEFT * 1.5)
        
        self.play(FadeIn(definition))
        
        formulas = VGroup(
            MathTex(r"S = A \oplus B", font_size=22, color=Colors.SUM),
            MathTex(r"C = A \land B", font_size=22, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.15)
        formulas.next_to(definition, DOWN, buff=0.3)
        
        self.play(FadeIn(formulas))
        
        # 简化电路图
        circuit = VGroup(
            Text("A, B", font_size=12, color=Colors.PRIMARY),
            Text("→", font_size=14, color=Colors.GRAY),
            create_gate_box("XOR", Colors.XOR_COLOR, size=0.5),
            Text("→ S", font_size=12, color=Colors.SUM),
        ).arrange(RIGHT, buff=0.2)
        
        circuit2 = VGroup(
            Text("A, B", font_size=12, color=Colors.PRIMARY),
            Text("→", font_size=14, color=Colors.GRAY),
            create_gate_box("AND", Colors.AND_COLOR, size=0.5),
            Text("→ C", font_size=12, color=Colors.CARRY),
        ).arrange(RIGHT, buff=0.2)
        
        circuits = VGroup(circuit, circuit2).arrange(DOWN, buff=0.2)
        circuits.next_to(definition, RIGHT, buff=0.8)
        
        self.play(FadeIn(circuits))
        
        limitation = Text("局限性: 没有进位输入，无法级联", font_size=14, color=Colors.ACCENT)
        limitation.next_to(formulas, DOWN, buff=0.3)
        
        self.play(FadeIn(limitation))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(formulas), FadeOut(circuits), FadeOut(limitation), run_time=0.5)
    
    def scene6_full_adder(self):
        """全加器"""
        section_title = Text("全加器 (Full Adder)", font_size=24, color=Colors.CARRY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = VGroup(
            Text("功能: 计算两个1位二进制数和进位的和", font_size=14, color=Colors.GRAY),
            Text("输入: A, B, Cin (进位输入)", font_size=14, color=Colors.PRIMARY),
            Text("输出: Sum, Cout (进位输出)", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).shift(LEFT * 1.5)
        
        self.play(FadeIn(definition))
        
        formulas = VGroup(
            MathTex(r"S = A \oplus B \oplus C_{in}", font_size=20, color=Colors.SUM),
            MathTex(r"C_{out} = (A \land B) \lor (C_{in} \land (A \oplus B))", font_size=16, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.1)
        formulas.next_to(definition, DOWN, buff=0.3)
        
        self.play(Write(formulas))
        
        structure = Text("结构: 两个半加器 + 一个OR门", font_size=14, color=Colors.TEXT)
        structure.next_to(formulas, DOWN, buff=0.3)
        
        self.play(FadeIn(structure))
        
        key_point = Text("关键优势: 有进位输入 → 可以级联！", font_size=16, color=Colors.PRIMARY)
        key_point.next_to(structure, DOWN, buff=0.3)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(formulas), FadeOut(structure), FadeOut(key_point), run_time=0.5)
    
    def scene6_ripple_adder(self):
        """行波加法器"""
        section_title = Text("多位加法器", font_size=24, color=Colors.PRIMARY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        principle = Text("将多个全加器级联，进位依次传递", font_size=16, color=Colors.GRAY)
        principle.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(principle))
        
        # 4个全加器
        fas = VGroup()
        for i in range(4):
            fa = VGroup()
            fa_box = RoundedRectangle(width=0.8, height=0.6, corner_radius=0.08,
                                       stroke_color=Colors.SUM, stroke_width=2)
            fa_label = Text(f"FA{i}", font_size=10, color=Colors.SUM)
            fa_label.move_to(fa_box.get_center())
            fa.add(fa_box, fa_label)
            fas.add(fa)
        
        fas.arrange(RIGHT, buff=0.3)
        fas.next_to(principle, DOWN, buff=0.4).set_x(0)
        
        # 进位箭头
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                fas[i].get_right() + RIGHT * 0.02,
                fas[i+1].get_left() + LEFT * 0.02,
                buff=0.02, stroke_width=2, color=Colors.CARRY, max_tip_length_to_length_ratio=0.3
            )
            arrows.add(arrow)
        
        adder_circuit = VGroup(fas, arrows)
        
        self.play(FadeIn(adder_circuit))
        
        # 计算示例
        calc = VGroup(
            Text("0101 + 0011 = 1000", font_size=14, color=Colors.TEXT),
            Text("(5 + 3 = 8)", font_size=12, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.2)
        calc.next_to(adder_circuit, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(calc))
        
        insight = VGroup(
            Text("从布尔代数到加法器：", font_size=14, color=Colors.PRIMARY),
            Text("数学抽象 → 逻辑门 → 电子电路 → 计算能力", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        insight.next_to(calc, DOWN, buff=0.4).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(principle), FadeOut(adder_circuit), FadeOut(calc), FadeOut(insight), FadeOut(insight_box), run_time=0.5)
    
    # ========== Scene 7: 总结与启示 ==========
    def scene7_knowledge_pyramid(self):
        """知识体系金字塔"""
        section_title = Text("知识体系回顾", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        layers_data = [
            ("晶体管 (物理基础)", 3.5, Colors.ZERO),
            ("逻辑门 (电路实现)", 3.0, Colors.AND_COLOR),
            ("布尔函数 (逻辑设计)", 2.5, Colors.OR_COLOR),
            ("布尔代数 (抽象数学)", 2.0, Colors.PRIMARY),
        ]
        
        layers = VGroup()
        for text, width, color in layers_data:
            layer = create_pyramid_layer(text, width, color, height=0.6)
            layers.add(layer)
        
        layers.arrange(UP, buff=0.05)
        layers.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for layer in layers:
            self.play(FadeIn(layer, shift=UP * 0.2), run_time=0.4)
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(layers), run_time=0.5)
    
    def scene7_three_insights(self):
        """三个核心启示"""
        section_title = Text("三个核心启示", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        cards = VGroup()
        
        card1 = VGroup(
            RoundedRectangle(width=2.8, height=1.6, corner_radius=0.1,
                            stroke_color=Colors.PRIMARY, stroke_width=2),
            Text("抽象与现实的桥梁", font_size=13, color=Colors.PRIMARY),
            Text("数学概念 → 电子电路", font_size=11, color=Colors.GRAY),
        )
        card1[1].move_to(card1[0].get_top() + DOWN * 0.3)
        card1[2].move_to(card1[0].get_center() + DOWN * 0.1)
        
        card2 = VGroup(
            RoundedRectangle(width=2.8, height=1.6, corner_radius=0.1,
                            stroke_color=Colors.SECONDARY, stroke_width=2),
            Text("计算机的逻辑基石", font_size=13, color=Colors.SECONDARY),
            Text("0和1的组合运算", font_size=11, color=Colors.GRAY),
        )
        card2[1].move_to(card2[0].get_top() + DOWN * 0.3)
        card2[2].move_to(card2[0].get_center() + DOWN * 0.1)
        
        card3 = VGroup(
            RoundedRectangle(width=2.8, height=1.6, corner_radius=0.1,
                            stroke_color=Colors.XOR_COLOR, stroke_width=2),
            Text("简化与优化的艺术", font_size=13, color=Colors.XOR_COLOR),
            Text("用定律简化逻辑", font_size=11, color=Colors.GRAY),
        )
        card3[1].move_to(card3[0].get_top() + DOWN * 0.3)
        card3[2].move_to(card3[0].get_center() + DOWN * 0.1)
        
        cards.add(card1, card2, card3)
        cards.arrange(RIGHT, buff=0.3)
        cards.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(cards), run_time=0.5)
    
    def scene7_finale(self):
        """升华与结语"""
        quote = VGroup(
            Text("0 和 1", font_size=40, color=Colors.ONE),
            Text("点亮数字世界", font_size=32, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.3)
        quote.move_to(ORIGIN + UP * 0.5)
        
        self.play(FadeIn(quote, scale=0.8))
        self.wait(1)
        
        recap = VGroup(
            Text("本章要点回顾:", font_size=16, color=Colors.TEXT),
            Text("✓ 布尔代数: 真与假的数学体系", font_size=14, color=Colors.GRAY),
            Text("✓ 三种运算: AND, OR, NOT", font_size=14, color=Colors.GRAY),
            Text("✓ 核心定律: 交换、结合、分配、德摩根", font_size=14, color=Colors.GRAY),
            Text("✓ 逻辑门: 布尔运算的电路实现", font_size=14, color=Colors.GRAY),
            Text("✓ 加法器: 从逻辑到计算的桥梁", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        recap.next_to(quote, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(recap, shift=UP * 0.2))
        self.wait(1)
        
        thanks = Text("感谢观看！", font_size=28, color=Colors.SECONDARY)
        thanks.next_to(recap, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(thanks, scale=0.8))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染完整视频: manim -pqh all_scenes.py BooleanAlgebra
    # 预览版本: manim -pql all_scenes.py BooleanAlgebra
    pass
