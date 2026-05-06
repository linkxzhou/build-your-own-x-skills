"""
递推与递归 - Scene 8: 总结与启示
回顾核心概念并展示编程启示

渲染命令: manim -pqh scene_08_summary.py RecursionSummary
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
    RECUR_COLOR = "#F39C12"  # 递推橙
    RECURSIVE_COLOR = "#9B59B6"  # 递归紫
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
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


def create_matryoshka(size, color, opacity=0.7):
    """创建俄罗斯套娃形状"""
    body = Ellipse(width=size * 0.8, height=size)
    body.set_stroke(color, width=2)
    body.set_fill(color, opacity=opacity)
    
    head = Circle(radius=size * 0.25)
    head.set_stroke(color, width=2)
    head.set_fill(color, opacity=opacity)
    head.next_to(body, UP, buff=-size * 0.15)
    
    return VGroup(body, head)


# ========== Scene 8: 总结与启示 ==========
class RecursionSummary(Scene):
    """总结与启示"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.two_sides_of_coin()
        self.efficiency_matters()
        self.programming_insights()
        self.closing()
        
        clear_scene(self)
    
    def two_sides_of_coin(self):
        """递推与递归是硬币的两面"""
        section_title = Text("总结一：硬币的两面", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 硬币比喻
        coin_title = Text("递推与递归", font_size=22, color=Colors.PRIMARY)
        coin_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(coin_title))
        
        # 两面
        side1 = VGroup(
            Text("递推", font_size=20, color=Colors.RECUR_COLOR),
            Text("正向迭代构造", font_size=16, color=Colors.TEXT),
            Text("从已知推向未知", font_size=14, color=Colors.GRAY),
            MathTex(r"a_1 \to a_2 \to a_3 \to \cdots", font_size=16, color=Colors.RECUR_COLOR),
        ).arrange(DOWN, buff=0.1)
        side1_box = SurroundingRectangle(side1, color=Colors.RECUR_COLOR, buff=0.15)
        side1_group = VGroup(side1, side1_box)
        
        side2 = VGroup(
            Text("递归", font_size=20, color=Colors.RECURSIVE_COLOR),
            Text("逆向分解合并", font_size=16, color=Colors.TEXT),
            Text("从问题降到基础", font_size=14, color=Colors.GRAY),
            MathTex(r"f(n) \to f(n-1) \to \cdots \to f(1)", font_size=16, color=Colors.RECURSIVE_COLOR),
        ).arrange(DOWN, buff=0.1)
        side2_box = SurroundingRectangle(side2, color=Colors.RECURSIVE_COLOR, buff=0.15)
        side2_group = VGroup(side2, side2_box)
        
        sides = VGroup(side1_group, side2_group).arrange(RIGHT, buff=0.6)
        sides.next_to(coin_title, DOWN, buff=0.4).set_x(0)
        
        # 双向箭头
        arrow = DoubleArrow(
            side1_group.get_right() + RIGHT * 0.1,
            side2_group.get_left() + LEFT * 0.1,
            color=Colors.GRAY, stroke_width=2
        )
        
        self.play(FadeIn(side1_group))
        self.wait(0.5)
        self.play(GrowArrow(arrow))
        self.play(FadeIn(side2_group))
        self.wait(0.5)
        
        # 核心思想
        core = VGroup(
            Text("核心思想：", font_size=18, color=Colors.SECONDARY),
            Text("化繁为简，分步解决", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        core.next_to(sides, DOWN, buff=0.4)
        
        core_box = SurroundingRectangle(core, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(coin_title),
            FadeOut(sides), FadeOut(arrow),
            FadeOut(core), FadeOut(core_box),
            run_time=0.5
        )
    
    def efficiency_matters(self):
        """效率至关重要"""
        section_title = Text("总结二：效率至关重要", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 警告
        warning = VGroup(
            Text("⚠️ 并非所有递归都高效！", font_size=20, color=Colors.ACCENT),
        )
        warning.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(warning))
        
        # 斐波那契例子
        fib_title = Text("例：朴素斐波那契递归", font_size=16, color=Colors.GRAY)
        fib_title.next_to(warning, DOWN, buff=0.4).align_to(warning, LEFT)
        
        self.play(FadeIn(fib_title))
        
        fib_problem = VGroup(
            Text("fib(5) 的调用树：", font_size=14, color=Colors.TEXT),
            Text("fib(5) 调用 fib(4) 和 fib(3)", font_size=12, color=Colors.GRAY),
            Text("fib(4) 又调用 fib(3) 和 fib(2)...", font_size=12, color=Colors.GRAY),
            Text("大量重复计算！", font_size=14, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        fib_problem.next_to(fib_title, DOWN, buff=0.15).shift(RIGHT * 0.3)
        
        self.play(FadeIn(fib_problem))
        self.wait(0.5)
        
        # 解决方案
        solutions_title = Text("优化方法：", font_size=16, color=Colors.SECONDARY)
        solutions_title.next_to(fib_problem, DOWN, buff=0.4).align_to(fib_title, LEFT)
        
        self.play(FadeIn(solutions_title))
        
        solutions = VGroup(
            VGroup(
                Text("① 记忆化", font_size=14, color=Colors.BASE_COLOR),
                Text("缓存已计算的结果", font_size=12, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("② 尾递归", font_size=14, color=Colors.BASE_COLOR),
                Text("编译器可优化为循环", font_size=12, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("③ 改用递推", font_size=14, color=Colors.BASE_COLOR),
                Text("直接用循环实现", font_size=12, color=Colors.GRAY),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        solutions.next_to(solutions_title, DOWN, buff=0.15).shift(RIGHT * 0.3)
        
        for sol in solutions:
            self.play(FadeIn(sol, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(1)
        
        # 建议
        advice = VGroup(
            Text("建议：", font_size=16, color=Colors.PRIMARY),
            Text("思考能否用循环替代递归", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        advice.next_to(solutions, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(advice))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(warning),
            FadeOut(fib_title), FadeOut(fib_problem),
            FadeOut(solutions_title), FadeOut(solutions),
            FadeOut(advice),
            run_time=0.5
        )
    
    def programming_insights(self):
        """编程启示"""
        section_title = Text("编程启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 启示列表
        insights = VGroup(
            VGroup(
                Text("① 递归是强大的编程范式", font_size=18, color=Colors.PRIMARY),
                Text("树/图遍历、分治算法、动态规划", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("② 函数式编程的基石", font_size=18, color=Colors.PRIMARY),
                Text("无副作用、声明式编程", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("③ 从数学到代码的桥梁", font_size=18, color=Colors.PRIMARY),
                Text("数学递推 → 算法实现 → 性能分析", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        insights.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for insight in insights:
            self.play(FadeIn(insight, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1)
        
        # 示例应用
        apps = VGroup(
            Text("应用举例：", font_size=16, color=Colors.SECONDARY),
            Text("• 文件系统遍历", font_size=14, color=Colors.TEXT),
            Text("• JSON/XML 解析", font_size=14, color=Colors.TEXT),
            Text("• 编译器语法分析", font_size=14, color=Colors.TEXT),
            Text("• 机器学习中的决策树", font_size=14, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        apps.next_to(insights, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(apps))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(insights), FadeOut(apps),
            run_time=0.5
        )
    
    def closing(self):
        """结语"""
        # 核心信息
        core_message = VGroup(
            Text("递推与递归", font_size=36, color=Colors.PRIMARY),
            Text("让计算机像\"俄罗斯套娃\"一样思考", font_size=20, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.3)
        core_message.set_x(0).set_y(0.5)
        
        self.play(FadeIn(core_message[0], scale=0.8))
        self.play(FadeIn(core_message[1], shift=UP * 0.2))
        self.wait(0.8)
        
        # 套娃动画
        colors = [Colors.ACCENT, Colors.RECURSIVE_COLOR, Colors.PRIMARY, Colors.SECONDARY, Colors.BASE_COLOR]
        sizes = [1.2, 0.95, 0.7, 0.5, 0.35]
        
        dolls = VGroup()
        for size, color in zip(sizes, colors):
            doll = create_matryoshka(size, color)
            dolls.add(doll)
        
        dolls.arrange(RIGHT, buff=0.2)
        dolls.next_to(core_message, DOWN, buff=0.5).set_x(0)
        dolls.scale(0.6)
        
        self.play(
            LaggedStart(*[FadeIn(d, scale=0.5) for d in dolls], lag_ratio=0.15),
            run_time=1
        )
        self.wait(0.5)
        
        # 总结语
        summary = VGroup(
            Text("掌握递推与递归，", font_size=18, color=Colors.TEXT),
            Text("是通往更高级算法和编程思维的关键一步", font_size=18, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        summary.next_to(dolls, DOWN, buff=0.5)
        
        summary_box = SurroundingRectangle(summary, color=Colors.SECONDARY, buff=0.2)
        
        self.play(FadeIn(summary), Create(summary_box))
        self.wait(2)
        
        # 淡出
        self.play(
            FadeOut(core_message), FadeOut(dolls),
            FadeOut(summary), FadeOut(summary_box),
            run_time=0.8
        )
        
        # 感谢
        thanks = Text("感谢观看", font_size=40, color=Colors.PRIMARY)
        thanks.set_x(0).set_y(0)
        
        self.play(FadeIn(thanks, scale=0.5))
        self.wait(2)
        
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_08_summary.py RecursionSummary
    pass
