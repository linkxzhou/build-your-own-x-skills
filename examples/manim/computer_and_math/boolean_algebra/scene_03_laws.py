"""
Scene 3: 核心定律
介绍布尔代数的核心定律，建立公理系统概念
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    ZERO = "#2C3E50"         # 0的颜色
    ONE = "#F39C12"          # 1的颜色
    AND_COLOR = "#E74C3C"    # AND颜色
    OR_COLOR = "#3498DB"     # OR颜色
    NOT_COLOR = "#9B59B6"    # NOT颜色
    XOR_COLOR = "#2ECC71"    # XOR颜色


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_law_card(name, formula, description, color, width=3.2, height=1.4):
    """创建定律卡片"""
    card = VGroup()
    
    # 背景框
    bg = RoundedRectangle(
        corner_radius=0.1,
        width=width,
        height=height,
        fill_color=Colors.BG,
        fill_opacity=0.9,
        stroke_color=color,
        stroke_width=2
    )
    
    # 定律名称
    name_text = Text(name, font_size=16, color=color)
    name_text.move_to(bg.get_top() + DOWN * 0.25)
    
    # 公式
    formula_text = MathTex(formula, font_size=22, color=Colors.TEXT)
    formula_text.move_to(bg.get_center() + DOWN * 0.05)
    
    # 描述
    desc_text = Text(description, font_size=12, color=Colors.GRAY)
    desc_text.move_to(bg.get_bottom() + UP * 0.25)
    
    card.add(bg, name_text, formula_text, desc_text)
    return card


def create_venn_diagram(set_a_color, set_b_color, overlap_color, result_color, 
                        label="", circle_radius=0.5, center_offset=0.3):
    """创建韦恩图"""
    venn = VGroup()
    
    # 两个圆
    circle_a = Circle(radius=circle_radius)
    circle_a.set_stroke(set_a_color, width=2)
    circle_a.shift(LEFT * center_offset)
    
    circle_b = Circle(radius=circle_radius)
    circle_b.set_stroke(set_b_color, width=2)
    circle_b.shift(RIGHT * center_offset)
    
    # 标签
    label_a = Text("A", font_size=14, color=set_a_color)
    label_a.next_to(circle_a, LEFT, buff=0.1)
    
    label_b = Text("B", font_size=14, color=set_b_color)
    label_b.next_to(circle_b, RIGHT, buff=0.1)
    
    venn.add(circle_a, circle_b, label_a, label_b)
    
    if label:
        title = Text(label, font_size=12, color=Colors.GRAY)
        title.next_to(venn, DOWN, buff=0.1)
        venn.add(title)
    
    return venn


def clear_scene(scene):
    """清理场景"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene03Laws(Scene):
    """Scene 3: 核心定律"""
    
    CHAPTER_TITLE = "第三章：布尔代数"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_intro()
        self.section_basic_laws()
        self.section_identity_complement()
        self.section_demorgan()
        self.section_summary()
        
        clear_scene(self)
    
    def section_intro(self):
        """引入：为什么需要定律"""
        section_title = Text("布尔代数的核心定律", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 引言
        intro = VGroup(
            Text("就像普通代数有加法、乘法的运算规则一样，", font_size=16, color=Colors.GRAY),
            Text("布尔代数也有自己的一套定律体系。", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        intro.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(intro))
        self.wait(1)
        
        # 提示
        hint = Text("这些定律是简化逻辑表达式的有力工具！", font_size=16, color=Colors.PRIMARY)
        hint.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(hint, scale=0.9))
        self.wait(1.5)
        
        # 清除
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(hint), run_time=0.5)
    
    def section_basic_laws(self):
        """基本定律：交换律、结合律、分配律"""
        section_title = Text("基本定律", font_size=22, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title))
        
        # === 交换律 ===
        commutative_title = Text("交换律 (Commutative)", font_size=18, color=Colors.PRIMARY)
        commutative_title.next_to(section_title, DOWN, buff=0.4).align_to(section_title, LEFT).shift(LEFT * 2)
        
        self.play(FadeIn(commutative_title))
        
        comm_formulas = VGroup(
            MathTex(r"a \lor b = b \lor a", font_size=22, color=Colors.OR_COLOR),
            MathTex(r"a \land b = b \land a", font_size=22, color=Colors.AND_COLOR),
        ).arrange(RIGHT, buff=0.8)
        comm_formulas.next_to(commutative_title, DOWN, buff=0.2)
        
        comm_desc = Text("交换操作数的顺序，结果不变", font_size=14, color=Colors.GRAY)
        comm_desc.next_to(comm_formulas, DOWN, buff=0.15)
        
        self.play(Write(comm_formulas))
        self.play(FadeIn(comm_desc))
        self.wait(0.8)
        
        # === 结合律 ===
        associative_title = Text("结合律 (Associative)", font_size=18, color=Colors.PRIMARY)
        associative_title.next_to(comm_desc, DOWN, buff=0.35).align_to(commutative_title, LEFT)
        
        self.play(FadeIn(associative_title))
        
        assoc_formulas = VGroup(
            MathTex(r"a \lor (b \lor c) = (a \lor b) \lor c", font_size=20, color=Colors.OR_COLOR),
            MathTex(r"a \land (b \land c) = (a \land b) \land c", font_size=20, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.15)
        assoc_formulas.next_to(associative_title, DOWN, buff=0.2)
        
        assoc_desc = Text("改变括号位置，结果不变", font_size=14, color=Colors.GRAY)
        assoc_desc.next_to(assoc_formulas, DOWN, buff=0.15)
        
        self.play(Write(assoc_formulas))
        self.play(FadeIn(assoc_desc))
        self.wait(0.8)
        
        # === 分配律 ===
        distributive_title = Text("分配律 (Distributive)", font_size=18, color=Colors.PRIMARY)
        distributive_title.next_to(assoc_desc, DOWN, buff=0.35).align_to(commutative_title, LEFT)
        
        self.play(FadeIn(distributive_title))
        
        dist_formulas = VGroup(
            MathTex(r"a \land (b \lor c) = (a \land b) \lor (a \land c)", font_size=20, color=Colors.AND_COLOR),
            MathTex(r"a \lor (b \land c) = (a \lor b) \land (a \lor c)", font_size=20, color=Colors.OR_COLOR),
        ).arrange(DOWN, buff=0.15)
        dist_formulas.next_to(distributive_title, DOWN, buff=0.2)
        
        dist_desc = Text("注意：第二条在普通代数中不成立！", font_size=14, color=Colors.ACCENT)
        dist_desc.next_to(dist_formulas, DOWN, buff=0.15)
        
        self.play(Write(dist_formulas))
        self.play(FadeIn(dist_desc))
        
        # 高亮第二条
        highlight = SurroundingRectangle(dist_formulas[1], color=Colors.ACCENT, buff=0.1)
        self.play(Create(highlight), run_time=0.5)
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, commutative_title, comm_formulas, comm_desc,
            associative_title, assoc_formulas, assoc_desc,
            distributive_title, dist_formulas, dist_desc, highlight
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_identity_complement(self):
        """同一律和互补律"""
        section_title = Text("特殊定律", font_size=22, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title))
        
        # 创建两列布局
        left_col = VGroup()
        right_col = VGroup()
        
        # === 同一律 (左列) ===
        identity_title = Text("同一律 (Identity)", font_size=18, color=Colors.PRIMARY)
        
        identity_formulas = VGroup(
            MathTex(r"a \lor 0 = a", font_size=22, color=Colors.OR_COLOR),
            MathTex(r"a \land 1 = a", font_size=22, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.2)
        
        identity_desc = VGroup(
            Text("0是OR的单位元", font_size=12, color=Colors.GRAY),
            Text("1是AND的单位元", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        left_col.add(identity_title, identity_formulas, identity_desc)
        left_col.arrange(DOWN, buff=0.2)
        
        # === 零一律 (中列) ===
        zero_one_title = Text("零一律 (Annihilator)", font_size=18, color=Colors.PRIMARY)
        
        zero_one_formulas = VGroup(
            MathTex(r"a \lor 1 = 1", font_size=22, color=Colors.OR_COLOR),
            MathTex(r"a \land 0 = 0", font_size=22, color=Colors.AND_COLOR),
        ).arrange(DOWN, buff=0.2)
        
        zero_one_desc = VGroup(
            Text("1是OR的零化元", font_size=12, color=Colors.GRAY),
            Text("0是AND的零化元", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        middle_col = VGroup(zero_one_title, zero_one_formulas, zero_one_desc)
        middle_col.arrange(DOWN, buff=0.2)
        
        # === 互补律 (右列) ===
        complement_title = Text("互补律 (Complement)", font_size=18, color=Colors.PRIMARY)
        
        complement_formulas = VGroup(
            MathTex(r"a \lor \neg a = 1", font_size=22, color=Colors.NOT_COLOR),
            MathTex(r"a \land \neg a = 0", font_size=22, color=Colors.NOT_COLOR),
        ).arrange(DOWN, buff=0.2)
        
        complement_desc = VGroup(
            Text("排中律", font_size=12, color=Colors.GRAY),
            Text("矛盾律", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        right_col.add(complement_title, complement_formulas, complement_desc)
        right_col.arrange(DOWN, buff=0.2)
        
        # 排列三列
        all_cols = VGroup(left_col, middle_col, right_col).arrange(RIGHT, buff=0.6)
        all_cols.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 动画展示
        self.play(FadeIn(left_col, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeIn(middle_col, shift=UP * 0.2))
        self.wait(0.5)
        self.play(FadeIn(right_col, shift=UP * 0.2))
        self.wait(1)
        
        # === 幂等律 ===
        idempotent_title = Text("幂等律 (Idempotent)", font_size=18, color=Colors.SECONDARY)
        
        idempotent_formulas = VGroup(
            MathTex(r"a \lor a = a", font_size=22, color=Colors.OR_COLOR),
            MathTex(r"a \land a = a", font_size=22, color=Colors.AND_COLOR),
        ).arrange(RIGHT, buff=0.6)
        
        idempotent_group = VGroup(idempotent_title, idempotent_formulas).arrange(DOWN, buff=0.2)
        idempotent_group.next_to(all_cols, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(idempotent_group, shift=UP * 0.2))
        
        # 双重否定
        double_neg_title = Text("双重否定律", font_size=18, color=Colors.SECONDARY)
        double_neg_formula = MathTex(r"\neg(\neg a) = a", font_size=24, color=Colors.NOT_COLOR)
        
        double_neg_group = VGroup(double_neg_title, double_neg_formula).arrange(RIGHT, buff=0.3)
        double_neg_group.next_to(idempotent_group, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(double_neg_group, shift=UP * 0.2))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(section_title, all_cols, idempotent_group, double_neg_group)
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_demorgan(self):
        """德摩根定律 - 重点讲解"""
        section_title = Text("德摩根定律 (De Morgan)", font_size=24, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 介绍
        intro = Text('"翻转"的艺术 —— 最重要的布尔代数定律之一', font_size=16, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        self.wait(0.5)
        
        # 两条定律
        law1_box = VGroup()
        law1 = MathTex(r"\neg(a \land b) = \neg a \lor \neg b", font_size=28, color=Colors.TEXT)
        law1_desc = Text('"非全真" = "存在假"', font_size=14, color=Colors.GRAY)
        law1_box.add(law1, law1_desc)
        law1_box.arrange(DOWN, buff=0.15)
        
        law2_box = VGroup()
        law2 = MathTex(r"\neg(a \lor b) = \neg a \land \neg b", font_size=28, color=Colors.TEXT)
        law2_desc = Text('"非存在真" = "全为假"', font_size=14, color=Colors.GRAY)
        law2_box.add(law2, law2_desc)
        law2_box.arrange(DOWN, buff=0.15)
        
        laws = VGroup(law1_box, law2_box).arrange(DOWN, buff=0.4)
        laws.next_to(intro, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(law1))
        self.play(FadeIn(law1_desc))
        self.wait(0.5)
        
        self.play(Write(law2))
        self.play(FadeIn(law2_desc))
        self.wait(0.8)
        
        # 记忆口诀
        mnemonic_title = Text("记忆口诀：", font_size=16, color=Colors.PRIMARY)
        mnemonic_title.next_to(laws, DOWN, buff=0.4).align_to(laws, LEFT).shift(LEFT * 0.5)
        
        mnemonic = VGroup(
            Text("长杠变短杠，开口换方向", font_size=18, color=Colors.SECONDARY),
        )
        mnemonic.next_to(mnemonic_title, RIGHT, buff=0.2)
        
        self.play(FadeIn(mnemonic_title), FadeIn(mnemonic))
        self.wait(1)
        
        # 验证示例
        verify_title = Text("真值表验证：", font_size=16, color=Colors.TEXT)
        verify_title.next_to(mnemonic_title, DOWN, buff=0.4).align_to(mnemonic_title, LEFT)
        
        self.play(FadeIn(verify_title))
        
        # 简化的验证表格
        table_header = VGroup(
            Text("a", font_size=14, color=Colors.TEXT),
            Text("b", font_size=14, color=Colors.TEXT),
            Text("a∧b", font_size=14, color=Colors.AND_COLOR),
            Text("¬(a∧b)", font_size=14, color=Colors.NOT_COLOR),
            Text("¬a∨¬b", font_size=14, color=Colors.OR_COLOR),
        ).arrange(RIGHT, buff=0.5)
        table_header.next_to(verify_title, DOWN, buff=0.2).set_x(0.5)
        
        self.play(FadeIn(table_header))
        
        # 数据行
        table_data = [
            (0, 0, 0, 1, 1),
            (0, 1, 0, 1, 1),
            (1, 0, 0, 1, 1),
            (1, 1, 1, 0, 0),
        ]
        
        rows = VGroup()
        for a, b, ab, nab, result in table_data:
            row = VGroup(
                Text(str(a), font_size=14, color=Colors.ONE if a else Colors.ZERO),
                Text(str(b), font_size=14, color=Colors.ONE if b else Colors.ZERO),
                Text(str(ab), font_size=14, color=Colors.ONE if ab else Colors.ZERO),
                Text(str(nab), font_size=14, color=Colors.ONE if nab else Colors.ZERO),
                Text(str(result), font_size=14, color=Colors.ONE if result else Colors.ZERO),
            ).arrange(RIGHT, buff=0.5)
            rows.add(row)
        
        rows.arrange(DOWN, buff=0.12)
        rows.next_to(table_header, DOWN, buff=0.15)
        
        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.1), run_time=0.25)
        
        # 高亮结果相等
        equal_highlight = VGroup(
            SurroundingRectangle(
                VGroup(table_header[3], *[r[3] for r in rows]),
                color=Colors.SECONDARY, buff=0.05
            ),
            SurroundingRectangle(
                VGroup(table_header[4], *[r[4] for r in rows]),
                color=Colors.SECONDARY, buff=0.05
            ),
        )
        
        self.play(Create(equal_highlight[0]), Create(equal_highlight[1]))
        
        equal_sign = Text("完全相等！", font_size=14, color=Colors.SECONDARY)
        equal_sign.next_to(rows, RIGHT, buff=0.3)
        
        self.play(FadeIn(equal_sign, scale=0.8))
        
        self.wait(2)
        
        # 清除
        all_elements = VGroup(
            section_title, intro, laws, mnemonic_title, mnemonic,
            verify_title, table_header, rows, equal_highlight, equal_sign
        )
        self.play(FadeOut(all_elements), run_time=0.5)
    
    def section_summary(self):
        """定律总结"""
        section_title = Text("核心定律总结", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建定律卡片网格
        cards = VGroup()
        
        # 第一行：基本定律
        card1 = create_law_card("交换律", r"a \circ b = b \circ a", "顺序可交换", Colors.PRIMARY)
        card2 = create_law_card("结合律", r"a \circ (b \circ c) = (a \circ b) \circ c", "括号可移动", Colors.PRIMARY)
        card3 = create_law_card("分配律", r"a \land (b \lor c)", "可展开", Colors.PRIMARY)
        
        row1 = VGroup(card1, card2, card3).arrange(RIGHT, buff=0.3)
        
        # 第二行：特殊定律
        card4 = create_law_card("同一律", r"a \lor 0 = a, a \land 1 = a", "单位元", Colors.SECONDARY)
        card5 = create_law_card("互补律", r"a \lor \neg a = 1", "矛盾与排中", Colors.NOT_COLOR)
        card6 = create_law_card("德摩根", r"\neg(a \land b) = \neg a \lor \neg b", "翻转定律", Colors.ACCENT)
        
        row2 = VGroup(card4, card5, card6).arrange(RIGHT, buff=0.3)
        
        cards.add(row1, row2)
        cards.arrange(DOWN, buff=0.3)
        cards.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        # 逐个显示
        for row in cards:
            for card in row:
                self.play(FadeIn(card, shift=UP * 0.2), run_time=0.3)
        
        self.wait(1)
        
        # 关键信息
        key_info = VGroup(
            Text("掌握这些定律，可以：", font_size=16, color=Colors.TEXT),
            Text("• 简化复杂的逻辑表达式", font_size=14, color=Colors.GRAY),
            Text("• 优化数字电路设计", font_size=14, color=Colors.GRAY),
            Text("• 证明逻辑等价性", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        key_info.next_to(cards, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_info, shift=UP * 0.2))
        
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_03_laws.py Scene03Laws
    pass
