"""
计算机与数字：二进制的奥秘
完整视频 - 整合所有场景

渲染命令:
  - 预览质量: manim -pql all_scenes.py ComputersAndNumbers
  - 高质量: manim -pqh all_scenes.py ComputersAndNumbers
  - 4K质量: manim -pqk all_scenes.py ComputersAndNumbers

单独渲染各场景:
  - manim -pql scene_01_intro.py Scene01Intro
  - manim -pql scene_02_number_systems.py Scene02NumberSystems
  - manim -pql scene_03_integers.py Scene03Integers
  - manim -pql scene_04_floats.py Scene04Floats
  - manim -pql scene_05_special_cases.py Scene05SpecialCases
  - manim -pql scene_06_summary.py Scene06Summary
"""

from manim import *


# ============================================================================
# 配色方案
# ============================================================================
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#FF6B6B"    # 警示红
    ACCENT = "#4ECDC4"       # 青绿
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    BINARY_0 = "#2C3E50"     # 0的颜色
    BINARY_1 = "#F39C12"     # 1的颜色
    SIGN_COLOR = "#E74C3C"   # 符号位颜色
    EXP_COLOR = "#3498DB"    # 指数位颜色
    MANTISSA_COLOR = "#2ECC71"  # 尾数位颜色
    HIGHLIGHT = "#9B59B6"    # 紫色高亮
    SUCCESS = "#2ECC71"      # 成功绿
    WARNING = "#F39C12"      # 警告橙
    DANGER = "#E74C3C"       # 危险红


# ============================================================================
# 工具函数
# ============================================================================
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
    binary = format(value, f'0{num_bits}b')
    
    cells = VGroup()
    for bit in binary:
        cell = create_bit_cell(int(bit), size=size)
        cells.add(cell)
    cells.arrange(RIGHT, buff=0.05)
    
    return cells


def create_digit_box(digit, color=Colors.PRIMARY, size=0.7):
    """创建一个数字方框"""
    box = Square(side_length=size)
    box.set_stroke(color, width=2)
    box.set_fill(color, opacity=0.2)
    
    text = Text(str(digit), font_size=int(size * 35), color=Colors.TEXT)
    text.move_to(box.get_center())
    
    return VGroup(box, text)


def create_power_label(base, power, font_size=18):
    """创建幂次标签"""
    return MathTex(f"{base}^{{{power}}}", font_size=font_size, color=Colors.GRAY)


def create_lightbulb(is_on=False, size=0.8):
    """创建一个灯泡图形"""
    bulb = Circle(radius=size * 0.4)
    bulb.set_stroke(Colors.PRIMARY, width=2)
    
    base_width = size * 0.3
    base_height = size * 0.2
    base = Rectangle(width=base_width, height=base_height)
    base.set_stroke(Colors.PRIMARY, width=2)
    base.set_fill(Colors.GRAY, opacity=0.5)
    base.next_to(bulb, DOWN, buff=0)
    
    if is_on:
        bulb.set_fill(Colors.BINARY_1, opacity=0.9)
        glow = Circle(radius=size * 0.6)
        glow.set_fill(Colors.BINARY_1, opacity=0.2)
        glow.set_stroke(width=0)
        glow.move_to(bulb.get_center())
        return VGroup(glow, bulb, base)
    else:
        bulb.set_fill(Colors.BINARY_0, opacity=0.5)
        return VGroup(bulb, base)


