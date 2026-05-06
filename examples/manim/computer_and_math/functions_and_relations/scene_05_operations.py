"""
函数与关系 - Scene 5: 关系的运算
介绍关系的复合、逆、补运算，以及n元关系与数据库

渲染命令: manim -pqh scene_05_operations.py RelationOperations
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
    INVERSE_COLOR = "#E91E63"    # 逆关系粉
    COMPLEMENT_COLOR = "#00BCD4" # 补关系青


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


def create_matrix_display(entries, row_labels=None, col_labels=None, 
                         highlight_ones=True, color=Colors.RELATION_COLOR):
    """创建矩阵显示"""
    group = VGroup()
    
    # 矩阵内容
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
    
    # 行标签
    if row_labels:
        rl = VGroup()
        for label in row_labels:
            t = Text(str(label), font_size=14, color=Colors.DOMAIN_COLOR)
            rl.add(t)
        rl.arrange(DOWN, buff=0.3)
        rl.next_to(matrix_cells, LEFT, buff=0.3)
        group.add(rl)
    
    # 列标签
    if col_labels:
        cl = VGroup()
        for label in col_labels:
            t = Text(str(label), font_size=14, color=Colors.CODOMAIN_COLOR)
            cl.add(t)
        cl.arrange(RIGHT, buff=0.4)
        cl.next_to(matrix_cells, UP, buff=0.2)
        group.add(cl)
    
    return group


# ========== Scene 5: 关系的运算 ==========
class RelationOperations(Scene):
    """关系的运算：复合、逆、补"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.intro()
        self.composition()
        self.inverse()
        self.complement()
        self.nary_relations()
        
        clear_scene(self)
    
    def intro(self):
        """引入"""
        section_title = Text("关系的运算", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = Text(
            "就像集合有并、交、补运算，关系也有自己的运算",
            font_size=16, color=Colors.GRAY
        )
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        
        operations = VGroup(
            VGroup(
                Circle(radius=0.2, color=Colors.COMPOSE_COLOR, stroke_width=2),
                Text("复合", font_size=14, color=Colors.COMPOSE_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Circle(radius=0.2, color=Colors.INVERSE_COLOR, stroke_width=2),
                Text("逆", font_size=14, color=Colors.INVERSE_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Circle(radius=0.2, color=Colors.COMPLEMENT_COLOR, stroke_width=2),
                Text("补", font_size=14, color=Colors.COMPLEMENT_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.0)
        operations.next_to(intro, DOWN, buff=0.5).set_x(0)
        
        for op in operations:
            self.play(FadeIn(op, scale=0.8), run_time=0.4)
        
        self.wait(1)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(operations), run_time=0.5)
    
    def composition(self):
        """关系的复合"""
        section_title = Text("关系的复合", font_size=24, color=Colors.COMPOSE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("设 R: A → B 和 S: B → C", font_size=16, color=Colors.GRAY),
            Text("复合 S ∘ R: A → C 定义为：", font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        formula = MathTex(
            r"(a, c) \in S \circ R \Leftrightarrow \exists b: (a, b) \in R \land (b, c) \in S",
            font_size=18, color=Colors.TEXT
        )
        formula.next_to(definition, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(formula))
        
        # 直观理解
        intuition = VGroup(
            Text('"存在中间桥梁 b 连接 a 和 c"', font_size=14, color=Colors.SECONDARY),
        )
        intuition.next_to(formula, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(intuition))
        
        # 矩阵表示
        matrix_title = Text("矩阵表示：布尔矩阵乘法", font_size=16, color=Colors.PRIMARY)
        matrix_title.next_to(intuition, DOWN, buff=0.4).align_to(definition, LEFT)
        
        self.play(FadeIn(matrix_title))
        
        # 示例矩阵
        # R: 2×2, S: 2×2
        r_matrix = VGroup(
            Text("R =", font_size=14, color=Colors.RELATION_COLOR),
            create_matrix_display([[1, 0], [1, 1]], color=Colors.RELATION_COLOR),
        ).arrange(RIGHT, buff=0.2)
        
        s_matrix = VGroup(
            Text("S =", font_size=14, color=Colors.SECONDARY),
            create_matrix_display([[0, 1], [1, 0]], color=Colors.SECONDARY),
        ).arrange(RIGHT, buff=0.2)
        
        result_matrix = VGroup(
            Text("S∘R =", font_size=14, color=Colors.COMPOSE_COLOR),
            create_matrix_display([[0, 1], [1, 1]], color=Colors.COMPOSE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        
        matrices = VGroup(r_matrix, s_matrix, result_matrix).arrange(RIGHT, buff=0.6)
        matrices.next_to(matrix_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(r_matrix))
        self.play(FadeIn(s_matrix))
        self.play(FadeIn(result_matrix))
        
        # 运算规则
        rule = Text(
            "用 AND(∧) 代替乘法，OR(∨) 代替加法",
            font_size=12, color=Colors.GRAY
        )
        rule.next_to(matrices, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(rule))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(formula),
            FadeOut(intuition), FadeOut(matrix_title), FadeOut(matrices), FadeOut(rule),
            run_time=0.5
        )
    
    def inverse(self):
        """逆关系"""
        section_title = Text("逆关系", font_size=24, color=Colors.INVERSE_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("把关系中所有有序对的方向调换", font_size=16, color=Colors.GRAY),
        )
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        formula = MathTex(
            r"R^{-1} = \{(b, a) \mid (a, b) \in R\}",
            font_size=24, color=Colors.INVERSE_COLOR
        )
        formula.next_to(definition, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(formula))
        
        # 示例
        example = VGroup(
            Text("例：R = {(1, a), (2, b)}", font_size=14, color=Colors.RELATION_COLOR),
            MathTex(r"\Rightarrow", font_size=20, color=Colors.GRAY),
            Text("R⁻¹ = {(a, 1), (b, 2)}", font_size=14, color=Colors.INVERSE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        example.next_to(formula, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example))
        
        # 矩阵表示
        matrix_info = VGroup(
            Text("矩阵表示：", font_size=14, color=Colors.PRIMARY),
            Text("转置矩阵", font_size=16, color=Colors.TEXT),
            MathTex(r"M_{R^{-1}} = M_R^T", font_size=20, color=Colors.INVERSE_COLOR),
        ).arrange(RIGHT, buff=0.2)
        matrix_info.next_to(example, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(matrix_info))
        
        # 可视化
        # 原矩阵
        orig = VGroup(
            create_matrix_display([[1, 0], [0, 1]], color=Colors.RELATION_COLOR),
            Text("R", font_size=14, color=Colors.RELATION_COLOR),
        ).arrange(DOWN, buff=0.1)
        
        arrow = Text("→ 转置 →", font_size=14, color=Colors.GRAY)
        
        # 转置后
        transposed = VGroup(
            create_matrix_display([[1, 0], [0, 1]], color=Colors.INVERSE_COLOR),
            Text("R⁻¹", font_size=14, color=Colors.INVERSE_COLOR),
        ).arrange(DOWN, buff=0.1)
        
        visual = VGroup(orig, arrow, transposed).arrange(RIGHT, buff=0.5)
        visual.next_to(matrix_info, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(visual))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(formula),
            FadeOut(example), FadeOut(matrix_info), FadeOut(visual),
            run_time=0.5
        )
    
    def complement(self):
        """补关系"""
        section_title = Text("补关系", font_size=24, color=Colors.COMPLEMENT_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 定义
        definition = VGroup(
            Text("所有不在 R 中的 A × B 有序对", font_size=16, color=Colors.GRAY),
        )
        definition.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(definition))
        
        formula = MathTex(
            r"\bar{R} = (A \times B) - R",
            font_size=24, color=Colors.COMPLEMENT_COLOR
        )
        formula.next_to(definition, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(formula))
        
        # 示例
        example = VGroup(
            Text("A = {1, 2}, B = {a, b}", font_size=12, color=Colors.GRAY),
            Text("R = {(1, a), (2, b)}", font_size=12, color=Colors.RELATION_COLOR),
            MathTex(r"\bar{R}", font_size=16, color=Colors.COMPLEMENT_COLOR),
            Text("= {(1, b), (2, a)}", font_size=12, color=Colors.COMPLEMENT_COLOR),
        ).arrange(DOWN, buff=0.1)
        example.next_to(formula, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(example))
        
        # 矩阵表示
        matrix_info = VGroup(
            Text("矩阵表示：", font_size=14, color=Colors.PRIMARY),
            Text("0 和 1 互换", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.2)
        matrix_info.next_to(example, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(matrix_info))
        
        # 可视化
        # 原矩阵
        orig = VGroup(
            create_matrix_display([[1, 0], [0, 1]], color=Colors.RELATION_COLOR),
            Text("R", font_size=14, color=Colors.RELATION_COLOR),
        ).arrange(DOWN, buff=0.1)
        
        arrow = Text("→ 取反 →", font_size=14, color=Colors.GRAY)
        
        # 补后
        complemented = VGroup(
            create_matrix_display([[0, 1], [1, 0]], color=Colors.COMPLEMENT_COLOR),
            MathTex(r"\bar{R}", font_size=16, color=Colors.COMPLEMENT_COLOR),
        ).arrange(DOWN, buff=0.1)
        
        visual = VGroup(orig, arrow, complemented).arrange(RIGHT, buff=0.5)
        visual.next_to(matrix_info, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(visual))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(definition), FadeOut(formula),
            FadeOut(example), FadeOut(matrix_info), FadeOut(visual),
            run_time=0.5
        )
    
    def nary_relations(self):
        """n元关系与数据库"""
        section_title = Text("n元关系与数据库", font_size=24, color=Colors.PRIMARY)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 推广
        generalization = VGroup(
            Text("二元关系可以推广到多个集合", font_size=16, color=Colors.GRAY),
        )
        generalization.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(generalization))
        
        # 定义
        definition = MathTex(
            r"R \subseteq A_1 \times A_2 \times \cdots \times A_n",
            font_size=22, color=Colors.RELATION_COLOR
        )
        definition.next_to(generalization, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(definition))
        
        # n元组
        tuple_def = VGroup(
            Text("由 n 元组 ", font_size=16, color=Colors.TEXT),
            MathTex(r"(a_1, a_2, \ldots, a_n)", font_size=18, color=Colors.TEXT),
            Text(" 构成", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.05)
        tuple_def.next_to(definition, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(tuple_def))
        
        # 数据库连接
        db_title = Text("与数据库的联系：", font_size=16, color=Colors.SECONDARY)
        db_title.next_to(tuple_def, DOWN, buff=0.4).align_to(generalization, LEFT)
        
        self.play(FadeIn(db_title))
        
        # 数据库表示例
        table_title = Text("学生表 (3元关系)", font_size=14, color=Colors.PRIMARY)
        table_title.next_to(db_title, DOWN, buff=0.3)
        
        # 表头
        header = VGroup(
            Text("ID", font_size=12, color=Colors.DOMAIN_COLOR),
            Text("姓名", font_size=12, color=Colors.CODOMAIN_COLOR),
            Text("年龄", font_size=12, color=Colors.SET_COLOR),
        ).arrange(RIGHT, buff=0.8)
        header.next_to(table_title, DOWN, buff=0.15)
        
        # 分隔线
        line = Line(
            header.get_left() + LEFT * 0.2 + DOWN * 0.15,
            header.get_right() + RIGHT * 0.2 + DOWN * 0.15,
            color=Colors.GRAY
        )
        
        # 数据行
        rows = VGroup()
        data = [
            ("001", "张三", "20"),
            ("002", "李四", "21"),
            ("003", "王五", "20"),
        ]
        for id_val, name, age in data:
            row = VGroup(
                Text(id_val, font_size=11, color=Colors.TEXT),
                Text(name, font_size=11, color=Colors.TEXT),
                Text(age, font_size=11, color=Colors.TEXT),
            ).arrange(RIGHT, buff=0.8)
            rows.add(row)
        rows.arrange(DOWN, buff=0.15)
        rows.next_to(line, DOWN, buff=0.15)
        
        table = VGroup(table_title, header, line, rows)
        
        self.play(FadeIn(table))
        
        # 说明
        explanation = VGroup(
            Text("• 每一行是一个 3 元组", font_size=12, color=Colors.GRAY),
            Text("• 整张表是一个 3 元关系", font_size=12, color=Colors.GRAY),
            Text("• SQL 查询 = 关系运算", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanation.next_to(table, RIGHT, buff=0.5)
        
        self.play(FadeIn(explanation))
        
        # 核心思想
        insight = Text(
            "关系型数据库的数学基础就是关系理论！",
            font_size=16, color=Colors.ACCENT
        )
        insight.next_to(rows, DOWN, buff=0.4).set_x(0)
        
        insight_box = SurroundingRectangle(insight, color=Colors.ACCENT, buff=0.1)
        
        self.play(FadeIn(insight), Create(insight_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(generalization), FadeOut(definition),
            FadeOut(tuple_def), FadeOut(db_title), FadeOut(table),
            FadeOut(explanation), FadeOut(insight), FadeOut(insight_box),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_05_operations.py RelationOperations
    pass
