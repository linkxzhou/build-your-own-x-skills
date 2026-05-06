"""
Scene 5: 计算中的奇怪情况 - 误差与特殊值
介绍舍入误差累积和特殊值 NaN、Inf
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
    WARNING = "#F39C12"      # 警告橙
    DANGER = "#E74C3C"       # 危险红


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_warning_box(content, title_text="⚠️ 警告"):
    """创建警告框"""
    title = Text(title_text, font_size=20, color=Colors.WARNING)
    body = content
    
    group = VGroup(title, body).arrange(DOWN, buff=0.2)
    
    box = SurroundingRectangle(
        group, color=Colors.WARNING, buff=0.2,
        corner_radius=0.1, stroke_width=2
    )
    box.set_fill(Colors.WARNING, opacity=0.1)
    
    return VGroup(box, group)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene05SpecialCases(Scene):
    """Scene 5: 特殊情况"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_error_accumulation()
        self.section_special_values()
        self.section_programmer_tips()
        
        clear_scene(self)
    
    def section_error_accumulation(self):
        """误差累积"""
        # 小节标题
        section_title = Text("舍入误差累积: 小误差, 大问题", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 场景描述
        scenario = Text(
            "在复杂的科学计算中...",
            font_size=20, color=Colors.GRAY
        )
        scenario.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(scenario))
        self.wait(0.3)
        
        # 误差放大示意图
        # 创建一个误差增长的折线图
        axes = Axes(
            x_range=[0, 6, 1],
            y_range=[0, 100, 20],
            x_length=6,
            y_length=3,
            axis_config={
                "color": Colors.GRAY,
                "include_numbers": False,
            }
        )
        axes.next_to(scenario, DOWN, buff=0.5).set_x(0)
        
        # X轴标签
        x_label = Text("计算步骤", font_size=14, color=Colors.GRAY)
        x_label.next_to(axes, DOWN, buff=0.2)
        
        # Y轴标签
        y_label = Text("误差", font_size=14, color=Colors.GRAY)
        y_label.next_to(axes, LEFT, buff=0.2).rotate(90 * DEGREES)
        
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
        
        # 误差增长曲线 (指数增长)
        error_graph = axes.plot(
            lambda x: 0.5 * (2 ** x),
            x_range=[0, 5.5],
            color=Colors.SECONDARY
        )
        
        self.play(Create(error_graph), run_time=1.5)
        
        # 添加标注
        tiny_dot = Dot(axes.c2p(1, 1), color=Colors.ACCENT, radius=0.08)
        tiny_label = Text("微小误差", font_size=12, color=Colors.ACCENT)
        tiny_label.next_to(tiny_dot, UP, buff=0.1)
        
        big_dot = Dot(axes.c2p(5, 16), color=Colors.DANGER, radius=0.12)
        big_label = Text("严重偏差!", font_size=14, color=Colors.DANGER)
        big_label.next_to(big_dot, UP, buff=0.1)
        
        self.play(FadeIn(tiny_dot), FadeIn(tiny_label))
        self.wait(0.3)
        self.play(FadeIn(big_dot), FadeIn(big_label))
        self.wait(0.5)
        
        # 警告
        warning_text = Text(
            "误差可能被一步步放大, 最终导致结果严重偏离预期!",
            font_size=18, color=Colors.WARNING
        )
        warning_text.next_to(axes, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(warning_text))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(scenario),
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(error_graph),
            FadeOut(tiny_dot),
            FadeOut(tiny_label),
            FadeOut(big_dot),
            FadeOut(big_label),
            FadeOut(warning_text),
            run_time=0.5
        )
    
    def section_special_values(self):
        """特殊值 NaN 和 Inf"""
        # 小节标题
        section_title = Text("特殊值: NaN 和 Inf", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # NaN 部分
        nan_title = Text("NaN - Not a Number (不是一个数字)", font_size=20, color=Colors.SECONDARY)
        nan_title.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(nan_title))
        self.wait(0.3)
        
        nan_desc = Text("由非法运算产生:", font_size=18, color=Colors.GRAY)
        nan_desc.next_to(nan_title, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(nan_desc))
        
        # NaN 例子
        nan_examples = VGroup(
            MathTex(r"\sqrt{-1} = \textrm{NaN}", font_size=24, color=Colors.TEXT),
            MathTex(r"0 / 0 = \textrm{NaN}", font_size=24, color=Colors.TEXT),
            MathTex(r"\infty - \infty = \textrm{NaN}", font_size=24, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        nan_examples.next_to(nan_desc, DOWN, buff=0.3).set_x(0)
        
        for ex in nan_examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.35)
        
        self.wait(0.8)
        
        # 淡出 NaN 部分
        self.play(
            FadeOut(nan_title),
            FadeOut(nan_desc),
            FadeOut(nan_examples),
            run_time=0.4
        )
        
        # Inf 部分
        inf_title = Text("Inf - Infinity (无穷大)", font_size=20, color=Colors.WARNING)
        inf_title.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(inf_title))
        self.wait(0.3)
        
        inf_desc = Text("当计算结果超出可表示的最大范围时出现:", font_size=18, color=Colors.GRAY)
        inf_desc.next_to(inf_title, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(inf_desc))
        
        # Inf 例子
        inf_examples = VGroup(
            MathTex(r"1 / 0 = +\infty", font_size=24, color=Colors.TEXT),
            MathTex(r"10^{1000} = +\infty", font_size=24, color=Colors.TEXT),
            MathTex(r"-1 / 0 = -\infty", font_size=24, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        inf_examples.next_to(inf_desc, DOWN, buff=0.3).set_x(0)
        
        for ex in inf_examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.35)
        
        self.wait(0.8)
        
        # 提示
        tip = VGroup(
            Text("提示: ", font_size=18, color=Colors.ACCENT),
            Text("这些特殊值会在后续计算中'传染'", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        tip.next_to(inf_examples, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(tip))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(inf_title),
            FadeOut(inf_desc),
            FadeOut(inf_examples),
            FadeOut(tip),
            run_time=0.5
        )
    
    def section_programmer_tips(self):
        """程序员提示"""
        # 小节标题
        section_title = Text("程序员必须警惕的陷阱", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 警示列表
        warnings = VGroup()
        
        # 警示1
        w1 = VGroup(
            Text("1. ", font_size=20, color=Colors.WARNING),
            Text("不要用 == 比较浮点数", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        warnings.add(w1)
        
        # 代码示例
        code1_bad = Text(
            "if (a == 0.3):  # 危险!",
            font_size=16, color=Colors.SECONDARY, font="Menlo"
        )
        code1_good = Text(
            "if (abs(a - 0.3) < 0.0001):  # 安全",
            font_size=16, color=Colors.ACCENT, font="Menlo"
        )
        code1 = VGroup(code1_bad, code1_good).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        code1.shift(RIGHT * 0.5)
        warnings.add(code1)
        
        # 警示2
        w2 = VGroup(
            Text("2. ", font_size=20, color=Colors.WARNING),
            Text("注意整数溢出", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        warnings.add(w2)
        
        # 警示3
        w3 = VGroup(
            Text("3. ", font_size=20, color=Colors.WARNING),
            Text("处理 NaN 和 Inf 的边界情况", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        warnings.add(w3)
        
        # 警示4
        w4 = VGroup(
            Text("4. ", font_size=20, color=Colors.WARNING),
            Text("金融计算使用专用的十进制类型", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        warnings.add(w4)
        
        warnings.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        warnings.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for w in warnings:
            self.play(FadeIn(w, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(1)
        
        # 总结框
        summary = VGroup(
            Text("理解这些原理", font_size=20, color=Colors.TEXT),
            Text("才能编写出正确、健壮的代码!", font_size=20, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.1)
        summary.next_to(warnings, DOWN, buff=0.5).set_x(0)
        
        box = SurroundingRectangle(summary, color=Colors.PRIMARY, buff=0.2, corner_radius=0.1)
        
        self.play(FadeIn(summary), Create(box))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_05_special_cases.py Scene05SpecialCases
    pass
