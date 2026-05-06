"""
Scene 7: 总结与启示
总结核心概念，强调布尔代数的重要性
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


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_pyramid_layer(text, width, color, height=0.5):
    """创建金字塔层"""
    layer = VGroup()
    
    # 梯形
    trapezoid = Polygon(
        LEFT * width/2 + UP * height/2,
        RIGHT * width/2 + UP * height/2,
        RIGHT * (width/2 - 0.3) + DOWN * height/2,
        LEFT * (width/2 - 0.3) + DOWN * height/2,
        fill_color=color,
        fill_opacity=0.3,
        stroke_color=color,
        stroke_width=2
    )
    
    label = Text(text, font_size=14, color=Colors.TEXT)
    label.move_to(trapezoid.get_center())
    
    layer.add(trapezoid, label)
    return layer


def create_insight_card(title, content, color, width=2.8, height=1.8):
    """创建启示卡片"""
    card = VGroup()
    
    bg = RoundedRectangle(
        corner_radius=0.12,
        width=width,
        height=height,
        fill_color=Colors.BG,
        fill_opacity=0.95,
        stroke_color=color,
        stroke_width=2
    )
    
    title_text = Text(title, font_size=14, color=color)
    title_text.move_to(bg.get_top() + DOWN * 0.3)
    
    content_text = Text(content, font_size=12, color=Colors.TEXT)
    content_text.move_to(bg.get_center() + DOWN * 0.1)
    
    card.add(bg, title_text, content_text)
    return card


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene07Summary(Scene):
    """Scene 7: 总结与启示"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_knowledge_pyramid()
        self.section_three_insights()
        self.section_finale()
        
        clear_scene(self)
    
    def section_knowledge_pyramid(self):
        """知识体系金字塔"""
        section_title = Text("知识体系回顾", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建金字塔
        pyramid = VGroup()
        
        # 从下到上
        layers_data = [
            ("晶体管 (物理基础)", 3.5, Colors.ZERO),
            ("逻辑门 (电路实现)", 3.0, Colors.AND_COLOR),
            ("布尔函数 (逻辑设计)", 2.5, Colors.OR_COLOR),
            ("布尔代数 (抽象数学)", 2.0, Colors.PRIMARY),
        ]
        
        layers = VGroup()
        for text, width, color in layers_data:
            layer = create_pyramid_layer(text, width, color, height=0.6)
            layers.add(layer)
        
        layers.arrange(UP, buff=0.05)
        layers.next_to(section_title, DOWN, buff=0.5).shift(LEFT * 1.5)
        
        # 从底部开始动画
        for i, layer in enumerate(layers):
            self.play(FadeIn(layer, shift=UP * 0.2), run_time=0.4)
        
        # 右侧说明
        explanations = VGroup(
            VGroup(
                Text("抽象层次:", font_size=14, color=Colors.PRIMARY),
            ),
            VGroup(
                Text("• 数学理论", font_size=12, color=Colors.GRAY),
                Text("  ↓ 具体化", font_size=10, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT),
            VGroup(
                Text("• 逻辑表达式", font_size=12, color=Colors.GRAY),
                Text("  ↓ 电路化", font_size=10, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT),
            VGroup(
                Text("• 门级电路", font_size=12, color=Colors.GRAY),
                Text("  ↓ 物理化", font_size=10, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT),
            VGroup(
                Text("• 电子元件", font_size=12, color=Colors.GRAY),
            ),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanations.next_to(layers, RIGHT, buff=0.8)
        
        self.play(FadeIn(explanations))
        
        # 箭头：从抽象到具体
        arrow = Arrow(
            layers.get_top() + UP * 0.2,
            layers.get_bottom() + DOWN * 0.2,
            color=Colors.SECONDARY, stroke_width=3, buff=0
        )
        arrow.next_to(layers, LEFT, buff=0.3)
        
        arrow_label = Text("抽象→具体", font_size=12, color=Colors.SECONDARY)
        arrow_label.next_to(arrow, LEFT, buff=0.1)
        
        self.play(Create(arrow), FadeIn(arrow_label))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(section_title, layers, explanations, arrow, arrow_label)
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_three_insights(self):
        """三个核心启示"""
        section_title = Text("三个核心启示", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三张卡片
        cards = VGroup()
        
        # 启示一：抽象与现实的桥梁
        card1 = VGroup()
        card1_bg = RoundedRectangle(
            width=3.2, height=2.0, corner_radius=0.12,
            fill_color=Colors.BG, fill_opacity=0.95,
            stroke_color=Colors.PRIMARY, stroke_width=2
        )
        card1_title = Text("抽象与现实的桥梁", font_size=14, color=Colors.PRIMARY)
        card1_title.move_to(card1_bg.get_top() + DOWN * 0.3)
        card1_content = VGroup(
            Text("布尔代数证明了：", font_size=11, color=Colors.TEXT),
            Text("纯粹的数学概念", font_size=11, color=Colors.GRAY),
            Text("可以转化为", font_size=11, color=Colors.GRAY),
            Text("实际的电子电路", font_size=11, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.08)
        card1_content.move_to(card1_bg.get_center() + DOWN * 0.15)
        card1.add(card1_bg, card1_title, card1_content)
        
        # 启示二：计算机的逻辑基石
        card2 = VGroup()
        card2_bg = RoundedRectangle(
            width=3.2, height=2.0, corner_radius=0.12,
            fill_color=Colors.BG, fill_opacity=0.95,
            stroke_color=Colors.SECONDARY, stroke_width=2
        )
        card2_title = Text("计算机的逻辑基石", font_size=14, color=Colors.SECONDARY)
        card2_title.move_to(card2_bg.get_top() + DOWN * 0.3)
        card2_content = VGroup(
            Text("所有计算都归结为：", font_size=11, color=Colors.TEXT),
            Text("0和1的", font_size=11, color=Colors.GRAY),
            Text("AND、OR、NOT", font_size=11, color=Colors.AND_COLOR),
            Text("组合运算", font_size=11, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08)
        card2_content.move_to(card2_bg.get_center() + DOWN * 0.15)
        card2.add(card2_bg, card2_title, card2_content)
        
        # 启示三：优化思维的体现
        card3 = VGroup()
        card3_bg = RoundedRectangle(
            width=3.2, height=2.0, corner_radius=0.12,
            fill_color=Colors.BG, fill_opacity=0.95,
            stroke_color=Colors.XOR_COLOR, stroke_width=2
        )
        card3_title = Text("简化与优化的艺术", font_size=14, color=Colors.XOR_COLOR)
        card3_title.move_to(card3_bg.get_top() + DOWN * 0.3)
        card3_content = VGroup(
            Text("布尔代数的定律", font_size=11, color=Colors.TEXT),
            Text("帮助我们简化", font_size=11, color=Colors.GRAY),
            Text("复杂的逻辑表达式", font_size=11, color=Colors.GRAY),
            Text("设计更高效的电路", font_size=11, color=Colors.XOR_COLOR),
        ).arrange(DOWN, buff=0.08)
        card3_content.move_to(card3_bg.get_center() + DOWN * 0.15)
        card3.add(card3_bg, card3_title, card3_content)
        
        cards.add(card1, card2, card3)
        cards.arrange(RIGHT, buff=0.4)
        cards.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=0.5)
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(section_title, cards)
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_finale(self):
        """升华与结语"""
        # 核心金句
        quote = VGroup(
            Text("0 和 1", font_size=40, color=Colors.ONE),
            Text("点亮数字世界", font_size=32, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.3)
        quote.move_to(ORIGIN + UP * 0.5)
        
        self.play(FadeIn(quote, scale=0.8))
        self.wait(1)
        
        # 回顾要点
        recap = VGroup(
            Text("本章要点回顾:", font_size=16, color=Colors.TEXT),
            Text("✓ 布尔代数: 真与假的数学体系", font_size=14, color=Colors.GRAY),
            Text("✓ 三种运算: AND, OR, NOT", font_size=14, color=Colors.GRAY),
            Text("✓ 核心定律: 交换、结合、分配、德摩根", font_size=14, color=Colors.GRAY),
            Text("✓ 逻辑门: 布尔运算的电路实现", font_size=14, color=Colors.GRAY),
            Text("✓ 加法器: 从逻辑到计算的桥梁", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        recap.next_to(quote, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(recap, shift=UP * 0.2))
        self.wait(1)
        
        # 展望
        outlook = VGroup(
            Text("下一站:", font_size=16, color=Colors.SECONDARY),
            Text("了解计算机如何用这些基础构建", font_size=14, color=Colors.GRAY),
            Text("CPU、内存、存储等复杂系统", font_size=14, color=Colors.PRIMARY),
        ).arrange(DOWN, buff=0.1)
        outlook.next_to(recap, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(outlook))
        
        self.wait(1)
        
        # 感谢
        thanks = Text("感谢观看！", font_size=28, color=Colors.SECONDARY)
        thanks.next_to(outlook, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(thanks, scale=0.8))
        
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_07_summary.py Scene07Summary
    pass
