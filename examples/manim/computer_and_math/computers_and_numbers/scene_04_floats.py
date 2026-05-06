"""
Scene 4: 浮点数的存储 - IEEE 754 标准
解释浮点数的存储结构，揭示精度问题的根源
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#FF6B6B"    # 警示红
    ACCENT = "#4ECDC4"       # 青绿
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    BINARY_0 = "#2C3E50"     # 0的颜色
    BINARY_1 = "#F39C12"     # 1的颜色
    SIGN_COLOR = "#E74C3C"   # 符号位颜色
    EXP_COLOR = "#3498DB"    # 指数位颜色
    MANTISSA_COLOR = "#2ECC71"  # 尾数位颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_ieee754_structure(width=10, height=0.8):
    """创建 IEEE 754 32位浮点数结构图"""
    # 各部分的比例
    sign_width = width * (1/32)
    exp_width = width * (8/32)
    mantissa_width = width * (23/32)
    
    # 创建三个矩形
    sign_rect = Rectangle(width=sign_width, height=height)
    sign_rect.set_fill(Colors.SIGN_COLOR, opacity=0.7)
    sign_rect.set_stroke(Colors.TEXT, width=2)
    
    exp_rect = Rectangle(width=exp_width, height=height)
    exp_rect.set_fill(Colors.EXP_COLOR, opacity=0.7)
    exp_rect.set_stroke(Colors.TEXT, width=2)
    
    mantissa_rect = Rectangle(width=mantissa_width, height=height)
    mantissa_rect.set_fill(Colors.MANTISSA_COLOR, opacity=0.7)
    mantissa_rect.set_stroke(Colors.TEXT, width=2)
    
    # 排列
    structure = VGroup(sign_rect, exp_rect, mantissa_rect)
    structure.arrange(RIGHT, buff=0)
    
    # 添加标签
    sign_label = Text("S", font_size=18, color=Colors.TEXT)
    sign_label.move_to(sign_rect.get_center())
    
    exp_label = Text("指数 (8位)", font_size=16, color=Colors.TEXT)
    exp_label.move_to(exp_rect.get_center())
    
    mantissa_label = Text("尾数 (23位)", font_size=16, color=Colors.TEXT)
    mantissa_label.move_to(mantissa_rect.get_center())
    
    # 位数标注
    sign_bits = Text("1位", font_size=12, color=Colors.SIGN_COLOR)
    sign_bits.next_to(sign_rect, UP, buff=0.1)
    
    exp_bits = Text("8位", font_size=12, color=Colors.EXP_COLOR)
    exp_bits.next_to(exp_rect, UP, buff=0.1)
    
    mantissa_bits = Text("23位", font_size=12, color=Colors.MANTISSA_COLOR)
    mantissa_bits.next_to(mantissa_rect, UP, buff=0.1)
    
    return VGroup(
        structure,
        sign_label, exp_label, mantissa_label,
        sign_bits, exp_bits, mantissa_bits
    )


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene04Floats(Scene):
    """Scene 4: 浮点数存储"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_why_approximate()
        self.section_ieee754_structure()
        self.section_scientific_notation()
        self.section_point_one_truth()
        
        clear_scene(self)
    
    def section_why_approximate(self):
        """为什么小数不能精确存储"""
        # 小节标题
        section_title = Text("浮点数: 近似存储", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 问题
        question = Text("为什么小数不能像整数一样精确存储?", font_size=22, color=Colors.GRAY)
        question.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question))
        self.wait(0.5)
        
        # 原因1: 实数是无限的
        reason1 = VGroup(
            Text("原因1: ", font_size=20, color=Colors.ACCENT),
            Text("实数是无限的 (如 ", font_size=20, color=Colors.TEXT),
            MathTex(r"\pi", font_size=24, color=Colors.PRIMARY),
            Text(" = 3.14159265...)", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        reason1.next_to(question, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(reason1))
        self.wait(0.5)
        
        # 原因2: 内存是有限的
        reason2 = VGroup(
            Text("原因2: ", font_size=20, color=Colors.ACCENT),
            Text("计算机内存是有限的", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        reason2.next_to(reason1, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(reason2))
        self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            Text("结论: ", font_size=20, color=Colors.SECONDARY),
            Text("只能存储最接近的近似值", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(reason2, DOWN, buff=0.4).set_x(0)
        
        box = SurroundingRectangle(conclusion, color=Colors.SECONDARY, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(box))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(question),
            FadeOut(reason1),
            FadeOut(reason2),
            FadeOut(conclusion),
            FadeOut(box),
            run_time=0.5
        )
    
    def section_ieee754_structure(self):
        """IEEE 754 结构"""
        # 小节标题
        section_title = Text("IEEE 754: 国际标准浮点数格式", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 32位浮点数
        format_label = Text("32位单精度浮点数结构:", font_size=20, color=Colors.GRAY)
        format_label.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(format_label))
        
        # 创建结构图
        ieee_struct = create_ieee754_structure(width=9, height=0.7)
        ieee_struct.next_to(format_label, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(ieee_struct), run_time=1)
        self.wait(0.5)
        
        # 各部分说明
        explanations = VGroup()
        
        # 符号位说明
        sign_exp = VGroup(
            Text("S (符号位): ", font_size=18, color=Colors.SIGN_COLOR),
            Text("0=正, 1=负", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explanations.add(sign_exp)
        
        # 指数位说明
        exp_exp = VGroup(
            Text("指数位: ", font_size=18, color=Colors.EXP_COLOR),
            Text("决定数值的大小范围", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explanations.add(exp_exp)
        
        # 尾数位说明
        mantissa_exp = VGroup(
            Text("尾数位: ", font_size=18, color=Colors.MANTISSA_COLOR),
            Text("决定数值的精度", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        explanations.add(mantissa_exp)
        
        explanations.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        explanations.next_to(ieee_struct, DOWN, buff=0.5).set_x(0)
        
        for exp in explanations:
            self.play(FadeIn(exp, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(format_label),
            FadeOut(ieee_struct),
            FadeOut(explanations),
            run_time=0.5
        )
    
    def section_scientific_notation(self):
        """科学计数法类比"""
        # 小节标题
        section_title = Text("原理: 二进制科学计数法", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 十进制科学计数法
        decimal_title = Text("十进制科学计数法:", font_size=20, color=Colors.GRAY)
        decimal_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(decimal_title))
        
        decimal_example = MathTex(
            r"6.022 \times 10^{23}",
            font_size=32, color=Colors.PRIMARY
        )
        decimal_example.next_to(decimal_title, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(decimal_example))
        self.wait(0.5)
        
        # 二进制科学计数法
        binary_title = Text("二进制浮点数:", font_size=20, color=Colors.GRAY)
        binary_title.next_to(decimal_example, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(binary_title))
        
        binary_formula = MathTex(
            r"\pm 1.xxxxx \times 2^{E}",
            font_size=32, color=Colors.ACCENT
        )
        binary_formula.next_to(binary_title, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(binary_formula))
        self.wait(0.5)
        
        # 各部分对应
        mapping = VGroup(
            VGroup(
                MathTex(r"\pm", font_size=24, color=Colors.SIGN_COLOR),
                Text(" = 符号位 S", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"xxxxx", font_size=24, color=Colors.MANTISSA_COLOR),
                Text(" = 尾数 M", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                MathTex(r"E", font_size=24, color=Colors.EXP_COLOR),
                Text(" = 指数 (需偏移)", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        mapping.next_to(binary_formula, DOWN, buff=0.4).set_x(0)
        
        for m in mapping:
            self.play(FadeIn(m, shift=RIGHT * 0.2), run_time=0.35)
        
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(decimal_title),
            FadeOut(decimal_example),
            FadeOut(binary_title),
            FadeOut(binary_formula),
            FadeOut(mapping),
            run_time=0.5
        )
    
    def section_point_one_truth(self):
        """0.1 的真相"""
        # 小节标题
        section_title = Text("揭秘: 0.1 的真相", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 问题回顾
        recall = VGroup(
            Text("还记得开头的问题吗?", font_size=20, color=Colors.GRAY),
        )
        recall.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(recall))
        
        code_result = Text(
            "0.1 + 0.2 = 0.30000000000000004",
            font_size=20, color=Colors.SECONDARY, font="Menlo"
        )
        code_result.next_to(recall, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(code_result))
        self.wait(0.5)
        
        # 原因揭示
        truth_title = Text("原因:", font_size=22, color=Colors.ACCENT)
        truth_title.next_to(code_result, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(truth_title))
        
        # 0.1 在二进制中是无限循环小数
        truth1 = VGroup(
            Text("0.1 在二进制中是", font_size=20, color=Colors.TEXT),
            Text("无限循环小数", font_size=20, color=Colors.SECONDARY),
            Text("!", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        truth1.next_to(truth_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(truth1))
        self.wait(0.3)
        
        # 二进制表示
        binary_rep = VGroup(
            MathTex(r"0.1_{10}", font_size=24, color=Colors.PRIMARY),
            Text(" = ", font_size=20, color=Colors.TEXT),
            MathTex(r"0.0001100110011..._2", font_size=22, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        binary_rep.next_to(truth1, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(binary_rep))
        self.wait(0.5)
        
        # 省略号动画 - 强调无限
        dots = Text("...(无限循环)", font_size=18, color=Colors.SECONDARY)
        dots.next_to(binary_rep, RIGHT, buff=0.1)
        
        self.play(FadeIn(dots, scale=1.2))
        self.wait(0.5)
        
        # 舍入
        truncate = VGroup(
            Text("存储时必须截断 → ", font_size=18, color=Colors.GRAY),
            Text("精度丢失!", font_size=20, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        truncate.next_to(binary_rep, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(truncate))
        self.wait(0.5)
        
        # 最终解释
        final_box = VGroup(
            Text("0.1 和 0.2 各自存储时都有微小误差", font_size=18, color=Colors.TEXT),
            Text("相加后误差累积, 出现了那个奇怪的结果", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        final_box.next_to(truncate, DOWN, buff=0.4).set_x(0)
        
        box = SurroundingRectangle(final_box, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(final_box), Create(box))
        self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            Text("这不是Bug, 而是", font_size=20, color=Colors.TEXT),
            Text("有限内存的必然结果", font_size=20, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(box, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(conclusion))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_04_floats.py Scene04Floats
    pass
