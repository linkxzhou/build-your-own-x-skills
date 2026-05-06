"""
场景3: 引擎室 - GPU、TPU与张量
基于content.md - 展示深度学习的计算基础和张量变形记

运行命令:
    manim -pql scene_03_gpu_tensor.py GPUTensorScene
    manim -pqh scene_03_gpu_tensor.py GPUTensorScene
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
    """场景3: 引擎室 - GPU、TPU与张量"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 为什么是GPU
        self.show_why_gpu()
        
        # 2. CPU vs GPU 对比
        self.show_cpu_vs_gpu()
        
        # 3. TPU简介
        self.show_tpu_intro()
        
        # 4. 张量变形记（核心动画）
        self.show_tensor_evolution()
        
        # 5. 深度学习框架
        self.show_frameworks()
        
        self.clear_scene()
    
    def show_why_gpu(self):
        """为什么是GPU"""
        # 标题
        title = Text("引擎室", font_size=48, color=ACCENT_COLOR)
        subtitle = Text("深度学习的计算基础", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        title_group = VGroup(title, subtitle)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        self.wait(1)
        
        # 过渡
        self.play(
            title_group.animate.scale(0.6).to_edge(UP, buff=0.3),
            run_time=0.6
        )
        
        # GPU历史
        history_title = Text("为什么是 GPU?", font_size=32, color=ACCENT_COLOR)
        history_title.next_to(title_group, DOWN, buff=0.4)
        
        self.play(Write(history_title), run_time=0.5)
        
        # 游戏场景
        game_icon = self.create_game_icon()
        game_icon.scale(0.8)
        game_icon.next_to(history_title, DOWN, buff=0.5).shift(LEFT * 3)
        
        game_label = Text("🎮 游戏画面渲染", font_size=20, color=SECONDARY_COLOR)
        game_label.next_to(game_icon, DOWN, buff=0.2)
        
        self.play(FadeIn(game_icon), Write(game_label), run_time=0.6)
        
        # 箭头
        arrow = Arrow(
            game_icon.get_right() + RIGHT * 0.3,
            game_icon.get_right() + RIGHT * 2.5,
            color=ACCENT_COLOR, stroke_width=3
        )
        
        self.play(GrowArrow(arrow), run_time=0.4)
        
        # 神经网络计算
        nn_icon = self.create_simple_nn()
        nn_icon.scale(0.6)
        nn_icon.next_to(arrow, RIGHT, buff=0.3)
        
        nn_label = Text("🧠 神经网络计算", font_size=20, color=PRIMARY_COLOR)
        nn_label.next_to(nn_icon, DOWN, buff=0.2)
        
        self.play(FadeIn(nn_icon), Write(nn_label), run_time=0.6)
        
        # 关键洞察
        insight = VGroup(
            Text("GPU擅长:", font_size=20, color=TEXT_COLOR),
            Text("同时进行成千上万次简单计算", font_size=18, color=SECONDARY_COLOR),
            Text("（并行计算）", font_size=16, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        insight.to_edge(DOWN, buff=0.8)
        
        self.play(Write(insight), run_time=0.8)
        
        # 惊喜发现
        surprise = Text(
            "游戏产业意外推动了AI革命！",
            font_size=22, color=ACCENT_COLOR
        )
        surprise.next_to(insight, UP, buff=0.3)
        
        self.play(Write(surprise), run_time=0.6)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_cpu_vs_gpu(self):
        """CPU vs GPU 对比"""
        # 标题
        title = Text("CPU vs GPU", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # CPU
        cpu_group = VGroup()
        cpu_title = Text("CPU", font_size=28, color=PRIMARY_COLOR)
        
        # CPU核心 - 少量大核心
        cpu_cores = VGroup()
        for i in range(4):
            core = Square(side_length=0.7, color=PRIMARY_COLOR, fill_opacity=0.5)
            core.set_stroke(PRIMARY_COLOR, width=2)
            cpu_cores.add(core)
        cpu_cores.arrange_in_grid(rows=2, cols=2, buff=0.15)
        
        cpu_desc = Text("4-16 个强力核心", font_size=16, color=PRIMARY_COLOR)
        cpu_analogy = Text("'一次做一件大事'", font_size=14, color=SUBTEXT_COLOR)
        
        cpu_group.add(cpu_title, cpu_cores, cpu_desc, cpu_analogy)
        cpu_group.arrange(DOWN, buff=0.25)
        cpu_group.move_to(LEFT * 3)
        
        # GPU
        gpu_group = VGroup()
        gpu_title = Text("GPU", font_size=28, color=SECONDARY_COLOR)
        
        # GPU核心 - 大量小核心
        gpu_cores = VGroup()
        for i in range(100):
            core = Square(side_length=0.11, color=SECONDARY_COLOR, fill_opacity=0.5)
            core.set_stroke(SECONDARY_COLOR, width=0.5)
            gpu_cores.add(core)
        gpu_cores.arrange_in_grid(rows=10, cols=10, buff=0.02)
        
        gpu_desc = Text("数千个小核心", font_size=16, color=SECONDARY_COLOR)
        gpu_analogy = Text("'同时做很多小事'", font_size=14, color=SUBTEXT_COLOR)
        
        gpu_group.add(gpu_title, gpu_cores, gpu_desc, gpu_analogy)
        gpu_group.arrange(DOWN, buff=0.25)
        gpu_group.move_to(RIGHT * 3)
        
        # VS
        vs_text = Text("vs", font_size=32, color=TEXT_COLOR)
        
        self.play(
            FadeIn(cpu_group),
            Write(vs_text),
            run_time=0.8
        )
        
        self.play(FadeIn(gpu_group, lag_ratio=0.005), run_time=1)
        
        # 高亮GPU核心 - 模拟并行计算
        self.play(
            gpu_cores.animate.set_fill(SECONDARY_COLOR, opacity=0.9),
            Flash(gpu_cores.get_center(), color=SECONDARY_COLOR, line_length=0.5),
            run_time=0.6
        )
        
        # 应用说明
        use_case = Text(
            "神经网络每层的计算正好需要这种并行能力!",
            font_size=20, color=ACCENT_COLOR
        )
        use_case.to_edge(DOWN, buff=0.6)
        
        self.play(Write(use_case), run_time=0.6)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_tpu_intro(self):
        """TPU简介"""
        # 标题
        title = Text("TPU — 张量处理器", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # Google logo 提示
        google_text = Text("谷歌专门为深度学习设计的定制芯片", font_size=22, color=TEXT_COLOR)
        google_text.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(google_text), run_time=0.5)
        
        # TPU芯片可视化
        tpu_chip = self.create_tpu_chip()
        tpu_chip.scale(0.8)
        tpu_chip.next_to(google_text, DOWN, buff=0.6)
        
        self.play(FadeIn(tpu_chip, scale=0.9), run_time=0.6)
        
        # 对比
        comparison = VGroup(
            VGroup(
                Text("GPU", font_size=20, color=SECONDARY_COLOR),
                Text("= 瑞士军刀", font_size=18, color=TEXT_COLOR),
                Text("（通用但不专精）", font_size=14, color=SUBTEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
            Text("→", font_size=24, color=TEXT_COLOR),
            VGroup(
                Text("TPU", font_size=20, color=NEURAL_COLOR),
                Text("= 专业厨刀", font_size=18, color=TEXT_COLOR),
                Text("（针对张量运算深度优化）", font_size=14, color=SUBTEXT_COLOR),
            ).arrange(DOWN, buff=0.1),
        ).arrange(RIGHT, buff=0.8)
        comparison.next_to(tpu_chip, DOWN, buff=0.5)
        
        self.play(FadeIn(comparison, lag_ratio=0.2), run_time=0.8)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_tensor_evolution(self):
        """张量变形记 - 核心动画"""
        # 标题
        title = Text("张量变形记", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 1. 标量 - 一个孤零零的数字
        scalar_label = Text("标量 (0维)", font_size=22, color=PRIMARY_COLOR)
        scalar_label.next_to(title, DOWN, buff=0.5).shift(LEFT * 4.5)
        
        scalar = self.create_scalar("5")
        scalar.next_to(scalar_label, DOWN, buff=0.3)
        
        scalar_desc = Text("一个孤零零的数字", font_size=14, color=SUBTEXT_COLOR)
        scalar_desc.next_to(scalar, DOWN, buff=0.2)
        
        self.play(Write(scalar_label), run_time=0.3)
        self.play(FadeIn(scalar, scale=1.2), run_time=0.4)
        self.play(Write(scalar_desc), run_time=0.3)
        
        self.wait(0.5)
        
        # 2. 向量 - 复制排成一列
        vector_label = Text("向量 (1维)", font_size=22, color=SECONDARY_COLOR)
        vector_label.align_to(scalar_label, UP).shift(RIGHT * 3)
        
        # 动画：标量复制成向量
        vector = self.create_vector(["5", "2", "8"])
        vector.next_to(vector_label, DOWN, buff=0.3)
        
        vector_desc = Text("复制排成一列", font_size=14, color=SUBTEXT_COLOR)
        vector_desc.next_to(vector, DOWN, buff=0.2)
        
        # 复制动画
        scalar_copy = scalar.copy()
        self.play(Write(vector_label), run_time=0.3)
        self.play(
            scalar_copy.animate.move_to(vector.get_center()),
            FadeOut(scalar_copy),
            FadeIn(vector),
            run_time=0.6
        )
        self.play(Write(vector_desc), run_time=0.3)
        
        self.wait(0.5)
        
        # 3. 矩阵 - 横向复制形成表格
        matrix_label = Text("矩阵 (2维)", font_size=22, color=ACCENT_COLOR)
        matrix_label.align_to(scalar_label, UP).shift(RIGHT * 6)
        
        matrix = self.create_matrix_visual()
        matrix.next_to(matrix_label, DOWN, buff=0.3)
        
        matrix_desc = Text("表格 / 灰度图", font_size=14, color=SUBTEXT_COLOR)
        matrix_desc.next_to(matrix, DOWN, buff=0.2)
        
        self.play(Write(matrix_label), run_time=0.3)
        self.play(FadeIn(matrix, scale=0.9), run_time=0.5)
        self.play(Write(matrix_desc), run_time=0.3)
        
        self.wait(0.5)
        
        # 4. 3D张量 - RGB图片
        tensor_label = Text("张量 (3维)", font_size=22, color=NEURAL_COLOR)
        tensor_label.align_to(scalar_label, UP).shift(RIGHT * 9)
        
        tensor_3d = self.create_3d_tensor_visual()
        tensor_3d.scale(0.8)
        tensor_3d.next_to(tensor_label, DOWN, buff=0.3)
        
        tensor_desc = Text("RGB图片: 通道×高×宽", font_size=14, color=SUBTEXT_COLOR)
        tensor_desc.next_to(tensor_3d, DOWN, buff=0.2)
        
        self.play(Write(tensor_label), run_time=0.3)
        self.play(FadeIn(tensor_3d, scale=0.9), run_time=0.5)
        self.play(Write(tensor_desc), run_time=0.3)
        
        self.wait(1)
        
        # 清理并展示批量
        self.play(
            FadeOut(scalar_label), FadeOut(scalar), FadeOut(scalar_desc),
            FadeOut(vector_label), FadeOut(vector), FadeOut(vector_desc),
            FadeOut(matrix_label), FadeOut(matrix), FadeOut(matrix_desc),
            FadeOut(tensor_label), FadeOut(tensor_3d), FadeOut(tensor_desc),
            run_time=0.5
        )
        
        # 批量张量
        batch_title = Text("批量处理 (4维)", font_size=28, color=ACCENT_COLOR)
        batch_title.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(batch_title), run_time=0.4)
        
        # 多个3D张量
        batch = VGroup()
        for i in range(4):
            cube = self.create_3d_tensor_visual()
            cube.scale(0.5)
            batch.add(cube)
        batch.arrange(RIGHT, buff=0.3)
        batch.next_to(batch_title, DOWN, buff=0.5)
        
        self.play(FadeIn(batch, lag_ratio=0.2), run_time=0.8)
        
        batch_desc = Text(
            "批量 × 通道 × 高 × 宽",
            font_size=22, color=TEXT_COLOR
        )
        batch_desc.next_to(batch, DOWN, buff=0.3)
        
        self.play(Write(batch_desc), run_time=0.5)
        
        # 数据流动效果
        flow_text = Text(
            "所有运算表现为张量间流光溢彩的数据流动",
            font_size=18, color=SECONDARY_COLOR
        )
        flow_text.to_edge(DOWN, buff=0.6)
        
        self.play(Write(flow_text), run_time=0.6)
        
        # 流动动画
        self.play(
            batch[0].animate.set_fill(PRIMARY_COLOR, opacity=0.8),
            run_time=0.3
        )
        for i in range(1, 4):
            self.play(
                batch[i-1].animate.set_fill(opacity=0.5),
                batch[i].animate.set_fill(SECONDARY_COLOR, opacity=0.8),
                run_time=0.2
            )
        self.play(batch[3].animate.set_fill(opacity=0.5), run_time=0.2)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_frameworks(self):
        """深度学习框架"""
        # 标题
        title = Text("深度学习框架", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 框架
        frameworks = VGroup()
        fw_data = [
            ("PyTorch", "研究首选\n灵活易用", PRIMARY_COLOR),
            ("TensorFlow", "工业级部署\n完整生态", SECONDARY_COLOR),
            ("JAX", "谷歌新秀\n函数式编程", NEURAL_COLOR),
        ]
        
        for name, desc, color in fw_data:
            fw = VGroup()
            box = RoundedRectangle(
                width=3, height=2,
                corner_radius=0.15,
                color=color,
                fill_opacity=0.2
            )
            box.set_stroke(color, width=2)
            
            fw_name = Text(name, font_size=24, color=color)
            fw_name.move_to(box.get_center() + UP * 0.4)
            
            fw_desc = Text(desc, font_size=14, color=TEXT_COLOR, line_spacing=1.2)
            fw_desc.next_to(fw_name, DOWN, buff=0.2)
            
            fw.add(box, fw_name, fw_desc)
            frameworks.add(fw)
        
        frameworks.arrange(RIGHT, buff=0.5)
        frameworks.next_to(title, DOWN, buff=0.6)
        
        self.play(FadeIn(frameworks, lag_ratio=0.2), run_time=1)
        
        # 核心功能
        core_func = VGroup(
            Text("核心功能:", font_size=22, color=ACCENT_COLOR),
            Text("• 高效操作'张量乐高'", font_size=18, color=TEXT_COLOR),
            Text("• 构建计算图", font_size=18, color=TEXT_COLOR),
            Text("• 自动微分", font_size=18, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        core_func.to_edge(DOWN, buff=0.6)
        
        self.play(Write(core_func), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_game_icon(self):
        """创建游戏图标"""
        icon = VGroup()
        
        # 屏幕
        screen = Rectangle(
            width=2, height=1.5,
            color=SECONDARY_COLOR,
            fill_opacity=0.3
        )
        screen.set_stroke(SECONDARY_COLOR, width=2)
        
        # 像素块
        for i in range(3):
            for j in range(2):
                pixel = Square(
                    side_length=0.25,
                    color=interpolate_color(ManimColor(PRIMARY_COLOR), ManimColor(SECONDARY_COLOR), (i+j)/4),
                    fill_opacity=0.6
                )
                pixel.move_to(screen.get_center() + np.array([
                    (i - 1) * 0.35, (j - 0.5) * 0.35, 0
                ]))
                icon.add(pixel)
        
        icon.add(screen)
        return icon
    
    def create_simple_nn(self):
        """创建简单神经网络图标"""
        nn = VGroup()
        
        layers = [3, 4, 2]
        all_nodes = []
        
        for i, size in enumerate(layers):
            layer_nodes = []
            for j in range(size):
                node = Circle(
                    radius=0.12,
                    color=NEURAL_COLOR,
                    fill_opacity=0.6
                )
                node.move_to([i * 0.8, (size - 1) / 2 * 0.35 - j * 0.35, 0])
                layer_nodes.append(node)
                nn.add(node)
            all_nodes.append(layer_nodes)
        
        # 连接
        for i in range(len(layers) - 1):
            for n1 in all_nodes[i]:
                for n2 in all_nodes[i + 1]:
                    line = Line(
                        n1.get_center(), n2.get_center(),
                        stroke_width=0.5, color=NEURAL_COLOR, stroke_opacity=0.4
                    )
                    nn.add(line)
        
        return nn
    
    def create_tpu_chip(self):
        """创建TPU芯片图标"""
        chip = VGroup()
        
        # 主体
        body = RoundedRectangle(
            width=2, height=2,
            corner_radius=0.1,
            color=NEURAL_COLOR,
            fill_opacity=0.4
        )
        body.set_stroke(NEURAL_COLOR, width=2)
        
        # 内部矩阵单元
        for i in range(4):
            for j in range(4):
                unit = Square(
                    side_length=0.3,
                    color=NEURAL_COLOR,
                    fill_opacity=0.6
                )
                unit.move_to(body.get_center() + np.array([
                    (i - 1.5) * 0.38, (j - 1.5) * 0.38, 0
                ]))
                chip.add(unit)
        
        # 引脚
        for side in [UP, DOWN]:
            for i in range(5):
                pin = Line(
                    body.get_edge_center(side) + LEFT * 0.7 + RIGHT * i * 0.35,
                    body.get_edge_center(side) + side * 0.2 + LEFT * 0.7 + RIGHT * i * 0.35,
                    color=NEURAL_COLOR, stroke_width=2
                )
                chip.add(pin)
        
        chip.add(body)
        return chip
    
    def create_scalar(self, value):
        """创建标量表示"""
        scalar = VGroup()
        
        circle = Circle(radius=0.4, color=PRIMARY_COLOR, fill_opacity=0.4)
        circle.set_stroke(PRIMARY_COLOR, width=2)
        
        text = Text(value, font_size=28, color=TEXT_COLOR)
        text.move_to(circle.get_center())
        
        scalar.add(circle, text)
        return scalar
    
    def create_vector(self, values):
        """创建向量表示"""
        vector = VGroup()
        
        # 元素
        for i, v in enumerate(values):
            cell = Square(side_length=0.5, color=SECONDARY_COLOR, fill_opacity=0.4)
            cell.set_stroke(SECONDARY_COLOR, width=2)
            cell.move_to([0, -i * 0.55, 0])
            
            text = Text(v, font_size=20, color=TEXT_COLOR)
            text.move_to(cell.get_center())
            
            vector.add(cell, text)
        
        return vector
    
    def create_matrix_visual(self):
        """创建矩阵可视化"""
        matrix = VGroup()
        
        data = [
            ["5", "2", "8"],
            ["1", "3", "4"],
        ]
        
        for i, row in enumerate(data):
            for j, val in enumerate(row):
                cell = Square(side_length=0.45, color=ACCENT_COLOR, fill_opacity=0.35)
                cell.set_stroke(ACCENT_COLOR, width=1.5)
                cell.move_to([j * 0.5, -i * 0.5, 0])
                
                text = Text(val, font_size=16, color=TEXT_COLOR)
                text.move_to(cell.get_center())
                
                matrix.add(cell, text)
        
        return matrix
    
    def create_3d_tensor_visual(self):
        """创建3D张量可视化（RGB层叠）"""
        tensor = VGroup()
        
        colors = [ERROR_COLOR, SECONDARY_COLOR, PRIMARY_COLOR]  # R, G, B
        
        for k, color in enumerate(colors):
            layer = VGroup()
            for i in range(3):
                for j in range(3):
                    cell = Square(side_length=0.3, color=color, fill_opacity=0.5)
                    cell.set_stroke(color, width=1)
                    cell.move_to([j * 0.35 + k * 0.25, -i * 0.35 - k * 0.25, 0])
                    layer.add(cell)
            tensor.add(layer)
        
        return tensor
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = GPUTensorScene()
    scene.render()
