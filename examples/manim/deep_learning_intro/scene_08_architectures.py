"""
场景8: 经典架构
展示MLP、CNN、Transformer等著名模型

运行命令:
    manim -pql scene_08_architectures.py ArchitecturesScene
    manim -pqh scene_08_architectures.py ArchitecturesScene
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


class ArchitecturesScene(Scene):
    """场景8: 经典架构"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 引入
        self.show_intro()
        
        # 2. MLP
        self.show_mlp()
        
        # 3. CNN/ResNet
        self.show_cnn_resnet()
        
        # 4. Transformer
        self.show_transformer()
        
        self.clear_scene()
    
    def show_intro(self):
        """引入"""
        # 标题
        title = Text("第五部分：经典架构", font_size=40, color=ACCENT_COLOR)
        subtitle = Text("明星AI模型的'设计图纸'", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.3)
        
        title_group = VGroup(title, subtitle)
        title_group.to_edge(UP, buff=0.8)
        
        self.play(Write(title), run_time=0.8)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.5)
        
        # 三大架构预览
        archs = VGroup()
        
        arch_data = [
            ("MLP", "多层感知机", PRIMARY_COLOR),
            ("CNN", "卷积神经网络", SECONDARY_COLOR),
            ("Transformer", "变换器", NEURAL_COLOR),
        ]
        
        for name, cn_name, color in arch_data:
            arch = VGroup()
            box = RoundedRectangle(
                width=2.5, height=1.5,
                corner_radius=0.15,
                color=color,
                fill_opacity=0.3
            )
            box.set_stroke(color, width=2)
            
            en_text = Text(name, font_size=24, color=color)
            cn_text = Text(cn_name, font_size=16, color=TEXT_COLOR)
            
            en_text.move_to(box.get_center() + UP * 0.2)
            cn_text.next_to(en_text, DOWN, buff=0.15)
            
            arch.add(box, en_text, cn_text)
            archs.add(arch)
        
        archs.arrange(RIGHT, buff=0.8)
        archs.next_to(subtitle, DOWN, buff=0.8)
        
        self.play(FadeIn(archs, lag_ratio=0.2), run_time=1)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_mlp(self):
        """多层感知机展示"""
        # 标题
        title = Text("1. 多层感知机 (MLP)", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 描述
        desc = Text("最古老的深度架构", font_size=24, color=SUBTEXT_COLOR)
        desc.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(desc), run_time=0.3)
        
        # MLP 结构图
        mlp = self.create_mlp_diagram()
        mlp.next_to(desc, DOWN, buff=0.5)
        
        self.play(FadeIn(mlp), run_time=0.8)
        
        # 结构说明
        structure = VGroup(
            Text("线性层", font_size=20, color=PRIMARY_COLOR),
            Text("+", font_size=20, color=TEXT_COLOR),
            Text("激活函数", font_size=20, color=SECONDARY_COLOR),
            Text("反复叠加", font_size=20, color=ACCENT_COLOR),
        ).arrange(RIGHT, buff=0.3)
        structure.next_to(mlp, DOWN, buff=0.4)
        
        self.play(Write(structure), run_time=0.6)
        
        # 特点
        features = VGroup(
            Text("✓ 简单、通用", font_size=18, color=TEXT_COLOR),
            Text("✓ 可作为复杂模型的一部分", font_size=18, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        features.next_to(structure, DOWN, buff=0.4)
        
        self.play(Write(features), run_time=0.5)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_cnn_resnet(self):
        """CNN和ResNet展示"""
        # 标题
        title = Text("2. 卷积神经网络 (CNN)", font_size=36, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 描述
        desc = Text("专门为图像处理设计的'王者'", font_size=24, color=TEXT_COLOR)
        desc.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(desc), run_time=0.4)
        
        # CNN 基本结构
        cnn_structure = self.create_cnn_diagram()
        cnn_structure.scale(0.85)
        cnn_structure.next_to(desc, DOWN, buff=0.4)
        
        self.play(FadeIn(cnn_structure), run_time=0.8)
        
        # 发展历程
        history = VGroup(
            Text("LeNet", font_size=18, color=SUBTEXT_COLOR),
            Text("→", font_size=18, color=TEXT_COLOR),
            Text("AlexNet", font_size=18, color=SUBTEXT_COLOR),
            Text("→", font_size=18, color=TEXT_COLOR),
            Text("VGG", font_size=18, color=SUBTEXT_COLOR),
            Text("→", font_size=18, color=TEXT_COLOR),
            Text("ResNet", font_size=18, color=ACCENT_COLOR),
        ).arrange(RIGHT, buff=0.2)
        history.next_to(cnn_structure, DOWN, buff=0.3)
        
        self.play(Write(history), run_time=0.8)
        
        self.wait(0.5)
        
        # ResNet 重点
        self.play(
            FadeOut(cnn_structure),
            history.animate.shift(UP * 1.5),
        )
        
        resnet_title = Text("ResNet — 残差网络", font_size=28, color=ACCENT_COLOR)
        resnet_title.next_to(history, DOWN, buff=0.4)
        
        self.play(Write(resnet_title), run_time=0.4)
        
        # 残差块
        resblock = self.create_residual_block()
        resblock.next_to(resnet_title, DOWN, buff=0.3)
        
        self.play(FadeIn(resblock), run_time=0.8)
        
        # 说明
        resnet_desc = VGroup(
            Text("核心创新: 残差块 (Residual Block)", font_size=20, color=TEXT_COLOR),
            Text("学习'残差'(差值)而非直接映射", font_size=18, color=SUBTEXT_COLOR),
            Text("→ 成功训练上百层的超深网络!", font_size=18, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.15)
        resnet_desc.next_to(resblock, DOWN, buff=0.3)
        
        for line in resnet_desc:
            self.play(Write(line), run_time=0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    
    def show_transformer(self):
        """Transformer展示"""
        # 标题
        title = Text("3. Transformer", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 描述
        desc = Text("自然语言处理领域的革命者，现已横扫各领域", font_size=22, color=TEXT_COLOR)
        desc.next_to(title, DOWN, buff=0.3)
        
        self.play(Write(desc), run_time=0.5)
        
        # Transformer 结构
        transformer = self.create_transformer_diagram()
        transformer.scale(0.9)
        transformer.next_to(desc, DOWN, buff=0.4)
        
        self.play(FadeIn(transformer), run_time=0.8)
        
        # 核心组件
        components = VGroup(
            Text("核心组件:", font_size=22, color=ACCENT_COLOR),
            VGroup(
                Text("• 自注意力层", font_size=18, color=PRIMARY_COLOR),
                Text("(Self-Attention)", font_size=14, color=SUBTEXT_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("• 前馈网络", font_size=18, color=SECONDARY_COLOR),
                Text("(Feed-Forward)", font_size=14, color=SUBTEXT_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("• 跳跃连接 + 层归一化", font_size=18, color=TEXT_COLOR),
            ),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        components.next_to(transformer, RIGHT, buff=0.5)
        
        self.play(Write(components), run_time=1)
        
        # 应用
        apps = VGroup(
            Text("基于Transformer:", font_size=20, color=ACCENT_COLOR),
            Text("• GPT系列 (文本生成)", font_size=16, color=TEXT_COLOR),
            Text("• BERT (文本理解)", font_size=16, color=TEXT_COLOR),
            Text("• ViT (图像分类)", font_size=16, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        apps.to_edge(DOWN, buff=0.6)
        
        self.play(Write(apps), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_mlp_diagram(self):
        """创建MLP结构图"""
        mlp = VGroup()
        
        layer_sizes = [4, 6, 6, 3]
        layer_colors = [PRIMARY_COLOR, NEURAL_COLOR, NEURAL_COLOR, ACCENT_COLOR]
        
        layers = VGroup()
        all_neurons = []
        
        for i, (size, color) in enumerate(zip(layer_sizes, layer_colors)):
            layer = VGroup()
            neurons = []
            
            for j in range(size):
                neuron = Circle(
                    radius=0.15,
                    color=color,
                    fill_opacity=0.5
                )
                neuron.set_stroke(color, width=2)
                y_pos = (size - 1) / 2 * 0.5 - j * 0.5
                neuron.move_to([i * 1.8, y_pos, 0])
                layer.add(neuron)
                neurons.append(neuron)
            
            layers.add(layer)
            all_neurons.append(neurons)
        
        # 连接线
        connections = VGroup()
        for i in range(len(layer_sizes) - 1):
            for n1 in all_neurons[i]:
                for n2 in all_neurons[i + 1]:
                    line = Line(
                        n1.get_center(), n2.get_center(),
                        stroke_width=0.5,
                        stroke_opacity=0.3,
                        color=TEXT_COLOR
                    )
                    connections.add(line)
        
        # 层标签
        labels = VGroup(
            Text("输入", font_size=14, color=PRIMARY_COLOR),
            Text("隐藏层", font_size=14, color=NEURAL_COLOR),
            Text("隐藏层", font_size=14, color=NEURAL_COLOR),
            Text("输出", font_size=14, color=ACCENT_COLOR),
        )
        
        for i, label in enumerate(labels):
            label.next_to(layers[i], DOWN, buff=0.3)
        
        mlp.add(connections, layers, labels)
        mlp.move_to(ORIGIN)
        
        return mlp
    
    def create_cnn_diagram(self):
        """创建CNN结构图"""
        cnn = VGroup()
        
        # 输入图像
        input_img = self.create_feature_map(1.5, 1.5, PRIMARY_COLOR, "输入")
        
        # 卷积层1
        conv1 = self.create_feature_map(1.2, 1.2, SECONDARY_COLOR, "Conv")
        conv1.next_to(input_img, RIGHT, buff=0.5)
        
        # 池化
        pool1 = self.create_feature_map(0.8, 0.8, ACCENT_COLOR, "Pool")
        pool1.next_to(conv1, RIGHT, buff=0.5)
        
        # 卷积层2
        conv2 = self.create_feature_map(0.6, 0.6, SECONDARY_COLOR, "Conv")
        conv2.next_to(pool1, RIGHT, buff=0.5)
        
        # 全连接层
        fc = RoundedRectangle(
            width=0.4, height=1.2,
            corner_radius=0.05,
            color=NEURAL_COLOR,
            fill_opacity=0.4
        )
        fc.set_stroke(NEURAL_COLOR, width=2)
        fc.next_to(conv2, RIGHT, buff=0.5)
        fc_label = Text("FC", font_size=12, color=TEXT_COLOR)
        fc_label.move_to(fc.get_center())
        
        # 输出
        output = Circle(radius=0.3, color=ERROR_COLOR, fill_opacity=0.4)
        output.set_stroke(ERROR_COLOR, width=2)
        output.next_to(fc, RIGHT, buff=0.5)
        out_label = Text("输出", font_size=12, color=TEXT_COLOR)
        out_label.next_to(output, DOWN, buff=0.1)
        
        # 箭头
        arrows = VGroup()
        elements = [input_img, conv1, pool1, conv2, VGroup(fc, fc_label), output]
        for i in range(len(elements) - 1):
            arrow = Arrow(
                elements[i].get_right(),
                elements[i + 1].get_left(),
                buff=0.1,
                stroke_width=2,
                color=TEXT_COLOR
            )
            arrows.add(arrow)
        
        cnn.add(input_img, conv1, pool1, conv2, fc, fc_label, output, out_label, arrows)
        cnn.move_to(ORIGIN)
        
        return cnn
    
    def create_feature_map(self, width, height, color, label_text):
        """创建特征图"""
        fm = VGroup()
        
        rect = Rectangle(
            width=width, height=height,
            color=color,
            fill_opacity=0.3
        )
        rect.set_stroke(color, width=2)
        
        label = Text(label_text, font_size=12, color=TEXT_COLOR)
        label.next_to(rect, DOWN, buff=0.1)
        
        fm.add(rect, label)
        return fm
    
    def create_residual_block(self):
        """创建残差块"""
        block = VGroup()
        
        # 主路径
        input_node = Circle(radius=0.2, color=PRIMARY_COLOR, fill_opacity=0.5)
        input_node.set_stroke(PRIMARY_COLOR, width=2)
        input_label = Text("x", font_size=16, color=TEXT_COLOR)
        input_label.move_to(input_node.get_center())
        
        # 层
        layer1 = RoundedRectangle(
            width=1.2, height=0.6,
            corner_radius=0.1,
            color=NEURAL_COLOR,
            fill_opacity=0.4
        )
        layer1.set_stroke(NEURAL_COLOR, width=2)
        layer1.next_to(input_node, RIGHT, buff=0.5)
        l1_text = Text("Conv+ReLU", font_size=10, color=TEXT_COLOR)
        l1_text.move_to(layer1.get_center())
        
        layer2 = layer1.copy()
        layer2.next_to(layer1, RIGHT, buff=0.5)
        l2_text = Text("Conv", font_size=10, color=TEXT_COLOR)
        l2_text.move_to(layer2.get_center())
        
        # 加法节点
        add_node = Circle(radius=0.2, color=ACCENT_COLOR, fill_opacity=0.5)
        add_node.set_stroke(ACCENT_COLOR, width=2)
        add_node.next_to(layer2, RIGHT, buff=0.5)
        add_text = Text("+", font_size=20, color=TEXT_COLOR)
        add_text.move_to(add_node.get_center())
        
        # 输出
        output_node = Circle(radius=0.2, color=SECONDARY_COLOR, fill_opacity=0.5)
        output_node.set_stroke(SECONDARY_COLOR, width=2)
        output_node.next_to(add_node, RIGHT, buff=0.5)
        output_label = Text("F(x)+x", font_size=14, color=TEXT_COLOR)
        output_label.next_to(output_node, DOWN, buff=0.1)
        
        # 连接线
        main_path = VGroup(
            Arrow(input_node.get_right(), layer1.get_left(), buff=0.05, stroke_width=2, color=TEXT_COLOR),
            Arrow(layer1.get_right(), layer2.get_left(), buff=0.05, stroke_width=2, color=TEXT_COLOR),
            Arrow(layer2.get_right(), add_node.get_left(), buff=0.05, stroke_width=2, color=TEXT_COLOR),
            Arrow(add_node.get_right(), output_node.get_left(), buff=0.05, stroke_width=2, color=TEXT_COLOR),
        )
        
        # 跳跃连接
        skip_path = CurvedArrow(
            input_node.get_top() + UP * 0.1,
            add_node.get_top() + UP * 0.1,
            angle=-TAU / 4,
            color=SECONDARY_COLOR,
            stroke_width=3
        )
        skip_label = Text("跳跃连接 (恒等映射)", font_size=12, color=SECONDARY_COLOR)
        skip_label.next_to(skip_path, UP, buff=0.05)
        
        block.add(
            input_node, input_label,
            layer1, l1_text,
            layer2, l2_text,
            add_node, add_text,
            output_node, output_label,
            main_path, skip_path, skip_label
        )
        
        block.move_to(ORIGIN)
        return block
    
    def create_transformer_diagram(self):
        """创建Transformer结构图"""
        transformer = VGroup()
        
        # Encoder 块
        encoder = VGroup()
        
        enc_box = RoundedRectangle(
            width=2.5, height=3,
            corner_radius=0.15,
            color=PRIMARY_COLOR,
            fill_opacity=0.2
        )
        enc_box.set_stroke(PRIMARY_COLOR, width=2)
        
        enc_title = Text("Encoder", font_size=18, color=PRIMARY_COLOR)
        enc_title.next_to(enc_box, UP, buff=0.1)
        
        # 内部组件
        mha = RoundedRectangle(
            width=2, height=0.6,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.4
        )
        mha.move_to(enc_box.get_center() + UP * 0.8)
        mha_text = Text("Multi-Head\nAttention", font_size=10, color=TEXT_COLOR)
        mha_text.move_to(mha.get_center())
        
        ff = RoundedRectangle(
            width=2, height=0.6,
            corner_radius=0.1,
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        )
        ff.move_to(enc_box.get_center() + DOWN * 0.3)
        ff_text = Text("Feed Forward", font_size=12, color=TEXT_COLOR)
        ff_text.move_to(ff.get_center())
        
        # Add & Norm
        an1 = Text("Add & Norm", font_size=8, color=SUBTEXT_COLOR)
        an1.next_to(mha, DOWN, buff=0.1)
        an2 = Text("Add & Norm", font_size=8, color=SUBTEXT_COLOR)
        an2.next_to(ff, DOWN, buff=0.1)
        
        encoder.add(enc_box, enc_title, mha, mha_text, ff, ff_text, an1, an2)
        encoder.move_to(LEFT * 2)
        
        # Decoder 块
        decoder = VGroup()
        
        dec_box = RoundedRectangle(
            width=2.5, height=3.5,
            corner_radius=0.15,
            color=NEURAL_COLOR,
            fill_opacity=0.2
        )
        dec_box.set_stroke(NEURAL_COLOR, width=2)
        
        dec_title = Text("Decoder", font_size=18, color=NEURAL_COLOR)
        dec_title.next_to(dec_box, UP, buff=0.1)
        
        # 内部组件
        masked_mha = RoundedRectangle(
            width=2, height=0.6,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.4
        )
        masked_mha.move_to(dec_box.get_center() + UP * 1.1)
        masked_text = Text("Masked\nAttention", font_size=10, color=TEXT_COLOR)
        masked_text.move_to(masked_mha.get_center())
        
        cross_mha = RoundedRectangle(
            width=2, height=0.6,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.4
        )
        cross_mha.move_to(dec_box.get_center() + UP * 0.2)
        cross_text = Text("Cross\nAttention", font_size=10, color=TEXT_COLOR)
        cross_text.move_to(cross_mha.get_center())
        
        ff2 = RoundedRectangle(
            width=2, height=0.6,
            corner_radius=0.1,
            color=SECONDARY_COLOR,
            fill_opacity=0.4
        )
        ff2.move_to(dec_box.get_center() + DOWN * 0.7)
        ff2_text = Text("Feed Forward", font_size=12, color=TEXT_COLOR)
        ff2_text.move_to(ff2.get_center())
        
        decoder.add(dec_box, dec_title, masked_mha, masked_text, cross_mha, cross_text, ff2, ff2_text)
        decoder.move_to(RIGHT * 2)
        
        # 连接箭头
        cross_arrow = Arrow(
            enc_box.get_right(),
            cross_mha.get_left(),
            buff=0.1,
            stroke_width=2,
            color=TEXT_COLOR
        )
        
        transformer.add(encoder, decoder, cross_arrow)
        transformer.move_to(DOWN * 0.3)
        
        return transformer
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = ArchitecturesScene()
    scene.render()
