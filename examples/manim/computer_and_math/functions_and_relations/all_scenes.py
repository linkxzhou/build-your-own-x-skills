"""
函数与关系：从映射到抽象
完整视频 - 所有场景合并

渲染命令: manim -pqh all_scenes.py FunctionsAndRelations
预览命令: manim -pql all_scenes.py FunctionsAndRelations
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
    FUNCTION_COLOR = "#E74C3C"   # 函数红
    RELATION_COLOR = "#9B59B6"   # 关系紫
    SET_COLOR = "#3498DB"        # 集合蓝
    DOMAIN_COLOR = "#E67E22"     # 定义域橙
    CODOMAIN_COLOR = "#27AE60"   # 值域绿
    ARROW_COLOR = "#F1C40F"      # 箭头黄
    COMPOSE_COLOR = "#9B59B6"    # 复合紫
    MATRIX_COLOR = "#1ABC9C"     # 矩阵色
    GRAPH_COLOR = "#E91E63"      # 图色
    EQUIV_COLOR = "#2ECC71"      # 等价绿
    ORDER_COLOR = "#F39C12"      # 偏序橙
    SURJECTIVE_COLOR = "#2ECC71" # 满射绿
    INJECTIVE_COLOR = "#E74C3C"  # 单射红
    BIJECTIVE_COLOR = "#9B59B6"  # 双射紫
    INVERSE_COLOR = "#E91E63"    # 逆关系粉
    COMPLEMENT_COLOR = "#00BCD4" # 补关系青
    REFLEXIVE_COLOR = "#F1C40F"  # 自反黄
    SYMMETRIC_COLOR = "#E74C3C"  # 对称红
    ANTISYMM_COLOR = "#E91E63"   # 反对称粉
    TRANSITIVE_COLOR = "#3498DB" # 传递蓝
    CLASS1_COLOR = "#E74C3C"     # 等价类1
    CLASS2_COLOR = "#3498DB"     # 等价类2
    CLASS3_COLOR = "#2ECC71"     # 等价类3
    HASSE_NODE = "#9B59B6"       # 哈斯图节点
    HASSE_EDGE = "#4ECDC4"       # 哈斯图边


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_mapping_arrow(start_pos, end_pos, color=Colors.ARROW_COLOR):
    """创建映射箭头"""
    arrow = Arrow(
        start_pos, end_pos,
        color=color,
        stroke_width=2,
        buff=0.1,
        max_tip_length_to_length_ratio=0.15
    )
    return arrow


def create_property_diagram(s_elems, t_elems, mappings, title_text, title_color,
                           highlight_targets=None, highlight_sources=None):
    """创建性质演示图"""
    group = VGroup()
    
    # 定义域椭圆
    s_ellipse = Ellipse(width=1.6, height=2.4)
    s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
    s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
    
    s_texts = VGroup()
    for i, elem in enumerate(s_elems):
        color = title_color if highlight_sources and i in highlight_sources else Colors.TEXT
        t = Text(str(elem), font_size=20, color=color)
        s_texts.add(t)
    s_texts.arrange(DOWN, buff=0.35)
    s_texts.move_to(s_ellipse.get_center())
    
    # 值域椭圆
    t_ellipse = Ellipse(width=1.6, height=2.4)
    t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
    t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
    t_ellipse.shift(RIGHT * 2.2)
    
    t_texts = VGroup()
    for i, elem in enumerate(t_elems):
        color = title_color if highlight_targets and i in highlight_targets else Colors.TEXT
        t = Text(str(elem), font_size=20, color=color)
        t_texts.add(t)
    t_texts.arrange(DOWN, buff=0.35)
    t_texts.move_to(t_ellipse.get_center())
    
    # 标签
    s_label = Text("S", font_size=16, color=Colors.DOMAIN_COLOR)
    s_label.next_to(s_ellipse, UP, buff=0.1)
    
    t_label = Text("T", font_size=16, color=Colors.CODOMAIN_COLOR)
    t_label.next_to(t_ellipse, UP, buff=0.1)
    
    # 箭头
    arrows = VGroup()
    for s_idx, t_idx in mappings:
        arrow = create_mapping_arrow(
            s_texts[s_idx].get_right() + RIGHT * 0.05,
            t_texts[t_idx].get_left() + LEFT * 0.05,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow)
    
    # 标题
    title = Text(title_text, font_size=16, color=title_color)
    
    diagram = VGroup(s_ellipse, s_texts, s_label, t_ellipse, t_texts, t_label, arrows)
    title.next_to(diagram, UP, buff=0.2)
    
    group.add(title, diagram)
    return group


def create_matrix_display(entries, row_labels=None, col_labels=None,
                         highlight_ones=True, color=Colors.RELATION_COLOR):
    """创建矩阵显示"""
    group = VGroup()
    
    matrix_cells = VGroup()
    for i, row in enumerate(entries):
        row_cells = VGroup()
        for j, val in enumerate(row):
            if highlight_ones:
                cell_color = color if val == 1 else Colors.GRAY
            else:
                cell_color = Colors.TEXT
            cell = Text(str(val), font_size=16, color=cell_color)
            row_cells.add(cell)
        row_cells.arrange(RIGHT, buff=0.4)
        matrix_cells.add(row_cells)
    matrix_cells.arrange(DOWN, buff=0.3)
    
    group.add(matrix_cells)
    
    if row_labels:
        rl = VGroup()
        for label in row_labels:
            t = Text(str(label), font_size=14, color=Colors.DOMAIN_COLOR)
            rl.add(t)
        rl.arrange(DOWN, buff=0.3)
        rl.next_to(matrix_cells, LEFT, buff=0.3)
        group.add(rl)
    
    if col_labels:
        cl = VGroup()
        for label in col_labels:
            t = Text(str(label), font_size=14, color=Colors.CODOMAIN_COLOR)
            cl.add(t)
        cl.arrange(RIGHT, buff=0.4)
        cl.next_to(matrix_cells, UP, buff=0.2)
        group.add(cl)
    
    return group


def create_hasse_node(label, color=Colors.HASSE_NODE, radius=0.25):
    """创建哈斯图节点"""
    circle = Circle(radius=radius, color=color, stroke_width=2)
    circle.set_fill(color, opacity=0.2)
    text = Text(label, font_size=14, color=Colors.TEXT)
    text.move_to(circle.get_center())
    return VGroup(circle, text)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== 主场景类 ==========
class FunctionsAndRelations(Scene):
    """函数与关系：完整视频"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题（全程显示）
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        
        # ===== Scene 1: 函数——集合之间的映射 =====
        self.scene1_opening()
        self.scene1_definition()
        self.scene1_arrow_diagram()
        self.scene1_valid_vs_invalid()
        
        # ===== Scene 2: 函数的特殊性质 =====
        self.scene2_intro()
        self.scene2_surjective()
        self.scene2_injective()
        self.scene2_bijective()
        
        # ===== Scene 3: 函数复合 =====
        self.scene3_definition()
        self.scene3_visualization()
        self.scene3_properties()
        
        # ===== Scene 4: 二元关系 =====
        self.scene4_from_function()
        self.scene4_definition()
        self.scene4_representations()
        
        # ===== Scene 5: 关系的运算 =====
        self.scene5_composition()
        self.scene5_inverse_complement()
        self.scene5_nary_relations()
        
        # ===== Scene 6: 等价关系 =====
        self.scene6_definition()
        self.scene6_examples()
        self.scene6_equivalence_classes()
        
        # ===== Scene 7: 偏序关系 =====
        self.scene7_definition()
        self.scene7_examples()
        self.scene7_hasse_diagram()
        
        # ===== Scene 8: 总结与启示 =====
        self.scene8_review()
        self.scene8_applications()
        self.scene8_finale()
        
        clear_scene(self)
    
    # ========== Scene 1: 函数——集合之间的映射 ==========
    def scene1_opening(self):
        """开场动画"""
        main_title = Text("函数与关系", font_size=56, color=Colors.PRIMARY)
        subtitle = Text("从映射到抽象", font_size=28, color=Colors.GRAY)
        
        title_group = VGroup(main_title, subtitle).arrange(DOWN, buff=0.3)
        title_group.set_x(0)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.5)
        self.wait(1)
        
        question = Text(
            "函数不只是 y = f(x)，它是一种更一般的概念",
            font_size=22, color=Colors.SECONDARY
        )
        question.next_to(title_group, DOWN, buff=0.8)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(
            FadeOut(subtitle),
            FadeOut(question),
            Transform(main_title, self.chapter_title),
            run_time=0.8
        )
        self.remove(main_title)
        self.add(self.chapter_title)
        self.wait(0.3)
    
    def scene1_definition(self):
        """函数的严格定义"""
        section_title = Text("函数的严格定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        def_line1 = VGroup(
            Text("给定两个集合 ", font_size=18, color=Colors.GRAY),
            Text("S", font_size=20, color=Colors.DOMAIN_COLOR),
            Text("（定义域）和 ", font_size=18, color=Colors.GRAY),
            Text("T", font_size=20, color=Colors.CODOMAIN_COLOR),
            Text("（值域）", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.05)
        
        def_line2 = VGroup(
            Text("函数 ", font_size=18, color=Colors.GRAY),
            MathTex(r"f: S \rightarrow T", font_size=24, color=Colors.FUNCTION_COLOR),
            Text(" 是有序对 ", font_size=18, color=Colors.GRAY),
            MathTex(r"(s, t)", font_size=22, color=Colors.TEXT),
            Text(" 的集合", font_size=18, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.05)
        
        definition = VGroup(def_line1, def_line2).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(definition))
        self.wait(1)
        
        constraint_title = Text("关键约束：", font_size=18, color=Colors.ACCENT)
        constraint_title.next_to(definition, DOWN, buff=0.4).align_to(definition, LEFT)
        
        constraint = Text(
            "S 中的每个元素都必须出现一次且仅出现一次作为第一元素",
            font_size=16, color=Colors.TEXT
        )
        constraint.next_to(constraint_title, DOWN, buff=0.1)
        
        self.play(FadeIn(constraint_title), FadeIn(constraint))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition),
            FadeOut(constraint_title), FadeOut(constraint),
            run_time=0.5
        )
    
    def scene1_arrow_diagram(self):
        """箭头图可视化"""
        section_title = Text("函数的可视化：箭头图", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 创建两个集合
        s_ellipse = Ellipse(width=2.0, height=2.8)
        s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=3)
        s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        s_ellipse.shift(LEFT * 2.5)
        
        s_label = Text("S", font_size=22, color=Colors.DOMAIN_COLOR)
        s_label.next_to(s_ellipse, UP, buff=0.15)
        
        s_elements = VGroup()
        for elem in ['a', 'b', 'c']:
            elem_text = Text(elem, font_size=22, color=Colors.TEXT)
            s_elements.add(elem_text)
        s_elements.arrange(DOWN, buff=0.4)
        s_elements.move_to(s_ellipse.get_center())
        
        t_ellipse = Ellipse(width=2.0, height=2.8)
        t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=3)
        t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        t_ellipse.shift(RIGHT * 2.5)
        
        t_label = Text("T", font_size=22, color=Colors.CODOMAIN_COLOR)
        t_label.next_to(t_ellipse, UP, buff=0.15)
        
        t_elements = VGroup()
        for elem in ['1', '2', '3']:
            elem_text = Text(elem, font_size=22, color=Colors.TEXT)
            t_elements.add(elem_text)
        t_elements.arrange(DOWN, buff=0.4)
        t_elements.move_to(t_ellipse.get_center())
        
        sets_group = VGroup(s_ellipse, s_label, s_elements, t_ellipse, t_label, t_elements)
        sets_group.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeIn(s_ellipse), FadeIn(s_label), FadeIn(s_elements),
            FadeIn(t_ellipse), FadeIn(t_label), FadeIn(t_elements),
            run_time=0.8
        )
        
        func_label = MathTex(r"f: S \rightarrow T", font_size=24, color=Colors.FUNCTION_COLOR)
        func_label.move_to((s_ellipse.get_center() + t_ellipse.get_center()) / 2 + UP * 1.8)
        
        self.play(FadeIn(func_label))
        
        # 绘制映射箭头
        arrows = VGroup()
        arrow1 = create_mapping_arrow(
            s_elements[0].get_right() + RIGHT * 0.1,
            t_elements[0].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow1)
        
        arrow2 = create_mapping_arrow(
            s_elements[1].get_right() + RIGHT * 0.1,
            t_elements[1].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow2)
        
        arrow3 = create_mapping_arrow(
            s_elements[2].get_right() + RIGHT * 0.1,
            t_elements[1].get_left() + LEFT * 0.1,
            Colors.ARROW_COLOR
        )
        arrows.add(arrow3)
        
        for arrow in arrows:
            self.play(GrowArrow(arrow), run_time=0.4)
        
        note = Text("注意：b 和 c 都对应 2，这是允许的！", font_size=16, color=Colors.SECONDARY)
        note.next_to(sets_group, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(sets_group),
            FadeOut(func_label), FadeOut(arrows), FadeOut(note),
            run_time=0.5
        )
    
    def scene1_valid_vs_invalid(self):
        """合法与非法映射对比"""
        section_title = Text("函数的关键约束", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        rules = VGroup(
            VGroup(
                Text("✓ 允许：", font_size=18, color=Colors.CODOMAIN_COLOR),
                Text("多个元素可对应同一值", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("✗ 禁止：", font_size=18, color=Colors.ACCENT),
                Text("一个元素对应多个值", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("✗ 禁止：", font_size=18, color=Colors.ACCENT),
                Text("定义域元素无对应值", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        rules.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for rule in rules:
            self.play(FadeIn(rule, shift=RIGHT * 0.2), run_time=0.4)
            self.wait(0.3)
        
        core = VGroup(
            Text("函数的本质：", font_size=18, color=Colors.PRIMARY),
            Text("为定义域中的每个元素分配唯一的值域元素", font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        core.next_to(rules, DOWN, buff=0.5).set_x(0)
        
        core_box = SurroundingRectangle(core, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(rules), FadeOut(core), FadeOut(core_box), run_time=0.5)
    
    # ========== Scene 2: 函数的特殊性质 ==========
    def scene2_intro(self):
        """引入"""
        section_title = Text("函数的特殊性质", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        properties = VGroup(
            Text("满射 (Surjective)", font_size=18, color=Colors.SURJECTIVE_COLOR),
            Text("单射 (Injective)", font_size=18, color=Colors.INJECTIVE_COLOR),
            Text("双射 (Bijective)", font_size=18, color=Colors.BIJECTIVE_COLOR),
        ).arrange(RIGHT, buff=0.8)
        properties.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=UP * 0.2), run_time=0.4)
        
        self.wait(1.5)
        self.play(FadeOut(section_title), FadeOut(properties), run_time=0.5)
    
    def scene2_surjective(self):
        """满射"""
        section_title = Text("满射：T 中每个元素都被指向", font_size=24, color=Colors.SURJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        math_def = MathTex(
            r"\forall t \in T, \exists s \in S: f(s) = t",
            font_size=22, color=Colors.TEXT
        )
        math_def.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(math_def))
        
        analogy = Text('类比："所有座位都坐满了"', font_size=16, color=Colors.SECONDARY)
        analogy.next_to(math_def, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(math_def), FadeOut(analogy), run_time=0.5)
    
    def scene2_injective(self):
        """单射"""
        section_title = Text("单射：不同元素对应不同值", font_size=24, color=Colors.INJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        math_def = MathTex(
            r"s_1 \neq s_2 \Rightarrow f(s_1) \neq f(s_2)",
            font_size=22, color=Colors.TEXT
        )
        math_def.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(math_def))
        
        analogy = Text('类比："没有两人坐同一座位"', font_size=16, color=Colors.SECONDARY)
        analogy.next_to(math_def, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(math_def), FadeOut(analogy), run_time=0.5)
    
    def scene2_bijective(self):
        """双射"""
        section_title = Text("双射：满射 + 单射 = 完美一一对应", font_size=24, color=Colors.BIJECTIVE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        explanation = VGroup(
            Text("• 每个 T 元素都被指向（满射）", font_size=14, color=Colors.SURJECTIVE_COLOR),
            Text("• 每个 T 元素最多被指向一次（单射）", font_size=14, color=Colors.INJECTIVE_COLOR),
            Text("→ 每个 T 元素恰好被指向一次", font_size=14, color=Colors.BIJECTIVE_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        explanation.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(explanation))
        
        property_box = VGroup(
            Text("重要性质：双射函数存在反函数", font_size=16, color=Colors.TEXT),
            MathTex(r"f^{-1}: T \rightarrow S", font_size=20, color=Colors.BIJECTIVE_COLOR),
        ).arrange(DOWN, buff=0.1)
        property_box.next_to(explanation, DOWN, buff=0.4).set_x(0)
        
        box = SurroundingRectangle(property_box, color=Colors.BIJECTIVE_COLOR, buff=0.15)
        
        self.play(FadeIn(property_box), Create(box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(explanation), FadeOut(property_box), FadeOut(box), run_time=0.5)
    
    # ========== Scene 3: 函数复合 ==========
    def scene3_definition(self):
        """复合定义"""
        section_title = Text("函数的复合", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        funcs = VGroup(
            MathTex(r"f: S \rightarrow T", font_size=22, color=Colors.FUNCTION_COLOR),
            MathTex(r"g: T \rightarrow U", font_size=22, color=Colors.SECONDARY),
        ).arrange(DOWN, buff=0.2)
        funcs.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(funcs))
        
        compose_def = MathTex(
            r"(g \circ f): S \rightarrow U",
            font_size=24, color=Colors.COMPOSE_COLOR
        )
        compose_def.next_to(funcs, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(compose_def))
        
        formula = MathTex(
            r"(g \circ f)(s) = g(f(s))",
            font_size=28, color=Colors.TEXT
        )
        formula.next_to(compose_def, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(formula))
        
        note = Text('注意：g ∘ f 读作 "g after f"（先f后g）', font_size=14, color=Colors.GRAY)
        note.next_to(formula, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(funcs), FadeOut(compose_def), FadeOut(formula), FadeOut(note), run_time=0.5)
    
    def scene3_visualization(self):
        """可视化"""
        section_title = Text("复合的可视化", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三个集合
        s_ellipse = Ellipse(width=1.4, height=2.0)
        s_ellipse.set_stroke(Colors.DOMAIN_COLOR, width=2)
        s_ellipse.set_fill(Colors.DOMAIN_COLOR, opacity=0.1)
        s_ellipse.shift(LEFT * 3.5)
        
        s_label = Text("S", font_size=18, color=Colors.DOMAIN_COLOR)
        s_label.next_to(s_ellipse, UP, buff=0.1)
        
        s_elements = VGroup(*[Text(e, font_size=18, color=Colors.TEXT) for e in ['a', 'b']])
        s_elements.arrange(DOWN, buff=0.4)
        s_elements.move_to(s_ellipse.get_center())
        
        t_ellipse = Ellipse(width=1.4, height=2.0)
        t_ellipse.set_stroke(Colors.CODOMAIN_COLOR, width=2)
        t_ellipse.set_fill(Colors.CODOMAIN_COLOR, opacity=0.1)
        
        t_label = Text("T", font_size=18, color=Colors.CODOMAIN_COLOR)
        t_label.next_to(t_ellipse, UP, buff=0.1)
        
        t_elements = VGroup(*[Text(e, font_size=18, color=Colors.TEXT) for e in ['1', '2']])
        t_elements.arrange(DOWN, buff=0.4)
        t_elements.move_to(t_ellipse.get_center())
        
        u_ellipse = Ellipse(width=1.4, height=2.0)
        u_ellipse.set_stroke(Colors.SECONDARY, width=2)
        u_ellipse.set_fill(Colors.SECONDARY, opacity=0.1)
        u_ellipse.shift(RIGHT * 3.5)
        
        u_label = Text("U", font_size=18, color=Colors.SECONDARY)
        u_label.next_to(u_ellipse, UP, buff=0.1)
        
        u_elements = VGroup(*[Text(e, font_size=18, color=Colors.TEXT) for e in ['x', 'y']])
        u_elements.arrange(DOWN, buff=0.4)
        u_elements.move_to(u_ellipse.get_center())
        
        sets_group = VGroup(
            s_ellipse, s_label, s_elements,
            t_ellipse, t_label, t_elements,
            u_ellipse, u_label, u_elements
        )
        sets_group.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(sets_group))
        
        # 箭头
        f_arrows = VGroup(
            create_mapping_arrow(s_elements[0].get_right() + RIGHT * 0.05, t_elements[0].get_left() + LEFT * 0.05, Colors.FUNCTION_COLOR),
            create_mapping_arrow(s_elements[1].get_right() + RIGHT * 0.05, t_elements[1].get_left() + LEFT * 0.05, Colors.FUNCTION_COLOR),
        )
        
        g_arrows = VGroup(
            create_mapping_arrow(t_elements[0].get_right() + RIGHT * 0.05, u_elements[0].get_left() + LEFT * 0.05, Colors.SECONDARY),
            create_mapping_arrow(t_elements[1].get_right() + RIGHT * 0.05, u_elements[1].get_left() + LEFT * 0.05, Colors.SECONDARY),
        )
        
        self.play(*[GrowArrow(arr) for arr in f_arrows], run_time=0.5)
        self.play(*[GrowArrow(arr) for arr in g_arrows], run_time=0.5)
        
        # 复合结果
        result = MathTex(r"(g \circ f)(a) = x, \quad (g \circ f)(b) = y", font_size=18, color=Colors.COMPOSE_COLOR)
        result.next_to(sets_group, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(result))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(sets_group), FadeOut(f_arrows), FadeOut(g_arrows), FadeOut(result), run_time=0.5)
    
    def scene3_properties(self):
        """性质"""
        section_title = Text("复合的性质", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        props = VGroup(
            VGroup(
                Text("1. 不满足交换律：", font_size=16, color=Colors.ACCENT),
                MathTex(r"g \circ f \neq f \circ g", font_size=20, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("2. 满足结合律：", font_size=16, color=Colors.SECONDARY),
                MathTex(r"(h \circ g) \circ f = h \circ (g \circ f)", font_size=20, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        props.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for prop in props:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.5)
        
        insight = Text("核心思想：复杂操作 = 简单操作的组合", font_size=16, color=Colors.PRIMARY)
        insight.next_to(props, DOWN, buff=0.5).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.PRIMARY, buff=0.15)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(props), FadeOut(insight), FadeOut(insight_box), run_time=0.5)
    
    # ========== Scene 4: 二元关系 ==========
    def scene4_from_function(self):
        """从函数到关系"""
        section_title = Text("从函数到关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        comparison = VGroup(
            VGroup(
                Text("函数的严格限制：", font_size=16, color=Colors.FUNCTION_COLOR),
                Text("• 每个元素必须有对应", font_size=12, color=Colors.GRAY),
                Text("• 每个元素只能对应一个值", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
            VGroup(
                Text("关系更自由：", font_size=16, color=Colors.RELATION_COLOR),
                Text("• 元素可以不参与配对", font_size=12, color=Colors.GRAY),
                Text("• 一个元素可以对应多个", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.1, aligned_edge=LEFT),
        ).arrange(RIGHT, buff=1.0)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(comparison))
        
        conclusion = VGroup(
            Text("函数是一种", font_size=16, color=Colors.TEXT),
            Text("特殊的", font_size=16, color=Colors.ACCENT),
            Text("二元关系", font_size=16, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(comparison, DOWN, buff=0.5).set_x(0)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.RELATION_COLOR, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(comparison), FadeOut(conclusion), FadeOut(conclusion_box), run_time=0.5)
    
    def scene4_definition(self):
        """关系的定义"""
        section_title = Text("二元关系的定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        cartesian = MathTex(
            r"A \times B = \{(a, b) \mid a \in A, b \in B\}",
            font_size=22, color=Colors.SET_COLOR
        )
        cartesian.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(cartesian))
        
        relation_def = MathTex(
            r"R \subseteq A \times B",
            font_size=26, color=Colors.RELATION_COLOR
        )
        relation_def.next_to(cartesian, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(relation_def))
        
        meaning = Text("二元关系 R 是笛卡尔积 A × B 的任意子集", font_size=16, color=Colors.GRAY)
        meaning.next_to(relation_def, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(meaning))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(cartesian), FadeOut(relation_def), FadeOut(meaning), run_time=0.5)
    
    def scene4_representations(self):
        """关系的表示"""
        section_title = Text("关系的三种表示方法", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        methods = VGroup(
            VGroup(
                Text("1. 集合列举法", font_size=16, color=Colors.SET_COLOR),
                Text("R = {(1,a), (1,b), (2,b)}", font_size=12, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("2. 矩阵表示法", font_size=16, color=Colors.MATRIX_COLOR),
                Text("0/1 矩阵", font_size=12, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("3. 有向图表示法", font_size=16, color=Colors.GRAPH_COLOR),
                Text("节点 + 有向边", font_size=12, color=Colors.TEXT),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.8)
        methods.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for method in methods:
            self.play(FadeIn(method, scale=0.9), run_time=0.5)
        
        # 关系数量
        count = VGroup(
            Text("关系数量 = ", font_size=16, color=Colors.TEXT),
            MathTex(r"2^{|A| \times |B|}", font_size=22, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.1)
        count.next_to(methods, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(count))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(methods), FadeOut(count), run_time=0.5)
    
    # ========== Scene 5: 关系的运算 ==========
    def scene5_composition(self):
        """关系的复合"""
        section_title = Text("关系的复合", font_size=24, color=Colors.COMPOSE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        formula = MathTex(
            r"(a, c) \in S \circ R \Leftrightarrow \exists b: (a, b) \in R \land (b, c) \in S",
            font_size=16, color=Colors.TEXT
        )
        formula.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(formula))
        
        intuition = Text('"存在中间桥梁 b 连接 a 和 c"', font_size=16, color=Colors.SECONDARY)
        intuition.next_to(formula, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intuition))
        
        matrix_info = Text("矩阵表示：布尔矩阵乘法（AND代替乘，OR代替加）", font_size=14, color=Colors.GRAY)
        matrix_info.next_to(intuition, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(matrix_info))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(formula), FadeOut(intuition), FadeOut(matrix_info), run_time=0.5)
    
    def scene5_inverse_complement(self):
        """逆关系和补关系"""
        section_title = Text("逆关系与补关系", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        inverse = VGroup(
            Text("逆关系", font_size=18, color=Colors.INVERSE_COLOR),
            MathTex(r"R^{-1} = \{(b, a) \mid (a, b) \in R\}", font_size=18, color=Colors.TEXT),
            Text("矩阵表示：转置", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        complement = VGroup(
            Text("补关系", font_size=18, color=Colors.COMPLEMENT_COLOR),
            MathTex(r"\bar{R} = (A \times B) - R", font_size=18, color=Colors.TEXT),
            Text("矩阵表示：0和1互换", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        
        ops = VGroup(inverse, complement).arrange(RIGHT, buff=1.0)
        ops.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(inverse), FadeIn(complement))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(ops), run_time=0.5)
    
    def scene5_nary_relations(self):
        """n元关系与数据库"""
        section_title = Text("n元关系与数据库", font_size=24, color=Colors.PRIMARY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        definition = MathTex(
            r"R \subseteq A_1 \times A_2 \times \cdots \times A_n",
            font_size=22, color=Colors.RELATION_COLOR
        )
        definition.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(Write(definition))
        
        connection = VGroup(
            Text("数据库表 = n元关系", font_size=18, color=Colors.SECONDARY),
            Text("每一行 = 一个 n 元组", font_size=16, color=Colors.GRAY),
            Text("SQL 查询 = 关系运算", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        connection.next_to(definition, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(connection))
        
        insight = Text("关系型数据库的数学基础就是关系理论！", font_size=16, color=Colors.ACCENT)
        insight.next_to(connection, DOWN, buff=0.4).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.ACCENT, buff=0.1)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(definition), FadeOut(connection), FadeOut(insight), FadeOut(insight_box), run_time=0.5)
    
    # ========== Scene 6: 等价关系 ==========
    def scene6_definition(self):
        """等价关系定义"""
        section_title = Text("等价关系的定义", font_size=24, color=Colors.EQUIV_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        properties = VGroup(
            VGroup(
                Text("1. 自反性", font_size=16, color=Colors.REFLEXIVE_COLOR),
                MathTex(r"\forall s: (s, s) \in R", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("2. 对称性", font_size=16, color=Colors.SYMMETRIC_COLOR),
                MathTex(r"(a, b) \in R \Rightarrow (b, a) \in R", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("3. 传递性", font_size=16, color=Colors.TRANSITIVE_COLOR),
                MathTex(r"(a, b) \in R \land (b, c) \in R \Rightarrow (a, c) \in R", font_size=16, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        properties.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.4)
        
        self.wait(2)
        self.play(FadeOut(section_title), FadeOut(properties), run_time=0.5)
    
    def scene6_examples(self):
        """等价关系例子"""
        section_title = Text("等价关系的例子", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        examples = VGroup(
            Text("• 整数的相等关系", font_size=16, color=Colors.GRAY),
            Text("• 模 n 同余关系", font_size=16, color=Colors.GRAY),
            Text("• 三角形的相似关系", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        examples.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(examples))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(examples), run_time=0.5)
    
    def scene6_equivalence_classes(self):
        """等价类"""
        section_title = Text("等价类", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        concept = Text("等价关系把集合划分成互不相交的等价类", font_size=16, color=Colors.GRAY)
        concept.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(concept))
        
        # 模3同余示例
        example_title = Text('例：模3同余把整数分成三类', font_size=16, color=Colors.SECONDARY)
        example_title.next_to(concept, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example_title))
        
        classes = VGroup(
            VGroup(
                Ellipse(width=2.2, height=0.8, color=Colors.CLASS1_COLOR, stroke_width=2),
                Text("[0]₃: ..., -3, 0, 3, 6, ...", font_size=12, color=Colors.CLASS1_COLOR),
            ),
            VGroup(
                Ellipse(width=2.2, height=0.8, color=Colors.CLASS2_COLOR, stroke_width=2),
                Text("[1]₃: ..., -2, 1, 4, 7, ...", font_size=12, color=Colors.CLASS2_COLOR),
            ),
            VGroup(
                Ellipse(width=2.2, height=0.8, color=Colors.CLASS3_COLOR, stroke_width=2),
                Text("[2]₃: ..., -1, 2, 5, 8, ...", font_size=12, color=Colors.CLASS3_COLOR),
            ),
        )
        
        for c in classes:
            c[0].set_fill(c[0].get_stroke_color(), opacity=0.15)
            c[1].move_to(c[0].get_center())
        
        classes.arrange(RIGHT, buff=0.3)
        classes.next_to(example_title, DOWN, buff=0.3).set_x(0)
        
        for c in classes:
            self.play(FadeIn(c, scale=0.9), run_time=0.4)
        
        self.wait(2)
        self.play(FadeOut(section_title), FadeOut(concept), FadeOut(example_title), FadeOut(classes), run_time=0.5)
    
    # ========== Scene 7: 偏序关系 ==========
    def scene7_definition(self):
        """偏序关系定义"""
        section_title = Text("偏序关系的定义", font_size=24, color=Colors.ORDER_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        properties = VGroup(
            VGroup(
                Text("1. 自反性", font_size=16, color=Colors.REFLEXIVE_COLOR),
                MathTex(r"\forall s: s \leq s", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("2. 反对称性", font_size=16, color=Colors.ANTISYMM_COLOR),
                MathTex(r"a \leq b \land b \leq a \Rightarrow a = b", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
            VGroup(
                Text("3. 传递性", font_size=16, color=Colors.TRANSITIVE_COLOR),
                MathTex(r"a \leq b \land b \leq c \Rightarrow a \leq c", font_size=18, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        properties.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.4)
        
        diff = Text('关键区别：对称性 → 反对称性（与等价关系不同）', font_size=14, color=Colors.ACCENT)
        diff.next_to(properties, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(diff))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(properties), FadeOut(diff), run_time=0.5)
    
    def scene7_examples(self):
        """偏序例子"""
        section_title = Text("偏序关系的例子", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        examples = VGroup(
            Text("• 整数的 ≤（全序：任意两元素可比）", font_size=14, color=Colors.GRAY),
            Text("• 集合的包含 ⊆（偏序：不是所有集合可比）", font_size=14, color=Colors.GRAY),
            Text("• 整除关系（偏序：2和3不可比）", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        examples.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(examples))
        
        meaning = Text('"偏"的含义：不是所有元素都能比较大小', font_size=16, color=Colors.ORDER_COLOR)
        meaning.next_to(examples, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(examples), FadeOut(meaning), run_time=0.5)
    
    def scene7_hasse_diagram(self):
        """哈斯图"""
        section_title = Text("哈斯图 (Hasse Diagram)", font_size=24, color=Colors.HASSE_NODE)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text("简化的有向图，用于可视化有限偏序集", font_size=14, color=Colors.GRAY)
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 示例：{a, b} 的幂集
        example_title = Text("例：{a, b} 的幂集，包含关系 ⊆", font_size=14, color=Colors.SECONDARY)
        example_title.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example_title))
        
        # 创建哈斯图
        node_empty = create_hasse_node("∅", Colors.HASSE_NODE)
        node_a = create_hasse_node("{a}", Colors.HASSE_NODE)
        node_b = create_hasse_node("{b}", Colors.HASSE_NODE)
        node_ab = create_hasse_node("{a,b}", Colors.HASSE_NODE)
        
        node_empty.move_to(DOWN * 0.8)
        node_a.move_to(LEFT * 0.8 + UP * 0.3)
        node_b.move_to(RIGHT * 0.8 + UP * 0.3)
        node_ab.move_to(UP * 1.4)
        
        hasse = VGroup(node_empty, node_a, node_b, node_ab)
        hasse.next_to(example_title, DOWN, buff=0.3)
        
        edges = VGroup(
            Line(node_empty[0].get_top(), node_a[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_empty[0].get_top(), node_b[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_a[0].get_top(), node_ab[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_b[0].get_top(), node_ab[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
        )
        
        self.play(FadeIn(hasse))
        for edge in edges:
            self.play(Create(edge), run_time=0.2)
        
        note = Text("从下到上表示包含关系，{a}和{b}无连线→不可比", font_size=12, color=Colors.GRAY)
        note.next_to(hasse, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(example_title), FadeOut(hasse), FadeOut(edges), FadeOut(note), run_time=0.5)
    
    # ========== Scene 8: 总结与启示 ==========
    def scene8_review(self):
        """知识体系回顾"""
        section_title = Text("知识体系回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        flow = VGroup(
            Text("函数", font_size=18, color=Colors.FUNCTION_COLOR),
            Text("→", font_size=20, color=Colors.GRAY),
            Text("关系", font_size=18, color=Colors.RELATION_COLOR),
            Text("→", font_size=20, color=Colors.GRAY),
            VGroup(
                Text("等价关系", font_size=16, color=Colors.EQUIV_COLOR),
                Text("偏序关系", font_size=16, color=Colors.ORDER_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.3)
        flow.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(flow))
        
        progress = VGroup(
            Text("从具体到抽象", font_size=14, color=Colors.PRIMARY),
            Text("从严格到灵活", font_size=14, color=Colors.SECONDARY),
            Text("从一般到特殊", font_size=14, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.6)
        progress.next_to(flow, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(progress))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(flow), FadeOut(progress), run_time=0.5)
    
    def scene8_applications(self):
        """计算机科学应用"""
        section_title = Text("计算机科学中的应用", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        apps = VGroup(
            VGroup(Text("函数", font_size=14, color=Colors.FUNCTION_COLOR), Text("程序中的函数/方法", font_size=11, color=Colors.GRAY)).arrange(DOWN, buff=0.05),
            VGroup(Text("关系", font_size=14, color=Colors.RELATION_COLOR), Text("数据库表", font_size=11, color=Colors.GRAY)).arrange(DOWN, buff=0.05),
            VGroup(Text("等价关系", font_size=14, color=Colors.EQUIV_COLOR), Text("数据分类/聚类", font_size=11, color=Colors.GRAY)).arrange(DOWN, buff=0.05),
            VGroup(Text("偏序关系", font_size=14, color=Colors.ORDER_COLOR), Text("任务调度/依赖", font_size=11, color=Colors.GRAY)).arrange(DOWN, buff=0.05),
        ).arrange(RIGHT, buff=0.5)
        apps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for app in apps:
            self.play(FadeIn(app, shift=UP * 0.2), run_time=0.4)
        
        core = Text("函数和关系是计算机处理数据的核心抽象！", font_size=16, color=Colors.ACCENT)
        core.next_to(apps, DOWN, buff=0.5).set_x(0)
        
        core_box = SurroundingRectangle(core, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(apps), FadeOut(core), FadeOut(core_box), run_time=0.5)
    
    def scene8_finale(self):
        """升华与结语"""
        quote = Text("理解事物间联系的框架", font_size=32, color=Colors.PRIMARY)
        quote.move_to(ORIGIN + UP * 1.0)
        
        self.play(FadeIn(quote, scale=0.8))
        self.wait(0.8)
        
        recap = VGroup(
            Text("本章要点：", font_size=16, color=Colors.TEXT),
            Text("✓ 函数：定义域到值域的唯一映射", font_size=13, color=Colors.GRAY),
            Text("✓ 单射/满射/双射：函数的特殊性质", font_size=13, color=Colors.GRAY),
            Text("✓ 二元关系：更自由的配对方式", font_size=13, color=Colors.GRAY),
            Text("✓ 等价关系：划分集合，构造新对象", font_size=13, color=Colors.GRAY),
            Text("✓ 偏序关系：表达顺序，绘制哈斯图", font_size=13, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        recap.next_to(quote, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(recap, shift=UP * 0.2))
        self.wait(1)
        
        thanks = Text("感谢观看！", font_size=28, color=Colors.SECONDARY)
        thanks.next_to(recap, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(thanks, scale=0.8))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染完整视频: manim -pqh all_scenes.py FunctionsAndRelations
    # 预览版本: manim -pql all_scenes.py FunctionsAndRelations
    pass
