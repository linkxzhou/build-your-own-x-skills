"""
Scene 6: 总结与启示
总结核心要点，强调对程序员的实际意义
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
    SUCCESS = "#2ECC71"      # 成功绿
    HIGHLIGHT = "#9B59B6"    # 紫色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


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


class Scene06Summary(Scene):
    """Scene 6: 总结与启示"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_key_points()
        self.section_hierarchy()
        self.section_final_message()
        
        clear_scene(self)
    
    def section_key_points(self):
        """核心要点回顾"""
        # 小节标题
        section_title = Text("核心要点", font_size=28, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 三个核心要点
        points = VGroup()
        
        # 要点1: 进制
        p1 = create_key_point_card(
            "进制是基础",
            "二进制和十六进制是理解计算机的钥匙",
            color=Colors.PRIMARY,
            width=5.5, height=1.2
        )
        points.add(p1)
        
        # 要点2: 整数
        p2 = create_key_point_card(
            "整数: 精确但有限",
            "范围内精确存储, 但要警惕溢出",
            color=Colors.ACCENT,
            width=5.5, height=1.2
        )
        points.add(p2)
        
        # 要点3: 浮点数
        p3 = create_key_point_card(
            "浮点数: 近似存储",
            "因内存限制存在固有误差",
            color=Colors.SECONDARY,
            width=5.5, height=1.2
        )
        points.add(p3)
        
        points.arrange(DOWN, buff=0.25)
        points.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for p in points:
            self.play(FadeIn(p, shift=RIGHT * 0.3), run_time=0.5)
        
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(points),
            run_time=0.5
        )
    
    def section_hierarchy(self):
        """层次结构图"""
        # 小节标题
        section_title = Text("知识体系", font_size=28, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 创建层次图
        # 顶层: 计算机数字表示
        top_box = RoundedRectangle(width=4, height=0.7, corner_radius=0.1)
        top_box.set_fill(Colors.PRIMARY, opacity=0.3)
        top_box.set_stroke(Colors.PRIMARY, width=2)
        top_text = Text("计算机数字表示", font_size=16, color=Colors.TEXT)
        top_text.move_to(top_box.get_center())
        top = VGroup(top_box, top_text)
        
        # 中层: 整数 和 浮点数
        mid_boxes = VGroup()
        
        int_box = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.1)
        int_box.set_fill(Colors.ACCENT, opacity=0.3)
        int_box.set_stroke(Colors.ACCENT, width=2)
        int_text = Text("整数", font_size=14, color=Colors.TEXT)
        int_text.move_to(int_box.get_center())
        int_group = VGroup(int_box, int_text)
        
        float_box = RoundedRectangle(width=2.5, height=0.6, corner_radius=0.1)
        float_box.set_fill(Colors.SECONDARY, opacity=0.3)
        float_box.set_stroke(Colors.SECONDARY, width=2)
        float_text = Text("浮点数", font_size=14, color=Colors.TEXT)
        float_text.move_to(float_box.get_center())
        float_group = VGroup(float_box, float_text)
        
        mid_boxes = VGroup(int_group, float_group).arrange(RIGHT, buff=1)
        
        # 底层: 二进制
        bottom_box = RoundedRectangle(width=4, height=0.6, corner_radius=0.1)
        bottom_box.set_fill(Colors.HIGHLIGHT, opacity=0.3)
        bottom_box.set_stroke(Colors.HIGHLIGHT, width=2)
        bottom_text = Text("二进制 (0和1)", font_size=14, color=Colors.TEXT)
        bottom_text.move_to(bottom_box.get_center())
        bottom = VGroup(bottom_box, bottom_text)
        
        # 排列
        hierarchy = VGroup(top, mid_boxes, bottom).arrange(DOWN, buff=0.5)
        hierarchy.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 连线
        lines = VGroup()
        
        # 从顶部到中间层
        line1 = Arrow(
            top_box.get_bottom(),
            int_box.get_top(),
            color=Colors.GRAY, buff=0.1,
            stroke_width=2
        )
        line2 = Arrow(
            top_box.get_bottom(),
            float_box.get_top(),
            color=Colors.GRAY, buff=0.1,
            stroke_width=2
        )
        lines.add(line1, line2)
        
        # 从中间层到底部
        line3 = Arrow(
            int_box.get_bottom(),
            bottom_box.get_top() + LEFT * 0.5,
            color=Colors.GRAY, buff=0.1,
            stroke_width=2
        )
        line4 = Arrow(
            float_box.get_bottom(),
            bottom_box.get_top() + RIGHT * 0.5,
            color=Colors.GRAY, buff=0.1,
            stroke_width=2
        )
        lines.add(line3, line4)
        
        # 动画显示
        self.play(FadeIn(bottom), run_time=0.4)
        self.wait(0.2)
        self.play(FadeIn(mid_boxes), Create(line3), Create(line4), run_time=0.5)
        self.wait(0.2)
        self.play(FadeIn(top), Create(line1), Create(line2), run_time=0.5)
        self.wait(1)
        
        # 标注
        foundation = Text("基础", font_size=14, color=Colors.HIGHLIGHT)
        foundation.next_to(bottom, LEFT, buff=0.3)
        
        application = Text("应用", font_size=14, color=Colors.PRIMARY)
        application.next_to(top, LEFT, buff=0.3)
        
        self.play(FadeIn(foundation), FadeIn(application))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(hierarchy),
            FadeOut(lines),
            FadeOut(foundation),
            FadeOut(application),
            run_time=0.5
        )
    
    def section_final_message(self):
        """最终寄语"""
        # 小节标题
        section_title = Text("启示", font_size=28, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 核心信息
        messages = VGroup()
        
        m1 = VGroup(
            Text("▸ ", font_size=20, color=Colors.PRIMARY),
            Text("选择合适的数据类型", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        messages.add(m1)
        
        m2 = VGroup(
            Text("▸ ", font_size=20, color=Colors.PRIMARY),
            Text("警惕溢出和精度问题", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        messages.add(m2)
        
        m3 = VGroup(
            Text("▸ ", font_size=20, color=Colors.PRIMARY),
            Text("在精度、范围和内存消耗之间做权衡", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        messages.add(m3)
        
        messages.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        messages.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for m in messages:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(0.5)
        
        # 升华
        final_thought = VGroup(
            Text("在编程世界里", font_size=22, color=Colors.GRAY),
            Text("数学概念必须与物理硬件相结合", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15)
        final_thought.next_to(messages, DOWN, buff=0.6).set_x(0)
        
        box = SurroundingRectangle(
            final_thought, color=Colors.ACCENT, buff=0.2,
            corner_radius=0.1, stroke_width=2
        )
        
        self.play(FadeIn(final_thought), Create(box))
        self.wait(1)
        
        # 结尾
        end_message = Text(
            "理解原理, 编写健壮的代码!",
            font_size=26, color=Colors.PRIMARY
        )
        end_message.next_to(box, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(end_message), run_time=0.8)
        
        # 闪烁效果
        self.play(
            end_message.animate.scale(1.05),
            rate_func=there_and_back,
            run_time=0.5
        )
        
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_06_summary.py Scene06Summary
    pass