def create_ieee754_structure(width=10, height=0.8):
    """创建 IEEE 754 32位浮点数结构图"""
    sign_width = width * (1/32)
    exp_width = width * (8/32)
    mantissa_width = width * (23/32)
    
    sign_rect = Rectangle(width=sign_width, height=height)
    sign_rect.set_fill(Colors.SIGN_COLOR, opacity=0.7)
    sign_rect.set_stroke(Colors.TEXT, width=2)
    
    exp_rect = Rectangle(width=exp_width, height=height)
    exp_rect.set_fill(Colors.EXP_COLOR, opacity=0.7)
    exp_rect.set_stroke(Colors.TEXT, width=2)
    
    mantissa_rect = Rectangle(width=mantissa_width, height=height)
    mantissa_rect.set_fill(Colors.MANTISSA_COLOR, opacity=0.7)
    mantissa_rect.set_stroke(Colors.TEXT, width=2)
    
    structure = VGroup(sign_rect, exp_rect, mantissa_rect)
    structure.arrange(RIGHT, buff=0)
    
    sign_label = Text("S", font_size=18, color=Colors.TEXT)
    sign_label.move_to(sign_rect.get_center())
    
    exp_label = Text("指数 (8位)", font_size=16, color=Colors.TEXT)
    exp_label.move_to(exp_rect.get_center())
    
    mantissa_label = Text("尾数 (23位)", font_size=16, color=Colors.TEXT)
    mantissa_label.move_to(mantissa_rect.get_center())
    
    sign_bits = Text("1位", font_size=12, color=Colors.SIGN_COLOR)
    sign_bits.next_to(sign_rect, UP, buff=0.1)
    
    exp_bits = Text("8位", font_size=12, color=Colors.EXP_COLOR)
    exp_bits.next_to(exp_rect, UP, buff=0.1)
    
    mantissa_bits = Text("23位", font_size=12, color=Colors.MANTISSA_COLOR)
    mantissa_bits.next_to(mantissa_rect, UP, buff=0.1)
    
    return VGroup(
        structure,
        sign_label, exp_label, mantissa_label,
        sign_bits, exp_bits, mantissa_bits
    )


def create_key_point_card(title, content, color=Colors.PRIMARY, width=5, height=1.5):
    """创建要点卡片"""
    card = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.15,
        fill_color=color, fill_opacity=0.15,
        stroke_color=color, stroke_width=2
    )
    
    title_text = Text(title, font_size=18, color=color)
    content_text = Text(content, font_size=14, color=Colors.TEXT)
    
    text_group = VGroup(title_text, content_text).arrange(DOWN, buff=0.15)
    text_group.move_to(card.get_center())
    
    return VGroup(card, text_group)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ============================================================================
