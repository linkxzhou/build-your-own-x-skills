"""
场景1: 开场序幕 - GPU驱动的智能新时代
基于《The Little Book of Deep Learning》- 展示2012年AlexNet的崛起

运行命令:
    manim -pql scene_01_intro.py IntroScene
    manim -pqh scene_01_intro.py IntroScene
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


class IntroScene(Scene):
    """场景1: 开场序幕 - GPU驱动的智能新时代"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 2012年ImageNet竞赛场景
        self.show_2012_imagenet()
        
        # 2. AlexNet的崛起 - 规模×GPU
        self.show_alexnet_revolution()
        
        # 3. 深度学习的本质
        self.show_deep_learning_essence()
        
        self.clear_scene()
    
    def show_2012_imagenet(self):
        """2012年ImageNet竞赛 - 传统算法vs神经网络"""
        # 年份与场景
        year_text = Text("2012年 秋天", font_size=48, color=ACCENT_COLOR)
        year_text.to_edge(UP, buff=0.8)
        
        self.play(Write(year_text), run_time=0.8)
        
        venue = Text(
            "计算机视觉顶级竞赛 ImageNet",
            font_size=28, color=TEXT_COLOR
        )
        venue.next_to(year_text, DOWN, buff=0.4)
        
        self.play(Write(venue), run_time=0.6)
        
        # 传统算法 - 复杂数学公式符号群
        traditional_group = VGroup()
        
        # 传统CV算法的代表性公式
        formulas = [
            r"SIFT",
            r"HOG",
            r"\nabla I",
            r"\frac{\partial^2 f}{\partial x^2}",
            r"\int_\Omega \|\nabla u\|",
            r"H(x) = \sum p_i \log p_i",
        ]
        
        for i, formula in enumerate(formulas):
            if i < 2:
                tex = Text(formula, font_size=22, color=SUBTEXT_COLOR)
            else:
                tex = MathTex(formula, font_size=24, color=SUBTEXT_COLOR)
            traditional_group.add(tex)
        
        traditional_group.arrange_in_grid(rows=2, cols=3, buff=0.4)
        traditional_group.move_to(LEFT * 3 + DOWN * 0.5)
        
        trad_label = Text("传统算法", font_size=24, color=SUBTEXT_COLOR)
        trad_label.next_to(traditional_group, UP, buff=0.3)
        
        # 传统算法边框 - 代表"精雕细琢"
        trad_box = SurroundingRectangle(
            traditional_group, color=SUBTEXT_COLOR, buff=0.4,
            stroke_width=2, corner_radius=0.15
        )
        
        self.play(
            FadeIn(traditional_group, lag_ratio=0.1),
            Write(trad_label),
            Create(trad_box),
            run_time=1.2
        )
        
        self.wait(0.5)
        
        # VS
        vs_text = Text("VS", font_size=40, color=TEXT_COLOR, weight=BOLD)
        vs_text.move_to(DOWN * 0.5)
        
        self.play(Write(vs_text), run_time=0.4)
        
        # AlexNet - 一个"朴实无华"的神经网络方块
        nn_block = self.create_simple_nn_block()
        nn_block.move_to(RIGHT * 3 + DOWN * 0.5)
        
        nn_label = Text("神经网络", font_size=24, color=NEURAL_COLOR)
        nn_label.next_to(nn_block, UP, buff=0.3)
        
        self.play(
            FadeIn(nn_block, scale=0.8),
            Write(nn_label),
            run_time=0.8
        )
        
        # 问号 - 悬念
        question = Text("?", font_size=64, color=ACCENT_COLOR)
        question.next_to(nn_block, DOWN, buff=0.3)
        
        self.play(Write(question), run_time=0.4)
        self.wait(1)
        
        self.clear_scene()
    
    def show_alexnet_revolution(self):
        """AlexNet的革命 - 规模 × GPU"""
        # 标题
        title = Text("AlexNet 横空出世", font_size=44, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 秘密揭示
        secret_text = Text(
            "秘密是什么？",
            font_size=28, color=TEXT_COLOR
        )
        secret_text.next_to(title, DOWN, buff=0.5)
        self.play(Write(secret_text), run_time=0.5)
        
        self.wait(0.5)
        
        # 两个关键因素
        self.play(FadeOut(secret_text))
        
        # 因素1: 规模 - 神经网络自我复制变大
        factor_group = VGroup()
        
        # 初始小方块
        initial_block = RoundedRectangle(
            width=0.8, height=0.6,
            corner_radius=0.08,
            color=NEURAL_COLOR,
            fill_opacity=0.5
        )
        initial_block.set_stroke(NEURAL_COLOR, width=2)
        initial_block.move_to(LEFT * 4)
        
        self.play(FadeIn(initial_block, scale=0.5), run_time=0.5)
        
        # 复制并膨胀动画
        blocks = VGroup(initial_block)
        
        for i in range(5):
            new_block = initial_block.copy()
            new_block.set_fill(NEURAL_COLOR, opacity=0.3 + i * 0.1)
            blocks.add(new_block)
        
        # 方块堆叠变大
        self.play(
            blocks.animate.arrange(RIGHT, buff=0.03).scale(2).move_to(LEFT * 2),
            run_time=1.2
        )
        
        # 100倍标注
        scale_text = Text(
            "比之前的模型大 100 倍!",
            font_size=26, color=ACCENT_COLOR
        )
        scale_text.next_to(blocks, DOWN, buff=0.4)
        
        self.play(Write(scale_text), run_time=0.6)
        
        # 因素2: GPU - 芯片飞入
        gpus = VGroup()
        for i in range(6):
            gpu = self.create_gpu_chip()
            gpu.scale(0.5)
            # 从屏幕外不同位置飞入
            angle = i * TAU / 6 + PI / 6
            gpu.move_to(5 * np.array([np.cos(angle), np.sin(angle), 0]))
            gpus.add(gpu)
        
        # GPU飞向神经网络
        target_pos = blocks.get_center() + RIGHT * 0.5
        
        self.play(
            gpus.animate.arrange_in_grid(rows=2, cols=3, buff=0.1).scale(0.8).move_to(RIGHT * 3),
            run_time=1
        )
        
        gpu_label = Text(
            "图形处理器 (GPU)",
            font_size=24, color=SECONDARY_COLOR
        )
        gpu_label.next_to(gpus, DOWN, buff=0.3)
        
        self.play(Write(gpu_label), run_time=0.5)
        
        # GPU发光效果 - 代表高速运转
        self.play(
            gpus.animate.set_fill(SECONDARY_COLOR, opacity=0.8),
            Flash(gpus.get_center(), color=SECONDARY_COLOR, line_length=0.4, num_lines=12),
            run_time=0.8
        )
        
        # 核心洞察
        insight_box = VGroup()
        insight_text = Text(
            "「核心架构早在1989年就被提出了」",
            font_size=22, color=TEXT_COLOR
        )
        insight_text2 = Text(
            "「秘密是: 规模 × 并行计算」",
            font_size=24, color=ACCENT_COLOR
        )
        insight_box.add(insight_text, insight_text2)
        insight_box.arrange(DOWN, buff=0.2)
        insight_box.to_edge(DOWN, buff=0.6)
        
        box_rect = SurroundingRectangle(
            insight_box, color=ACCENT_COLOR, buff=0.25,
            corner_radius=0.1, stroke_width=2
        )
        
        self.play(
            Write(insight_text),
            Write(insight_text2),
            Create(box_rect),
            run_time=1.2
        )
        
        # 竞赛结果
        self.wait(1)
        
        self.clear_scene()
        
        # 结果展示
        result_title = Text("竞赛结果", font_size=36, color=ACCENT_COLOR)
        result_title.to_edge(UP, buff=0.6)
        
        self.play(Write(result_title), run_time=0.5)
        
        # 错误率对比
        results = VGroup()
        
        alexnet_result = VGroup(
            Text("AlexNet", font_size=28, color=NEURAL_COLOR),
            Text("15.3%", font_size=48, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2)
        
        second_result = VGroup(
            Text("第二名", font_size=28, color=SUBTEXT_COLOR),
            Text("26.2%", font_size=48, color=ERROR_COLOR),
        ).arrange(DOWN, buff=0.2)
        
        results.add(alexnet_result, second_result)
        results.arrange(RIGHT, buff=2)
        results.next_to(result_title, DOWN, buff=0.8)
        
        self.play(FadeIn(alexnet_result, scale=1.1), run_time=0.6)
        self.play(FadeIn(second_result, scale=0.9), run_time=0.6)
        
        # 碾压箭头
        crush_arrow = Arrow(
            alexnet_result.get_bottom() + DOWN * 0.5,
            second_result.get_bottom() + DOWN * 0.5,
            color=SECONDARY_COLOR,
            stroke_width=4
        )
        crush_text = Text("碾压!", font_size=24, color=SECONDARY_COLOR)
        crush_text.next_to(crush_arrow, DOWN, buff=0.1)
        
        self.play(GrowArrow(crush_arrow), Write(crush_text), run_time=0.6)
        
        # 画外音
        voiceover = Text(
            "「力量的根源，来自规模与并行」",
            font_size=26, color=TEXT_COLOR
        )
        voiceover.to_edge(DOWN, buff=0.8)
        
        vo_box = SurroundingRectangle(
            voiceover, color=ACCENT_COLOR, buff=0.2,
            corner_radius=0.1
        )
        
        self.play(Write(voiceover), Create(vo_box), run_time=1)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_deep_learning_essence(self):
        """深度学习的本质"""
        # 主标题
        title = Text(
            "《深度学习简明指南》",
            font_size=48, color=TEXT_COLOR
        )
        title.set_color_by_gradient(PRIMARY_COLOR, NEURAL_COLOR)
        
        subtitle = Text(
            "一次从神经元到创造力的思维漫游",
            font_size=26, color=SUBTEXT_COLOR
        )
        subtitle.next_to(title, DOWN, buff=0.4)
        
        # 引用
        reference = Text(
            "基于 François Fleuret《The Little Book of Deep Learning》",
            font_size=16, color=SUBTEXT_COLOR
        )
        reference.next_to(subtitle, DOWN, buff=0.3)
        
        self.play(Write(title), run_time=1.5)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(reference), run_time=0.5)
        
        self.wait(1.5)
        
        # 淡出标题
        self.play(FadeOut(title), FadeOut(subtitle), FadeOut(reference))
        
        # 三要素
        essence_title = Text(
            "深度学习的三大要素",
            font_size=38, color=ACCENT_COLOR
        )
        essence_title.to_edge(UP, buff=0.5)
        
        self.play(Write(essence_title), run_time=0.6)
        
        # 三个圆形要素
        elements = VGroup()
        
        elem_data = [
            ("算力", "GPU/TPU", PRIMARY_COLOR, "⚡"),
            ("数据", "海量样本", SECONDARY_COLOR, "📊"),
            ("模型", "深度网络", NEURAL_COLOR, "🧠"),
        ]
        
        for name, desc, color, emoji in elem_data:
            elem = VGroup()
            
            # 圆形背景
            circle = Circle(radius=1.1, color=color, fill_opacity=0.25)
            circle.set_stroke(color, width=3)
            
            # emoji图标
            icon = Text(emoji, font_size=40)
            icon.move_to(circle.get_center() + UP * 0.25)
            
            # 中文名
            name_text = Text(name, font_size=28, color=color, weight=BOLD)
            name_text.next_to(icon, DOWN, buff=0.1)
            
            # 描述
            desc_text = Text(desc, font_size=16, color=TEXT_COLOR)
            desc_text.next_to(name_text, DOWN, buff=0.1)
            
            elem.add(circle, icon, name_text, desc_text)
            elements.add(elem)
        
        elements.arrange(RIGHT, buff=1)
        elements.next_to(essence_title, DOWN, buff=0.7)
        
        # 依次显示
        for elem in elements:
            self.play(FadeIn(elem, scale=0.8), run_time=0.6)
        
        # 加号和等号
        plus1 = Text("+", font_size=48, color=TEXT_COLOR)
        plus1.move_to((elements[0].get_center() + elements[1].get_center()) / 2)
        
        plus2 = Text("+", font_size=48, color=TEXT_COLOR)
        plus2.move_to((elements[1].get_center() + elements[2].get_center()) / 2)
        
        self.play(Write(plus1), Write(plus2), run_time=0.4)
        
        # 结果
        equals = Text("=", font_size=48, color=TEXT_COLOR)
        equals.next_to(elements, DOWN, buff=0.5)
        
        result = Text(
            "从海量数据中学习复杂的模式和表示",
            font_size=26, color=ACCENT_COLOR
        )
        result.next_to(equals, DOWN, buff=0.3)
        
        self.play(Write(equals), Write(result), run_time=0.8)
        
        # 融合说明
        fusion = Text(
            "融合线性代数、微积分、概率论与计算机科学",
            font_size=20, color=SUBTEXT_COLOR
        )
        fusion.to_edge(DOWN, buff=0.8)
        
        encourage = Text(
            "别担心，我们将一步步拆解！",
            font_size=24, color=SECONDARY_COLOR
        )
        encourage.next_to(fusion, UP, buff=0.2)
        
        self.play(Write(fusion), Write(encourage), run_time=1)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_simple_nn_block(self):
        """创建简单的神经网络方块"""
        block = VGroup()
        
        # 主方块
        main = RoundedRectangle(
            width=2.2, height=1.8,
            corner_radius=0.15,
            color=NEURAL_COLOR,
            fill_opacity=0.35
        )
        main.set_stroke(NEURAL_COLOR, width=2)
        
        # 内部简化的层结构 - 三列节点
        layers = VGroup()
        for col in range(3):
            layer = VGroup()
            num_nodes = [3, 4, 2][col]
            for row in range(num_nodes):
                node = Circle(
                    radius=0.1,
                    color=NEURAL_COLOR,
                    fill_opacity=0.7
                )
                y_offset = (row - (num_nodes - 1) / 2) * 0.3
                node.move_to([(col - 1) * 0.6, y_offset, 0])
                layer.add(node)
            layers.add(layer)
        
        layers.move_to(main.get_center())
        
        # 简化的连接线
        connections = VGroup()
        for i, node1 in enumerate(layers[0]):
            for node2 in layers[1]:
                line = Line(
                    node1.get_right(), node2.get_left(),
                    stroke_width=0.5, color=NEURAL_COLOR, stroke_opacity=0.3
                )
                connections.add(line)
        
        for node1 in layers[1]:
            for node2 in layers[2]:
                line = Line(
                    node1.get_right(), node2.get_left(),
                    stroke_width=0.5, color=NEURAL_COLOR, stroke_opacity=0.3
                )
                connections.add(line)
        
        block.add(main, connections, layers)
        return block
    
    def create_gpu_chip(self):
        """创建GPU芯片图标"""
        chip = VGroup()
        
        # 芯片主体
        body = Square(side_length=0.8, color=SECONDARY_COLOR, fill_opacity=0.5)
        body.set_stroke(SECONDARY_COLOR, width=2)
        
        # 核心网格 - 代表并行计算单元
        cores = VGroup()
        for i in range(4):
            for j in range(4):
                core = Square(side_length=0.12, color=SECONDARY_COLOR, fill_opacity=0.7)
                core.move_to(body.get_center() + np.array([
                    (i - 1.5) * 0.15, (j - 1.5) * 0.15, 0
                ]))
                cores.add(core)
        
        # 引脚
        pins = VGroup()
        for side in [UP, DOWN, LEFT, RIGHT]:
            for offset in [-0.25, -0.08, 0.08, 0.25]:
                pin_offset = offset * np.array([abs(side[1]), abs(side[0]), 0])
                pin = Line(
                    body.get_edge_center(side) + pin_offset,
                    body.get_edge_center(side) + pin_offset + side * 0.12,
                    color=SECONDARY_COLOR, stroke_width=1.5
                )
                pins.add(pin)
        
        chip.add(body, cores, pins)
        return chip
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = IntroScene()
    scene.render()
