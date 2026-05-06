"""
场景12: 尾声 - 演进与未来
基于scenes.md - 总结回顾，展望未来

运行命令:
    manim -pql scene_12_future.py FutureScene
    manim -pqh scene_12_future.py FutureScene
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


class FutureScene(Scene):
    """场景12: 尾声 - 演进与未来"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 演进之路
        self.show_evolution()
        
        # 2. 分支扩展
        self.show_branches()
        
        # 3. 未完的征程
        self.show_unexplored()
        
        # 4. 总结
        self.show_summary()
        
        # 5. 结尾
        self.show_ending()
        
        self.clear_scene()
    
    def show_evolution(self):
        """演进之路"""
        # 标题
        title = Text("演进之路", font_size=44, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 时间线
        timeline = NumberLine(
            x_range=[1950, 2025, 10],
            length=10,
            color=SUBTEXT_COLOR,
            include_numbers=True,
            numbers_with_elongated_ticks=[1950, 1980, 2012, 2020],
            font_size=16,
        )
        timeline.next_to(title, DOWN, buff=0.8)
        
        self.play(Create(timeline), run_time=0.8)
        
        # 里程碑事件
        milestones = [
            (1958, "感知机\n(单层)", PRIMARY_COLOR, 0.3),
            (1986, "反向传播\n(多层)", SECONDARY_COLOR, 0.4),
            (2012, "AlexNet\n(深度+GPU)", ACCENT_COLOR, 0.6),
            (2017, "Transformer\n(注意力)", NEURAL_COLOR, 0.8),
            (2022, "GPT时代\n(大模型)", ERROR_COLOR, 1.0),
        ]
        
        milestone_groups = VGroup()
        
        for year, label, color, scale in milestones:
            # 标记点
            point = timeline.n2p(year)
            dot = Dot(point, radius=0.12 * scale + 0.08, color=color)
            
            # 标签
            label_text = Text(label, font_size=12, color=color, line_spacing=1.1)
            label_text.next_to(dot, UP, buff=0.2)
            
            milestone_group = VGroup(dot, label_text)
            milestone_groups.add(milestone_group)
        
        # 依次显示里程碑
        for i, group in enumerate(milestone_groups):
            self.play(
                FadeIn(group[0], scale=1.5),
                Write(group[1]),
                run_time=0.4
            )
            
            # 连接线（表示发展）
            if i > 0:
                prev_dot = milestone_groups[i-1][0]
                curr_dot = group[0]
                
                line = Line(
                    prev_dot.get_center() + RIGHT * 0.15,
                    curr_dot.get_center() + LEFT * 0.15,
                    color=TEXT_COLOR, stroke_width=1.5, stroke_opacity=0.5
                )
                self.play(Create(line), run_time=0.15)
        
        # 网络演化动画
        evolution_visual = VGroup()
        
        # 1950s: 简单神经元
        simple_neuron = Circle(radius=0.2, color=PRIMARY_COLOR, fill_opacity=0.5)
        simple_neuron.set_stroke(PRIMARY_COLOR, width=2)
        
        # 1980s: 小多层网络
        small_mlp = self.create_mini_network([2, 3, 2], SECONDARY_COLOR, 0.4)
        
        # 2020s: 巨型网络
        giant_network = self.create_mini_network([3, 5, 5, 5, 3], NEURAL_COLOR, 0.5)
        
        evolution_visual.add(simple_neuron, small_mlp, giant_network)
        evolution_visual.arrange(RIGHT, buff=1.5)
        evolution_visual.to_edge(DOWN, buff=1)
        
        # 演化过程
        self.play(FadeIn(simple_neuron), run_time=0.3)
        
        arrow1 = Arrow(
            simple_neuron.get_right(),
            small_mlp.get_left(),
            color=TEXT_COLOR, stroke_width=2, buff=0.2
        )
        self.play(GrowArrow(arrow1), FadeIn(small_mlp), run_time=0.4)
        
        arrow2 = Arrow(
            small_mlp.get_right(),
            giant_network.get_left(),
            color=TEXT_COLOR, stroke_width=2, buff=0.2
        )
        self.play(GrowArrow(arrow2), FadeIn(giant_network), run_time=0.4)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_branches(self):
        """分支扩展"""
        # 标题
        title = Text("分支扩展", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 中心节点
        center = VGroup()
        center_circle = Circle(radius=0.6, color=NEURAL_COLOR, fill_opacity=0.3)
        center_circle.set_stroke(NEURAL_COLOR, width=3)
        center_text = Text("深度学习", font_size=18, color=NEURAL_COLOR)
        center_text.move_to(center_circle.get_center())
        center.add(center_circle, center_text)
        
        self.play(FadeIn(center), run_time=0.5)
        
        # 分支
        branches = [
            ("感知\n(看懂世界的'眼')", PRIMARY_COLOR, UP * 1.8 + LEFT * 2),
            ("生成\n(创作诗画的'手')", SECONDARY_COLOR, UP * 1.8 + RIGHT * 2),
            ("多模态\n(连接万物的'触角')", ACCENT_COLOR, DOWN * 1.5 + LEFT * 2.5),
            ("具身智能\n(行动的'身体')", ERROR_COLOR, DOWN * 1.5 + RIGHT * 2.5),
        ]
        
        branch_groups = VGroup()
        
        for label, color, pos in branches:
            # 分支节点
            branch = VGroup()
            branch_circle = Circle(radius=0.5, color=color, fill_opacity=0.2)
            branch_circle.set_stroke(color, width=2)
            branch_circle.move_to(pos)
            
            branch_text = Text(label, font_size=14, color=color, line_spacing=1.1)
            branch_text.move_to(branch_circle.get_center())
            
            # 连接线
            line = Line(
                center_circle.get_center(),
                branch_circle.get_center(),
                color=color, stroke_width=2, stroke_opacity=0.6
            )
            
            branch.add(line, branch_circle, branch_text)
            branch_groups.add(branch)
        
        # 依次展开分支
        for branch in branch_groups:
            self.play(
                Create(branch[0]),
                FadeIn(branch[1]),
                Write(branch[2]),
                run_time=0.5
            )
        
        # 说明
        desc = Text(
            "从单一任务到多领域融合",
            font_size=20, color=TEXT_COLOR
        )
        desc.to_edge(DOWN, buff=0.5)
        
        self.play(Write(desc), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_unexplored(self):
        """未完的征程"""
        # 标题
        title = Text("未完的征程", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.6)
        
        # 副标题
        subtitle = Text("还有很多未涉及的领域...", font_size=24, color=TEXT_COLOR)
        subtitle.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(subtitle), run_time=0.4)
        
        # 未涉及的领域
        unexplored = VGroup()
        topics = [
            "RNN\n循环神经网络",
            "GNN\n图神经网络",
            "自监督学习",
            "强化学习进阶",
            "世界模型",
            "神经符号融合",
        ]
        
        colors = [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, NEURAL_COLOR, ERROR_COLOR, SUBTEXT_COLOR]
        
        for topic, color in zip(topics, colors):
            box = VGroup()
            rect = RoundedRectangle(
                width=2.2, height=1.3,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.15
            )
            rect.set_stroke(color, width=2, dash_length=0.1)
            
            text = Text(topic, font_size=12, color=color, line_spacing=1.1)
            text.move_to(rect.get_center())
            
            question = Text("?", font_size=24, color=color)
            question.move_to(rect.get_corner(UR) + LEFT * 0.2 + DOWN * 0.2)
            
            box.add(rect, text, question)
            unexplored.add(box)
        
        unexplored.arrange_in_grid(rows=2, cols=3, buff=0.4)
        unexplored.next_to(subtitle, DOWN, buff=0.5)
        
        self.play(FadeIn(unexplored, lag_ratio=0.1), run_time=1)
        
        # 说明
        note = Text(
            "领域仍在飞速扩展和深化",
            font_size=20, color=SECONDARY_COLOR
        )
        note.to_edge(DOWN, buff=0.5)
        
        self.play(Write(note), run_time=0.5)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_summary(self):
        """总结"""
        # 标题
        title = Text("深度学习的成功密码", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.6)
        
        # 三要素
        formula = VGroup()
        
        elements = [
            ("算力", PRIMARY_COLOR, "GPU/TPU\n并行计算"),
            ("数据", SECONDARY_COLOR, "海量训练\n数据集"),
            ("模型规模", NEURAL_COLOR, "千亿参数\n深层网络"),
        ]
        
        for i, (name, color, desc) in enumerate(elements):
            elem = VGroup()
            
            circle = Circle(radius=0.8, color=color, fill_opacity=0.2)
            circle.set_stroke(color, width=3)
            
            name_text = Text(name, font_size=20, color=color)
            name_text.move_to(circle.get_center() + UP * 0.15)
            
            desc_text = Text(desc, font_size=12, color=TEXT_COLOR, line_spacing=1.1)
            desc_text.next_to(name_text, DOWN, buff=0.1)
            
            elem.add(circle, name_text, desc_text)
            formula.add(elem)
        
        # 加号和等号
        plus1 = Text("+", font_size=36, color=TEXT_COLOR)
        plus2 = Text("+", font_size=36, color=TEXT_COLOR)
        equals = Text("=", font_size=36, color=TEXT_COLOR)
        
        result = VGroup()
        result_circle = Circle(radius=0.8, color=ACCENT_COLOR, fill_opacity=0.3)
        result_circle.set_stroke(ACCENT_COLOR, width=3)
        result_text = Text("成功", font_size=24, color=ACCENT_COLOR)
        result_text.move_to(result_circle.get_center())
        result.add(result_circle, result_text)
        
        # 排列
        full_formula = VGroup(formula[0], plus1, formula[1], plus2, formula[2], equals, result)
        full_formula.arrange(RIGHT, buff=0.3)
        full_formula.next_to(title, DOWN, buff=0.6)
        
        self.play(FadeIn(formula[0]), run_time=0.4)
        self.play(Write(plus1), FadeIn(formula[1]), run_time=0.4)
        self.play(Write(plus2), FadeIn(formula[2]), run_time=0.4)
        self.play(Write(equals), FadeIn(result, scale=1.2), run_time=0.5)
        
        # 核心洞察
        insight = VGroup(
            Text("不仅是冰冷的数学和代码", font_size=20, color=SUBTEXT_COLOR),
            Text("更是构建、训练和激发'硅基大脑'的", font_size=20, color=TEXT_COLOR),
            Text("手艺与艺术", font_size=28, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.15)
        insight.to_edge(DOWN, buff=0.6)
        
        self.play(Write(insight), run_time=1)
        
        self.wait(2)
        self.clear_scene()
    
    def show_ending(self):
        """结尾 - 星海中的智能体"""
        # 创建星空背景
        stars = VGroup()
        np.random.seed(42)
        
        for _ in range(100):
            star = Dot(
                point=[
                    np.random.uniform(-7, 7),
                    np.random.uniform(-4, 4),
                    0
                ],
                radius=np.random.uniform(0.01, 0.04),
                color=WHITE
            )
            star.set_opacity(np.random.uniform(0.3, 1.0))
            stars.add(star)
        
        self.play(FadeIn(stars, lag_ratio=0.01), run_time=1)
        
        # 中心的智能体（神经网络结构）
        agent = self.create_neural_agent()
        agent.scale(0.8)
        
        self.play(FadeIn(agent, scale=0.8), run_time=0.8)
        
        # 发光效果
        glow = Circle(radius=2, color=ACCENT_COLOR, fill_opacity=0.1)
        glow.set_stroke(ACCENT_COLOR, width=2, opacity=0.5)
        
        self.play(
            Create(glow),
            agent.animate.scale(1.1),
            run_time=0.6
        )
        
        # 连接到各方向的光线（知识与工具宇宙）
        connections = VGroup()
        directions = [
            UP * 3 + LEFT * 2,
            UP * 3 + RIGHT * 2,
            RIGHT * 4,
            DOWN * 3 + RIGHT * 2,
            DOWN * 3 + LEFT * 2,
            LEFT * 4,
        ]
        
        colors = [PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR, NEURAL_COLOR, ERROR_COLOR, SUBTEXT_COLOR]
        
        for direction, color in zip(directions, colors):
            line = Line(
                ORIGIN,
                direction * 0.8,
                color=color,
                stroke_width=2,
                stroke_opacity=0.6
            )
            
            end_dot = Dot(direction * 0.8, radius=0.1, color=color)
            
            connections.add(VGroup(line, end_dot))
        
        self.play(FadeIn(connections, lag_ratio=0.1), run_time=0.8)
        
        # 结尾文字
        ending_text = VGroup(
            Text("这场智能革命", font_size=28, color=TEXT_COLOR),
            Text("才刚刚拉开序幕", font_size=32, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        ending_text.to_edge(DOWN, buff=0.8)
        
        self.play(Write(ending_text), run_time=1)
        
        # 最终高亮
        self.play(
            glow.animate.scale(1.2).set_opacity(0.3),
            Flash(agent.get_center(), color=ACCENT_COLOR, line_length=0.5, num_lines=16),
            run_time=0.8
        )
        
        self.wait(3)
    
    # ============ 辅助方法 ============
    
    def create_mini_network(self, layer_sizes, color, scale):
        """创建迷你网络图"""
        network = VGroup()
        
        all_neurons = []
        
        for i, size in enumerate(layer_sizes):
            layer = VGroup()
            neurons = []
            
            for j in range(size):
                neuron = Circle(
                    radius=0.08 * scale,
                    color=color,
                    fill_opacity=0.5
                )
                neuron.set_stroke(color, width=1)
                y_pos = (size - 1) / 2 * 0.3 * scale - j * 0.3 * scale
                neuron.move_to([i * 0.5 * scale, y_pos, 0])
                layer.add(neuron)
                neurons.append(neuron)
            
            network.add(layer)
            all_neurons.append(neurons)
        
        # 连接线
        for i in range(len(layer_sizes) - 1):
            for n1 in all_neurons[i]:
                for n2 in all_neurons[i + 1]:
                    line = Line(
                        n1.get_center(), n2.get_center(),
                        stroke_width=0.5 * scale,
                        stroke_opacity=0.3,
                        color=color
                    )
                    network.add(line)
        
        network.move_to(ORIGIN)
        return network
    
    def create_neural_agent(self):
        """创建神经网络智能体"""
        agent = VGroup()
        
        # 核心大脑结构
        brain = VGroup()
        
        # 中心球
        center = Circle(radius=0.5, color=NEURAL_COLOR, fill_opacity=0.4)
        center.set_stroke(NEURAL_COLOR, width=3)
        
        # 围绕的神经元
        for i in range(8):
            angle = i * TAU / 8
            neuron = Circle(
                radius=0.15,
                color=interpolate_color(ManimColor(PRIMARY_COLOR), ManimColor(SECONDARY_COLOR), i / 8),
                fill_opacity=0.5
            )
            neuron.set_stroke(color=interpolate_color(ManimColor(PRIMARY_COLOR), ManimColor(SECONDARY_COLOR), i / 8), width=2)
            neuron.move_to(center.get_center() + np.array([
                np.cos(angle) * 1.0,
                np.sin(angle) * 1.0,
                0
            ]))
            
            # 连接到中心
            conn = Line(
                center.get_center(),
                neuron.get_center(),
                color=SUBTEXT_COLOR,
                stroke_width=1,
                stroke_opacity=0.5
            )
            
            brain.add(conn, neuron)
        
        brain.add(center)
        
        # 外层光环
        outer_ring = Circle(radius=1.5, color=ACCENT_COLOR)
        outer_ring.set_stroke(ACCENT_COLOR, width=1, opacity=0.3)
        
        agent.add(outer_ring, brain)
        return agent
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = FutureScene()
    scene.render()
