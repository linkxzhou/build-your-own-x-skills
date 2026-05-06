"""
数学归纳法 - Scene 7: 总结与启示
回顾知识点并展示编程启示

渲染命令: manim -pqh scene_07_summary.py InductionSummary
"""

from manim import *
import numpy as np


# ========== 配色方案 ==========
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    DOMINO_COLOR = "#F39C12" # 多米诺橙
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    INDUCT_COLOR = "#9B59B6" # 归纳步骤紫
    LOOP_COLOR = "#E74C3C"   # 循环红
    CODE_COLOR = "#3498DB"   # 代码蓝


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== Scene 7: 总结与启示 ==========
class InductionSummary(Scene):
    """总结与编程启示"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.knowledge_review()
        self.programming_insights()
        self.closing()
        
        clear_scene(self)
    
    def knowledge_review(self):
        """知识回顾"""
        section_title = Text("知识回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 核心要点列表
        points = VGroup()
        
        # 1. 归纳法核心
        point1 = VGroup(
            Text("① 归纳法的核心", font_size=18, color=Colors.PRIMARY),
            Text("两步走：基础步骤 + 归纳步骤", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        points.add(point1)
        
        # 2. 两种归纳法
        point2 = VGroup(
            Text("② 弱归纳 vs 强归纳", font_size=18, color=Colors.PRIMARY),
            VGroup(
                Text("弱归纳：假设 P(m)", font_size=14, color=Colors.INDUCT_COLOR),
                Text("强归纳：假设 P(1)...P(m)", font_size=14, color=Colors.LOOP_COLOR),
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        points.add(point2)
        
        # 3. 常见陷阱
        point3 = VGroup(
            Text("③ 常见陷阱", font_size=18, color=Colors.PRIMARY),
            VGroup(
                Text("• 忘记基础步骤", font_size=14, color=Colors.ACCENT),
                Text("• 逆转蕴含方向", font_size=14, color=Colors.ACCENT),
                Text("• 归纳步骤有漏洞", font_size=14, color=Colors.ACCENT),
            ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        points.add(point3)
        
        # 4. 循环不变量
        point4 = VGroup(
            Text("④ 循环不变量", font_size=18, color=Colors.PRIMARY),
            Text("初始化 → 保持 → 终止", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        points.add(point4)
        
        # 排列
        points.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        points.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for point in points:
            self.play(FadeIn(point, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(points), run_time=0.5)
    
    def programming_insights(self):
        """编程启示"""
        section_title = Text("编程启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 启示1：递归与归纳
        insight1_title = Text('① 递归与归纳是"双胞胎"', font_size=20, color=Colors.SECONDARY)
        insight1_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(insight1_title))
        
        # 对比表
        comparison = VGroup(
            VGroup(
                Text("递归（编程）", font_size=16, color=Colors.CODE_COLOR),
                Text("基本情况 (base case)", font_size=14, color=Colors.BASE_COLOR),
                Text("递归调用 (recursive call)", font_size=14, color=Colors.INDUCT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
            VGroup(
                Text("归纳（数学）", font_size=16, color=Colors.INDUCT_COLOR),
                Text("基础步骤 (base case)", font_size=14, color=Colors.BASE_COLOR),
                Text("归纳步骤 (inductive step)", font_size=14, color=Colors.INDUCT_COLOR),
            ).arrange(DOWN, buff=0.15, aligned_edge=LEFT),
        ).arrange(RIGHT, buff=1.0)
        comparison.next_to(insight1_title, DOWN, buff=0.2).set_x(0)
        
        # 双向箭头
        arrow = DoubleArrow(
            comparison[0].get_right() + RIGHT * 0.1,
            comparison[1].get_left() + LEFT * 0.1,
            color=Colors.GRAY
        )
        
        self.play(FadeIn(comparison), GrowArrow(arrow))
        self.wait(1)
        
        # 启示2
        self.play(FadeOut(insight1_title), FadeOut(comparison), FadeOut(arrow))
        
        insight2_title = Text("② 循环不变量提升代码质量", font_size=20, color=Colors.SECONDARY)
        insight2_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(insight2_title))
        
        insight2_content = VGroup(
            Text("写循环前先思考不变量 → 代码更清晰", font_size=16, color=Colors.TEXT),
            Text("用不变量验证正确性 → 减少 bug", font_size=16, color=Colors.TEXT),
            Text("不变量是最好的循环注释", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        insight2_content.next_to(insight2_title, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        for line in insight2_content:
            self.play(FadeIn(line, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(0.8)
        
        # 启示3
        self.play(FadeOut(insight2_title), FadeOut(insight2_content))
        
        insight3_title = Text('③ 从"大概能运行"到"逻辑保证正确"', font_size=20, color=Colors.SECONDARY)
        insight3_title.next_to(section_title, DOWN, buff=0.5).align_to(section_title, LEFT)
        
        self.play(FadeIn(insight3_title))
        
        levels = VGroup(
            VGroup(
                Text("Level 1:", font_size=16, color=Colors.GRAY),
                Text("写代码，跑测试，能过就行", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("Level 2:", font_size=16, color=Colors.SECONDARY),
                Text("思考边界条件，处理特殊情况", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("Level 3:", font_size=16, color=Colors.PRIMARY),
                Text("用不变量和归纳法证明正确性", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        levels.next_to(insight3_title, DOWN, buff=0.3).set_x(0)
        
        for i, level in enumerate(levels):
            self.play(FadeIn(level, shift=RIGHT * 0.1), run_time=0.5)
            if i == 2:
                # 高亮 Level 3
                highlight = SurroundingRectangle(level, color=Colors.PRIMARY, buff=0.1)
                self.play(Create(highlight))
        
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(insight3_title), FadeOut(levels), FadeOut(highlight))
    
    def closing(self):
        """结语"""
        section_title = Text("结语", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 核心信息
        core_message = VGroup(
            Text("数学归纳法", font_size=32, color=Colors.PRIMARY),
            Text("开启算法正确性证明的钥匙", font_size=22, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.3)
        core_message.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(core_message[0], scale=0.8))
        self.play(FadeIn(core_message[1], shift=UP * 0.2))
        self.wait(0.8)
        
        # 精华总结
        summary_points = VGroup(
            VGroup(
                Text("无限问题", font_size=18, color=Colors.GRAY),
                MathTex(r"\xrightarrow{\text{归纳法}}", font_size=22, color=Colors.INDUCT_COLOR),
                Text("有限证明", font_size=18, color=Colors.BASE_COLOR),
            ).arrange(RIGHT, buff=0.2),
        )
        # 修复：使用 Text 替代 MathTex 中的中文
        summary_fixed = VGroup(
            Text("无限问题", font_size=18, color=Colors.GRAY),
            Text("→ 归纳法 →", font_size=18, color=Colors.INDUCT_COLOR),
            Text("有限证明", font_size=18, color=Colors.BASE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        summary_fixed.next_to(core_message, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(summary_fixed))
        self.wait(0.5)
        
        # 多米诺骨牌再现
        domino_row = VGroup()
        for i in range(7):
            domino = Rectangle(height=0.8, width=0.12)
            domino.set_stroke(Colors.DOMINO_COLOR, width=2)
            domino.set_fill(Colors.DOMINO_COLOR, opacity=0.7)
            domino.shift(RIGHT * i * 0.35)
            domino_row.add(domino)
        
        dots = Text("...", font_size=24, color=Colors.DOMINO_COLOR)
        dots.next_to(domino_row, RIGHT, buff=0.2)
        
        domino_group = VGroup(domino_row, dots)
        domino_group.next_to(summary_fixed, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(domino_group))
        
        # 骨牌依次倒下
        for i, domino in enumerate(domino_row):
            self.play(
                Rotate(domino, angle=-PI/3, about_point=domino.get_bottom()),
                run_time=0.15
            )
        
        self.wait(0.5)
        
        # 最后的话
        final_words = VGroup(
            Text("掌握归纳法，", font_size=20, color=Colors.TEXT),
            Text('让你的代码从"能用"升级为"正确"', font_size=20, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        final_words.next_to(domino_group, DOWN, buff=0.5).set_x(0)
        
        final_box = SurroundingRectangle(final_words, color=Colors.SECONDARY, buff=0.2)
        
        self.play(FadeIn(final_words), Create(final_box))
        self.wait(2)
        
        # 淡出
        self.play(
            FadeOut(section_title), FadeOut(core_message),
            FadeOut(summary_fixed), FadeOut(domino_group),
            FadeOut(final_words), FadeOut(final_box),
            run_time=0.8
        )
        
        # 感谢
        thanks = Text("感谢观看", font_size=40, color=Colors.PRIMARY)
        thanks.set_x(0).set_y(0)
        
        self.play(FadeIn(thanks, scale=0.5))
        self.wait(2)
        
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_07_summary.py InductionSummary
    pass
