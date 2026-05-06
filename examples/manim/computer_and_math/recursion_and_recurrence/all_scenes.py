"""
递推与递归 - 完整动画合集
第六章：递推与递归 - 数学中的迭代，编程中的分解术

本文件导入所有单独的场景，并提供一个合并的场景类。

渲染命令:
- 完整渲染: manim -pqh all_scenes.py RecursionAndRecurrence
- 低质量预览: manim -pql all_scenes.py RecursionAndRecurrence
- 单独场景请参考各场景文件

场景列表:
1. RecursionIntro - 开场与概念引入
2. RecurrenceBasics - 递推关系基础
3. LinearRecurrence - 伪随机数与线性递推
4. NonlinearRecurrence - 非线性递推的奇妙世界
5. SolvingRecurrence - 解递推关系
6. RecursionBasics - 递归基础概念
7. RecursionExamples - 递归算法示例
8. RecursionSummary - 总结与启示
"""

from manim import *
import numpy as np

# 导入所有单独场景
from scene_01_intro import RecursionIntro
from scene_02_recurrence_basics import RecurrenceBasics
from scene_03_linear_recurrence import LinearRecurrence
from scene_04_nonlinear_recurrence import NonlinearRecurrence
from scene_05_solving_recurrence import SolvingRecurrence
from scene_06_recursion_intro import RecursionBasics as RecursionBasicsIntro
from scene_07_recursion_examples import RecursionExamples
from scene_08_summary import RecursionSummary


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


