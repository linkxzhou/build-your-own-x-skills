"""
Scene 1: 布尔代数引入
通过"开关"比喻引入布尔代数概念，建立直觉
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
    ZERO = "#2C3E50"         # 0的颜色（深蓝灰）
    ONE = "#F39C12"          # 1的颜色（金橙）
    AND_COLOR = "#E74C3C"    # AND颜色
    OR_COLOR = "#3498DB"     # OR颜色
    NOT_COLOR = "#9B59B6"    # NOT颜色
    XOR_COLOR = "#2ECC71"    # XOR颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_switch(is_on=False, size=1.0):
    """创建一个开关"""
    # 开关底座
    base = RoundedRectangle(
        width=size * 1.5, height=size * 0.8,
        corner_radius=size * 0.4,
        fill_color=Colors.ONE if is_on else Colors.ZERO,
        fill_opacity=0.8,
        stroke_color=Colors.PRIMARY,
        stroke_width=2
    )
    
    # 开关滑块
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
    # 灯泡主体
    bulb = Circle(radius=size * 0.4)
    bulb.set_stroke(Colors.PRIMARY, width=2)
    if is_on:
        bulb.set_fill(Colors.ONE, opacity=0.9)
    else:
        bulb.set_fill(Colors.ZERO, opacity=0.5)
    
    # 灯座
    base_rect = Rectangle(width=size * 0.3, height=size * 0.2)
    base_rect.set_stroke(Colors.PRIMARY, width=2)
    base_rect.set_fill(Colors.GRAY, opacity=0.5)
    base_rect.next_to(bulb, DOWN, buff=0)
    
    # 光芒（仅当开启时）
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


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene01Intro(Scene):
    """Scene 1: 布尔代数引入"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        self.section_opening()
        self.section_switch_metaphor()
        self.section_definition()
        self.section_history()
        
        clear_scene(self)
    
    def section_opening(self):
        """开场动画"""
        # 大标题
        main_title = Text("布尔代数", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("真与假的数学", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        # 提出问题
        question = Text(
            "计算机如何用 0 和 1 理解整个世界？",
            font_size=24, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        # 转换为章节标题
        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def section_switch_metaphor(self):
        """开关比喻"""
        # 小节标题
        section_title = Text('"开关数学"', font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建开关和灯泡的对应
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
        
        # 动画展示
        self.play(FadeIn(off_label))
        self.play(
            FadeIn(switch_off),
            FadeIn(bulb_off),
            run_time=0.6
        )
        self.play(
            FadeIn(zero_bit),
            FadeIn(false_text),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        self.play(FadeIn(on_label))
        self.play(
            FadeIn(switch_on),
            FadeIn(bulb_on),
            run_time=0.6
        )
        self.play(
            FadeIn(one_bit),
            FadeIn(true_text),
            run_time=0.5
        )
        
        self.wait(0.5)
        
        # 等价关系
        equiv = VGroup(
            Text("开 = 1 = 真", font_size=20, color=Colors.ONE),
            Text("关 = 0 = 假", font_size=20, color=Colors.ZERO),
        ).arrange(DOWN, buff=0.2)
        equiv.to_edge(RIGHT, buff=1.0).shift(DOWN * 0.5)
        
        box = SurroundingRectangle(equiv, color=Colors.PRIMARY, buff=0.2)
        
        self.play(FadeIn(equiv), Create(box))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(off_group), FadeOut(off_label),
            FadeOut(on_group), FadeOut(on_label),
            FadeOut(equiv), FadeOut(box),
            run_time=0.5
        )
    
    def section_definition(self):
        """布尔代数定义"""
        # 小节标题
        section_title = Text("什么是布尔代数？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("布尔代数是一套关于", font_size=20, color=Colors.GRAY),
            Text('"真与假"', font_size=22, color=Colors.PRIMARY),
            Text("的数学体系", font_size=20, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 核心元素
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
        self.wait(0.5)
        
        # 三种基本运算
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
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(elements_title),
            FadeOut(elements),
            FadeOut(ops_title),
            FadeOut(ops),
            run_time=0.5
        )
    
    def section_history(self):
        """历史背景"""
        # 小节标题
        section_title = Text("历史背景", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 乔治·布尔
        boole_name = Text("乔治·布尔 (George Boole)", font_size=24, color=Colors.PRIMARY)
        boole_name.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(boole_name))
        
        # 年份
        year = Text("1854年", font_size=20, color=Colors.ONE)
        year.next_to(boole_name, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(year))
        
        # 著作
        book = VGroup(
            Text("发表《思维规律的研究》", font_size=18, color=Colors.GRAY),
            Text("(The Laws of Thought)", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        book.next_to(year, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(book))
        self.wait(0.5)
        
        # 意义
        significance = VGroup(
            Text("首次将逻辑推理数学化", font_size=18, color=Colors.TEXT),
            Text("为现代计算机科学奠定基础", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2)
        significance.next_to(book, DOWN, buff=0.5).set_x(0)
        
        for line in significance:
            self.play(FadeIn(line, shift=RIGHT * 0.2), run_time=0.5)
        
        # 时间线
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
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_01_intro.py Scene01Intro
    pass
