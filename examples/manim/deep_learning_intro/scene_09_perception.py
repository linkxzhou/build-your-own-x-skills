"""
场景9: 感知与预测应用
基于scenes.md - 展示深度学习在感知类任务的应用

运行命令:
    manim -pql scene_09_perception.py PerceptionScene
    manim -pqh scene_09_perception.py PerceptionScene
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


class PerceptionScene(Scene):
    """场景9: 感知与预测应用"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入
        self.show_intro()
        
        # 2. 图像分类
        self.show_image_classification()
        
        # 3. 目标检测
        self.show_object_detection()
        
        # 4. 语义分割
        self.show_semantic_segmentation()
        
        # 5. CLIP多模态
        self.show_clip()
        
        self.clear_scene()
    
    def show_intro(self):
        """引入"""
        # 标题
        title = Text("感知与预测应用", font_size=44, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.8)
        
        # 副标题
        subtitle = Text("AI如何'看懂'世界", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(FadeIn(subtitle), run_time=0.4)
        
        # 应用领域预览
        apps = VGroup()
        app_data = [
            ("图像分类", "识别物体类别", PRIMARY_COLOR),
            ("目标检测", "定位并识别", SECONDARY_COLOR),
            ("语义分割", "像素级理解", ACCENT_COLOR),
            ("多模态", "连接视觉与语言", NEURAL_COLOR),
        ]
        
        for name, desc, color in app_data:
            app = VGroup()
            box = RoundedRectangle(
                width=2.4, height=1.4,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.2
            )
            box.set_stroke(color, width=2)
            
            name_text = Text(name, font_size=18, color=color)
            name_text.move_to(box.get_center() + UP * 0.2)
            
            desc_text = Text(desc, font_size=12, color=SUBTEXT_COLOR)
            desc_text.next_to(name_text, DOWN, buff=0.15)
            
            app.add(box, name_text, desc_text)
            apps.add(app)
        
        apps.arrange(RIGHT, buff=0.4)
        apps.next_to(subtitle, DOWN, buff=0.6)
        
        self.play(FadeIn(apps, lag_ratio=0.15), run_time=1)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_image_classification(self):
        """图像分类"""
        # 标题
        title = Text("图像分类 — CV的'Hello World'", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 输入图片
        img = self.create_image_placeholder("🐱", PRIMARY_COLOR)
        img.scale(0.8)
        img.move_to(LEFT * 4)
        
        img_label = Text("输入图片", font_size=16, color=SUBTEXT_COLOR)
        img_label.next_to(img, DOWN, buff=0.2)
        
        self.play(FadeIn(img), Write(img_label), run_time=0.5)
        
        # 模型
        model_box = RoundedRectangle(
            width=2, height=1.5,
            corner_radius=0.1,
            color=NEURAL_COLOR,
            fill_opacity=0.3
        )
        model_box.set_stroke(NEURAL_COLOR, width=2)
        model_label = Text("ResNet/ViT", font_size=16, color=NEURAL_COLOR)
        model_label.move_to(model_box.get_center())
        
        model = VGroup(model_box, model_label)
        model.move_to(ORIGIN)
        
        # 箭头
        arrow1 = Arrow(img.get_right(), model.get_left(), color=TEXT_COLOR, buff=0.3, stroke_width=2)
        
        self.play(FadeIn(model), GrowArrow(arrow1), run_time=0.5)
        
        # 输出概率分布
        output = self.create_probability_bars()
        output.scale(0.8)
        output.move_to(RIGHT * 4)
        
        arrow2 = Arrow(model.get_right(), output.get_left(), color=TEXT_COLOR, buff=0.3, stroke_width=2)
        
        self.play(GrowArrow(arrow2), FadeIn(output), run_time=0.5)
        
        # 概率条动画
        bars = output[1]
        self.play(
            bars[0][0].animate.set_fill(SECONDARY_COLOR, opacity=0.8),
            run_time=0.4
        )
        
        # 结果
        result = Text("预测：猫 (95%)", font_size=20, color=SECONDARY_COLOR)
        result.to_edge(DOWN, buff=0.8)
        
        self.play(Write(result), run_time=0.4)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_object_detection(self):
        """目标检测"""
        # 标题
        title = Text("目标检测 — 定位并识别", font_size=36, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 场景图片
        scene = self.create_scene_image()
        scene.scale(0.9)
        scene.move_to(DOWN * 0.3)
        
        self.play(FadeIn(scene), run_time=0.5)
        
        # 边界框动画
        bbox_data = [
            (LEFT * 1.5 + UP * 0.3, 1.2, 0.8, "猫", ERROR_COLOR),
            (RIGHT * 0.8 + DOWN * 0.2, 0.8, 1.0, "狗", PRIMARY_COLOR),
            (RIGHT * 2 + UP * 0.5, 0.6, 0.5, "球", ACCENT_COLOR),
        ]
        
        bboxes = VGroup()
        for pos, w, h, label, color in bbox_data:
            bbox = Rectangle(
                width=w, height=h,
                color=color,
                stroke_width=3
            )
            bbox.move_to(scene.get_center() + pos)
            
            label_bg = Rectangle(
                width=len(label) * 0.25 + 0.2,
                height=0.3,
                color=color,
                fill_opacity=0.8
            )
            label_bg.next_to(bbox, UP, buff=0)
            label_bg.align_to(bbox, LEFT)
            
            label_text = Text(label, font_size=14, color=TEXT_COLOR)
            label_text.move_to(label_bg.get_center())
            
            bbox_group = VGroup(bbox, label_bg, label_text)
            bboxes.add(bbox_group)
        
        for bbox in bboxes:
            self.play(Create(bbox[0]), FadeIn(bbox[1]), Write(bbox[2]), run_time=0.4)
        
        # 说明
        desc = VGroup(
            Text("不仅分类，还要定位", font_size=20, color=TEXT_COLOR),
            Text("代表方法：YOLO, SSD, Faster R-CNN", font_size=16, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.15)
        desc.to_edge(DOWN, buff=0.5)
        
        self.play(Write(desc), run_time=0.6)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_semantic_segmentation(self):
        """语义分割"""
        # 标题
        title = Text("语义分割 — 像素级分类", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 原图
        original = self.create_segmentation_original()
        original.scale(0.7)
        original.move_to(LEFT * 3 + DOWN * 0.3)
        
        orig_label = Text("原图", font_size=16, color=SUBTEXT_COLOR)
        orig_label.next_to(original, DOWN, buff=0.2)
        
        self.play(FadeIn(original), Write(orig_label), run_time=0.5)
        
        # 箭头
        arrow = Arrow(
            original.get_right() + RIGHT * 0.2,
            original.get_right() + RIGHT * 2,
            color=NEURAL_COLOR, stroke_width=3
        )
        
        arrow_label = Text("分割网络", font_size=14, color=NEURAL_COLOR)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        self.play(GrowArrow(arrow), Write(arrow_label), run_time=0.4)
        
        # 分割结果
        segmented = self.create_segmentation_result()
        segmented.scale(0.7)
        segmented.move_to(RIGHT * 3 + DOWN * 0.3)
        
        seg_label = Text("分割结果", font_size=16, color=SUBTEXT_COLOR)
        seg_label.next_to(segmented, DOWN, buff=0.2)
        
        self.play(FadeIn(segmented, lag_ratio=0.02), Write(seg_label), run_time=1)
        
        # 图例
        legend = VGroup(
            self.create_legend_item("天空", PRIMARY_COLOR),
            self.create_legend_item("建筑", ACCENT_COLOR),
            self.create_legend_item("道路", SUBTEXT_COLOR),
            self.create_legend_item("植物", SECONDARY_COLOR),
        ).arrange(RIGHT, buff=0.5)
        legend.to_edge(DOWN, buff=0.5)
        
        self.play(FadeIn(legend), run_time=0.5)
        
        # 说明
        desc = Text(
            "为每个像素打上类别标签 — 像给图片上'语义油漆'",
            font_size=18, color=TEXT_COLOR
        )
        desc.next_to(legend, UP, buff=0.3)
        
        self.play(Write(desc), run_time=0.6)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_clip(self):
        """CLIP多模态"""
        # 标题
        title = Text("CLIP — 多模态里程碑", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 核心思想
        idea = Text(
            "同时学习图像和文本，映射到同一语义空间",
            font_size=22, color=TEXT_COLOR
        )
        idea.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(idea), run_time=0.6)
        
        # 双塔结构
        # 图像编码器
        img_encoder = VGroup()
        img_box = RoundedRectangle(
            width=2, height=2.5,
            corner_radius=0.1,
            color=PRIMARY_COLOR,
            fill_opacity=0.2
        )
        img_box.set_stroke(PRIMARY_COLOR, width=2)
        img_title = Text("图像编码器", font_size=16, color=PRIMARY_COLOR)
        img_title.next_to(img_box, UP, buff=0.1)
        
        img_icon = self.create_image_placeholder("🖼", PRIMARY_COLOR, 0.8)
        img_icon.scale(0.5)
        img_icon.move_to(img_box.get_center())
        
        img_encoder.add(img_box, img_title, img_icon)
        img_encoder.move_to(LEFT * 3 + DOWN * 0.5)
        
        # 文本编码器
        txt_encoder = VGroup()
        txt_box = RoundedRectangle(
            width=2, height=2.5,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.2
        )
        txt_box.set_stroke(ACCENT_COLOR, width=2)
        txt_title = Text("文本编码器", font_size=16, color=ACCENT_COLOR)
        txt_title.next_to(txt_box, UP, buff=0.1)
        
        txt_icon = Text("📝", font_size=36)
        txt_icon.move_to(txt_box.get_center())
        
        txt_encoder.add(txt_box, txt_title, txt_icon)
        txt_encoder.move_to(RIGHT * 3 + DOWN * 0.5)
        
        self.play(FadeIn(img_encoder), FadeIn(txt_encoder), run_time=0.6)
        
        # 共享语义空间
        shared_space = Circle(
            radius=1.2,
            color=SECONDARY_COLOR,
            fill_opacity=0.1
        )
        shared_space.set_stroke(SECONDARY_COLOR, width=2, dash_length=0.1)
        
        space_label = Text("共享语义空间", font_size=14, color=SECONDARY_COLOR)
        space_label.next_to(shared_space, DOWN, buff=0.1)
        
        space = VGroup(shared_space, space_label)
        space.move_to(DOWN * 0.5)
        
        self.play(Create(shared_space), Write(space_label), run_time=0.5)
        
        # 映射箭头
        arrow1 = Arrow(
            img_encoder.get_right(),
            shared_space.get_left(),
            color=PRIMARY_COLOR, stroke_width=2, buff=0.2
        )
        
        arrow2 = Arrow(
            txt_encoder.get_left(),
            shared_space.get_right(),
            color=ACCENT_COLOR, stroke_width=2, buff=0.2
        )
        
        self.play(GrowArrow(arrow1), GrowArrow(arrow2), run_time=0.4)
        
        # 点（向量）
        img_point = Dot(
            shared_space.get_center() + LEFT * 0.3 + UP * 0.2,
            radius=0.15, color=PRIMARY_COLOR
        )
        txt_point = Dot(
            shared_space.get_center() + LEFT * 0.2 + UP * 0.3,
            radius=0.15, color=ACCENT_COLOR
        )
        
        self.play(FadeIn(img_point), FadeIn(txt_point), run_time=0.3)
        
        # 相似度连线
        sim_line = DashedLine(
            img_point.get_center(),
            txt_point.get_center(),
            color=SECONDARY_COLOR, stroke_width=2
        )
        
        self.play(Create(sim_line), run_time=0.3)
        
        # 零样本能力
        zero_shot = VGroup(
            Text("零样本预测能力:", font_size=18, color=ACCENT_COLOR),
            Text("没见过'斑马素描'也能识别", font_size=16, color=TEXT_COLOR),
            Text("因为理解了图像和文本的深层联系", font_size=14, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        zero_shot.to_edge(DOWN, buff=0.4)
        
        self.play(Write(zero_shot), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_image_placeholder(self, emoji, color, size=1.5):
        """创建图片占位符"""
        img = VGroup()
        
        box = RoundedRectangle(
            width=size, height=size,
            corner_radius=0.1,
            color=color,
            fill_opacity=0.3
        )
        box.set_stroke(color, width=2)
        
        icon = Text(emoji, font_size=int(36 * size / 1.5))
        icon.move_to(box.get_center())
        
        img.add(box, icon)
        return img
    
    def create_probability_bars(self):
        """创建概率分布条形图"""
        output = VGroup()
        
        title = Text("类别概率", font_size=14, color=SUBTEXT_COLOR)
        
        bars = VGroup()
        bar_data = [
            ("猫", 0.95, SECONDARY_COLOR),
            ("狗", 0.03, SUBTEXT_COLOR),
            ("鸟", 0.02, SUBTEXT_COLOR),
        ]
        
        for label, prob, color in bar_data:
            bar_group = VGroup()
            
            label_text = Text(label, font_size=14, color=TEXT_COLOR)
            
            bar_bg = Rectangle(
                width=2, height=0.3,
                color=SUBTEXT_COLOR,
                fill_opacity=0.2
            )
            bar_bg.set_stroke(SUBTEXT_COLOR, width=1)
            
            bar_fill = Rectangle(
                width=2 * prob, height=0.3,
                color=color,
                fill_opacity=0.6
            )
            bar_fill.set_stroke(color, width=1)
            bar_fill.align_to(bar_bg, LEFT)
            
            prob_text = Text(f"{prob:.0%}", font_size=12, color=TEXT_COLOR)
            prob_text.next_to(bar_bg, RIGHT, buff=0.1)
            
            label_text.next_to(bar_bg, LEFT, buff=0.1)
            
            bar_group.add(bar_fill, bar_bg, label_text, prob_text)
            bars.add(bar_group)
        
        bars.arrange(DOWN, buff=0.2)
        title.next_to(bars, UP, buff=0.2)
        
        output.add(title, bars)
        return output
    
    def create_scene_image(self):
        """创建场景图片"""
        scene = VGroup()
        
        # 背景
        bg = Rectangle(
            width=5, height=3.5,
            color=PRIMARY_COLOR,
            fill_opacity=0.2
        )
        bg.set_stroke(PRIMARY_COLOR, width=2)
        
        # 简化的场景元素
        elements_text = Text("场景图片", font_size=24, color=SUBTEXT_COLOR)
        elements_text.move_to(bg.get_center())
        
        scene.add(bg, elements_text)
        return scene
    
    def create_segmentation_original(self):
        """创建分割原图"""
        img = VGroup()
        
        # 创建像素网格
        for i in range(8):
            for j in range(6):
                pixel = Square(side_length=0.3, fill_opacity=0.4)
                pixel.set_stroke(SUBTEXT_COLOR, width=0.5)
                
                # 简单的颜色分布
                if j < 2:  # 天空
                    pixel.set_fill(PRIMARY_COLOR, opacity=0.3)
                elif i < 3:  # 左侧建筑
                    pixel.set_fill(ACCENT_COLOR, opacity=0.3)
                elif i > 5:  # 右侧植物
                    pixel.set_fill(SECONDARY_COLOR, opacity=0.3)
                else:  # 道路
                    pixel.set_fill(SUBTEXT_COLOR, opacity=0.3)
                
                pixel.move_to([i * 0.32, -j * 0.32, 0])
                img.add(pixel)
        
        img.move_to(ORIGIN)
        return img
    
    def create_segmentation_result(self):
        """创建分割结果"""
        img = VGroup()
        
        # 创建像素网格
        for i in range(8):
            for j in range(6):
                pixel = Square(side_length=0.3, fill_opacity=0.7)
                pixel.set_stroke(WHITE, width=0.3)
                
                # 分割颜色
                if j < 2:  # 天空
                    pixel.set_fill(PRIMARY_COLOR, opacity=0.7)
                elif i < 3:  # 左侧建筑
                    pixel.set_fill(ACCENT_COLOR, opacity=0.7)
                elif i > 5:  # 右侧植物
                    pixel.set_fill(SECONDARY_COLOR, opacity=0.7)
                else:  # 道路
                    pixel.set_fill(SUBTEXT_COLOR, opacity=0.7)
                
                pixel.move_to([i * 0.32, -j * 0.32, 0])
                img.add(pixel)
        
        img.move_to(ORIGIN)
        return img
    
    def create_legend_item(self, label, color):
        """创建图例项"""
        item = VGroup()
        
        box = Square(side_length=0.3, color=color, fill_opacity=0.7)
        box.set_stroke(color, width=1)
        
        text = Text(label, font_size=12, color=TEXT_COLOR)
        text.next_to(box, RIGHT, buff=0.1)
        
        item.add(box, text)
        return item
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = PerceptionScene()
    scene.render()
