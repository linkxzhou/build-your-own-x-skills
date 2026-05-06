"""
场景10: 挑战与未来
展示深度学习的挑战、优化技术和总结

运行命令:
    manim -pql scene_10_future.py FutureScene
    manim -pqh scene_10_future.py FutureScene
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
    """场景10: 挑战与未来"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 挑战
        self.show_challenges()
        
        # 2. 优化技术
        self.show_optimization_techniques()
        
        # 3. 总结回顾
        self.show_summary()
        
        # 4. 结语
        self.show_ending()
        
        self.clear_scene()
    
    def show_challenges(self):
        """展示挑战"""
        # 标题
        title = Text("第七部分：挑战与未来", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 挑战描述
        challenge = Text(
            "大模型的代价",
            font_size=32, color=ERROR_COLOR
        )
        challenge.next_to(title, DOWN, buff=0.5)
        
        self.play(Write(challenge), run_time=0.5)
        
        # 参数量增长
        growth_chart = self.create_growth_chart()
        growth_chart.scale(0.8)
        growth_chart.next_to(challenge, DOWN, buff=0.5)
        
        self.play(FadeIn(growth_chart), run_time=0.8)
        
        # 代价说明
        costs = VGroup(
            VGroup(
                Text("💰", font_size=24),
                Text("训练成本: 数百万美元", font_size=20, color=TEXT_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("⚡", font_size=24),
                Text("电力消耗: 相当于小型城市", font_size=20, color=TEXT_COLOR),
            ).arrange(RIGHT, buff=0.2),
            VGroup(
                Text("🖥️", font_size=24),
                Text("硬件需求: 数千块GPU", font_size=20, color=TEXT_COLOR),
            ).arrange(RIGHT, buff=0.2),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        costs.next_to(growth_chart, DOWN, buff=0.4)
        
        for cost in costs:
            self.play(FadeIn(cost, shift=RIGHT * 0.3), run_time=0.4)
        
        # 问题
        question = Text(
            "如何让普通人也能用上大模型？",
            font_size=24, color=ACCENT_COLOR
        )
        question.to_edge(DOWN, buff=0.6)
        
        self.play(Write(question), run_time=0.6)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_optimization_techniques(self):
        """展示优化技术"""
        # 标题
        title = Text("让大模型触手可及", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 四种技术
        techniques = VGroup()
        
        # 1. 提示工程
        prompt_eng = self.create_technique_card(
            "提示工程",
            "Prompt Engineering",
            "精心设计问题引导回答",
            "不修改模型，只改输入",
            PRIMARY_COLOR
        )
        
        # 2. 量化
        quantization = self.create_technique_card(
            "量化",
            "Quantization",
            "降低参数精度 32位→8位",
            "专业天平 → 小台秤",
            SECONDARY_COLOR
        )
        
        # 3. 适配器
        adapter = self.create_technique_card(
            "适配器",
            "Adapters / LoRA",
            "只训练一小部分新参数",
            "极大降低微调成本",
            NEURAL_COLOR
        )
        
        # 4. 模型合并
        merge = self.create_technique_card(
            "模型合并",
            "Model Merging",
            "融合多个专家模型知识",
            "有趣的研究方向",
            ACCENT_COLOR
        )
        
        techniques.add(prompt_eng, quantization, adapter, merge)
        techniques.arrange_in_grid(rows=2, cols=2, buff=0.5)
        techniques.next_to(title, DOWN, buff=0.4)
        
        for tech in techniques:
            self.play(FadeIn(tech, scale=0.9), run_time=0.5)
        
        self.wait(1)
        
        # 思维链提示
        cot_text = VGroup(
            Text("思维链 (Chain of Thought):", font_size=20, color=ACCENT_COLOR),
            Text("让模型'一步一步地思考'", font_size=18, color=TEXT_COLOR),
            Text("→ 显著提高复杂推理准确性", font_size=18, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.1)
        cot_text.to_edge(DOWN, buff=0.5)
        
        self.play(Write(cot_text), run_time=0.8)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_summary(self):
        """总结回顾"""
        # 标题
        title = Text("深度学习 = ?", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 公式化总结
        formula = VGroup(
            Text("数据", font_size=28, color=PRIMARY_COLOR),
            Text("+", font_size=28, color=TEXT_COLOR),
            Text("算力 (GPU)", font_size=28, color=SECONDARY_COLOR),
            Text("+", font_size=28, color=TEXT_COLOR),
            Text("算法", font_size=28, color=NEURAL_COLOR),
        ).arrange(RIGHT, buff=0.3)
        formula.next_to(title, DOWN, buff=0.6)
        
        self.play(Write(formula), run_time=1)
        
        # 箭头
        arrow = Arrow(
            formula.get_bottom() + DOWN * 0.2,
            formula.get_bottom() + DOWN * 1,
            color=TEXT_COLOR,
            stroke_width=3
        )
        
        self.play(GrowArrow(arrow), run_time=0.5)
        
        # 结果
        result = Text(
            "优化深度模型，学会预测或创造",
            font_size=28, color=ACCENT_COLOR
        )
        result.next_to(arrow, DOWN, buff=0.2)
        
        self.play(Write(result), run_time=0.8)
        
        # 核心流程回顾
        review = VGroup(
            Text("核心流程回顾:", font_size=24, color=TEXT_COLOR),
            Text("1. 收集数据 (训练集)", font_size=20, color=PRIMARY_COLOR),
            Text("2. 设计模型 (网络架构)", font_size=20, color=NEURAL_COLOR),
            Text("3. 定义损失 (衡量好坏)", font_size=20, color=ERROR_COLOR),
            Text("4. 反向传播 (计算梯度)", font_size=20, color=SECONDARY_COLOR),
            Text("5. 梯度下降 (更新参数)", font_size=20, color=ACCENT_COLOR),
            Text("6. 重复直到收敛!", font_size=20, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.15, aligned_edge=LEFT)
        review.next_to(result, DOWN, buff=0.5)
        
        for i, line in enumerate(review):
            self.play(Write(line), run_time=0.3 if i > 0 else 0.4)
        
        self.wait(1.5)
        
        # 清理
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.8)
    
    def show_ending(self):
        """结语"""
        # 未来展望
        future_title = Text("未来的问题", font_size=36, color=ACCENT_COLOR)
        future_title.to_edge(UP, buff=0.8)
        
        self.play(Write(future_title), run_time=0.5)
        
        questions = VGroup(
            Text("• 如何让模型更高效？", font_size=24, color=TEXT_COLOR),
            Text("• 如何让模型更公平？", font_size=24, color=TEXT_COLOR),
            Text("• 如何让模型更可解释？", font_size=24, color=TEXT_COLOR),
            Text("• 如何用更少能源做更多事？", font_size=24, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        questions.next_to(future_title, DOWN, buff=0.5)
        
        for q in questions:
            self.play(FadeIn(q, shift=RIGHT * 0.3), run_time=0.4)
        
        self.wait(1)
        
        # 清理问题
        self.play(FadeOut(future_title), FadeOut(questions), run_time=0.5)
        
        # 邀请
        invitation = VGroup(
            Text("未来的AI科学家和工程师们", font_size=28, color=TEXT_COLOR),
            Text("希望这份'导游手册'", font_size=24, color=SUBTEXT_COLOR),
            Text("能成为你探索AI世界的第一个台阶", font_size=24, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.3)
        invitation.move_to(UP * 0.5)
        
        self.play(Write(invitation), run_time=1.2)
        
        self.wait(0.5)
        
        # 号召
        call_to_action = Text(
            "动手去尝试，去创造吧！",
            font_size=36, color=ACCENT_COLOR
        )
        call_to_action.next_to(invitation, DOWN, buff=0.8)
        
        self.play(
            Write(call_to_action),
            Circumscribe(call_to_action, color=ACCENT_COLOR),
            run_time=1
        )
        
        self.wait(1.5)
        
        # 感谢
        self.play(FadeOut(invitation), FadeOut(call_to_action), run_time=0.5)
        
        thanks = Text("感谢观看！", font_size=56, color=TEXT_COLOR)
        thanks.set_color_by_gradient(PRIMARY_COLOR, NEURAL_COLOR, SECONDARY_COLOR)
        
        self.play(FadeIn(thanks, scale=1.3), run_time=1)
        
        # 粒子效果
        particles = VGroup()
        for _ in range(30):
            particle = Dot(
                point=np.array([
                    np.random.uniform(-6, 6),
                    np.random.uniform(-3, 3),
                    0
                ]),
                radius=0.04,
                color=np.random.choice([PRIMARY_COLOR, SECONDARY_COLOR, ACCENT_COLOR])
            )
            particle.set_opacity(np.random.uniform(0.3, 0.8))
            particles.add(particle)
        
        self.play(FadeIn(particles, lag_ratio=0.02), run_time=0.8)
        
        self.wait(2)
    
    # ============ 辅助方法 ============
    
    def create_growth_chart(self):
        """创建参数增长图表"""
        chart = VGroup()
        
        # 坐标轴
        axes = Axes(
            x_range=[2018, 2024, 1],
            y_range=[0, 200, 50],
            x_length=6,
            y_length=3,
            axis_config={
                "include_tip": False,
                "include_numbers": True,
                "color": SUBTEXT_COLOR,
            },
        )
        
        # Y轴标签
        y_label = Text("参数量 (十亿)", font_size=14, color=SUBTEXT_COLOR)
        y_label.rotate(PI / 2)
        y_label.next_to(axes, LEFT, buff=0.3)
        
        # 数据点
        data = [
            (2018, 0.3),   # BERT
            (2019, 1.5),   # GPT-2
            (2020, 175),   # GPT-3
            (2022, 180),   # GPT-3.5
            (2023, 200),   # 估计
        ]
        
        bars = VGroup()
        for year, params in data:
            bar = Rectangle(
                width=0.5,
                height=params / 200 * 3,
                color=NEURAL_COLOR,
                fill_opacity=0.6
            )
            bar.set_stroke(NEURAL_COLOR, width=2)
            bar.move_to(axes.c2p(year, params / 2))
            bars.add(bar)
        
        # GPT-3 标注
        gpt3_label = Text("GPT-3\n1750亿", font_size=10, color=ACCENT_COLOR)
        gpt3_label.next_to(bars[2], UP, buff=0.1)
        
        chart.add(axes, y_label, bars, gpt3_label)
        return chart
    
    def create_technique_card(self, cn_name, en_name, desc1, desc2, color):
        """创建技术卡片"""
        card = VGroup()
        
        box = RoundedRectangle(
            width=3.8, height=2,
            corner_radius=0.15,
            color=color,
            fill_opacity=0.2
        )
        box.set_stroke(color, width=2)
        
        title_cn = Text(cn_name, font_size=22, color=color)
        title_en = Text(en_name, font_size=14, color=SUBTEXT_COLOR)
        description1 = Text(desc1, font_size=14, color=TEXT_COLOR)
        description2 = Text(desc2, font_size=12, color=SUBTEXT_COLOR)
        
        title_cn.move_to(box.get_center() + UP * 0.6)
        title_en.next_to(title_cn, DOWN, buff=0.1)
        description1.next_to(title_en, DOWN, buff=0.2)
        description2.next_to(description1, DOWN, buff=0.1)
        
        card.add(box, title_cn, title_en, description1, description2)
        return card
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = FutureScene()
    scene.render()
