"""
场景2: 学习范式 - 从规则到模式
基于content.md - 展示监督/无监督/强化学习，以及3D损失函数景观

运行命令:
    manim -pql scene_02_learning_paradigms.py LearningParadigmsScene
    manim -pqh scene_02_learning_paradigms.py LearningParadigmsScene
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


class LearningParadigmsScene(ThreeDScene):
    """场景2: 学习范式 - 从规则到模式"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 范式转变：传统编程 vs 机器学习
        self.show_paradigm_shift()
        
        # 2. 三种学习方式
        self.show_three_paradigms()
        
        # 3. 损失函数景观（核心3D动画）
        self.show_loss_landscape_3d()
        
        self.clear_scene()
    
    def show_paradigm_shift(self):
        """范式转变：传统编程 vs 机器学习"""
        # 标题
        title = Text("范式转变", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 传统编程
        trad_title = Text("传统编程", font_size=28, color=SUBTEXT_COLOR)
        trad_title.move_to(LEFT * 3 + UP * 1.5)
        
        trad_flow = VGroup(
            self.create_flow_box("规则", PRIMARY_COLOR, 1.2),
            Text("+", font_size=24, color=TEXT_COLOR),
            self.create_flow_box("数据", SECONDARY_COLOR, 1.2),
            Arrow(LEFT * 0.3, RIGHT * 0.3, color=TEXT_COLOR, stroke_width=2),
            self.create_flow_box("答案", ACCENT_COLOR, 1.2),
        ).arrange(RIGHT, buff=0.2)
        trad_flow.next_to(trad_title, DOWN, buff=0.3)
        
        trad_desc = Text(
            "我们告诉计算机规则",
            font_size=16, color=SUBTEXT_COLOR
        )
        trad_desc.next_to(trad_flow, DOWN, buff=0.2)
        
        self.play(Write(trad_title), run_time=0.3)
        self.play(FadeIn(trad_flow, lag_ratio=0.1), run_time=0.8)
        self.play(Write(trad_desc), run_time=0.4)
        
        # VS
        vs_text = Text("VS", font_size=36, color=TEXT_COLOR, weight=BOLD)
        vs_text.move_to(ORIGIN)
        
        self.play(Write(vs_text), run_time=0.3)
        
        # 机器学习
        ml_title = Text("机器学习", font_size=28, color=ACCENT_COLOR)
        ml_title.move_to(RIGHT * 3 + UP * 1.5)
        
        ml_flow = VGroup(
            self.create_flow_box("数据", PRIMARY_COLOR, 1.2),
            Text("+", font_size=24, color=TEXT_COLOR),
            self.create_flow_box("答案", SECONDARY_COLOR, 1.2),
            Arrow(LEFT * 0.3, RIGHT * 0.3, color=TEXT_COLOR, stroke_width=2),
            self.create_flow_box("规则", ACCENT_COLOR, 1.2),
        ).arrange(RIGHT, buff=0.2)
        ml_flow.next_to(ml_title, DOWN, buff=0.3)
        
        ml_desc = Text(
            "让计算机自己总结规则",
            font_size=16, color=SECONDARY_COLOR
        )
        ml_desc.next_to(ml_flow, DOWN, buff=0.2)
        
        self.play(Write(ml_title), run_time=0.3)
        self.play(FadeIn(ml_flow, lag_ratio=0.1), run_time=0.8)
        self.play(Write(ml_desc), run_time=0.4)
        
        # 革命性
        revolution = Text(
            "这是一个革命性的转变！",
            font_size=24, color=ACCENT_COLOR
        )
        revolution.to_edge(DOWN, buff=0.6)
        
        self.play(Write(revolution), run_time=0.6)
        self.wait(1.5)
        
        self.clear_scene()
    
    def show_three_paradigms(self):
        """三种学习方式"""
        # 标题
        title = Text("三种学习方式", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 三种方式并排
        paradigms = VGroup()
        
        # 监督学习
        supervised = self.create_paradigm_card(
            "监督学习",
            "Supervised Learning",
            "图片 + 标签 → 学习关联",
            "识别猫狗",
            PRIMARY_COLOR,
            self.create_supervised_icon()
        )
        
        # 无监督学习
        unsupervised = self.create_paradigm_card(
            "无监督学习",
            "Unsupervised Learning",
            "只给数据 → 发现结构",
            "文章聚类",
            SECONDARY_COLOR,
            self.create_unsupervised_icon()
        )
        
        # 强化学习
        reinforcement = self.create_paradigm_card(
            "强化学习",
            "Reinforcement Learning",
            "试错 + 奖励 → 学习策略",
            "AlphaGo 下棋",
            NEURAL_COLOR,
            self.create_reinforcement_icon()
        )
        
        paradigms.add(supervised, unsupervised, reinforcement)
        paradigms.arrange(RIGHT, buff=0.5)
        paradigms.next_to(title, DOWN, buff=0.6)
        
        # 依次显示
        for paradigm in paradigms:
            self.play(FadeIn(paradigm, scale=0.9), run_time=0.6)
            self.wait(0.3)
        
        # 核心概念
        core_concept = VGroup(
            Text("核心概念:", font_size=24, color=ACCENT_COLOR),
            Text("损失函数 — 衡量模型预测有多'糟糕'", font_size=22, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.2)
        core_concept.to_edge(DOWN, buff=0.6)
        
        self.play(Write(core_concept), run_time=0.8)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_loss_landscape_3d(self):
        """3D损失函数景观动画 - content.md中的核心场景"""
        # 设置3D相机
        self.set_camera_orientation(phi=65 * DEGREES, theta=-45 * DEGREES)
        
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
            # 主要山谷
            main_valley = 0.3 * (u ** 2 + v ** 2)
            # 添加一些起伏
            ripples = 0.2 * np.sin(2 * u) * np.sin(2 * v)
            # 局部最小值
            local_min = 0.4 * np.exp(-((u - 1) ** 2 + (v - 1) ** 2) / 0.5)
            return main_valley + ripples + local_min + 0.5
        
        surface = Surface(
            lambda u, v: np.array([u, v, loss_func(u, v)]),
            u_range=[-2.5, 2.5],
            v_range=[-2.5, 2.5],
            resolution=(40, 40),
            fill_opacity=0.75
        )
        
        # 颜色映射 - 高度对应颜色（绿色低谷，红色高峰）
        surface.set_style(fill_opacity=0.75)
        surface.set_fill_by_value(
            axes=Axes(x_range=[-2.5, 2.5], y_range=[-2.5, 2.5], z_range=[0, 3]),
            colorscale=[
                (SECONDARY_COLOR, 0.2),
                (ACCENT_COLOR, 0.5),
                (ERROR_COLOR, 1.0),
            ],
            axis=2
        )
        
        # 坐标轴
        axes_3d = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 3, 0.5],
            x_length=6,
            y_length=6,
            z_length=4,
        )
        axes_3d.set_color(SUBTEXT_COLOR)
        
        self.play(Create(axes_3d), run_time=0.8)
        self.play(Create(surface), run_time=1.5)
        
        # 旁白文字1
        narration1 = Text(
            "高度 = 损失值，我们的目标是最低点（山谷）",
            font_size=18, color=TEXT_COLOR
        )
        narration1.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration1)
        self.play(Write(narration1), run_time=0.6)
        
        self.wait(0.5)
        
        # 小球 - 随机起点
        start_u, start_v = 2.0, 2.0
        start_pos = np.array([start_u, start_v, loss_func(start_u, start_v)])
        ball = Sphere(radius=0.12, color=PRIMARY_COLOR)
        ball.set_opacity(0.9)
        ball.move_to(axes_3d.c2p(*start_pos))
        
        self.play(FadeIn(ball, scale=1.5), run_time=0.5)
        
        # 更新旁白
        self.play(FadeOut(narration1))
        narration2 = Text(
            "我们最初对世界一无所知，随机站在某个位置",
            font_size=18, color=TEXT_COLOR
        )
        narration2.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration2)
        self.play(Write(narration2), run_time=0.6)
        
        self.wait(0.8)
        
        # 更新旁白
        self.play(FadeOut(narration2))
        narration3 = Text(
            "沿着最陡的下坡方向滚动（梯度下降）",
            font_size=18, color=SECONDARY_COLOR
        )
        narration3.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration3)
        self.play(Write(narration3), run_time=0.5)
        
        # 梯度下降动画
        current_u, current_v = start_u, start_v
        learning_rate = 0.25
        
        # 绘制轨迹
        trajectory_points = [axes_3d.c2p(current_u, current_v, loss_func(current_u, current_v))]
        
        for step in range(15):
            # 计算数值梯度
            eps = 0.01
            grad_u = (loss_func(current_u + eps, current_v) - 
                     loss_func(current_u - eps, current_v)) / (2 * eps)
            grad_v = (loss_func(current_u, current_v + eps) - 
                     loss_func(current_u, current_v - eps)) / (2 * eps)
            
            # 更新位置
            current_u -= learning_rate * grad_u
            current_v -= learning_rate * grad_v
            current_u = np.clip(current_u, -2.5, 2.5)
            current_v = np.clip(current_v, -2.5, 2.5)
            current_z = loss_func(current_u, current_v)
            
            new_point = axes_3d.c2p(current_u, current_v, current_z)
            trajectory_points.append(new_point)
            
            self.play(
                ball.animate.move_to(new_point),
                run_time=0.25
            )
        
        # 绘制轨迹线
        trajectory = VMobject()
        trajectory.set_points_smoothly(trajectory_points)
        trajectory.set_stroke(PRIMARY_COLOR, width=2, opacity=0.6)
        self.play(Create(trajectory), run_time=0.5)
        
        # 到达山谷
        self.play(FadeOut(narration3))
        narration4 = Text(
            "找到了山谷！模型学到了东西",
            font_size=18, color=SECONDARY_COLOR
        )
        narration4.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(narration4)
        
        self.play(
            Write(narration4),
            Flash(ball.get_center(), color=SECONDARY_COLOR, line_length=0.3, num_lines=12),
            run_time=0.8
        )
        
        # 旋转相机展示
        self.begin_ambient_camera_rotation(rate=0.15)
        self.wait(2.5)
        self.stop_ambient_camera_rotation()
        
        # 核心洞察
        self.play(FadeOut(narration4))
        insight = Text(
            '目标：调整模型内部无数的"旋钮"（参数），让损失值降到最低',
            font_size=16, color=ACCENT_COLOR
        )
        insight.to_corner(DR, buff=0.5)
        self.add_fixed_in_frame_mobjects(insight)
        self.play(Write(insight), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理3D场景
        self.play(
            FadeOut(surface), FadeOut(axes_3d), FadeOut(ball),
            FadeOut(title), FadeOut(insight), FadeOut(trajectory),
            run_time=0.8
        )
        
        # 重置相机
        self.set_camera_orientation(phi=0, theta=-90 * DEGREES)
    
    # ============ 辅助方法 ============
    
    def create_flow_box(self, text, color, width=1.5):
        """创建流程框"""
        box = VGroup()
        rect = RoundedRectangle(
            width=width, height=0.6,
            corner_radius=0.1,
            color=color,
            fill_opacity=0.3
        )
        rect.set_stroke(color, width=2)
        
        label = Text(text, font_size=16, color=color)
        label.move_to(rect.get_center())
        
        box.add(rect, label)
        return box
    
    def create_paradigm_card(self, cn_name, en_name, desc, example, color, icon):
        """创建学习范式卡片"""
        card = VGroup()
        
        # 背景
        bg = RoundedRectangle(
            width=3.8, height=3.2,
            corner_radius=0.15,
            color=color,
            fill_opacity=0.15
        )
        bg.set_stroke(color, width=2)
        
        # 图标
        icon.scale(0.5)
        icon.move_to(bg.get_center() + UP * 0.9)
        
        # 中文名
        cn = Text(cn_name, font_size=24, color=color)
        cn.next_to(icon, DOWN, buff=0.2)
        
        # 英文名
        en = Text(en_name, font_size=12, color=SUBTEXT_COLOR)
        en.next_to(cn, DOWN, buff=0.1)
        
        # 描述
        description = Text(desc, font_size=14, color=TEXT_COLOR)
        description.next_to(en, DOWN, buff=0.2)
        
        # 例子
        example_text = Text(f"例: {example}", font_size=12, color=SUBTEXT_COLOR)
        example_text.next_to(description, DOWN, buff=0.15)
        
        card.add(bg, icon, cn, en, description, example_text)
        return card
    
    def create_supervised_icon(self):
        """创建监督学习图标（图片+标签）"""
        icon = VGroup()
        
        # 图片
        img = Square(side_length=0.6, color=PRIMARY_COLOR, fill_opacity=0.4)
        img.set_stroke(PRIMARY_COLOR, width=2)
        
        # 标签
        label = RoundedRectangle(
            width=0.5, height=0.25,
            corner_radius=0.05,
            color=SECONDARY_COLOR,
            fill_opacity=0.6
        )
        label.next_to(img, RIGHT, buff=0.1)
        
        # 箭头
        arrow = Arrow(
            img.get_right() + DOWN * 0.15,
            label.get_left() + DOWN * 0.15,
            buff=0.05, stroke_width=2, color=TEXT_COLOR
        )
        
        icon.add(img, label, arrow)
        return icon
    
    def create_unsupervised_icon(self):
        """创建无监督学习图标（聚类）"""
        icon = VGroup()
        
        # 多个点聚类
        np.random.seed(42)
        for i in range(2):
            cluster_center = LEFT * 0.3 if i == 0 else RIGHT * 0.3
            color = PRIMARY_COLOR if i == 0 else SECONDARY_COLOR
            for _ in range(4):
                dot = Dot(
                    point=cluster_center + np.array([
                        np.random.uniform(-0.2, 0.2),
                        np.random.uniform(-0.2, 0.2),
                        0
                    ]),
                    radius=0.06,
                    color=color
                )
                icon.add(dot)
        
        return icon
    
    def create_reinforcement_icon(self):
        """创建强化学习图标（智能体+环境）"""
        icon = VGroup()
        
        # 智能体
        agent = Circle(radius=0.2, color=NEURAL_COLOR, fill_opacity=0.6)
        agent.set_stroke(NEURAL_COLOR, width=2)
        agent.shift(LEFT * 0.3)
        
        # 环境（网格）
        env = VGroup()
        for i in range(2):
            for j in range(2):
                cell = Square(side_length=0.25, color=ACCENT_COLOR, fill_opacity=0.3)
                cell.set_stroke(ACCENT_COLOR, width=1)
                cell.move_to(RIGHT * 0.3 + np.array([i * 0.28 - 0.14, j * 0.28 - 0.14, 0]))
                env.add(cell)
        
        # 箭头（动作）
        arrow = Arrow(
            agent.get_right(),
            env.get_left(),
            buff=0.1, stroke_width=2, color=SECONDARY_COLOR
        )
        
        icon.add(agent, env, arrow)
        return icon
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = LearningParadigmsScene()
    scene.render()
