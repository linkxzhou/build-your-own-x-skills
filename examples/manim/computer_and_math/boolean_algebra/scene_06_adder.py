"""
Scene 6: 二进制加法器
终极应用案例，展示如何用逻辑门构建加法器
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
    CARRY = "#FF9800"        # 进位颜色
    SUM = "#00BCD4"          # 和颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_bit_cell(value, size=0.4):
    """创建一个比特单元格"""
    color = Colors.ONE if value == 1 else Colors.ZERO
    
    rect = Square(side_length=size)
    rect.set_fill(color, opacity=0.8)
    rect.set_stroke(Colors.PRIMARY, width=2)
    
    text = Text(str(value), font_size=int(size * 40), color=Colors.TEXT)
    text.move_to(rect.get_center())
    
    return VGroup(rect, text)


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


def create_half_adder_circuit(size=1.0):
    """创建半加器电路图"""
    circuit = VGroup()
    
    # 输入标签
    input_a = Text("A", font_size=14, color=Colors.PRIMARY)
    input_b = Text("B", font_size=14, color=Colors.PRIMARY)
    
    # XOR门 (计算Sum)
    xor_gate = create_gate_box("XOR", Colors.XOR_COLOR, size=0.7)
    
    # AND门 (计算Carry)
    and_gate = create_gate_box("AND", Colors.AND_COLOR, size=0.7)
    
    # 输出标签
    output_s = Text("S", font_size=14, color=Colors.SUM)
    output_c = Text("C", font_size=14, color=Colors.CARRY)
    
    # 布局
    input_a.move_to(LEFT * 2 * size + UP * 0.5 * size)
    input_b.move_to(LEFT * 2 * size + DOWN * 0.5 * size)
    
    xor_gate.move_to(UP * 0.3 * size)
    and_gate.move_to(DOWN * 0.5 * size)
    
    output_s.move_to(RIGHT * 2 * size + UP * 0.3 * size)
    output_c.move_to(RIGHT * 2 * size + DOWN * 0.5 * size)
    
    # 连线
    # A到XOR
    line_a_xor = Line(
        input_a.get_right() + RIGHT * 0.1,
        xor_gate.get_left() + UP * 0.1,
        color=Colors.PRIMARY, stroke_width=2
    )
    # A到AND (分支)
    line_a_and = VGroup(
        Line(input_a.get_right() + RIGHT * 0.1, 
             input_a.get_right() + RIGHT * 0.3,
             color=Colors.PRIMARY, stroke_width=2),
        Line(input_a.get_right() + RIGHT * 0.3,
             input_a.get_right() + RIGHT * 0.3 + DOWN * 0.85,
             color=Colors.PRIMARY, stroke_width=2),
        Line(input_a.get_right() + RIGHT * 0.3 + DOWN * 0.85,
             and_gate.get_left() + UP * 0.08,
             color=Colors.PRIMARY, stroke_width=2),
    )
    
    # B到XOR
    line_b_xor = VGroup(
        Line(input_b.get_right() + RIGHT * 0.1,
             input_b.get_right() + RIGHT * 0.5,
             color=Colors.PRIMARY, stroke_width=2),
        Line(input_b.get_right() + RIGHT * 0.5,
             input_b.get_right() + RIGHT * 0.5 + UP * 0.65,
             color=Colors.PRIMARY, stroke_width=2),
        Line(input_b.get_right() + RIGHT * 0.5 + UP * 0.65,
             xor_gate.get_left() + DOWN * 0.1,
             color=Colors.PRIMARY, stroke_width=2),
    )
    # B到AND
    line_b_and = Line(
        input_b.get_right() + RIGHT * 0.1,
        and_gate.get_left() + DOWN * 0.08,
        color=Colors.PRIMARY, stroke_width=2
    )
    
    # XOR到S
    line_xor_s = Line(
        xor_gate.get_right(),
        output_s.get_left() + LEFT * 0.1,
        color=Colors.SUM, stroke_width=2
    )
    
    # AND到C
    line_and_c = Line(
        and_gate.get_right(),
        output_c.get_left() + LEFT * 0.1,
        color=Colors.CARRY, stroke_width=2
    )
    
    circuit.add(
        input_a, input_b, xor_gate, and_gate, output_s, output_c,
        line_a_xor, line_a_and, line_b_xor, line_b_and,
        line_xor_s, line_and_c
    )
    
    return circuit


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene06Adder(Scene):
    """Scene 6: 二进制加法器"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_intro()
        self.section_half_adder()
        self.section_full_adder()
        self.section_ripple_adder()
        
        clear_scene(self)
    
    def section_intro(self):
        """引入：从逻辑到计算"""
        section_title = Text("从逻辑到计算", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题引入
        question = VGroup(
            Text("核心问题：如何用逻辑门实现加法？", font_size=18, color=Colors.PRIMARY),
        )
        question.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(question))
        self.wait(0.5)
        
        # 一位二进制加法
        example_title = Text("一位二进制加法真值表：", font_size=16, color=Colors.TEXT)
        example_title.next_to(question, DOWN, buff=0.5).align_to(question, LEFT).shift(LEFT * 1)
        
        self.play(FadeIn(example_title))
        
        # 真值表
        table_header = VGroup(
            Text("A", font_size=14, color=Colors.PRIMARY),
            Text("B", font_size=14, color=Colors.PRIMARY),
            Text("Sum", font_size=14, color=Colors.SUM),
            Text("Carry", font_size=14, color=Colors.CARRY),
        ).arrange(RIGHT, buff=0.5)
        table_header.next_to(example_title, DOWN, buff=0.2)
        
        self.play(FadeIn(table_header))
        
        # 数据行
        table_data = [
            (0, 0, 0, 0),
            (0, 1, 1, 0),
            (1, 0, 1, 0),
            (1, 1, 0, 1),  # 关键行：1+1=10
        ]
        
        rows = VGroup()
        for a, b, s, c in table_data:
            row = VGroup(
                create_bit_cell(a, size=0.35),
                create_bit_cell(b, size=0.35),
                create_bit_cell(s, size=0.35),
                create_bit_cell(c, size=0.35),
            ).arrange(RIGHT, buff=0.4)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.1)
        rows.next_to(table_header, DOWN, buff=0.15)
        
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.3)
        
        # 高亮最后一行
        highlight = SurroundingRectangle(rows[3], color=Colors.ACCENT, buff=0.05)
        note = Text("1+1=10 (二进制)", font_size=12, color=Colors.ACCENT)
        note.next_to(highlight, RIGHT, buff=0.2)
        
        self.play(Create(highlight), FadeIn(note))
        
        # 观察
        observation = VGroup(
            Text("观察：", font_size=14, color=Colors.TEXT),
            Text("• Sum = A XOR B", font_size=14, color=Colors.SUM),
            Text("• Carry = A AND B", font_size=14, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        observation.next_to(table_header, RIGHT, buff=1.2)
        
        self.play(FadeIn(observation))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, question, example_title, table_header,
            rows, highlight, note, observation
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_half_adder(self):
        """半加器"""
        section_title = Text("半加器 (Half Adder)", font_size=24, color=Colors.SUM)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("功能: 计算两个1位二进制数的和", font_size=14, color=Colors.GRAY),
            Text("输入: A, B", font_size=14, color=Colors.PRIMARY),
            Text("输出: Sum (S), Carry (C)", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(definition))
        
        # 公式
        formulas_title = Text("逻辑公式:", font_size=14, color=Colors.TEXT)
        formulas_title.next_to(definition, DOWN, buff=0.3).align_to(definition, LEFT)
        
        formulas = VGroup(
            MathTex(r"S = A \oplus B", font_size=22, color=Colors.SUM),
            MathTex(r"C = A \land B", font_size=22, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.15)
        formulas.next_to(formulas_title, DOWN, buff=0.15)
        
        self.play(FadeIn(formulas_title), FadeIn(formulas))
        
        # 电路图示意
        circuit_title = Text("电路结构:", font_size=14, color=Colors.TEXT)
        circuit_title.next_to(definition, RIGHT, buff=1.5)
        
        self.play(FadeIn(circuit_title))
        
        # 简化的电路图
        circuit = VGroup()
        
        # 输入
        in_a = Text("A", font_size=12, color=Colors.PRIMARY)
        in_b = Text("B", font_size=12, color=Colors.PRIMARY)
        in_a.move_to(LEFT * 1.5 + UP * 0.3)
        in_b.move_to(LEFT * 1.5 + DOWN * 0.3)
        
        # XOR门
        xor_box = create_gate_box("XOR", Colors.XOR_COLOR, size=0.6)
        xor_box.move_to(UP * 0.3)
        
        # AND门
        and_box = create_gate_box("AND", Colors.AND_COLOR, size=0.6)
        and_box.move_to(DOWN * 0.3)
        
        # 输出
        out_s = Text("S (Sum)", font_size=12, color=Colors.SUM)
        out_c = Text("C (Carry)", font_size=12, color=Colors.CARRY)
        out_s.move_to(RIGHT * 1.5 + UP * 0.3)
        out_c.move_to(RIGHT * 1.5 + DOWN * 0.3)
        
        # 连线
        lines = VGroup(
            Arrow(in_a.get_right(), xor_box.get_left() + UP * 0.05, 
                  buff=0.1, stroke_width=2, color=Colors.PRIMARY),
            Arrow(in_a.get_right() + RIGHT * 0.15, and_box.get_left() + UP * 0.05,
                  buff=0.1, stroke_width=2, color=Colors.PRIMARY),
            Arrow(in_b.get_right(), and_box.get_left() + DOWN * 0.05,
                  buff=0.1, stroke_width=2, color=Colors.PRIMARY),
            Arrow(in_b.get_right() + RIGHT * 0.15, xor_box.get_left() + DOWN * 0.05,
                  buff=0.1, stroke_width=2, color=Colors.PRIMARY),
            Arrow(xor_box.get_right(), out_s.get_left(),
                  buff=0.1, stroke_width=2, color=Colors.SUM),
            Arrow(and_box.get_right(), out_c.get_left(),
                  buff=0.1, stroke_width=2, color=Colors.CARRY),
        )
        
        circuit.add(in_a, in_b, xor_box, and_box, out_s, out_c, lines)
        circuit.next_to(circuit_title, DOWN, buff=0.3)
        
        self.play(FadeIn(circuit))
        
        # 局限性
        limitation = VGroup(
            Text("局限性:", font_size=14, color=Colors.ACCENT),
            Text("没有进位输入，无法级联", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        limitation.next_to(formulas, DOWN, buff=0.4).align_to(formulas, LEFT)
        
        self.play(FadeIn(limitation))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, definition, formulas_title, formulas,
            circuit_title, circuit, limitation
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_full_adder(self):
        """全加器"""
        section_title = Text("全加器 (Full Adder)", font_size=24, color=Colors.CARRY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("功能: 计算两个1位二进制数和进位的和", font_size=14, color=Colors.GRAY),
            Text("输入: A, B, Cin (进位输入)", font_size=14, color=Colors.PRIMARY),
            Text("输出: Sum, Cout (进位输出)", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(definition))
        
        # 公式
        formulas_title = Text("逻辑公式:", font_size=14, color=Colors.TEXT)
        formulas_title.next_to(definition, DOWN, buff=0.3).align_to(definition, LEFT)
        
        formulas = VGroup(
            MathTex(r"S = A \oplus B \oplus C_{in}", font_size=20, color=Colors.SUM),
            MathTex(r"C_{out} = (A \land B) \lor (C_{in} \land (A \oplus B))", 
                    font_size=18, color=Colors.CARRY),
        ).arrange(DOWN, buff=0.15)
        formulas.next_to(formulas_title, DOWN, buff=0.15)
        
        self.play(FadeIn(formulas_title), Write(formulas))
        
        # 结构说明
        structure_title = Text("结构: 两个半加器 + 一个OR门", font_size=14, color=Colors.TEXT)
        structure_title.next_to(formulas, DOWN, buff=0.4).align_to(formulas_title, LEFT)
        
        self.play(FadeIn(structure_title))
        
        # 简化框图
        block_diagram = VGroup()
        
        # 第一个半加器
        ha1 = VGroup()
        ha1_box = RoundedRectangle(width=1.0, height=0.6, corner_radius=0.1,
                                    stroke_color=Colors.SUM, stroke_width=2)
        ha1_label = Text("HA1", font_size=12, color=Colors.SUM)
        ha1_label.move_to(ha1_box.get_center())
        ha1.add(ha1_box, ha1_label)
        
        # 第二个半加器
        ha2 = VGroup()
        ha2_box = RoundedRectangle(width=1.0, height=0.6, corner_radius=0.1,
                                    stroke_color=Colors.SUM, stroke_width=2)
        ha2_label = Text("HA2", font_size=12, color=Colors.SUM)
        ha2_label.move_to(ha2_box.get_center())
        ha2.add(ha2_box, ha2_label)
        
        # OR门
        or_gate = VGroup()
        or_box = RoundedRectangle(width=0.8, height=0.5, corner_radius=0.1,
                                   stroke_color=Colors.OR_COLOR, stroke_width=2)
        or_label = Text("OR", font_size=12, color=Colors.OR_COLOR)
        or_label.move_to(or_box.get_center())
        or_gate.add(or_box, or_label)
        
        # 布局
        ha1.move_to(LEFT * 1.2 + UP * 0.3)
        ha2.move_to(RIGHT * 0.3)
        or_gate.move_to(RIGHT * 0.3 + DOWN * 0.7)
        
        # 标签
        in_a = Text("A", font_size=10, color=Colors.PRIMARY)
        in_b = Text("B", font_size=10, color=Colors.PRIMARY)
        in_cin = Text("Cin", font_size=10, color=Colors.CARRY)
        out_s = Text("S", font_size=10, color=Colors.SUM)
        out_cout = Text("Cout", font_size=10, color=Colors.CARRY)
        
        in_a.next_to(ha1, LEFT, buff=0.3).shift(UP * 0.1)
        in_b.next_to(ha1, LEFT, buff=0.3).shift(DOWN * 0.1)
        in_cin.next_to(ha2, LEFT, buff=0.5).shift(UP * 0.4)
        out_s.next_to(ha2, RIGHT, buff=0.3)
        out_cout.next_to(or_gate, RIGHT, buff=0.3)
        
        block_diagram.add(ha1, ha2, or_gate, in_a, in_b, in_cin, out_s, out_cout)
        block_diagram.next_to(structure_title, RIGHT, buff=0.8)
        
        self.play(FadeIn(block_diagram))
        
        # 关键点
        key_point = VGroup(
            Text("关键优势:", font_size=14, color=Colors.PRIMARY),
            Text("有进位输入 → 可以级联！", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        key_point.next_to(structure_title, DOWN, buff=0.5).align_to(structure_title, LEFT)
        
        self.play(FadeIn(key_point))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, definition, formulas_title, formulas,
            structure_title, block_diagram, key_point
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_ripple_adder(self):
        """行波加法器（多位加法器）"""
        section_title = Text("多位加法器", font_size=24, color=Colors.PRIMARY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 原理
        principle = Text("将多个全加器级联，进位依次传递", font_size=16, color=Colors.GRAY)
        principle.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(principle))
        
        # 4位加法器示意
        adder_title = Text("4位行波加法器:", font_size=16, color=Colors.TEXT)
        adder_title.next_to(principle, DOWN, buff=0.4).align_to(principle, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(adder_title))
        
        # 创建4个全加器
        fas = VGroup()
        for i in range(4):
            fa = VGroup()
            fa_box = RoundedRectangle(width=0.9, height=0.7, corner_radius=0.08,
                                       stroke_color=Colors.SUM, stroke_width=2)
            fa_label = Text(f"FA{i}", font_size=11, color=Colors.SUM)
            fa_label.move_to(fa_box.get_center())
            fa.add(fa_box, fa_label)
            fas.add(fa)
        
        fas.arrange(RIGHT, buff=0.4)
        fas.next_to(adder_title, DOWN, buff=0.4).set_x(0)
        
        # 输入标签
        a_labels = VGroup()
        b_labels = VGroup()
        s_labels = VGroup()
        
        for i, fa in enumerate(fas):
            a_label = Text(f"A{i}", font_size=9, color=Colors.PRIMARY)
            a_label.next_to(fa, UP, buff=0.15).shift(LEFT * 0.15)
            a_labels.add(a_label)
            
            b_label = Text(f"B{i}", font_size=9, color=Colors.PRIMARY)
            b_label.next_to(fa, UP, buff=0.15).shift(RIGHT * 0.15)
            b_labels.add(b_label)
            
            s_label = Text(f"S{i}", font_size=9, color=Colors.SUM)
            s_label.next_to(fa, DOWN, buff=0.15)
            s_labels.add(s_label)
        
        # 进位连接箭头
        carry_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                fas[i].get_right() + RIGHT * 0.05,
                fas[i+1].get_left() + LEFT * 0.05,
                buff=0.05, stroke_width=2, color=Colors.CARRY, max_tip_length_to_length_ratio=0.2
            )
            carry_arrows.add(arrow)
        
        # C0输入
        c0_label = Text("0", font_size=10, color=Colors.CARRY)
        c0_label.next_to(fas[0], LEFT, buff=0.3)
        c0_arrow = Arrow(c0_label.get_right(), fas[0].get_left(), 
                         buff=0.05, stroke_width=2, color=Colors.CARRY, max_tip_length_to_length_ratio=0.3)
        
        # C4输出
        c4_label = Text("C4", font_size=10, color=Colors.CARRY)
        c4_label.next_to(fas[3], RIGHT, buff=0.3)
        c4_arrow = Arrow(fas[3].get_right(), c4_label.get_left(),
                         buff=0.05, stroke_width=2, color=Colors.CARRY, max_tip_length_to_length_ratio=0.3)
        
        adder_circuit = VGroup(
            fas, a_labels, b_labels, s_labels,
            carry_arrows, c0_label, c0_arrow, c4_label, c4_arrow
        )
        
        self.play(FadeIn(adder_circuit))
        
        self.wait(1)
        
        # 计算示例
        example_title = Text("计算示例:", font_size=14, color=Colors.TEXT)
        example_title.next_to(adder_circuit, DOWN, buff=0.5).align_to(adder_title, LEFT)
        
        self.play(FadeIn(example_title))
        
        # 0101 + 0011 = 1000
        calc = VGroup(
            VGroup(
                Text("A =", font_size=12, color=Colors.PRIMARY),
                Text("0101", font_size=14, color=Colors.PRIMARY),
                Text("(5)", font_size=10, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("B =", font_size=12, color=Colors.PRIMARY),
                Text("0011", font_size=14, color=Colors.PRIMARY),
                Text("(3)", font_size=10, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("S =", font_size=12, color=Colors.SUM),
                Text("1000", font_size=14, color=Colors.SUM),
                Text("(8)", font_size=10, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        calc.next_to(example_title, RIGHT, buff=0.3)
        
        self.play(FadeIn(calc))
        
        # 进位传播说明
        carry_note = VGroup(
            Text("进位传播:", font_size=12, color=Colors.CARRY),
            MathTex(r"0 \rightarrow 1 \rightarrow 1 \rightarrow 1 \rightarrow 0", 
                    font_size=16, color=Colors.CARRY),
        ).arrange(RIGHT, buff=0.2)
        carry_note.next_to(calc, DOWN, buff=0.25)
        
        self.play(FadeIn(carry_note))
        
        # 升华
        insight = VGroup(
            Text("从布尔代数到加法器：", font_size=14, color=Colors.PRIMARY),
            Text("数学抽象 → 逻辑门 → 电子电路 → 计算能力", font_size=14, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        insight.next_to(carry_note, DOWN, buff=0.4).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(insight), Create(insight_box))
        
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_06_adder.py Scene06Adder
    pass