# ========== 完整合并场景类 ==========
class RecursionAndRecurrence(Scene):
    """
    递推与递归完整章节
    
    这个场景类整合了所有8个独立场景的内容，
    按顺序播放完整的教学动画。
    
    由于内容较多，建议分别渲染各个独立场景进行测试，
    然后使用视频编辑软件进行合并。
    
    或者直接运行此场景以获得完整视频。
    """
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # ========== Part 1: 开场与概念引入 ==========
        self.part1_opening()
        clear_scene(self)
        
        # ========== Part 2-8: 后续内容 ==========
        # 由于内容较长，这里提供精简版本
        # 完整内容请参考各独立场景文件
        
        self.add(self.chapter_title)
        self.part_summary()
        clear_scene(self)
    
    def part1_opening(self):
        """Part 1: 开场动画"""
        main_title = Text("递推与递归", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("数学中的迭代，编程中的分解术", font_size=24, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
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
        self.wait(0.5)
        
        # 魔法一：递推
        section_title = Text("公式魔法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        magic1_title = Text("魔法一：递推", font_size=20, color=Colors.RECUR_COLOR)
        magic1_content = Text("从前一个结果推算出下一个", font_size=16, color=Colors.TEXT)
        magic1 = VGroup(magic1_title, magic1_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        magic1_box = SurroundingRectangle(magic1, color=Colors.RECUR_COLOR, buff=0.15)
        magic1_group = VGroup(magic1, magic1_box)
        
        magic2_title = Text("魔法二：递归", font_size=20, color=Colors.RECURSIVE_COLOR)
        magic2_content = Text("把大问题拆成迷你版的自己", font_size=16, color=Colors.TEXT)
        magic2 = VGroup(magic2_title, magic2_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        magic2_box = SurroundingRectangle(magic2, color=Colors.RECURSIVE_COLOR, buff=0.15)
        magic2_group = VGroup(magic2, magic2_box)
        
        magics = VGroup(magic1_group, magic2_group).arrange(DOWN, buff=0.4)
        magics.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(magic1_group, shift=RIGHT * 0.2))
        self.wait(0.8)
        self.play(FadeIn(magic2_group, shift=RIGHT * 0.2))
        self.wait(1)
        
        # 俄罗斯套娃
        self.play(FadeOut(section_title), FadeOut(magics))
        
        section_title2 = Text("俄罗斯套娃思维", font_size=26, color=Colors.TEXT)
        section_title2.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title2, shift=DOWN * 0.2))
        
        colors = [Colors.FIBO_COLOR, Colors.RECURSIVE_COLOR, Colors.PRIMARY, Colors.SECONDARY, Colors.BASE_COLOR]
        sizes = [1.5, 1.2, 0.9, 0.6, 0.4]
        
        dolls = VGroup()
        for i, (size, color) in enumerate(zip(sizes, colors)):
            doll = create_matryoshka(size, color, opacity=0.7)
            dolls.add(doll)
        
        dolls.arrange(RIGHT, buff=0.3)
        dolls.next_to(section_title2, DOWN, buff=0.6).set_x(0)
        
        for i, doll in enumerate(dolls):
            self.play(FadeIn(doll, scale=0.5), run_time=0.4)
        
        self.wait(0.5)
        
        explain = VGroup(
            Text("递归：大问题包含小问题", font_size=16, color=Colors.TEXT),
            Text("基准情况：最小的娃娃，直接解决", font_size=16, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.2)
        explain.next_to(dolls, DOWN, buff=0.5)
        
        self.play(FadeIn(explain))
        self.wait(1.5)
        
        # 章节概览
        self.play(FadeOut(section_title2), FadeOut(dolls), FadeOut(explain))
        
        overview_title = Text("本章内容", font_size=26, color=Colors.TEXT)
        overview_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(overview_title, shift=DOWN * 0.2))
        
        part1_title = Text("第一部分：递推关系", font_size=18, color=Colors.RECUR_COLOR)
        part1_items = VGroup(
            Text("• 等差数列、等比数列、斐波那契数列", font_size=13, color=Colors.GRAY),
            Text("• 伪随机数生成、混沌与分形", font_size=13, color=Colors.GRAY),
            Text("• 解递推关系（特征方程法）", font_size=13, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        part1 = VGroup(part1_title, part1_items).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        part1_box = SurroundingRectangle(part1, color=Colors.RECUR_COLOR, buff=0.12)
        part1_group = VGroup(part1, part1_box)
        
        part2_title = Text("第二部分：递归", font_size=18, color=Colors.RECURSIVE_COLOR)
        part2_items = VGroup(
            Text("• 递归的核心要素（基准情况、递归情况）", font_size=13, color=Colors.GRAY),
            Text("• 经典算法（阶乘、快速幂、快速排序、汉诺塔）", font_size=13, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.06, aligned_edge=LEFT)
        part2 = VGroup(part2_title, part2_items).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        part2_box = SurroundingRectangle(part2, color=Colors.RECURSIVE_COLOR, buff=0.12)
        part2_group = VGroup(part2, part2_box)
        
        parts = VGroup(part1_group, part2_group).arrange(DOWN, buff=0.3)
        parts.next_to(overview_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(part1_group, shift=RIGHT * 0.2))
        self.wait(0.5)
        self.play(FadeIn(part2_group, shift=RIGHT * 0.2))
        self.wait(1.5)
        
        transition = Text("让我们开始这段奇妙的旅程...", font_size=18, color=Colors.SECONDARY)
        transition.next_to(parts, DOWN, buff=0.5)
        
        self.play(FadeIn(transition))
        self.wait(1.5)
    
    def part_summary(self):
        """最终总结"""
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
        
        # 总结要点
        key_points = VGroup(
            Text("✓ 递推：从已知推向未知", font_size=16, color=Colors.RECUR_COLOR),
            Text("✓ 递归：从问题降到基础", font_size=16, color=Colors.RECURSIVE_COLOR),
            Text("✓ 核心思想：化繁为简，分步解决", font_size=16, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        key_points.next_to(dolls, DOWN, buff=0.5)
        
        for point in key_points:
            self.play(FadeIn(point, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(1)
        
        # 总结语
        summary = VGroup(
            Text("掌握递推与递归，", font_size=18, color=Colors.TEXT),
            Text("是通往更高级算法和编程思维的关键一步", font_size=18, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        summary.next_to(key_points, DOWN, buff=0.5)
        
        summary_box = SurroundingRectangle(summary, color=Colors.SECONDARY, buff=0.2)
        
        self.play(FadeIn(summary), Create(summary_box))
        self.wait(2)
        
        # 淡出
        self.play(
            FadeOut(core_message), FadeOut(dolls),
            FadeOut(key_points),
            FadeOut(summary), FadeOut(summary_box),
            run_time=0.8
        )
        
        # 感谢
        thanks = Text("感谢观看", font_size=40, color=Colors.PRIMARY)
        thanks.set_x(0).set_y(0)
        
        self.play(FadeIn(thanks, scale=0.5))
        self.wait(2)
        
        self.play(FadeOut(thanks))


# ========== 便捷渲染函数 ==========
def render_all_scenes():
    """
    批量渲染所有场景的便捷函数
    
    使用方法:
    python -c "from all_scenes import render_all_scenes; render_all_scenes()"
    
    或者分别运行:
    manim -pqh scene_01_intro.py RecursionIntro
    manim -pqh scene_02_recurrence_basics.py RecurrenceBasics
    manim -pqh scene_03_linear_recurrence.py LinearRecurrence
    manim -pqh scene_04_nonlinear_recurrence.py NonlinearRecurrence
    manim -pqh scene_05_solving_recurrence.py SolvingRecurrence
    manim -pqh scene_06_recursion_intro.py RecursionBasics
    manim -pqh scene_07_recursion_examples.py RecursionExamples
    manim -pqh scene_08_summary.py RecursionSummary
    """
    import subprocess
    
    scenes = [
        ("scene_01_intro.py", "RecursionIntro"),
        ("scene_02_recurrence_basics.py", "RecurrenceBasics"),
        ("scene_03_linear_recurrence.py", "LinearRecurrence"),
        ("scene_04_nonlinear_recurrence.py", "NonlinearRecurrence"),
        ("scene_05_solving_recurrence.py", "SolvingRecurrence"),
        ("scene_06_recursion_intro.py", "RecursionBasics"),
        ("scene_07_recursion_examples.py", "RecursionExamples"),
        ("scene_08_summary.py", "RecursionSummary"),
    ]
    
    for filename, scene_name in scenes:
        print(f"渲染 {filename} - {scene_name}...")
        subprocess.run(["manim", "-pqh", filename, scene_name])
        print(f"完成 {scene_name}\n")


if __name__ == "__main__":
    # 渲染完整场景: manim -pqh all_scenes.py RecursionAndRecurrence
    # 或运行 render_all_scenes() 批量渲染所有独立场景
    pass
