"""
函数与关系 - Scene 8: 总结与启示
回顾本章内容，总结核心思想和计算机科学应用

渲染命令: manim -pqh scene_08_summary.py Summary
"""

from manim import *
import numpy as np


# ========== 配色方案 ==========
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#4ECDC4"    # 青绿
    ACCENT = "#FF6B6B"       # 警示红
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    FUNCTION_COLOR = "#E74C3C"   # 函数红
    RELATION_COLOR = "#9B59B6"   # 关系紫
    SET_COLOR = "#3498DB"        # 集合蓝
    EQUIV_COLOR = "#2ECC71"      # 等价绿
    ORDER_COLOR = "#F39C12"      # 偏序橙


# ========== 工具函数 ==========
def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


def create_pyramid_layer(text, width, color, height=0.5):
    """创建金字塔层"""
    layer = VGroup()
    
    trapezoid = Polygon(
        LEFT * width/2 + UP * height/2,
        RIGHT * width/2 + UP * height/2,
        RIGHT * (width/2 - 0.3) + DOWN * height/2,
        LEFT * (width/2 - 0.3) + DOWN * height/2,
        fill_color=color,
        fill_opacity=0.3,
        stroke_color=color,
        stroke_width=2
    )
    
    label = Text(text, font_size=14, color=Colors.TEXT)
    label.move_to(trapezoid.get_center())
    
    layer.add(trapezoid, label)
    return layer


