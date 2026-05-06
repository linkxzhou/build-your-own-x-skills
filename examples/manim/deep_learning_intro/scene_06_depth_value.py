"""
场景6: 梯度挑战与深度的秘密
基于scenes.md - 展示链式法则、梯度消失/爆炸，以及深度网络的表示学习能力

运行命令:
    manim -pql scene_06_depth_value.py DepthValueScene
    manim -pqh scene_06_depth_value.py DepthValueScene
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


class DepthValueScene(Scene):
    """场景6: 梯度挑战与深度的秘密"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 反向传播的数学 - 链式法则
        self.show_chain_rule()
        
        # 2. 梯度消失/爆炸问题
        self.show_gradient_problems()
        
        # 3. 深度的价值 - 核心动画（数据点变形）
        self.show_depth_value_animation()
        
        # 4. 核心洞察
        self.show_insights()
        
        self.clear_scene()
    
    def show_chain_rule(self):
        """反向传播的数学 - 链式法则"""
        # 标题
        title = Text("反向传播的数学", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("链式法则", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.3)
        
        # 创建多层网络示意
        layers = VGroup()
        layer_labels = ["输入", "层1", "层2", "层3", "输出"]
        
        for i, label in enumerate(layer_labels):
            box = RoundedRectangle(
                width=1.2, height=0.8,
                corner_radius=0.1,
                color=PRIMARY_COLOR if i == 0 else (ACCENT_COLOR if i == 4 else NEURAL_COLOR),
                fill_opacity=0.3
            )
            box.set_stroke(PRIMARY_COLOR if i == 0 else (ACCENT_COLOR if i == 4 else NEURAL_COLOR), width=2)
            
            text = Text(label, font_size=14, color=TEXT_COLOR)
            text.move_to(box.get_center())
            
            layer_group = VGroup(box, text)
            layers.add(layer_group)
        
        layers.arrange(RIGHT, buff=0.5)
        layers.next_to(title_group, DOWN, buff=0.6)
        
        # 箭头和变量标注
        arrows = VGroup()
        var_labels = ["x", "z_1", "z_2", "z_3", "y"]
        
        for i in range(len(layers) - 1):
            arrow = Arrow(
                layers[i].get_right(),
                layers[i + 1].get_left(),
                color=PRIMARY_COLOR, stroke_width=2, buff=0.1
            )
            arrows.add(arrow)
        
        # 变量标注
        for i, var in enumerate(var_labels):
            var_text = MathTex(var, font_size=18, color=SUBTEXT_COLOR)
            var_text.next_to(layers[i], DOWN, buff=0.15)
            arrows.add(var_text)
        
        self.play(FadeIn(layers), run_time=0.6)
        self.play(FadeIn(arrows), run_time=0.4)
        
        # 损失 L
        loss_label = MathTex("L", font_size=24, color=ERROR_COLOR)
        loss_label.next_to(layers[-1], RIGHT, buff=0.3)
        
        self.play(FadeIn(loss_label), run_time=0.3)
        
        # 链式法则公式
        chain_rule = MathTex(
            r"\frac{\partial L}{\partial w}",
            r" = ",
            r"\frac{\partial L}{\partial y}",
            r" \cdot ",
            r"\frac{\partial y}{\partial z_3}",
            r" \cdot ",
            r"\frac{\partial z_3}{\partial z_2}",
            r" \cdot ",
            r"\frac{\partial z_2}{\partial z_1}",
            r" \cdot ",
            r"\frac{\partial z_1}{\partial w}",
            font_size=24
        )
        
        chain_rule[0].set_color(ACCENT_COLOR)
        chain_rule[2].set_color(ERROR_COLOR)
        chain_rule[4].set_color(NEURAL_COLOR)
        chain_rule[6].set_color(NEURAL_COLOR)
        chain_rule[8].set_color(NEURAL_COLOR)
        chain_rule[10].set_color(PRIMARY_COLOR)
        
        chain_rule.next_to(layers, DOWN, buff=0.8)
        
        self.play(Write(chain_rule), run_time=1.2)
        
        # 高亮"乘积链"
        highlight_box = SurroundingRectangle(
            chain_rule[4:11], 
            color=ACCENT_COLOR, buff=0.1, corner_radius=0.05
        )
        
        self.play(Create(highlight_box), run_time=0.4)
        
        # 说明
        explanation = Text(
            "从输出的错误倒推每个参数的责任 — 乘积链",
            font_size=18, color=SECONDARY_COLOR
        )
        explanation.next_to(chain_rule, DOWN, buff=0.4)
        
        self.play(Write(explanation), run_time=0.6)
        
        # 核心价值
        value = Text(
            "让海量参数的高效调整成为可能！",
            font_size=20, color=ACCENT_COLOR
        )
        value.to_edge(DOWN, buff=0.5)
        
        self.play(Write(value), run_time=0.5)
        
        self.wait(2)
        self.clear_scene()
    
    def show_gradient_problems(self):
        """梯度消失/爆炸问题"""
        # 标题
        title = Text("梯度消失与爆炸", font_size=36, color=ERROR_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 创建深层网络示意
        layers = VGroup()
        for i in range(8):
            box = RoundedRectangle(
                width=0.6, height=0.8,
                corner_radius=0.05,
                color=NEURAL_COLOR,
                fill_opacity=0.3
            )
            box.set_stroke(NEURAL_COLOR, width=2)
            layers.add(box)
        
        layers.arrange(RIGHT, buff=0.3)
        layers.next_to(title, DOWN, buff=0.6)
        
        # 标注
        start_label = Text("输入", font_size=14, color=PRIMARY_COLOR)
        start_label.next_to(layers[0], DOWN, buff=0.2)
        
        end_label = Text("输出", font_size=14, color=ACCENT_COLOR)
        end_label.next_to(layers[-1], DOWN, buff=0.2)
        
        self.play(FadeIn(layers), Write(start_label), Write(end_label), run_time=0.6)
        
        # 梯度消失动画
        vanish_title = Text("梯度消失", font_size=22, color=ERROR_COLOR)
        vanish_title.next_to(layers, DOWN, buff=0.8)
        
        self.play(Write(vanish_title), run_time=0.4)
        
        # 梯度流动（从右到左，逐渐变淡）
        gradient_dots = VGroup()
        for i, layer in enumerate(reversed(layers)):
            opacity = 1.0 - i * 0.12
            dot = Dot(
                layer.get_center(),
                radius=0.15 * opacity + 0.05,
                color=ERROR_COLOR
            )
            dot.set_opacity(max(0.1, opacity))
            gradient_dots.add(dot)
        
        self.play(FadeIn(gradient_dots, lag_ratio=0.1), run_time=1)
        
        # 说明
        vanish_desc = Text(
            "梯度经过很多层连乘 → 变得极小",
            font_size=16, color=SUBTEXT_COLOR
        )
        vanish_desc.next_to(vanish_title, DOWN, buff=0.2)
        
        problem = Text(
            "前面的层收不到有效信号，学不到东西！",
            font_size=18, color=ERROR_COLOR
        )
        problem.next_to(vanish_desc, DOWN, buff=0.2)
        
        self.play(Write(vanish_desc), run_time=0.5)
        self.play(Write(problem), run_time=0.5)
        
        self.wait(1)
        
        # 解决方案
        self.play(
            FadeOut(gradient_dots), FadeOut(vanish_title),
            FadeOut(vanish_desc), FadeOut(problem),
            run_time=0.4
        )
        
        solution_title = Text("解决思路", font_size=24, color=SECONDARY_COLOR)
        solution_title.next_to(layers, DOWN, buff=0.6)
        
        self.play(Write(solution_title), run_time=0.4)
        
        solutions = VGroup(
            Text("• 跳跃连接 (Skip Connection)", font_size=18, color=TEXT_COLOR),
            Text('  给梯度开"绿色通道"', font_size=14, color=SUBTEXT_COLOR),
            Text("• 批量归一化 (BatchNorm)", font_size=18, color=TEXT_COLOR),
            Text("  稳定每层输入分布", font_size=14, color=SUBTEXT_COLOR),
            Text("• 更好的激活函数 (ReLU)", font_size=18, color=TEXT_COLOR),
            Text("  避免梯度被压缩", font_size=14, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        solutions.next_to(solution_title, DOWN, buff=0.3)
        
        self.play(FadeIn(solutions, lag_ratio=0.1), run_time=1)
        
        # 跳跃连接可视化
        skip_arrow = CurvedArrow(
            layers[1].get_top() + UP * 0.1,
            layers[5].get_top() + UP * 0.1,
            color=SECONDARY_COLOR, stroke_width=3, angle=-TAU/4
        )
        skip_label = Text("跳跃!", font_size=12, color=SECONDARY_COLOR)
        skip_label.next_to(skip_arrow, UP, buff=0.1)
        
        self.play(Create(skip_arrow), Write(skip_label), run_time=0.6)
        
        self.wait(2)
        self.clear_scene()
    
    def show_depth_value_animation(self):
        """深度的价值 - 核心动画（数据点分类变形）"""
        # 标题
        title = Text("深度的价值", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("8层网络如何分类两类混杂的点", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.4)
        
        self.play(Write(title), run_time=0.6)
        self.play(FadeIn(subtitle), run_time=0.3)
        
        # 创建初始数据点（两类混杂）
        np.random.seed(42)
        n_points = 30
        
        # 类1（红色）- 螺旋状
        theta1 = np.linspace(0, 2 * np.pi, n_points // 2)
        r1 = 0.5 + theta1 * 0.15
        class1_x = r1 * np.cos(theta1) + np.random.normal(0, 0.08, n_points // 2)
        class1_y = r1 * np.sin(theta1) + np.random.normal(0, 0.08, n_points // 2)
        
        # 类2（蓝色）- 另一个螺旋
        theta2 = np.linspace(0, 2 * np.pi, n_points // 2) + np.pi
        r2 = 0.5 + theta2 * 0.15 - np.pi * 0.15
        class2_x = r2 * np.cos(theta2) + np.random.normal(0, 0.08, n_points // 2)
        class2_y = r2 * np.sin(theta2) + np.random.normal(0, 0.08, n_points // 2)
        
        # 归一化
        all_x = np.concatenate([class1_x, class2_x])
        all_y = np.concatenate([class1_y, class2_y])
        scale = max(np.abs(all_x).max(), np.abs(all_y).max()) / 1.5
        
        class1_x /= scale
        class1_y /= scale
        class2_x /= scale
        class2_y /= scale
        
        # 创建点
        class1_dots = VGroup()
        class2_dots = VGroup()
        
        for x, y in zip(class1_x, class1_y):
            dot = Dot(
                point=[x * 2, y * 2, 0],
                radius=0.08,
                color=ERROR_COLOR
            )
            class1_dots.add(dot)
        
        for x, y in zip(class2_x, class2_y):
            dot = Dot(
                point=[x * 2, y * 2, 0],
                radius=0.08,
                color=PRIMARY_COLOR
            )
            class2_dots.add(dot)
        
        all_dots = VGroup(class1_dots, class2_dots)
        all_dots.move_to(LEFT * 3)
        
        # 坐标系
        axes = Axes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            x_length=4,
            y_length=4,
            axis_config={"color": SUBTEXT_COLOR, "stroke_width": 1}
        )
        axes.move_to(LEFT * 3)
        
        # 初始状态标签
        initial_label = Text("初始：两类混杂", font_size=18, color=TEXT_COLOR)
        initial_label.next_to(axes, DOWN, buff=0.3)
        
        self.play(Create(axes), run_time=0.5)
        self.play(FadeIn(all_dots), Write(initial_label), run_time=0.6)
        
        # 尝试画直线分割（失败）
        failed_line = Line(
            axes.c2p(-2, 2), axes.c2p(2, -2),
            color=ACCENT_COLOR, stroke_width=2
        )
        
        fail_label = Text("❌ 无法用直线分开", font_size=16, color=ERROR_COLOR)
        fail_label.next_to(initial_label, DOWN, buff=0.15)
        
        self.play(Create(failed_line), Write(fail_label), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(failed_line), FadeOut(fail_label), run_time=0.3)
        
        # 层处理过程
        layer_indicator = VGroup()
        layer_boxes = VGroup()
        
        for i in range(8):
            box = RoundedRectangle(
                width=0.4, height=0.5,
                corner_radius=0.05,
                color=NEURAL_COLOR,
                fill_opacity=0.3
            )
            box.set_stroke(NEURAL_COLOR, width=2)
            layer_boxes.add(box)
        
        layer_boxes.arrange(RIGHT, buff=0.15)
        layer_boxes.move_to(RIGHT * 3 + UP * 2)
        
        layer_title = Text("网络层", font_size=16, color=NEURAL_COLOR)
        layer_title.next_to(layer_boxes, UP, buff=0.2)
        
        self.play(FadeIn(layer_boxes), Write(layer_title), run_time=0.4)
        
        # 变形过程（8步）
        transformation_steps = [
            # 每步变换参数 [scale_x, scale_y, rotation, shift_x, shift_y]
            [1.1, 0.9, 0.1, 0.1, 0],
            [0.9, 1.1, -0.15, 0, 0.1],
            [1.0, 1.0, 0.2, 0.15, -0.1],
            [1.15, 0.85, -0.1, -0.1, 0.15],
            [0.85, 1.15, 0.15, 0.1, 0],
            [1.0, 1.0, -0.2, 0, -0.1],
            [1.2, 0.8, 0.1, -0.15, 0.1],
            [0.9, 1.1, 0, 0.2, 0.1],  # 最终拉开
        ]
        
        # 最终目标位置（两类完全分开）
        final_class1_positions = []
        final_class2_positions = []
        
        for i in range(n_points // 2):
            # 红色点移到上方
            x = np.random.uniform(-1.5, 1.5)
            y = np.random.uniform(0.5, 2.0)
            final_class1_positions.append([x, y, 0])
        
        for i in range(n_points // 2):
            # 蓝色点移到下方
            x = np.random.uniform(-1.5, 1.5)
            y = np.random.uniform(-2.0, -0.5)
            final_class2_positions.append([x, y, 0])
        
        # 逐层变换
        for step in range(8):
            # 高亮当前层
            self.play(
                layer_boxes[step].animate.set_fill(ACCENT_COLOR, opacity=0.6),
                run_time=0.2
            )
            
            # 计算插值位置
            progress = (step + 1) / 8
            
            anims = []
            for i, dot in enumerate(class1_dots):
                start = np.array(dot.get_center())
                end = np.array(final_class1_positions[i]) + np.array(axes.get_center())
                new_pos = start + (end - start) * (progress ** 0.5) * 0.8
                
                # 添加一些随机扰动
                noise = np.array([
                    np.random.uniform(-0.1, 0.1),
                    np.random.uniform(-0.1, 0.1),
                    0
                ])
                anims.append(dot.animate.move_to(new_pos + noise * (1 - progress)))
            
            for i, dot in enumerate(class2_dots):
                start = np.array(dot.get_center())
                end = np.array(final_class2_positions[i]) + np.array(axes.get_center())
                new_pos = start + (end - start) * (progress ** 0.5) * 0.8
                
                noise = np.array([
                    np.random.uniform(-0.1, 0.1),
                    np.random.uniform(-0.1, 0.1),
                    0
                ])
                anims.append(dot.animate.move_to(new_pos + noise * (1 - progress)))
            
            self.play(*anims, run_time=0.4)
            
            # 更新层状态
            self.play(
                layer_boxes[step].animate.set_fill(SECONDARY_COLOR, opacity=0.4),
                run_time=0.15
            )
        
        # 最终状态
        self.play(FadeOut(initial_label), run_time=0.2)
        
        final_label = Text("最终：两类完全分开！", font_size=18, color=SECONDARY_COLOR)
        final_label.next_to(axes, DOWN, buff=0.3)
        
        self.play(Write(final_label), run_time=0.4)
        
        # 画分割线
        separator = DashedLine(
            axes.c2p(-2.5, 0), axes.c2p(2.5, 0),
            color=ACCENT_COLOR, stroke_width=3
        )
        
        success_label = Text("✓ 一条直线就能分开", font_size=16, color=SECONDARY_COLOR)
        success_label.next_to(final_label, DOWN, buff=0.15)
        
        self.play(Create(separator), Write(success_label), run_time=0.6)
        
        # 核心洞察
        insight = Text(
            "每一层都在'重新编码'数据，把杂乱变成易处理",
            font_size=20, color=ACCENT_COLOR
        )
        insight.to_edge(DOWN, buff=0.4)
        
        box = SurroundingRectangle(insight, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1)
        
        self.play(Write(insight), Create(box), run_time=0.6)
        
        self.wait(2)
        self.clear_scene()
    
    def show_insights(self):
        """核心洞察总结"""
        # 标题
        title = Text("表示学习的威力", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.6)
        
        # 核心概念
        concepts = VGroup(
            Text("深度网络学习的是", font_size=24, color=TEXT_COLOR),
            Text('"数据的表示"', font_size=32, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2)
        concepts.next_to(title, DOWN, buff=0.6)
        
        self.play(Write(concepts), run_time=0.8)
        
        # 变换过程图示
        transform_visual = VGroup()
        
        # 混乱输入
        chaos = VGroup()
        np.random.seed(123)
        for _ in range(15):
            dot = Dot(
                point=[np.random.uniform(-0.8, 0.8), np.random.uniform(-0.8, 0.8), 0],
                radius=0.06,
                color=np.random.choice([ERROR_COLOR, PRIMARY_COLOR])
            )
            chaos.add(dot)
        
        chaos_box = RoundedRectangle(
            width=2, height=2,
            corner_radius=0.1,
            color=SUBTEXT_COLOR,
            fill_opacity=0.1
        )
        chaos_box.set_stroke(SUBTEXT_COLOR, width=1)
        chaos.move_to(chaos_box.get_center())
        
        chaos_label = Text("混乱数据", font_size=16, color=SUBTEXT_COLOR)
        chaos_label.next_to(chaos_box, DOWN, buff=0.2)
        
        chaos_group = VGroup(chaos_box, chaos, chaos_label)
        chaos_group.move_to(LEFT * 3.5)
        
        # 箭头
        arrow = Arrow(
            chaos_group.get_right() + RIGHT * 0.2,
            chaos_group.get_right() + RIGHT * 2.5,
            color=NEURAL_COLOR, stroke_width=3
        )
        
        arrow_label = Text("多层变换", font_size=14, color=NEURAL_COLOR)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        # 整齐输出
        order = VGroup()
        for i in range(7):
            dot = Dot(
                point=[0, 0.5 + i * 0.15, 0],
                radius=0.06,
                color=ERROR_COLOR
            )
            order.add(dot)
        for i in range(8):
            dot = Dot(
                point=[0, -0.5 - i * 0.15, 0],
                radius=0.06,
                color=PRIMARY_COLOR
            )
            order.add(dot)
        
        order_box = RoundedRectangle(
            width=2, height=2,
            corner_radius=0.1,
            color=SECONDARY_COLOR,
            fill_opacity=0.1
        )
        order_box.set_stroke(SECONDARY_COLOR, width=2)
        order.move_to(order_box.get_center())
        
        separator = DashedLine(
            order_box.get_left() + RIGHT * 0.2,
            order_box.get_right() + LEFT * 0.2,
            color=ACCENT_COLOR, stroke_width=2
        )
        separator.move_to(order_box.get_center())
        
        order_label = Text("易处理形式", font_size=16, color=SECONDARY_COLOR)
        order_label.next_to(order_box, DOWN, buff=0.2)
        
        order_group = VGroup(order_box, order, separator, order_label)
        order_group.move_to(RIGHT * 3.5)
        
        transform_visual.add(chaos_group, arrow, arrow_label, order_group)
        transform_visual.next_to(concepts, DOWN, buff=0.6)
        
        self.play(FadeIn(chaos_group), run_time=0.5)
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=0.4)
        self.play(FadeIn(order_group), run_time=0.5)
        
        # 最终总结
        summary = Text(
            '这就是"表示学习"的威力',
            font_size=24, color=ACCENT_COLOR
        )
        summary.to_edge(DOWN, buff=0.5)
        
        box = SurroundingRectangle(summary, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1)
        
        self.play(Write(summary), Create(box), run_time=0.6)
        
        self.wait(2)
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = DepthValueScene()
    scene.render()
