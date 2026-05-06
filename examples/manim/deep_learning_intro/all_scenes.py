"""
深度学习简明指南 - 完整场景合集
一次从神经元到创造力的思维漫游

基于 François Fleuret 的《The Little Book of Deep Learning》

运行单个场景:
    manim -pql all_scenes.py IntroScene
    manim -pqh all_scenes.py IntroScene

运行所有场景（顺序）:
    manim -pql all_scenes.py AllScenesSequence
"""

# 导入所有场景模块
from scene_01_intro import IntroScene
from scene_02_learning_paradigms import LearningParadigmsScene
from scene_03_gpu_tensor import GPUTensorScene
from scene_04_forward_backward import ForwardBackwardScene
from scene_05_loss_optimization import LossOptimizationScene
from scene_06_depth_value import DepthValueScene
from scene_07_building_blocks import BuildingBlocksScene
from scene_08_architectures import ArchitecturesScene
from scene_09_perception import PerceptionScene
from scene_10_generation import GenerationScene
from scene_11_large_models import LargeModelsScene
from scene_12_future import FutureScene

from manim import *

# ============ 颜色定义 ============
PRIMARY_COLOR = "#00D4FF"      # 青色 - 输入、数据
SECONDARY_COLOR = "#00FF88"    # 绿色 - 正确、优化
ACCENT_COLOR = "#FFD700"       # 金色 - 重点、高亮
NEURAL_COLOR = "#8B5CF6"       # 紫色 - 神经网络
ERROR_COLOR = "#FF6B6B"        # 红色 - 错误、损失
BG_COLOR = "#1a1a2e"           # 深色背景
TEXT_COLOR = "#FFFFFF"         # 白色文字
SUBTEXT_COLOR = "#A0A0A0"      # 灰色次要文字


# ============ 场景目录 ============
SCENE_REGISTRY = {
    "01": ("开场序幕 - GPU驱动的智能新时代", IntroScene),
    "02": ("学习范式 - 从规则到模式", LearningParadigmsScene),
    "03": ("引擎室 - GPU、TPU与张量", GPUTensorScene),
    "04": ("训练的艺术 - 前向传播与反向传播", ForwardBackwardScene),
    "05": ("损失函数与优化", LossOptimizationScene),
    "06": ("梯度挑战与深度的秘密", DepthValueScene),
    "07": ("模型组件库 - 构建AI大脑的乐高积木", BuildingBlocksScene),
    "08": ("经典架构 - 组装乐高，成就杰作", ArchitecturesScene),
    "09": ("感知与预测应用", PerceptionScene),
    "10": ("生成与创造", GenerationScene),
    "11": ("大模型时代的新技能", LargeModelsScene),
    "12": ("尾声 - 演进与未来", FutureScene),
}


def print_scene_info():
    """打印场景信息"""
    print("\n" + "=" * 60)
    print("深度学习简明指南 - 场景列表")
    print("=" * 60)
    
    for key, (name, scene_class) in SCENE_REGISTRY.items():
        print(f"  Scene {key}: {name}")
        print(f"            Class: {scene_class.__name__}")
    
    print("=" * 60)
    print("\n运行示例:")
    print("  manim -pql all_scenes.py IntroScene")
    print("  manim -pqh scene_02_learning_paradigms.py LearningParadigmsScene")
    print("\n")


class ChapterTitle(Scene):
    """章节标题场景 - 用于分隔不同部分"""
    
    def __init__(self, chapter_num=1, chapter_title="章节标题", **kwargs):
        super().__init__(**kwargs)
        self.chapter_num = chapter_num
        self.chapter_title = chapter_title
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 章节编号
        num = Text(f"第{self.chapter_num}章", font_size=28, color=SUBTEXT_COLOR)
        num.to_edge(UP, buff=1.5)
        
        # 章节标题
        title = Text(self.chapter_title, font_size=44, color=ACCENT_COLOR)
        title.next_to(num, DOWN, buff=0.4)
        
        # 装饰线
        line = Line(LEFT * 3, RIGHT * 3, color=ACCENT_COLOR, stroke_width=2)
        line.next_to(title, DOWN, buff=0.4)
        
        # 动画
        self.play(Write(num), run_time=0.5)
        self.play(Write(title), run_time=0.8)
        self.play(Create(line), run_time=0.4)
        
        self.wait(1.5)
        
        self.play(
            FadeOut(num), FadeOut(title), FadeOut(line),
            run_time=0.5
        )


