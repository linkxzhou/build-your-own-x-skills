"""
场景4: GPU与张量 - 计算引擎
展示深度学习的硬件基础和数据结构

运行命令:
    manim -pql scene_04_gpu_tensor.py GPUTensorScene
    manim -pqh scene_04_gpu_tensor.py GPUTensorScene
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


class GPUTensorScene(Scene):
    """场景4: GPU与张量"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入：计算需求
        self.show_compute_need()
        
        # 2. GPU介绍
        self.show_gpu_intro()
        
        # 3. 张量可视化
        self.show_tensor_visualization()
        
        self.clear_scene()
    
    def show_compute_need(self):
        """展示计算需求"""
        # 标题
        title = Text("第二部分：引擎房", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("深度学习的'硬核'计算", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        # 计算量展示
        compute_text = Text("训练一个强大的模型需要:", font_size=28, color=TEXT_COLOR)
        compute_text.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(Write(compute_text), run_time=0.5)
        
        # 数字动画
        numbers = VGroup()
        
        params = Text("参数量: ", font_size=24, color=SUBTEXT_COLOR)
        params_num = Text("1,750亿", font_size=32, color=PRIMARY_COLOR)
        params_group = VGroup(params, params_num).arrange(RIGHT, buff=0.2)
        
        data = Text("训练数据: ", font_size=24, color=SUBTEXT_COLOR)
        data_num = Text("数万亿 tokens", font_size=32, color=SECONDARY_COLOR)
        data_group = VGroup(data, data_num).arrange(RIGHT, buff=0.2)
        
        compute = Text("计算量: ", font_size=24, color=SUBTEXT_COLOR)
        compute_num = Text("数百 PFLOPS", font_size=32, color=ACCENT_COLOR)
        compute_group = VGroup(compute, compute_num).arrange(RIGHT, buff=0.2)
        
        numbers.add(params_group, data_group, compute_group)
        numbers.arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        numbers.next_to(compute_text, DOWN, buff=0.6)
        
        for num in numbers:
            self.play(FadeIn(num, shift=RIGHT * 0.3), run_time=0.4)
        
        # GPT-3 标注
        gpt_note = Text("(GPT-3 规模)", font_size=18, color=SUBTEXT_COLOR)
        gpt_note.next_to(params_group, RIGHT, buff=0.3)
        self.play(FadeIn(gpt_note), run_time=0.3)
        
        self.wait(1)
        
        # 结论
        conclusion = Text(
            "这离不开强大的硬件!",
            font_size=32, color=ACCENT_COLOR
        )
        conclusion.to_edge(DOWN, buff=0.8)
        
        self.play(Write(conclusion), run_time=0.8)
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_gpu_intro(self):
        """GPU介绍"""
        # 标题
        title = Text("GPU - 图形处理器", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # CPU vs GPU 对比
        cpu_title = Text("CPU", font_size=28, color=PRIMARY_COLOR)
        gpu_title = Text("GPU", font_size=28, color=SECONDARY_COLOR)
        vs_text = Text("vs", font_size=24, color=TEXT_COLOR)
        
        cpu_title.move_to(LEFT * 3.5 + UP * 1.5)
        gpu_title.move_to(RIGHT * 3.5 + UP * 1.5)
        vs_text.move_to(UP * 1.5)
        
        self.play(Write(cpu_title), Write(gpu_title), Write(vs_text), run_time=0.5)
        
        # CPU - 少量强大核心
        cpu_cores = VGroup()
        for i in range(4):
            core = Square(side_length=0.6, color=PRIMARY_COLOR, fill_opacity=0.6)
            core.set_stroke(PRIMARY_COLOR, width=2)
            cpu_cores.add(core)
        cpu_cores.arrange_in_grid(rows=2, cols=2, buff=0.1)
        cpu_cores.move_to(LEFT * 3.5)
        
        cpu_label = Text("4-16 个强力核心", font_size=18, color=PRIMARY_COLOR)
        cpu_label.next_to(cpu_cores, DOWN, buff=0.3)
        
        cpu_desc = Text("'一次做一件大事'", font_size=16, color=SUBTEXT_COLOR)
        cpu_desc.next_to(cpu_label, DOWN, buff=0.15)
        
        self.play(FadeIn(cpu_cores, scale=0.8), run_time=0.5)
        self.play(Write(cpu_label), Write(cpu_desc), run_time=0.5)
        
        # GPU - 大量小核心
        gpu_cores = VGroup()
        for i in range(64):
            core = Square(side_length=0.12, color=SECONDARY_COLOR, fill_opacity=0.6)
            core.set_stroke(SECONDARY_COLOR, width=1)
            gpu_cores.add(core)
        gpu_cores.arrange_in_grid(rows=8, cols=8, buff=0.02)
        gpu_cores.move_to(RIGHT * 3.5)
        
        gpu_label = Text("数千个小核心", font_size=18, color=SECONDARY_COLOR)
        gpu_label.next_to(gpu_cores, DOWN, buff=0.3)
        
        gpu_desc = Text("'同时做很多小事'", font_size=16, color=SUBTEXT_COLOR)
        gpu_desc.next_to(gpu_label, DOWN, buff=0.15)
        
        self.play(FadeIn(gpu_cores, lag_ratio=0.01), run_time=1)
        self.play(Write(gpu_label), Write(gpu_desc), run_time=0.5)
        
        self.wait(1)
        
        # 游戏产业连接
        game_text = VGroup(
            Text("🎮 本来用于游戏渲染", font_size=22, color=TEXT_COLOR),
            Text("→ 被深度学习'借用'做矩阵运算", font_size=22, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        game_text.to_edge(DOWN, buff=1.5)
        
        self.play(Write(game_text), run_time=1)
        
        # 有趣的历史
        history = Text(
            "游戏产业的繁荣，意外地为AI革命提供了燃料！",
            font_size=20, color=SUBTEXT_COLOR
        )
        history.next_to(game_text, DOWN, buff=0.3)
        
        self.play(Write(history), run_time=0.8)
        self.wait(1.5)
        
        # TPU 简介
        self.play(
            FadeOut(cpu_cores), FadeOut(cpu_label), FadeOut(cpu_desc),
            FadeOut(gpu_cores), FadeOut(gpu_label), FadeOut(gpu_desc),
            FadeOut(cpu_title), FadeOut(gpu_title), FadeOut(vs_text),
            FadeOut(game_text), FadeOut(history),
        )
        
        tpu_title = Text("TPU - 张量处理器", font_size=32, color=NEURAL_COLOR)
        tpu_title.next_to(title, DOWN, buff=0.8)
        
        tpu_desc = VGroup(
            Text("谷歌专门为深度学习设计的定制芯片", font_size=24, color=TEXT_COLOR),
            VGroup(
                Text("从'瑞士军刀'(GPU)", font_size=22, color=SECONDARY_COLOR),
                Text("→", font_size=22, color=TEXT_COLOR),
                Text("'专业厨刀'(TPU)", font_size=22, color=NEURAL_COLOR),
            ).arrange(RIGHT, buff=0.3),
        ).arrange(DOWN, buff=0.4)
        tpu_desc.next_to(tpu_title, DOWN, buff=0.5)
        
        self.play(Write(tpu_title), run_time=0.5)
        self.play(Write(tpu_desc), run_time=1)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_tensor_visualization(self):
        """张量可视化"""
        # 标题
        title = Text("张量 - 数据的基本单位", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 不要怕
        dont_fear = Text("别怕这个词！让我们一步步理解", font_size=24, color=SUBTEXT_COLOR)
        dont_fear.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(dont_fear), run_time=0.5)
        self.wait(0.5)
        self.play(FadeOut(dont_fear))
        
        # 1. 标量
        scalar_title = Text("标量 (0维)", font_size=28, color=PRIMARY_COLOR)
        scalar_title.move_to(LEFT * 4.5 + UP * 1)
        
        scalar = self.create_scalar("36.5°")
        scalar.next_to(scalar_title, DOWN, buff=0.3)
        
        scalar_example = Text("例: 温度", font_size=18, color=SUBTEXT_COLOR)
        scalar_example.next_to(scalar, DOWN, buff=0.2)
        
        self.play(Write(scalar_title), run_time=0.3)
        self.play(FadeIn(scalar, scale=0.8), Write(scalar_example), run_time=0.5)
        
        # 2. 向量
        vector_title = Text("向量 (1维)", font_size=28, color=SECONDARY_COLOR)
        vector_title.move_to(LEFT * 1.5 + UP * 1)
        
        vector = self.create_vector(["175", "65"])
        vector.next_to(vector_title, DOWN, buff=0.3)
        
        vector_example = Text("例: [身高, 体重]", font_size=18, color=SUBTEXT_COLOR)
        vector_example.next_to(vector, DOWN, buff=0.2)
        
        self.play(Write(vector_title), run_time=0.3)
        self.play(FadeIn(vector, scale=0.8), Write(vector_example), run_time=0.5)
        
        # 3. 矩阵
        matrix_title = Text("矩阵 (2维)", font_size=28, color=ACCENT_COLOR)
        matrix_title.move_to(RIGHT * 1.5 + UP * 1)
        
        matrix = self.create_matrix()
        matrix.next_to(matrix_title, DOWN, buff=0.3)
        
        matrix_example = Text("例: 成绩表", font_size=18, color=SUBTEXT_COLOR)
        matrix_example.next_to(matrix, DOWN, buff=0.2)
        
        self.play(Write(matrix_title), run_time=0.3)
        self.play(FadeIn(matrix, scale=0.8), Write(matrix_example), run_time=0.5)
        
        # 4. 张量
        tensor_title = Text("张量 (多维)", font_size=28, color=NEURAL_COLOR)
        tensor_title.move_to(RIGHT * 4.5 + UP * 1)
        
        tensor = self.create_3d_tensor()
        tensor.scale(0.6)
        tensor.next_to(tensor_title, DOWN, buff=0.3)
        
        tensor_example = Text("例: RGB图片", font_size=18, color=SUBTEXT_COLOR)
        tensor_example.next_to(tensor, DOWN, buff=0.2)
        
        self.play(Write(tensor_title), run_time=0.3)
        self.play(FadeIn(tensor, scale=0.8), Write(tensor_example), run_time=0.5)
        
        self.wait(1)
        
        # 维度说明
        dimension_text = VGroup(
            Text("一张 RGB 图片", font_size=22, color=TEXT_COLOR),
            Text("= 3 × 高 × 宽 的张量", font_size=22, color=NEURAL_COLOR),
            Text("(红、绿、蓝三个通道)", font_size=18, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.15)
        dimension_text.to_edge(DOWN, buff=0.8)
        
        self.play(Write(dimension_text), run_time=1)
        
        self.wait(1.5)
        
        # RGB 分解动画
        self.play(
            FadeOut(scalar_title), FadeOut(scalar), FadeOut(scalar_example),
            FadeOut(vector_title), FadeOut(vector), FadeOut(vector_example),
            FadeOut(matrix_title), FadeOut(matrix), FadeOut(matrix_example),
            FadeOut(tensor_title), FadeOut(tensor), FadeOut(tensor_example),
            FadeOut(dimension_text),
        )
        
        # RGB 图片分解
        rgb_demo = self.create_rgb_decomposition()
        rgb_demo.scale(0.8)
        rgb_demo.next_to(title, DOWN, buff=0.8)
        
        self.play(FadeIn(rgb_demo), run_time=1)
        
        # 说明
        rgb_text = VGroup(
            Text("每个颜色通道都是一个矩阵", font_size=22, color=TEXT_COLOR),
            Text("三个矩阵堆叠 = 一个3D张量", font_size=22, color=NEURAL_COLOR),
        ).arrange(DOWN, buff=0.2)
        rgb_text.to_edge(DOWN, buff=0.8)
        
        self.play(Write(rgb_text), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_scalar(self, value):
        """创建标量表示"""
        scalar = VGroup()
        
        circle = Circle(radius=0.4, color=PRIMARY_COLOR, fill_opacity=0.3)
        circle.set_stroke(PRIMARY_COLOR, width=2)
        
        text = Text(value, font_size=22, color=TEXT_COLOR)
        text.move_to(circle.get_center())
        
        scalar.add(circle, text)
        return scalar
    
    def create_vector(self, values):
        """创建向量表示"""
        vector = VGroup()
        
        # 括号
        left_bracket = Text("[", font_size=32, color=SECONDARY_COLOR)
        right_bracket = Text("]", font_size=32, color=SECONDARY_COLOR)
        
        # 元素
        elements = VGroup()
        for v in values:
            elem = Text(v, font_size=20, color=TEXT_COLOR)
            elements.add(elem)
        elements.arrange(DOWN, buff=0.2)
        
        left_bracket.next_to(elements, LEFT, buff=0.1)
        right_bracket.next_to(elements, RIGHT, buff=0.1)
        
        vector.add(left_bracket, elements, right_bracket)
        return vector
    
    def create_matrix(self):
        """创建矩阵表示"""
        matrix = VGroup()
        
        # 3x3 网格
        data = [
            ["90", "85", "92"],
            ["78", "88", "95"],
            ["85", "90", "88"],
        ]
        
        cells = VGroup()
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                cell = Square(side_length=0.5, color=ACCENT_COLOR, fill_opacity=0.2)
                cell.set_stroke(ACCENT_COLOR, width=1)
                cell.move_to([j * 0.55, -i * 0.55, 0])
                
                text = Text(val, font_size=14, color=TEXT_COLOR)
                text.move_to(cell.get_center())
                
                cells.add(VGroup(cell, text))
        
        cells.move_to(ORIGIN)
        matrix.add(cells)
        return matrix
    
    def create_3d_tensor(self):
        """创建3D张量表示"""
        tensor = VGroup()
        
        colors = [ERROR_COLOR, SECONDARY_COLOR, PRIMARY_COLOR]  # R, G, B
        
        for k, color in enumerate(colors):
            layer = VGroup()
            for i in range(3):
                for j in range(3):
                    cell = Square(side_length=0.35, color=color, fill_opacity=0.4)
                    cell.set_stroke(color, width=1)
                    cell.move_to([j * 0.4 + k * 0.3, -i * 0.4 - k * 0.3, 0])
                    layer.add(cell)
            tensor.add(layer)
        
        return tensor
    
    def create_rgb_decomposition(self):
        """创建RGB分解图"""
        demo = VGroup()
        
        # 原始图片
        original = VGroup()
        original_frame = Square(side_length=2, color=TEXT_COLOR, fill_opacity=0)
        original_frame.set_stroke(TEXT_COLOR, width=2)
        
        # 简化的图片内容
        img_content = VGroup()
        for i in range(4):
            for j in range(4):
                color = interpolate_color(
                    ManimColor(PRIMARY_COLOR), ManimColor(ERROR_COLOR),
                    (i + j) / 6
                )
                cell = Square(side_length=0.45, color=color, fill_opacity=0.8)
                cell.move_to([(j - 1.5) * 0.48, (1.5 - i) * 0.48, 0])
                img_content.add(cell)
        
        img_content.move_to(original_frame.get_center())
        original_label = Text("原始图片", font_size=18, color=TEXT_COLOR)
        original_label.next_to(original_frame, DOWN, buff=0.2)
        
        original.add(original_frame, img_content, original_label)
        original.move_to(LEFT * 4)
        
        # 箭头
        arrow = Arrow(LEFT * 2.5, LEFT * 0.5, color=TEXT_COLOR, stroke_width=2)
        arrow_label = Text("分解", font_size=18, color=SUBTEXT_COLOR)
        arrow_label.next_to(arrow, UP, buff=0.1)
        
        # 三个通道
        channels = VGroup()
        channel_colors = [
            (ERROR_COLOR, "R 红色通道"),
            (SECONDARY_COLOR, "G 绿色通道"),
            (PRIMARY_COLOR, "B 蓝色通道"),
        ]
        
        for idx, (color, label) in enumerate(channel_colors):
            channel = VGroup()
            
            frame = Square(side_length=1.5, color=color, fill_opacity=0)
            frame.set_stroke(color, width=2)
            
            # 灰度值
            content = VGroup()
            for i in range(3):
                for j in range(3):
                    intensity = 0.3 + (i + j) * 0.1
                    cell = Square(side_length=0.45, color=color, fill_opacity=intensity)
                    cell.move_to([(j - 1) * 0.48, (1 - i) * 0.48, 0])
                    content.add(cell)
            
            content.move_to(frame.get_center())
            
            channel_label = Text(label, font_size=14, color=color)
            channel_label.next_to(frame, DOWN, buff=0.15)
            
            channel.add(frame, content, channel_label)
            channels.add(channel)
        
        channels.arrange(RIGHT, buff=0.3)
        channels.move_to(RIGHT * 2.5)
        
        demo.add(original, arrow, arrow_label, channels)
        return demo
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = GPUTensorScene()
    scene.render()
