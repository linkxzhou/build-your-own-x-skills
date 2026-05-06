"""
场景7: 神经网络积木库
展示组成神经网络的各种层

运行命令:
    manim -pql scene_07_building_blocks.py BuildingBlocksScene
    manim -pqh scene_07_building_blocks.py BuildingBlocksScene
"""

from manim import *
import numpy as np

# ============ 颜色定义 ============
PRIMARY_COLOR = "#00D4FF"      # 青色 - 输入、数据
SECONDARY_COLOR = "#00FF88"    # 绿色 - 正确、优化
ACCENT_COLOR = "#FFD700"       # 金色 - 重点、高亮
NEURAL_COLOR = "#8B5CF6"       # 紫色 - 神经网络
ERROR_COLOR = "#FF6B6B"        # 红色 - 错误、损失
BG_COLOR = "#1a1a2e"           # 深色背景
TEXT_COLOR = "#FFFFFF"         # 白色文字
SUBTEXT_COLOR = "#A0A0A0"      # 灰色次要文字


class BuildingBlocksScene(Scene):
    """场景7: 神经网络积木库"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入
        self.show_intro()
        
        # 2. 各种层
        self.show_linear_layer()
        self.show_conv_layer()
        self.show_activation()
        self.show_pooling_dropout()
        self.show_skip_connection()
        self.show_attention()
        
        self.clear_scene()
    
    def show_intro(self):
        """引入：乐高类比"""
        # 标题
        title = Text("第四部分：积木库", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("组成AI模型的'乐高'零件", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        # 乐高积木可视化
        blocks = self.create_lego_blocks()
        blocks.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(FadeIn(blocks, lag_ratio=0.1), run_time=1)
        
        # 说明
        desc = Text(
            "神经网络由标准化的'层'像搭积木一样堆叠而成",
            font_size=24, color=TEXT_COLOR
        )
        desc.next_to(blocks, DOWN, buff=0.5)
        
        self.play(Write(desc), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_linear_layer(self):
        """线性层展示"""
        # 标题
        title = Text("1. 线性层 (全连接层)", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 说明
        desc = Text("最基本的组件", font_size=24, color=SUBTEXT_COLOR)
        desc.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(desc), run_time=0.3)
        
        # 神经元示意
        neuron = self.create_neuron_detail()
        neuron.next_to(desc, DOWN, buff=0.5)
        
        self.play(FadeIn(neuron), run_time=0.8)
        
        # 过程说明
        steps = VGroup(
            Text("① 接收输入信号", font_size=20, color=PRIMARY_COLOR),
            Text("② 每个信号乘以权重", font_size=20, color=SECONDARY_COLOR),
            Text("③ 加总并加偏置", font_size=20, color=ACCENT_COLOR),
            Text("④ 输出结果", font_size=20, color=NEURAL_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        steps.next_to(neuron, RIGHT, buff=0.8)
        
        for step in steps:
            self.play(Write(step), run_time=0.3)
        
        # 公式
        formula = MathTex(r"y = Wx + b", font_size=32)
        formula.to_edge(DOWN, buff=1)
        
        self.play(Write(formula), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_conv_layer(self):
        """卷积层展示"""
        # 标题
        title = Text("2. 卷积层 — 图像处理利器", font_size=36, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 类比
        desc = Text("像'局部放大镜'在图上滑动", font_size=24, color=TEXT_COLOR)
        desc.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(desc), run_time=0.5)
        
        # 图像网格
        image_grid = self.create_image_grid(6, 6)
        image_grid.scale(0.8)
        image_grid.move_to(LEFT * 2.5 + DOWN * 0.3)
        
        self.play(FadeIn(image_grid), run_time=0.5)
        
        # 卷积核 (3x3)
        kernel = self.create_kernel(3, 3)
        kernel.scale(0.8)
        kernel.move_to(image_grid.get_corner(UL) + RIGHT * 0.6 + DOWN * 0.6)
        
        self.play(FadeIn(kernel), run_time=0.3)
        
        # 输出网格
        output_label = Text("输出特征图", font_size=18, color=SUBTEXT_COLOR)
        output_grid = self.create_output_grid(4, 4)
        output_grid.scale(0.8)
        output_grid.move_to(RIGHT * 3 + DOWN * 0.3)
        output_label.next_to(output_grid, UP, buff=0.2)
        
        self.play(FadeIn(output_grid), Write(output_label), run_time=0.5)
        
        # 滑动动画
        positions = []
        for i in range(4):
            for j in range(4):
                pos = image_grid.get_corner(UL) + RIGHT * (0.6 + j * 0.4) + DOWN * (0.6 + i * 0.4)
                positions.append((pos, i, j))
        
        # 简化的滑动演示
        for idx, (pos, i, j) in enumerate(positions[:8]):  # 只显示前8个
            self.play(
                kernel.animate.move_to(pos),
                run_time=0.2
            )
            
            # 高亮输出
            output_cell = output_grid[i * 4 + j]
            self.play(
                output_cell.animate.set_fill(SECONDARY_COLOR, opacity=0.8),
                run_time=0.1
            )
        
        # 特征提取说明
        feature_text = VGroup(
            Text("提取局部特征:", font_size=20, color=TEXT_COLOR),
            Text("• 边缘", font_size=18, color=PRIMARY_COLOR),
            Text("• 纹理", font_size=18, color=SECONDARY_COLOR),
            Text("• 形状", font_size=18, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        feature_text.to_edge(RIGHT, buff=0.8)
        
        self.play(Write(feature_text), run_time=0.8)
        self.wait(1)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_activation(self):
        """激活函数展示"""
        # 标题
        title = Text("3. 激活函数 — 引入非线性", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 原因
        reason = Text(
            "如果只有线性层叠加，无论堆多少层都是线性变换",
            font_size=22, color=TEXT_COLOR
        )
        reason.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(reason), run_time=0.6)
        
        # ReLU 图示
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-1, 3, 1],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True, "color": SUBTEXT_COLOR},
        )
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes), run_time=0.5)
        
        # ReLU 函数
        relu_graph = axes.plot(
            lambda x: max(0, x),
            x_range=[-2.5, 2.5],
            color=SECONDARY_COLOR,
            stroke_width=3
        )
        
        relu_label = Text("ReLU", font_size=24, color=SECONDARY_COLOR)
        relu_label.next_to(axes, UP, buff=0.2)
        
        self.play(Create(relu_graph), Write(relu_label), run_time=0.8)
        
        # ReLU 公式和说明
        relu_formula = MathTex(r"\text{ReLU}(x) = \max(0, x)", font_size=28)
        relu_formula.to_corner(DR, buff=1)
        
        relu_desc = VGroup(
            Text("负数 → 0", font_size=18, color=ERROR_COLOR),
            Text("正数 → 保留", font_size=18, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.1)
        relu_desc.next_to(relu_formula, UP, buff=0.3)
        
        self.play(Write(relu_formula), Write(relu_desc), run_time=0.6)
        
        # 类比
        analogy = Text(
            "像开关，过滤掉'负能量'信号",
            font_size=20, color=SUBTEXT_COLOR
        )
        analogy.to_edge(DOWN, buff=0.6)
        
        self.play(Write(analogy), run_time=0.5)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_pooling_dropout(self):
        """池化层和Dropout展示"""
        # 标题
        title = Text("4-5. 池化层 & Dropout", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 左: 池化层
        pooling_title = Text("池化层", font_size=24, color=PRIMARY_COLOR)
        pooling_title.move_to(LEFT * 3.5 + UP * 1.5)
        
        # 池化演示
        pooling_demo = self.create_pooling_demo()
        pooling_demo.next_to(pooling_title, DOWN, buff=0.3)
        
        pooling_desc = Text("'压缩'数据\n保留最大值", font_size=16, color=SUBTEXT_COLOR)
        pooling_desc.next_to(pooling_demo, DOWN, buff=0.2)
        
        self.play(
            Write(pooling_title),
            FadeIn(pooling_demo),
            Write(pooling_desc),
            run_time=0.8
        )
        
        # 右: Dropout
        dropout_title = Text("Dropout", font_size=24, color=ERROR_COLOR)
        dropout_title.move_to(RIGHT * 3.5 + UP * 1.5)
        
        # Dropout 演示
        dropout_demo = self.create_dropout_demo()
        dropout_demo.next_to(dropout_title, DOWN, buff=0.3)
        
        dropout_desc = Text("随机'关闭'\n部分神经元", font_size=16, color=SUBTEXT_COLOR)
        dropout_desc.next_to(dropout_demo, DOWN, buff=0.2)
        
        self.play(
            Write(dropout_title),
            FadeIn(dropout_demo),
            Write(dropout_desc),
            run_time=0.8
        )
        
        # 动画: Dropout 效果
        neurons = dropout_demo[0]
        np.random.seed(42)
        
        for _ in range(3):
            # 随机选择要关闭的神经元
            dropout_indices = np.random.choice(len(neurons), size=4, replace=False)
            
            anims = []
            for i, neuron in enumerate(neurons):
                if i in dropout_indices:
                    anims.append(neuron.animate.set_fill(BG_COLOR, opacity=0.3))
                else:
                    anims.append(neuron.animate.set_fill(SECONDARY_COLOR, opacity=0.6))
            
            self.play(*anims, run_time=0.4)
            self.wait(0.2)
        
        # Dropout 类比
        analogy = Text(
            "强迫网络不过分依赖少数神经元 — 防止'过拟合'",
            font_size=20, color=TEXT_COLOR
        )
        analogy.to_edge(DOWN, buff=0.8)
        
        self.play(Write(analogy), run_time=0.6)
        self.wait(1)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_skip_connection(self):
        """跳跃连接展示"""
        # 标题
        title = Text("6. 跳跃连接 — 给梯度开'高速公路'", font_size=34, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 问题回顾
        problem = Text("解决梯度消失的天才设计!", font_size=22, color=TEXT_COLOR)
        problem.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(problem), run_time=0.5)
        
        # 跳跃连接示意
        skip_demo = self.create_skip_connection_demo()
        skip_demo.next_to(problem, DOWN, buff=0.5)
        
        self.play(FadeIn(skip_demo), run_time=0.8)
        
        # 说明
        explanation = VGroup(
            Text("数据直接'跳跃'到更后面的层", font_size=20, color=TEXT_COLOR),
            Text("梯度可以沿'高速公路'直接传回去", font_size=20, color=SECONDARY_COLOR),
            Text("→ 确保前面层也能得到有效更新", font_size=20, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        explanation.next_to(skip_demo, DOWN, buff=0.5)
        
        for line in explanation:
            self.play(Write(line), run_time=0.4)
        
        # ResNet 提及
        resnet = Text(
            "ResNet (残差网络) 通过这个思想，成功训练了上百层的超深网络!",
            font_size=18, color=NEURAL_COLOR
        )
        resnet.to_edge(DOWN, buff=0.6)
        
        self.play(Write(resnet), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_attention(self):
        """注意力机制展示"""
        # 标题
        title = Text("7. 注意力层 — 让模型学会'划重点'", font_size=34, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 类比
        analogy = Text(
            "像读历史书时，看到'秦始皇'就联想到'统一六国'",
            font_size=22, color=TEXT_COLOR
        )
        analogy.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(analogy), run_time=0.6)
        
        # 注意力可视化
        attention_demo = self.create_attention_demo()
        attention_demo.next_to(analogy, DOWN, buff=0.5)
        
        self.play(FadeIn(attention_demo), run_time=0.8)
        
        # Q K V 说明
        qkv = VGroup(
            VGroup(
                Text("Q", font_size=24, color=PRIMARY_COLOR),
                Text("(Query)", font_size=16, color=SUBTEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("K", font_size=24, color=SECONDARY_COLOR),
                Text("(Key)", font_size=16, color=SUBTEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("V", font_size=24, color=ACCENT_COLOR),
                Text("(Value)", font_size=16, color=SUBTEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=1)
        qkv.next_to(attention_demo, DOWN, buff=0.4)
        
        self.play(FadeIn(qkv), run_time=0.5)
        
        # 公式
        formula = MathTex(
            r"\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V",
            font_size=24
        )
        formula.to_edge(DOWN, buff=0.6)
        
        self.play(Write(formula), run_time=0.8)
        
        # 重要性
        importance = Text(
            "这是 GPT、Transformer 等大语言模型的核心!",
            font_size=20, color=NEURAL_COLOR
        )
        importance.next_to(formula, UP, buff=0.3)
        
        self.play(Write(importance), run_time=0.6)
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_lego_blocks(self):
        """创建乐高积木效果"""
        blocks = VGroup()
        
        colors = [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, NEURAL_COLOR, ERROR_COLOR]
        labels = ["线性层", "卷积层", "激活", "池化", "Dropout"]
        
        for i, (color, label) in enumerate(zip(colors, labels)):
            block = VGroup()
            
            rect = RoundedRectangle(
                width=1.2, height=0.8,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.6
            )
            rect.set_stroke(color, width=2)
            
            # 乐高凸点
            for j in range(2):
                dot = Circle(radius=0.1, color=color, fill_opacity=0.8)
                dot.move_to(rect.get_top() + LEFT * 0.25 + RIGHT * j * 0.5 + UP * 0.05)
                block.add(dot)
            
            text = Text(label, font_size=12, color=TEXT_COLOR)
            text.move_to(rect.get_center())
            
            block.add(rect, text)
            blocks.add(block)
        
        blocks.arrange(RIGHT, buff=0.3)
        return blocks
    
    def create_neuron_detail(self):
        """创建神经元详细图"""
        neuron = VGroup()
        
        # 输入
        inputs = VGroup()
        for i in range(3):
            inp = Circle(radius=0.15, color=PRIMARY_COLOR, fill_opacity=0.6)
            inp.move_to(LEFT * 3 + UP * (1 - i))
            label = MathTex(f"x_{i+1}", font_size=18)
            label.next_to(inp, LEFT, buff=0.1)
            inputs.add(VGroup(inp, label))
        
        # 求和节点
        sum_node = Circle(radius=0.4, color=ACCENT_COLOR, fill_opacity=0.4)
        sum_node.set_stroke(ACCENT_COLOR, width=2)
        sum_text = MathTex(r"\Sigma", font_size=28)
        sum_text.move_to(sum_node.get_center())
        
        # 输出
        output = Circle(radius=0.15, color=NEURAL_COLOR, fill_opacity=0.6)
        output.move_to(RIGHT * 2)
        output_label = MathTex("y", font_size=18)
        output_label.next_to(output, RIGHT, buff=0.1)
        
        # 连接线和权重
        weights = ["w_1", "w_2", "w_3"]
        for i, inp_group in enumerate(inputs):
            inp = inp_group[0]
            line = Arrow(
                inp.get_right(), sum_node.get_left() + UP * (0.5 - i * 0.5),
                buff=0.1, stroke_width=2, color=SECONDARY_COLOR
            )
            w_label = MathTex(weights[i], font_size=16, color=SECONDARY_COLOR)
            w_label.move_to(line.get_center() + UP * 0.2)
            neuron.add(line, w_label)
        
        # 偏置
        bias_arrow = Arrow(
            sum_node.get_top() + UP * 0.3, sum_node.get_top(),
            buff=0.05, stroke_width=2, color=SUBTEXT_COLOR
        )
        bias_label = MathTex("b", font_size=16, color=SUBTEXT_COLOR)
        bias_label.next_to(bias_arrow, UP, buff=0.05)
        
        # 输出箭头
        out_arrow = Arrow(
            sum_node.get_right(), output.get_left(),
            buff=0.1, stroke_width=2, color=NEURAL_COLOR
        )
        
        neuron.add(inputs, sum_node, sum_text, output, output_label)
        neuron.add(bias_arrow, bias_label, out_arrow)
        
        return neuron
    
    def create_image_grid(self, rows, cols):
        """创建图像网格"""
        grid = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=0.35, color=PRIMARY_COLOR, fill_opacity=0.3)
                cell.set_stroke(PRIMARY_COLOR, width=1)
                cell.move_to([j * 0.4, -i * 0.4, 0])
                grid.add(cell)
        
        # 居中
        grid.move_to(ORIGIN)
        return grid
    
    def create_kernel(self, rows, cols):
        """创建卷积核"""
        kernel = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=0.35, color=ACCENT_COLOR, fill_opacity=0.6)
                cell.set_stroke(ACCENT_COLOR, width=2)
                cell.move_to([j * 0.4, -i * 0.4, 0])
                kernel.add(cell)
        
        kernel.move_to(ORIGIN)
        return kernel
    
    def create_output_grid(self, rows, cols):
        """创建输出网格"""
        grid = VGroup()
        
        for i in range(rows):
            for j in range(cols):
                cell = Square(side_length=0.35, color=SECONDARY_COLOR, fill_opacity=0.2)
                cell.set_stroke(SECONDARY_COLOR, width=1)
                cell.move_to([j * 0.4, -i * 0.4, 0])
                grid.add(cell)
        
        grid.move_to(ORIGIN)
        return grid
    
    def create_pooling_demo(self):
        """创建池化演示"""
        demo = VGroup()
        
        # 输入 4x4
        input_grid = VGroup()
        values = [
            [1, 3, 2, 1],
            [4, 6, 5, 2],
            [2, 1, 3, 4],
            [1, 2, 1, 3],
        ]
        
        for i, row in enumerate(values):
            for j, val in enumerate(row):
                cell = Square(side_length=0.4, color=PRIMARY_COLOR, fill_opacity=0.3)
                cell.set_stroke(PRIMARY_COLOR, width=1)
                cell.move_to([j * 0.45, -i * 0.45, 0])
                text = Text(str(val), font_size=14, color=TEXT_COLOR)
                text.move_to(cell.get_center())
                input_grid.add(VGroup(cell, text))
        
        input_grid.move_to(LEFT * 1)
        
        # 箭头
        arrow = Arrow(LEFT * 0.2, RIGHT * 0.2, color=TEXT_COLOR, stroke_width=2)
        
        # 输出 2x2 (最大值)
        output_grid = VGroup()
        max_values = [
            [6, 5],
            [2, 4],
        ]
        
        for i, row in enumerate(max_values):
            for j, val in enumerate(row):
                cell = Square(side_length=0.5, color=SECONDARY_COLOR, fill_opacity=0.5)
                cell.set_stroke(SECONDARY_COLOR, width=2)
                cell.move_to([j * 0.55, -i * 0.55, 0])
                text = Text(str(val), font_size=16, color=TEXT_COLOR)
                text.move_to(cell.get_center())
                output_grid.add(VGroup(cell, text))
        
        output_grid.move_to(RIGHT * 1.2)
        
        demo.add(input_grid, arrow, output_grid)
        return demo
    
    def create_dropout_demo(self):
        """创建Dropout演示"""
        demo = VGroup()
        
        neurons = VGroup()
        for i in range(3):
            for j in range(3):
                neuron = Circle(radius=0.2, color=SECONDARY_COLOR, fill_opacity=0.6)
                neuron.set_stroke(SECONDARY_COLOR, width=2)
                neuron.move_to([j * 0.6, -i * 0.6, 0])
                neurons.add(neuron)
        
        neurons.move_to(ORIGIN)
        demo.add(neurons)
        
        return demo
    
    def create_skip_connection_demo(self):
        """创建跳跃连接演示"""
        demo = VGroup()
        
        # 层
        layers = VGroup()
        for i in range(4):
            layer = RoundedRectangle(
                width=0.8, height=1.2,
                corner_radius=0.1,
                color=NEURAL_COLOR,
                fill_opacity=0.4
            )
            layer.set_stroke(NEURAL_COLOR, width=2)
            layer.move_to([i * 2, 0, 0])
            label = Text(f"层{i+1}", font_size=14, color=TEXT_COLOR)
            label.move_to(layer.get_center())
            layers.add(VGroup(layer, label))
        
        layers.move_to(ORIGIN)
        
        # 正常连接
        normal_arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                layers[i][0].get_right(),
                layers[i+1][0].get_left(),
                buff=0.1, stroke_width=2, color=TEXT_COLOR
            )
            normal_arrows.add(arrow)
        
        # 跳跃连接
        skip_arrow = CurvedArrow(
            layers[0][0].get_top() + UP * 0.1,
            layers[2][0].get_top() + UP * 0.1,
            angle=-TAU / 4,
            color=SECONDARY_COLOR,
            stroke_width=3
        )
        skip_label = Text("跳跃连接", font_size=14, color=SECONDARY_COLOR)
        skip_label.next_to(skip_arrow, UP, buff=0.1)
        
        demo.add(layers, normal_arrows, skip_arrow, skip_label)
        return demo
    
    def create_attention_demo(self):
        """创建注意力机制演示"""
        demo = VGroup()
        
        # 词序列
        words = ["秦始皇", "统一", "六国", "公元前", "221年"]
        word_boxes = VGroup()
        
        for i, word in enumerate(words):
            box = RoundedRectangle(
                width=1.2, height=0.5,
                corner_radius=0.1,
                color=PRIMARY_COLOR,
                fill_opacity=0.3
            )
            box.set_stroke(PRIMARY_COLOR, width=2)
            box.move_to([i * 1.4 - 2.8, 0, 0])
            text = Text(word, font_size=14, color=TEXT_COLOR)
            text.move_to(box.get_center())
            word_boxes.add(VGroup(box, text))
        
        # 注意力连接 (从"秦始皇"到其他词)
        attention_lines = VGroup()
        weights = [1.0, 0.8, 0.7, 0.3, 0.4]
        
        for i, weight in enumerate(weights):
            if i == 0:
                continue
            line = Line(
                word_boxes[0].get_center() + DOWN * 0.3,
                word_boxes[i].get_center() + DOWN * 0.3,
                color=ACCENT_COLOR,
                stroke_width=weight * 3,
                stroke_opacity=weight
            )
            attention_lines.add(line)
        
        # 高亮当前词
        highlight = SurroundingRectangle(word_boxes[0], color=ACCENT_COLOR, buff=0.05)
        
        demo.add(word_boxes, attention_lines, highlight)
        return demo
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = BuildingBlocksScene()
    scene.render()
