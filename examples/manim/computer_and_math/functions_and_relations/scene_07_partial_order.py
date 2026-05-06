"""
函数与关系 - Scene 7: 偏序关系
介绍偏序关系的定义、性质和哈斯图

渲染命令: manim -pqh scene_07_partial_order.py PartialOrder
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
    EQUIV_COLOR = "#2ECC71"      # 等价绿
    ORDER_COLOR = "#F39C12"      # 偏序橙
    REFLEXIVE_COLOR = "#F1C40F"  # 自反黄
    ANTISYMM_COLOR = "#E91E63"   # 反对称粉
    TRANSITIVE_COLOR = "#3498DB" # 传递蓝
    HASSE_NODE = "#9B59B6"       # 哈斯图节点
    HASSE_EDGE = "#4ECDC4"       # 哈斯图边


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


def create_hasse_node(label, color=Colors.HASSE_NODE, radius=0.25):
    """创建哈斯图节点"""
    circle = Circle(radius=radius, color=color, stroke_width=2)
    circle.set_fill(color, opacity=0.2)
    text = Text(label, font_size=14, color=Colors.TEXT)
    text.move_to(circle.get_center())
    return VGroup(circle, text)


# ========== Scene 7: 偏序关系 ==========
class PartialOrder(Scene):
    """偏序关系的定义、性质和哈斯图"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.intro()
        self.definition()
        self.compare_with_equivalence()
        self.examples()
        self.hasse_diagram()
        
        clear_scene(self)
    
    def intro(self):
        """引入"""
        section_title = Text("偏序关系", font_size=28, color=Colors.ORDER_COLOR)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        intro = VGroup(
            Text("另一种重要的关系类型", font_size=16, color=Colors.GRAY),
            Text('它能表达"顺序"或"大小"的概念', font_size=16, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.15)
        intro.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(intro))
        
        question = Text(
            "但这种顺序可能是"偏"的——不是所有元素都能比较",
            font_size=16, color=Colors.SECONDARY
        )
        question.next_to(intro, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(question, shift=UP * 0.2))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(intro), FadeOut(question), run_time=0.5)
    
    def definition(self):
        """偏序关系的定义"""
        section_title = Text("偏序关系的定义", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 前提
        premise = Text(
            "在集合 S 上的二元关系（记作 ≤），如果满足：",
            font_size=16, color=Colors.GRAY
        )
        premise.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(premise))
        
        # 三条性质
        properties = VGroup()
        
        # 自反性
        reflexive = VGroup(
            Text("1. 自反性", font_size=16, color=Colors.REFLEXIVE_COLOR),
            MathTex(r"\forall s: s \leq s", font_size=20, color=Colors.TEXT),
            Text("每个元素与自己可比", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(reflexive)
        
        # 反对称性（与等价关系的区别！）
        antisymmetric = VGroup(
            Text("2. 反对称性", font_size=16, color=Colors.ANTISYMM_COLOR),
            MathTex(r"a \leq b \land b \leq a \Rightarrow a = b", font_size=18, color=Colors.TEXT),
            Text("双向关系意味着相等", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(antisymmetric)
        
        # 传递性
        transitive = VGroup(
            Text("3. 传递性", font_size=16, color=Colors.TRANSITIVE_COLOR),
            MathTex(r"a \leq b \land b \leq c \Rightarrow a \leq c", font_size=18, color=Colors.TEXT),
            Text("顺序可以传递", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        properties.add(transitive)
        
        properties.arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        properties.next_to(premise, DOWN, buff=0.3).shift(LEFT * 0.5)
        
        for prop in properties:
            self.play(FadeIn(prop, shift=RIGHT * 0.2), run_time=0.5)
            self.wait(0.3)
        
        # 偏序集定义
        poset_def = VGroup(
            Text("配备了偏序关系的集合称为", font_size=16, color=Colors.TEXT),
            Text("偏序集 (Poset)", font_size=18, color=Colors.ORDER_COLOR),
        ).arrange(RIGHT, buff=0.1)
        poset_def.next_to(properties, DOWN, buff=0.4).set_x(0)
        
        poset_box = SurroundingRectangle(poset_def, color=Colors.ORDER_COLOR, buff=0.15)
        
        self.play(FadeIn(poset_def), Create(poset_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(premise), FadeOut(properties),
            FadeOut(poset_def), FadeOut(poset_box),
            run_time=0.5
        )
    
    def compare_with_equivalence(self):
        """与等价关系的对比"""
        section_title = Text("偏序 vs 等价", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 对比表
        comparison = VGroup()
        
        # 等价关系
        equiv_col = VGroup(
            Text("等价关系", font_size=18, color=Colors.EQUIV_COLOR),
            Text("自反性 ✓", font_size=14, color=Colors.REFLEXIVE_COLOR),
            Text("对称性 ✓", font_size=14, color=Colors.SECONDARY),
            Text("传递性 ✓", font_size=14, color=Colors.TRANSITIVE_COLOR),
        ).arrange(DOWN, buff=0.2)
        comparison.add(equiv_col)
        
        # VS
        vs = Text("vs", font_size=20, color=Colors.GRAY)
        comparison.add(vs)
        
        # 偏序关系
        order_col = VGroup(
            Text("偏序关系", font_size=18, color=Colors.ORDER_COLOR),
            Text("自反性 ✓", font_size=14, color=Colors.REFLEXIVE_COLOR),
            Text("反对称性 ✓", font_size=14, color=Colors.ANTISYMM_COLOR),
            Text("传递性 ✓", font_size=14, color=Colors.TRANSITIVE_COLOR),
        ).arrange(DOWN, buff=0.2)
        comparison.add(order_col)
        
        comparison.arrange(RIGHT, buff=0.8)
        comparison.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(comparison))
        
        # 关键区别
        key_diff = VGroup(
            Text("关键区别：", font_size=16, color=Colors.ACCENT),
            Text("对称性 → 反对称性", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.2)
        key_diff.next_to(comparison, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(key_diff))
        
        # 解释
        explain = VGroup(
            Text("等价关系：a ∼ b → b ∼ a（双向）", font_size=14, color=Colors.EQUIV_COLOR),
            Text("偏序关系：a ≤ b ∧ b ≤ a → a = b（单向，除非相等）", font_size=14, color=Colors.ORDER_COLOR),
        ).arrange(DOWN, buff=0.15)
        explain.next_to(key_diff, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(explain))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(comparison),
            FadeOut(key_diff), FadeOut(explain),
            run_time=0.5
        )
    
    def examples(self):
        """偏序的例子"""
        section_title = Text("偏序关系的例子", font_size=24, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        examples = VGroup()
        
        # 例1：整数的 ≤
        ex1 = VGroup(
            Text("1. 整数的 ≤", font_size=16, color=Colors.PRIMARY),
            Text("这是全序（任意两元素可比）", font_size=12, color=Colors.GRAY),
            Text("1 ≤ 2 ≤ 3 ≤ ...", font_size=12, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        ex1_box = SurroundingRectangle(ex1, color=Colors.PRIMARY, buff=0.1)
        examples.add(VGroup(ex1_box, ex1))
        
        # 例2：集合的包含关系
        ex2 = VGroup(
            Text("2. 集合的包含 ⊆", font_size=16, color=Colors.SECONDARY),
            Text("这是偏序（不是所有集合可比）", font_size=12, color=Colors.GRAY),
            Text("{1} ⊆ {1,2}，但 {1} 与 {2} 不可比", font_size=11, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        ex2_box = SurroundingRectangle(ex2, color=Colors.SECONDARY, buff=0.1)
        examples.add(VGroup(ex2_box, ex2))
        
        # 例3：整除关系
        ex3 = VGroup(
            Text("3. 整除关系", font_size=16, color=Colors.ORDER_COLOR),
            Text("a | b 表示 a 整除 b", font_size=12, color=Colors.GRAY),
            Text("2 | 4 | 8，但 2 与 3 不可比", font_size=11, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        ex3_box = SurroundingRectangle(ex3, color=Colors.ORDER_COLOR, buff=0.1)
        examples.add(VGroup(ex3_box, ex3))
        
        examples.arrange(RIGHT, buff=0.3)
        examples.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for ex in examples:
            self.play(FadeIn(ex, shift=UP * 0.2), run_time=0.5)
        
        # "偏"的含义
        partial_meaning = VGroup(
            Text('"偏"的含义：', font_size=16, color=Colors.ACCENT),
            Text("不是所有元素都能比较大小", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.2)
        partial_meaning.next_to(examples, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(partial_meaning))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(examples), FadeOut(partial_meaning),
            run_time=0.5
        )
    
    def hasse_diagram(self):
        """哈斯图"""
        section_title = Text("哈斯图 (Hasse Diagram)", font_size=24, color=Colors.HASSE_NODE)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 介绍
        intro = VGroup(
            Text("一种简化的有向图，用于可视化有限偏序集", font_size=14, color=Colors.GRAY),
        )
        intro.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(intro))
        
        # 简化规则
        rules = VGroup(
            Text("简化规则：", font_size=14, color=Colors.PRIMARY),
            Text("• 省略自反性的环（自己指向自己）", font_size=12, color=Colors.GRAY),
            Text("• 省略传递性必然存在的边", font_size=12, color=Colors.GRAY),
            Text("• 只保留直接的"覆盖"关系", font_size=12, color=Colors.GRAY),
            Text("• 较小的元素画在下面", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        rules.next_to(intro, DOWN, buff=0.3).shift(LEFT * 2)
        
        self.play(FadeIn(rules))
        
        # 示例：{a, b} 的幂集上的包含关系
        example_title = Text("例：{a, b} 的幂集，包含关系 ⊆", font_size=14, color=Colors.SECONDARY)
        example_title.next_to(rules, RIGHT, buff=0.8).align_to(rules, UP)
        
        self.play(FadeIn(example_title))
        
        # 创建哈斯图
        # 节点：∅, {a}, {b}, {a,b}
        node_empty = create_hasse_node("∅", Colors.HASSE_NODE)
        node_a = create_hasse_node("{a}", Colors.HASSE_NODE)
        node_b = create_hasse_node("{b}", Colors.HASSE_NODE)
        node_ab = create_hasse_node("{a,b}", Colors.HASSE_NODE)
        
        # 位置安排
        node_empty.move_to(DOWN * 0.8)
        node_a.move_to(LEFT * 0.8 + UP * 0.3)
        node_b.move_to(RIGHT * 0.8 + UP * 0.3)
        node_ab.move_to(UP * 1.4)
        
        hasse = VGroup(node_empty, node_a, node_b, node_ab)
        hasse.next_to(example_title, DOWN, buff=0.3)
        
        # 边
        edges = VGroup(
            Line(node_empty[0].get_top(), node_a[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_empty[0].get_top(), node_b[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_a[0].get_top(), node_ab[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
            Line(node_b[0].get_top(), node_ab[0].get_bottom(), color=Colors.HASSE_EDGE, stroke_width=2),
        )
        
        self.play(FadeIn(hasse))
        for edge in edges:
            self.play(Create(edge), run_time=0.3)
        
        # 说明
        note = VGroup(
            Text("读图：", font_size=12, color=Colors.PRIMARY),
            Text("• 从下到上表示"包含于"", font_size=11, color=Colors.GRAY),
            Text("• {a}和{b}无连线 → 不可比", font_size=11, color=Colors.GRAY),
            Text("• 没有画 ∅→{a,b} 的边", font_size=11, color=Colors.GRAY),
            Text("  （因为它可以通过传递性得到）", font_size=10, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.08, aligned_edge=LEFT)
        note.next_to(hasse, RIGHT, buff=0.5)
        
        self.play(FadeIn(note))
        
        # 应用
        applications = Text(
            "应用：任务调度、版本控制、类型层次...",
            font_size=14, color=Colors.ACCENT
        )
        applications.next_to(VGroup(rules, hasse), DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(applications))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(intro), FadeOut(rules),
            FadeOut(example_title), FadeOut(hasse), FadeOut(edges),
            FadeOut(note), FadeOut(applications),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_07_partial_order.py PartialOrder
    pass
