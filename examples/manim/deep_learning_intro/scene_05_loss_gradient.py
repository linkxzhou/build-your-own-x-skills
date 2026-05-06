"""
场景5: 损失函数与梯度下降
基于content.md - 展示3D损失函数景观与梯度下降动画

运行命令:
    manim -pql scene_05_loss_gradient.py LossGradientScene
    manim -pqh scene_05_loss_gradient.py LossGradientScene
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


class LossGradientScene(ThreeDScene):
    """场景5: 损失函数与梯度下降 - 含3D损失景观"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 损失函数景观 - 3D可视化
        self.show_loss_landscape_3d()
        
        # 2. 梯度下降直觉 (2D)
        self.show_gradient_descent_2d()
        
        # 3. 学习率对比
        self.show_learning_rate_comparison()
        
        self.clear_scene()
    
    def show_loss_landscape_3d(self):
        """3D损失函数景观动画 - content.md中的核心场景"""
        # 设置3D相机
        self.set_camera_orientation(phi=60 * DEGREES, theta=-45 * DEGREES)
        
        # 标题 (2D覆盖)
        title = Text(
            "损失函数景观",
            font_size=36, color=ACCENT_COLOR
        )
        title.to_corner(UL, buff=0.5)
        
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=0.5)
        
        # 创建3D损失曲面 - 起伏不平的山地
        def loss_func(u, v):
            """损失函数: 有多个局部最小值的复杂曲面"""
            return 0.3 * (
                np.sin(u) ** 2 + np.sin(v) ** 2 +
                0.5 * np.exp(-((u - 0.5) ** 2 + (v - 0.5) ** 2))
            ) + 0.1 * (u ** 2 + v ** 2) + 0.5
        
        surface = Surface(
            lambda u, v: np.array([u, v, loss_func(u, v)]),
            u_range=[-2, 2],
            v_range=[-2, 2],
            resolution=(30, 30),
            fill_opacity=0.7
        )
        
        # 颜色映射 - 高度对应颜色
        surface.set_style(fill_opacity=0.7)
        surface.set_fill_by_value(
            axes=Axes(x_range=[-2, 2], y_range=[-2, 2], z_range=[0, 2]),
            colorscale=[
                (SECONDARY_COLOR, 0.3),
                (ACCENT_COLOR, 0.6),
                (ERROR_COLOR, 1.0),
            ],
            axis=2
        )
        
        # 坐标轴
        axes_3d = ThreeDAxes(
            x_range=[-2.5, 2.5, 1],
            y_range=[-2.5, 2.5, 1],
            z_range=[0, 2, 0.5],
            x_length=5,
            y_length=5,
            z_length=3,
        )
        axes_3d.set_color(SUBTEXT_COLOR)
        
        self.play(Create(axes_3d), run_time=0.8)
        self.play(Create(surface), run_time=1.5)
        
        # 旁白文字
        narration1 = Text(
            "我们最初对世界一无所知",
            font_size=20, color=TEXT_COLOR
        )
        narration1.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration1)
        self.play(Write(narration1), run_time=0.6)
        
        # 小球 - 随机起点
        start_pos = np.array([1.5, 1.5, loss_func(1.5, 1.5)])
        ball = Sphere(radius=0.1, color=PRIMARY_COLOR)
        ball.move_to(axes_3d.c2p(*start_pos))
        
        self.play(FadeIn(ball, scale=1.5), run_time=0.5)
        
        # 旁白更新
        self.play(FadeOut(narration1))
        narration2 = Text(
            "沿着最陡的下坡方向滚动",
            font_size=20, color=SECONDARY_COLOR
        )
        narration2.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration2)
        self.play(Write(narration2), run_time=0.5)
        
        # 梯度下降动画
        current_pos = start_pos.copy()
        learning_rate = 0.3
        
        for step in range(12):
            # 计算数值梯度
            eps = 0.01
            grad_u = (loss_func(current_pos[0] + eps, current_pos[1]) - 
                     loss_func(current_pos[0] - eps, current_pos[1])) / (2 * eps)
            grad_v = (loss_func(current_pos[0], current_pos[1] + eps) - 
                     loss_func(current_pos[0], current_pos[1] - eps)) / (2 * eps)
            
            # 更新位置
            current_pos[0] -= learning_rate * grad_u
            current_pos[1] -= learning_rate * grad_v
            current_pos[0] = np.clip(current_pos[0], -2, 2)
            current_pos[1] = np.clip(current_pos[1], -2, 2)
            current_pos[2] = loss_func(current_pos[0], current_pos[1])
            
            new_point = axes_3d.c2p(*current_pos)
            
            self.play(
                ball.animate.move_to(new_point),
                run_time=0.3
            )
        
        # 到达山谷
        self.play(FadeOut(narration2))
        narration3 = Text(
            "找到了山谷! (局部最优)",
            font_size=20, color=SECONDARY_COLOR
        )
        narration3.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration3)
        
        self.play(
            Write(narration3),
            Flash(ball.get_center(), color=SECONDARY_COLOR),
            run_time=0.8
        )
        
        # 旋转相机展示
        self.begin_ambient_camera_rotation(rate=0.2)
        self.wait(2)
        self.stop_ambient_camera_rotation()
        
        # 清理3D场景
        self.play(
            FadeOut(surface), FadeOut(axes_3d), FadeOut(ball),
            FadeOut(title), FadeOut(narration3),
            run_time=0.8
        )
        
        # 重置相机
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
    
    def show_gradient_descent_2d(self):
        """2D梯度下降直觉"""
        # 标题
        title = Text(
            "梯度下降 — 闭眼下山找最低点",
            font_size=32, color=ACCENT_COLOR
        )
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 直觉类比
        intuition = Text(
            "想象你闭着眼在山上，脚能感觉坡度(梯度)",
            font_size=22, color=TEXT_COLOR
        )
        intuition.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(intuition), run_time=0.6)
        
        # 创建2D损失曲线
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=4,
            axis_config={
                "include_tip": True,
                "color": SUBTEXT_COLOR,
            },
        )
        axes.shift(DOWN * 0.5)
        
        # 轴标签
        x_label = Text("参数 w", font_size=18, color=SUBTEXT_COLOR)
        x_label.next_to(axes.x_axis, RIGHT, buff=0.2)
        
        y_label = Text("Loss", font_size=18, color=SUBTEXT_COLOR)
        y_label.next_to(axes.y_axis, UP, buff=0.2)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.8)
        
        # 损失曲线 (抛物线)
        loss_curve = axes.plot(
            lambda x: x ** 2 + 0.3,
            x_range=[-2.8, 2.8],
            color=ERROR_COLOR,
            stroke_width=3
        )
        
        self.play(Create(loss_curve), run_time=0.8)
        
        # 起始位置
        start_x = 2.5
        ball = Dot(
            axes.c2p(start_x, start_x ** 2 + 0.3),
            color=PRIMARY_COLOR,
            radius=0.15
        )
        
        self.play(FadeIn(ball, scale=1.5), run_time=0.5)
        
        # 显示梯度箭头
        x = start_x
        gradient = 2 * x
        
        tangent_line = axes.plot(
            lambda t: gradient * (t - x) + (x ** 2 + 0.3),
            x_range=[x - 0.8, x + 0.3],
            color=ACCENT_COLOR,
            stroke_width=2
        )
        
        gradient_arrow = Arrow(
            axes.c2p(x, x ** 2 + 0.3 + 0.3),
            axes.c2p(x - 0.6, x ** 2 + 0.3 + 0.3),
            color=SECONDARY_COLOR,
            stroke_width=3,
            buff=0
        )
        
        gradient_label = Text(
            "下坡方向",
            font_size=16, color=SECONDARY_COLOR
        )
        gradient_label.next_to(gradient_arrow, UP, buff=0.1)
        
        self.play(
            Create(tangent_line),
            GrowArrow(gradient_arrow),
            Write(gradient_label),
            run_time=0.8
        )
        
        self.wait(0.5)
        
        # 移除梯度标注，开始下降
        self.play(
            FadeOut(tangent_line),
            FadeOut(gradient_arrow),
            FadeOut(gradient_label),
            run_time=0.3
        )
        
        # 下降步骤
        step_text = Text(
            "沿最陡方向走一小步 (学习率 α)",
            font_size=20, color=ACCENT_COLOR
        )
        step_text.to_corner(DL, buff=0.6)
        
        self.play(Write(step_text), run_time=0.4)
        
        # 梯度下降动画
        learning_rate = 0.35
        path_dots = VGroup()
        
        for i in range(7):
            # 记录路径
            path_dot = Dot(
                axes.c2p(x, x ** 2 + 0.3),
                radius=0.04,
                color=PRIMARY_COLOR,
                fill_opacity=0.5
            )
            path_dots.add(path_dot)
            
            gradient = 2 * x
            x = x - learning_rate * gradient
            x = max(-2.8, min(2.8, x))
            
            new_point = axes.c2p(x, x ** 2 + 0.3)
            
            self.play(
                ball.animate.move_to(new_point),
                FadeIn(path_dot),
                run_time=0.35
            )
            
            if abs(x) < 0.1:
                break
        
        # 找到最低点
        success = Text(
            "找到最低点!",
            font_size=24, color=SECONDARY_COLOR
        )
        success.to_corner(DR, buff=0.6)
        
        self.play(
            Write(success),
            Flash(ball.get_center(), color=SECONDARY_COLOR),
            run_time=0.8
        )
        
        # 公式
        formula = MathTex(
            r"w_{new} = w_{old} - \alpha \cdot \nabla L",
            font_size=28
        )
        formula.next_to(success, UP, buff=0.3)
        formula_box = SurroundingRectangle(
            formula, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1
        )
        
        self.play(Write(formula), Create(formula_box), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_learning_rate_comparison(self):
        """学习率对比"""
        # 标题
        title = Text(
            "学习率 α 的影响",
            font_size=36, color=ACCENT_COLOR
        )
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 三个坐标系
        axes_group = VGroup()
        labels = [
            ("α 太小", ERROR_COLOR),
            ("α 合适", SECONDARY_COLOR),
            ("α 太大", ACCENT_COLOR),
        ]
        
        for i in range(3):
            ax = Axes(
                x_range=[-2.5, 2.5, 1],
                y_range=[0, 4, 1],
                x_length=3.5,
                y_length=2.5,
                axis_config={
                    "include_tip": False,
                    "color": SUBTEXT_COLOR,
                },
            )
            axes_group.add(ax)
        
        axes_group.arrange(RIGHT, buff=0.6)
        axes_group.shift(DOWN * 0.3)
        
        self.play(Create(axes_group), run_time=0.8)
        
        # 损失曲线和标签
        curves = VGroup()
        label_texts = VGroup()
        
        for i, (label, color) in enumerate(labels):
            curve = axes_group[i].plot(
                lambda x: x ** 2 + 0.2,
                x_range=[-2.2, 2.2],
                color=ERROR_COLOR,
                stroke_width=2
            )
            curves.add(curve)
            
            label_text = Text(label, font_size=18, color=color)
            label_text.next_to(axes_group[i], UP, buff=0.2)
            label_texts.add(label_text)
        
        self.play(
            *[Create(c) for c in curves],
            *[Write(l) for l in label_texts],
            run_time=0.6
        )
        
        # 三个小球同时下降
        balls = VGroup()
        start_x = 2.0
        
        for ax in axes_group:
            ball = Dot(
                ax.c2p(start_x, start_x ** 2 + 0.2),
                color=PRIMARY_COLOR,
                radius=0.1
            )
            balls.add(ball)
        
        self.play(FadeIn(balls), run_time=0.3)
        
        # 不同学习率
        learning_rates = [0.08, 0.4, 1.1]
        xs = [start_x, start_x, start_x]
        
        # 路径线
        paths = [VGroup() for _ in range(3)]
        
        for step in range(20):
            anims = []
            
            for i in range(3):
                # 记录旧位置
                old_x = xs[i]
                
                gradient = 2 * xs[i]
                xs[i] = xs[i] - learning_rates[i] * gradient
                xs[i] = max(-2.2, min(2.2, xs[i]))
                
                new_point = axes_group[i].c2p(xs[i], xs[i] ** 2 + 0.2)
                old_point = axes_group[i].c2p(old_x, old_x ** 2 + 0.2)
                
                # 路径线
                path_line = Line(
                    old_point, new_point,
                    color=labels[i][1],
                    stroke_width=1,
                    stroke_opacity=0.6
                )
                paths[i].add(path_line)
                
                anims.append(balls[i].animate.move_to(new_point))
                anims.append(FadeIn(path_line))
            
            self.play(*anims, run_time=0.2)
        
        # 结果说明
        results_data = [
            ("收敛太慢 😴", ERROR_COLOR),
            ("平稳收敛 ✓", SECONDARY_COLOR),
            ("震荡/发散 ❌", ACCENT_COLOR),
        ]
        
        results = VGroup()
        for i, (text, color) in enumerate(results_data):
            result = Text(text, font_size=16, color=color)
            result.next_to(axes_group[i], DOWN, buff=0.3)
            results.add(result)
        
        self.play(FadeIn(results), run_time=0.5)
        
        self.wait(1.5)
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = LossGradientScene()
    scene.render()
