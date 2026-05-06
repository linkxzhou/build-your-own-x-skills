"""
场景2: 机器学习基础
展示训练集、模型、参数、损失四个核心概念

运行命令:
    manim -pql scene_02_ml_basics.py MLBasicsScene
    manim -pqh scene_02_ml_basics.py MLBasicsScene
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


class MLBasicsScene(Scene):
    """场景2: 机器学习基础概念"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 核心任务展示
        self.show_core_task()
        
        # 2. 四个核心概念
        self.show_four_concepts()
        
        # 3. 训练目标
        self.show_training_goal()
        
        self.clear_scene()
    
    def show_core_task(self):
        """展示机器学习的核心任务"""
        # 标题
        title = Text("机器学习的核心任务", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 猫狗图片网格
        images = VGroup()
        labels = ["猫", "狗", "猫", "狗", "猫", "狗"]
        colors = [PRIMARY_COLOR, SECONDARY_COLOR] * 3
        
        for i in range(6):
            # 简化的图片表示
            img = RoundedRectangle(
                width=1.2, height=1,
                corner_radius=0.1,
                color=colors[i],
                fill_opacity=0.3
            )
            img.set_stroke(colors[i], width=2)
            
            # 图片中的图标
            if labels[i] == "猫":
                icon = self.create_cat_icon().scale(0.5)
            else:
                icon = self.create_dog_icon().scale(0.5)
            icon.move_to(img.get_center())
            
            # 标签
            label = Text(labels[i], font_size=18, color=colors[i])
            label.next_to(img, DOWN, buff=0.1)
            
            images.add(VGroup(img, icon, label))
        
        images.arrange_in_grid(rows=2, cols=3, buff=0.4)
        images.next_to(title, DOWN, buff=0.6).shift(LEFT * 2)
        
        # 显示图片
        self.play(FadeIn(images, lag_ratio=0.1), run_time=1)
        
        # 箭头和模型
        arrow1 = Arrow(
            images.get_right() + RIGHT * 0.3,
            images.get_right() + RIGHT * 1.5,
            color=TEXT_COLOR,
            stroke_width=3
        )
        
        model_box = self.create_model_box()
        model_box.next_to(arrow1, RIGHT, buff=0.3)
        
        self.play(GrowArrow(arrow1), run_time=0.5)
        self.play(FadeIn(model_box, scale=0.8), run_time=0.5)
        
        # 学习过程
        learn_text = Text("学习规律", font_size=20, color=ACCENT_COLOR)
        learn_text.next_to(arrow1, UP, buff=0.1)
        self.play(Write(learn_text), run_time=0.3)
        
        self.wait(0.5)
        
        # 新图片测试
        new_img = RoundedRectangle(
            width=1.2, height=1,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.3
        )
        new_img.set_stroke(ACCENT_COLOR, width=2)
        new_icon = self.create_cat_icon().scale(0.5)
        new_icon.move_to(new_img.get_center())
        question = Text("?", font_size=28, color=ACCENT_COLOR)
        question.next_to(new_img, DOWN, buff=0.1)
        new_group = VGroup(new_img, new_icon, question)
        new_group.next_to(model_box, DOWN, buff=0.8)
        
        new_label = Text("新图片", font_size=18, color=SUBTEXT_COLOR)
        new_label.next_to(new_group, LEFT, buff=0.3)
        
        self.play(FadeIn(new_group), Write(new_label), run_time=0.5)
        
        # 预测结果
        arrow2 = Arrow(
            new_group.get_right(),
            new_group.get_right() + RIGHT * 1,
            color=SECONDARY_COLOR,
            stroke_width=3
        )
        
        result = Text("猫!", font_size=28, color=SECONDARY_COLOR)
        result.next_to(arrow2, RIGHT, buff=0.2)
        
        self.play(GrowArrow(arrow2), run_time=0.3)
        self.play(Write(result), run_time=0.3)
        
        # 强调
        self.play(
            Circumscribe(result, color=SECONDARY_COLOR),
            run_time=0.5
        )
        
        self.wait(1)
        
        # 总结
        summary = Text(
            "给机器看很多例子，让它自己总结规律",
            font_size=26, color=TEXT_COLOR
        )
        summary.to_edge(DOWN, buff=0.6)
        
        self.play(Write(summary), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=0.8
        )
    
    def show_four_concepts(self):
        """展示四个核心概念"""
        # 标题
        title = Text("四个核心概念", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        concepts = []
        
        # 1. 训练集
        training_set = self.create_concept_card(
            "训练集",
            "Training Set",
            "给机器学习的'例子'",
            PRIMARY_COLOR,
            self.create_dataset_icon()
        )
        concepts.append(training_set)
        
        # 2. 模型
        model = self.create_concept_card(
            "模型",
            "Model",
            "学习用的'数学公式'",
            NEURAL_COLOR,
            self.create_model_icon()
        )
        concepts.append(model)
        
        # 3. 参数
        params = self.create_concept_card(
            "参数",
            "Parameters",
            "模型内部的'旋钮'",
            SECONDARY_COLOR,
            self.create_params_icon()
        )
        concepts.append(params)
        
        # 4. 损失
        loss = self.create_concept_card(
            "损失",
            "Loss",
            "衡量'猜得有多差'",
            ERROR_COLOR,
            self.create_loss_icon()
        )
        concepts.append(loss)
        
        # 依次展示
        for i, concept in enumerate(concepts):
            # 定位
            if i < 2:
                row = 0
                col = i
            else:
                row = 1
                col = i - 2
            
            x_pos = (col - 0.5) * 4
            y_pos = -row * 2.5 + 0.5
            concept.move_to([x_pos, y_pos, 0])
            
            self.play(FadeIn(concept, scale=0.8), run_time=0.6)
            self.wait(0.3)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_training_goal(self):
        """展示训练目标"""
        # 标题
        title = Text("训练目标", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 损失仪表盘
        gauge = self.create_loss_gauge()
        gauge.shift(UP * 0.3)
        
        self.play(FadeIn(gauge), run_time=0.8)
        
        # 目标说明
        goal = Text("目标: 调整参数，把损失降到最低", font_size=28, color=TEXT_COLOR)
        goal.next_to(gauge, DOWN, buff=0.8)
        
        self.play(Write(goal), run_time=0.8)
        
        # 动画：损失下降
        pointer = gauge[1]  # 指针
        
        self.play(
            Rotate(pointer, angle=-PI * 0.6, about_point=gauge[0].get_center()),
            run_time=2
        )
        
        # 成功提示
        success = Text("损失降低 = 预测更准确!", font_size=26, color=SECONDARY_COLOR)
        success.next_to(goal, DOWN, buff=0.5)
        
        self.play(
            FadeIn(success, scale=1.2),
            Flash(gauge.get_center(), color=SECONDARY_COLOR),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 公式展示
        formula_title = Text("感知机公式:", font_size=24, color=SUBTEXT_COLOR)
        formula_title.to_edge(DOWN, buff=1.2)
        
        formula = MathTex(
            r"y = f\left(\sum_{i=1}^{n} w_i x_i + b\right)",
            font_size=32
        )
        formula.next_to(formula_title, DOWN, buff=0.2)
        
        self.play(Write(formula_title), Write(formula), run_time=1)
        self.wait(1.5)
    
    # ============ 辅助方法 ============
    
    def create_cat_icon(self):
        """创建猫图标"""
        cat = VGroup()
        
        # 头
        head = Circle(radius=0.3, color=PRIMARY_COLOR, fill_opacity=0.6)
        
        # 耳朵
        ear_left = Polygon(
            [-0.25, 0.2, 0], [-0.15, 0.45, 0], [-0.05, 0.2, 0],
            color=PRIMARY_COLOR, fill_opacity=0.6
        )
        ear_right = ear_left.copy().shift(RIGHT * 0.3)
        
        # 眼睛
        eye_left = Circle(radius=0.05, color=BG_COLOR, fill_opacity=1)
        eye_left.move_to(head.get_center() + LEFT * 0.1 + UP * 0.05)
        eye_right = eye_left.copy().shift(RIGHT * 0.2)
        
        # 胡须
        whisker1 = Line(LEFT * 0.15, LEFT * 0.35, stroke_width=1, color=PRIMARY_COLOR)
        whisker2 = whisker1.copy().rotate(PI / 8, about_point=whisker1.get_start())
        whisker3 = whisker1.copy().rotate(-PI / 8, about_point=whisker1.get_start())
        whiskers_left = VGroup(whisker1, whisker2, whisker3)
        whiskers_left.shift(DOWN * 0.05)
        
        whiskers_right = whiskers_left.copy()
        whiskers_right.rotate(PI, about_point=ORIGIN)
        
        cat.add(head, ear_left, ear_right, eye_left, eye_right, whiskers_left, whiskers_right)
        return cat
    
    def create_dog_icon(self):
        """创建狗图标"""
        dog = VGroup()
        
        # 头
        head = Circle(radius=0.3, color=SECONDARY_COLOR, fill_opacity=0.6)
        
        # 耳朵（下垂）
        ear_left = Ellipse(width=0.15, height=0.25, color=SECONDARY_COLOR, fill_opacity=0.7)
        ear_left.move_to(head.get_left() + DOWN * 0.1 + LEFT * 0.05)
        ear_right = ear_left.copy()
        ear_right.move_to(head.get_right() + DOWN * 0.1 + RIGHT * 0.05)
        
        # 眼睛
        eye_left = Circle(radius=0.05, color=BG_COLOR, fill_opacity=1)
        eye_left.move_to(head.get_center() + LEFT * 0.1 + UP * 0.05)
        eye_right = eye_left.copy().shift(RIGHT * 0.2)
        
        # 鼻子
        nose = Circle(radius=0.05, color=BG_COLOR, fill_opacity=1)
        nose.move_to(head.get_center() + DOWN * 0.1)
        
        dog.add(head, ear_left, ear_right, eye_left, eye_right, nose)
        return dog
    
    def create_model_box(self):
        """创建模型黑盒"""
        model = VGroup()
        
        # 主体
        box = RoundedRectangle(
            width=1.8, height=1.4,
            corner_radius=0.15,
            color=NEURAL_COLOR,
            fill_opacity=0.3
        )
        box.set_stroke(NEURAL_COLOR, width=2)
        
        # 齿轮图标
        gear = self.create_gear_icon().scale(0.4)
        gear.move_to(box.get_center())
        
        # 标签
        label = Text("模型", font_size=18, color=NEURAL_COLOR)
        label.next_to(box, DOWN, buff=0.1)
        
        model.add(box, gear, label)
        return model
    
    def create_gear_icon(self):
        """创建齿轮图标"""
        gear = VGroup()
        
        # 中心圆
        center = Circle(radius=0.3, color=NEURAL_COLOR, fill_opacity=0.5)
        
        # 齿
        for i in range(8):
            angle = i * PI / 4
            tooth = Rectangle(
                width=0.15, height=0.25,
                color=NEURAL_COLOR,
                fill_opacity=0.5
            )
            tooth.move_to(center.get_center() + 0.4 * np.array([np.cos(angle), np.sin(angle), 0]))
            tooth.rotate(angle)
            gear.add(tooth)
        
        # 中心小圆
        inner = Circle(radius=0.1, color=BG_COLOR, fill_opacity=1)
        
        gear.add(center, inner)
        return gear
    
    def create_concept_card(self, cn_name, en_name, desc, color, icon):
        """创建概念卡片"""
        card = VGroup()
        
        # 背景
        bg = RoundedRectangle(
            width=3.5, height=2.2,
            corner_radius=0.15,
            color=color,
            fill_opacity=0.1
        )
        bg.set_stroke(color, width=2)
        
        # 图标
        icon.scale(0.6)
        icon.move_to(bg.get_center() + UP * 0.4)
        
        # 中文名
        cn = Text(cn_name, font_size=26, color=color)
        cn.next_to(icon, DOWN, buff=0.2)
        
        # 英文名
        en = Text(en_name, font_size=16, color=SUBTEXT_COLOR)
        en.next_to(cn, DOWN, buff=0.1)
        
        # 描述
        description = Text(desc, font_size=16, color=TEXT_COLOR)
        description.next_to(en, DOWN, buff=0.15)
        
        card.add(bg, icon, cn, en, description)
        return card
    
    def create_dataset_icon(self):
        """创建数据集图标"""
        icon = VGroup()
        
        # 多个小方块表示数据
        for i in range(3):
            for j in range(3):
                rect = Square(side_length=0.25, color=PRIMARY_COLOR, fill_opacity=0.5)
                rect.move_to([i * 0.3 - 0.3, j * 0.3 - 0.3, 0])
                icon.add(rect)
        
        return icon
    
    def create_model_icon(self):
        """创建模型图标"""
        return self.create_gear_icon()
    
    def create_params_icon(self):
        """创建参数图标（滑块）"""
        icon = VGroup()
        
        for i in range(3):
            # 滑轨
            track = Line(
                LEFT * 0.4, RIGHT * 0.4,
                color=SECONDARY_COLOR, stroke_width=2
            )
            track.shift(DOWN * i * 0.25)
            
            # 滑块
            slider = Circle(
                radius=0.08, color=SECONDARY_COLOR, fill_opacity=0.8
            )
            slider.move_to(track.point_from_proportion(0.3 + i * 0.2))
            
            icon.add(track, slider)
        
        return icon
    
    def create_loss_icon(self):
        """创建损失图标（仪表盘）"""
        icon = VGroup()
        
        # 半圆
        arc = Arc(
            radius=0.4, start_angle=PI, angle=PI,
            color=ERROR_COLOR, stroke_width=3
        )
        
        # 刻度
        for i in range(5):
            angle = PI - i * PI / 4
            tick_start = 0.35 * np.array([np.cos(angle), np.sin(angle), 0])
            tick_end = 0.45 * np.array([np.cos(angle), np.sin(angle), 0])
            tick = Line(tick_start, tick_end, color=ERROR_COLOR, stroke_width=2)
            icon.add(tick)
        
        # 指针
        pointer = Arrow(
            ORIGIN, UP * 0.3 + RIGHT * 0.1,
            color=ERROR_COLOR, stroke_width=2,
            buff=0
        )
        
        icon.add(arc, pointer)
        return icon
    
    def create_loss_gauge(self):
        """创建损失仪表盘（大版本）"""
        gauge = VGroup()
        
        # 半圆底座
        arc = Arc(
            radius=2, start_angle=PI, angle=PI,
            color=TEXT_COLOR, stroke_width=4
        )
        
        # 颜色渐变区域
        for i in range(10):
            angle = PI - i * PI / 10
            next_angle = PI - (i + 1) * PI / 10
            sector = AnnularSector(
                inner_radius=1.5, outer_radius=2,
                angle=PI / 10, start_angle=next_angle,
                color=interpolate_color(ManimColor(SECONDARY_COLOR), ManimColor(ERROR_COLOR), i / 10),
                fill_opacity=0.6
            )
            gauge.add(sector)
        
        # 刻度
        for i in range(11):
            angle = PI - i * PI / 10
            tick_start = 2.1 * np.array([np.cos(angle), np.sin(angle), 0])
            tick_end = 2.3 * np.array([np.cos(angle), np.sin(angle), 0])
            tick = Line(tick_start, tick_end, color=TEXT_COLOR, stroke_width=2)
            gauge.add(tick)
        
        gauge.add(arc)
        
        # 指针
        pointer = Arrow(
            ORIGIN, UP * 1.4 + RIGHT * 1,
            color=ACCENT_COLOR, stroke_width=4,
            buff=0
        )
        pointer.rotate(-PI / 6, about_point=ORIGIN)
        
        # 中心点
        center = Circle(radius=0.15, color=ACCENT_COLOR, fill_opacity=1)
        
        gauge.add(pointer, center)
        
        # 标签
        high_label = Text("高", font_size=20, color=ERROR_COLOR)
        high_label.move_to([2.5, 0.3, 0])
        
        low_label = Text("低", font_size=20, color=SECONDARY_COLOR)
        low_label.move_to([-2.5, 0.3, 0])
        
        loss_label = Text("损失", font_size=24, color=TEXT_COLOR)
        loss_label.move_to([0, -0.5, 0])
        
        gauge.add(high_label, low_label, loss_label)
        
        return gauge
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = MLBasicsScene()
    scene.render()