class TransitionScene(Scene):
    """过渡场景 - 用于场景之间的过渡"""
    
    def __init__(self, transition_text="过渡", **kwargs):
        super().__init__(**kwargs)
        self.transition_text = transition_text
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        text = Text(self.transition_text, font_size=24, color=TEXT_COLOR)
        
        self.play(FadeIn(text, scale=0.9), run_time=0.5)
        self.wait(1)
        self.play(FadeOut(text), run_time=0.3)


class OpeningCredits(Scene):
    """开场字幕"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 主标题
        main_title = Text(
            "深度学习简明指南",
            font_size=52, color=ACCENT_COLOR
        )
        main_title.to_edge(UP, buff=1.5)
        
        # 副标题
        subtitle = Text(
            "一次从神经元到创造力的思维漫游",
            font_size=28, color=TEXT_COLOR
        )
        subtitle.next_to(main_title, DOWN, buff=0.5)
        
        # 装饰线
        line = Line(LEFT * 4, RIGHT * 4, color=NEURAL_COLOR, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.4)
        
        # 基于
        based_on = VGroup(
            Text("基于", font_size=18, color=SUBTEXT_COLOR),
            Text("François Fleuret", font_size=20, color=PRIMARY_COLOR),
            Text("《The Little Book of Deep Learning》", font_size=18, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        based_on.next_to(line, DOWN, buff=0.6)
        
        # 目标受众
        audience = Text(
            "面向科技爱好者与终身学习者",
            font_size=18, color=SECONDARY_COLOR
        )
        audience.to_edge(DOWN, buff=1)
        
        # 动画
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.play(Create(line), run_time=0.4)
        self.play(FadeIn(based_on), run_time=0.6)
        self.play(Write(audience), run_time=0.5)
        
        self.wait(2)
        
        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=0.8
        )


class ClosingCredits(Scene):
    """结尾字幕"""
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 感谢观看
        thanks = Text("感谢观看", font_size=48, color=ACCENT_COLOR)
        thanks.to_edge(UP, buff=1.5)
        
        self.play(Write(thanks), run_time=0.8)
        
        # 参考资料
        reference = VGroup(
            Text("参考资料:", font_size=20, color=TEXT_COLOR),
            Text("François Fleuret", font_size=18, color=PRIMARY_COLOR),
            Text("《The Little Book of Deep Learning》", font_size=18, color=SUBTEXT_COLOR),
            Text("V1.2, May 19, 2024", font_size=14, color=SUBTEXT_COLOR),
        ).arrange(DOWN, buff=0.1)
        reference.next_to(thanks, DOWN, buff=0.8)
        
        self.play(FadeIn(reference), run_time=0.6)
        
        # 制作信息
        made_with = VGroup(
            Text("Made with", font_size=16, color=SUBTEXT_COLOR),
            Text("Manim", font_size=20, color=SECONDARY_COLOR),
        ).arrange(RIGHT, buff=0.2)
        made_with.to_edge(DOWN, buff=1)
        
        self.play(Write(made_with), run_time=0.5)
        
        self.wait(2)
        
        self.play(
            *[FadeOut(m) for m in self.mobjects],
            run_time=1
        )


class AllScenesSequence(Scene):
    """
    完整场景序列 - 一次性播放所有12个场景
    
    注意：由于每个场景有独立的辅助方法，建议使用 render_all.sh 脚本
    分别渲染各场景后用 ffmpeg 合并。
    
    或者单独运行各场景:
        manim -pql scene_01_intro.py IntroScene
        manim -pql scene_02_learning_paradigms.py LearningParadigmsScene
        ...
    
    本类提供简化版合集预览。
    """
    
    def construct(self):
        self.camera.background_color = BG_COLOR
        
        # 场景信息列表
        scenes_info = [
            ("01", "开场序幕", "GPU驱动的智能新时代"),
            ("02", "学习范式", "从规则到模式的转变"),
            ("03", "引擎室", "GPU、TPU与张量运算"),
            ("04", "训练的艺术", "前向传播与反向传播"),
            ("05", "损失与优化", "目标函数与优化器"),
            ("06", "深度的价值", "梯度挑战与表示学习"),
            ("07", "组件库", "构建AI大脑的乐高积木"),
            ("08", "经典架构", "MLP、CNN、Transformer"),
            ("09", "感知应用", "分类、检测与分割"),
            ("10", "生成与创造", "GPT与扩散模型"),
            ("11", "大模型技能", "提示工程与高效微调"),
            ("12", "未来展望", "AI的演进与可能"),
        ]
        
        # 开场字幕
        self.show_opening()
        
        # 显示场景目录概览
        self.show_table_of_contents(scenes_info)
        
        # 提示信息
        self.show_usage_info()
        
        # 结尾
        self.show_closing()
    
    def show_opening(self):
        """开场字幕"""
        main_title = Text("深度学习简明指南", font_size=52, color=ACCENT_COLOR)
        main_title.to_edge(UP, buff=1.2)
        
        subtitle = Text("一次从神经元到创造力的思维漫游", font_size=28, color=TEXT_COLOR)
        subtitle.next_to(main_title, DOWN, buff=0.5)
        
        line = Line(LEFT * 4, RIGHT * 4, color=NEURAL_COLOR, stroke_width=2)
        line.next_to(subtitle, DOWN, buff=0.4)
        
        based_on = VGroup(
            Text("基于 François Fleuret", font_size=18, color=SUBTEXT_COLOR),
            Text("《The Little Book of Deep Learning》", font_size=18, color=PRIMARY_COLOR),
        ).arrange(DOWN, buff=0.1)
        based_on.next_to(line, DOWN, buff=0.5)
        
        self.play(Write(main_title), run_time=1)
        self.play(FadeIn(subtitle, shift=UP * 0.3), run_time=0.6)
        self.play(Create(line), run_time=0.4)
        self.play(FadeIn(based_on), run_time=0.6)
        
        self.wait(2)
        self.clear_all()
    
    def show_table_of_contents(self, scenes_info):
        """显示目录"""
        title = Text("内容目录", font_size=36, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.5)
        self.play(Write(title), run_time=0.5)
        
        # 分两列显示
        left_items = []
        right_items = []
        
        for i, (num, name, desc) in enumerate(scenes_info):
            item = VGroup(
                Text(f"{num}.", font_size=16, color=SUBTEXT_COLOR),
                Text(name, font_size=18, color=TEXT_COLOR),
            ).arrange(RIGHT, buff=0.1)
            
            if i < 6:
                left_items.append(item)
            else:
                right_items.append(item)
        
        left_col = VGroup(*left_items).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        right_col = VGroup(*right_items).arrange(DOWN, buff=0.25, aligned_edge=LEFT)
        
        left_col.move_to(LEFT * 2.5)
        right_col.move_to(RIGHT * 2.5)
        
        cols = VGroup(left_col, right_col)
        cols.next_to(title, DOWN, buff=0.6)
        
        # 逐个显示
        for item in left_items + right_items:
            self.play(FadeIn(item, shift=RIGHT * 0.2), run_time=0.15)
        
        self.wait(2)
        self.clear_all()
    
    def show_usage_info(self):
        """显示使用说明"""
        title = Text("运行各场景", font_size=32, color=ACCENT_COLOR)
        title.to_edge(UP, buff=0.8)
        
        commands = VGroup(
            Text("# 运行单个场景", font_size=16, color=SUBTEXT_COLOR),
            Text("manim -pql scene_01_intro.py IntroScene", font_size=14, color=SECONDARY_COLOR),
            Text("", font_size=10),
            Text("# 批量渲染并合并", font_size=16, color=SUBTEXT_COLOR),
            Text("./render_all.sh", font_size=14, color=SECONDARY_COLOR),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        commands.next_to(title, DOWN, buff=0.6)
        
        self.play(Write(title), run_time=0.5)
        self.play(FadeIn(commands), run_time=0.8)
        
        self.wait(2)
        self.clear_all()
    
    def show_closing(self):
        """结尾"""
        thanks = Text("开始探索深度学习的世界吧！", font_size=36, color=ACCENT_COLOR)
        self.play(Write(thanks), run_time=0.8)
        self.wait(2)
        self.clear_all()
    
    def clear_all(self):
        """清除所有对象"""
        if self.mobjects:
            self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)


# ============ 测试入口 ============
if __name__ == "__main__":
    print_scene_info()
