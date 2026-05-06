"""
Scene 3: 整数的存储 - 精确的数字世界
解释计算机如何存储整数，引入位数限制、溢出和补码概念
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#FF6B6B"    # 警示红
    ACCENT = "#4ECDC4"       # 青绿
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    BINARY_0 = "#2C3E50"     # 0的颜色
    BINARY_1 = "#F39C12"     # 1的颜色
    HIGHLIGHT = "#9B59B6"    # 紫色高亮
    SUCCESS = "#2ECC71"      # 成功绿


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_bit_cell(value, size=0.6, show_value=True):
    """创建一个比特单元格"""
    bg_color = Colors.BINARY_1 if value == 1 else Colors.BINARY_0
    
    rect = Square(side_length=size)
    rect.set_fill(bg_color, opacity=0.8)
    rect.set_stroke(Colors.PRIMARY, width=2)
    
    if show_value:
        digit = Text(str(value), font_size=int(size * 35), color=WHITE)
        digit.move_to(rect.get_center())
        return VGroup(rect, digit)
    return rect


def create_byte_display(value, num_bits=8, size=0.5):
    """创建一个字节的显示"""
    # 转换为二进制字符串
    binary = format(value, f'0{num_bits}b')
    
    cells = VGroup()
    for bit in binary:
        cell = create_bit_cell(int(bit), size=size)
        cells.add(cell)
    cells.arrange(RIGHT, buff=0.05)
    
    return cells


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene03Integers(Scene):
    """Scene 3: 整数存储"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_fixed_bits()
        self.section_range_limit()
        self.section_overflow()
        self.section_negative_numbers()
        
        clear_scene(self)
    
    def section_fixed_bits(self):
        """固定位数存储"""
        # 小节标题
        section_title = Text("整数: 精确存储", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 内存比喻
        memory_intro = Text(
            "计算机用固定数量的'格子'存放数字",
            font_size=22, color=Colors.GRAY
        )
        memory_intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(memory_intro))
        self.wait(0.5)
        
        # 8位存储空间可视化
        byte_label = Text("8位 (1字节)", font_size=20, color=Colors.PRIMARY)
        byte_label.next_to(memory_intro, DOWN, buff=0.5).set_x(0)
        
        # 创建8个空格子
        empty_cells = VGroup()
        for _ in range(8):
            cell = Square(side_length=0.6)
            cell.set_stroke(Colors.PRIMARY, width=2)
            cell.set_fill(Colors.BG, opacity=0.5)
            empty_cells.add(cell)
        empty_cells.arrange(RIGHT, buff=0.05)
        empty_cells.next_to(byte_label, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(byte_label))
        self.play(
            LaggedStart(
                *[FadeIn(c, scale=0.8) for c in empty_cells],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 存入数字 42
        store_text = VGroup(
            Text("存入数字: ", font_size=22, color=Colors.TEXT),
            Text("42", font_size=28, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        store_text.next_to(empty_cells, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(store_text))
        self.wait(0.3)
        
        # 转换为二进制: 42 = 00101010
        binary_42 = create_byte_display(42, num_bits=8, size=0.6)
        binary_42.move_to(empty_cells.get_center())
        
        self.play(
            FadeOut(empty_cells),
            FadeIn(binary_42),
            run_time=0.8
        )
        
        # 显示二进制值
        binary_text = VGroup(
            Text("二进制: ", font_size=20, color=Colors.GRAY),
            Text("00101010", font_size=22, color=Colors.PRIMARY, font="Menlo"),
        ).arrange(RIGHT, buff=0.1)
        binary_text.next_to(binary_42, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(binary_text))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(memory_intro),
            FadeOut(byte_label),
            FadeOut(binary_42),
            FadeOut(store_text),
            FadeOut(binary_text),
            run_time=0.5
        )
    
    def section_range_limit(self):
        """范围限制"""
        # 小节标题
        section_title = Text("范围限制: 有多少格子, 能存多大的数", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 公式
        formula = VGroup(
            Text("n位无符号整数范围: ", font_size=20, color=Colors.GRAY),
            MathTex(r"[0, 2^n - 1]", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        formula.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(formula))
        self.wait(0.5)
        
        # 具体例子
        examples = VGroup()
        
        # 8位
        ex8 = VGroup(
            Text("8位: ", font_size=20, color=Colors.TEXT),
            MathTex(r"[0, 255]", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.2)
        examples.add(ex8)
        
        # 16位
        ex16 = VGroup(
            Text("16位: ", font_size=20, color=Colors.TEXT),
            MathTex(r"[0, 65535]", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.2)
        examples.add(ex16)
        
        # 32位
        ex32 = VGroup(
            Text("32位: ", font_size=20, color=Colors.TEXT),
            MathTex(r"[0, 4294967295]", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.2)
        examples.add(ex32)
        
        examples.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        examples.next_to(formula, DOWN, buff=0.5).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(0.5)
        
        # 可视化8位范围
        range_visual = VGroup()
        
        # 数轴
        number_line = NumberLine(
            x_range=[0, 255, 50],
            length=8,
            include_numbers=True,
            numbers_to_include=[0, 50, 100, 150, 200, 255],
            font_size=16,
            color=Colors.GRAY
        )
        range_visual.add(number_line)
        range_visual.next_to(examples, DOWN, buff=0.6).set_x(0)
        
        self.play(Create(number_line), run_time=1)
        
        # 高亮范围
        brace = BraceBetweenPoints(
            number_line.n2p(0) + UP * 0.3,
            number_line.n2p(255) + UP * 0.3,
            direction=UP,
            color=Colors.PRIMARY
        )
        brace_text = Text("8位能表示的全部范围", font_size=18, color=Colors.PRIMARY)
        brace_text.next_to(brace, UP, buff=0.1)
        
        self.play(Create(brace), FadeIn(brace_text))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(formula),
            FadeOut(examples),
            FadeOut(number_line),
            FadeOut(brace),
            FadeOut(brace_text),
            run_time=0.5
        )
    
    def section_overflow(self):
        """溢出演示"""
        # 小节标题
        section_title = Text("溢出: 超出范围会怎样?", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 场景: 255 + 1
        scenario = VGroup(
            Text("8位存储: ", font_size=22, color=Colors.GRAY),
            Text("255 + 1 = ?", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        scenario.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(scenario))
        self.wait(0.5)
        
        # 显示255的二进制
        label_255 = Text("255 =", font_size=20, color=Colors.TEXT)
        binary_255 = create_byte_display(255, num_bits=8, size=0.5)
        group_255 = VGroup(label_255, binary_255).arrange(RIGHT, buff=0.3)
        group_255.next_to(scenario, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(label_255), FadeIn(binary_255))
        self.wait(0.5)
        
        # +1 操作
        plus_one = Text("+1", font_size=24, color=Colors.ACCENT)
        plus_one.next_to(binary_255, RIGHT, buff=0.3)
        
        self.play(FadeIn(plus_one, scale=1.2))
        self.wait(0.3)
        
        # 结果应该是 256 = 100000000 (9位)
        result_label = Text("理论结果: ", font_size=20, color=Colors.GRAY)
        result_label.next_to(group_255, DOWN, buff=0.4)
        result_label.align_to(label_255, LEFT)
        
        # 9位二进制
        binary_256_9bit = VGroup()
        overflow_bit = create_bit_cell(1, size=0.5)
        overflow_bit.set_opacity(0.5)
        for bit in "00000000":
            cell = create_bit_cell(int(bit), size=0.5)
            binary_256_9bit.add(cell)
        
        full_result = VGroup(overflow_bit, binary_256_9bit).arrange(RIGHT, buff=0.05)
        full_result.next_to(result_label, RIGHT, buff=0.2)
        
        # 创建一个包含标签的组
        result_group = VGroup(result_label)
        self.play(FadeIn(result_label))
        self.play(FadeIn(full_result), run_time=0.5)
        self.wait(0.5)
        
        # 高位被丢弃的动画
        warning = Text("但只有8位! 高位被丢弃!", font_size=20, color=Colors.SECONDARY)
        warning.next_to(full_result, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(warning))
        self.wait(0.3)
        
        # 溢出位消失
        cross = Cross(overflow_bit, color=Colors.SECONDARY, stroke_width=3)
        self.play(Create(cross), run_time=0.3)
        self.play(
            FadeOut(overflow_bit),
            FadeOut(cross),
            run_time=0.5
        )
        self.wait(0.3)
        
        # 最终结果
        final_result = VGroup(
            Text("实际结果: ", font_size=20, color=Colors.TEXT),
            Text("0", font_size=28, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        final_result.next_to(warning, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(final_result))
        
        # 警告框
        alert_box = VGroup(
            Text("⚠️ 溢出是程序员必须警惕的陷阱!", font_size=20, color=Colors.SECONDARY),
        )
        alert_box.next_to(final_result, DOWN, buff=0.4).set_x(0)
        
        alert_rect = SurroundingRectangle(alert_box, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(alert_box), Create(alert_rect))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(scenario),
            FadeOut(group_255),
            FadeOut(plus_one),
            FadeOut(result_label),
            FadeOut(binary_256_9bit),
            FadeOut(warning),
            FadeOut(final_result),
            FadeOut(alert_box),
            FadeOut(alert_rect),
            run_time=0.5
        )
    
    def section_negative_numbers(self):
        """负数表示 - 补码"""
        # 小节标题
        section_title = Text("负数怎么办? 补码的巧妙设计", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 问题引入
        problem = Text("计算机只有0和1, 如何表示负数?", font_size=22, color=Colors.GRAY)
        problem.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(problem))
        self.wait(0.5)
        
        # 解决方案: 补码
        solution_title = Text("解决方案: 二进制补码", font_size=22, color=Colors.ACCENT)
        solution_title.next_to(problem, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(solution_title))
        self.wait(0.3)
        
        # 补码的核心思想
        idea = VGroup(
            Text("最高位作为符号位:", font_size=20, color=Colors.TEXT),
            Text("0 = 正数, 1 = 负数", font_size=20, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.3)
        idea.next_to(solution_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(idea))
        self.wait(0.5)
        
        # 例子
        examples_title = Text("8位有符号整数示例:", font_size=20, color=Colors.GRAY)
        examples_title.next_to(idea, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(examples_title))
        
        # +5 的表示
        pos_example = VGroup(
            Text("+5 = ", font_size=20, color=Colors.SUCCESS),
        )
        pos_binary = create_byte_display(5, num_bits=8, size=0.45)
        pos_group = VGroup(pos_example, pos_binary).arrange(RIGHT, buff=0.2)
        pos_group.next_to(examples_title, DOWN, buff=0.3)
        pos_group.set_x(0)
        
        self.play(FadeIn(pos_group))
        
        # 高亮符号位
        sign_highlight = SurroundingRectangle(
            pos_binary[0], color=Colors.SUCCESS, buff=0.02, stroke_width=2
        )
        sign_label = Text("符号位=0 (正)", font_size=14, color=Colors.SUCCESS)
        sign_label.next_to(sign_highlight, UP, buff=0.1)
        
        self.play(Create(sign_highlight), FadeIn(sign_label))
        self.wait(0.5)
        
        # -5 的表示 (补码: 11111011)
        neg_example = VGroup(
            Text("-5 = ", font_size=20, color=Colors.SECONDARY),
        )
        # -5 in 8-bit two's complement is 251 in unsigned
        neg_binary = create_byte_display(251, num_bits=8, size=0.45)
        neg_group = VGroup(neg_example, neg_binary).arrange(RIGHT, buff=0.2)
        neg_group.next_to(pos_group, DOWN, buff=0.4)
        neg_group.set_x(0)
        
        self.play(
            FadeOut(sign_highlight),
            FadeOut(sign_label),
            FadeIn(neg_group)
        )
        
        # 高亮负数符号位
        neg_sign_highlight = SurroundingRectangle(
            neg_binary[0], color=Colors.SECONDARY, buff=0.02, stroke_width=2
        )
        neg_sign_label = Text("符号位=1 (负)", font_size=14, color=Colors.SECONDARY)
        neg_sign_label.next_to(neg_sign_highlight, UP, buff=0.1)
        
        self.play(Create(neg_sign_highlight), FadeIn(neg_sign_label))
        self.wait(0.5)
        
        # 补码的好处
        benefit = VGroup(
            Text("补码的好处:", font_size=20, color=Colors.ACCENT),
            Text("同一套电路可以处理加法和减法!", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.3)
        benefit.next_to(neg_group, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeOut(neg_sign_highlight),
            FadeOut(neg_sign_label),
            FadeIn(benefit)
        )
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_03_integers.py Scene03Integers
    pass
