"""
场景9: 应用场景
展示深度学习的预测和合成任务

运行命令:
    manim -pql scene_09_applications.py ApplicationsScene
    manim -pqh scene_09_applications.py ApplicationsScene
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


class ApplicationsScene(Scene):
    """场景9: 应用场景"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入
        self.show_intro()
        
        # 2. 预测类任务
        self.show_prediction_tasks()
        
        # 3. 合成类任务
        self.show_generation_tasks()
        
        self.clear_scene()
    
    def show_intro(self):
        """引入"""
        # 标题
        title = Text("第六部分：大展身手", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("深度学习在做什么？", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        # 两大类
        categories = VGroup()
        
        # 预测
        predict_box = RoundedRectangle(
            width=4, height=2,
            corner_radius=0.2,
            color=PRIMARY_COLOR,
            fill_opacity=0.3
        )
        predict_box.set_stroke(PRIMARY_COLOR, width=2)
        
        predict_title = Text("预测", font_size=28, color=PRIMARY_COLOR)
        predict_desc = Text("给输入，让它猜答案", font_size=18, color=TEXT_COLOR)
        predict_title.move_to(predict_box.get_center() + UP * 0.3)
        predict_desc.next_to(predict_title, DOWN, buff=0.2)
        
        predict_group = VGroup(predict_box, predict_title, predict_desc)
        
        # 合成
        gen_box = RoundedRectangle(
            width=4, height=2,
            corner_radius=0.2,
            color=SECONDARY_COLOR,
            fill_opacity=0.3
        )
        gen_box.set_stroke(SECONDARY_COLOR, width=2)
        
        gen_title = Text("合成", font_size=28, color=SECONDARY_COLOR)
        gen_desc = Text("让它创造新东西", font_size=18, color=TEXT_COLOR)
        gen_title.move_to(gen_box.get_center() + UP * 0.3)
        gen_desc.next_to(gen_title, DOWN, buff=0.2)
        
        gen_group = VGroup(gen_box, gen_title, gen_desc)
        
        categories.add(predict_group, gen_group)
        categories.arrange(RIGHT, buff=1.5)
        categories.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(FadeIn(categories, lag_ratio=0.3), run_time=1)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_prediction_tasks(self):
        """预测类任务展示"""
        # 标题
        title = Text("预测类任务", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 1. 图像分类
        self.show_image_classification(title)
        
        # 2. 目标检测
        self.show_object_detection(title)
        
        # 3. 其他任务简介
        self.show_other_prediction_tasks(title)
    
    def show_image_classification(self, title):
        """图像分类展示"""
        # 子标题
        subtitle = Text("1. 图像分类", font_size=28, color=ACCENT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.3)
        
        # 图片
        img = self.create_cat_image()
        img.move_to(LEFT * 3)
        
        # 模型
        model = RoundedRectangle(
            width=1.5, height=1,
            corner_radius=0.15,
            color=NEURAL_COLOR,
            fill_opacity=0.4
        )
        model.set_stroke(NEURAL_COLOR, width=2)
        model_text = Text("CNN/ViT", font_size=14, color=TEXT_COLOR)
        model_text.move_to(model.get_center())
        model_group = VGroup(model, model_text)
        
        # 输出
        output = VGroup()
        classes = [("猫", 0.92), ("狗", 0.05), ("鸟", 0.03)]
        
        for i, (name, prob) in enumerate(classes):
            bar = Rectangle(
                width=prob * 3, height=0.3,
                color=SECONDARY_COLOR if i == 0 else SUBTEXT_COLOR,
                fill_opacity=0.7 if i == 0 else 0.3
            )
            bar.align_to(ORIGIN, LEFT)
            bar.shift(DOWN * i * 0.5)
            
            label = Text(f"{name}: {prob:.0%}", font_size=14, color=TEXT_COLOR)
            label.next_to(bar, LEFT, buff=0.2)
            
            output.add(VGroup(bar, label))
        
        output.move_to(RIGHT * 3)
        
        # 箭头
        arrow1 = Arrow(
            img.get_right(), model.get_left(),
            buff=0.2, stroke_width=2, color=TEXT_COLOR
        )
        arrow2 = Arrow(
            model.get_right(), output.get_left() + LEFT * 0.5,
            buff=0.2, stroke_width=2, color=TEXT_COLOR
        )
        
        self.play(FadeIn(img), run_time=0.3)
        self.play(GrowArrow(arrow1), FadeIn(model_group), run_time=0.3)
        self.play(GrowArrow(arrow2), FadeIn(output), run_time=0.5)
        
        self.wait(1)
        
        # 清理当前内容
        self.play(
            FadeOut(img), FadeOut(arrow1), FadeOut(model_group),
            FadeOut(arrow2), FadeOut(output), FadeOut(subtitle),
            run_time=0.5
        )
    
    def show_object_detection(self, title):
        """目标检测展示"""
        subtitle = Text("2. 目标检测", font_size=28, color=ACCENT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.3)
        
        # 图片背景
        img_bg = Rectangle(
            width=5, height=3.5,
            color=SUBTEXT_COLOR,
            fill_opacity=0.2
        )
        img_bg.set_stroke(SUBTEXT_COLOR, width=1)
        img_bg.shift(DOWN * 0.5)
        
        self.play(FadeIn(img_bg), run_time=0.3)
        
        # 检测框
        detections = [
            (LEFT * 1.5 + UP * 0.3, 1.2, 1.5, "人", PRIMARY_COLOR),
            (RIGHT * 1 + DOWN * 0.5, 1.5, 1, "车", SECONDARY_COLOR),
            (RIGHT * 1.8 + UP * 0.5, 0.6, 0.6, "狗", ACCENT_COLOR),
        ]
        
        boxes = VGroup()
        for pos, w, h, label, color in detections:
            box = Rectangle(width=w, height=h, color=color, stroke_width=3)
            box.move_to(pos)
            
            label_bg = Rectangle(
                width=0.6, height=0.3,
                color=color, fill_opacity=0.8
            )
            label_bg.next_to(box, UP, buff=0, aligned_edge=LEFT)
            
            label_text = Text(label, font_size=14, color=BG_COLOR)
            label_text.move_to(label_bg.get_center())
            
            boxes.add(VGroup(box, label_bg, label_text))
        
        for box in boxes:
            self.play(FadeIn(box, scale=1.1), run_time=0.3)
        
        # 说明
        desc = Text(
            "不仅知道是什么，还知道在哪 (YOLO, SSD)",
            font_size=18, color=SUBTEXT_COLOR
        )
        desc.to_edge(DOWN, buff=0.6)
        
        self.play(Write(desc), run_time=0.5)
        
        self.wait(1)
        
        # 清理
        self.play(
            FadeOut(img_bg), FadeOut(boxes), FadeOut(subtitle), FadeOut(desc),
            run_time=0.5
        )
    
    def show_other_prediction_tasks(self, title):
        """其他预测任务简介"""
        subtitle = Text("更多预测任务", font_size=28, color=ACCENT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.3)
        
        # 任务列表
        tasks = VGroup(
            self.create_task_card("语义分割", "给每个像素打标签", PRIMARY_COLOR),
            self.create_task_card("语音识别", "声音 → 文字", SECONDARY_COLOR),
            self.create_task_card("强化学习", "AlphaGo, 走迷宫", NEURAL_COLOR),
        )
        tasks.arrange(RIGHT, buff=0.8)
        tasks.next_to(subtitle, DOWN, buff=0.6)
        
        self.play(FadeIn(tasks, lag_ratio=0.2), run_time=0.8)
        
        # 强化学习类比
        rl_desc = Text(
            "强化学习: 通过试错学习策略 - 像训练小鼠走迷宫找奶酪",
            font_size=18, color=SUBTEXT_COLOR
        )
        rl_desc.to_edge(DOWN, buff=0.6)
        
        self.play(Write(rl_desc), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_generation_tasks(self):
        """合成类任务展示"""
        # 标题
        title = Text("合成类任务", font_size=36, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 1. 文本生成
        self.show_text_generation(title)
        
        # 2. 图像生成
        self.show_image_generation(title)
    
    def show_text_generation(self, title):
        """文本生成展示"""
        subtitle = Text("1. 文本生成 (GPT)", font_size=28, color=ACCENT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.3)
        
        # 自回归过程演示
        prompt = Text("从前有一个", font_size=24, color=PRIMARY_COLOR)
        prompt.move_to(UP * 0.5 + LEFT * 2)
        
        self.play(Write(prompt), run_time=0.5)
        
        # 逐词生成
        words = ["小", "王", "子", "，", "他", "..."]
        current_text = "从前有一个"
        
        for word in words:
            new_word = Text(word, font_size=24, color=SECONDARY_COLOR)
            current_end = prompt.get_right() + RIGHT * 0.1
            new_word.next_to(prompt, RIGHT, buff=0.1)
            
            self.play(
                FadeIn(new_word, shift=UP * 0.2),
                run_time=0.3
            )
            
            # 更新 prompt 组
            prompt = VGroup(prompt, new_word)
            
            self.wait(0.2)
        
        # 自回归说明
        ar_desc = VGroup(
            Text("自回归:", font_size=20, color=ACCENT_COLOR),
            Text("每次预测下一个词", font_size=18, color=TEXT_COLOR),
            Text("把新词加入输入", font_size=18, color=TEXT_COLOR),
            Text("再预测下一个...", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        ar_desc.move_to(DOWN * 1.5)
        
        self.play(Write(ar_desc), run_time=0.8)
        
        # 应用
        apps = Text(
            "应用: 故事、代码、邮件、对话...",
            font_size=18, color=SUBTEXT_COLOR
        )
        apps.to_edge(DOWN, buff=0.6)
        
        self.play(Write(apps), run_time=0.5)
        
        self.wait(1)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects if m != title], run_time=0.5)
        self.add(title)
    
    def show_image_generation(self, title):
        """图像生成展示"""
        subtitle = Text("2. 图像生成 (DALL-E, Stable Diffusion)", font_size=26, color=ACCENT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.3)
        
        # 文字描述
        prompt_text = Text(
            '"一只戴墨镜的猫在沙滩上"',
            font_size=22, color=PRIMARY_COLOR
        )
        prompt_text.next_to(subtitle, DOWN, buff=0.5)
        
        self.play(Write(prompt_text), run_time=0.5)
        
        # 扩散过程
        # 噪声 → 图像
        noise_img = self.create_noise_image()
        noise_img.move_to(LEFT * 3 + DOWN * 0.5)
        noise_label = Text("随机噪声", font_size=14, color=SUBTEXT_COLOR)
        noise_label.next_to(noise_img, DOWN, buff=0.1)
        
        self.play(FadeIn(noise_img), Write(noise_label), run_time=0.5)
        
        # 箭头
        arrows = VGroup()
        for i in range(3):
            arrow = Arrow(
                LEFT * (1.5 - i * 1.5) + DOWN * 0.5,
                LEFT * (0.5 - i * 1.5) + DOWN * 0.5,
                buff=0.1, stroke_width=2, color=TEXT_COLOR
            )
            arrows.add(arrow)
        
        # 中间状态
        mid_imgs = VGroup()
        opacities = [0.7, 0.4, 0.1]
        for i, opacity in enumerate(opacities):
            mid_img = self.create_partially_denoised(opacity)
            mid_img.move_to(LEFT * (1.5 - i * 1.5) + DOWN * 0.5)
            mid_imgs.add(mid_img)
        
        # 最终图像
        final_img = self.create_cat_beach_image()
        final_img.move_to(RIGHT * 2.5 + DOWN * 0.5)
        final_label = Text("生成图像", font_size=14, color=SECONDARY_COLOR)
        final_label.next_to(final_img, DOWN, buff=0.1)
        
        # 动画
        for i in range(3):
            self.play(
                GrowArrow(arrows[i]),
                FadeIn(mid_imgs[i]),
                run_time=0.4
            )
        
        self.play(
            FadeIn(final_img, scale=1.1),
            Write(final_label),
            run_time=0.5
        )
        
        # 扩散模型说明
        diffusion_desc = Text(
            "扩散模型: 逐步将噪声'去噪'成清晰图片",
            font_size=18, color=TEXT_COLOR
        )
        diffusion_desc.to_edge(DOWN, buff=0.6)
        
        self.play(Write(diffusion_desc), run_time=0.6)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_cat_image(self):
        """创建猫图像表示"""
        img = VGroup()
        
        frame = Rectangle(
            width=1.8, height=1.5,
            color=PRIMARY_COLOR,
            fill_opacity=0.3
        )
        frame.set_stroke(PRIMARY_COLOR, width=2)
        
        # 简化猫脸
        face = Circle(radius=0.4, color=ACCENT_COLOR, fill_opacity=0.5)
        
        ear_left = Polygon(
            [-0.3, 0.3, 0], [-0.15, 0.6, 0], [0, 0.3, 0],
            color=ACCENT_COLOR, fill_opacity=0.5
        )
        ear_right = ear_left.copy().shift(RIGHT * 0.3)
        
        eye_left = Circle(radius=0.06, color=BG_COLOR, fill_opacity=1)
        eye_left.move_to(face.get_center() + LEFT * 0.12 + UP * 0.05)
        eye_right = eye_left.copy().shift(RIGHT * 0.24)
        
        cat_face = VGroup(face, ear_left, ear_right, eye_left, eye_right)
        cat_face.move_to(frame.get_center())
        
        img.add(frame, cat_face)
        return img
    
    def create_task_card(self, name, desc, color):
        """创建任务卡片"""
        card = VGroup()
        
        box = RoundedRectangle(
            width=2.8, height=1.5,
            corner_radius=0.1,
            color=color,
            fill_opacity=0.2
        )
        box.set_stroke(color, width=2)
        
        title = Text(name, font_size=20, color=color)
        title.move_to(box.get_center() + UP * 0.25)
        
        description = Text(desc, font_size=14, color=TEXT_COLOR)
        description.next_to(title, DOWN, buff=0.2)
        
        card.add(box, title, description)
        return card
    
    def create_noise_image(self):
        """创建噪声图像"""
        noise = VGroup()
        
        frame = Rectangle(
            width=1.5, height=1.2,
            color=SUBTEXT_COLOR,
            fill_opacity=0.3
        )
        frame.set_stroke(SUBTEXT_COLOR, width=1)
        
        # 随机噪点
        np.random.seed(42)
        for _ in range(30):
            dot = Dot(
                point=frame.get_center() + np.array([
                    np.random.uniform(-0.6, 0.6),
                    np.random.uniform(-0.5, 0.5),
                    0
                ]),
                radius=0.03,
                color=interpolate_color(ManimColor(PRIMARY_COLOR), ManimColor(ERROR_COLOR), np.random.random())
            )
            dot.set_opacity(np.random.uniform(0.3, 1))
            noise.add(dot)
        
        noise.add(frame)
        return noise
    
    def create_partially_denoised(self, noise_level):
        """创建部分去噪图像"""
        img = VGroup()
        
        frame = Rectangle(
            width=1.2, height=1,
            color=SUBTEXT_COLOR,
            fill_opacity=0.2
        )
        frame.set_stroke(SUBTEXT_COLOR, width=1)
        
        # 混合噪声和形状
        if noise_level > 0.5:
            np.random.seed(43)
            for _ in range(int(15 * noise_level)):
                dot = Dot(
                    point=frame.get_center() + np.array([
                        np.random.uniform(-0.5, 0.5),
                        np.random.uniform(-0.4, 0.4),
                        0
                    ]),
                    radius=0.02,
                    color=SUBTEXT_COLOR
                )
                img.add(dot)
        else:
            # 更清晰的形状
            shape = Circle(radius=0.25, color=ACCENT_COLOR, fill_opacity=0.3 * (1 - noise_level))
            shape.move_to(frame.get_center())
            img.add(shape)
        
        img.add(frame)
        return img
    
    def create_cat_beach_image(self):
        """创建猫在沙滩图像"""
        img = VGroup()
        
        frame = Rectangle(
            width=1.8, height=1.5,
            color=SECONDARY_COLOR,
            fill_opacity=0.3
        )
        frame.set_stroke(SECONDARY_COLOR, width=2)
        
        # 沙滩背景
        beach = Rectangle(
            width=1.6, height=0.5,
            color=ACCENT_COLOR,
            fill_opacity=0.4
        )
        beach.move_to(frame.get_center() + DOWN * 0.35)
        
        # 天空
        sky = Rectangle(
            width=1.6, height=0.8,
            color=PRIMARY_COLOR,
            fill_opacity=0.3
        )
        sky.move_to(frame.get_center() + UP * 0.2)
        
        # 猫
        cat = Circle(radius=0.3, color=ACCENT_COLOR, fill_opacity=0.7)
        cat.move_to(frame.get_center())
        
        # 墨镜
        glass_left = Rectangle(width=0.15, height=0.08, color=BG_COLOR, fill_opacity=1)
        glass_right = glass_left.copy()
        glass_left.move_to(cat.get_center() + LEFT * 0.08 + UP * 0.05)
        glass_right.move_to(cat.get_center() + RIGHT * 0.08 + UP * 0.05)
        
        img.add(frame, sky, beach, cat, glass_left, glass_right)
        return img
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = ApplicationsScene()
    scene.render()
