"""
场景11: 大模型时代的新技能
基于scenes.md - 介绍高效使用大模型的技术

运行命令:
    manim -pql scene_11_large_models.py LargeModelsScene
    manim -pqh scene_11_large_models.py LargeModelsScene
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


class LargeModelsScene(Scene):
    """场景11: 大模型时代的新技能"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 1. 挑战
        self.show_challenge()
        
        # 2. 提示工程
        self.show_prompt_engineering()
        
        # 3. 量化
        self.show_quantization()
        
        # 4. LoRA适配器
        self.show_lora()
        
        # 5. 总结
        self.show_summary()
        
        self.clear_scene()
    
    def show_challenge(self):
        """大模型的挑战"""
        # 标题
        title = Text("大模型时代的新技能", font_size=40, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.8)
        
        # 参数量指数增长曲线
        axes = Axes(
            x_range=[2018, 2024, 1],
            y_range=[0, 1000, 200],
            x_length=8,
            y_length=4,
            axis_config={"color": SUBTEXT_COLOR, "include_numbers": False},
            x_axis_config={"numbers_to_include": [2018, 2020, 2022, 2024]},
        )
        axes.next_to(title, DOWN, buff=0.5)
        
        x_label = Text("年份", font_size=14, color=SUBTEXT_COLOR)
        x_label.next_to(axes.x_axis, DOWN, buff=0.1)
        
        y_label = Text("参数量(B)", font_size=14, color=SUBTEXT_COLOR)
        y_label.next_to(axes.y_axis, LEFT, buff=0.1)
        
        self.play(Create(axes), Write(x_label), Write(y_label), run_time=0.6)
        
        # 指数增长曲线
        def param_growth(x):
            return 0.5 * np.exp((x - 2018) * 0.9)
        
        curve = axes.plot(
            param_growth,
            x_range=[2018, 2023.5],
            color=ERROR_COLOR
        )
        
        self.play(Create(curve), run_time=1)
        
        # 标注点
        points_data = [
            (2018, "BERT\n0.3B", 0.3),
            (2020, "GPT-3\n175B", 175),
            (2022, "PaLM\n540B", 540),
            (2023, "GPT-4\n?", 800),
        ]
        
        for year, label, _ in points_data:
            y_val = param_growth(year)
            point = Dot(axes.c2p(year, min(y_val, 950)), radius=0.08, color=ACCENT_COLOR)
            
            label_text = Text(label, font_size=10, color=TEXT_COLOR)
            label_text.next_to(point, UP, buff=0.1)
            
            self.play(FadeIn(point), Write(label_text), run_time=0.3)
        
        # 挑战
        challenges = VGroup(
            Text("挑战:", font_size=22, color=ERROR_COLOR),
            Text("• 千亿参数，天价算力", font_size=18, color=TEXT_COLOR),
            Text("• 需要专业级GPU集群", font_size=18, color=TEXT_COLOR),
            Text("• 如何高效使用它们?", font_size=18, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT)
        challenges.to_edge(DOWN, buff=0.5)
        
        self.play(Write(challenges), run_time=0.8)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_prompt_engineering(self):
        """提示工程"""
        # 标题
        title = Text("1. 提示工程", font_size=36, color=PRIMARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 核心思想
        idea = Text("精心设计输入，'唤醒'大模型特定能力", font_size=24, color=TEXT_COLOR)
        idea.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(idea), run_time=0.5)
        
        # 示例对比
        examples = VGroup()
        
        # 普通提示
        bad_prompt = VGroup()
        bad_box = RoundedRectangle(
            width=5, height=1.5,
            corner_radius=0.1,
            color=ERROR_COLOR,
            fill_opacity=0.1
        )
        bad_box.set_stroke(ERROR_COLOR, width=2)
        
        bad_title = Text("普通提示", font_size=16, color=ERROR_COLOR)
        bad_title.next_to(bad_box, UP, buff=0.1)
        
        bad_text = Text('"25+37等于多少?"', font_size=16, color=SUBTEXT_COLOR)
        bad_text.move_to(bad_box.get_center())
        
        bad_prompt.add(bad_box, bad_title, bad_text)
        
        # 优化提示（思维链）
        good_prompt = VGroup()
        good_box = RoundedRectangle(
            width=5, height=2,
            corner_radius=0.1,
            color=SECONDARY_COLOR,
            fill_opacity=0.1
        )
        good_box.set_stroke(SECONDARY_COLOR, width=2)
        
        good_title = Text("思维链提示", font_size=16, color=SECONDARY_COLOR)
        good_title.next_to(good_box, UP, buff=0.1)
        
        good_text = VGroup(
            Text('"让我们一步一步思考:', font_size=14, color=ACCENT_COLOR),
            Text('25+37 = ?', font_size=14, color=TEXT_COLOR),
            Text('首先,个位: 5+7=12......"', font_size=14, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        good_text.move_to(good_box.get_center())
        
        good_prompt.add(good_box, good_title, good_text)
        
        examples.add(bad_prompt, good_prompt)
        examples.arrange(RIGHT, buff=1)
        examples.next_to(idea, DOWN, buff=0.5)
        
        self.play(FadeIn(bad_prompt), run_time=0.5)
        self.wait(0.3)
        self.play(FadeIn(good_prompt), run_time=0.5)
        
        # 箭头
        arrow = Arrow(
            bad_box.get_right(),
            good_box.get_left(),
            color=ACCENT_COLOR, stroke_width=2
        )
        improve_label = Text("升级", font_size=14, color=ACCENT_COLOR)
        improve_label.next_to(arrow, UP, buff=0.05)
        
        self.play(GrowArrow(arrow), Write(improve_label), run_time=0.4)
        
        # 关键技巧
        tips = VGroup(
            Text("关键技巧:", font_size=18, color=ACCENT_COLOR),
            Text("• 思维链 (Chain of Thought)", font_size=16, color=TEXT_COLOR),
            Text("• 少样本示例 (Few-shot)", font_size=16, color=TEXT_COLOR),
            Text("• 角色扮演 (Role-playing)", font_size=16, color=TEXT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        tips.to_edge(DOWN, buff=0.5)
        
        self.play(Write(tips), run_time=0.6)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_quantization(self):
        """量化"""
        # 标题
        title = Text("2. 量化", font_size=36, color=SECONDARY_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 核心思想
        idea = Text("降低精度，大幅减少存储和计算", font_size=24, color=TEXT_COLOR)
        idea.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(idea), run_time=0.5)
        
        # 精度对比
        precision_demo = VGroup()
        
        # FP32
        fp32 = VGroup()
        fp32_bar = Rectangle(
            width=4, height=0.8,
            color=ERROR_COLOR,
            fill_opacity=0.5
        )
        fp32_bar.set_stroke(ERROR_COLOR, width=2)
        fp32_label = Text("FP32 (32位浮点)", font_size=16, color=ERROR_COLOR)
        fp32_label.next_to(fp32_bar, LEFT, buff=0.3)
        fp32_size = Text("4字节/参数", font_size=14, color=SUBTEXT_COLOR)
        fp32_size.next_to(fp32_bar, RIGHT, buff=0.3)
        fp32.add(fp32_bar, fp32_label, fp32_size)
        
        # FP16
        fp16 = VGroup()
        fp16_bar = Rectangle(
            width=2, height=0.8,
            color=ACCENT_COLOR,
            fill_opacity=0.5
        )
        fp16_bar.set_stroke(ACCENT_COLOR, width=2)
        fp16_label = Text("FP16 (16位浮点)", font_size=16, color=ACCENT_COLOR)
        fp16_label.next_to(fp16_bar, LEFT, buff=0.3)
        fp16_size = Text("2字节/参数", font_size=14, color=SUBTEXT_COLOR)
        fp16_size.next_to(fp16_bar, RIGHT, buff=0.3)
        fp16.add(fp16_bar, fp16_label, fp16_size)
        
        # INT8
        int8 = VGroup()
        int8_bar = Rectangle(
            width=1, height=0.8,
            color=SECONDARY_COLOR,
            fill_opacity=0.5
        )
        int8_bar.set_stroke(SECONDARY_COLOR, width=2)
        int8_label = Text("INT8 (8位整数)", font_size=16, color=SECONDARY_COLOR)
        int8_label.next_to(int8_bar, LEFT, buff=0.3)
        int8_size = Text("1字节/参数", font_size=14, color=SUBTEXT_COLOR)
        int8_size.next_to(int8_bar, RIGHT, buff=0.3)
        int8.add(int8_bar, int8_label, int8_size)
        
        # INT4
        int4 = VGroup()
        int4_bar = Rectangle(
            width=0.5, height=0.8,
            color=PRIMARY_COLOR,
            fill_opacity=0.5
        )
        int4_bar.set_stroke(PRIMARY_COLOR, width=2)
        int4_label = Text("INT4 (4位整数)", font_size=16, color=PRIMARY_COLOR)
        int4_label.next_to(int4_bar, LEFT, buff=0.3)
        int4_size = Text("0.5字节/参数", font_size=14, color=SUBTEXT_COLOR)
        int4_size.next_to(int4_bar, RIGHT, buff=0.3)
        int4.add(int4_bar, int4_label, int4_size)
        
        precision_demo.add(fp32, fp16, int8, int4)
        precision_demo.arrange(DOWN, buff=0.3, aligned_edge=LEFT)
        precision_demo.next_to(idea, DOWN, buff=0.5)
        
        for item in precision_demo:
            self.play(FadeIn(item), run_time=0.3)
        
        # 效果
        effect = VGroup(
            Text("效果:", font_size=18, color=ACCENT_COLOR),
            Text("• 模型大小减少 4-8倍", font_size=16, color=SECONDARY_COLOR),
            Text("• 可部署在手机、边缘设备", font_size=16, color=TEXT_COLOR),
            Text("• 精度损失通常可接受", font_size=16, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        effect.to_edge(DOWN, buff=0.5)
        
        self.play(Write(effect), run_time=0.6)
        
        # 类比
        analogy = Text(
            "像'用小台秤代替专业天平'——够用就行",
            font_size=16, color=SUBTEXT_COLOR
        )
        analogy.next_to(effect, UP, buff=0.2)
        
        self.play(Write(analogy), run_time=0.4)
        
        self.wait(1.5)
        self.clear_scene()
    
    def show_lora(self):
        """LoRA适配器"""
        # 标题
        title = Text("3. LoRA 适配器", font_size=36, color=NEURAL_COLOR)
        title.to_edge(UP, buff=0.5)
        
        self.play(Write(title), run_time=0.5)
        
        # 核心思想
        idea = Text("高效微调：不更新整个模型，只训练小'适配器'", font_size=22, color=TEXT_COLOR)
        idea.next_to(title, DOWN, buff=0.4)
        
        self.play(Write(idea), run_time=0.5)
        
        # 可视化
        # 原始大模型
        big_model = VGroup()
        big_box = RoundedRectangle(
            width=3, height=4,
            corner_radius=0.15,
            color=SUBTEXT_COLOR,
            fill_opacity=0.2
        )
        big_box.set_stroke(SUBTEXT_COLOR, width=2)
        
        big_label = Text("原始大模型", font_size=18, color=SUBTEXT_COLOR)
        big_label.next_to(big_box, UP, buff=0.1)
        
        big_params = Text("100B 参数\n(冻结)", font_size=14, color=SUBTEXT_COLOR)
        big_params.move_to(big_box.get_center())
        
        # 冻结图标
        freeze_icon = Text("🔒", font_size=24)
        freeze_icon.next_to(big_params, DOWN, buff=0.2)
        
        big_model.add(big_box, big_label, big_params, freeze_icon)
        big_model.move_to(LEFT * 2 + DOWN * 0.5)
        
        self.play(FadeIn(big_model), run_time=0.5)
        
        # LoRA适配器（小块）
        lora_adapter = VGroup()
        lora_box = RoundedRectangle(
            width=1, height=1.5,
            corner_radius=0.1,
            color=ACCENT_COLOR,
            fill_opacity=0.5
        )
        lora_box.set_stroke(ACCENT_COLOR, width=3)
        
        lora_label = Text("LoRA\n适配器", font_size=14, color=TEXT_COLOR)
        lora_label.move_to(lora_box.get_center())
        
        lora_params = Text("0.1% 参数\n(可训练)", font_size=10, color=SECONDARY_COLOR)
        lora_params.next_to(lora_box, DOWN, buff=0.1)
        
        lora_adapter.add(lora_box, lora_label, lora_params)
        lora_adapter.next_to(big_box, RIGHT, buff=0.2).shift(UP * 0.5)
        
        # 插入动画
        self.play(
            FadeIn(lora_adapter, shift=LEFT * 0.5),
            run_time=0.6
        )
        
        # 连接线
        connection = Line(
            big_box.get_right() + UP * 0.3,
            lora_box.get_left(),
            color=ACCENT_COLOR, stroke_width=2
        )
        
        self.play(Create(connection), run_time=0.3)
        
        # 输出
        output_arrow = Arrow(
            lora_box.get_right(),
            lora_box.get_right() + RIGHT * 1.5,
            color=SECONDARY_COLOR, stroke_width=3
        )
        
        output_label = Text("定制能力", font_size=16, color=SECONDARY_COLOR)
        output_label.next_to(output_arrow, UP, buff=0.1)
        
        self.play(GrowArrow(output_arrow), Write(output_label), run_time=0.4)
        
        # 优势
        advantages = VGroup(
            Text("LoRA优势:", font_size=18, color=ACCENT_COLOR),
            Text("• 只需训练 0.1% 的参数", font_size=16, color=TEXT_COLOR),
            Text("• 存储成本极低", font_size=16, color=TEXT_COLOR),
            Text("• 可以同时保存多个适配器", font_size=16, color=TEXT_COLOR),
            Text("• 快速切换不同任务", font_size=16, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        advantages.to_edge(RIGHT, buff=0.5)
        
        self.play(Write(advantages), run_time=0.8)
        
        # 类比
        analogy = Text(
            "像'给大模型戴上不同的眼镜'",
            font_size=18, color=SUBTEXT_COLOR
        )
        analogy.to_edge(DOWN, buff=0.5)
        
        self.play(Write(analogy), run_time=0.4)
        
        self.wait(2)
        self.clear_scene()
    
    def show_summary(self):
        """总结"""
        # 标题
        title = Text("让普通人也能用上大模型", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.6)
        
        self.play(Write(title), run_time=0.6)
        
        # 三大技术
        techniques = VGroup()
        
        tech_data = [
            ("提示工程", "设计输入，唤醒能力", PRIMARY_COLOR),
            ("量化", "降低精度，减少开销", SECONDARY_COLOR),
            ("LoRA", "小适配器，快速定制", NEURAL_COLOR),
        ]
        
        for name, desc, color in tech_data:
            tech = VGroup()
            box = RoundedRectangle(
                width=3, height=1.8,
                corner_radius=0.1,
                color=color,
                fill_opacity=0.2
            )
            box.set_stroke(color, width=2)
            
            name_text = Text(name, font_size=22, color=color)
            name_text.move_to(box.get_center() + UP * 0.3)
            
            desc_text = Text(desc, font_size=14, color=TEXT_COLOR)
            desc_text.next_to(name_text, DOWN, buff=0.2)
            
            tech.add(box, name_text, desc_text)
            techniques.add(tech)
        
        techniques.arrange(RIGHT, buff=0.5)
        techniques.next_to(title, DOWN, buff=0.6)
        
        self.play(FadeIn(techniques, lag_ratio=0.2), run_time=0.8)
        
        # 最终洞察
        insight = VGroup(
            Text("这些技术让", font_size=22, color=TEXT_COLOR),
            Text("任何人都能参与AI革命", font_size=26, color=ACCENT_COLOR),
        ).arrange(DOWN, buff=0.2)
        insight.to_edge(DOWN, buff=0.6)
        
        box = SurroundingRectangle(insight, color=ACCENT_COLOR, buff=0.2, corner_radius=0.1)
        
        self.play(Write(insight), Create(box), run_time=0.8)
        
        self.wait(2)
    
    def clear_scene(self):
        """清除场景"""
        if len(self.mobjects) > 0:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# 测试运行
if __name__ == "__main__":
    scene = LargeModelsScene()
    scene.render()
