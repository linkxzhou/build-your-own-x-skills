"""
递推与递归 - Scene 1: 开场与概念引入
通过俄罗斯套娃比喻引入递推与递归的核心概念

渲染命令: manim -pqh scene_01_intro.py RecursionIntro
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
    FIBO_COLOR = "#E91E63"   # 斐波那契粉


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


def create_matryoshka(size, color, opacity=0.8):
    """创建俄罗斯套娃形状（简化版椭圆）"""
    body = Ellipse(width=size * 0.8, height=size)
    body.set_stroke(color, width=2)
    body.set_fill(color, opacity=opacity)
    
    # 头部
    head = Circle(radius=size * 0.25)
    head.set_stroke(color, width=2)
    head.set_fill(color, opacity=opacity)
    head.next_to(body, UP, buff=-size * 0.15)
    
    return VGroup(body, head)


# ========== Scene 1: 开场与概念引入 ==========
class RecursionIntro(Scene):
    """递推与递归的概念引入"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # 各部分
        self.opening()
        self.magic_formula_intro()
        self.matryoshka_concept()
        self.chapter_overview()
        
        clear_scene(self)
    
    def opening(self):
        """开场动画"""
        main_title = Text("递推与递归", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("数学中的迭代，编程中的分解术", font_size=24, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        # 标题动画
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        # 引入语
        intro = Text(
            "想象一下，你有一种特殊的\"公式魔法\"...",
            font_size=20, color=Colors.SECONDARY
        )
        intro.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(intro, shift=UP * 0.2))
        self.wait(1.5)
        
        # 转换到章节标题
        self.play(
            FadeOut(subtitle),
            FadeOut(intro),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def magic_formula_intro(self):
        """公式魔法介绍"""
        section_title = Text("公式魔法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 魔法一：递推
        magic1_title = Text("魔法一：递推", font_size=20, color=Colors.RECUR_COLOR)
        magic1_content = Text(
            "从前一个结果推算出下一个",
            font_size=16, color=Colors.TEXT
        )
        magic1 = VGroup(magic1_title, magic1_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        magic1_box = SurroundingRectangle(magic1, color=Colors.RECUR_COLOR, buff=0.15)
        magic1_group = VGroup(magic1, magic1_box)
        
        # 魔法二：递归
        magic2_title = Text("魔法二：递归", font_size=20, color=Colors.RECURSIVE_COLOR)
        magic2_content = Text(
            "把大问题拆成迷你版的自己",
            font_size=16, color=Colors.TEXT
        )
        magic2 = VGroup(magic2_title, magic2_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        magic2_box = SurroundingRectangle(magic2, color=Colors.RECURSIVE_COLOR, buff=0.15)
        magic2_group = VGroup(magic2, magic2_box)
        
        # 排列
        magics = VGroup(magic1_group, magic2_group).arrange(DOWN, buff=0.4)
        magics.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(magic1_group, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(magic2_group, shift=RIGHT * 0.2))
        self.wait(1)
        
        # 动画演示递推
        recur_demo_title = Text("递推示例：", font_size=16, color=Colors.RECUR_COLOR)
        recur_demo_title.next_to(magics, DOWN, buff=0.5).align_to(magics, LEFT)
        
        self.play(FadeIn(recur_demo_title))
        
        # 数列动画
        nums = VGroup()
        arrows = VGroup()
        for i, val in enumerate([1, 2, 3, 4, 5]):
            num = Text(str(val), font_size=24, color=Colors.RECUR_COLOR)
            num.shift(RIGHT * i * 0.8)
            nums.add(num)
            
            if i > 0:
                arrow = Arrow(
                    nums[i-1].get_right() + RIGHT * 0.1,
                    num.get_left() + LEFT * 0.1,
                    buff=0.05, color=Colors.GRAY, stroke_width=2
                )
                arrows.add(arrow)
        
        dots = Text("...", font_size=24, color=Colors.RECUR_COLOR)
        dots.next_to(nums, RIGHT, buff=0.3)
        
        demo_group = VGroup(nums, arrows, dots)
        demo_group.next_to(recur_demo_title, DOWN, buff=0.2).set_x(0)
        
        # 逐个显示
        for i, num in enumerate(nums):
            if i == 0:
                self.play(FadeIn(num, scale=0.5), run_time=0.3)
            else:
                self.play(
                    GrowArrow(arrows[i-1]),
                    FadeIn(num, scale=0.5),
                    run_time=0.3
                )
        self.play(FadeIn(dots))
        
        # 规则说明
        rule = MathTex(r"a_n = a_{n-1} + 1", font_size=24, color=Colors.RECUR_COLOR)
        rule.next_to(demo_group, DOWN, buff=0.3)
        
        self.play(FadeIn(rule))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(magics),
            FadeOut(recur_demo_title), FadeOut(demo_group), FadeOut(rule),
            run_time=0.5
        )
    
    def matryoshka_concept(self):
        """俄罗斯套娃概念"""
        section_title = Text("俄罗斯套娃思维", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建套娃（从大到小）
        colors = [Colors.FIBO_COLOR, Colors.RECURSIVE_COLOR, Colors.PRIMARY, Colors.SECONDARY, Colors.BASE_COLOR]
        sizes = [1.5, 1.2, 0.9, 0.6, 0.4]
        
        dolls = VGroup()
        for i, (size, color) in enumerate(zip(sizes, colors)):
            doll = create_matryoshka(size, color, opacity=0.7)
            dolls.add(doll)
        
        dolls.arrange(RIGHT, buff=0.3)
        dolls.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        # 从大到小依次出现
        for i, doll in enumerate(dolls):
            self.play(FadeIn(doll, scale=0.5), run_time=0.4)
        
        self.wait(0.5)
        
        # 说明文字
        explain1 = VGroup(
            Text("递归：", font_size=18, color=Colors.RECURSIVE_COLOR),
            Text("大问题包含小问题", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explain1.next_to(dolls, DOWN, buff=0.5)
        
        self.play(FadeIn(explain1))
        self.wait(0.5)
        
        explain2 = VGroup(
            Text("基准情况：", font_size=18, color=Colors.BASE_COLOR),
            Text("最小的娃娃，直接解决", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explain2.next_to(explain1, DOWN, buff=0.2)
        
        self.play(FadeIn(explain2))
        
        # 高亮最小的娃娃
        highlight = SurroundingRectangle(dolls[-1], color=Colors.BASE_COLOR, buff=0.1)
        self.play(Create(highlight))
        self.wait(1)
        
        # 套娃合并动画（从小到大）
        merge_title = Text("解决问题：从小到大合并结果", font_size=16, color=Colors.SECONDARY)
        merge_title.next_to(explain2, DOWN, buff=0.4)
        
        self.play(FadeIn(merge_title), FadeOut(highlight))
        
        # 合并动画
        for i in range(len(dolls) - 1, 0, -1):
            self.play(
                dolls[i].animate.move_to(dolls[i-1].get_center()),
                run_time=0.4
            )
        
        self.wait(1)
        
        # 核心理念
        core = VGroup(
            Text("核心理念：", font_size=18, color=Colors.PRIMARY),
            Text("化繁为简，分步解决", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        core.next_to(merge_title, DOWN, buff=0.4)
        
        core_box = SurroundingRectangle(core, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(dolls),
            FadeOut(explain1), FadeOut(explain2),
            FadeOut(merge_title), FadeOut(core), FadeOut(core_box),
            run_time=0.5
        )
    
    def chapter_overview(self):
        """章节概览"""
        section_title = Text("本章内容", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 第一部分
        part1_title = Text("第一部分：递推关系", font_size=20, color=Colors.RECUR_COLOR)
        part1_items = VGroup(
            Text("• 等差数列、等比数列", font_size=14, color=Colors.GRAY),
            Text("• 斐波那契数列", font_size=14, color=Colors.GRAY),
            Text("• 伪随机数生成", font_size=14, color=Colors.GRAY),
            Text("• 混沌与分形", font_size=14, color=Colors.GRAY),
            Text("• 解递推关系", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        
        part1 = VGroup(part1_title, part1_items).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        part1_box = SurroundingRectangle(part1, color=Colors.RECUR_COLOR, buff=0.15)
        part1_group = VGroup(part1, part1_box)
        
        # 第二部分
        part2_title = Text("第二部分：递归", font_size=20, color=Colors.RECURSIVE_COLOR)
        part2_items = VGroup(
            Text("• 递归的核心要素", font_size=14, color=Colors.GRAY),
            Text("• 阶乘与乘方", font_size=14, color=Colors.GRAY),
            Text("• 快速排序", font_size=14, color=Colors.GRAY),
            Text("• 汉诺塔问题", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        
        part2 = VGroup(part2_title, part2_items).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        part2_box = SurroundingRectangle(part2, color=Colors.RECURSIVE_COLOR, buff=0.15)
        part2_group = VGroup(part2, part2_box)
        
        # 排列
        parts = VGroup(part1_group, part2_group).arrange(DOWN, buff=0.4)
        parts.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(part1_group, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(part2_group, shift=RIGHT * 0.2))
        self.wait(1.5)
        
        # 过渡语
        transition = Text(
            "让我们开始这段奇妙的旅程...",
            font_size=18, color=Colors.SECONDARY
        )
        transition.next_to(parts, DOWN, buff=0.5)
        
        self.play(FadeIn(transition))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(parts), FadeOut(transition),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_01_intro.py RecursionIntro
    pass
