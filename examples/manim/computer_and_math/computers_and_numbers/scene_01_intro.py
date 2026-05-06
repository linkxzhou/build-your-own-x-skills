"""
Scene 1: 开场引入 - 计算机的二进制世界
通过一个惊人的计算"错误"引发好奇，引出计算机的二进制本质
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


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_binary_digit(value, size=0.6):
    """创建一个二进制位的可视化"""
    bg_color = Colors.BINARY_1 if value == 1 else Colors.BINARY_0
    
    square = Square(side_length=size)
    square.set_fill(bg_color, opacity=0.8)
    square.set_stroke(Colors.PRIMARY, width=2)
    
    digit = Text(str(value), font_size=int(size * 40), color=WHITE)
    digit.move_to(square.get_center())
    
    return VGroup(square, digit)


def create_lightbulb(is_on=False, size=0.8):
    """创建一个灯泡图形"""
    # 灯泡主体
    bulb = Circle(radius=size * 0.4)
    bulb.set_stroke(Colors.PRIMARY, width=2)
    
    # 灯座
    base_width = size * 0.3
    base_height = size * 0.2
    base = Rectangle(width=base_width, height=base_height)
    base.set_stroke(Colors.PRIMARY, width=2)
    base.set_fill(Colors.GRAY, opacity=0.5)
    base.next_to(bulb, DOWN, buff=0)
    
    if is_on:
        bulb.set_fill(Colors.BINARY_1, opacity=0.9)
        # 发光效果
        glow = Circle(radius=size * 0.6)
        glow.set_fill(Colors.BINARY_1, opacity=0.2)
        glow.set_stroke(width=0)
        glow.move_to(bulb.get_center())
        return VGroup(glow, bulb, base)
    else:
        bulb.set_fill(Colors.BINARY_0, opacity=0.5)
        return VGroup(bulb, base)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene01Intro(Scene):
    """Scene 1: 开场引入"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        self.section_opening()
        self.section_mystery_code()
        self.section_binary_world()
        self.section_lightbulb_demo()
        
        clear_scene(self)
    
    def section_opening(self):
        """开场动画"""
        # 大标题
        main_title = Text("计算机与数字", font_size=48, color=Colors.PRIMARY)
        subtitle = Text("二进制的奥秘", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        # 转换为章节标题
        self.play(
            FadeOut(subtitle),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.5)
    
    def section_mystery_code(self):
        """展示神秘的计算结果"""
        # 问题标题
        question = Text("一个奇怪的现象...", font_size=28, color=Colors.TEXT)
        question.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(question, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 代码框
        code_bg = RoundedRectangle(
            width=8, height=2.5,
            corner_radius=0.2,
            fill_color="#0d1117",
            fill_opacity=0.9,
            stroke_color=Colors.PRIMARY,
            stroke_width=2
        )
        code_bg.next_to(question, DOWN, buff=0.5).set_x(0)
        
        # Python 代码
        code_text = VGroup(
            Text(">>> 0.1 + 0.2", font_size=22, color=Colors.ACCENT, font="Menlo"),
        )
        code_text.move_to(code_bg.get_center() + UP * 0.4)
        
        self.play(FadeIn(code_bg), run_time=0.3)
        self.play(Write(code_text), run_time=0.8)
        self.wait(0.5)
        
        # 预期结果
        expected = Text("我们期望的结果: 0.3", font_size=20, color=Colors.GRAY)
        expected.next_to(code_bg, DOWN, buff=0.3).set_x(0)
        self.play(FadeIn(expected))
        self.wait(0.3)
        
        # 实际结果（惊人的）
        result_text = Text(
            "0.30000000000000004",
            font_size=22, color=Colors.SECONDARY, font="Menlo"
        )
        result_text.move_to(code_bg.get_center() + DOWN * 0.3)
        
        self.play(Write(result_text), run_time=0.8)
        self.wait(0.3)
        
        # 惊叹效果
        surprise = Text("???", font_size=36, color=Colors.SECONDARY)
        surprise.next_to(code_bg, RIGHT, buff=0.5)
        
        self.play(
            FadeIn(surprise, scale=1.5),
            Flash(result_text, color=Colors.SECONDARY, line_length=0.3),
            run_time=0.5
        )
        self.wait(1)
        
        # 问题
        big_question = Text(
            "计算机真的会算错吗?",
            font_size=32,
            color=Colors.TEXT
        )
        big_question.next_to(expected, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeOut(expected),
            FadeOut(surprise),
            Write(big_question),
            run_time=0.8
        )
        self.wait(1.5)
        
        # 清除这部分
        self.play(
            FadeOut(question),
            FadeOut(code_bg),
            FadeOut(code_text),
            FadeOut(result_text),
            FadeOut(big_question),
            run_time=0.5
        )
    
    def section_binary_world(self):
        """揭示二进制世界"""
        # 答案揭晓
        answer_title = Text("答案是...", font_size=28, color=Colors.TEXT)
        answer_title.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(answer_title))
        self.wait(0.5)
        
        # 核心概念
        core_concept = VGroup(
            Text("计算机只认识", font_size=32, color=Colors.TEXT),
            Text("0 和 1", font_size=48, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.2)
        core_concept.next_to(answer_title, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeIn(core_concept[0]),
            run_time=0.5
        )
        self.play(
            Write(core_concept[1]),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 二进制数字流动画
        binary_stream = VGroup()
        for i in range(16):
            digit = create_binary_digit(i % 2, size=0.5)
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
        
        # 解释文字
        explain = Text(
            "这就是 '二进制' - 计算机的母语",
            font_size=24,
            color=Colors.GRAY
        )
        explain.next_to(binary_stream, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(explain, shift=UP * 0.2))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(answer_title),
            FadeOut(core_concept),
            FadeOut(binary_stream),
            FadeOut(explain),
            run_time=0.5
        )
    
    def section_lightbulb_demo(self):
        """灯泡演示二进制"""
        # 标题
        demo_title = Text("开关 = 二进制位", font_size=28, color=Colors.TEXT)
        demo_title.next_to(self.chapter_title, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(demo_title))
        self.wait(0.3)
        
        # 创建灯泡组
        bulb_off = create_lightbulb(is_on=False, size=1.2)
        bulb_on = create_lightbulb(is_on=True, size=1.2)
        
        bulbs = VGroup(bulb_off, bulb_on).arrange(RIGHT, buff=2)
        bulbs.next_to(demo_title, DOWN, buff=0.8).set_x(0)
        
        # 标签
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
        
        # 显示灯泡
        self.play(FadeIn(bulb_off), FadeIn(bulb_on), run_time=0.5)
        self.play(FadeIn(label_off), FadeIn(label_on), run_time=0.5)
        self.wait(1)
        
        # 切换动画
        # 创建闪烁效果
        for _ in range(2):
            # 关灯
            new_bulb_on = create_lightbulb(is_on=False, size=1.2)
            new_bulb_on.move_to(bulb_on.get_center())
            self.play(
                Transform(bulb_on, new_bulb_on),
                run_time=0.3
            )
            self.wait(0.2)
            
            # 开灯
            new_bulb_on2 = create_lightbulb(is_on=True, size=1.2)
            new_bulb_on2.move_to(bulb_on.get_center())
            self.play(
                Transform(bulb_on, new_bulb_on2),
                run_time=0.3
            )
            self.wait(0.2)
        
        # 总结
        summary = VGroup(
            Text("计算机的一切数据", font_size=24, color=Colors.TEXT),
            Text("都由无数个 0 和 1 组成", font_size=24, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        summary.next_to(VGroup(label_off, label_on), DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_01_intro.py Scene01Intro
    pass
