"""
Scene 1: 开场引入 - 集合的概念
通过生活化比喻引入集合概念，建立直觉
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    SET_A = "#E74C3C"        # 集合A颜色
    SET_B = "#3498DB"        # 集合B颜色
    INTERSECTION = "#9B59B6" # 交集颜色
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_element_circle(value, color=Colors.PRIMARY, radius=0.3):
    """创建一个元素圆圈"""
    circle = Circle(radius=radius)
    circle.set_fill(color, opacity=0.7)
    circle.set_stroke(Colors.TEXT, width=2)
    
    text = Text(str(value), font_size=int(radius * 60), color=Colors.TEXT)
    text.move_to(circle.get_center())
    
    return VGroup(circle, text)


def create_set_box(width=4, height=2.5, label="S"):
    """创建集合容器（收纳盒）"""
    box = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.3,
        fill_color=Colors.BG,
        fill_opacity=0.3,
        stroke_color=Colors.PRIMARY,
        stroke_width=3
    )
    
    label_text = MathTex(label, font_size=28, color=Colors.PRIMARY)
    label_text.next_to(box, UP, buff=0.2)
    
    return VGroup(box, label_text)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene01Intro(Scene):
    """Scene 1: 开场引入 - 集合的概念"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        self.section_opening()
        self.section_set_concept()
        self.section_set_notation()
        
        clear_scene(self)
    
    def section_opening(self):
        """开场动画"""
        # 大标题
        main_title = Text("集合与抽象代数", font_size=48, color=Colors.PRIMARY)
        subtitle = Text("从基础到无限", font_size=28, color=Colors.GRAY)
        
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
    
    def section_set_concept(self):
        """集合概念介绍"""
        # 小节标题
        section_title = Text("集合 - 万物的基础", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 收纳盒比喻
        metaphor = Text(
            "你可以把集合想象成一个'收纳盒'",
            font_size=22, color=Colors.GRAY
        )
        metaphor.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(metaphor))
        self.wait(0.5)
        
        # 创建收纳盒
        box = create_set_box(width=5, height=3, label="S")
        box.next_to(metaphor, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(box), run_time=0.8)
        self.wait(0.3)
        
        # 元素逐个进入
        elements = [1, 2, 5]
        element_circles = VGroup()
        
        for i, val in enumerate(elements):
            elem = create_element_circle(val, color=Colors.SECONDARY)
            # 从屏幕外进入
            elem.move_to(box[0].get_top() + UP * 1.5)
            element_circles.add(elem)
        
        # 最终位置
        final_positions = [
            box[0].get_center() + LEFT * 1.2,
            box[0].get_center(),
            box[0].get_center() + RIGHT * 1.2,
        ]
        
        for i, (elem, pos) in enumerate(zip(element_circles, final_positions)):
            self.play(
                elem.animate.move_to(pos),
                run_time=0.5
            )
            self.wait(0.2)
        
        self.wait(0.5)
        
        # 说明文字
        properties = VGroup(
            Text("• 确定的元素", font_size=18, color=Colors.TEXT),
            Text("• 互不相同", font_size=18, color=Colors.TEXT),
            Text("• 可以是数字、字母、甚至其他集合", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        properties.next_to(box, DOWN, buff=0.4).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.3)
        
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(metaphor),
            FadeOut(box),
            FadeOut(element_circles),
            FadeOut(properties),
            run_time=0.5
        )
    
    def section_set_notation(self):
        """集合符号表示"""
        # 小节标题
        section_title = Text("数学符号表示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 花括号表示
        notation_intro = Text("用花括号 { } 包围元素:", font_size=20, color=Colors.GRAY)
        notation_intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(notation_intro))
        
        # 集合表达式
        set_expr = MathTex(r"S = \{1, 2, 5\}", font_size=36, color=Colors.PRIMARY)
        set_expr.next_to(notation_intro, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(set_expr), run_time=1)
        self.wait(0.5)
        
        # 基数说明
        cardinality_text = VGroup(
            Text("基数 (元素个数): ", font_size=20, color=Colors.TEXT),
            MathTex(r"|S| = 3", font_size=28, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        cardinality_text.next_to(set_expr, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(cardinality_text))
        self.wait(0.5)
        
        # 元素符号
        element_notation = VGroup(
            Text("元素属于集合: ", font_size=20, color=Colors.TEXT),
            MathTex(r"1 \in S", font_size=28, color=Colors.SECONDARY),
            Text(", ", font_size=20, color=Colors.TEXT),
            MathTex(r"4 \notin S", font_size=28, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        element_notation.next_to(cardinality_text, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(element_notation))
        self.wait(1)
        
        # 关键点
        key_point = VGroup(
            Text("集合中", font_size=20, color=Colors.TEXT),
            Text("元素无序", font_size=20, color=Colors.SECONDARY),
            Text("且", font_size=20, color=Colors.TEXT),
            Text("不重复", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        key_point.next_to(element_notation, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_point))
        
        # 等价说明
        equivalence = MathTex(
            r"\{1, 2, 5\} = \{5, 1, 2\} = \{1, 1, 2, 5\}",
            font_size=24, color=Colors.GRAY
        )
        equivalence.next_to(key_point, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(equivalence))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_01_intro.py Scene01Intro
    pass
