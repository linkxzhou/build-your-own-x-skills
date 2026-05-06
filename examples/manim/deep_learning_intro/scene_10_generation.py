"""
场景10: 生成与创造
基于scenes.md - 展示AI从感知到创造的飞跃：GPT自回归 + 扩散模型去噪

运行命令:
    manim -pql scene_10_generation.py GenerationScene
    manim -pqh scene_10_generation.py GenerationScene
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


class GenerationScene(Scene):
    """场景10: 生成与创造"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入
        self.show_intro()
        
        # 2. 文本生成 - GPT自回归
        self.show_text_generation()
        
        # 3. 图像生成 - 扩散模型（核心动画）
        self.show_diffusion_model()
        
        # 4. 核心洞察
        self.show_insight()
        
        self.clear_scene()
    
    def show_intro(self):
        """引入"""
        # 标题
        title = Text("生成与创造", font_size=48, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.8)
        
        # 副标题
        subtitle = Text("AI从'看懂世界'走向'创造世界'", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(FadeIn(subtitle), run_time=0.5)
        
        # 两大方向
        directions = VGroup()
        
        # 文本生成
        text_gen = VGroup()
        text_box = RoundedRectangle(
            width=4, height=2,
            corner_radius=0.15,
            color=PRIMARY_COLOR,
            fill_opacity=0.2
        )
        text_box.set_stroke(PRIMARY_COLOR, width=2)
        
        text_title = Text("文本生成", font_size=24, color=PRIMARY_COLOR)
        text_title.move_to(text_box.get_center() + UP * 0.4)
        
        text_desc = Text("GPT系列\n对话、写作、编程", font_size=16, color=TEXT_COLOR, line_spacing=1.2)
        text_desc.next_to(text_title, DOWN, buff=0.2)
        
        text_gen.add(text_box, text_title, text_desc)
        
        # 图像生成
        img_gen = VGroup()
        img_box = RoundedRectangle(
            width=4, height=2,
            corner_radius=0.15,
            color=NEURAL_COLOR,
            fill_opacity=0.2
        )
        img_box.set_stroke(NEURAL_COLOR, width=2)
        
        img_title = Text("图像生成", font_size=24, color=NEURAL_COLOR)
        img_title.move_to(img_box.get_center() + UP * 0.4)
        
        img_desc = Text("扩散模型\n从噪声到艺术", font_size=16, color=TEXT_COLOR, line_spacing=1.2)
        img_desc.next_to(img_title, DOWN, buff=0.2)
        
        img_gen.add(img_box, img_title, img_desc)
        
        directions.add(text_gen, img_gen)
        directions.arrange(RIGHT, buff=1)
        directions.next_to(subtitle, DOWN, buff=0.6)
        
        self.play(FadeIn(directions, lag_ratio=0.2), run_time=0.8)
        
        # 激动人心
        exciting = Text(
            "这是当前最激动人心的领域！",
            font_size=22, color=ACCENT_COLOR
        )
        exciting.to_edge(DOWN, buff=0.6)
        
        self.play(Write(exciting), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_text_generation(self):
        """文本生成 - GPT自回归"""
        # 标题
        title = Text("文本生成 — GPT系列", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 核心原理
        principle = Text("自回归：每次预测下一个词", font_size=24, color=TEXT_COLOR)
        principle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(principle), run_time=0.5)
        
        # 逐词生成动画
        prompt = Text("提示: ", font_size=20, color=SUBTEXT_COLOR)
        prompt.move_to(LEFT * 4 + UP * 0.5)
        
        self.play(Write(prompt), run_time=0.3)
        
        # 初始提示
        initial_words = ["深度", "学习"]
        generated_words = ["是", "一种", "强大", "的", "技术", "..."]
        
        all_words = VGroup()
        current_pos = prompt.get_right() + RIGHT * 0.2
        
        # 显示提示词
        for word in initial_words:
            word_text = Text(word, font_size=22, color=PRIMARY_COLOR)
            word_text.move_to(current_pos + RIGHT * len(word) * 0.15)
            current_pos = word_text.get_right() + RIGHT * 0.1
            all_words.add(word_text)
            self.play(Write(word_text), run_time=0.2)
        
        self.wait(0.3)
        
        # 逐词生成
        gen_label = Text("生成: ", font_size=20, color=ACCENT_COLOR)
        gen_label.next_to(all_words, RIGHT, buff=0.3)
        
        self.play(Write(gen_label), run_time=0.2)
        
        current_pos = gen_label.get_right() + RIGHT * 0.2
        
        for word in generated_words:
            word_text = Text(word, font_size=22, color=SECONDARY_COLOR)
            word_text.move_to(current_pos + RIGHT * len(word) * 0.15)
            current_pos = word_text.get_right() + RIGHT * 0.1
            
            # 闪烁效果
            self.play(
                FadeIn(word_text, scale=1.2),
                run_time=0.25
            )
        
        # GPT的能力
        abilities = VGroup(
            Text("GPT的能力:", font_size=22, color=ACCENT_COLOR),
            Text("• 对话交流", font_size=18, color=TEXT_COLOR),
            Text("• 文章写作", font_size=18, color=TEXT_COLOR),
            Text("• 代码编程", font_size=18, color=TEXT_COLOR),
            Text("• 逻辑推理（思维链）", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        abilities.to_edge(DOWN, buff=0.5)
        
        self.play(Write(abilities), run_time=0.8)
        
        # 类比
        analogy = Text(
            "像'接龙游戏'，每次续写一个词",
            font_size=18, color=SUBTEXT_COLOR
        )
        analogy.next_to(abilities, UP, buff=0.3)
        
        self.play(Write(analogy), run_time=0.4)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_diffusion_model(self):
        """扩散模型 - 核心动画"""
        # 标题
        title = Text("图像生成 — 扩散模型", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 核心思想
        idea = Text("从噪声中'雕刻'出图像", font_size=24, color=TEXT_COLOR)
        idea.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(idea), run_time=0.4)
        
        # 两个过程
        process_title = VGroup(
            Text("加噪过程", font_size=20, color=ERROR_COLOR),
            Text("去噪过程", font_size=20, color=SECONDARY_COLOR),
        ).arrange(RIGHT, buff=3)
        process_title.next_to(idea, DOWN, buff=0.4)
        
        self.play(Write(process_title), run_time=0.4)
        
        # 加噪过程演示
        noise_stages = 8
        img_size = 1.2
        
        # 清晰图像 -> 噪声
        add_noise_images = VGroup()
        for i in range(noise_stages):
            img = self.create_noisy_image(i / (noise_stages - 1), img_size)
            add_noise_images.add(img)
        
        add_noise_images.arrange(RIGHT, buff=0.15)
        add_noise_images.scale(0.7)
        add_noise_images.move_to(LEFT * 3 + DOWN * 0.8)
        
        # 显示加噪过程
        self.play(FadeIn(add_noise_images[0]), run_time=0.3)
        
        for i in range(1, noise_stages):
            arrow = Arrow(
                add_noise_images[i-1].get_right(),
                add_noise_images[i].get_left(),
                buff=0.05, stroke_width=1, color=ERROR_COLOR, max_tip_length_to_length_ratio=0.3
            )
            self.play(
                GrowArrow(arrow),
                FadeIn(add_noise_images[i]),
                run_time=0.15
            )
        
        add_label = Text("逐渐添加噪声", font_size=14, color=ERROR_COLOR)
        add_label.next_to(add_noise_images, DOWN, buff=0.2)
        self.play(Write(add_label), run_time=0.3)
        
        self.wait(0.5)
        
        # 去噪过程（核心）
        denoise_images = VGroup()
        for i in range(noise_stages):
            img = self.create_noisy_image(1 - i / (noise_stages - 1), img_size)
            denoise_images.add(img)
        
        denoise_images.arrange(RIGHT, buff=0.15)
        denoise_images.scale(0.7)
        denoise_images.move_to(RIGHT * 3 + DOWN * 0.8)
        
        # 显示去噪过程
        self.play(FadeIn(denoise_images[0]), run_time=0.3)
        
        # 文本条件
        text_prompt = Text('"一只猫"', font_size=16, color=ACCENT_COLOR)
        text_prompt.next_to(denoise_images, UP, buff=0.3)
        
        self.play(Write(text_prompt), run_time=0.3)
        
        for i in range(1, noise_stages):
            arrow = Arrow(
                denoise_images[i-1].get_right(),
                denoise_images[i].get_left(),
                buff=0.05, stroke_width=1, color=SECONDARY_COLOR, max_tip_length_to_length_ratio=0.3
            )
            self.play(
                GrowArrow(arrow),
                FadeIn(denoise_images[i]),
                run_time=0.2
            )
        
        denoise_label = Text("逐步去除噪声", font_size=14, color=SECONDARY_COLOR)
        denoise_label.next_to(denoise_images, DOWN, buff=0.2)
        self.play(Write(denoise_label), run_time=0.3)
        
        # 高亮最终结果
        self.play(
            Flash(denoise_images[-1].get_center(), color=SECONDARY_COLOR, line_length=0.3),
            run_time=0.5
        )
        
        # 说明
        explanation = VGroup(
            Text("1. 从纯噪声开始", font_size=16, color=TEXT_COLOR),
            Text("2. 网络预测'不属于猫'的噪声部分", font_size=16, color=TEXT_COLOR),
            Text("3. 逐步减去这些噪声", font_size=16, color=TEXT_COLOR),
            Text("4. 猫从混沌中'浮现'", font_size=16, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        explanation.to_edge(DOWN, buff=0.4)
        
        self.play(Write(explanation), run_time=1)
        
        self.wait(2)
        self.clear_scene()
    
    def show_insight(self):
        """核心洞察"""
        # 标题
        title = Text("从混沌到秩序", font_size=44, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.8)
        
        self.play(Write(title), run_time=0.6)
        
        # 美学描述
        aesthetic = Text(
            "扩散模型像艺术家画画：从模糊到清晰",
            font_size=26, color=TEXT_COLOR
        )
        aesthetic.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(aesthetic), run_time=0.6)
        
        # 可视化：混沌 -> 秩序
        chaos = VGroup()
        np.random.seed(42)
        for _ in range(50):
            dot = Dot(
                point=[np.random.uniform(-1.5, 1.5), np.random.uniform(-1, 1), 0],
                radius=0.05,
                color=np.random.choice([PRIMARY_COLOR, NEURAL_COLOR, ERROR_COLOR])
            )
            chaos.add(dot)
        
        chaos.move_to(LEFT * 3)
        
        chaos_label = Text("混沌", font_size=18, color=ERROR_COLOR)
        chaos_label.next_to(chaos, DOWN, buff=0.3)
        
        # 秩序（有结构的图案）
        order = VGroup()
        # 创建一个简单的猫脸轮廓
        face = Circle(radius=0.8, color=SECONDARY_COLOR, fill_opacity=0.3)
        face.set_stroke(SECONDARY_COLOR, width=2)
        
        ear1 = Triangle(color=SECONDARY_COLOR, fill_opacity=0.3)
        ear1.scale(0.3)
        ear1.move_to(face.get_top() + LEFT * 0.4 + UP * 0.1)
        ear1.set_stroke(SECONDARY_COLOR, width=2)
        
        ear2 = ear1.copy()
        ear2.move_to(face.get_top() + RIGHT * 0.4 + UP * 0.1)
        
        eye1 = Dot(face.get_center() + LEFT * 0.3 + UP * 0.1, radius=0.1, color=ACCENT_COLOR)
        eye2 = Dot(face.get_center() + RIGHT * 0.3 + UP * 0.1, radius=0.1, color=ACCENT_COLOR)
        
        nose = Triangle(color=ERROR_COLOR, fill_opacity=0.6)
        nose.scale(0.1)
        nose.rotate(PI)
        nose.move_to(face.get_center() + DOWN * 0.1)
        
        order.add(face, ear1, ear2, eye1, eye2, nose)
        order.move_to(RIGHT * 3)
        
        order_label = Text("秩序", font_size=18, color=SECONDARY_COLOR)
        order_label.next_to(order, DOWN, buff=0.3)
        
        self.play(FadeIn(chaos), Write(chaos_label), run_time=0.5)
        
        # 箭头
        arrow = Arrow(
            chaos.get_right() + RIGHT * 0.5,
            order.get_left() + LEFT * 0.5,
            color=ACCENT_COLOR, stroke_width=3
        )
        arrow_label = Text("去噪网络", font_size=16, color=ACCENT_COLOR)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=0.5)
        self.play(FadeIn(order), Write(order_label), run_time=0.5)
        
        # 核心洞察
        insight = VGroup(
            Text("核心洞察:", font_size=22, color=ACCENT_COLOR),
            Text("AI从'看懂世界'走向了'创造世界'", font_size=24, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2)
        insight.to_edge(DOWN, buff=0.6)
        
        box = SurroundingRectangle(insight, color=ACCENT_COLOR, buff=0.2, corner_radius=0.1)
        
        self.play(Write(insight), Create(box), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_noisy_image(self, noise_level, size):
        """创建带噪声的图像"""
        img = VGroup()
        
        # 背景
        bg = Square(side_length=size, color=SUBTEXT_COLOR, fill_opacity=0.1)
        bg.set_stroke(SUBTEXT_COLOR, width=1)
        
        # 像素网格
        grid_size = 6
        pixel_size = size / grid_size
        
        np.random.seed(int(noise_level * 1000) % 100)
        
        for i in range(grid_size):
            for j in range(grid_size):
                pixel = Square(side_length=pixel_size * 0.9)
                pixel.move_to(bg.get_center() + np.array([
                    (i - grid_size/2 + 0.5) * pixel_size,
                    (j - grid_size/2 + 0.5) * pixel_size,
                    0
                ]))
                
                # 根据噪声级别决定颜色
                if noise_level > 0.8:
                    # 纯噪声
                    color = np.random.choice([PRIMARY_COLOR, NEURAL_COLOR, ERROR_COLOR, SUBTEXT_COLOR])
                    pixel.set_fill(color, opacity=0.6)
                elif noise_level > 0.5:
                    # 部分噪声
                    if np.random.random() > 0.5:
                        color = np.random.choice([PRIMARY_COLOR, NEURAL_COLOR, ERROR_COLOR])
                    else:
                        # 显示一些结构
                        if (i - grid_size/2)**2 + (j - grid_size/2)**2 < 4:
                            color = ACCENT_COLOR
                        else:
                            color = SECONDARY_COLOR
                    pixel.set_fill(color, opacity=0.5)
                elif noise_level > 0.2:
                    # 轻微噪声
                    if (i - grid_size/2)**2 + (j - grid_size/2)**2 < 3:
                        color = ACCENT_COLOR
                    elif j > grid_size/2:
                        color = SECONDARY_COLOR
                    else:
                        color = PRIMARY_COLOR
                    pixel.set_fill(color, opacity=0.4 + np.random.random() * 0.3)
                else:
                    # 清晰图像
                    # 简单的猫脸模式
                    dist_center = (i - grid_size/2)**2 + (j - grid_size/2)**2
                    if dist_center < 2:
                        color = ACCENT_COLOR  # 眼睛/鼻子区域
                    elif dist_center < 6:
                        color = SECONDARY_COLOR  # 脸
                    else:
                        color = PRIMARY_COLOR  # 背景
                    pixel.set_fill(color, opacity=0.6)
                
                pixel.set_stroke(width=0)
                img.add(pixel)
        
        img.add(bg)
        return img
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = GenerationScene()
    scene.render()
