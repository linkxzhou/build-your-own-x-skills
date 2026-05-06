"""
Scene 8: 总结与启示
总结核心要点，强调实际意义
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


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


def create_insight_card(icon, title, description, color, width=5, height=1.4):
    """创建启示卡片"""
    card = RoundedRectangle(
        width=width, height=height,
        corner_radius=0.15,
        fill_color=Colors.BG,
        fill_opacity=0.5,
        stroke_color=color,
        stroke_width=2
    )
    
    # 图标
    icon_text = Text(icon, font_size=28)
    icon_text.move_to(card.get_left() + RIGHT * 0.5)
    
    # 标题
    title_text = Text(title, font_size=16, color=color)
    title_text.next_to(icon_text, RIGHT, buff=0.3)
    
    # 描述
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.next_to(title_text, DOWN, buff=0.1).align_to(title_text, LEFT)
    
    return VGroup(card, icon_text, title_text, desc_text)


class Scene08Summary(Scene):
    """Scene 8: 总结与启示"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_knowledge_map()
        self.section_insights()
        self.section_closing()
        
        clear_scene(self)
    
    def section_knowledge_map(self):
        """知识体系回顾"""
        # 小节标题
        section_title = Text("知识体系回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建思维导图节点
        nodes = [
            ("集合", Colors.PRIMARY, ORIGIN),
            ("表示", Colors.SECONDARY, LEFT * 2.5 + UP * 1),
            ("运算", Colors.SET_A, LEFT * 1 + DOWN * 1.5),
            ("定律", Colors.SET_B, RIGHT * 1 + DOWN * 1.5),
            ("群论", Colors.INTERSECTION, RIGHT * 2.5 + UP * 1),
            ("无限", Colors.ACCENT, RIGHT * 3 + DOWN * 0.5),
        ]
        
        # 创建节点
        node_mobjects = {}
        for name, color, pos in nodes:
            # 节点圆圈
            circle = Circle(radius=0.5)
            circle.set_fill(color, opacity=0.3)
            circle.set_stroke(color, width=2)
            circle.move_to(pos + DOWN * 0.8)
            
            # 文字
            text = Text(name, font_size=14, color=Colors.TEXT)
            text.move_to(circle.get_center())
            
            node_group = VGroup(circle, text)
            node_mobjects[name] = node_group
        
        # 先显示中心节点
        self.play(FadeIn(node_mobjects["集合"]))
        self.wait(0.3)
        
        # 添加连线并显示其他节点
        lines = []
        center = node_mobjects["集合"][0].get_center()
        for name in ["表示", "运算", "定律", "群论"]:
            end = node_mobjects[name][0].get_center()
            line = Line(center, end, color=Colors.GRAY, stroke_width=1.5)
            lines.append(line)
            self.play(Create(line), FadeIn(node_mobjects[name]), run_time=0.4)
        
        # 群论到无限的连线
        group_center = node_mobjects["群论"][0].get_center()
        infinity_center = node_mobjects["无限"][0].get_center()
        line_to_infinity = Line(group_center, infinity_center, color=Colors.GRAY, stroke_width=1.5)
        self.play(Create(line_to_infinity), FadeIn(node_mobjects["无限"]), run_time=0.4)
        lines.append(line_to_infinity)
        
        self.wait(1)
        
        # 路径强调
        path_text = VGroup(
            Text("学习路径: ", font_size=14, color=Colors.TEXT),
            Text("集合 → 运算 → 定律 → 群论 → 无限", font_size=14, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        path_text.to_edge(DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(path_text))
        self.wait(1.5)
        
        # 清除
        all_nodes = list(node_mobjects.values())
        self.play(
            FadeOut(section_title),
            *[FadeOut(node) for node in all_nodes],
            *[FadeOut(line) for line in lines],
            FadeOut(path_text),
            run_time=0.5
        )
    
    def section_insights(self):
        """三个核心启示"""
        # 小节标题
        section_title = Text("三个核心启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三张启示卡片
        insights = [
            ("🧱", "集合是编程的基石", "数组、列表、字典都是集合的变体", Colors.PRIMARY),
            ("🔮", "抽象是强大的工具", "群论用同一语言描述时钟、魔方、密码学", Colors.SECONDARY),
            ("♾️", "理解无限与边界", "计算机能力有极限，理解可计算性很重要", Colors.ACCENT),
        ]
        
        cards = VGroup()
        for icon, title, desc, color in insights:
            card = create_insight_card(icon, title, desc, color, width=5.5, height=1.2)
            cards.add(card)
        
        cards.arrange(DOWN, buff=0.25)
        cards.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for card in cards:
            self.play(FadeIn(card, shift=RIGHT * 0.3), run_time=0.6)
            self.wait(0.3)
        
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(cards),
            run_time=0.5
        )
    
    def section_closing(self):
        """结束动画"""
        # 升华语句
        closing_text = VGroup(
            Text("集合与抽象代数", font_size=28, color=Colors.PRIMARY),
            Text("不仅是数学工具", font_size=22, color=Colors.TEXT),
            Text("更是", font_size=22, color=Colors.TEXT),
            Text("逻辑与抽象思维", font_size=22, color=Colors.SECONDARY),
            Text("的核心锻炼", font_size=22, color=Colors.TEXT),
        )
        
        line1 = closing_text[0]
        line2 = VGroup(closing_text[1])
        line3 = VGroup(closing_text[2], closing_text[3], closing_text[4]).arrange(RIGHT, buff=0.1)
        
        all_lines = VGroup(line1, line2, line3).arrange(DOWN, buff=0.3)
        all_lines.set_x(0)
        
        self.play(FadeIn(line1, shift=UP * 0.3))
        self.wait(0.3)
        self.play(FadeIn(line2, shift=UP * 0.3))
        self.wait(0.3)
        self.play(FadeIn(line3, shift=UP * 0.3))
        self.wait(1)
        
        # 关键公式回顾
        formulas = VGroup(
            MathTex(r"A \cup B", font_size=24, color=Colors.PRIMARY),
            MathTex(r"A \cap B", font_size=24, color=Colors.SECONDARY),
            MathTex(r"\mathcal{P}(A)", font_size=24, color=Colors.SET_A),
            MathTex(r"(G, \cdot)", font_size=24, color=Colors.INTERSECTION),
            MathTex(r"\aleph_0", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.8)
        formulas.next_to(all_lines, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(formulas, shift=UP * 0.2))
        self.wait(1)
        
        # 渐隐效果
        self.play(
            FadeOut(self.chapter_title),
            all_lines.animate.scale(0.8).shift(UP * 0.5),
            formulas.animate.scale(0.8),
            run_time=0.8
        )
        
        # 感谢语
        thanks = Text("感谢观看", font_size=36, color=Colors.PRIMARY)
        thanks.set_x(0)
        
        self.play(
            FadeOut(all_lines),
            FadeOut(formulas),
            FadeIn(thanks, scale=1.2),
            run_time=1
        )
        self.wait(2)
        
        # 最终淡出
        self.play(FadeOut(thanks), run_time=1)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_08_summary.py Scene08Summary
    pass