# ========== Scene 8: 总结与启示 ==========
class Summary(Scene):
    """总结与启示"""
    
    CHAPTER_TITLE = "第四章：函数与关系"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.knowledge_review()
        self.computer_science_applications()
        self.three_insights()
        self.finale()
        
        clear_scene(self)
    
    def knowledge_review(self):
        """知识体系回顾"""
        section_title = Text("知识体系回顾", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 知识流程图
        # 函数 → 关系 → 特殊关系（等价/偏序）
        flow = VGroup()
        
        # 函数
        func_box = VGroup(
            RoundedRectangle(width=2.2, height=1.0, corner_radius=0.1,
                            stroke_color=Colors.FUNCTION_COLOR, stroke_width=2),
            Text("函数", font_size=16, color=Colors.FUNCTION_COLOR),
            Text("严格的配对", font_size=10, color=Colors.GRAY),
        )
        func_box[1].move_to(func_box[0].get_center() + UP * 0.15)
        func_box[2].move_to(func_box[0].get_center() + DOWN * 0.15)
        flow.add(func_box)
        
        arrow1 = Arrow(ORIGIN, RIGHT * 0.8, color=Colors.GRAY, stroke_width=2, buff=0)
        flow.add(arrow1)
        
        # 关系
        rel_box = VGroup(
            RoundedRectangle(width=2.2, height=1.0, corner_radius=0.1,
                            stroke_color=Colors.RELATION_COLOR, stroke_width=2),
            Text("二元关系", font_size=16, color=Colors.RELATION_COLOR),
            Text("自由的配对", font_size=10, color=Colors.GRAY),
        )
        rel_box[1].move_to(rel_box[0].get_center() + UP * 0.15)
        rel_box[2].move_to(rel_box[0].get_center() + DOWN * 0.15)
        flow.add(rel_box)
        
        arrow2 = Arrow(ORIGIN, RIGHT * 0.8, color=Colors.GRAY, stroke_width=2, buff=0)
        flow.add(arrow2)
        
        # 特殊关系
        special = VGroup()
        
        equiv_box = VGroup(
            RoundedRectangle(width=2.0, height=0.7, corner_radius=0.1,
                            stroke_color=Colors.EQUIV_COLOR, stroke_width=2),
            Text("等价关系", font_size=14, color=Colors.EQUIV_COLOR),
        )
        equiv_box[1].move_to(equiv_box[0].get_center())
        
        order_box = VGroup(
            RoundedRectangle(width=2.0, height=0.7, corner_radius=0.1,
                            stroke_color=Colors.ORDER_COLOR, stroke_width=2),
            Text("偏序关系", font_size=14, color=Colors.ORDER_COLOR),
        )
        order_box[1].move_to(order_box[0].get_center())
        
        special.add(equiv_box, order_box)
        special.arrange(DOWN, buff=0.2)
        flow.add(special)
        
        flow.arrange(RIGHT, buff=0.2)
        flow.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        # 调整箭头位置
        arrow1.next_to(func_box, RIGHT, buff=0.1)
        rel_box.next_to(arrow1, RIGHT, buff=0.1)
        arrow2.next_to(rel_box, RIGHT, buff=0.1)
        special.next_to(arrow2, RIGHT, buff=0.1)
        
        self.play(FadeIn(func_box))
        self.play(GrowArrow(arrow1))
        self.play(FadeIn(rel_box))
        self.play(GrowArrow(arrow2))
        self.play(FadeIn(special))
        
        # 核心进展
        progress = VGroup(
            Text("从具体到抽象", font_size=14, color=Colors.PRIMARY),
            Text("从严格到灵活", font_size=14, color=Colors.SECONDARY),
            Text("从一般到特殊", font_size=14, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.8)
        progress.next_to(flow, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(progress))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(func_box), FadeOut(arrow1),
            FadeOut(rel_box), FadeOut(arrow2), FadeOut(special),
            FadeOut(progress),
            run_time=0.5
        )
    
    def computer_science_applications(self):
        """计算机科学的应用"""
        section_title = Text("计算机科学中的应用", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        applications = VGroup()
        
        # 函数应用
        app1 = VGroup(
            Text("函数", font_size=16, color=Colors.FUNCTION_COLOR),
            Text("程序中的函数/方法", font_size=12, color=Colors.GRAY),
            Text("输入 → 输出 的映射", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        app1_box = SurroundingRectangle(app1, color=Colors.FUNCTION_COLOR, buff=0.15)
        applications.add(VGroup(app1_box, app1))
        
        # 关系应用
        app2 = VGroup(
            Text("关系", font_size=16, color=Colors.RELATION_COLOR),
            Text("数据库表", font_size=12, color=Colors.GRAY),
            Text("n 元关系 = 数据表", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        app2_box = SurroundingRectangle(app2, color=Colors.RELATION_COLOR, buff=0.15)
        applications.add(VGroup(app2_box, app2))
        
        # 等价关系应用
        app3 = VGroup(
            Text("等价关系", font_size=16, color=Colors.EQUIV_COLOR),
            Text("数据分类/聚类", font_size=12, color=Colors.GRAY),
            Text("状态合并/去重", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        app3_box = SurroundingRectangle(app3, color=Colors.EQUIV_COLOR, buff=0.15)
        applications.add(VGroup(app3_box, app3))
        
        # 偏序关系应用
        app4 = VGroup(
            Text("偏序关系", font_size=16, color=Colors.ORDER_COLOR),
            Text("任务调度/依赖", font_size=12, color=Colors.GRAY),
            Text("版本控制/继承", font_size=12, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1)
        app4_box = SurroundingRectangle(app4, color=Colors.ORDER_COLOR, buff=0.15)
        applications.add(VGroup(app4_box, app4))
        
        applications.arrange(RIGHT, buff=0.3)
        applications.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        for app in applications:
            self.play(FadeIn(app, shift=UP * 0.2), run_time=0.5)
        
        # 核心信息
        core = Text(
            "函数和关系是计算机处理数据的核心抽象！",
            font_size=18, color=Colors.ACCENT
        )
        core.next_to(applications, DOWN, buff=0.5).set_x(0)
        
        core_box = SurroundingRectangle(core, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(core), Create(core_box))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(applications),
            FadeOut(core), FadeOut(core_box),
            run_time=0.5
        )
    
    def three_insights(self):
        """三个核心启示"""
        section_title = Text("三个核心启示", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        insights = VGroup()
        
        # 启示1
        insight1 = VGroup(
            RoundedRectangle(width=3.0, height=1.8, corner_radius=0.1,
                            stroke_color=Colors.PRIMARY, stroke_width=2),
            Text("抽象的威力", font_size=16, color=Colors.PRIMARY),
            VGroup(
                Text("一套理论", font_size=12, color=Colors.GRAY),
                Text("多种应用", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05),
        )
        insight1[1].move_to(insight1[0].get_top() + DOWN * 0.35)
        insight1[2].move_to(insight1[0].get_center() + DOWN * 0.2)
        insights.add(insight1)
        
        # 启示2
        insight2 = VGroup(
            RoundedRectangle(width=3.0, height=1.8, corner_radius=0.1,
                            stroke_color=Colors.SECONDARY, stroke_width=2),
            Text("结构的重要性", font_size=16, color=Colors.SECONDARY),
            VGroup(
                Text("识别数据间的", font_size=12, color=Colors.GRAY),
                Text("隐藏结构", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05),
        )
        insight2[1].move_to(insight2[0].get_top() + DOWN * 0.35)
        insight2[2].move_to(insight2[0].get_center() + DOWN * 0.2)
        insights.add(insight2)
        
        # 启示3
        insight3 = VGroup(
            RoundedRectangle(width=3.0, height=1.8, corner_radius=0.1,
                            stroke_color=Colors.ACCENT, stroke_width=2),
            Text("放松与灵活", font_size=16, color=Colors.ACCENT),
            VGroup(
                Text("放松约束", font_size=12, color=Colors.GRAY),
                Text("获得更大灵活性", font_size=12, color=Colors.GRAY),
            ).arrange(DOWN, buff=0.05),
        )
        insight3[1].move_to(insight3[0].get_top() + DOWN * 0.35)
        insight3[2].move_to(insight3[0].get_center() + DOWN * 0.2)
        insights.add(insight3)
        
        insights.arrange(RIGHT, buff=0.3)
        insights.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for insight in insights:
            self.play(FadeIn(insight, scale=0.9), run_time=0.5)
        
        self.wait(2)
        
        self.play(FadeOut(section_title), FadeOut(insights), run_time=0.5)
    
    def finale(self):
        """升华与结语"""
        # 主题句
        quote = VGroup(
            Text("理解事物间联系的框架", font_size=32, color=Colors.PRIMARY),
        )
        quote.move_to(ORIGIN + UP * 1.0)
        
        self.play(FadeIn(quote, scale=0.8))
        self.wait(0.8)
        
        # 框架总结
        framework = VGroup(
            Text("精确配对", font_size=16, color=Colors.FUNCTION_COLOR),
            Text("→", font_size=20, color=Colors.GRAY),
            Text("自由联系", font_size=16, color=Colors.RELATION_COLOR),
            Text("→", font_size=20, color=Colors.GRAY),
            Text("结构梳理", font_size=16, color=Colors.EQUIV_COLOR),
        ).arrange(RIGHT, buff=0.2)
        framework.next_to(quote, DOWN, buff=0.5)
        
        framework_labels = VGroup(
            Text("函数", font_size=12, color=Colors.GRAY),
            Text("", font_size=12),
            Text("关系", font_size=12, color=Colors.GRAY),
            Text("", font_size=12),
            Text("等价/偏序", font_size=12, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.3)
        framework_labels.next_to(framework, DOWN, buff=0.1)
        
        self.play(FadeIn(framework), FadeIn(framework_labels))
        self.wait(1)
        
        # 要点回顾
        recap = VGroup(
            Text("本章要点：", font_size=16, color=Colors.TEXT),
            Text("✓ 函数：定义域到值域的唯一映射", font_size=13, color=Colors.GRAY),
            Text("✓ 单射/满射/双射：函数的特殊性质", font_size=13, color=Colors.GRAY),
            Text("✓ 二元关系：更自由的配对方式", font_size=13, color=Colors.GRAY),
            Text("✓ 关系的表示：集合、矩阵、有向图", font_size=13, color=Colors.GRAY),
            Text("✓ 等价关系：划分集合，构造新对象", font_size=13, color=Colors.GRAY),
            Text("✓ 偏序关系：表达顺序，绘制哈斯图", font_size=13, color=Colors.GRAY),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        recap.next_to(framework_labels, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(recap, shift=UP * 0.2))
        self.wait(1)
        
        # 感谢
        thanks = Text("感谢观看！", font_size=28, color=Colors.SECONDARY)
        thanks.next_to(recap, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(thanks, scale=0.8))
        self.wait(2.5)


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_08_summary.py Summary
    pass
