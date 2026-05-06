"""
递推与递归 - Scene 4: 非线性递推的奇妙世界
展示逻辑斯蒂映射的混沌行为和曼德博集

渲染命令: manim -pqh scene_04_nonlinear_recurrence.py NonlinearRecurrence
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
    CHAOS_COLOR = "#E74C3C"  # 混沌红
    STABLE_COLOR = "#2ECC71" # 稳定绿
    PERIODIC_COLOR = "#F39C12"  # 周期橙
    MANDEL_COLOR = "#9B59B6" # 曼德博紫


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


def logistic_map(x, r):
    """逻辑斯蒂映射"""
    return r * x * (1 - x)


# ========== Scene 4: 非线性递推 ==========
class NonlinearRecurrence(Scene):
    """非线性递推的奇妙世界"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.nonlinear_intro()
        self.logistic_map_intro()
        self.logistic_behavior()
        self.mandelbrot_intro()
        
        clear_scene(self)
    
    def nonlinear_intro(self):
        """非线性递推介绍"""
        section_title = Text("非线性递推", font_size=26, color=Colors.CHAOS_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 对比
        comparison = VGroup(
            VGroup(
                Text("线性递推：", font_size=18, color=Colors.SECONDARY),
                Text("加、减、数乘", font_size=16, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("非线性递推：", font_size=18, color=Colors.CHAOS_COLOR),
                Text("乘法、平方、更复杂的运算", font_size=16, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(comparison))
        self.wait(1)
        
        # 特点
        feature = VGroup(
            Text("特点：", font_size=18, color=Colors.PRIMARY),
            Text("能产生更奇妙的现象！", font_size=18, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        feature.next_to(comparison, DOWN, buff=0.4)
        
        self.play(FadeIn(feature))
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(comparison), FadeOut(feature),
            run_time=0.5
        )
    
    def logistic_map_intro(self):
        """逻辑斯蒂映射介绍"""
        section_title = Text("逻辑斯蒂映射", font_size=26, color=Colors.CHAOS_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 公式
        formula = MathTex(
            r"x_{n+1} = r \cdot x_n \cdot (1 - x_n)",
            font_size=28, color=Colors.CHAOS_COLOR
        )
        formula.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        formula_box = SurroundingRectangle(formula, color=Colors.CHAOS_COLOR, buff=0.15)
        
        self.play(FadeIn(formula), Create(formula_box))
        self.wait(0.5)
        
        # 参数说明
        params = VGroup(
            VGroup(Text("x", font_size=18, color=Colors.CHAOS_COLOR), Text(" ∈ [0, 1]：当前状态（如人口比例）", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
            VGroup(Text("r", font_size=18, color=Colors.CHAOS_COLOR), Text(" ：增长率参数（关键！）", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        params.next_to(formula_box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(params))
        self.wait(0.5)
        
        # 背景故事
        story = VGroup(
            Text("背景：", font_size=16, color=Colors.SECONDARY),
            Text("模拟人口增长的简化模型", font_size=14, color=Colors.GRAY),
            Text("人口增长但资源有限 → 增长受限", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        story.next_to(params, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(story))
        
        # 神奇之处
        magic = VGroup(
            Text("神奇之处：", font_size=16, color=Colors.ACCENT),
            Text("简单公式产生极其复杂的行为！", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        magic.next_to(story, DOWN, buff=0.4)
        
        self.play(FadeIn(magic))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(formula), FadeOut(formula_box),
            FadeOut(params), FadeOut(story), FadeOut(magic),
            run_time=0.5
        )
    
    def logistic_behavior(self):
        """逻辑斯蒂映射的行为"""
        section_title = Text("参数 r 的影响", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三种行为
        behaviors = VGroup(
            VGroup(
                Text("r < 3：稳定", font_size=18, color=Colors.STABLE_COLOR),
                Text("收敛到固定点", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(
                Text("3 < r < 3.57：周期", font_size=18, color=Colors.PERIODIC_COLOR),
                Text("在几个值之间循环", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(
                Text("r > 3.57：混沌", font_size=18, color=Colors.CHAOS_COLOR),
                Text("看似随机，对初始值极敏感", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        behaviors.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for behavior in behaviors:
            self.play(FadeIn(behavior, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1)
        
        # 演示稳定情况
        self.play(FadeOut(behaviors))
        
        demo_title = Text("演示 r = 2.5（稳定）", font_size=18, color=Colors.STABLE_COLOR)
        demo_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(demo_title))
        
        # 计算序列
        r = 2.5
        x = 0.1
        values_stable = [x]
        for _ in range(15):
            x = logistic_map(x, r)
            values_stable.append(x)
        
        # 绘制折线图
        axes = Axes(
            x_range=[0, 15, 5],
            y_range=[0, 1, 0.2],
            x_length=5,
            y_length=2.5,
            axis_config={"color": Colors.GRAY, "stroke_width": 1},
            tips=False,
        )
        axes.next_to(demo_title, DOWN, buff=0.3).set_x(0)
        
        x_label = Text("n", font_size=14, color=Colors.GRAY)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.1)
        y_label = Text("xₙ", font_size=14, color=Colors.GRAY)
        y_label.next_to(axes.y_axis, UP, buff=0.1)
        
        self.play(Create(axes), FadeIn(x_label), FadeIn(y_label))
        
        # 绘制点和线
        dots_stable = VGroup()
        for i, val in enumerate(values_stable):
            dot = Dot(axes.c2p(i, val), radius=0.04, color=Colors.STABLE_COLOR)
            dots_stable.add(dot)
        
        lines_stable = VGroup()
        for i in range(len(values_stable) - 1):
            line = Line(
                axes.c2p(i, values_stable[i]),
                axes.c2p(i+1, values_stable[i+1]),
                color=Colors.STABLE_COLOR, stroke_width=2
            )
            lines_stable.add(line)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_stable], lag_ratio=0.1),
            LaggedStart(*[Create(line) for line in lines_stable], lag_ratio=0.1),
            run_time=2
        )
        
        stable_result = Text(f"收敛到 ≈ {values_stable[-1]:.3f}", font_size=14, color=Colors.STABLE_COLOR)
        stable_result.next_to(axes, DOWN, buff=0.2)
        
        self.play(FadeIn(stable_result))
        self.wait(1)
        
        # 清理，演示混沌
        self.play(
            FadeOut(demo_title), FadeOut(axes), FadeOut(x_label), FadeOut(y_label),
            FadeOut(dots_stable), FadeOut(lines_stable), FadeOut(stable_result)
        )
        
        demo_title2 = Text("演示 r = 3.9（混沌）", font_size=18, color=Colors.CHAOS_COLOR)
        demo_title2.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(demo_title2))
        
        # 混沌序列
        r = 3.9
        x = 0.1
        values_chaos = [x]
        for _ in range(30):
            x = logistic_map(x, r)
            values_chaos.append(x)
        
        axes2 = Axes(
            x_range=[0, 30, 10],
            y_range=[0, 1, 0.2],
            x_length=5,
            y_length=2.5,
            axis_config={"color": Colors.GRAY, "stroke_width": 1},
            tips=False,
        )
        axes2.next_to(demo_title2, DOWN, buff=0.3).set_x(0)
        
        self.play(Create(axes2))
        
        # 绘制混沌序列
        dots_chaos = VGroup()
        lines_chaos = VGroup()
        
        for i, val in enumerate(values_chaos[:20]):
            dot = Dot(axes2.c2p(i, val), radius=0.03, color=Colors.CHAOS_COLOR)
            dots_chaos.add(dot)
            
            if i > 0:
                line = Line(
                    axes2.c2p(i-1, values_chaos[i-1]),
                    axes2.c2p(i, val),
                    color=Colors.CHAOS_COLOR, stroke_width=1.5
                )
                lines_chaos.add(line)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots_chaos], lag_ratio=0.05),
            LaggedStart(*[Create(line) for line in lines_chaos], lag_ratio=0.05),
            run_time=2
        )
        
        chaos_result = Text("完全不规则，无法预测！", font_size=14, color=Colors.CHAOS_COLOR)
        chaos_result.next_to(axes2, DOWN, buff=0.2)
        
        self.play(FadeIn(chaos_result))
        self.wait(1)
        
        # 蝴蝶效应
        butterfly = VGroup(
            Text("蝴蝶效应：", font_size=16, color=Colors.ACCENT),
            Text("初始值微小差异 → 结果完全不同", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        butterfly.next_to(chaos_result, DOWN, buff=0.3)
        
        self.play(FadeIn(butterfly))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(demo_title2),
            FadeOut(axes2), FadeOut(dots_chaos), FadeOut(lines_chaos),
            FadeOut(chaos_result), FadeOut(butterfly),
            run_time=0.5
        )
    
    def mandelbrot_intro(self):
        """曼德博集简介"""
        section_title = Text("曼德博集（分形）", font_size=26, color=Colors.MANDEL_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 公式
        formula = MathTex(
            r"z_{n+1} = z_n^2 + c",
            font_size=28, color=Colors.MANDEL_COLOR
        )
        formula.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        formula_box = SurroundingRectangle(formula, color=Colors.MANDEL_COLOR, buff=0.15)
        
        self.play(FadeIn(formula), Create(formula_box))
        
        # 说明
        explain = VGroup(
            Text("z 和 c 是复数", font_size=16, color=Colors.GRAY),
            Text("从 z₀ = 0 开始迭代", font_size=16, color=Colors.GRAY),
            Text('判断序列是否"爆炸"（趋向无穷）', font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explain.next_to(formula_box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(explain))
        self.wait(1)
        
        # 曼德博集定义
        definition = VGroup(
            Text("曼德博集：", font_size=18, color=Colors.MANDEL_COLOR),
            Text('所有使序列"不爆炸"的 c 值的集合', font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(explain, DOWN, buff=0.3)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 简化的曼德博集展示
        self.play(FadeOut(explain), FadeOut(formula), FadeOut(formula_box))
        
        result_title = Text("结果：无限复杂的分形图案", font_size=18, color=Colors.SECONDARY)
        result_title.next_to(definition, DOWN, buff=0.4)
        
        self.play(FadeIn(result_title))
        
        # 绘制简化的曼德博集轮廓
        # 使用参数化曲线近似心形
        t_values = np.linspace(0, 2 * PI, 100)
        
        # 心脏线（主心形部分）近似
        def cardioid(t):
            r = 0.5 * (1 - np.cos(t))
            x = r * np.cos(t) - 0.25
            y = r * np.sin(t)
            return np.array([x * 2, y * 2, 0])
        
        cardioid_curve = ParametricFunction(
            cardioid,
            t_range=[0, 2 * PI],
            color=Colors.MANDEL_COLOR,
            stroke_width=2
        )
        cardioid_curve.next_to(result_title, DOWN, buff=0.3).set_x(0)
        cardioid_curve.scale(0.8)
        
        # 圆形（主圆盘）
        circle = Circle(radius=0.2, color=Colors.MANDEL_COLOR, stroke_width=2)
        circle.move_to(cardioid_curve.get_center() + LEFT * 0.5)
        
        mandel_shape = VGroup(cardioid_curve, circle)
        mandel_shape.set_fill(Colors.MANDEL_COLOR, opacity=0.3)
        
        self.play(Create(mandel_shape), run_time=1.5)
        
        # 分形特点
        fractal_note = VGroup(
            Text("分形特点：", font_size=14, color=Colors.GRAY),
            Text("无限放大仍有无限细节", font_size=14, color=Colors.GRAY),
            Text("简单规则 → 无限复杂", font_size=14, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        fractal_note.next_to(mandel_shape, DOWN, buff=0.3)
        
        self.play(FadeIn(fractal_note))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(result_title), FadeOut(mandel_shape), FadeOut(fractal_note),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_04_nonlinear_recurrence.py NonlinearRecurrence
    pass
