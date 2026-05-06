"""
神经网络原理教学视频
使用 ManimCE 创建详细的神经网络教学动画

运行命令:
    manim -pql neural_network.py NeuralNetworkTutorial  # 低质量预览
    manim -pqh neural_network.py NeuralNetworkTutorial  # 高质量渲染
"""

from manim import *
import numpy as np

# 颜色定义
INPUT_COLOR = "#3498DB"      # 蓝色 - 输入层
HIDDEN_COLOR = "#9B59B6"     # 紫色 - 隐藏层
OUTPUT_COLOR = "#E67E22"     # 橙色 - 输出层
POSITIVE_WEIGHT = "#2ECC71"  # 绿色 - 正权重
NEGATIVE_WEIGHT = "#E74C3C"  # 红色 - 负权重
ACTIVATION_COLOR = "#F1C40F" # 黄色 - 激活状态
GRADIENT_COLOR = "#1ABC9C"   # 青色 - 梯度


class NeuralNetworkTutorial(Scene):
    """神经网络原理完整教程"""
    
    def construct(self):
        # 1. 开场引入
        self.intro_scene()
        
        # 2. 生物神经元
        self.biological_neuron_scene()
        
        # 3. 感知机
        self.perceptron_scene()
        
        # 4. 激活函数
        self.activation_functions_scene()
        
        # 5. 多层神经网络
        self.multilayer_network_scene()
        
        # 6. 前向传播
        self.forward_propagation_scene()
        
        # 7. 损失函数
        self.loss_function_scene()
        
        # 8. 反向传播
        self.backpropagation_scene()
        
        # 9. 梯度下降
        self.gradient_descent_scene()
        
        # 10. 实际案例
        self.mnist_example_scene()
        
        # 11. 过拟合与正则化
        self.regularization_scene()
        
        # 12. 总结
        self.summary_scene()

    # ============ 工具方法 ============
    
    def create_neuron(self, radius=0.3, color=HIDDEN_COLOR, fill_opacity=0.8):
        """创建单个神经元"""
        return Circle(radius=radius, color=color, fill_opacity=fill_opacity, stroke_width=2)
    
    def create_neural_network(self, layer_sizes, x_spacing=2.5, y_spacing=0.8):
        """创建神经网络结构图"""
        layers = VGroup()
        all_neurons = []
        
        colors = [INPUT_COLOR, HIDDEN_COLOR, HIDDEN_COLOR, OUTPUT_COLOR]
        
        for i, size in enumerate(layer_sizes):
            layer = VGroup()
            neurons = []
            color = colors[min(i, len(colors)-1)] if i == 0 else (colors[-1] if i == len(layer_sizes)-1 else HIDDEN_COLOR)
            
            for j in range(size):
                neuron = self.create_neuron(radius=0.25, color=color)
                y_pos = (size - 1) / 2 * y_spacing - j * y_spacing
                neuron.move_to([i * x_spacing - (len(layer_sizes)-1) * x_spacing / 2, y_pos, 0])
                layer.add(neuron)
                neurons.append(neuron)
            
            layers.add(layer)
            all_neurons.append(neurons)
        
        # 创建连接线
        connections = VGroup()
        for i in range(len(all_neurons) - 1):
            for n1 in all_neurons[i]:
                for n2 in all_neurons[i+1]:
                    line = Line(
                        n1.get_center(), n2.get_center(),
                        stroke_width=1, stroke_opacity=0.4, color=WHITE
                    )
                    connections.add(line)
        
        return layers, connections, all_neurons

    def clear_scene(self):
        """清除当前场景"""
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)

    # ============ 场景实现 ============
    
    def intro_scene(self):
        """场景1: 开场引入"""
        # 标题
        title = Text("神经网络原理详解", font_size=56, color=WHITE)
        subtitle = Text("Neural Networks Explained", font_size=32, color=GRAY)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP*0.3), run_time=0.8)
        self.wait(1)
        
        # 问题引入
        self.play(FadeOut(title), FadeOut(subtitle))
        
        question = Text("计算机如何像人脑一样思考？", font_size=44, color=YELLOW)
        self.play(Write(question), run_time=1.5)
        self.wait(1)
        
        # 大脑图示
        brain = SVGMobject("brain.svg") if False else self.create_brain_shape()
        brain.scale(1.5).next_to(question, DOWN, buff=0.8)
        
        self.play(FadeIn(brain, scale=0.8), run_time=1)
        self.wait(1)
        
        # 过渡
        answer = Text("让我们从最基本的单元开始...", font_size=36, color=WHITE)
        answer.to_edge(DOWN, buff=1)
        self.play(Write(answer), run_time=1)
        self.wait(1)
        
        self.clear_scene()
    
    def create_brain_shape(self):
        """创建简化的大脑形状"""
        brain = VGroup()
        # 左半球
        left = Ellipse(width=2, height=2.5, color=PINK, fill_opacity=0.3)
        left.shift(LEFT*0.8)
        # 右半球
        right = Ellipse(width=2, height=2.5, color=PINK, fill_opacity=0.3)
        right.shift(RIGHT*0.8)
        # 中间连接
        brain.add(left, right)
        
        # 添加一些神经连接线
        for _ in range(8):
            start = np.array([np.random.uniform(-1.5, 1.5), np.random.uniform(-1, 1), 0])
            end = np.array([np.random.uniform(-1.5, 1.5), np.random.uniform(-1, 1), 0])
            line = Line(start, end, stroke_width=1, color=BLUE_C, stroke_opacity=0.5)
            brain.add(line)
        
        return brain
    
    def biological_neuron_scene(self):
        """场景2: 生物神经元"""
        # 标题
        title = Text("生物神经元", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 创建生物神经元结构
        neuron = self.create_biological_neuron()
        neuron.scale(0.9).shift(DOWN*0.3)
        
        self.play(FadeIn(neuron), run_time=1)
        self.wait(0.5)
        
        # 标注各部分
        labels = VGroup()
        
        dendrite_label = Text("树突 (Dendrites)\n接收信号", font_size=20, color=BLUE)
        dendrite_label.move_to([-4.5, 1.5, 0])
        
        soma_label = Text("细胞体\n处理信号", font_size=20, color=GREEN)
        soma_label.move_to([-1, -2, 0])
        
        axon_label = Text("轴突 (Axon)\n传递信号", font_size=20, color=ORANGE)
        axon_label.move_to([2.5, -1.5, 0])
        
        synapse_label = Text("突触\n连接下一个", font_size=20, color=RED)
        synapse_label.move_to([5, 0.5, 0])
        
        labels.add(dendrite_label, soma_label, axon_label, synapse_label)
        
        for label in labels:
            self.play(FadeIn(label), run_time=0.5)
        
        self.wait(1)
        
        # 信号传递动画
        signal_text = Text("信号传递过程", font_size=32, color=YELLOW)
        signal_text.to_edge(DOWN, buff=0.5)
        self.play(Write(signal_text), run_time=0.5)
        
        # 创建信号点
        signal = Dot(color=YELLOW, radius=0.15)
        signal.move_to([-5, 1, 0])
        
        self.play(FadeIn(signal))
        
        # 信号沿着路径移动
        path_points = [[-5, 1, 0], [-3, 0.5, 0], [-1, 0, 0], [1, 0, 0], [3, 0, 0], [5, 0, 0]]
        for i in range(len(path_points) - 1):
            self.play(
                signal.animate.move_to(path_points[i+1]),
                run_time=0.4
            )
        
        self.wait(1)
        
        # 阈值概念
        threshold_text = Text("当输入信号超过阈值时，神经元被激活", font_size=28, color=WHITE)
        threshold_text.next_to(signal_text, UP, buff=0.3)
        self.play(Write(threshold_text), run_time=1)
        
        self.wait(1.5)
        self.clear_scene()
    
    def create_biological_neuron(self):
        """创建生物神经元图形"""
        neuron = VGroup()
        
        # 细胞体
        soma = Circle(radius=0.8, color=GREEN, fill_opacity=0.5)
        soma.move_to([-1, 0, 0])
        neuron.add(soma)
        
        # 树突 (多个输入分支)
        for i in range(5):
            angle = PI/2 + (i - 2) * PI/6
            start = soma.get_center() + np.array([np.cos(angle), np.sin(angle), 0]) * 0.8
            
            # 主干
            branch_end = start + np.array([np.cos(angle), np.sin(angle), 0]) * 1.5
            branch = Line(start, branch_end, color=BLUE, stroke_width=3)
            neuron.add(branch)
            
            # 小分支
            for j in range(3):
                sub_start = start + (branch_end - start) * (0.3 + j * 0.25)
                sub_angle = angle + (np.random.random() - 0.5) * PI/3
                sub_end = sub_start + np.array([np.cos(sub_angle), np.sin(sub_angle), 0]) * 0.4
                sub_branch = Line(sub_start, sub_end, color=BLUE, stroke_width=2)
                neuron.add(sub_branch)
        
        # 轴突
        axon_points = [
            soma.get_center() + RIGHT * 0.8,
            soma.get_center() + RIGHT * 2,
            soma.get_center() + RIGHT * 3.5 + DOWN * 0.3,
            soma.get_center() + RIGHT * 5,
        ]
        axon = VMobject(color=ORANGE, stroke_width=4)
        axon.set_points_smoothly([np.array(p) for p in axon_points])
        neuron.add(axon)
        
        # 突触末端
        for i in range(3):
            end_point = axon_points[-1] + np.array([0.5, (i-1)*0.4, 0])
            terminal = Circle(radius=0.15, color=RED, fill_opacity=0.7)
            terminal.move_to(end_point)
            neuron.add(terminal)
            
            connector = Line(axon_points[-1], end_point, color=ORANGE, stroke_width=2)
            neuron.add(connector)
        
        return neuron
    
    def perceptron_scene(self):
        """场景3: 感知机"""
        # 标题
        title = Text("感知机 - 最简单的神经网络", font_size=44, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=1)
        
        # 类比说明
        analogy = Text("生物神经元 → 人工神经元", font_size=32, color=YELLOW)
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeOut(analogy))
        
        # 创建感知机结构
        perceptron = self.create_perceptron()
        perceptron.shift(LEFT * 1.5)
        
        self.play(FadeIn(perceptron), run_time=1)
        self.wait(0.5)
        
        # 数学公式
        formula_title = Text("数学表达:", font_size=28, color=WHITE)
        formula_title.move_to([3.5, 2, 0])
        
        formula = MathTex(
            r"y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)",
            font_size=36
        )
        formula.next_to(formula_title, DOWN, buff=0.3)
        
        self.play(Write(formula_title), run_time=0.5)
        self.play(Write(formula), run_time=1)
        
        # 解释各部分
        explanations = VGroup(
            VGroup(MathTex(r"x_i", font_size=24), Text(" - Input", font_size=18)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"w_i", font_size=24), Text(" - Weight", font_size=18)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"b", font_size=24), Text(" - Bias", font_size=18)).arrange(RIGHT, buff=0.1),
            VGroup(MathTex(r"f", font_size=24), Text(" - Activation", font_size=18)).arrange(RIGHT, buff=0.1),
        )
        explanations.arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        explanations.next_to(formula, DOWN, buff=0.5)
        
        for exp in explanations:
            self.play(FadeIn(exp), run_time=0.3)
        
        self.wait(1.5)
        
        # AND 门示例
        self.play(FadeOut(explanations), FadeOut(formula), FadeOut(formula_title))
        
        example_title = Text("示例: 实现 AND 门", font_size=32, color=YELLOW)
        example_title.move_to([3.5, 2, 0])
        self.play(Write(example_title), run_time=0.5)
        
        # AND 门真值表
        table_data = [
            ["x1", "x2", "输出"],
            ["0", "0", "0"],
            ["0", "1", "0"],
            ["1", "0", "0"],
            ["1", "1", "1"],
        ]
        
        table = self.create_table(table_data)
        table.scale(0.7).move_to([3.5, -0.5, 0])
        
        self.play(FadeIn(table), run_time=0.8)
        
        # 参数设置
        params = MathTex(r"w_1 = 1, w_2 = 1, b = -1.5", font_size=28)
        params.next_to(table, DOWN, buff=0.3)
        self.play(Write(params), run_time=0.5)
        
        self.wait(2)
        self.clear_scene()
    
    def create_perceptron(self):
        """创建感知机图形"""
        perceptron = VGroup()
        
        # 输入节点
        inputs = VGroup()
        input_labels = ["x_1", "x_2", "x_3"]
        for i, label in enumerate(input_labels):
            node = Circle(radius=0.3, color=INPUT_COLOR, fill_opacity=0.7)
            node.move_to([-3, (1-i)*1.2, 0])
            text = MathTex(label, font_size=24).move_to(node.get_center())
            inputs.add(VGroup(node, text))
        perceptron.add(inputs)
        
        # 求和节点
        sum_node = Circle(radius=0.5, color=HIDDEN_COLOR, fill_opacity=0.7)
        sum_node.move_to([0, 0, 0])
        sum_text = MathTex(r"\Sigma", font_size=32).move_to(sum_node.get_center())
        perceptron.add(sum_node, sum_text)
        
        # 激活函数节点
        act_node = Circle(radius=0.5, color=ACTIVATION_COLOR, fill_opacity=0.7)
        act_node.move_to([2, 0, 0])
        act_text = MathTex(r"f", font_size=32).move_to(act_node.get_center())
        perceptron.add(act_node, act_text)
        
        # 输出节点
        output_node = Circle(radius=0.3, color=OUTPUT_COLOR, fill_opacity=0.7)
        output_node.move_to([4, 0, 0])
        output_text = MathTex(r"y", font_size=24).move_to(output_node.get_center())
        perceptron.add(output_node, output_text)
        
        # 连接线和权重
        weights = ["w_1", "w_2", "w_3"]
        for i, (inp, w) in enumerate(zip(inputs, weights)):
            line = Arrow(
                inp[0].get_right(), sum_node.get_left() + UP*(1-i)*0.3,
                buff=0.1, stroke_width=2, color=WHITE
            )
            w_label = MathTex(w, font_size=20, color=POSITIVE_WEIGHT)
            w_label.move_to(line.get_center() + UP*0.25)
            perceptron.add(line, w_label)
        
        # 偏置
        bias_arrow = Arrow(
            sum_node.get_top() + UP*0.5, sum_node.get_top(),
            buff=0.1, stroke_width=2, color=GRAY
        )
        bias_label = MathTex("b", font_size=20, color=GRAY)
        bias_label.next_to(bias_arrow, UP, buff=0.1)
        perceptron.add(bias_arrow, bias_label)
        
        # 求和到激活函数
        arr1 = Arrow(sum_node.get_right(), act_node.get_left(), buff=0.1, stroke_width=2)
        perceptron.add(arr1)
        
        # 激活函数到输出
        arr2 = Arrow(act_node.get_right(), output_node.get_left(), buff=0.1, stroke_width=2)
        perceptron.add(arr2)
        
        return perceptron
    
    def create_table(self, data):
        """创建简单表格"""
        table = VGroup()
        rows = len(data)
        cols = len(data[0])
        
        cell_width = 0.8
        cell_height = 0.5
        
        for i, row in enumerate(data):
            for j, cell in enumerate(row):
                rect = Rectangle(
                    width=cell_width, height=cell_height,
                    stroke_width=1, color=WHITE
                )
                rect.move_to([j * cell_width, -i * cell_height, 0])
                
                text = Text(cell, font_size=18)
                text.move_to(rect.get_center())
                
                if i == 0:
                    rect.set_fill(BLUE_E, opacity=0.3)
                
                table.add(rect, text)
        
        table.move_to(ORIGIN)
        return table
    
    def activation_functions_scene(self):
        """场景4: 激活函数"""
        title = Text("激活函数", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 为什么需要激活函数
        why = Text("为什么需要激活函数？", font_size=32, color=YELLOW)
        why.next_to(title, DOWN, buff=0.3)
        self.play(Write(why), run_time=0.5)
        
        reason = Text("引入非线性，否则多层网络等同于单层", font_size=28, color=WHITE)
        reason.next_to(why, DOWN, buff=0.2)
        self.play(Write(reason), run_time=0.8)
        self.wait(1)
        
        self.play(FadeOut(why), FadeOut(reason))
        
        # 创建坐标轴
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-1.5, 1.5, 0.5],
            x_length=5,
            y_length=3,
            axis_config={"include_tip": True, "include_numbers": True},
        )
        axes.shift(DOWN * 0.5)
        
        self.play(Create(axes), run_time=0.8)
        
        # 激活函数列表
        functions = [
            ("Step Function", lambda x: 1 if x >= 0 else 0, RED),
            ("Sigmoid", lambda x: 1 / (1 + np.exp(-x)), BLUE),
            ("Tanh", lambda x: np.tanh(x), GREEN),
            ("ReLU", lambda x: max(0, x), ORANGE),
        ]
        
        formulas = [
            r"\text{Step}(x) = \begin{cases} 1 & x \geq 0 \\ 0 & x < 0 \end{cases}",
            r"\sigma(x) = \frac{1}{1 + e^{-x}}",
            r"\tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}",
            r"\text{ReLU}(x) = \max(0, x)",
        ]
        
        current_graph = None
        current_label = None
        current_formula = None
        
        for i, ((name, func, color), formula_tex) in enumerate(zip(functions, formulas)):
            # 名称
            label = Text(name, font_size=32, color=color)
            label.move_to([-4, 2, 0])
            
            # 公式
            formula = MathTex(formula_tex, font_size=28)
            formula.move_to([4, 1.5, 0])
            
            # 图像
            graph = axes.plot(
                lambda x, f=func: f(x),
                x_range=[-4.5, 4.5],
                color=color,
                use_smoothing=True
            )
            
            if current_graph is None:
                self.play(
                    Create(graph),
                    Write(label),
                    Write(formula),
                    run_time=1
                )
            else:
                self.play(
                    ReplacementTransform(current_graph, graph),
                    ReplacementTransform(current_label, label),
                    ReplacementTransform(current_formula, formula),
                    run_time=0.8
                )
            
            current_graph = graph
            current_label = label
            current_formula = formula
            
            self.wait(1)
        
        self.wait(1)
        self.clear_scene()
    
    def multilayer_network_scene(self):
        """场景5: 多层神经网络"""
        title = Text("多层神经网络结构", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 创建网络
        layer_sizes = [4, 6, 6, 3]
        layers, connections, all_neurons = self.create_neural_network(layer_sizes)
        
        network = VGroup(connections, layers)
        network.shift(DOWN * 0.3)
        
        # 先显示连接线，再显示神经元
        self.play(Create(connections), run_time=1)
        self.play(FadeIn(layers), run_time=0.8)
        
        # 层标签
        layer_names = ["输入层\nInput", "隐藏层\nHidden", "隐藏层\nHidden", "输出层\nOutput"]
        labels = VGroup()
        
        for i, (name, layer) in enumerate(zip(layer_names, layers)):
            label = Text(name, font_size=20, color=WHITE)
            label.next_to(layer, DOWN, buff=0.4)
            labels.add(label)
        
        self.play(FadeIn(labels), run_time=0.5)
        self.wait(1)
        
        # 数据流动动画
        flow_text = Text("信息前向传播", font_size=32, color=YELLOW)
        flow_text.to_edge(DOWN, buff=0.5)
        self.play(Write(flow_text), run_time=0.5)
        
        # 逐层激活动画
        for layer_idx, layer in enumerate(layers):
            anims = []
            for neuron in layer:
                anims.append(neuron.animate.set_fill(ACTIVATION_COLOR, opacity=0.9))
            self.play(*anims, run_time=0.5)
            self.wait(0.2)
            
            # 恢复颜色
            if layer_idx < len(layers) - 1:
                color = INPUT_COLOR if layer_idx == 0 else HIDDEN_COLOR
                anims = []
                for neuron in layer:
                    anims.append(neuron.animate.set_fill(color, opacity=0.8))
                self.play(*anims, run_time=0.3)
        
        self.wait(1.5)
        self.clear_scene()
    
    def forward_propagation_scene(self):
        """场景6: 前向传播"""
        title = Text("前向传播详解", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 简化网络
        layer_sizes = [3, 4, 2]
        layers, connections, all_neurons = self.create_neural_network(layer_sizes, x_spacing=3.5)
        
        network = VGroup(connections, layers)
        network.scale(0.8).shift(LEFT * 2 + DOWN * 0.5)
        
        self.play(FadeIn(network), run_time=0.8)
        
        # 矩阵公式
        formulas = VGroup(
            MathTex(r"a^{(1)} = f(W^{(1)}x + b^{(1)})", font_size=28),
            MathTex(r"a^{(2)} = f(W^{(2)}a^{(1)} + b^{(2)})", font_size=28),
            MathTex(r"y = f(W^{(3)}a^{(2)} + b^{(3)})", font_size=28),
        )
        formulas.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        formulas.move_to([3.5, 0, 0])
        
        for formula in formulas:
            self.play(Write(formula), run_time=0.6)
        
        self.wait(1)
        
        # 具体数值示例
        self.play(FadeOut(formulas))
        
        example_title = Text("数值计算示例", font_size=28, color=YELLOW)
        example_title.move_to([3.5, 2, 0])
        self.play(Write(example_title), run_time=0.5)
        
        # 输入向量
        input_vec = MathTex(r"x = \begin{bmatrix} 0.5 \\ 0.3 \\ 0.8 \end{bmatrix}", font_size=24)
        input_vec.move_to([3.5, 0.5, 0])
        self.play(Write(input_vec), run_time=0.5)
        
        # 高亮输入层
        for neuron in all_neurons[0]:
            self.play(neuron.animate.set_fill(ACTIVATION_COLOR), run_time=0.2)
        
        # 计算过程
        calc = MathTex(r"z^{(1)} = W^{(1)}x + b^{(1)}", font_size=24)
        calc.next_to(input_vec, DOWN, buff=0.3)
        self.play(Write(calc), run_time=0.5)
        
        # 激活
        activation = MathTex(r"a^{(1)} = \sigma(z^{(1)})", font_size=24)
        activation.next_to(calc, DOWN, buff=0.2)
        self.play(Write(activation), run_time=0.5)
        
        # 高亮隐藏层
        for neuron in all_neurons[1]:
            self.play(neuron.animate.set_fill(ACTIVATION_COLOR), run_time=0.15)
        
        # 输出
        output = MathTex(r"y = \sigma(W^{(2)}a^{(1)} + b^{(2)})", font_size=24)
        output.next_to(activation, DOWN, buff=0.3)
        self.play(Write(output), run_time=0.5)
        
        # 高亮输出层
        for neuron in all_neurons[2]:
            self.play(neuron.animate.set_fill(ACTIVATION_COLOR), run_time=0.2)
        
        self.wait(1.5)
        self.clear_scene()
    
    def loss_function_scene(self):
        """场景7: 损失函数"""
        title = Text("损失函数", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 什么是损失函数
        what_is = Text("损失函数衡量预测值与真实值的差距", font_size=32, color=WHITE)
        what_is.next_to(title, DOWN, buff=0.5)
        self.play(Write(what_is), run_time=0.8)
        self.wait(0.5)
        
        self.play(FadeOut(what_is))
        
        # MSE
        mse_title = Text("均方误差 (MSE)", font_size=32, color=BLUE)
        mse_title.move_to([-3.5, 1.5, 0])
        
        mse_formula = MathTex(r"L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2", font_size=32)
        mse_formula.next_to(mse_title, DOWN, buff=0.3)
        
        self.play(Write(mse_title), run_time=0.5)
        self.play(Write(mse_formula), run_time=0.8)
        
        # Cross-Entropy
        ce_title = Text("交叉熵 (Cross-Entropy)", font_size=32, color=GREEN)
        ce_title.move_to([3, 1.5, 0])
        
        ce_formula = MathTex(r"L = -\sum_{i=1}^{n}y_i\log(\hat{y}_i)", font_size=32)
        ce_formula.next_to(ce_title, DOWN, buff=0.3)
        
        self.play(Write(ce_title), run_time=0.5)
        self.play(Write(ce_formula), run_time=0.8)
        
        self.wait(1)
        
        # 损失曲面可视化 (简化的2D)
        self.play(
            FadeOut(mse_title), FadeOut(mse_formula),
            FadeOut(ce_title), FadeOut(ce_formula)
        )
        
        surface_title = Text("损失曲面", font_size=32, color=YELLOW)
        surface_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(surface_title), run_time=0.5)
        
        # 创建简单的损失曲线
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=6,
            y_length=3,
            axis_config={"include_tip": True},
        )
        axes.shift(DOWN * 0.8)
        
        x_label = axes.get_x_axis_label("w", direction=RIGHT)
        y_label = axes.get_y_axis_label("Loss", direction=UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        
        # 损失曲线
        loss_curve = axes.plot(lambda x: x**2 + 0.5, x_range=[-2.5, 2.5], color=RED)
        self.play(Create(loss_curve), run_time=1)
        
        # 最优点
        optimal_point = Dot(axes.c2p(0, 0.5), color=GREEN, radius=0.1)
        optimal_label = Text("最优解", font_size=20, color=GREEN)
        optimal_label.next_to(optimal_point, DOWN, buff=0.2)
        
        self.play(FadeIn(optimal_point), Write(optimal_label), run_time=0.5)
        
        goal_text = Text("目标: 最小化损失函数", font_size=28, color=WHITE)
        goal_text.to_edge(DOWN, buff=0.5)
        self.play(Write(goal_text), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def backpropagation_scene(self):
        """场景8: 反向传播"""
        title = Text("反向传播算法", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 链式法则
        chain_title = Text("核心: 链式法则", font_size=32, color=YELLOW)
        chain_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(chain_title), run_time=0.5)
        
        chain_formula = MathTex(
            r"\frac{\partial L}{\partial w} = \frac{\partial L}{\partial y} \cdot \frac{\partial y}{\partial z} \cdot \frac{\partial z}{\partial w}",
            font_size=36
        )
        chain_formula.next_to(chain_title, DOWN, buff=0.3)
        self.play(Write(chain_formula), run_time=1)
        
        self.wait(1)
        self.play(FadeOut(chain_title), FadeOut(chain_formula))
        
        # 创建简单网络
        layer_sizes = [2, 3, 2]
        layers, connections, all_neurons = self.create_neural_network(layer_sizes, x_spacing=3)
        
        network = VGroup(connections, layers)
        network.scale(0.7).shift(DOWN * 0.3)
        
        self.play(FadeIn(network), run_time=0.8)
        
        # 前向传播
        forward_text = Text("前向传播 →", font_size=24, color=BLUE)
        forward_text.to_edge(LEFT, buff=1).shift(UP * 2)
        self.play(Write(forward_text), run_time=0.3)
        
        # 前向传播动画
        forward_arrow = Arrow(LEFT * 4, RIGHT * 4, color=BLUE, stroke_width=3)
        forward_arrow.shift(DOWN * 2.5)
        self.play(GrowArrow(forward_arrow), run_time=0.8)
        
        self.wait(0.5)
        
        # 反向传播
        backward_text = Text("← 反向传播 (梯度)", font_size=24, color=GRADIENT_COLOR)
        backward_text.to_edge(RIGHT, buff=1).shift(UP * 2)
        self.play(Write(backward_text), run_time=0.3)
        
        # 反向传播动画
        backward_arrow = Arrow(RIGHT * 4, LEFT * 4, color=GRADIENT_COLOR, stroke_width=3)
        backward_arrow.shift(DOWN * 3)
        self.play(GrowArrow(backward_arrow), run_time=0.8)
        
        # 梯度流动可视化
        gradient_dots = []
        for layer in reversed(all_neurons):
            for neuron in layer:
                dot = Dot(neuron.get_center(), color=GRADIENT_COLOR, radius=0.15)
                gradient_dots.append(dot)
        
        # 逐层显示梯度
        layer_idx = 0
        for i, layer in enumerate(reversed(all_neurons)):
            anims = []
            for j, neuron in enumerate(layer):
                dot = gradient_dots[layer_idx + j]
                anims.append(FadeIn(dot, scale=1.5))
            self.play(*anims, run_time=0.4)
            layer_idx += len(layer)
        
        # 权重更新公式
        update_formula = MathTex(r"w_{new} = w_{old} - \alpha \cdot \frac{\partial L}{\partial w}", font_size=32)
        update_formula.to_edge(DOWN, buff=0.3)
        self.play(Write(update_formula), run_time=0.8)
        
        self.wait(1.5)
        self.clear_scene()
    
    def gradient_descent_scene(self):
        """场景9: 梯度下降"""
        title = Text("梯度下降优化", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 直觉类比
        analogy = Text("类比: 在山上找最低点", font_size=32, color=YELLOW)
        analogy.next_to(title, DOWN, buff=0.3)
        self.play(Write(analogy), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(analogy))
        
        # 创建损失曲面
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=4,
            axis_config={"include_tip": True, "include_numbers": True},
        )
        axes.shift(DOWN * 0.5)
        
        x_label = axes.get_x_axis_label("w", direction=RIGHT)
        y_label = axes.get_y_axis_label("Loss", direction=UP)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        
        # 损失曲线
        loss_curve = axes.plot(lambda x: x**2 + 0.3, x_range=[-2.8, 2.8], color=RED)
        self.play(Create(loss_curve), run_time=0.8)
        
        # 梯度下降动画
        start_x = 2.5
        current_point = Dot(axes.c2p(start_x, start_x**2 + 0.3), color=BLUE, radius=0.12)
        self.play(FadeIn(current_point), run_time=0.3)
        
        # 更新公式
        formula = MathTex(r"w = w - \alpha \cdot \nabla L", font_size=28, color=WHITE)
        formula.to_corner(UR, buff=0.5)
        self.play(Write(formula), run_time=0.5)
        
        # 学习率
        lr_text = MathTex(r"\alpha = 0.3", font_size=24, color=YELLOW)
        lr_text.next_to(formula, DOWN, buff=0.2)
        self.play(Write(lr_text), run_time=0.3)
        
        # 迭代下降
        learning_rate = 0.3
        x = start_x
        
        for i in range(8):
            gradient = 2 * x  # d/dx(x^2) = 2x
            new_x = x - learning_rate * gradient
            new_x = max(-2.8, min(2.8, new_x))  # 边界限制
            
            # 绘制切线
            tangent_line = axes.plot(
                lambda t, x0=x, g=gradient: (t - x0) * g + (x0**2 + 0.3),
                x_range=[x - 0.8, x + 0.8],
                color=GREEN,
                stroke_width=2
            )
            self.play(Create(tangent_line), run_time=0.3)
            
            # 移动点
            new_point = axes.c2p(new_x, new_x**2 + 0.3)
            self.play(
                current_point.animate.move_to(new_point),
                FadeOut(tangent_line),
                run_time=0.4
            )
            
            x = new_x
            
            if abs(x) < 0.1:
                break
        
        # 收敛
        converge_text = Text("收敛到最优解!", font_size=28, color=GREEN)
        converge_text.to_edge(DOWN, buff=0.5)
        self.play(Write(converge_text), run_time=0.5)
        
        self.wait(1)
        
        # 学习率对比
        self.play(FadeOut(converge_text), FadeOut(current_point))
        
        compare_title = Text("学习率的影响", font_size=28, color=YELLOW)
        compare_title.to_edge(DOWN, buff=2)
        self.play(Write(compare_title), run_time=0.5)
        
        # 三种学习率
        lr_labels = ["α=0.1 (太小)", "α=0.5 (合适)", "α=1.5 (太大)"]
        colors = [BLUE, GREEN, RED]
        start_positions = [2.5, 2.5, 2.5]
        lrs = [0.1, 0.5, 1.5]
        
        dots = []
        for i, (lr, color, label) in enumerate(zip(lrs, colors, lr_labels)):
            dot = Dot(axes.c2p(start_positions[i], start_positions[i]**2 + 0.3), color=color, radius=0.1)
            dots.append(dot)
            label_text = Text(label, font_size=18, color=color)
            label_text.move_to(axes.c2p(-2, 4 - i * 0.5))
            self.play(FadeIn(dot), Write(label_text), run_time=0.3)
        
        # 同时更新三个点
        xs = list(start_positions)
        for step in range(10):
            anims = []
            for i, (dot, lr) in enumerate(zip(dots, lrs)):
                gradient = 2 * xs[i]
                xs[i] = xs[i] - lr * gradient
                xs[i] = max(-2.8, min(2.8, xs[i]))
                new_pos = axes.c2p(xs[i], xs[i]**2 + 0.3)
                anims.append(dot.animate.move_to(new_pos))
            self.play(*anims, run_time=0.3)
        
        self.wait(1.5)
        self.clear_scene()
    
    def mnist_example_scene(self):
        """场景10: MNIST 示例"""
        title = Text("实际案例: 手写数字识别", font_size=44, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # MNIST 介绍
        mnist_intro = Text("MNIST 数据集: 28×28 灰度手写数字图像", font_size=28, color=WHITE)
        mnist_intro.next_to(title, DOWN, buff=0.3)
        self.play(Write(mnist_intro), run_time=0.6)
        
        # 创建模拟的数字图像
        digit_grid = self.create_digit_5()
        digit_grid.scale(0.8).shift(LEFT * 4)
        
        self.play(FadeIn(digit_grid), run_time=0.8)
        
        # 网络结构
        structure_text = VGroup(
            Text("网络结构:", font_size=24, color=YELLOW),
            Text("• 输入层: 784 (28×28)", font_size=20),
            Text("• 隐藏层: 128 → 64", font_size=20),
            Text("• 输出层: 10 (0-9)", font_size=20),
        )
        structure_text.arrange(DOWN, aligned_edge=LEFT, buff=0.15)
        structure_text.move_to([0, 0, 0])
        
        for text in structure_text:
            self.play(Write(text), run_time=0.3)
        
        # 简化网络图
        mini_network = VGroup()
        
        # 输入
        input_rect = Rectangle(width=0.8, height=2, color=INPUT_COLOR, fill_opacity=0.5)
        input_rect.move_to([2.5, 0, 0])
        input_label = Text("784", font_size=16).next_to(input_rect, DOWN, buff=0.1)
        
        # 隐藏层
        hidden1 = Rectangle(width=0.5, height=1.5, color=HIDDEN_COLOR, fill_opacity=0.5)
        hidden1.move_to([3.5, 0, 0])
        h1_label = Text("128", font_size=16).next_to(hidden1, DOWN, buff=0.1)
        
        hidden2 = Rectangle(width=0.4, height=1, color=HIDDEN_COLOR, fill_opacity=0.5)
        hidden2.move_to([4.3, 0, 0])
        h2_label = Text("64", font_size=16).next_to(hidden2, DOWN, buff=0.1)
        
        # 输出
        output_rect = Rectangle(width=0.3, height=0.8, color=OUTPUT_COLOR, fill_opacity=0.5)
        output_rect.move_to([5, 0, 0])
        output_label = Text("10", font_size=16).next_to(output_rect, DOWN, buff=0.1)
        
        # 连接
        arr1 = Arrow(input_rect.get_right(), hidden1.get_left(), buff=0.1, stroke_width=2)
        arr2 = Arrow(hidden1.get_right(), hidden2.get_left(), buff=0.1, stroke_width=2)
        arr3 = Arrow(hidden2.get_right(), output_rect.get_left(), buff=0.1, stroke_width=2)
        
        mini_network.add(
            input_rect, input_label,
            hidden1, h1_label,
            hidden2, h2_label,
            output_rect, output_label,
            arr1, arr2, arr3
        )
        
        self.play(FadeIn(mini_network), run_time=0.8)
        
        # 输出概率
        output_probs = VGroup()
        probs = [0.01, 0.02, 0.01, 0.03, 0.05, 0.82, 0.02, 0.01, 0.02, 0.01]
        
        for i, prob in enumerate(probs):
            bar = Rectangle(
                width=prob * 2, height=0.2,
                color=GREEN if i == 5 else GRAY,
                fill_opacity=0.7
            )
            bar.move_to([6 + prob, 1.8 - i * 0.4, 0])
            label = Text(f"{i}: {prob:.0%}", font_size=12)
            label.next_to(bar, RIGHT, buff=0.1)
            output_probs.add(bar, label)
        
        self.play(FadeIn(output_probs), run_time=0.8)
        
        # 预测结果
        result = Text("预测: 5 ✓", font_size=32, color=GREEN)
        result.to_edge(DOWN, buff=0.5)
        self.play(Write(result), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def create_digit_5(self):
        """创建数字5的像素网格"""
        grid = VGroup()
        
        # 简化的5的像素模式
        pattern = [
            [0,1,1,1,1,1,0],
            [0,1,0,0,0,0,0],
            [0,1,1,1,1,0,0],
            [0,0,0,0,0,1,0],
            [0,0,0,0,0,1,0],
            [0,1,0,0,0,1,0],
            [0,0,1,1,1,0,0],
        ]
        
        cell_size = 0.25
        for i, row in enumerate(pattern):
            for j, val in enumerate(row):
                cell = Square(side_length=cell_size)
                cell.move_to([j * cell_size, -i * cell_size, 0])
                if val == 1:
                    cell.set_fill(WHITE, opacity=0.9)
                else:
                    cell.set_fill(BLACK, opacity=0.3)
                cell.set_stroke(GRAY, width=0.5)
                grid.add(cell)
        
        grid.move_to(ORIGIN)
        return grid
    
    def regularization_scene(self):
        """场景11: 过拟合与正则化"""
        title = Text("过拟合与正则化", font_size=48, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 什么是过拟合
        overfit_text = Text("过拟合: 模型在训练数据上表现很好，但在新数据上表现差", font_size=24, color=WHITE)
        overfit_text.next_to(title, DOWN, buff=0.3)
        self.play(Write(overfit_text), run_time=0.8)
        
        # 创建对比图
        # 欠拟合
        ax1 = Axes(
            x_range=[0, 5, 1], y_range=[0, 5, 1],
            x_length=2.5, y_length=2.5,
            axis_config={"include_tip": False}
        )
        ax1.shift(LEFT * 4.5 + DOWN * 0.5)
        
        # 数据点
        points1 = VGroup()
        data = [(0.5, 1), (1, 1.5), (1.5, 2.5), (2, 2), (2.5, 3), (3, 3.5), (3.5, 3), (4, 4)]
        for x, y in data:
            dot = Dot(ax1.c2p(x, y), color=BLUE, radius=0.06)
            points1.add(dot)
        
        # 欠拟合线
        underfit = ax1.plot(lambda x: 2, x_range=[0.3, 4.2], color=RED)
        underfit_label = Text("欠拟合", font_size=18, color=RED)
        underfit_label.next_to(ax1, DOWN, buff=0.2)
        
        # 合适拟合
        ax2 = ax1.copy().shift(RIGHT * 4.5)
        points2 = points1.copy().shift(RIGHT * 4.5)
        goodfit = ax2.plot(lambda x: 0.8 * x + 0.5, x_range=[0.3, 4.2], color=GREEN)
        goodfit_label = Text("合适拟合", font_size=18, color=GREEN)
        goodfit_label.next_to(ax2, DOWN, buff=0.2)
        
        # 过拟合
        ax3 = ax1.copy().shift(RIGHT * 9)
        points3 = points1.copy().shift(RIGHT * 9)
        overfit = ax3.plot(
            lambda x: 0.5 * np.sin(3*x) * x + 1.5,
            x_range=[0.3, 4.2], color=ORANGE
        )
        overfit_label = Text("过拟合", font_size=18, color=ORANGE)
        overfit_label.next_to(ax3, DOWN, buff=0.2)
        
        self.play(
            Create(ax1), FadeIn(points1),
            Create(ax2), FadeIn(points2),
            Create(ax3), FadeIn(points3),
            run_time=0.8
        )
        
        self.play(
            Create(underfit), Write(underfit_label),
            Create(goodfit), Write(goodfit_label),
            Create(overfit), Write(overfit_label),
            run_time=1
        )
        
        self.wait(1)
        
        # 正则化方法
        self.play(
            FadeOut(ax1), FadeOut(points1), FadeOut(underfit), FadeOut(underfit_label),
            FadeOut(ax2), FadeOut(points2), FadeOut(goodfit), FadeOut(goodfit_label),
            FadeOut(ax3), FadeOut(points3), FadeOut(overfit), FadeOut(overfit_label),
            FadeOut(overfit_text)
        )
        
        reg_title = Text("正则化方法", font_size=36, color=YELLOW)
        reg_title.next_to(title, DOWN, buff=0.3)
        self.play(Write(reg_title), run_time=0.5)
        
        methods = VGroup(
            VGroup(
                Text("L2 正则化", font_size=24, color=BLUE),
                MathTex(r"L_{total} = L + \lambda\sum w^2", font_size=24)
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Dropout", font_size=24, color=GREEN),
                Text("随机丢弃神经元", font_size=20)
            ).arrange(DOWN, buff=0.1),
            VGroup(
                Text("Early Stopping", font_size=24, color=ORANGE),
                Text("验证集损失不再下降时停止", font_size=20)
            ).arrange(DOWN, buff=0.1),
        )
        methods.arrange(RIGHT, buff=1.5)
        methods.shift(DOWN * 0.5)
        
        for method in methods:
            self.play(FadeIn(method), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def summary_scene(self):
        """场景12: 总结"""
        title = Text("总结", font_size=56, color=WHITE)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.8)
        
        # 核心概念
        concepts = VGroup(
            Text("神经网络核心概念", font_size=36, color=YELLOW),
            Text("1. 神经元: 输入 → 加权求和 → 激活函数 → 输出", font_size=24),
            Text("2. 前向传播: 数据从输入层流向输出层", font_size=24),
            Text("3. 损失函数: 衡量预测与真实的差距", font_size=24),
            Text("4. 反向传播: 计算梯度，传播误差", font_size=24),
            Text("5. 梯度下降: 沿梯度方向更新参数", font_size=24),
        )
        concepts.arrange(DOWN, aligned_edge=LEFT, buff=0.25)
        concepts.shift(UP * 0.3)
        
        for concept in concepts:
            self.play(Write(concept), run_time=0.5)
        
        self.wait(1.5)
        
        # 发展
        evolution = Text("神经网络的发展: CNN → RNN → Transformer → ...", font_size=28, color=WHITE)
        evolution.next_to(concepts, DOWN, buff=0.5)
        self.play(Write(evolution), run_time=0.8)
        
        self.wait(1)
        
        # 感谢
        self.play(*[FadeOut(m) for m in self.mobjects])
        
        thanks = Text("感谢观看！", font_size=56, color=WHITE)
        self.play(FadeIn(thanks, scale=1.2), run_time=1)
        self.wait(1.5)
        
        self.play(FadeOut(thanks))


# 单独场景类，方便测试
class IntroScene(Scene):
    """单独的开场场景"""
    def construct(self):
        tutorial = NeuralNetworkTutorial()
        tutorial.intro_scene = lambda: None
        self.intro_scene()


class PerceptronScene(Scene):
    """单独的感知机场景"""
    def construct(self):
        tutorial = NeuralNetworkTutorial()
        tutorial.perceptron_scene()


class ActivationScene(Scene):
    """单独的激活函数场景"""
    def construct(self):
        tutorial = NeuralNetworkTutorial()
        tutorial.activation_functions_scene()


class BackpropScene(Scene):
    """单独的反向传播场景"""
    def construct(self):
        tutorial = NeuralNetworkTutorial()
        tutorial.backpropagation_scene()
