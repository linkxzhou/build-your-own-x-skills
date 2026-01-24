"""
Transformer 原理教学视频 - Manim 动画
详细展示 Transformer 架构的核心概念和工作原理

运行方式:
    # 低质量预览
    manim -pql transformer.py TransformerTutorial

    # 高质量渲染
    manim -pqh transformer.py TransformerTutorial

    # 4K 渲染
    manim -pqk transformer.py TransformerTutorial
"""

from manim import *
import numpy as np


# ============ 颜色常量 ============
QUERY_COLOR = BLUE
KEY_COLOR = GREEN
VALUE_COLOR = ORANGE
ATTENTION_COLOR = RED_C
HIGHLIGHT_COLOR = YELLOW
DEFAULT_COLOR = BLUE_C


class TransformerTutorial(Scene):
    """
    Transformer 原理完整教学视频
    场景：开场 → RNN局限 → 注意力直觉 → QKV概念 → 自注意力计算 
         → 多头注意力 → 位置编码 → 完整架构 → 优势 → 总结
    """

    def construct(self):
        # 1. 开场引入
        self.intro_scene()

        # 2. RNN 的局限性
        self.rnn_limitation_scene()

        # 3. 注意力机制直觉
        self.attention_intuition_scene()

        # 4. Query, Key, Value 概念
        self.qkv_concept_scene()

        # 5. 自注意力计算过程
        self.self_attention_scene()

        # 6. 多头注意力
        self.multi_head_scene()

        # 7. 位置编码
        self.positional_encoding_scene()

        # 8. 完整架构
        self.full_architecture_scene()

        # 9. 优势总结
        self.advantages_scene()

        # 10. 总结
        self.summary_scene()

    def clear_all(self):
        """清除所有元素"""
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

    # ============ Scene 1: 开场引入 ============

    def intro_scene(self):
        """开场引入"""
        # 主标题
        title = Text("Transformer", font_size=72, color=WHITE)
        subtitle = Text("注意力机制的革命", font_size=36, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)

        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle), run_time=0.8)
        self.wait(1)

        # 移到顶部
        self.play(
            VGroup(title, subtitle).animate.scale(0.5).to_edge(UP),
            run_time=0.8
        )

        # 展示句子
        sentence = Text(
            "The animal didn't cross the street because it was too tired",
            font_size=24, color=WHITE
        )
        sentence.shift(UP * 0.5)
        self.play(Write(sentence), run_time=1.5)

        # 高亮 "it" 和 "animal"
        it_box = SurroundingRectangle(
            sentence[44:46], color=YELLOW, buff=0.05
        )
        animal_box = SurroundingRectangle(
            sentence[4:10], color=GREEN, buff=0.05
        )

        question = Text(
            '"it" 指的是什么？',
            font_size=28, color=YELLOW
        )
        question.next_to(sentence, DOWN, buff=0.8)

        self.play(Create(it_box), Write(question), run_time=0.8)
        self.wait(0.5)

        # 连接线
        arrow = CurvedArrow(
            sentence[44:46].get_bottom() + DOWN * 0.1,
            sentence[4:10].get_bottom() + DOWN * 0.1,
            color=GREEN, angle=-TAU/4
        )
        self.play(Create(animal_box), Create(arrow), run_time=0.8)

        answer = Text(
            "人类轻松理解，但机器需要'看到'整个句子",
            font_size=22, color=GRAY
        )
        answer.next_to(question, DOWN, buff=0.4)
        self.play(FadeIn(answer), run_time=0.6)

        # 核心问题
        core = Text(
            "机器如何理解语言中的长距离依赖？",
            font_size=26, color=HIGHLIGHT_COLOR
        )
        core.to_edge(DOWN, buff=0.8)
        self.play(Write(core), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 2: RNN 的局限性 ============

    def rnn_limitation_scene(self):
        """RNN 的局限性"""
        title = Text("传统方法：RNN 的困境", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # RNN 结构
        cells = VGroup()
        arrows = VGroup()
        words = ["The", "cat", "sat", "on", "the", "mat"]

        for i in range(6):
            cell = Square(side_length=0.8, color=BLUE, fill_opacity=0.3)
            cell.shift(RIGHT * (i - 2.5) * 1.3)
            cells.add(cell)

            word = Text(words[i], font_size=16, color=WHITE)
            word.next_to(cell, DOWN, buff=0.2)
            cells.add(word)

            if i > 0:
                arrow = Arrow(
                    cells[2 * (i - 1)].get_right(),
                    cell.get_left(),
                    buff=0.1, color=GRAY, stroke_width=2
                )
                arrows.add(arrow)

        rnn_group = VGroup(cells, arrows)
        rnn_group.shift(UP * 0.5)

        self.play(Create(cells), run_time=1)
        self.play(Create(arrows), run_time=0.6)

        # 信息衰减动画
        decay_text = Text("信息随时间衰减...", font_size=20, color=RED_C)
        decay_text.next_to(rnn_group, UP, buff=0.3)
        self.play(FadeIn(decay_text), run_time=0.5)

        # 显示信息流衰减
        for i, arrow in enumerate(arrows):
            opacity = 1 - i * 0.18
            self.play(
                arrow.animate.set_opacity(opacity),
                run_time=0.2
            )

        # 问题说明
        problems = VGroup(
            Text("问题 1: 长距离依赖困难", font_size=22, color=RED_C),
            Text("信息传得越远，丢失得越多", font_size=18, color=GRAY),
            Text("问题 2: 无法并行计算", font_size=22, color=RED_C),
            Text("必须按顺序处理，训练很慢", font_size=18, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        problems.to_edge(DOWN, buff=0.8)

        for p in problems:
            self.play(FadeIn(p, shift=RIGHT), run_time=0.4)

        # 类比
        analogy = Text(
            "RNN 像传话游戏，信息传得越远，失真越严重",
            font_size=20, color=YELLOW
        )
        analogy.next_to(problems, UP, buff=0.4)
        self.play(Write(analogy), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 3: 注意力机制直觉 ============

    def attention_intuition_scene(self):
        """注意力机制的直觉"""
        title = Text("核心思想：注意力机制", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 句子
        words = ["The", "animal", "didn't", "cross", "because", "it", "was", "tired"]
        word_texts = VGroup()
        for i, w in enumerate(words):
            t = Text(w, font_size=24, color=WHITE)
            t.shift(RIGHT * (i - 3.5) * 1.4 + UP * 0.5)
            word_texts.add(t)

        self.play(Write(word_texts), run_time=1)

        # 高亮 "it"
        it_idx = 5
        self.play(word_texts[it_idx].animate.set_color(YELLOW), run_time=0.3)

        # 注意力连接
        attention_text = Text(
            '"it" 在关注哪些词？',
            font_size=22, color=YELLOW
        )
        attention_text.next_to(word_texts, DOWN, buff=0.8)
        self.play(Write(attention_text), run_time=0.6)

        # 注意力权重（模拟）
        weights = [0.05, 0.7, 0.05, 0.05, 0.05, 0.0, 0.05, 0.05]
        lines = VGroup()

        for i, w in enumerate(weights):
            if i != it_idx and w > 0:
                line = Line(
                    word_texts[it_idx].get_bottom() + DOWN * 0.1,
                    word_texts[i].get_top() + UP * 0.1,
                    color=ATTENTION_COLOR,
                    stroke_width=w * 8
                )
                line.set_opacity(w + 0.3)
                lines.add(line)

        self.play(Create(lines), run_time=0.8)

        # 高亮 "animal"（最高权重）
        self.play(
            word_texts[1].animate.set_color(GREEN).scale(1.2),
            run_time=0.5
        )

        # 解释
        explain = VGroup(
            Text("注意力机制：", font_size=22, color=WHITE),
            Text("• 让每个词都能'看到'整个句子", font_size=18, color=GRAY),
            Text("• 动态计算词与词之间的相关性", font_size=18, color=GRAY),
            Text("• 重点关注最相关的部分", font_size=18, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        explain.to_edge(DOWN, buff=0.6)

        for e in explain:
            self.play(FadeIn(e, shift=RIGHT), run_time=0.3)

        self.wait(2)
        self.clear_all()

    # ============ Scene 4: QKV 概念 ============

    def qkv_concept_scene(self):
        """Query, Key, Value 概念"""
        title = Text("核心概念：Query, Key, Value", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 图书馆类比
        analogy_title = Text("类比：图书馆查询系统", font_size=26, color=GRAY)
        analogy_title.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(analogy_title), run_time=0.4)

        # QKV 解释
        qkv_items = VGroup(
            VGroup(
                Text("Query (Q)", font_size=28, color=QUERY_COLOR),
                Text("你想找什么？", font_size=20, color=GRAY),
                Text("'我想找关于猫的书'", font_size=18, color=WHITE),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Key (K)", font_size=28, color=KEY_COLOR),
                Text("每本书的标签", font_size=20, color=GRAY),
                Text("'动物类'、'宠物类'...", font_size=18, color=WHITE),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Value (V)", font_size=28, color=VALUE_COLOR),
                Text("书的实际内容", font_size=20, color=GRAY),
                Text("书中的知识和信息", font_size=18, color=WHITE),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1.2)
        qkv_items.shift(UP * 0.3)

        for item in qkv_items:
            self.play(FadeIn(item, shift=UP), run_time=0.5)

        self.wait(0.5)

        # 在 Transformer 中
        transformer_text = Text(
            "在 Transformer 中：",
            font_size=24, color=WHITE
        )
        transformer_text.shift(DOWN * 1.2)
        self.play(Write(transformer_text), run_time=0.5)

        process = VGroup(
            Text("每个词 → 生成自己的 Q, K, V", font_size=20, color=GRAY),
            Text("用 Q 去查询其他词的 K", font_size=20, color=GRAY),
            Text("根据匹配程度获取对应的 V", font_size=20, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        process.next_to(transformer_text, DOWN, buff=0.3)

        for p in process:
            self.play(FadeIn(p, shift=RIGHT), run_time=0.3)

        # 核心公式预览
        formula_hint = Text(
            "Attention(Q, K, V) = softmax(QK^T / √d) × V",
            font_size=22, color=YELLOW
        )
        formula_hint.to_edge(DOWN, buff=0.5)
        self.play(Write(formula_hint), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 5: 自注意力计算 ============

    def self_attention_scene(self):
        """自注意力计算过程"""
        title = Text("自注意力计算过程", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.6)

        # 输入序列
        input_label = Text("输入词向量:", font_size=18, color=GRAY)
        input_label.shift(UP * 2 + LEFT * 5)
        self.play(FadeIn(input_label), run_time=0.3)

        words = ["I", "love", "AI"]
        word_boxes = VGroup()
        for i, w in enumerate(words):
            box = VGroup(
                Rectangle(width=0.8, height=0.5, color=WHITE, fill_opacity=0.2),
                Text(w, font_size=16, color=WHITE)
            )
            box.shift(UP * 2 + LEFT * 3 + RIGHT * i * 1.2)
            word_boxes.add(box)

        self.play(Create(word_boxes), run_time=0.5)

        # Step 1: 生成 Q, K, V
        step1 = Text("Step 1: 通过权重矩阵生成 Q, K, V", font_size=18, color=HIGHLIGHT_COLOR)
        step1.shift(UP * 1 + LEFT * 2)
        self.play(Write(step1), run_time=0.5)

        # QKV 矩阵
        q_matrix = VGroup(
            Rectangle(width=1.2, height=0.8, color=QUERY_COLOR, fill_opacity=0.4),
            Text("Q", font_size=20, color=QUERY_COLOR)
        )
        k_matrix = VGroup(
            Rectangle(width=1.2, height=0.8, color=KEY_COLOR, fill_opacity=0.4),
            Text("K", font_size=20, color=KEY_COLOR)
        )
        v_matrix = VGroup(
            Rectangle(width=1.2, height=0.8, color=VALUE_COLOR, fill_opacity=0.4),
            Text("V", font_size=20, color=VALUE_COLOR)
        )

        qkv_group = VGroup(q_matrix, k_matrix, v_matrix).arrange(RIGHT, buff=0.5)
        qkv_group.shift(UP * 0.2)

        arrows_to_qkv = VGroup(*[
            Arrow(word_boxes.get_bottom(), qkv_group.get_top(), buff=0.2, color=GRAY, stroke_width=2)
        ])

        self.play(Create(arrows_to_qkv), run_time=0.3)
        self.play(Create(qkv_group), run_time=0.5)

        # Step 2: 计算注意力分数
        step2 = Text("Step 2: 计算注意力分数 Q × K^T", font_size=18, color=HIGHLIGHT_COLOR)
        step2.shift(DOWN * 0.8 + LEFT * 2)
        self.play(Write(step2), run_time=0.5)

        # 注意力分数矩阵
        score_matrix = VGroup(
            Rectangle(width=1.5, height=1.5, color=ATTENTION_COLOR, fill_opacity=0.3),
            Text("Scores", font_size=16, color=ATTENTION_COLOR)
        )
        score_matrix.shift(DOWN * 0.8 + RIGHT * 2)

        self.play(
            q_matrix.copy().animate.move_to(score_matrix.get_left() + LEFT * 0.5),
            k_matrix.copy().animate.move_to(score_matrix.get_top() + UP * 0.3),
            run_time=0.5
        )
        self.play(Create(score_matrix), run_time=0.4)

        # Step 3: Softmax
        step3 = Text("Step 3: Softmax 归一化", font_size=18, color=HIGHLIGHT_COLOR)
        step3.shift(DOWN * 2 + LEFT * 2)
        self.play(Write(step3), run_time=0.5)

        softmax_text = MathTex(
            r"\text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)",
            font_size=28, color=WHITE
        )
        softmax_text.shift(DOWN * 2 + RIGHT * 2)
        self.play(Write(softmax_text), run_time=0.6)

        # Step 4: 加权求和
        step4 = Text("Step 4: 与 V 加权求和得到输出", font_size=18, color=HIGHLIGHT_COLOR)
        step4.shift(DOWN * 3 + LEFT * 2)
        self.play(Write(step4), run_time=0.5)

        # 完整公式
        full_formula = MathTex(
            r"\text{Attention}(Q,K,V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=26, color=YELLOW
        )
        full_formula.to_edge(DOWN, buff=0.4)
        self.play(Write(full_formula), run_time=0.8)

        self.wait(2)
        self.clear_all()

    # ============ Scene 6: 多头注意力 ============

    def multi_head_scene(self):
        """多头注意力"""
        title = Text("多头注意力 (Multi-Head Attention)", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 问题引入
        problem = Text(
            "单头注意力只能关注一种关系...",
            font_size=22, color=GRAY
        )
        problem.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(problem), run_time=0.5)

        # 多个注意力头
        heads = VGroup()
        head_colors = [RED, GREEN, BLUE, PURPLE]
        head_names = ["语法关系", "语义关系", "位置关系", "其他模式"]

        for i in range(4):
            head = VGroup(
                Rectangle(width=1.2, height=1.8, color=head_colors[i], fill_opacity=0.4),
                Text(f"Head {i + 1}", font_size=14, color=head_colors[i]),
                Text(head_names[i], font_size=12, color=GRAY)
            )
            head[1].move_to(head[0].get_top() + DOWN * 0.3)
            head[2].move_to(head[0].get_bottom() + UP * 0.3)
            heads.add(head)

        heads.arrange(RIGHT, buff=0.4)
        heads.shift(UP * 0.3)

        self.play(Create(heads), run_time=1)

        # 解释
        explain = Text(
            "多头注意力：同时从多个角度分析关系",
            font_size=22, color=HIGHLIGHT_COLOR
        )
        explain.next_to(heads, DOWN, buff=0.6)
        self.play(Write(explain), run_time=0.6)

        # 合并过程
        concat_text = Text("最后拼接 (Concat) 并投影", font_size=20, color=GRAY)
        concat_text.next_to(explain, DOWN, buff=0.4)

        # 箭头汇聚
        output_box = Rectangle(width=2, height=0.8, color=WHITE, fill_opacity=0.3)
        output_box.next_to(concat_text, DOWN, buff=0.4)
        output_label = Text("Output", font_size=16, color=WHITE)
        output_label.move_to(output_box)

        arrows = VGroup(*[
            Arrow(heads[i].get_bottom(), output_box.get_top(), buff=0.1, color=GRAY, stroke_width=2)
            for i in range(4)
        ])

        self.play(Write(concat_text), run_time=0.5)
        self.play(Create(arrows), Create(output_box), Write(output_label), run_time=0.6)

        # 公式
        formula = MathTex(
            r"\text{MultiHead} = \text{Concat}(\text{head}_1,...,\text{head}_h)W^O",
            font_size=24, color=WHITE
        )
        formula.to_edge(DOWN, buff=0.4)
        self.play(Write(formula), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 7: 位置编码 ============

    def positional_encoding_scene(self):
        """位置编码"""
        title = Text("位置编码 (Positional Encoding)", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 问题
        problem = VGroup(
            Text("问题：自注意力没有位置概念", font_size=22, color=RED_C),
            Text('"猫吃鱼" 和 "鱼吃猫" 对注意力来说一样！', font_size=20, color=GRAY),
        ).arrange(DOWN, buff=0.2)
        problem.next_to(title, DOWN, buff=0.4)
        self.play(FadeIn(problem), run_time=0.6)

        # 解决方案
        solution = Text(
            "解决：给每个位置添加唯一的位置编码",
            font_size=22, color=GREEN
        )
        solution.next_to(problem, DOWN, buff=0.5)
        self.play(Write(solution), run_time=0.6)

        # 正弦波可视化
        axes = Axes(
            x_range=[0, 4 * PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=6,
            y_length=2,
            axis_config={"include_tip": False},
        )
        axes.shift(DOWN * 0.8)

        sin_graph = axes.plot(lambda x: np.sin(x), color=BLUE)
        cos_graph = axes.plot(lambda x: np.cos(x), color=RED)

        sin_label = Text("sin", font_size=16, color=BLUE)
        sin_label.next_to(sin_graph, RIGHT, buff=0.1)
        cos_label = Text("cos", font_size=16, color=RED)
        cos_label.next_to(cos_graph, RIGHT, buff=0.1).shift(UP * 0.3)

        self.play(Create(axes), run_time=0.5)
        self.play(Create(sin_graph), Create(cos_graph), run_time=0.8)
        self.play(FadeIn(sin_label), FadeIn(cos_label), run_time=0.3)

        # 公式
        pe_formula = MathTex(
            r"PE_{(pos,2i)} = \sin\left(\frac{pos}{10000^{2i/d}}\right)",
            font_size=22, color=WHITE
        )
        pe_formula.to_edge(DOWN, buff=0.8)
        self.play(Write(pe_formula), run_time=0.6)

        # 解释
        explain = Text(
            "正弦/余弦函数为每个位置生成唯一的'坐标'",
            font_size=20, color=YELLOW
        )
        explain.next_to(pe_formula, UP, buff=0.3)
        self.play(Write(explain), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 8: 完整架构 ============

    def full_architecture_scene(self):
        """完整 Transformer 架构"""
        title = Text("Transformer 完整架构", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.3)
        self.play(Write(title), run_time=0.6)

        # 编码器
        encoder_title = Text("Encoder", font_size=20, color=BLUE)
        encoder_box = Rectangle(width=2.5, height=4, color=BLUE, fill_opacity=0.2)
        encoder_title.next_to(encoder_box, UP, buff=0.1)

        encoder_components = VGroup(
            self.create_component("Multi-Head\nAttention", BLUE_C),
            self.create_component("Add & Norm", GRAY),
            self.create_component("Feed\nForward", BLUE_C),
            self.create_component("Add & Norm", GRAY),
        ).arrange(DOWN, buff=0.15)
        encoder_components.move_to(encoder_box)

        encoder_group = VGroup(encoder_box, encoder_title, encoder_components)
        encoder_group.shift(LEFT * 2.5)

        # 解码器
        decoder_title = Text("Decoder", font_size=20, color=GREEN)
        decoder_box = Rectangle(width=2.5, height=5, color=GREEN, fill_opacity=0.2)
        decoder_title.next_to(decoder_box, UP, buff=0.1)

        decoder_components = VGroup(
            self.create_component("Masked\nSelf-Attention", GREEN_C),
            self.create_component("Add & Norm", GRAY),
            self.create_component("Cross\nAttention", ORANGE),
            self.create_component("Add & Norm", GRAY),
            self.create_component("Feed\nForward", GREEN_C),
            self.create_component("Add & Norm", GRAY),
        ).arrange(DOWN, buff=0.1)
        decoder_components.move_to(decoder_box)

        decoder_group = VGroup(decoder_box, decoder_title, decoder_components)
        decoder_group.shift(RIGHT * 2.5)

        # 显示
        self.play(Create(encoder_group), run_time=1)
        self.play(Create(decoder_group), run_time=1)

        # 连接箭头
        cross_arrow = Arrow(
            encoder_box.get_right(),
            decoder_components[2].get_left(),
            buff=0.1, color=ORANGE, stroke_width=3
        )
        self.play(Create(cross_arrow), run_time=0.5)

        # 输入输出
        input_text = Text("输入", font_size=16, color=WHITE)
        input_text.next_to(encoder_box, DOWN, buff=0.3)
        output_text = Text("输出", font_size=16, color=WHITE)
        output_text.next_to(decoder_box, DOWN, buff=0.3)

        self.play(FadeIn(input_text), FadeIn(output_text), run_time=0.4)

        # 说明
        explain = VGroup(
            Text("编码器：理解输入序列", font_size=18, color=BLUE),
            Text("解码器：生成输出序列", font_size=18, color=GREEN),
            Text("Cross Attention：连接编码器和解码器", font_size=18, color=ORANGE),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        explain.to_edge(DOWN, buff=0.3)

        for e in explain:
            self.play(FadeIn(e, shift=RIGHT), run_time=0.3)

        self.wait(2)
        self.clear_all()

    def create_component(self, text, color):
        """创建架构组件"""
        box = Rectangle(width=2, height=0.5, color=color, fill_opacity=0.4)
        label = Text(text, font_size=10, color=WHITE)
        label.move_to(box)
        return VGroup(box, label)

    # ============ Scene 9: 优势 ============

    def advantages_scene(self):
        """Transformer 的优势"""
        title = Text("为什么 Transformer 如此成功？", font_size=40, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 优势列表
        advantages = VGroup(
            VGroup(
                Text("1. 并行计算", font_size=26, color=GREEN),
                Text("所有位置同时处理，训练速度大幅提升", font_size=18, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("2. 长距离依赖", font_size=26, color=BLUE),
                Text("任意两个位置直接连接，信息不衰减", font_size=18, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("3. 可扩展性", font_size=26, color=ORANGE),
                Text("轻松扩展到更大规模，性能持续提升", font_size=18, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
            VGroup(
                Text("4. 可解释性", font_size=26, color=PURPLE),
                Text("注意力权重可视化，了解模型关注点", font_size=18, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.1),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.4)
        advantages.next_to(title, DOWN, buff=0.5)

        for adv in advantages:
            self.play(FadeIn(adv, shift=RIGHT), run_time=0.5)

        # 对比
        compare = Text(
            "vs RNN: 并行 ✓  长距离 ✓  可扩展 ✓",
            font_size=22, color=YELLOW
        )
        compare.to_edge(DOWN, buff=0.6)
        self.play(Write(compare), run_time=0.6)

        self.wait(2)
        self.clear_all()

    # ============ Scene 10: 总结 ============

    def summary_scene(self):
        """总结"""
        title = Text("总结", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.6)

        # 核心概念
        summary = VGroup(
            Text("Transformer 核心概念:", font_size=26, color=WHITE),
            VGroup(
                Text("自注意力", font_size=22, color=BLUE),
                Text("让每个词都能看到整个序列", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(
                Text("Q, K, V", font_size=22, color=GREEN),
                Text("查询 - 匹配 - 取值", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(
                Text("多头注意力", font_size=22, color=ORANGE),
                Text("多角度同时分析", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
            VGroup(
                Text("位置编码", font_size=22, color=PURPLE),
                Text("赋予序列位置信息", font_size=16, color=GRAY),
            ).arrange(DOWN, aligned_edge=LEFT, buff=0.08),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        summary.next_to(title, DOWN, buff=0.4).shift(LEFT * 2)

        for item in summary:
            self.play(FadeIn(item, shift=RIGHT), run_time=0.35)

        # 应用
        apps_title = Text("应用:", font_size=22, color=WHITE)
        apps_title.to_edge(RIGHT, buff=1.5).shift(UP * 1)
        apps = VGroup(
            Text("• GPT (语言生成)", font_size=18, color=GRAY),
            Text("• BERT (语言理解)", font_size=18, color=GRAY),
            Text("• ViT (图像识别)", font_size=18, color=GRAY),
            Text("• Stable Diffusion", font_size=18, color=GRAY),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        apps.next_to(apps_title, DOWN, buff=0.2)

        self.play(FadeIn(apps_title), run_time=0.3)
        self.play(FadeIn(apps), run_time=0.5)

        # 核心思想
        key = Text(
            '"Attention Is All You Need"',
            font_size=24, color=YELLOW
        )
        key.to_edge(DOWN, buff=1)
        self.play(Write(key), run_time=0.8)

        self.wait(1.5)

        # 感谢
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

        thanks = Text("感谢观看！", font_size=56, color=WHITE)
        self.play(FadeIn(thanks, scale=1.2), run_time=0.8)
        self.wait(2)
        self.play(FadeOut(thanks))


if __name__ == "__main__":
    scene = TransformerTutorial()
    scene.render()
