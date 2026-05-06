"""
递推与递归 - Scene 5: 解递推关系
展示如何用特征方程求解递推关系的直接公式

渲染命令: manim -pqh scene_05_solving_recurrence.py SolvingRecurrence
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
    FORMULA_COLOR = "#E67E22" # 公式橙
    FIBO_COLOR = "#E91E63"   # 斐波那契粉
    GOLDEN_COLOR = "#FFD700" # 黄金色


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


# ========== Scene 5: 解递推关系 ==========
class SolvingRecurrence(Scene):
    """解递推关系"""
    
    CHAPTER_TITLE = "第六章：递推与递归"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.why_solve()
        self.first_order_solution()
        self.second_order_solution()
        self.binet_formula()
        
        clear_scene(self)
    
    def why_solve(self):
        """为什么需要求解"""
        section_title = Text("为什么需要直接公式？", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题
        problem = VGroup(
            Text("问题：", font_size=18, color=Colors.PRIMARY),
            Text("想知道第 1000 项，难道要算 999 次？", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        problem.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(problem))
        self.wait(0.5)
        
        # 对比
        comparison = VGroup(
            VGroup(
                Text("递推计算：", font_size=16, color=Colors.ACCENT),
                MathTex(r"a_1 \to a_2 \to \cdots \to a_n", font_size=20, color=Colors.TEXT),
                Text("需要 n-1 步", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("直接公式：", font_size=16, color=Colors.SECONDARY),
                MathTex(r"a_n = f(n)", font_size=20, color=Colors.SECONDARY),
                Text("一步到位！", font_size=14, color=Colors.SECONDARY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        comparison.next_to(problem, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(comparison))
        self.wait(1)
        
        # 方法预告
        method = VGroup(
            Text("方法：", font_size=18, color=Colors.FORMULA_COLOR),
            Text("特征方程法", font_size=18, color=Colors.FORMULA_COLOR),
        ).arrange(RIGHT, buff=0.1)
        method.next_to(comparison, DOWN, buff=0.4)
        
        method_box = SurroundingRectangle(method, color=Colors.FORMULA_COLOR, buff=0.15)
        
        self.play(FadeIn(method), Create(method_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(problem),
            FadeOut(comparison), FadeOut(method), FadeOut(method_box),
            run_time=0.5
        )
    
    def first_order_solution(self):
        """一阶递推的解法"""
        section_title = Text("一阶递推的解法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 示例
        example = VGroup(
            Text("示例：", font_size=18, color=Colors.PRIMARY),
            MathTex(r"a_n = r \cdot a_{n-1}", font_size=24, color=Colors.RECUR_COLOR),
        ).arrange(RIGHT, buff=0.1)
        example.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example))
        
        # 步骤1：特征方程
        step1_title = Text("步骤1：构造特征方程", font_size=16, color=Colors.SECONDARY)
        step1_title.next_to(example, DOWN, buff=0.4).align_to(example, LEFT)
        
        step1 = MathTex(r"x - r = 0", font_size=22, color=Colors.FORMULA_COLOR)
        step1.next_to(step1_title, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(step1_title), FadeIn(step1))
        self.wait(0.5)
        
        # 步骤2：解方程
        step2_title = Text("步骤2：解方程", font_size=16, color=Colors.SECONDARY)
        step2_title.next_to(step1, DOWN, buff=0.3).align_to(step1_title, LEFT)
        
        step2 = MathTex(r"x = r", font_size=22, color=Colors.FORMULA_COLOR)
        step2.next_to(step2_title, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(step2_title), FadeIn(step2))
        self.wait(0.5)
        
        # 步骤3：写出通解
        step3_title = Text("步骤3：通解形式", font_size=16, color=Colors.SECONDARY)
        step3_title.next_to(step2, DOWN, buff=0.3).align_to(step2_title, LEFT)
        
        step3 = MathTex(r"a_n = A \cdot r^n", font_size=22, color=Colors.FORMULA_COLOR)
        step3.next_to(step3_title, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(step3_title), FadeIn(step3))
        self.wait(0.5)
        
        # 步骤4：确定常数
        step4_title = Text("步骤4：用初始值确定 A", font_size=16, color=Colors.SECONDARY)
        step4_title.next_to(step3, DOWN, buff=0.3).align_to(step3_title, LEFT)
        
        step4 = VGroup(
            MathTex(r"a_1 = A \cdot r^1 = A \cdot r", font_size=18, color=Colors.TEXT),
            MathTex(r"\Rightarrow A = \frac{a_1}{r}", font_size=18, color=Colors.FORMULA_COLOR),
        ).arrange(DOWN, buff=0.1)
        step4.next_to(step4_title, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(step4_title), FadeIn(step4))
        self.wait(1)
        
        # 最终公式
        final = VGroup(
            Text("最终公式：", font_size=16, color=Colors.PRIMARY),
            MathTex(r"a_n = a_1 \cdot r^{n-1}", font_size=24, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.1)
        final.next_to(step4, DOWN, buff=0.4).set_x(0)
        
        final_box = SurroundingRectangle(final, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(final), Create(final_box))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(example),
            FadeOut(step1_title), FadeOut(step1),
            FadeOut(step2_title), FadeOut(step2),
            FadeOut(step3_title), FadeOut(step3),
            FadeOut(step4_title), FadeOut(step4),
            FadeOut(final), FadeOut(final_box),
            run_time=0.5
        )
    
    def second_order_solution(self):
        """二阶递推的解法（斐波那契）"""
        section_title = Text("二阶递推的解法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 斐波那契递推
        example = VGroup(
            Text("斐波那契数列：", font_size=18, color=Colors.FIBO_COLOR),
            MathTex(r"a_n = a_{n-1} + a_{n-2}", font_size=24, color=Colors.FIBO_COLOR),
        ).arrange(RIGHT, buff=0.1)
        example.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example))
        
        # 特征方程
        step1 = VGroup(
            Text("特征方程：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"x^2 - x - 1 = 0", font_size=22, color=Colors.FORMULA_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        step1.next_to(example, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(step1))
        self.wait(0.5)
        
        # 求解
        step2 = VGroup(
            Text("解方程：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"x = \frac{1 \pm \sqrt{5}}{2}", font_size=22, color=Colors.FORMULA_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        step2.next_to(step1, DOWN, buff=0.3).align_to(step1, LEFT)
        
        self.play(FadeIn(step2))
        self.wait(0.5)
        
        # 黄金比例！
        golden_title = Text("这就是著名的黄金比例！", font_size=16, color=Colors.GOLDEN_COLOR)
        golden_title.next_to(step2, DOWN, buff=0.3).set_x(0)
        
        golden = VGroup(
            MathTex(r"\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618", font_size=22, color=Colors.GOLDEN_COLOR),
            MathTex(r"\psi = \frac{1 - \sqrt{5}}{2} \approx -0.618", font_size=20, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        golden.next_to(golden_title, DOWN, buff=0.2)
        
        self.play(FadeIn(golden_title), FadeIn(golden))
        
        # 高亮黄金比例
        phi_box = SurroundingRectangle(golden[0], color=Colors.GOLDEN_COLOR, buff=0.1)
        self.play(Create(phi_box))
        self.wait(1)
        
        # 通解形式
        general = VGroup(
            Text("通解形式：", font_size=16, color=Colors.SECONDARY),
            MathTex(r"a_n = A \cdot \varphi^n + B \cdot \psi^n", font_size=22, color=Colors.FORMULA_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        general.next_to(golden, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeOut(phi_box), FadeIn(general))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(example),
            FadeOut(step1), FadeOut(step2),
            FadeOut(golden_title), FadeOut(golden),
            FadeOut(general),
            run_time=0.5
        )
    
    def binet_formula(self):
        """比内公式"""
        section_title = Text("比内公式", font_size=26, color=Colors.FIBO_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 说明
        intro = Text("代入初始值后，得到斐波那契数列的直接公式：", font_size=16, color=Colors.TEXT)
        intro.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 比内公式
        binet = MathTex(
            r"F_n = \frac{\varphi^n - \psi^n}{\sqrt{5}}",
            font_size=32, color=Colors.FIBO_COLOR
        )
        binet.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        binet_box = SurroundingRectangle(binet, color=Colors.FIBO_COLOR, buff=0.2)
        
        self.play(FadeIn(binet), Create(binet_box))
        self.wait(1)
        
        # 简化形式
        simplified = MathTex(
            r"F_n = \frac{1}{\sqrt{5}} \left[ \left(\frac{1+\sqrt{5}}{2}\right)^n - \left(\frac{1-\sqrt{5}}{2}\right)^n \right]",
            font_size=20, color=Colors.GRAY
        )
        simplified.next_to(binet_box, DOWN, buff=0.3)
        
        self.play(FadeIn(simplified))
        self.wait(0.5)
        
        # 魔力展示
        magic_title = Text("神奇之处：", font_size=18, color=Colors.SECONDARY)
        magic_title.next_to(simplified, DOWN, buff=0.4).align_to(intro, LEFT)
        
        self.play(FadeIn(magic_title))
        
        # 计算示例
        calc_title = Text("直接计算 F₁₀：", font_size=16, color=Colors.PRIMARY)
        calc_title.next_to(magic_title, DOWN, buff=0.2).align_to(magic_title, LEFT)
        
        # φ^10 ≈ 122.99, ψ^10 ≈ 0.0081, (φ^10 - ψ^10)/√5 ≈ 55
        phi_10 = (1 + np.sqrt(5)) / 2
        phi_10_pow = phi_10 ** 10
        psi_10_pow = ((1 - np.sqrt(5)) / 2) ** 10
        f_10 = int(round((phi_10_pow - psi_10_pow) / np.sqrt(5)))
        
        calc = VGroup(
            Text(f"F₁₀ ≈ ({phi_10_pow:.2f} - {psi_10_pow:.4f}) / √5", font_size=14, color=Colors.TEXT),
            Text(f"= {f_10}", font_size=18, color=Colors.FIBO_COLOR),
        ).arrange(DOWN, buff=0.1)
        calc.next_to(calc_title, DOWN, buff=0.15).shift(RIGHT * 0.3)
        
        self.play(FadeIn(calc_title), FadeIn(calc))
        self.wait(0.5)
        
        # 对比
        comparison = VGroup(
            Text("对比：", font_size=16, color=Colors.GRAY),
            Text("递推需要 9 步，直接公式只需 1 步！", font_size=14, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        comparison.next_to(calc, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(comparison))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(intro),
            FadeOut(binet), FadeOut(binet_box), FadeOut(simplified),
            FadeOut(magic_title), FadeOut(calc_title), FadeOut(calc),
            FadeOut(comparison),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_05_solving_recurrence.py SolvingRecurrence
    pass
