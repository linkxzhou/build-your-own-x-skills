"""
场景5: 损失函数与优化
基于scenes.md - 展示MSE vs 交叉熵损失，以及学习率对比动画

运行命令:
    manim -pql scene_05_loss_optimization.py LossOptimizationScene
    manim -pqh scene_05_loss_optimization.py LossOptimizationScene
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


class LossOptimizationScene(Scene):
    """场景5: 损失函数与优化"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 损失函数类型
        self.show_loss_types()
        
        # 2. 梯度下降直觉
        self.show_gradient_intuition()
        
        # 3. 学习率对比（核心动画）
        self.show_learning_rate_comparison()
        
        # 4. 核心洞察总结
        self.show_summary()
        
        self.clear_scene()
    
    def show_loss_types(self):
        """损失函数类型"""
        # 标题
        title = Text("损失函数类型", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # MSE损失
        mse_group = VGroup()
        
        mse_title = Text("MSE (均方误差)", font_size=26, color=PRIMARY_COLOR)
        mse_formula = MathTex(
            r"L = \frac{1}{n}\sum_{i=1}^{n}(y_i - \hat{y}_i)^2",
            font_size=28
        )
        mse_formula.set_color(PRIMARY_COLOR)
        
        mse_use = Text("用于：预测数值", font_size=18, color=TEXT_COLOR)
        mse_example = Text("例如：房价、温度、分数", font_size=16, color=SUBTEXT_COLOR)
        
        mse_visual = self.create_mse_visual()
        mse_visual.scale(0.7)
        
        mse_group.add(mse_title, mse_formula, mse_visual, mse_use, mse_example)
        mse_group.arrange(DOWN, buff=0.25)
        mse_group.move_to(LEFT * 3 + DOWN * 0.3)
        
        # 交叉熵损失
        ce_group = VGroup()
        
        ce_title = Text("交叉熵损失", font_size=26, color=ERROR_COLOR)
        ce_formula = MathTex(
            r"L = -\sum_{i=1}^{n}y_i\log(\hat{y}_i)",
            font_size=28
        )
        ce_formula.set_color(ERROR_COLOR)
        
        ce_use = Text("用于：分类任务", font_size=18, color=TEXT_COLOR)
        ce_example = Text("例如：判断猫/狗、情感分析", font_size=16, color=SUBTEXT_COLOR)
        
        ce_visual = self.create_ce_visual()
        ce_visual.scale(0.7)
        
        ce_group.add(ce_title, ce_formula, ce_visual, ce_use, ce_example)
        ce_group.arrange(DOWN, buff=0.25)
        ce_group.move_to(RIGHT * 3 + DOWN * 0.3)
        
        # 分隔线
        separator = Line(UP * 2.5, DOWN * 2.5, color=SUBTEXT_COLOR, stroke_width=1)
        separator.set_opacity(0.5)
        
        # 依次显示
        self.play(FadeIn(mse_group, shift=RIGHT * 0.3), run_time=0.8)
        self.play(Create(separator), run_time=0.3)
        self.play(FadeIn(ce_group, shift=LEFT * 0.3), run_time=0.8)
        
        # 比喻
        mse_analogy = Text('测量"距离"', font_size=16, color=PRIMARY_COLOR)
        mse_analogy.next_to(mse_group, DOWN, buff=0.3)
        
        ce_analogy = Text('测量"概率分布差异"', font_size=16, color=ERROR_COLOR)
        ce_analogy.next_to(ce_group, DOWN, buff=0.3)
        
        self.play(Write(mse_analogy), Write(ce_analogy), run_time=0.5)
        
        self.wait(2)
        self.clear_scene()
    
    def show_gradient_intuition(self):
        """梯度下降直觉"""
        # 标题
        title = Text("梯度下降直觉", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 迷宫比喻
        maze_title = Text("想象在全黑的迷宫里找出口...", font_size=24, color=TEXT_COLOR)
        maze_title.next_to(title, DOWN, buff=0.6)
        
        self.play(Write(maze_title), run_time=0.5)
        
        # 创建损失曲面等高线
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            x_length=5,
            y_length=5,
            axis_config={"color": SUBTEXT_COLOR, "stroke_width": 1}
        )
        axes.next_to(maze_title, DOWN, buff=0.5)
        
        # 等高线
        contours = VGroup()
        for r in [0.5, 1.0, 1.5, 2.0, 2.5]:
            contour = Circle(radius=r * 0.7, color=NEURAL_COLOR, stroke_width=1.5)
            contour.set_opacity(1 - r / 3)
            contour.move_to(axes.get_center())
            contours.add(contour)
        
        self.play(Create(axes), run_time=0.5)
        self.play(FadeIn(contours, lag_ratio=0.1), run_time=0.6)
        
        # 小球
        ball = Dot(radius=0.15, color=SECONDARY_COLOR)
        ball.move_to(axes.get_center() + UP * 1.5 + RIGHT * 1)
        
        self.play(FadeIn(ball, scale=1.5), run_time=0.3)
        
        # 步骤说明
        steps = VGroup(
            Text("1. 脚能感觉坡度（梯度）", font_size=18, color=TEXT_COLOR),
            Text("2. 沿最陡下坡方向走一小步", font_size=18, color=TEXT_COLOR),
            Text("3. 这一步的大小叫 学习率 α", font_size=18, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        steps.to_edge(RIGHT, buff=0.8)
        
        # 梯度箭头
        gradient_arrow = Arrow(
            ball.get_center(),
            ball.get_center() + (axes.get_center() - ball.get_center()).normalized() * 0.8,
            color=ERROR_COLOR, stroke_width=3, buff=0
        )
        
        self.play(GrowArrow(gradient_arrow), run_time=0.4)
        self.play(Write(steps[0]), run_time=0.4)
        
        # 移动小球
        for i in range(5):
            current_pos = ball.get_center()
            target = axes.get_center()
            direction = (target - current_pos).normalized()
            new_pos = current_pos + direction * 0.35
            
            new_arrow = Arrow(
                new_pos,
                new_pos + (target - new_pos).normalized() * 0.5,
                color=ERROR_COLOR, stroke_width=3, buff=0
            )
            
            self.play(
                ball.animate.move_to(new_pos),
                Transform(gradient_arrow, new_arrow),
                run_time=0.25
            )
            
            if i == 0:
                self.play(Write(steps[1]), run_time=0.3)
            elif i == 2:
                self.play(Write(steps[2]), run_time=0.3)
        
        # 到达中心
        self.play(
            Flash(ball.get_center(), color=SECONDARY_COLOR, line_length=0.3),
            FadeOut(gradient_arrow),
            run_time=0.5
        )
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_learning_rate_comparison(self):
        """学习率对比 - 核心动画"""
        # 标题
        title = Text("学习率的影响", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.4)
        
        self.play(Write(title), run_time=0.6)
        
        # 三个并排的损失曲面
        surfaces = VGroup()
        balls = VGroup()
        trajectories = []
        labels = []
        
        lr_configs = [
            ("α 太小", 0.05, PRIMARY_COLOR, "缓慢爬行"),
            ("α 合适", 0.3, SECONDARY_COLOR, "平稳收敛"),
            ("α 太大", 0.8, ERROR_COLOR, "来回震荡"),
        ]
        
        for i, (label, lr, color, desc) in enumerate(lr_configs):
            # 创建等高线图
            surface_group = VGroup()
            
            # 等高线
            center = LEFT * 4 + RIGHT * i * 4
            contours = VGroup()
            for r in [0.4, 0.8, 1.2, 1.6]:
                contour = Circle(radius=r * 0.6, color=NEURAL_COLOR, stroke_width=1)
                contour.set_opacity(0.7 - r / 3)
                contour.move_to(center)
                contours.add(contour)
            
            surface_group.add(contours)
            
            # 标签
            lr_label = Text(label, font_size=20, color=color)
            lr_label.next_to(contours, UP, buff=0.3)
            
            desc_text = Text(desc, font_size=14, color=SUBTEXT_COLOR)
            desc_text.next_to(contours, DOWN, buff=0.3)
            
            surface_group.add(lr_label, desc_text)
            surfaces.add(surface_group)
            
            # 小球
            start_pos = center + UP * 1.2 + RIGHT * 0.5
            ball = Dot(radius=0.12, color=color)
            ball.move_to(start_pos)
            balls.add(ball)
            
            trajectories.append([start_pos.copy()])
            labels.append((lr, center))
        
        # 显示三个场景
        self.play(FadeIn(surfaces), run_time=0.8)
        self.play(FadeIn(balls), run_time=0.3)
        
        # 同时运行三个下降动画
        for step in range(20):
            anims = []
            for i, (lr, center) in enumerate(labels):
                ball = balls[i]
                current_pos = np.array(ball.get_center())
                target = np.array(center)
                
                # 计算梯度方向
                direction = target - current_pos
                dist = np.linalg.norm(direction)
                
                if dist > 0.05:
                    direction = direction / dist
                    
                    # 根据学习率计算步长
                    if i == 0:  # 太小
                        step_size = 0.08
                    elif i == 1:  # 合适
                        step_size = min(0.25, dist * 0.4)
                    else:  # 太大 - 震荡
                        # 添加震荡
                        overshoot = 0.4 * np.sin(step * 0.8)
                        perpendicular = np.array([-direction[1], direction[0], 0])
                        direction = direction + perpendicular * overshoot
                        step_size = 0.35
                    
                    new_pos = current_pos + direction * step_size
                    
                    # 约束在范围内
                    to_center = np.array(center) - new_pos
                    if np.linalg.norm(to_center) > 1.8:
                        new_pos = np.array(center) + to_center / np.linalg.norm(to_center) * 1.8
                    
                    trajectories[i].append(new_pos.copy())
                    anims.append(ball.animate.move_to(new_pos))
            
            if anims:
                self.play(*anims, run_time=0.15)
        
        # 绘制轨迹
        for i, (points, (lr, center)) in enumerate(zip(trajectories, labels)):
            if len(points) > 1:
                traj = VMobject()
                traj.set_points_smoothly(points)
                traj.set_stroke(
                    [PRIMARY_COLOR, SECONDARY_COLOR, ERROR_COLOR][i],
                    width=2, opacity=0.6
                )
                self.play(Create(traj), run_time=0.4)
        
        # 结论
        conclusion = VGroup(
            Text("学习率是", font_size=22, color=TEXT_COLOR),
            Text('"最关键的超参数之一"', font_size=24, color=ACCENT_COLOR),
        ).arrange(RIGHT, buff=0.2)
        conclusion.to_edge(DOWN, buff=0.5)
        
        box = SurroundingRectangle(conclusion, color=ACCENT_COLOR, buff=0.15, corner_radius=0.1)
        
        self.play(Write(conclusion), Create(box), run_time=0.6)
        
        self.wait(2)
        self.clear_scene()
    
    def show_summary(self):
        """核心洞察总结"""
        # 标题
        title = Text("优化的艺术", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.6)
        
        # 核心公式
        formula = MathTex(
            r"w_{new} = w_{old} - \alpha \cdot \nabla L",
            font_size=36
        )
        formula.next_to(title, DOWN, buff=0.6)
        
        formula_box = SurroundingRectangle(formula, color=ACCENT_COLOR, buff=0.2, corner_radius=0.1)
        
        self.play(Write(formula), Create(formula_box), run_time=0.8)
        
        # 分解说明
        explanations = VGroup(
            MathTex(r"w_{new}", font_size=24, color=SECONDARY_COLOR),
            Text("= 新参数", font_size=18, color=TEXT_COLOR),
            MathTex(r"w_{old}", font_size=24, color=TEXT_COLOR),
            Text("= 旧参数", font_size=18, color=TEXT_COLOR),
            MathTex(r"\alpha", font_size=24, color=ACCENT_COLOR),
            Text("= 学习率（步长）", font_size=18, color=TEXT_COLOR),
            MathTex(r"\nabla L", font_size=24, color=ERROR_COLOR),
            Text("= 梯度（下降方向）", font_size=18, color=TEXT_COLOR),
        )
        
        # 排列成网格
        grid = VGroup()
        for i in range(0, 8, 2):
            row = VGroup(explanations[i], explanations[i+1]).arrange(RIGHT, buff=0.2)
            grid.add(row)
        grid.arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        grid.next_to(formula_box, DOWN, buff=0.5)
        
        self.play(FadeIn(grid, lag_ratio=0.1), run_time=1)
        
        # 最终洞察
        insight = Text(
            "反复迭代这个过程，模型的表现就越来越好",
            font_size=22, color=SECONDARY_COLOR
        )
        insight.to_edge(DOWN, buff=0.6)
        
        self.play(Write(insight), run_time=0.6)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_mse_visual(self):
        """创建MSE可视化"""
        visual = VGroup()
        
        # 坐标轴
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 4, 1],
            x_length=2.5,
            y_length=2,
            axis_config={"color": SUBTEXT_COLOR, "stroke_width": 1}
        )
        
        # 真实值点
        true_points = [
            axes.c2p(1, 1),
            axes.c2p(2, 2),
            axes.c2p(3, 2.5),
            axes.c2p(4, 3.5),
        ]
        
        true_dots = VGroup(*[
            Dot(p, radius=0.08, color=SECONDARY_COLOR)
            for p in true_points
        ])
        
        # 预测线
        pred_line = axes.plot(
            lambda x: 0.8 * x + 0.3,
            x_range=[0.5, 4.5],
            color=PRIMARY_COLOR,
            stroke_width=2
        )
        
        # 误差线（距离）
        error_lines = VGroup()
        for p in true_points:
            x_val = axes.p2c(p)[0]
            pred_y = 0.8 * x_val + 0.3
            pred_point = axes.c2p(x_val, pred_y)
            
            error_line = DashedLine(
                p, pred_point,
                color=ERROR_COLOR, stroke_width=1.5
            )
            error_lines.add(error_line)
        
        visual.add(axes, pred_line, true_dots, error_lines)
        return visual
    
    def create_ce_visual(self):
        """创建交叉熵可视化"""
        visual = VGroup()
        
        # 两个概率分布
        # 真实分布
        true_bars = VGroup()
        true_heights = [0.9, 0.05, 0.05]
        colors = [SECONDARY_COLOR, SUBTEXT_COLOR, SUBTEXT_COLOR]
        
        for i, (h, c) in enumerate(zip(true_heights, colors)):
            bar = Rectangle(
                width=0.4, height=h * 2,
                color=c, fill_opacity=0.7
            )
            bar.move_to([i * 0.5 - 0.5, h, 0])
            true_bars.add(bar)
        
        true_label = Text("真实", font_size=12, color=SECONDARY_COLOR)
        true_label.next_to(true_bars, DOWN, buff=0.1)
        
        # 预测分布
        pred_bars = VGroup()
        pred_heights = [0.6, 0.3, 0.1]
        
        for i, h in enumerate(pred_heights):
            bar = Rectangle(
                width=0.4, height=h * 2,
                color=ERROR_COLOR, fill_opacity=0.5
            )
            bar.move_to([i * 0.5 + 1.2, h, 0])
            pred_bars.add(bar)
        
        pred_label = Text("预测", font_size=12, color=ERROR_COLOR)
        pred_label.next_to(pred_bars, DOWN, buff=0.1)
        
        # 箭头（差异）
        arrow = Arrow(
            true_bars.get_right() + RIGHT * 0.2,
            pred_bars.get_left() + LEFT * 0.2,
            color=ACCENT_COLOR, stroke_width=2, buff=0
        )
        diff_label = Text("差异", font_size=10, color=ACCENT_COLOR)
        diff_label.next_to(arrow, UP, buff=0.05)
        
        visual.add(true_bars, true_label, pred_bars, pred_label, arrow, diff_label)
        visual.move_to(ORIGIN)
        return visual
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = LossOptimizationScene()
    scene.render()
