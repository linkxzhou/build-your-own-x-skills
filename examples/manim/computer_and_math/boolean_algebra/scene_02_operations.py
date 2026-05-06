"""
Scene 2: 三种基本运算
详细介绍AND、OR、NOT三种基本运算
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


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_bit_cell(value, size=0.5):
    """创建一个比特单元格"""
    color = Colors.ONE if value == 1 else Colors.ZERO
    
    rect = Square(side_length=size)
    rect.set_fill(color, opacity=0.8)
    rect.set_stroke(Colors.PRIMARY, width=2)
    
    text = Text(str(value), font_size=int(size * 35), color=Colors.TEXT)
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


def create_switch_circuit(switch_states, is_series=True, size=0.6):
    """创建开关电路图 - 串联或并联"""
    circuit = VGroup()
    
    # 电池
    battery = VGroup(
        Line(LEFT * 0.15, RIGHT * 0.15, color=Colors.PRIMARY, stroke_width=3),
        Line(LEFT * 0.08 + DOWN * 0.1, RIGHT * 0.08 + DOWN * 0.1, color=Colors.PRIMARY, stroke_width=3),
    )
    battery.scale(size)
    
    # 灯泡
    bulb = Circle(radius=size * 0.2)
    all_on = all(switch_states) if is_series else any(switch_states)
    bulb.set_stroke(Colors.PRIMARY, width=2)
    bulb.set_fill(Colors.ONE if all_on else Colors.ZERO, opacity=0.8)
    
    if is_series:
        # 串联电路
        switches = VGroup()
        for i, state in enumerate(switch_states):
            sw = VGroup()
            # 开关两端
            left_dot = Dot(color=Colors.PRIMARY, radius=size * 0.05)
            right_dot = Dot(color=Colors.PRIMARY, radius=size * 0.05)
            right_dot.next_to(left_dot, RIGHT, buff=size * 0.4)
            
            # 开关臂
            if state:
                arm = Line(left_dot.get_center(), right_dot.get_center(), 
                          color=Colors.ONE, stroke_width=3)
            else:
                arm = Line(left_dot.get_center(), 
                          right_dot.get_center() + UP * size * 0.2,
                          color=Colors.ZERO, stroke_width=3)
            
            sw.add(left_dot, right_dot, arm)
            
            label = Text(f"S{i+1}", font_size=int(size * 20), color=Colors.GRAY)
            label.next_to(sw, DOWN, buff=size * 0.1)
            sw.add(label)
            
            switches.add(sw)
        
        switches.arrange(RIGHT, buff=size * 0.3)
        
        # 连接线
        battery.next_to(switches, LEFT, buff=size * 0.3)
        bulb.next_to(switches, RIGHT, buff=size * 0.3)
        
        # 导线
        wire1 = Line(battery.get_right(), switches.get_left(), color=Colors.PRIMARY, stroke_width=2)
        wire2 = Line(switches.get_right(), bulb.get_left(), color=Colors.PRIMARY, stroke_width=2)
        
        circuit.add(battery, wire1, switches, wire2, bulb)
    else:
        # 并联电路
        switches = VGroup()
        for i, state in enumerate(switch_states):
            sw = VGroup()
            left_dot = Dot(color=Colors.PRIMARY, radius=size * 0.05)
            right_dot = Dot(color=Colors.PRIMARY, radius=size * 0.05)
            right_dot.next_to(left_dot, RIGHT, buff=size * 0.4)
            
            if state:
                arm = Line(left_dot.get_center(), right_dot.get_center(),
                          color=Colors.ONE, stroke_width=3)
            else:
                arm = Line(left_dot.get_center(),
                          right_dot.get_center() + UP * size * 0.15,
                          color=Colors.ZERO, stroke_width=3)
            
            sw.add(left_dot, right_dot, arm)
            
            label = Text(f"S{i+1}", font_size=int(size * 18), color=Colors.GRAY)
            label.next_to(sw, RIGHT, buff=size * 0.1)
            sw.add(label)
            
            switches.add(sw)
        
        switches.arrange(DOWN, buff=size * 0.2)
        
        battery.next_to(switches, LEFT, buff=size * 0.5)
        bulb.next_to(switches, RIGHT, buff=size * 0.5)
        
        circuit.add(battery, switches, bulb)
    
    return circuit


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene02Operations(Scene):
    """Scene 2: 三种基本运算"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_and_operation()
        self.section_or_operation()
        self.section_not_operation()
        self.section_summary()
        
        clear_scene(self)
    
    def section_and_operation(self):
        """AND运算"""
        # 小节标题
        section_title = VGroup(
            Text("AND 运算 (与)", font_size=26, color=Colors.AND_COLOR),
            MathTex(r"\land", font_size=32, color=Colors.AND_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 含义
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"而且" - 全真才真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        # 真值表
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        # 表头
        header = create_truth_table_header(["A", "B"], "A ∧ B", Colors.AND_COLOR)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1)
        
        self.play(FadeIn(header))
        
        # 数据行
        and_data = [
            ([0, 0], 0),
            ([0, 1], 0),
            ([1, 0], 0),
            ([1, 1], 1),  # 只有这个是1
        ]
        
        rows = VGroup()
        for values, result in and_data:
            row = create_truth_table_row(values, result, Colors.AND_COLOR)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(header, DOWN, buff=0.2)
        
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
            if i == 3:  # 高亮最后一行
                highlight = SurroundingRectangle(row, color=Colors.AND_COLOR, buff=0.05)
                self.play(Create(highlight), run_time=0.3)
        
        # 类比：串联开关
        analogy_title = Text("类比: 串联开关", font_size=16, color=Colors.TEXT)
        analogy_title.next_to(truth_table_title, RIGHT, buff=2.5)
        
        self.play(FadeIn(analogy_title))
        
        analogy_desc = Text("两个开关都闭合，灯才亮", font_size=14, color=Colors.GRAY)
        analogy_desc.next_to(analogy_title, DOWN, buff=0.2)
        
        self.play(FadeIn(analogy_desc))
        
        # 示意图
        circuit_on = VGroup(
            Text("S1=1, S2=1 → 亮", font_size=14, color=Colors.ONE),
        )
        circuit_off = VGroup(
            Text("其他情况 → 灭", font_size=14, color=Colors.ZERO),
        )
        
        circuits = VGroup(circuit_on, circuit_off).arrange(DOWN, buff=0.2)
        circuits.next_to(analogy_desc, DOWN, buff=0.3)
        
        self.play(FadeIn(circuits))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(highlight),
            FadeOut(analogy_title), FadeOut(analogy_desc),
            FadeOut(circuits),
            run_time=0.5
        )
    
    def section_or_operation(self):
        """OR运算"""
        # 小节标题
        section_title = VGroup(
            Text("OR 运算 (或)", font_size=26, color=Colors.OR_COLOR),
            MathTex(r"\lor", font_size=32, color=Colors.OR_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 含义
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"或者" - 有真即真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        # 真值表
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        # 表头
        header = create_truth_table_header(["A", "B"], "A ∨ B", Colors.OR_COLOR)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1)
        
        self.play(FadeIn(header))
        
        # 数据行
        or_data = [
            ([0, 0], 0),  # 只有这个是0
            ([0, 1], 1),
            ([1, 0], 1),
            ([1, 1], 1),
        ]
        
        rows = VGroup()
        highlights = VGroup()
        for i, (values, result) in enumerate(or_data):
            row = create_truth_table_row(values, result, Colors.OR_COLOR)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(header, DOWN, buff=0.2)
        
        for i, row in enumerate(rows):
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
            if i > 0:  # 高亮结果为1的行
                highlight = SurroundingRectangle(row, color=Colors.OR_COLOR, buff=0.05)
                highlights.add(highlight)
                self.play(Create(highlight), run_time=0.2)
        
        # 类比：并联开关
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
        
        # 清除
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(highlights),
            FadeOut(analogy_title), FadeOut(analogy_desc),
            FadeOut(circuits),
            run_time=0.5
        )
    
    def section_not_operation(self):
        """NOT运算"""
        # 小节标题
        section_title = VGroup(
            Text("NOT 运算 (非)", font_size=26, color=Colors.NOT_COLOR),
            MathTex(r"\neg", font_size=32, color=Colors.NOT_COLOR),
        ).arrange(RIGHT, buff=0.3)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 含义
        meaning = VGroup(
            Text("含义: ", font_size=18, color=Colors.TEXT),
            Text('"取反" - 真变假，假变真', font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        
        # 真值表
        truth_table_title = Text("真值表:", font_size=16, color=Colors.TEXT)
        truth_table_title.next_to(meaning, DOWN, buff=0.4).align_to(meaning, LEFT)
        
        self.play(FadeIn(truth_table_title))
        
        # 表头
        header = VGroup(
            Text("A", font_size=18, color=Colors.TEXT),
            Text("¬A", font_size=18, color=Colors.NOT_COLOR),
        ).arrange(RIGHT, buff=1.0)
        header.next_to(truth_table_title, DOWN, buff=0.2).set_x(-1.5)
        
        self.play(FadeIn(header))
        
        # 数据行
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
        
        self.wait(0.5)
        
        # 可视化：翻转动画
        flip_title = Text("取反可视化:", font_size=16, color=Colors.TEXT)
        flip_title.next_to(truth_table_title, RIGHT, buff=2.5)
        
        self.play(FadeIn(flip_title))
        
        # 创建翻转动画
        bit_0 = create_bit_cell(0, size=0.7)
        bit_0.next_to(flip_title, DOWN, buff=0.5)
        
        self.play(FadeIn(bit_0))
        self.wait(0.3)
        
        # 翻转效果
        bit_1 = create_bit_cell(1, size=0.7)
        bit_1.move_to(bit_0.get_center())
        
        arrow = MathTex(r"\xrightarrow{\neg}", font_size=24, color=Colors.NOT_COLOR)
        arrow.next_to(bit_0, RIGHT, buff=0.3)
        
        bit_1_copy = create_bit_cell(1, size=0.7)
        bit_1_copy.next_to(arrow, RIGHT, buff=0.3)
        
        self.play(FadeIn(arrow), FadeIn(bit_1_copy))
        self.wait(0.5)
        
        # 反向
        arrow2 = MathTex(r"\xrightarrow{\neg}", font_size=24, color=Colors.NOT_COLOR)
        arrow2.next_to(bit_1_copy, RIGHT, buff=0.3)
        
        bit_0_result = create_bit_cell(0, size=0.7)
        bit_0_result.next_to(arrow2, RIGHT, buff=0.3)
        
        self.play(FadeIn(arrow2), FadeIn(bit_0_result))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title), FadeOut(meaning),
            FadeOut(truth_table_title), FadeOut(header),
            FadeOut(rows), FadeOut(flip_title),
            FadeOut(bit_0), FadeOut(arrow), FadeOut(bit_1_copy),
            FadeOut(arrow2), FadeOut(bit_0_result),
            run_time=0.5
        )
    
    def section_summary(self):
        """运算总结"""
        # 小节标题
        section_title = Text("三种运算总结", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建总结卡片
        cards = VGroup()
        
        # AND卡片
        and_card = VGroup(
            Text("AND (∧)", font_size=20, color=Colors.AND_COLOR),
            Text("全真才真", font_size=14, color=Colors.GRAY),
            MathTex(r"1 \land 1 = 1", font_size=18, color=Colors.TEXT),
            Text("其余为 0", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        and_box = SurroundingRectangle(and_card, color=Colors.AND_COLOR, buff=0.2)
        cards.add(VGroup(and_box, and_card))
        
        # OR卡片
        or_card = VGroup(
            Text("OR (∨)", font_size=20, color=Colors.OR_COLOR),
            Text("有真即真", font_size=14, color=Colors.GRAY),
            MathTex(r"0 \lor 0 = 0", font_size=18, color=Colors.TEXT),
            Text("其余为 1", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        or_box = SurroundingRectangle(or_card, color=Colors.OR_COLOR, buff=0.2)
        cards.add(VGroup(or_box, or_card))
        
        # NOT卡片
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
        
        # 关键点
        key_point = VGroup(
            Text("所有复杂逻辑都可以用这三种运算组合而成！", font_size=18, color=Colors.PRIMARY),
        )
        key_point.next_to(cards, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_02_operations.py Scene02Operations
    pass
