"""
场景3: 过拟合与数据集划分
用学生考试类比解释过拟合，展示训练/验证/测试集划分

运行命令:
    manim -pql scene_03_overfitting.py OverfittingScene
    manim -pqh scene_03_overfitting.py OverfittingScene
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

TRAIN_COLOR = "#00D4FF"        # 训练集颜色
VAL_COLOR = "#FFD700"          # 验证集颜色
TEST_COLOR = "#FF6B6B"         # 测试集颜色


class OverfittingScene(Scene):
    """场景3: 过拟合与数据集划分"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入：这里有个大坑
        self.show_warning()
        
        # 2. 过拟合类比
        self.show_overfitting_analogy()
        
        # 3. 数据集划分
        self.show_dataset_split()
        
        # 4. 总结
        self.show_summary()
        
        self.clear_scene()
    
    def show_warning(self):
        """引入警告"""
        # 警告图标
        warning = VGroup()
        
        triangle = Triangle(color=ACCENT_COLOR, fill_opacity=0.3)
        triangle.set_stroke(ACCENT_COLOR, width=3)
        triangle.scale(1.5)
        
        exclamation = Text("!", font_size=48, color=ACCENT_COLOR)
        exclamation.move_to(triangle.get_center())
        
        warning.add(triangle, exclamation)
        
        self.play(
            FadeIn(warning, scale=1.5),
            run_time=0.8
        )
        self.play(
            warning.animate.scale(0.8).to_edge(UP, buff=1),
            run_time=0.5
        )
        
        # 警告文字
        text = Text("不过，这里有个大坑...", font_size=40, color=ACCENT_COLOR)
        text.next_to(warning, DOWN, buff=0.5)
        
        self.play(Write(text), run_time=0.8)
        
        # 过拟合
        overfit_text = Text("过拟合 (Overfitting)", font_size=48, color=ERROR_COLOR)
        overfit_text.next_to(text, DOWN, buff=0.8)
        
        self.play(
            FadeIn(overfit_text, scale=1.2),
            Flash(overfit_text.get_center(), color=ERROR_COLOR),
            run_time=0.8
        )
        
        self.wait(1.5)
        
        # 清理
        self.play(
            FadeOut(warning), FadeOut(text), FadeOut(overfit_text),
            run_time=0.5
        )
    
    def show_overfitting_analogy(self):
        """过拟合类比：学生死记硬背"""
        # 标题
        title = Text("什么是过拟合？", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 学生形象
        student = self.create_student()
        student.move_to(LEFT * 4 + DOWN * 0.5)
        
        self.play(FadeIn(student), run_time=0.5)
        
        # 题库
        book = self.create_book("五年高考\n三年模拟")
        book.next_to(student, RIGHT, buff=0.5)
        
        self.play(FadeIn(book), run_time=0.5)
        
        # 步骤1: 死记硬背
        step1 = Text("死记硬背每道题的答案", font_size=24, color=TEXT_COLOR)
        step1.to_edge(DOWN, buff=1.5)
        
        self.play(Write(step1), run_time=0.5)
        
        # 动画：答案飞入学生脑中
        answers = VGroup()
        for i in range(5):
            ans = Text(f"答案{i+1}", font_size=16, color=PRIMARY_COLOR)
            ans.move_to(book.get_center())
            answers.add(ans)
        
        self.play(FadeIn(answers, lag_ratio=0.1), run_time=0.3)
        
        for ans in answers:
            self.play(
                ans.animate.move_to(student.get_center() + UP * 0.3),
                run_time=0.2
            )
            self.play(FadeOut(ans, scale=0.5), run_time=0.1)
        
        # 训练集表现
        train_result = VGroup(
            Text("训练题目:", font_size=20, color=SUBTEXT_COLOR),
            Text("100分!", font_size=28, color=SECONDARY_COLOR),
        ).arrange(RIGHT, buff=0.3)
        train_result.next_to(student, DOWN, buff=0.8)
        
        self.play(FadeIn(train_result), run_time=0.5)
        self.wait(0.5)
        
        # 步骤2: 新题型
        self.play(FadeOut(step1))
        step2 = Text("考试出了新题型...", font_size=24, color=ERROR_COLOR)
        step2.to_edge(DOWN, buff=1.5)
        
        self.play(Write(step2), run_time=0.5)
        
        # 新试卷
        new_exam = self.create_book("高考真题\n(新题型)")
        new_exam[0].set_color(ERROR_COLOR)
        new_exam.move_to(RIGHT * 2 + DOWN * 0.5)
        
        self.play(FadeIn(new_exam, shift=LEFT), run_time=0.5)
        
        # 傻眼动画
        confused = Text("???", font_size=36, color=ERROR_COLOR)
        confused.next_to(student, UP, buff=0.3)
        
        self.play(
            FadeIn(confused),
            student.animate.shift(DOWN * 0.1),
            run_time=0.5
        )
        
        # 测试集表现
        test_result = VGroup(
            Text("新题目:", font_size=20, color=SUBTEXT_COLOR),
            Text("30分...", font_size=28, color=ERROR_COLOR),
        ).arrange(RIGHT, buff=0.3)
        test_result.next_to(train_result, DOWN, buff=0.3)
        
        self.play(FadeIn(test_result), run_time=0.5)
        self.wait(1)
        
        # 总结
        self.play(
            FadeOut(step2), FadeOut(confused),
            FadeOut(book), FadeOut(new_exam),
        )
        
        conclusion = VGroup(
            Text("'记住'了题目", font_size=24, color=ERROR_COLOR),
            Text("≠", font_size=28, color=TEXT_COLOR),
            Text("'理解'了知识", font_size=24, color=SECONDARY_COLOR),
        ).arrange(RIGHT, buff=0.3)
        conclusion.next_to(test_result, DOWN, buff=0.6)
        
        self.play(Write(conclusion), run_time=0.8)
        
        # 定义
        definition = VGroup(
            Text("过拟合:", font_size=24, color=ACCENT_COLOR),
            Text("模型在训练集上表现完美", font_size=20, color=TEXT_COLOR),
            Text("但对新数据一塌糊涂", font_size=20, color=ERROR_COLOR),
        ).arrange(DOWN, buff=0.15)
        definition.to_edge(RIGHT, buff=1)
        
        box = SurroundingRectangle(definition, color=ACCENT_COLOR, buff=0.2)
        
        self.play(Write(definition), Create(box), run_time=1)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_dataset_split(self):
        """数据集划分"""
        # 标题
        title = Text("解决方案：数据集划分", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 数据条
        data_bar = Rectangle(
            width=10, height=0.8,
            color=TEXT_COLOR,
            fill_opacity=0.3
        )
        data_bar.set_stroke(TEXT_COLOR, width=2)
        
        self.play(Create(data_bar), run_time=0.5)
        
        # 三个部分
        train_part = Rectangle(
            width=6, height=0.8,
            color=TRAIN_COLOR,
            fill_opacity=0.6
        )
        train_part.set_stroke(TRAIN_COLOR, width=2)
        train_part.align_to(data_bar, LEFT)
        
        val_part = Rectangle(
            width=2, height=0.8,
            color=VAL_COLOR,
            fill_opacity=0.6
        )
        val_part.set_stroke(VAL_COLOR, width=2)
        val_part.next_to(train_part, RIGHT, buff=0)
        
        test_part = Rectangle(
            width=2, height=0.8,
            color=TEST_COLOR,
            fill_opacity=0.6
        )
        test_part.set_stroke(TEST_COLOR, width=2)
        test_part.next_to(val_part, RIGHT, buff=0)
        
        # 动画：分割
        self.play(
            ReplacementTransform(data_bar.copy(), train_part),
            run_time=0.5
        )
        self.play(
            FadeIn(val_part, shift=LEFT * 0.3),
            run_time=0.3
        )
        self.play(
            FadeIn(test_part, shift=LEFT * 0.3),
            run_time=0.3
        )
        
        self.play(FadeOut(data_bar))
        
        parts = VGroup(train_part, val_part, test_part)
        
        # 标签和百分比
        train_label = Text("训练集 60%", font_size=20, color=TRAIN_COLOR)
        train_label.next_to(train_part, DOWN, buff=0.2)
        
        val_label = Text("验证集 20%", font_size=20, color=VAL_COLOR)
        val_label.next_to(val_part, DOWN, buff=0.2)
        
        test_label = Text("测试集 20%", font_size=20, color=TEST_COLOR)
        test_label.next_to(test_part, DOWN, buff=0.2)
        
        self.play(
            Write(train_label), Write(val_label), Write(test_label),
            run_time=0.5
        )
        
        # 移动到上方
        all_bar = VGroup(parts, train_label, val_label, test_label)
        self.play(all_bar.animate.shift(UP * 1.5), run_time=0.5)
        
        # 详细说明
        explanations = VGroup()
        
        # 训练集说明
        train_exp = VGroup(
            self.create_book_icon(TRAIN_COLOR),
            Text("训练集", font_size=24, color=TRAIN_COLOR),
            Text("课本和习题", font_size=18, color=TEXT_COLOR),
            Text("用于学习", font_size=16, color=SUBTEXT_COLOR),
        )
        train_exp[0].scale(0.5)
        train_exp.arrange(DOWN, buff=0.15)
        
        # 验证集说明
        val_exp = VGroup(
            self.create_exam_icon(VAL_COLOR),
            Text("验证集", font_size=24, color=VAL_COLOR),
            Text("模拟考卷", font_size=18, color=TEXT_COLOR),
            Text("调整学习方法", font_size=16, color=SUBTEXT_COLOR),
        )
        val_exp[0].scale(0.5)
        val_exp.arrange(DOWN, buff=0.15)
        
        # 测试集说明
        test_exp = VGroup(
            self.create_exam_icon(TEST_COLOR),
            Text("测试集", font_size=24, color=TEST_COLOR),
            Text("高考试卷", font_size=18, color=TEXT_COLOR),
            Text("最终评估前不能看!", font_size=16, color=ERROR_COLOR),
        )
        test_exp[0].scale(0.5)
        test_exp.arrange(DOWN, buff=0.15)
        
        explanations.add(train_exp, val_exp, test_exp)
        explanations.arrange(RIGHT, buff=1.5)
        explanations.next_to(all_bar, DOWN, buff=0.8)
        
        for exp in explanations:
            self.play(FadeIn(exp, scale=0.8), run_time=0.5)
        
        self.wait(1.5)
        
        # 关键提示
        warning = VGroup(
            Text("⚠️", font_size=24),
            Text("测试集绝不能用于训练或调参!", font_size=22, color=ERROR_COLOR),
        ).arrange(RIGHT, buff=0.2)
        warning.to_edge(DOWN, buff=0.8)
        
        self.play(Write(warning), run_time=0.8)
        self.wait(1.5)
    
    def show_summary(self):
        """总结"""
        # 清理之前的内容
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
        
        # 标题
        title = Text("关键洞察", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 核心观点
        points = VGroup(
            Text("1. 过拟合 = 只记住答案，没有真正理解", font_size=24, color=TEXT_COLOR),
            Text("2. 用验证集检测过拟合，调整学习策略", font_size=24, color=TEXT_COLOR),
            Text("3. 测试集是最终考验，训练时绝不能看", font_size=24, color=TEXT_COLOR),
        )
        points.arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        points.next_to(title, DOWN, buff=0.8)
        
        for point in points:
            self.play(Write(point), run_time=0.6)
        
        self.wait(0.5)
        
        # 核心思想
        insight = VGroup(
            Text("深度学习核心思想:", font_size=28, color=ACCENT_COLOR),
            Text("优秀的模型不仅需要强大的计算能力", font_size=24, color=TEXT_COLOR),
            Text("更需要巧妙的设计来防止'学傻了'", font_size=24, color=SECONDARY_COLOR),
        )
        insight.arrange(DOWN, buff=0.2)
        insight.next_to(points, DOWN, buff=0.8)
        
        box = SurroundingRectangle(insight, color=ACCENT_COLOR, buff=0.3, corner_radius=0.1)
        
        self.play(Write(insight), Create(box), run_time=1.2)
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_student(self):
        """创建学生形象"""
        student = VGroup()
        
        # 身体
        body = RoundedRectangle(
            width=0.8, height=1.2,
            corner_radius=0.1,
            color=PRIMARY_COLOR,
            fill_opacity=0.5
        )
        
        # 头
        head = Circle(radius=0.35, color=PRIMARY_COLOR, fill_opacity=0.5)
        head.next_to(body, UP, buff=-0.05)
        
        # 眼睛
        eye_left = Circle(radius=0.05, color=BG_COLOR, fill_opacity=1)
        eye_left.move_to(head.get_center() + LEFT * 0.1 + UP * 0.05)
        eye_right = eye_left.copy().shift(RIGHT * 0.2)
        
        # 嘴巴
        mouth = Arc(radius=0.1, angle=-PI / 2, color=BG_COLOR, stroke_width=2)
        mouth.move_to(head.get_center() + DOWN * 0.1)
        
        student.add(body, head, eye_left, eye_right, mouth)
        return student
    
    def create_book(self, text):
        """创建书本形象"""
        book = VGroup()
        
        # 书本主体
        cover = RoundedRectangle(
            width=1.5, height=2,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.3
        )
        cover.set_stroke(ACCENT_COLOR, width=2)
        
        # 书脊
        spine = Line(
            cover.get_corner(UL) + RIGHT * 0.2,
            cover.get_corner(DL) + RIGHT * 0.2,
            color=ACCENT_COLOR,
            stroke_width=2
        )
        
        # 书名
        title = Text(text, font_size=14, color=TEXT_COLOR)
        title.move_to(cover.get_center())
        
        book.add(cover, spine, title)
        return book
    
    def create_book_icon(self, color):
        """创建书本图标"""
        icon = VGroup()
        
        # 书本
        book = RoundedRectangle(
            width=0.8, height=1,
            corner_radius=0.05,
            color=color,
            fill_opacity=0.4
        )
        book.set_stroke(color, width=2)
        
        # 书页
        for i in range(3):
            page = Line(
                book.get_left() + RIGHT * 0.15 + UP * (0.3 - i * 0.2),
                book.get_right() + LEFT * 0.15 + UP * (0.3 - i * 0.2),
                color=color,
                stroke_width=1
            )
            icon.add(page)
        
        icon.add(book)
        return icon
    
    def create_exam_icon(self, color):
        """创建试卷图标"""
        icon = VGroup()
        
        # 试卷
        paper = RoundedRectangle(
            width=0.7, height=1,
            corner_radius=0.03,
            color=color,
            fill_opacity=0.3
        )
        paper.set_stroke(color, width=2)
        
        # 文字行
        for i in range(4):
            line = Line(
                paper.get_left() + RIGHT * 0.1 + UP * (0.3 - i * 0.15),
                paper.get_right() + LEFT * 0.1 + UP * (0.3 - i * 0.15),
                color=color,
                stroke_width=1
            )
            icon.add(line)
        
        # 勾选框
        checkbox = Square(side_length=0.12, color=color, stroke_width=1)
        checkbox.move_to(paper.get_corner(DR) + UL * 0.2)
        
        icon.add(paper, checkbox)
        return icon
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = OverfittingScene()
    scene.render()
