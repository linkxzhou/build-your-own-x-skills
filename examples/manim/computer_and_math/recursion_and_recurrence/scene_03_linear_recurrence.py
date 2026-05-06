"""
递推与递归 - Scene 3: 伪随机数与线性递推
展示线性递推在伪随机数生成中的应用

渲染命令: manim -pqh scene_03_linear_recurrence.py LinearRecurrence
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
    RANDOM_COLOR = "#9B59B6" # 随机紫
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


# ========== Scene 3: 线性递推与伪随机数 ==========
class LinearRecurrence(Scene):
    """线性递推与伪随机数生成"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.linear_recurrence_intro()
        self.pseudo_random_formula()
        self.random_visualization()
        self.applications()
        
        clear_scene(self)
    
    def linear_recurrence_intro(self):
        """线性递推介绍"""
        section_title = Text("线性递推", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("线性递推的特点：", font_size=18, color=Colors.RECUR_COLOR),
            Text("项之间只做 加、减、数乘 运算", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 一般形式
        general_form_title = Text("一般形式：", font_size=16, color=Colors.GRAY)
        general_form_title.next_to(definition, DOWN, buff=0.4).align_to(definition, LEFT)
        
        general_form = MathTex(
            r"a_n = c_1 \cdot a_{n-1} + c_2 \cdot a_{n-2} + \cdots + c_k \cdot a_{n-k}",
            font_size=22, color=Colors.RECUR_COLOR
        )
        general_form.next_to(general_form_title, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(general_form_title), FadeIn(general_form))
        self.wait(1)
        
        # 例子回顾
        examples = VGroup(
            Text("例如：", font_size=16, color=Colors.SECONDARY),
            VGroup(
                Text("等差数列：", font_size=14, color=Colors.GRAY),
                MathTex(r"a_n = a_{n-1} + d", font_size=18, color=Colors.CODE_COLOR),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("斐波那契：", font_size=14, color=Colors.GRAY),
                MathTex(r"a_n = a_{n-1} + a_{n-2}", font_size=18, color=Colors.CODE_COLOR),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        examples.next_to(general_form, DOWN, buff=0.4).set_x(0)
        
        for item in examples:
            self.play(FadeIn(item, shift=RIGHT * 0.1), run_time=0.4)
        
        self.wait(1)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(general_form_title), FadeOut(general_form),
            FadeOut(examples),
            run_time=0.5
        )
    
    def pseudo_random_formula(self):
        """伪随机数公式"""
        section_title = Text("伪随机数生成器", font_size=26, color=Colors.RANDOM_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题
        question = VGroup(
            Text("问题：", font_size=18, color=Colors.PRIMARY),
            Text("计算机如何生成随机数？", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        question.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(question))
        self.wait(0.5)
        
        # 答案
        answer = VGroup(
            Text("答案：", font_size=18, color=Colors.SECONDARY),
            Text("线性同余生成器（LCG）", font_size=18, color=Colors.RANDOM_COLOR),
        ).arrange(RIGHT, buff=0.1)
        answer.next_to(question, DOWN, buff=0.3)
        
        self.play(FadeIn(answer))
        
        # 公式
        formula_title = Text("公式：", font_size=16, color=Colors.GRAY)
        formula_title.next_to(answer, DOWN, buff=0.4).align_to(answer, LEFT)
        
        formula = MathTex(
            r"x_{n+1} = (a \times x_n + b) \mod c",
            font_size=26, color=Colors.RANDOM_COLOR
        )
        formula.next_to(formula_title, DOWN, buff=0.15).set_x(0)
        
        formula_box = SurroundingRectangle(formula, color=Colors.RANDOM_COLOR, buff=0.15)
        
        self.play(FadeIn(formula_title), FadeIn(formula), Create(formula_box))
        self.wait(1)
        
        # 参数说明
        params = VGroup(
            VGroup(Text("a", font_size=16, color=Colors.RANDOM_COLOR), Text(" = 乘数", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
            VGroup(Text("b", font_size=16, color=Colors.RANDOM_COLOR), Text(" = 增量", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
            VGroup(Text("c", font_size=16, color=Colors.RANDOM_COLOR), Text(" = 模数（决定周期）", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
            VGroup(Text("x₀", font_size=16, color=Colors.BASE_COLOR), Text(" = 种子（初始值）", font_size=14, color=Colors.TEXT)).arrange(RIGHT, buff=0.08),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        params.next_to(formula_box, DOWN, buff=0.3).set_x(0)
        
        for param in params:
            self.play(FadeIn(param, shift=RIGHT * 0.1), run_time=0.3)
        
        self.wait(1)
        
        # 示例计算
        self.play(FadeOut(params))
        
        example_title = VGroup(
            Text("示例：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"a=5, b=3, c=16, x_0=7", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(formula_box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(example_title))
        
        # 计算过程
        a, b, c = 5, 3, 16
        x = 7
        calcs = []
        
        for i in range(5):
            new_x = (a * x + b) % c
            calc_text = f"x₁ = (5×{x}+3) mod 16 = {new_x}" if i == 0 else f"x_{i+1} = (5×{x}+3) mod 16 = {new_x}"
            calcs.append((x, new_x))
            x = new_x
        
        calc_items = VGroup()
        for i, (old, new) in enumerate(calcs):
            item = Text(f"x{i+1} = (5×{old}+3) mod 16 = {new}", font_size=14, color=Colors.TEXT)
            calc_items.add(item)
        
        calc_items.arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        calc_items.next_to(example_title, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        for item in calc_items:
            self.play(FadeIn(item), run_time=0.3)
        
        # 生成的序列
        seq_values = [7]
        x = 7
        for _ in range(5):
            x = (5 * x + 3) % 16
            seq_values.append(x)
        
        seq = VGroup(
            Text("生成序列：", font_size=14, color=Colors.RANDOM_COLOR),
            Text(", ".join(map(str, seq_values)) + ", ...", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        seq.next_to(calc_items, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(seq))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(question), FadeOut(answer),
            FadeOut(formula_title), FadeOut(formula), FadeOut(formula_box),
            FadeOut(example_title), FadeOut(calc_items), FadeOut(seq),
            run_time=0.5
        )
    
    def random_visualization(self):
        """随机数可视化"""
        section_title = Text("随机性可视化", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 生成一些伪随机数
        a, b, c = 1103515245, 12345, 2**31
        x = 42  # 种子
        
        points = []
        for _ in range(100):
            x = (a * x + b) % c
            px = (x % 1000) / 1000 * 4 - 2  # 归一化到 [-2, 2]
            x = (a * x + b) % c
            py = (x % 1000) / 1000 * 2.5 - 1.5  # 归一化到 [-1.5, 1]
            points.append((px, py))
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2, 1.5, 1],
            x_length=5,
            y_length=3,
            axis_config={"color": Colors.GRAY, "stroke_width": 1},
        )
        axes.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(Create(axes), run_time=0.5)
        
        # 绘制点
        dots = VGroup()
        for px, py in points[:50]:
            dot = Dot(
                axes.c2p(px, py),
                radius=0.04,
                color=Colors.RANDOM_COLOR
            )
            dots.add(dot)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in dots], lag_ratio=0.05),
            run_time=2
        )
        
        # 说明
        explain = VGroup(
            Text("看起来随机分布...", font_size=16, color=Colors.SECONDARY),
            Text("但其实是确定性的！", font_size=16, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.1)
        explain.next_to(axes, DOWN, buff=0.4)
        
        self.play(FadeIn(explain))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(axes), FadeOut(dots), FadeOut(explain),
            run_time=0.5
        )
    
    def applications(self):
        """应用场景"""
        section_title = Text("应用场景", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 应用列表
        apps = VGroup(
            VGroup(
                Text("① 游戏开发", font_size=18, color=Colors.PRIMARY),
                Text("随机地图、掉落物品、敌人AI", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(
                Text("② 模拟仿真", font_size=18, color=Colors.PRIMARY),
                Text("蒙特卡洛模拟、物理引擎", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(
                Text("③ 密码学（早期）", font_size=18, color=Colors.PRIMARY),
                Text("生成密钥、初始化向量", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
            VGroup(
                Text("④ 科学计算", font_size=18, color=Colors.PRIMARY),
                Text("随机采样、统计分析", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.08, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        apps.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for app in apps:
            self.play(FadeIn(app, shift=RIGHT * 0.2), run_time=0.5)
        
        self.wait(1)
        
        # 重要提醒
        warning = VGroup(
            Text("⚠️ 重要提醒：", font_size=18, color=Colors.ACCENT),
            Text("伪随机数不是真正随机！", font_size=16, color=Colors.TEXT),
            Text("相同种子 → 相同序列", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        warning.next_to(apps, DOWN, buff=0.4).set_x(0)
        
        warning_box = SurroundingRectangle(warning, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(warning), Create(warning_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(apps),
            FadeOut(warning), FadeOut(warning_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_03_linear_recurrence.py LinearRecurrence
    pass