# 主场景: 完整视频
# ============================================================================
class ComputersAndNumbers(Scene):
    """计算机与数字 - 完整教学视频"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # Scene 1: 开场引入
        self.scene_01_intro()
        
        # Scene 2: 进制转换
        self.scene_02_number_systems()
        
        # Scene 3: 整数存储
        self.scene_03_integers()
        
        # Scene 4: 浮点数存储
        self.scene_04_floats()
        
        # Scene 5: 特殊情况
        self.scene_05_special_cases()
        
        # Scene 6: 总结
        self.scene_06_summary()
        
        # 结束
        self.play(FadeOut(self.chapter_title))
        self.wait(0.5)
    
    # ========================================================================
    # Scene 1: 开场引入
    # ========================================================================
    def scene_01_intro(self):
        """开场引入 - 计算机的二进制世界"""
        # 大标题
        main_title = Text("计算机与数字", font_size=48, color=Colors.PRIMARY)
        subtitle = Text("二进制的奥秘", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        self.play(
            FadeOut(subtitle),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.5)
        
        # 神秘计算
        question = Text("一个奇怪的现象...", font_size=28, color=Colors.TEXT)
        question.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(question, shift=DOWN * 0.2))
        self.wait(0.5)
        
        code_bg = RoundedRectangle(
            width=8, height=2.5, corner_radius=0.2,
            fill_color="#0d1117", fill_opacity=0.9,
            stroke_color=Colors.PRIMARY, stroke_width=2
        )
        code_bg.next_to(question, DOWN, buff=0.5).set_x(0)
        
        code_text = Text(">>> 0.1 + 0.2", font_size=22, color=Colors.ACCENT, font="Menlo")
        code_text.move_to(code_bg.get_center() + UP * 0.4)
        
        self.play(FadeIn(code_bg), run_time=0.3)
        self.play(Write(code_text), run_time=0.8)
        self.wait(0.5)
        
        result_text = Text(
            "0.30000000000000004",
            font_size=22, color=Colors.SECONDARY, font="Menlo"
        )
        result_text.move_to(code_bg.get_center() + DOWN * 0.3)
        
        self.play(Write(result_text), run_time=0.8)
        self.play(Flash(result_text, color=Colors.SECONDARY, line_length=0.3), run_time=0.5)
        self.wait(0.5)
        
        big_question = Text("计算机真的会算错吗?", font_size=32, color=Colors.TEXT)
        big_question.next_to(code_bg, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(big_question), run_time=0.8)
        self.wait(1)
        
        self.play(
            FadeOut(question), FadeOut(code_bg), FadeOut(code_text),
            FadeOut(result_text), FadeOut(big_question),
            run_time=0.5
        )
        
        # 揭示二进制
        core_concept = VGroup(
            Text("计算机只认识", font_size=32, color=Colors.TEXT),
            Text("0 和 1", font_size=48, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.2)
        core_concept.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(core_concept[0]), run_time=0.5)
        self.play(Write(core_concept[1]), run_time=0.8)
        self.wait(0.5)
        
        binary_stream = VGroup()
        for i in range(16):
            digit = create_bit_cell(i % 2, size=0.5)
            binary_stream.add(digit)
        binary_stream.arrange(RIGHT, buff=0.1)
        binary_stream.next_to(core_concept, DOWN, buff=0.6).set_x(0)
        
        self.play(
            LaggedStart(
                *[FadeIn(d, scale=0.5) for d in binary_stream],
                lag_ratio=0.1
            ),
            run_time=1.5
        )
        self.wait(1)
        
        self.play(FadeOut(core_concept), FadeOut(binary_stream), run_time=0.5)
        
        # 灯泡演示
        demo_title = Text("开关 = 二进制位", font_size=28, color=Colors.TEXT)
        demo_title.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(demo_title))
        
        bulb_off = create_lightbulb(is_on=False, size=1.2)
        bulb_on = create_lightbulb(is_on=True, size=1.2)
        
        bulbs = VGroup(bulb_off, bulb_on).arrange(RIGHT, buff=2)
        bulbs.next_to(demo_title, DOWN, buff=0.8).set_x(0)
        
        label_off = VGroup(
            Text("关", font_size=24, color=Colors.GRAY),
            Text("= 0", font_size=28, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.1)
        label_off.next_to(bulb_off, DOWN, buff=0.3)
        
        label_on = VGroup(
            Text("开", font_size=24, color=Colors.GRAY),
            Text("= 1", font_size=28, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.1)
        label_on.next_to(bulb_on, DOWN, buff=0.3)
        
        self.play(FadeIn(bulb_off), FadeIn(bulb_on), run_time=0.5)
        self.play(FadeIn(label_off), FadeIn(label_on), run_time=0.5)
        self.wait(1)
        
        summary = VGroup(
            Text("计算机的一切数据", font_size=24, color=Colors.TEXT),
            Text("都由无数个 0 和 1 组成", font_size=24, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        summary.next_to(VGroup(label_off, label_on), DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(
            FadeOut(demo_title), FadeOut(bulbs),
            FadeOut(label_off), FadeOut(label_on), FadeOut(summary),
            run_time=0.5
        )
    
    # ========================================================================
    # Scene 2: 进制转换
    # ========================================================================
    def scene_02_number_systems(self):
        """进制转换 - 数字的多种语言"""
        # 十进制
        section_title = Text("十进制 - 我们熟悉的语言", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        example_num = Text("1234", font_size=48, color=Colors.PRIMARY)
        example_num.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(Write(example_num))
        self.wait(0.5)
        
        key_point = Text("关键: 满十进一", font_size=22, color=Colors.GRAY)
        key_point.next_to(example_num, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(example_num), FadeOut(key_point), run_time=0.5)
        
        # 二进制
        section_title = Text("二进制 - 计算机的语言", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        concept = VGroup(
            Text("只用 0 和 1", font_size=24, color=Colors.ACCENT),
            Text("满二进一", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=1)
        concept.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(concept))
        
        example_title = VGroup(
            Text("例: ", font_size=24, color=Colors.TEXT),
            MathTex(r"1011_2", font_size=28, color=Colors.PRIMARY),
            Text(" 等于多少?", font_size=24, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(concept, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_title))
        
        calc_steps = VGroup(
            MathTex(r"1 \times 2^3", font_size=22, color=Colors.TEXT),
            MathTex(r"+ 0 \times 2^2", font_size=22, color=Colors.GRAY),
            MathTex(r"+ 1 \times 2^1", font_size=22, color=Colors.TEXT),
            MathTex(r"+ 1 \times 2^0", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.15)
        calc_steps.next_to(example_title, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(calc_steps), run_time=1)
        
        result_steps = VGroup(
            MathTex(r"= 8", font_size=22, color=Colors.ACCENT),
            MathTex(r"+ 0", font_size=22, color=Colors.GRAY),
            MathTex(r"+ 2", font_size=22, color=Colors.ACCENT),
            MathTex(r"+ 1", font_size=22, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.15)
        result_steps.next_to(calc_steps, DOWN, buff=0.25).set_x(0)
        
        self.play(FadeIn(result_steps, shift=UP * 0.2))
        
        final = MathTex(r"= 11", font_size=36, color=Colors.PRIMARY)
        final.next_to(result_steps, DOWN, buff=0.25).set_x(0)
        
        self.play(Write(final))
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(concept), FadeOut(example_title),
            FadeOut(calc_steps), FadeOut(result_steps), FadeOut(final),
            run_time=0.5
        )
        
        # 十六进制
        section_title = Text("十六进制 - 程序员的缩写", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        mapping_title = Text("使用 0-9 和 A-F (共16个符号)", font_size=22, color=Colors.GRAY)
        mapping_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(mapping_title))
        
        example_title = VGroup(
            Text("例: ", font_size=24, color=Colors.TEXT),
            MathTex(r"A3_{16}", font_size=28, color=Colors.PRIMARY),
            Text(" = 10×16 + 3 = ", font_size=24, color=Colors.TEXT),
            Text("163", font_size=28, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(mapping_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_title))
        self.wait(1)
        
        # 总结
        summary = VGroup(
            Text("关键理解:", font_size=22, color=Colors.ACCENT),
            Text("数值本身不变, 只是表示方式不同", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.3)
        summary.next_to(example_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(mapping_title),
            FadeOut(example_title), FadeOut(summary),
            run_time=0.5
        )
    
    # ========================================================================
    # Scene 3: 整数存储
    # ========================================================================
    def scene_03_integers(self):
        """整数存储 - 精确的数字世界"""
        # 固定位数
        section_title = Text("整数: 精确存储", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        memory_intro = Text(
            "计算机用固定数量的'格子'存放数字",
            font_size=22, color=Colors.GRAY
        )
        memory_intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(memory_intro))
        
        byte_label = Text("8位 (1字节) 存储数字 42:", font_size=20, color=Colors.PRIMARY)
        byte_label.next_to(memory_intro, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(byte_label))
        
        binary_42 = create_byte_display(42, num_bits=8, size=0.6)
        binary_42.next_to(byte_label, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(binary_42), run_time=0.8)
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(memory_intro),
            FadeOut(byte_label), FadeOut(binary_42),
            run_time=0.5
        )
        
        # 范围限制
        section_title = Text("范围限制: 有多少格子, 能存多大的数", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        formula = VGroup(
            Text("n位无符号整数范围: ", font_size=20, color=Colors.GRAY),
            MathTex(r"[0, 2^n - 1]", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        formula.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(formula))
        
        examples = VGroup(
            VGroup(Text("8位: ", font_size=20), MathTex(r"[0, 255]", font_size=24, color=Colors.ACCENT)).arrange(RIGHT),
            VGroup(Text("16位: ", font_size=20), MathTex(r"[0, 65535]", font_size=24, color=Colors.ACCENT)).arrange(RIGHT),
            VGroup(Text("32位: ", font_size=20), MathTex(r"[0, 4294967295]", font_size=24, color=Colors.ACCENT)).arrange(RIGHT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        examples.next_to(formula, DOWN, buff=0.4).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.35)
        
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(formula), FadeOut(examples), run_time=0.5)
        
        # 溢出
        section_title = Text("溢出: 超出范围会怎样?", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        scenario = VGroup(
            Text("8位存储: ", font_size=22, color=Colors.GRAY),
            Text("255 + 1 = ?", font_size=28, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.2)
        scenario.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(scenario))
        
        binary_255 = create_byte_display(255, num_bits=8, size=0.5)
        binary_255.next_to(scenario, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(binary_255))
        self.wait(0.5)
        
        warning = Text("高位被丢弃! 结果变成 0", font_size=22, color=Colors.SECONDARY)
        warning.next_to(binary_255, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(warning))
        
        alert_box = Text("⚠️ 溢出是程序员必须警惕的陷阱!", font_size=20, color=Colors.SECONDARY)
        alert_box.next_to(warning, DOWN, buff=0.3).set_x(0)
        
        alert_rect = SurroundingRectangle(alert_box, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(alert_box), Create(alert_rect))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(scenario), FadeOut(binary_255),
            FadeOut(warning), FadeOut(alert_box), FadeOut(alert_rect),
            run_time=0.5
        )
    
    # ========================================================================
    # Scene 4: 浮点数存储
    # ========================================================================
    def scene_04_floats(self):
        """浮点数存储 - IEEE 754 标准"""
        # 为什么近似
        section_title = Text("浮点数: 近似存储", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        reason1 = VGroup(
            Text("实数是无限的 (如 ", font_size=20, color=Colors.TEXT),
            MathTex(r"\pi", font_size=24, color=Colors.PRIMARY),
            Text(" = 3.14159...)", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        reason1.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(reason1))
        
        reason2 = Text("但计算机内存是有限的", font_size=20, color=Colors.TEXT)
        reason2.next_to(reason1, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(reason2))
        
        conclusion = Text("→ 只能存储最接近的近似值", font_size=20, color=Colors.SECONDARY)
        conclusion.next_to(reason2, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(conclusion))
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(reason1), FadeOut(reason2), FadeOut(conclusion), run_time=0.5)
        
        # IEEE 754 结构
        section_title = Text("IEEE 754: 国际标准浮点数格式", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        format_label = Text("32位单精度浮点数结构:", font_size=20, color=Colors.GRAY)
        format_label.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(format_label))
        
        ieee_struct = create_ieee754_structure(width=9, height=0.7)
        ieee_struct.next_to(format_label, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(ieee_struct), run_time=1)
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(format_label), FadeOut(ieee_struct), run_time=0.5)
        
        # 0.1 的真相
        section_title = Text("揭秘: 0.1 的真相", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        truth1 = VGroup(
            Text("0.1 在二进制中是", font_size=20, color=Colors.TEXT),
            Text("无限循环小数", font_size=20, color=Colors.SECONDARY),
            Text("!", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        truth1.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(truth1))
        
        binary_rep = VGroup(
            MathTex(r"0.1_{10}", font_size=24, color=Colors.PRIMARY),
            Text(" = ", font_size=20, color=Colors.TEXT),
            MathTex(r"0.0001100110011..._2", font_size=22, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        binary_rep.next_to(truth1, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(binary_rep))
        
        truncate = VGroup(
            Text("存储时必须截断 → ", font_size=18, color=Colors.GRAY),
            Text("精度丢失!", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        truncate.next_to(binary_rep, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(truncate))
        
        final_box = VGroup(
            Text("这不是Bug, 而是", font_size=20, color=Colors.TEXT),
            Text("有限内存的必然结果", font_size=20, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        final_box.next_to(truncate, DOWN, buff=0.4).set_x(0)
        
        box = SurroundingRectangle(final_box, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(final_box), Create(box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(truth1), FadeOut(binary_rep),
            FadeOut(truncate), FadeOut(final_box), FadeOut(box),
            run_time=0.5
        )
    
    # ========================================================================
    # Scene 5: 特殊情况
    # ========================================================================
    def scene_05_special_cases(self):
        """特殊情况 - 误差与特殊值"""
        # 误差累积
        section_title = Text("舍入误差累积: 小误差, 大问题", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        scenario = Text("在复杂的科学计算中...", font_size=20, color=Colors.GRAY)
        scenario.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(scenario))
        
        warning_text = Text(
            "误差可能被一步步放大, 最终导致结果严重偏离预期!",
            font_size=18, color=Colors.WARNING
        )
        warning_text.next_to(scenario, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(warning_text))
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(scenario), FadeOut(warning_text), run_time=0.5)
        
        # NaN 和 Inf
        section_title = Text("特殊值: NaN 和 Inf", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        nan_info = VGroup(
            Text("NaN (不是一个数字): ", font_size=20, color=Colors.SECONDARY),
            MathTex(r"\sqrt{-1}", font_size=24, color=Colors.TEXT),
            Text(", 0/0 等非法运算", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        nan_info.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(nan_info))
        
        inf_info = VGroup(
            Text("Inf (无穷大): ", font_size=20, color=Colors.WARNING),
            Text("1/0, 超出最大范围等", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        inf_info.next_to(nan_info, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(inf_info))
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(nan_info), FadeOut(inf_info), run_time=0.5)
        
        # 程序员提示
        section_title = Text("程序员必须警惕的陷阱", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        warnings = VGroup(
            Text("1. 不要用 == 比较浮点数", font_size=20, color=Colors.TEXT),
            Text("2. 注意整数溢出", font_size=20, color=Colors.TEXT),
            Text("3. 处理 NaN 和 Inf 的边界情况", font_size=20, color=Colors.TEXT),
            Text("4. 金融计算使用专用的十进制类型", font_size=20, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        warnings.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for w in warnings:
            self.play(FadeIn(w, shift=RIGHT * 0.2), run_time=0.35)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(warnings), run_time=0.5)
    
    # ========================================================================
    # Scene 6: 总结
    # ========================================================================
    def scene_06_summary(self):
        """总结与启示"""
        # 核心要点
        section_title = Text("核心要点", font_size=28, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        points = VGroup()
        
        p1 = create_key_point_card(
            "进制是基础",
            "二进制和十六进制是理解计算机的钥匙",
            color=Colors.PRIMARY, width=5.5, height=1.2
        )
        points.add(p1)
        
        p2 = create_key_point_card(
            "整数: 精确但有限",
            "范围内精确存储, 但要警惕溢出",
            color=Colors.ACCENT, width=5.5, height=1.2
        )
        points.add(p2)
        
        p3 = create_key_point_card(
            "浮点数: 近似存储",
            "因内存限制存在固有误差",
            color=Colors.SECONDARY, width=5.5, height=1.2
        )
        points.add(p3)
        
        points.arrange(DOWN, buff=0.25)
        points.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(points), run_time=0.5)
        
        # 最终寄语
        section_title = Text("启示", font_size=28, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        messages = VGroup(
            Text("▸ 选择合适的数据类型", font_size=20, color=Colors.TEXT),
            Text("▸ 警惕溢出和精度问题", font_size=20, color=Colors.TEXT),
            Text("▸ 在精度、范围和内存消耗之间做权衡", font_size=20, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        messages.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for m in messages:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.4)
        
        final_thought = VGroup(
            Text("在编程世界里", font_size=22, color=Colors.GRAY),
            Text("数学概念必须与物理硬件相结合", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15)
        final_thought.next_to(messages, DOWN, buff=0.6).set_x(0)
        
        box = SurroundingRectangle(final_thought, color=Colors.ACCENT, buff=0.2, corner_radius=0.1)
        
        self.play(FadeIn(final_thought), Create(box))
        
        end_message = Text(
            "理解原理, 编写健壮的代码!",
            font_size=26, color=Colors.PRIMARY
        )
        end_message.next_to(box, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(end_message), run_time=0.8)
        self.play(end_message.animate.scale(1.05), rate_func=there_and_back, run_time=0.5)
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(messages),
            FadeOut(final_thought), FadeOut(box), FadeOut(end_message),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令:
    # manim -pql all_scenes.py ComputersAndNumbers
    pass
