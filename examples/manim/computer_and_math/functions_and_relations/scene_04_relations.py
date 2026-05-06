"""
函数与关系 - Scene 4: 二元关系——对函数的抽象
介绍二元关系的定义和三种表示方法

渲染命令: manim -pqh scene_04_relations.py BinaryRelations
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
    MATRIX_COLOR = "#1ABC9C"     # 矩阵色
    GRAPH_COLOR = "#E91E63"      # 图色


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


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


# ========== Scene 4: 二元关系 ==========
class BinaryRelations(Scene):
    """二元关系的定义和表示"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.from_function_to_relation()
        self.definition()
        self.set_representation()
        self.matrix_representation()
        self.graph_representation()
        self.counting()
        
        clear_scene(self)
    
    def from_function_to_relation(self):
        """从函数到关系"""
        section_title = Text("从函数到关系", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 函数的限制
        func_limits = VGroup(
            Text("函数的严格限制：", font_size=18, color=Colors.FUNCTION_COLOR),
            Text("• 每个定义域元素必须有对应", font_size=14, color=Colors.GRAY),
            Text("• 每个定义域元素只能对应一个值", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        func_limits.next_to(section_title, DOWN, buff=0.4).shift(LEFT * 1)
        
        self.play(FadeIn(func_limits))
        
        # 放松限制
        question = Text("如果放松这些限制呢？", font_size=18, color=Colors.SECONDARY)
        question.next_to(func_limits, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        
        # 关系更自由
        relation_freedom = VGroup(
            Text("二元关系——更自由的配对：", font_size=18, color=Colors.RELATION_COLOR),
            Text("• 元素可以不参与配对", font_size=14, color=Colors.GRAY),
            Text("• 一个元素可以对应多个元素", font_size=14, color=Colors.GRAY),
            Text("• 甚至可以没有任何配对", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        relation_freedom.next_to(question, DOWN, buff=0.4).shift(LEFT * 0.5)
        
        self.play(FadeIn(relation_freedom))
        
        # 结论
        conclusion = VGroup(
            Text("函数是一种", font_size=16, color=Colors.TEXT),
            Text("特殊的", font_size=16, color=Colors.ACCENT),
            Text("二元关系", font_size=16, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.1)
        conclusion.next_to(relation_freedom, DOWN, buff=0.4).set_x(0)
        
        conclusion_box = SurroundingRectangle(conclusion, color=Colors.RELATION_COLOR, buff=0.15)
        
        self.play(FadeIn(conclusion), Create(conclusion_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(func_limits), FadeOut(question),
            FadeOut(relation_freedom), FadeOut(conclusion), FadeOut(conclusion_box),
            run_time=0.5
        )
    
    def definition(self):
        """关系的定义"""
        section_title = Text("二元关系的定义", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 笛卡尔积
        cartesian = VGroup(
            Text("给定两个集合 A 和 B，它们的", font_size=16, color=Colors.GRAY),
            Text("笛卡尔积", font_size=18, color=Colors.SET_COLOR),
            Text("是：", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        cartesian.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(cartesian))
        
        cartesian_def = MathTex(
            r"A \times B = \{(a, b) \mid a \in A, b \in B\}",
            font_size=24, color=Colors.TEXT
        )
        cartesian_def.next_to(cartesian, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(cartesian_def))
        
        # 关系定义
        relation_def = VGroup(
            Text("二元关系 R 是 A × B 的", font_size=16, color=Colors.GRAY),
            Text("任意子集", font_size=18, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.1)
        relation_def.next_to(cartesian_def, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(relation_def))
        
        relation_formula = MathTex(
            r"R \subseteq A \times B",
            font_size=26, color=Colors.RELATION_COLOR
        )
        relation_formula.next_to(relation_def, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(relation_formula))
        
        # 含义
        meaning = VGroup(
            Text("如果 (a, b) ∈ R，我们说", font_size=14, color=Colors.GRAY),
            Text('"a 与 b 有关系 R"', font_size=14, color=Colors.SECONDARY),
            Text("或记作 aRb", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        meaning.next_to(relation_formula, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(meaning))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(cartesian), FadeOut(cartesian_def),
            FadeOut(relation_def), FadeOut(relation_formula), FadeOut(meaning),
            run_time=0.5
        )
    
    def set_representation(self):
        """集合列举法"""
        section_title = Text("表示方法一：集合列举法", font_size=24, color=Colors.SET_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 示例
        example = VGroup(
            Text("设 A = {1, 2, 3}，B = {a, b}", font_size=16, color=Colors.GRAY),
        )
        example.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example))
        
        relation = VGroup(
            Text('关系 "小于等于元素在字母表中的位置":', font_size=14, color=Colors.TEXT),
        )
        relation.next_to(example, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(relation))
        
        # 列举
        listing = MathTex(
            r"R = \{(1, a), (1, b), (2, b)\}",
            font_size=24, color=Colors.RELATION_COLOR
        )
        listing.next_to(relation, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(listing))
        
        # 解释
        explanation = VGroup(
            Text("• 1 ≤ 1(a的位置) ✓  → (1, a) ∈ R", font_size=12, color=Colors.GRAY),
            Text("• 1 ≤ 2(b的位置) ✓  → (1, b) ∈ R", font_size=12, color=Colors.GRAY),
            Text("• 2 ≤ 2(b的位置) ✓  → (2, b) ∈ R", font_size=12, color=Colors.GRAY),
            Text("• 3 > 1, 3 > 2      → 3与任何字母无关系", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanation.next_to(listing, DOWN, buff=0.3).shift(LEFT * 0.5)
        
        self.play(FadeIn(explanation))
        
        # 特点
        feature = VGroup(
            Text("特点：", font_size=14, color=Colors.PRIMARY),
            Text("直观、精确，适合小规模关系", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        feature.next_to(explanation, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(feature))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(example), FadeOut(relation),
            FadeOut(listing), FadeOut(explanation), FadeOut(feature),
            run_time=0.5
        )
    
    def matrix_representation(self):
        """矩阵表示法"""
        section_title = Text("表示方法二：矩阵表示法", font_size=24, color=Colors.MATRIX_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 说明
        desc = Text(
            "用矩阵 M 表示关系，M[i][j] = 1 表示 (aᵢ, bⱼ) ∈ R",
            font_size=14, color=Colors.GRAY
        )
        desc.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(desc))
        
        # 示例
        example = VGroup(
            Text("A = {1, 2, 3}", font_size=14, color=Colors.DOMAIN_COLOR),
            Text("B = {a, b}", font_size=14, color=Colors.CODOMAIN_COLOR),
            Text("R = {(1,a), (1,b), (2,b)}", font_size=14, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.5)
        example.next_to(desc, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(example))
        
        # 矩阵
        matrix_label = Text("关系矩阵 M:", font_size=16, color=Colors.TEXT)
        matrix_label.next_to(example, DOWN, buff=0.4).shift(LEFT * 2)
        
        # 创建矩阵
        matrix_entries = [
            [1, 1],  # 行1: (1,a)=1, (1,b)=1
            [0, 1],  # 行2: (2,a)=0, (2,b)=1
            [0, 0],  # 行3: (3,a)=0, (3,b)=0
        ]
        
        # 行标签
        row_labels = VGroup()
        for i, label in enumerate(['1', '2', '3']):
            t = Text(label, font_size=16, color=Colors.DOMAIN_COLOR)
            row_labels.add(t)
        row_labels.arrange(DOWN, buff=0.35)
        
        # 列标签
        col_labels = VGroup()
        for label in ['a', 'b']:
            t = Text(label, font_size=16, color=Colors.CODOMAIN_COLOR)
            col_labels.add(t)
        col_labels.arrange(RIGHT, buff=0.5)
        
        # 矩阵内容
        matrix_cells = VGroup()
        for i, row in enumerate(matrix_entries):
            row_cells = VGroup()
            for j, val in enumerate(row):
                color = Colors.RELATION_COLOR if val == 1 else Colors.GRAY
                cell = Text(str(val), font_size=18, color=color)
                row_cells.add(cell)
            row_cells.arrange(RIGHT, buff=0.5)
            matrix_cells.add(row_cells)
        matrix_cells.arrange(DOWN, buff=0.35)
        
        # 括号
        left_bracket = MathTex(r"\begin{bmatrix} \\ \\ \\ \end{bmatrix}", font_size=50)
        left_bracket.next_to(matrix_cells, LEFT, buff=0.1)
        right_bracket = MathTex(r"\begin{bmatrix} \\ \\ \\ \end{bmatrix}", font_size=50)
        right_bracket.next_to(matrix_cells, RIGHT, buff=0.1)
        
        matrix_group = VGroup(matrix_cells)
        matrix_group.next_to(matrix_label, RIGHT, buff=0.5)
        
        row_labels.next_to(matrix_group, LEFT, buff=0.3)
        col_labels.next_to(matrix_group, UP, buff=0.2)
        
        self.play(FadeIn(matrix_label))
        self.play(FadeIn(row_labels), FadeIn(col_labels))
        
        # 逐行显示矩阵
        for row in matrix_cells:
            self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.3)
        
        # 优点
        advantages = VGroup(
            Text("优点：", font_size=14, color=Colors.PRIMARY),
            Text("• 便于计算机存储和处理", font_size=12, color=Colors.GRAY),
            Text("• 关系运算可转化为矩阵运算", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        advantages.next_to(matrix_group, RIGHT, buff=0.8)
        
        self.play(FadeIn(advantages))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(desc), FadeOut(example),
            FadeOut(matrix_label), FadeOut(row_labels), FadeOut(col_labels),
            FadeOut(matrix_cells), FadeOut(advantages),
            run_time=0.5
        )
    
    def graph_representation(self):
        """有向图表示法"""
        section_title = Text("表示方法三：有向图表示法", font_size=24, color=Colors.GRAPH_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 说明
        desc = Text(
            "用点表示元素，用有向边表示关系",
            font_size=16, color=Colors.GRAY
        )
        desc.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(desc))
        
        # 示例信息
        example = Text(
            "R = {(1, a), (1, b), (2, b)}",
            font_size=16, color=Colors.RELATION_COLOR
        )
        example.next_to(desc, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(example))
        
        # 创建有向图
        # A 的节点
        nodes_a = VGroup()
        positions_a = [LEFT * 2 + UP * 0.8, LEFT * 2, LEFT * 2 + DOWN * 0.8]
        labels_a = ['1', '2', '3']
        for pos, label in zip(positions_a, labels_a):
            node = Circle(radius=0.25, color=Colors.DOMAIN_COLOR, stroke_width=2)
            node.set_fill(Colors.DOMAIN_COLOR, opacity=0.2)
            node.move_to(pos)
            node_label = Text(label, font_size=16, color=Colors.TEXT)
            node_label.move_to(node.get_center())
            nodes_a.add(VGroup(node, node_label))
        
        # B 的节点
        nodes_b = VGroup()
        positions_b = [RIGHT * 2 + UP * 0.4, RIGHT * 2 + DOWN * 0.4]
        labels_b = ['a', 'b']
        for pos, label in zip(positions_b, labels_b):
            node = Circle(radius=0.25, color=Colors.CODOMAIN_COLOR, stroke_width=2)
            node.set_fill(Colors.CODOMAIN_COLOR, opacity=0.2)
            node.move_to(pos)
            node_label = Text(label, font_size=16, color=Colors.TEXT)
            node_label.move_to(node.get_center())
            nodes_b.add(VGroup(node, node_label))
        
        graph = VGroup(nodes_a, nodes_b)
        graph.next_to(example, DOWN, buff=0.5).set_x(0)
        
        # 集合标签
        a_label = Text("A", font_size=18, color=Colors.DOMAIN_COLOR)
        a_label.next_to(nodes_a, LEFT, buff=0.3)
        
        b_label = Text("B", font_size=18, color=Colors.CODOMAIN_COLOR)
        b_label.next_to(nodes_b, RIGHT, buff=0.3)
        
        self.play(FadeIn(graph), FadeIn(a_label), FadeIn(b_label))
        
        # 绘制边
        edges = VGroup()
        
        # (1, a)
        edge1 = Arrow(
            nodes_a[0][0].get_right() + RIGHT * 0.05,
            nodes_b[0][0].get_left() + LEFT * 0.05,
            color=Colors.ARROW_COLOR, stroke_width=2, buff=0.1
        )
        edges.add(edge1)
        
        # (1, b)
        edge2 = Arrow(
            nodes_a[0][0].get_right() + RIGHT * 0.05,
            nodes_b[1][0].get_left() + LEFT * 0.05,
            color=Colors.ARROW_COLOR, stroke_width=2, buff=0.1
        )
        edges.add(edge2)
        
        # (2, b)
        edge3 = Arrow(
            nodes_a[1][0].get_right() + RIGHT * 0.05,
            nodes_b[1][0].get_left() + LEFT * 0.05,
            color=Colors.ARROW_COLOR, stroke_width=2, buff=0.1
        )
        edges.add(edge3)
        
        for edge in edges:
            self.play(GrowArrow(edge), run_time=0.4)
        
        # 注释
        note = VGroup(
            Text("• 1 有两条出边（对应两个元素）", font_size=12, color=Colors.GRAY),
            Text("• 3 没有出边（不参与关系）", font_size=12, color=Colors.GRAY),
            Text("• 这在函数中是不允许的！", font_size=12, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        note.next_to(graph, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(note))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(desc), FadeOut(example),
            FadeOut(graph), FadeOut(edges), FadeOut(a_label), FadeOut(b_label),
            FadeOut(note),
            run_time=0.5
        )
    
    def counting(self):
        """关系的计数"""
        section_title = Text("关系的数量", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题
        question = Text(
            "A 和 B 之间可能有多少种不同的关系？",
            font_size=18, color=Colors.SECONDARY
        )
        question.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question))
        
        # 推理
        reasoning = VGroup(
            Text("• A × B 共有 |A| × |B| 个有序对", font_size=14, color=Colors.GRAY),
            Text("• 每个有序对可以在 R 中，也可以不在", font_size=14, color=Colors.GRAY),
            Text("• 这是一个子集选择问题", font_size=14, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        reasoning.next_to(question, DOWN, buff=0.3).shift(LEFT * 0.5)
        
        self.play(FadeIn(reasoning))
        
        # 公式
        formula = VGroup(
            Text("关系数量 = ", font_size=18, color=Colors.TEXT),
            MathTex(r"2^{|A| \times |B|}", font_size=28, color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.1)
        formula.next_to(reasoning, DOWN, buff=0.4).set_x(0)
        
        formula_box = SurroundingRectangle(formula, color=Colors.RELATION_COLOR, buff=0.15)
        
        self.play(Write(formula), Create(formula_box))
        
        # 示例
        example = VGroup(
            Text("例：|A| = 2, |B| = 2", font_size=14, color=Colors.TEXT),
            MathTex(r"2^{2 \times 2} = 2^4 = 16", font_size=20, color=Colors.PRIMARY),
            Text("种不同的关系", font_size=14, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.2)
        example.next_to(formula_box, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example))
        
        # 感叹
        remark = Text(
            "关系的数量增长非常快！",
            font_size=16, color=Colors.ACCENT
        )
        remark.next_to(example, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(remark))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(question), FadeOut(reasoning),
            FadeOut(formula), FadeOut(formula_box), FadeOut(example), FadeOut(remark),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_04_relations.py BinaryRelations
    pass
