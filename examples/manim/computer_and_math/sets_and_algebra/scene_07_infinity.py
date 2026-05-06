"""
Scene 7: 无限的探索
介绍可数无限和不可数无限
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


class Scene07Infinity(Scene):
    """Scene 7: 无限的探索"""
    
    CHAPTER_TITLE = "第二章：集合与抽象代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_intro_infinity()
        self.section_countable_infinity()
        self.section_cantor_diagonal()
        self.section_infinity_hierarchy()
        
        clear_scene(self)
    
    def section_intro_infinity(self):
        """无限的引入"""
        # 小节标题
        section_title = Text("无限 - 没有尽头的世界", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题引入
        question = Text('无限有多"大"？所有无限都一样大吗？', font_size=20, color=Colors.GRAY)
        question.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question))
        self.wait(0.5)
        
        # 两种无限
        infinity_types = VGroup(
            VGroup(
                Text("可数无限", font_size=20, color=Colors.PRIMARY),
                Text("(Countably Infinite)", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("不可数无限", font_size=20, color=Colors.ACCENT),
                Text("(Uncountably Infinite)", font_size=14, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=2.0)
        infinity_types.next_to(question, DOWN, buff=0.6).set_x(0)
        
        # 可数无限框
        box1 = SurroundingRectangle(infinity_types[0], color=Colors.PRIMARY, buff=0.2)
        # 不可数无限框
        box2 = SurroundingRectangle(infinity_types[1], color=Colors.ACCENT, buff=0.2)
        
        self.play(FadeIn(infinity_types[0]), Create(box1))
        self.wait(0.3)
        self.play(FadeIn(infinity_types[1]), Create(box2))
        
        # 关键发现
        discovery = VGroup(
            Text("惊人发现: ", font_size=18, color=Colors.SECONDARY),
            Text('有些无限比另一些无限"更大"！', font_size=18, color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.1)
        discovery.next_to(infinity_types, DOWN, buff=0.8).set_x(0)
        
        self.play(FadeIn(discovery))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(question),
            FadeOut(infinity_types),
            FadeOut(box1),
            FadeOut(box2),
            FadeOut(discovery),
            run_time=0.5
        )
    
    def section_countable_infinity(self):
        """可数无限"""
        # 小节标题
        section_title = Text("可数无限", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("如果一个集合可以与自然数", font_size=18, color=Colors.GRAY),
            MathTex(r"\mathbb{N}", font_size=22, color=Colors.PRIMARY),
            Text("建立一一对应，则称为可数无限", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(0.5)
        
        # 自然数与整数的对应
        example_title = VGroup(
            Text("例: ", font_size=16, color=Colors.TEXT),
            MathTex(r"\mathbb{Z}", font_size=20, color=Colors.SET_B),
            Text(" 与 ", font_size=16, color=Colors.TEXT),
            MathTex(r"\mathbb{N}", font_size=20, color=Colors.PRIMARY),
            Text(" 的一一对应", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(definition, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_title))
        
        # 对应关系
        # N: 0, 1, 2, 3, 4, 5, 6, ...
        # Z: 0, 1,-1, 2,-2, 3,-3, ...
        
        n_row = VGroup(
            MathTex(r"\mathbb{N}:", font_size=18, color=Colors.PRIMARY),
            MathTex("0", font_size=16, color=Colors.TEXT),
            MathTex("1", font_size=16, color=Colors.TEXT),
            MathTex("2", font_size=16, color=Colors.TEXT),
            MathTex("3", font_size=16, color=Colors.TEXT),
            MathTex("4", font_size=16, color=Colors.TEXT),
            MathTex("5", font_size=16, color=Colors.TEXT),
            MathTex("6", font_size=16, color=Colors.TEXT),
            MathTex(r"\cdots", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.35)
        n_row.next_to(example_title, DOWN, buff=0.4).set_x(0)
        
        # 箭头
        arrows = VGroup()
        for i in range(1, 8):  # 跳过标签
            arrow = Arrow(
                n_row[i].get_bottom(),
                n_row[i].get_bottom() + DOWN * 0.4,
                buff=0.05,
                stroke_width=1.5,
                color=Colors.GRAY,
                max_tip_length_to_length_ratio=0.3
            )
            arrows.add(arrow)
        
        z_row = VGroup(
            MathTex(r"\mathbb{Z}:", font_size=18, color=Colors.SET_B),
            MathTex("0", font_size=16, color=Colors.TEXT),
            MathTex("1", font_size=16, color=Colors.TEXT),
            MathTex("-1", font_size=16, color=Colors.TEXT),
            MathTex("2", font_size=16, color=Colors.TEXT),
            MathTex("-2", font_size=16, color=Colors.TEXT),
            MathTex("3", font_size=16, color=Colors.TEXT),
            MathTex("-3", font_size=16, color=Colors.TEXT),
            MathTex(r"\cdots", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.3)
        z_row.next_to(n_row, DOWN, buff=0.8).align_to(n_row, LEFT)
        
        self.play(FadeIn(n_row))
        self.play(
            *[GrowArrow(arrow) for arrow in arrows],
            FadeIn(z_row),
            run_time=1
        )
        self.wait(0.5)
        
        # 结论
        conclusion = VGroup(
            Text("所以 ", font_size=16, color=Colors.TEXT),
            MathTex(r"|\mathbb{Z}| = |\mathbb{N}| = \aleph_0", font_size=22, color=Colors.PRIMARY),
            Text(" (阿列夫零)", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(z_row, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(conclusion))
        
        # 其他可数集
        more = VGroup(
            Text("同样可数:", font_size=14, color=Colors.TEXT),
            MathTex(r"\mathbb{Q}", font_size=18, color=Colors.SECONDARY),
            Text(" (有理数), ", font_size=14, color=Colors.TEXT),
            MathTex(r"\mathbb{N} \times \mathbb{N}", font_size=18, color=Colors.SECONDARY),
            Text(" (自然数对)", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        more.next_to(conclusion, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(more))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(definition),
            FadeOut(example_title),
            FadeOut(n_row),
            FadeOut(arrows),
            FadeOut(z_row),
            FadeOut(conclusion),
            FadeOut(more),
            run_time=0.5
        )
    
    def section_cantor_diagonal(self):
        """康托尔对角线论证"""
        # 小节标题
        section_title = Text("康托尔对角线论证", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 引入
        intro = VGroup(
            Text("实数", font_size=18, color=Colors.TEXT),
            MathTex(r"\mathbb{R}", font_size=22, color=Colors.ACCENT),
            Text(" 能与自然数一一对应吗？", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        self.wait(0.5)
        
        # 假设可以枚举 (0,1) 之间的所有实数
        assume = Text("假设可以列出 (0,1) 之间所有实数:", font_size=16, color=Colors.GRAY)
        assume.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(assume))
        
        # 构造列表（简化的对角线论证）
        # 每行是一个实数的小数展开
        rows = [
            ["r_1", "0", ".", "5", "1", "4", "2", "..."],
            ["r_2", "0", ".", "3", "7", "8", "9", "..."],
            ["r_3", "0", ".", "2", "4", "6", "1", "..."],
            ["r_4", "0", ".", "1", "5", "9", "3", "..."],
        ]
        
        matrix = VGroup()
        diagonal_positions = []
        
        for i, row in enumerate(rows):
            row_group = VGroup()
            for j, val in enumerate(row):
                if j == 0:
                    tex = MathTex(val, font_size=16, color=Colors.SET_B)
                else:
                    tex = MathTex(val, font_size=16, color=Colors.TEXT)
                row_group.add(tex)
            row_group.arrange(RIGHT, buff=0.15)
            matrix.add(row_group)
            # 记录对角线位置 (跳过 r_i, 0, . 所以是 i+3)
            diagonal_positions.append((i, i + 3))
        
        matrix.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        matrix.next_to(assume, DOWN, buff=0.4).shift(LEFT * 0.5)
        
        self.play(FadeIn(matrix))
        self.wait(0.5)
        
        # 高亮对角线
        diagonal_highlights = VGroup()
        for i, j in diagonal_positions:
            highlight = SurroundingRectangle(
                matrix[i][j],
                color=Colors.ACCENT,
                buff=0.05
            )
            diagonal_highlights.add(highlight)
        
        self.play(*[Create(h) for h in diagonal_highlights])
        self.wait(0.3)
        
        # 对角线数字
        diagonal_desc = VGroup(
            Text("对角线: ", font_size=14, color=Colors.TEXT),
            MathTex("5, 7, 6, 5, ...", font_size=18, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.1)
        diagonal_desc.next_to(matrix, RIGHT, buff=0.5)
        
        self.play(FadeIn(diagonal_desc))
        
        # 构造新数
        new_number = VGroup(
            Text("新数 (每位+1): ", font_size=14, color=Colors.TEXT),
            MathTex("0.6870...", font_size=18, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        new_number.next_to(diagonal_desc, DOWN, buff=0.3).align_to(diagonal_desc, LEFT)
        
        self.play(FadeIn(new_number))
        self.wait(0.5)
        
        # 矛盾
        contradiction = VGroup(
            Text("这个新数", font_size=14, color=Colors.TEXT),
            Text("不在列表中", font_size=14, color=Colors.ACCENT),
            Text("！", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.05)
        contradiction.next_to(matrix, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(contradiction))
        
        # 结论
        conclusion = VGroup(
            Text("结论: ", font_size=16, color=Colors.TEXT),
            MathTex(r"|\mathbb{R}| > |\mathbb{N}|", font_size=22, color=Colors.PRIMARY),
            Text(" 实数是不可数的！", font_size=16, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        conclusion.to_edge(DOWN, buff=0.5).set_x(0)
        
        box = SurroundingRectangle(conclusion, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(box))
        self.wait(2)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(intro),
            FadeOut(assume),
            FadeOut(matrix),
            FadeOut(diagonal_highlights),
            FadeOut(diagonal_desc),
            FadeOut(new_number),
            FadeOut(contradiction),
            FadeOut(conclusion),
            FadeOut(box),
            run_time=0.5
        )
    
    def section_infinity_hierarchy(self):
        """无限的层级"""
        # 小节标题
        section_title = Text("无限的阶梯", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 关键定理
        theorem = VGroup(
            Text("康托尔定理: ", font_size=18, color=Colors.TEXT),
            MathTex(r"|A| < |\mathcal{P}(A)|", font_size=24, color=Colors.PRIMARY),
        ).arrange(RIGHT, buff=0.1)
        theorem.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(theorem))
        
        explanation = Text("任何集合都比它的幂集"小"", font_size=16, color=Colors.GRAY)
        explanation.next_to(theorem, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(explanation))
        self.wait(0.5)
        
        # 无限阶梯
        ladder_title = Text("无限的阶梯:", font_size=18, color=Colors.TEXT)
        ladder_title.next_to(explanation, DOWN, buff=0.5).align_to(explanation, LEFT)
        
        self.play(FadeIn(ladder_title))
        
        # 创建阶梯图
        levels = [
            (r"|\mathbb{N}| = \aleph_0", "可数无限", 0, Colors.PRIMARY),
            (r"|\mathcal{P}(\mathbb{N})| = |\mathbb{R}| = \aleph_1", "连续统", 1, Colors.SECONDARY),
            (r"|\mathcal{P}(\mathcal{P}(\mathbb{N}))|", "更高层级", 2, Colors.INTERSECTION),
            (r"\cdots", "无穷无尽", 3, Colors.ACCENT),
        ]
        
        ladder = VGroup()
        for formula, desc, level, color in levels:
            step = VGroup(
                RoundedRectangle(
                    width=4.5 - level * 0.3,
                    height=0.6,
                    corner_radius=0.1,
                    fill_color=color,
                    fill_opacity=0.3,
                    stroke_color=color,
                    stroke_width=2
                ),
            )
            formula_tex = MathTex(formula, font_size=18, color=Colors.TEXT)
            formula_tex.move_to(step[0].get_center() + LEFT * 0.3)
            
            desc_text = Text(desc, font_size=12, color=Colors.GRAY)
            desc_text.move_to(step[0].get_center() + RIGHT * 1.2)
            
            step.add(formula_tex, desc_text)
            ladder.add(step)
        
        ladder.arrange(UP, buff=0.15)
        ladder.next_to(ladder_title, DOWN, buff=0.3).set_x(0)
        
        for step in ladder:
            self.play(FadeIn(step, shift=UP * 0.2), run_time=0.5)
            self.wait(0.2)
        
        # 洞见
        insight = VGroup(
            Text("无限不是一个数，而是一个", font_size=16, color=Colors.TEXT),
            Text("无穷无尽的阶梯", font_size=16, color=Colors.PRIMARY),
            Text("！", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.05)
        insight.to_edge(DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(insight))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_07_infinity.py Scene07Infinity
    pass
