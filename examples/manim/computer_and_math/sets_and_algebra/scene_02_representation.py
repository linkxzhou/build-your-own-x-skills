"""
Scene 2: 集合的表示方法
介绍列举法和描述法，引入重要数集
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


def create_set_box(width=4, height=2.5, label="S", color=None):
    """创建集合容器"""
    stroke_color = color if color else Colors.PRIMARY
    box = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.3,
        fill_color=Colors.BG,
        fill_opacity=0.3,
        stroke_color=stroke_color,
        stroke_width=3
    )
    
    label_text = MathTex(label, font_size=28, color=stroke_color)
    label_text.next_to(box, UP, buff=0.2)
    
    return VGroup(box, label_text)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene02Representation(Scene):
    """Scene 2: 集合的表示方法"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_enumeration()
        self.section_set_builder()
        self.section_number_sets()
        
        clear_scene(self)
    
    def section_enumeration(self):
        """列举法"""
        # 小节标题
        section_title = Text("列举法 - 逐一列出元素", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 说明
        desc = Text("直接写出集合中的所有元素", font_size=20, color=Colors.GRAY)
        desc.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(desc))
        
        # 示例
        examples = VGroup(
            VGroup(
                Text("数字集合: ", font_size=18, color=Colors.TEXT),
                MathTex(r"A = \{1, 2, 3, 4, 5\}", font_size=28, color=Colors.PRIMARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("字母集合: ", font_size=18, color=Colors.TEXT),
                MathTex(r"B = \{a, b, c\}", font_size=28, color=Colors.SECONDARY),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("混合集合: ", font_size=18, color=Colors.TEXT),
                MathTex(r"C = \{1, x, \triangle\}", font_size=28, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        examples.next_to(desc, DOWN, buff=0.5).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        
        # 基数强调
        cardinality = VGroup(
            Text("基数:", font_size=18, color=Colors.TEXT),
            MathTex(r"|A| = 5", font_size=24, color=Colors.PRIMARY),
            Text(",", font_size=18, color=Colors.TEXT),
            MathTex(r"|B| = 3", font_size=24, color=Colors.SECONDARY),
            Text(",", font_size=18, color=Colors.TEXT),
            MathTex(r"|C| = 3", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.15)
        cardinality.next_to(examples, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(cardinality))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(desc),
            FadeOut(examples),
            FadeOut(cardinality),
            run_time=0.5
        )
    
    def section_set_builder(self):
        """描述法 (集合构建器)"""
        # 小节标题
        section_title = Text("描述法 - 用条件定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 说明
        desc = Text("描述元素必须满足的条件", font_size=20, color=Colors.GRAY)
        desc.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(desc))
        
        # 格式
        format_text = VGroup(
            Text("格式: ", font_size=18, color=Colors.TEXT),
            MathTex(r"\{x \mid P(x)\}", font_size=32, color=Colors.PRIMARY),
            Text(' 读作 "满足条件 P(x) 的所有 x"', font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.15)
        format_text.next_to(desc, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(format_text))
        self.wait(0.5)
        
        # 示例1: 偶数
        example1_label = Text("例1: 小于20的正偶数", font_size=18, color=Colors.TEXT)
        example1_label.next_to(format_text, DOWN, buff=0.5).align_to(format_text, LEFT)
        
        example1_set = MathTex(
            r"A = \{x \mid x \in \mathbb{Z}^+, x < 20, x \text{ mod } 2 = 0\}",
            font_size=24, color=Colors.SECONDARY
        )
        example1_set.next_to(example1_label, DOWN, buff=0.2).set_x(0)
        
        example1_result = VGroup(
            Text("= ", font_size=18, color=Colors.TEXT),
            MathTex(r"\{2, 4, 6, 8, 10, 12, 14, 16, 18\}", font_size=22, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        example1_result.next_to(example1_set, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(example1_label))
        self.play(Write(example1_set), run_time=1)
        self.play(FadeIn(example1_result))
        self.wait(0.5)
        
        # 程序员视角
        programmer_note = VGroup(
            Text("程序员视角: ", font_size=16, color=Colors.ACCENT),
            Text("[x for x in range(1, 20) if x % 2 == 0]", 
                 font_size=14, color=Colors.ACCENT, font="Courier New"),
        ).arrange(RIGHT, buff=0.1)
        programmer_note.next_to(example1_result, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(programmer_note))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(desc),
            FadeOut(format_text),
            FadeOut(example1_label),
            FadeOut(example1_set),
            FadeOut(example1_result),
            FadeOut(programmer_note),
            run_time=0.5
        )
    
    def section_number_sets(self):
        """重要数集的包含关系"""
        # 小节标题
        section_title = Text("重要数集", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.3)
        
        # 创建嵌套椭圆表示数集
        # C > R > Q > Z > N
        sets_data = [
            ("C", "复数", 5.5, 3.0, "#9B59B6"),
            ("R", "实数", 4.4, 2.4, "#E74C3C"),
            ("Q", "有理数", 3.3, 1.8, "#F39C12"),
            ("Z", "整数", 2.2, 1.2, "#3498DB"),
            ("N", "自然数", 1.1, 0.6, "#2ECC71"),
        ]
        
        ellipses = VGroup()
        labels = VGroup()
        
        center = DOWN * 0.8
        
        for symbol, name, width, height, color in sets_data:
            ellipse = Ellipse(width=width, height=height)
            ellipse.set_stroke(color, width=2)
            ellipse.set_fill(color, opacity=0.1)
            ellipse.move_to(center)
            ellipses.add(ellipse)
            
            # 标签放在椭圆右侧
            label = MathTex(r"\mathbb{" + symbol + "}", font_size=24, color=color)
            label.next_to(ellipse, RIGHT, buff=0.15)
            labels.add(label)
        
        # 逐个显示
        for i, (ellipse, label) in enumerate(zip(ellipses, labels)):
            self.play(
                Create(ellipse),
                FadeIn(label),
                run_time=0.5
            )
            self.wait(0.2)
        
        self.wait(0.5)
        
        # 包含关系符号
        inclusion = MathTex(
            r"\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}",
            font_size=28, color=Colors.PRIMARY
        )
        inclusion.to_edge(DOWN, buff=0.8).set_x(0)
        
        self.play(Write(inclusion))
        self.wait(0.5)
        
        # 说明
        explanations = VGroup(
            VGroup(
                MathTex(r"\mathbb{N}", font_size=18, color="#2ECC71"),
                Text(": 0, 1, 2, 3...", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\mathbb{Z}", font_size=18, color="#3498DB"),
                Text(": ...-2, -1, 0, 1, 2...", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\mathbb{Q}", font_size=18, color="#F39C12"),
                Text(": 分数, 如 1/2", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\mathbb{R}", font_size=18, color="#E74C3C"),
                Text(": 包含无理数, 如 π", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"\mathbb{C}", font_size=18, color="#9B59B6"),
                Text(": 包含虚数, 如 i", font_size=14, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanations.to_edge(LEFT, buff=0.5).shift(DOWN * 0.5)
        
        self.play(FadeIn(explanations, shift=RIGHT * 0.2))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_02_representation.py Scene02Representation
    pass
