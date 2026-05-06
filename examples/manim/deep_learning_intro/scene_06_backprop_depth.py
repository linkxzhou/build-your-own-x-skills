"""
场景6: 反向传播与深度的价值
展示梯度如何计算，以及深度网络的意义

运行命令:
    manim -pql scene_06_backprop_depth.py BackpropDepthScene
    manim -pqh scene_06_backprop_depth.py BackpropDepthScene
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
GRADIENT_COLOR = "#1ABC9C"     # 梯度颜色


class BackpropDepthScene(Scene):
    """场景6: 反向传播与深度的价值"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 反向传播介绍
        self.show_backpropagation()
        
        # 2. 梯度问题
        self.show_gradient_problems()
        
        # 3. 深度的价值
        self.show_depth_value()
        
        self.clear_scene()
    
    def show_backpropagation(self):
        """反向传播介绍"""
        # 标题
        title = Text("反向传播 — '闻着味儿'找错误来源", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 类比
        analogy = Text(
            "从出口处的错误，一层层倒推每个岔路口的责任",
            font_size=24, color=TEXT_COLOR
        )
        analogy.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(analogy), run_time=0.8)
        
        # 创建简化网络
        network = self.create_simple_network()
        network.scale(0.9)
        network.shift(DOWN * 0.3)
        
        self.play(FadeIn(network), run_time=0.8)
        
        # 前向传播
        forward_label = Text("前向传播 →", font_size=22, color=PRIMARY_COLOR)
        forward_label.next_to(network, UP, buff=0.3).shift(LEFT * 2)
        
        self.play(Write(forward_label), run_time=0.3)
        
        # 前向传播动画
        layers = network[0]
        for i, layer in enumerate(layers):
            self.play(
                layer.animate.set_fill(PRIMARY_COLOR, opacity=0.6),
                run_time=0.3
            )
            if i < len(layers) - 1:
                self.play(
                    layer.animate.set_fill(PRIMARY_COLOR, opacity=0.2),
                    run_time=0.1
                )
        
        # 计算损失
        loss_label = Text("计算损失", font_size=20, color=ERROR_COLOR)
        loss_label.next_to(layers[-1], RIGHT, buff=0.5)
        
        self.play(Write(loss_label), run_time=0.3)
        self.wait(0.3)
        
        # 反向传播
        backward_label = Text("← 反向传播 (梯度)", font_size=22, color=GRADIENT_COLOR)
        backward_label.next_to(network, DOWN, buff=0.3).shift(RIGHT * 2)
        
        self.play(Write(backward_label), FadeOut(loss_label), run_time=0.3)
        
        # 反向传播动画
        for i, layer in enumerate(reversed(layers)):
            self.play(
                layer.animate.set_fill(GRADIENT_COLOR, opacity=0.6),
                run_time=0.3
            )
            if i < len(layers) - 1:
                self.play(
                    layer.animate.set_fill(GRADIENT_COLOR, opacity=0.2),
                    run_time=0.1
                )
        
        self.wait(0.5)
        
        # 链式法则
        chain_title = Text("核心: 链式法则", font_size=26, color=ACCENT_COLOR)
        chain_title.to_edge(DOWN, buff=1.8)
        
        chain_formula = MathTex(
            r"\frac{\partial L}{\partial w} = ",
            r"\frac{\partial L}{\partial y}",
            r" \cdot ",
            r"\frac{\partial y}{\partial z}",
            r" \cdot ",
            r"\frac{\partial z}{\partial w}",
            font_size=28
        )
        chain_formula[1].set_color(ERROR_COLOR)
        chain_formula[3].set_color(NEURAL_COLOR)
        chain_formula[5].set_color(PRIMARY_COLOR)
        
        chain_formula.next_to(chain_title, DOWN, buff=0.2)
        
        self.play(Write(chain_title), run_time=0.3)
        self.play(Write(chain_formula), run_time=1)
        
        # 说明
        explanation = Text(
            "让海量参数的高效调整成为可能！",
            font_size=22, color=SECONDARY_COLOR
        )
        explanation.next_to(chain_formula, DOWN, buff=0.3)
        
        self.play(Write(explanation), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_gradient_problems(self):
        """梯度问题"""
        # 标题
        title = Text("致命问题: 梯度消失/爆炸", font_size=36, color=ERROR_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题描述
        problem = VGroup(
            Text("梯度经过很多层后:", font_size=24, color=TEXT_COLOR),
            VGroup(
                Text("• 变得", font_size=22, color=TEXT_COLOR),
                Text("极其微弱", font_size=22, color=PRIMARY_COLOR),
                Text("(消失)", font_size=22, color=SUBTEXT_COLOR),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("• 变得", font_size=22, color=TEXT_COLOR),
                Text("极其巨大", font_size=22, color=ERROR_COLOR),
                Text("(爆炸)", font_size=22, color=SUBTEXT_COLOR),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        problem.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(problem), run_time=1)
        
        # 可视化: 梯度消失
        vanish_demo = self.create_gradient_vanish_demo()
        vanish_demo.shift(DOWN * 0.8)
        
        self.play(FadeIn(vanish_demo), run_time=0.8)
        
        # 动画: 梯度逐层衰减
        gradient_bars = vanish_demo[1]
        
        for i, bar in enumerate(gradient_bars):
            target_height = 1.5 * (0.5 ** i)
            target_bar = Rectangle(
                width=0.4, height=max(0.1, target_height),
                color=GRADIENT_COLOR, fill_opacity=0.8
            )
            target_bar.move_to(bar.get_bottom(), aligned_edge=DOWN)
            
            self.play(
                Transform(bar, target_bar),
                run_time=0.3
            )
        
        # 结果说明
        result = Text("前面层几乎学不到东西!", font_size=22, color=ERROR_COLOR)
        result.next_to(vanish_demo, DOWN, buff=0.3)
        
        self.play(Write(result), run_time=0.5)
        
        self.wait(1)
        
        # 解决思路
        self.play(FadeOut(vanish_demo), FadeOut(result))
        
        solution = VGroup(
            Text("解决思路:", font_size=28, color=ACCENT_COLOR),
            Text("与其只改进优化算法,", font_size=24, color=TEXT_COLOR),
            Text("不如把模型本身设计得更容易被优化", font_size=24, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.3)
        solution.next_to(problem, DOWN, buff=0.6)
        
        self.play(Write(solution), run_time=1)
        
        # 例子
        examples = VGroup(
            Text("→ ResNet (跳跃连接)", font_size=22, color=PRIMARY_COLOR),
            Text("→ Transformer (注意力机制)", font_size=22, color=NEURAL_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        examples.next_to(solution, DOWN, buff=0.4)
        
        self.play(Write(examples), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_depth_value(self):
        """深度的价值"""
        # 标题
        title = Text("'深度'的价值 — 多层协作", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 问题设置
        question = Text(
            "为什么模型要'深'(有很多层)?",
            font_size=26, color=TEXT_COLOR
        )
        question.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(question), run_time=0.6)
        
        # 创建分类演示
        # 初始状态: 两类点混在一起
        np.random.seed(42)
        
        # 生成两类数据点
        class1_points = []
        class2_points = []
        
        for _ in range(15):
            # 类1: 圆形分布
            angle = np.random.uniform(0, 2 * PI)
            r = np.random.uniform(0.3, 0.8)
            class1_points.append([r * np.cos(angle), r * np.sin(angle)])
        
        for _ in range(15):
            # 类2: 外圈分布
            angle = np.random.uniform(0, 2 * PI)
            r = np.random.uniform(1.0, 1.5)
            class2_points.append([r * np.cos(angle), r * np.sin(angle)])
        
        # 创建点
        dots1 = VGroup()
        dots2 = VGroup()
        
        for p in class1_points:
            dot = Dot(point=[p[0], p[1], 0], color=PRIMARY_COLOR, radius=0.08)
            dots1.add(dot)
        
        for p in class2_points:
            dot = Dot(point=[p[0], p[1], 0], color=ERROR_COLOR, radius=0.08)
            dots2.add(dot)
        
        all_dots = VGroup(dots1, dots2)
        all_dots.shift(DOWN * 0.8 + LEFT * 3)
        
        # 坐标框
        frame = Rectangle(width=4, height=4, color=SUBTEXT_COLOR, stroke_width=1)
        frame.move_to(all_dots.get_center())
        
        # 标签
        stage1_label = Text("初始: 两类混在一起", font_size=18, color=SUBTEXT_COLOR)
        stage1_label.next_to(frame, DOWN, buff=0.2)
        
        self.play(
            FadeIn(frame),
            FadeIn(all_dots),
            Write(stage1_label),
            run_time=0.8
        )
        
        # 网络层示意
        layers_demo = VGroup()
        layer_labels = ["层1", "层2", "层3", "层4"]
        
        for i, label in enumerate(layer_labels):
            layer_box = RoundedRectangle(
                width=0.8, height=0.6,
                corner_radius=0.1,
                color=NEURAL_COLOR,
                fill_opacity=0.3
            )
            layer_text = Text(label, font_size=14, color=NEURAL_COLOR)
            layer_text.move_to(layer_box.get_center())
            layers_demo.add(VGroup(layer_box, layer_text))
        
        layers_demo.arrange(RIGHT, buff=0.3)
        layers_demo.move_to(RIGHT * 3 + UP * 0.5)
        
        self.play(FadeIn(layers_demo), run_time=0.5)
        
        # 变换过程
        process_text = Text(
            "每层对数据进行微小'扭曲'",
            font_size=20, color=TEXT_COLOR
        )
        process_text.next_to(layers_demo, DOWN, buff=0.3)
        
        self.play(Write(process_text), run_time=0.5)
        
        # 逐层变换动画
        transformations = [
            lambda p: [p[0] * 1.2, p[1] * 0.8],  # 拉伸
            lambda p: [p[0] + 0.3 * p[1], p[1]],  # 剪切
            lambda p: [p[0], p[1] + 0.2 * np.sign(p[0])],  # 偏移
            lambda p: [p[0] * 1.1, p[1] * 1.2],  # 再拉伸
        ]
        
        current_class1 = [[p[0], p[1]] for p in class1_points]
        current_class2 = [[p[0], p[1]] for p in class2_points]
        
        for i, transform in enumerate(transformations):
            # 高亮当前层
            self.play(
                layers_demo[i][0].animate.set_fill(ACCENT_COLOR, opacity=0.6),
                run_time=0.2
            )
            
            # 应用变换
            new_class1 = [transform(p) for p in current_class1]
            new_class2 = [transform(p) for p in current_class2]
            
            # 动画
            anims = []
            for j, dot in enumerate(dots1):
                target = [new_class1[j][0], new_class1[j][1], 0]
                offset = all_dots.get_center() - ORIGIN
                target = [target[0] + offset[0] - LEFT[0] * 3, target[1] + offset[1] - DOWN[1] * 0.8, 0]
                anims.append(dot.animate.move_to(frame.get_center() + np.array([new_class1[j][0], new_class1[j][1], 0])))
            
            for j, dot in enumerate(dots2):
                anims.append(dot.animate.move_to(frame.get_center() + np.array([new_class2[j][0], new_class2[j][1], 0])))
            
            self.play(*anims, run_time=0.6)
            
            # 恢复层颜色
            self.play(
                layers_demo[i][0].animate.set_fill(NEURAL_COLOR, opacity=0.3),
                run_time=0.1
            )
            
            current_class1 = new_class1
            current_class2 = new_class2
        
        # 更新标签
        self.play(FadeOut(stage1_label))
        stage2_label = Text("变换后: 可以被直线分开!", font_size=18, color=SECONDARY_COLOR)
        stage2_label.next_to(frame, DOWN, buff=0.2)
        
        self.play(Write(stage2_label), run_time=0.5)
        
        # 画分类线
        separator = Line(
            frame.get_center() + LEFT * 2 + UP * 0.3,
            frame.get_center() + RIGHT * 2 + DOWN * 0.3,
            color=SECONDARY_COLOR,
            stroke_width=3
        )
        
        self.play(Create(separator), run_time=0.5)
        
        # 最后一层说明
        final_text = Text(
            "最后一层只需'画条线'即可分类!",
            font_size=20, color=SECONDARY_COLOR
        )
        final_text.next_to(process_text, DOWN, buff=0.3)
        
        self.play(Write(final_text), run_time=0.6)
        
        self.wait(1)
        
        # 核心洞察
        insight = VGroup(
            Text("核心洞察:", font_size=26, color=ACCENT_COLOR),
            Text("深度网络通过一系列变换", font_size=22, color=TEXT_COLOR),
            Text("把杂乱数据变成易处理的形式", font_size=22, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2)
        insight.to_edge(DOWN, buff=0.5)
        
        box = SurroundingRectangle(insight, color=ACCENT_COLOR, buff=0.2, corner_radius=0.1)
        
        self.play(Write(insight), Create(box), run_time=1)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_simple_network(self):
        """创建简化的网络图"""
        network = VGroup()
        
        layers = VGroup()
        layer_sizes = [3, 4, 4, 2]
        
        for i, size in enumerate(layer_sizes):
            layer = VGroup()
            for j in range(size):
                neuron = Circle(
                    radius=0.2,
                    color=NEURAL_COLOR,
                    fill_opacity=0.2
                )
                neuron.set_stroke(NEURAL_COLOR, width=2)
                neuron.move_to([i * 2 - 3, (size - 1) / 2 * 0.6 - j * 0.6, 0])
                layer.add(neuron)
            layers.add(layer)
        
        # 连接线
        connections = VGroup()
        for i in range(len(layer_sizes) - 1):
            for n1 in layers[i]:
                for n2 in layers[i + 1]:
                    line = Line(
                        n1.get_center(), n2.get_center(),
                        stroke_width=0.5,
                        stroke_opacity=0.3,
                        color=TEXT_COLOR
                    )
                    connections.add(line)
        
        network.add(layers, connections)
        return network
    
    def create_gradient_vanish_demo(self):
        """创建梯度消失演示"""
        demo = VGroup()
        
        # 层标签
        layer_labels = VGroup()
        for i in range(5):
            label = Text(f"层{5 - i}", font_size=16, color=SUBTEXT_COLOR)
            label.move_to([i * 1.5 - 3, 1.2, 0])
            layer_labels.add(label)
        
        # 梯度条
        gradient_bars = VGroup()
        for i in range(5):
            bar = Rectangle(
                width=0.4, height=1.5,
                color=GRADIENT_COLOR,
                fill_opacity=0.8
            )
            bar.move_to([i * 1.5 - 3, 0, 0])
            gradient_bars.add(bar)
        
        # 箭头
        arrows = VGroup()
        for i in range(4):
            arrow = Arrow(
                [i * 1.5 - 2.5, 0, 0],
                [i * 1.5 - 2, 0, 0],
                color=GRADIENT_COLOR,
                stroke_width=2,
                buff=0.1
            )
            arrows.add(arrow)
        
        demo.add(layer_labels, gradient_bars, arrows)
        return demo
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = BackpropDepthScene()
    scene.render()
