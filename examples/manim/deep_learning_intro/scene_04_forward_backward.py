"""
场景4: 训练的艺术 - 前向传播与反向传播
基于content.md - 展示深度学习的灵魂：前向传播、反向传播、梯度下降

运行命令:
    manim -pql scene_04_forward_backward.py ForwardBackwardScene
    manim -pqh scene_04_forward_backward.py ForwardBackwardScene
"""

from manim import *
import numpy as np

# ============ 颜色定义 ============
PRIMARY_COLOR = "#00D4FF"      # 青色 - 输入、数据、前向传播
SECONDARY_COLOR = "#00FF88"    # 绿色 - 正确、优化
ACCENT_COLOR = "#FFD700"       # 金色 - 重点、高亮
NEURAL_COLOR = "#8B5CF6"       # 紫色 - 神经网络
ERROR_COLOR = "#FF6B6B"        # 红色 - 错误、损失、反向传播
BG_COLOR = "#1a1a2e"           # 深色背景
TEXT_COLOR = "#FFFFFF"         # 白色文字
SUBTEXT_COLOR = "#A0A0A0"      # 灰色次要文字


class ForwardBackwardScene(Scene):
    """场景4: 训练的艺术 - 前向传播与反向传播"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 前向传播流水线
        self.show_forward_propagation()
        
        # 2. 反向传播 - 学习发生的瞬间
        self.show_backward_propagation()
        
        # 3. 梯度下降
        self.show_gradient_descent()
        
        # 4. 深度的价值
        self.show_depth_value()
        
        self.clear_scene()
    
    def show_forward_propagation(self):
        """前向传播流水线"""
        # 标题
        title = Text("训练的艺术", font_size=44, color=ACCENT_COLOR)
        subtitle = Text("前向传播 — 数据穿过流水线", font_size=26, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.4)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        self.wait(0.5)
        
        # 输入图片（猫）
        cat_img = self.create_cat_image()
        cat_img.scale(0.7)
        cat_img.move_to(LEFT * 5.5)
        
        cat_label = Text("猫图片", font_size=14, color=PRIMARY_COLOR)
        cat_label.next_to(cat_img, DOWN, buff=0.2)
        
        self.play(FadeIn(cat_img), Write(cat_label), run_time=0.5)
        
        # 多层流水线盒子
        layers = VGroup()
        layer_names = ["层1\n边缘", "层2\n纹理", "层3\n部件", "层4\n物体"]
        layer_colors = [PRIMARY_COLOR, SECONDARY_COLOR, NEURAL_COLOR, ACCENT_COLOR]
        
        for i, (name, color) in enumerate(zip(layer_names, layer_colors)):
            layer_box = self.create_layer_box(name, color)
            layer_box.scale(0.7)
            layers.add(layer_box)
        
        layers.arrange(RIGHT, buff=0.4)
        layers.next_to(cat_img, RIGHT, buff=0.8)
        
        # 箭头
        arrows = VGroup()
        input_arrow = Arrow(
            cat_img.get_right(),
            layers[0].get_left(),
            buff=0.2, color=PRIMARY_COLOR, stroke_width=3
        )
        arrows.add(input_arrow)
        
        for i in range(len(layers) - 1):
            arrow = Arrow(
                layers[i].get_right(),
                layers[i + 1].get_left(),
                buff=0.1, color=layer_colors[i], stroke_width=3
            )
            arrows.add(arrow)
        
        self.play(FadeIn(layers), FadeIn(arrows), run_time=0.8)
        
        # 输出概率
        output = self.create_probability_output()
        output.scale(0.7)
        output.next_to(layers[-1], RIGHT, buff=0.6)
        
        output_arrow = Arrow(
            layers[-1].get_right(),
            output.get_left(),
            buff=0.2, color=ACCENT_COLOR, stroke_width=3
        )
        
        self.play(GrowArrow(output_arrow), FadeIn(output), run_time=0.5)
        
        # 数据流动动画
        flow_dot = Dot(color=PRIMARY_COLOR, radius=0.12)
        flow_dot.move_to(cat_img.get_center())
        
        self.play(FadeIn(flow_dot), run_time=0.2)
        
        # 流经每层
        flow_path = [cat_img.get_right()]
        for layer in layers:
            flow_path.append(layer.get_left())
            flow_path.append(layer.get_right())
        flow_path.append(output.get_left())
        
        for i in range(0, len(flow_path) - 1, 2):
            if i + 1 < len(flow_path):
                self.play(
                    flow_dot.animate.move_to(flow_path[i + 1]),
                    run_time=0.2
                )
                if i + 2 < len(flow_path):
                    self.play(
                        flow_dot.animate.move_to(flow_path[i + 2]),
                        run_time=0.15
                    )
        
        self.play(FadeOut(flow_dot), run_time=0.2)
        
        # 说明
        forward_note = Text(
            "流水线的长度 = 模型的深度",
            font_size=20, color=SECONDARY_COLOR
        )
        forward_note.to_edge(DOWN, buff=0.5)
        
        self.play(Write(forward_note), run_time=0.5)
        
        self.wait(1)
        
        # 保存当前状态用于反向传播
        self.forward_elements = VGroup(
            cat_img, cat_label, layers, arrows, output, output_arrow, forward_note,
            title_group
        )
        
        self.play(
            FadeOut(title_group), FadeOut(forward_note),
            self.forward_elements.animate.shift(UP * 0.3).scale(0.85),
            run_time=0.5
        )
    
    def show_backward_propagation(self):
        """反向传播 - 学习发生的瞬间"""
        # 新标题
        title = Text("反向传播 — 学习发生的瞬间", font_size=32, color=ERROR_COLOR)
        title.to_edge(UP, buff=0.3)
        
        self.play(Write(title), run_time=0.6)
        
        # 获取现有元素位置
        layers = self.forward_elements[2]
        output = self.forward_elements[4]
        
        # 计算误差
        error_label = Text("误差", font_size=18, color=ERROR_COLOR)
        error_value = Text("0.8", font_size=36, color=ERROR_COLOR, weight=BOLD)
        error_group = VGroup(error_label, error_value).arrange(DOWN, buff=0.1)
        error_group.next_to(output, UP, buff=0.3)
        
        self.play(FadeIn(error_group, scale=1.3), run_time=0.5)
        
        # 误差分解动画
        error_streams = VGroup()
        num_streams = 8
        
        for i in range(num_streams):
            stream = Dot(radius=0.06, color=ERROR_COLOR)
            stream.move_to(error_group.get_center())
            error_streams.add(stream)
        
        self.play(FadeIn(error_streams), run_time=0.2)
        
        # 误差逆向回溯
        backprop_note = Text(
            "红色误差流沿着蓝色箭头逆向回溯",
            font_size=18, color=TEXT_COLOR
        )
        backprop_note.to_edge(DOWN, buff=0.5)
        
        self.play(Write(backprop_note), run_time=0.4)
        
        # 逆向流动到每层
        for i, layer in enumerate(reversed(layers)):
            # 分散流向该层
            target_positions = [
                layer.get_center() + np.array([
                    np.random.uniform(-0.3, 0.3),
                    np.random.uniform(-0.3, 0.3),
                    0
                ])
                for _ in range(num_streams)
            ]
            
            anims = [
                stream.animate.move_to(pos)
                for stream, pos in zip(error_streams, target_positions)
            ]
            
            self.play(
                *anims,
                layer.animate.set_fill(ERROR_COLOR, opacity=0.4),
                run_time=0.4
            )
            
            # 显示梯度强度
            gradient_indicator = Rectangle(
                width=0.15 * (4 - i),
                height=0.4,
                color=ERROR_COLOR,
                fill_opacity=0.8
            )
            gradient_indicator.next_to(layer, DOWN, buff=0.1)
            
            self.play(FadeIn(gradient_indicator), run_time=0.2)
        
        # 链式法则
        chain_rule = MathTex(
            r"\frac{\partial L}{\partial w} = ",
            r"\frac{\partial L}{\partial y}",
            r" \cdot ",
            r"\frac{\partial y}{\partial z}",
            r" \cdot ",
            r"\frac{\partial z}{\partial w}",
            font_size=26
        )
        chain_rule[1].set_color(ERROR_COLOR)
        chain_rule[3].set_color(NEURAL_COLOR)
        chain_rule[5].set_color(PRIMARY_COLOR)
        
        chain_rule.to_edge(DOWN, buff=1.2)
        
        self.play(FadeOut(backprop_note), run_time=0.2)
        self.play(Write(chain_rule), run_time=0.8)
        
        insight = Text(
            "精确计算每个参数'应该承担多少责任'",
            font_size=18, color=SECONDARY_COLOR
        )
        insight.next_to(chain_rule, DOWN, buff=0.2)
        
        self.play(Write(insight), run_time=0.5)
        
        self.wait(1.5)
        
        self.clear_scene()
    
    def show_gradient_descent(self):
        """梯度下降"""
        # 标题
        title = Text("梯度下降 — 参数微调", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 参数可视化
        params_title = Text("模型参数（旋钮）", font_size=22, color=TEXT_COLOR)
        params_title.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(params_title), run_time=0.3)
        
        # 创建旋钮/滑块
        sliders = VGroup()
        for i in range(5):
            slider = self.create_slider(0.3 + i * 0.1)
            sliders.add(slider)
        
        sliders.arrange(RIGHT, buff=0.5)
        sliders.next_to(params_title, DOWN, buff=0.4)
        
        self.play(FadeIn(sliders), run_time=0.5)
        
        # 梯度箭头
        gradient_arrows = VGroup()
        for i, slider in enumerate(sliders):
            direction = 1 if i % 2 == 0 else -1
            arrow = Arrow(
                slider.get_top() + UP * 0.1,
                slider.get_top() + UP * 0.5 + RIGHT * direction * 0.2,
                color=ERROR_COLOR, stroke_width=2, buff=0
            )
            gradient_arrows.add(arrow)
        
        self.play(FadeIn(gradient_arrows), run_time=0.4)
        
        # 公式
        formula = MathTex(
            r"w_{new} = w_{old} - \alpha \cdot \nabla L",
            font_size=32
        )
        formula.next_to(sliders, DOWN, buff=0.6)
        
        formula_box = SurroundingRectangle(formula, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1)
        
        self.play(Write(formula), Create(formula_box), run_time=0.6)
        
        # 学习率说明
        lr_note = VGroup(
            Text("α = 学习率", font_size=18, color=ACCENT_COLOR),
            Text("（步长的大小）", font_size=14, color=SUBTEXT_COLOR),
        ).arrange(RIGHT, buff=0.2)
        lr_note.next_to(formula_box, DOWN, buff=0.3)
        
        self.play(Write(lr_note), run_time=0.4)
        
        # 参数更新动画
        update_text = Text("参数根据梯度方向微调...", font_size=20, color=SECONDARY_COLOR)
        update_text.to_edge(DOWN, buff=0.6)
        
        self.play(Write(update_text), run_time=0.4)
        
        # 滑块移动动画
        for i, slider in enumerate(sliders):
            # 获取滑块中的指示器
            indicator = slider[1]
            direction = -0.2 if i % 2 == 0 else 0.2
            
            self.play(
                indicator.animate.shift(RIGHT * direction),
                run_time=0.3
            )
        
        # 误差变小
        self.play(FadeOut(update_text), FadeOut(gradient_arrows), run_time=0.3)
        
        result = VGroup(
            Text("再次前向传播...", font_size=20, color=TEXT_COLOR),
            Text("误差: 0.8 → 0.5", font_size=24, color=SECONDARY_COLOR),
            Text("变小了！反复迭代，模型越来越好", font_size=18, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        result.to_edge(DOWN, buff=0.5)
        
        self.play(Write(result), run_time=1)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_depth_value(self):
        """深度的价值"""
        # 标题
        title = Text("深度的价值 — 特征层次", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 特征层次可视化
        levels = VGroup()
        level_data = [
            ("底层", "边缘、颜色", PRIMARY_COLOR),
            ("中层", "纹理、部件", SECONDARY_COLOR),
            ("高层", "物体、场景", NEURAL_COLOR),
        ]
        
        for name, desc, color in level_data:
            level = VGroup()
            
            box = RoundedRectangle(
                width=2.8, height=1.2,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.3
            )
            box.set_stroke(color, width=2)
            
            level_name = Text(name, font_size=22, color=color)
            level_name.move_to(box.get_center() + UP * 0.25)
            
            level_desc = Text(desc, font_size=16, color=TEXT_COLOR)
            level_desc.next_to(level_name, DOWN, buff=0.1)
            
            level.add(box, level_name, level_desc)
            levels.add(level)
        
        levels.arrange(RIGHT, buff=0.4)
        levels.next_to(title, DOWN, buff=0.6)
        
        # 依次显示并连接
        arrows = VGroup()
        for i, level in enumerate(levels):
            self.play(FadeIn(level, scale=0.9), run_time=0.4)
            
            if i < len(levels) - 1:
                arrow = Arrow(
                    level.get_right(),
                    levels[i + 1].get_left(),
                    color=TEXT_COLOR, stroke_width=2, buff=0.1
                )
                arrows.add(arrow)
                self.play(GrowArrow(arrow), run_time=0.2)
        
        # 核心洞察
        insight = VGroup(
            Text("多层结构 →", font_size=20, color=TEXT_COLOR),
            Text("学习极其复杂和抽象的特征层次", font_size=20, color=SECONDARY_COLOR),
        ).arrange(RIGHT, buff=0.2)
        insight.next_to(levels, DOWN, buff=0.6)
        
        self.play(Write(insight), run_time=0.6)
        
        # 深度带来表达能力
        power = Text(
            "深度带来了强大的表达能力",
            font_size=24, color=ACCENT_COLOR
        )
        power.to_edge(DOWN, buff=0.6)
        
        box = SurroundingRectangle(power, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1)
        
        self.play(Write(power), Create(box), run_time=0.6)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_cat_image(self):
        """创建猫图片表示"""
        img = VGroup()
        
        # 边框
        frame = Rectangle(width=1.6, height=1.3, color=PRIMARY_COLOR, stroke_width=2)
        
        # 像素网格
        pixels = VGroup()
        for i in range(4):
            for j in range(3):
                pixel = Square(
                    side_length=0.35,
                    color=interpolate_color(ManimColor(PRIMARY_COLOR), ManimColor(ACCENT_COLOR), (i + j) / 6),
                    fill_opacity=0.6
                )
                pixel.move_to(frame.get_center() + np.array([
                    (i - 1.5) * 0.37, (j - 1) * 0.37, 0
                ]))
                pixels.add(pixel)
        
        img.add(frame, pixels)
        return img
    
    def create_layer_box(self, name, color):
        """创建层盒子"""
        layer = VGroup()
        
        box = RoundedRectangle(
            width=1.4, height=1.8,
            corner_radius=0.1,
            color=color,
            fill_opacity=0.3
        )
        box.set_stroke(color, width=2)
        
        label = Text(name, font_size=12, color=color, line_spacing=1.1)
        label.move_to(box.get_center())
        
        layer.add(box, label)
        return layer
    
    def create_probability_output(self):
        """创建概率输出"""
        output = VGroup()
        
        # 猫/狗概率条
        cat_bar = Rectangle(width=1.2, height=0.4, color=SECONDARY_COLOR, fill_opacity=0.8)
        cat_bar.set_stroke(SECONDARY_COLOR, width=2)
        cat_label = Text("猫 0.9", font_size=14, color=TEXT_COLOR)
        cat_label.move_to(cat_bar.get_center())
        
        dog_bar = Rectangle(width=0.2, height=0.4, color=SUBTEXT_COLOR, fill_opacity=0.4)
        dog_bar.set_stroke(SUBTEXT_COLOR, width=1)
        dog_label = Text("狗 0.1", font_size=14, color=SUBTEXT_COLOR)
        dog_label.move_to(dog_bar.get_center())
        
        cat_group = VGroup(cat_bar, cat_label)
        dog_group = VGroup(dog_bar, dog_label)
        
        output.add(cat_group, dog_group)
        output.arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        
        return output
    
    def create_slider(self, value):
        """创建滑块/旋钮"""
        slider = VGroup()
        
        # 轨道
        track = Line(LEFT * 0.5, RIGHT * 0.5, color=SUBTEXT_COLOR, stroke_width=3)
        
        # 指示器
        indicator = Circle(radius=0.1, color=SECONDARY_COLOR, fill_opacity=0.8)
        indicator.move_to(track.point_from_proportion(value))
        
        slider.add(track, indicator)
        return slider
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = ForwardBackwardScene()
    scene.render()
