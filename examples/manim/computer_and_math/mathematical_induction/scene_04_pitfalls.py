"""
数学归纳法 - Scene 4: 归纳法的陷阱
展示使用归纳法时的常见错误和著名诡辩

渲染命令: manim -pqh scene_04_pitfalls.py InductionPitfalls
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
    DOMINO_COLOR = "#F39C12" # 多米诺橙
    BASE_COLOR = "#2ECC71"   # 基础步骤绿
    INDUCT_COLOR = "#9B59B6" # 归纳步骤紫
    LOOP_COLOR = "#E74C3C"   # 循环红
    CODE_COLOR = "#3498DB"   # 代码蓝
    WARNING_COLOR = "#F39C12" # 警告橙


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


def create_horse(color=Colors.DOMINO_COLOR, scale=1.0):
    """创建简化的马图标"""
    # 用简单的形状组合表示马
    body = Ellipse(width=0.8, height=0.4)
    body.set_stroke(color, width=2)
    body.set_fill(color, opacity=0.6)
    
    head = Circle(radius=0.15)
    head.set_stroke(color, width=2)
    head.set_fill(color, opacity=0.6)
    head.next_to(body, RIGHT, buff=-0.1).shift(UP * 0.1)
    
    horse = VGroup(body, head)
    horse.scale(scale)
    return horse


# ========== Scene 4: 归纳法的陷阱 ==========
class InductionPitfalls(Scene):
    """归纳法的常见陷阱"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.pitfall_intro()
        self.pitfall_no_base()
        self.pitfall_wrong_direction()
        self.pitfall_all_horses()
        
        clear_scene(self)
    
    def pitfall_intro(self):
        """陷阱介绍"""
        section_title = Text("归纳法的常见陷阱", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        warning = VGroup(
            Text("⚠️ 警告", font_size=24, color=Colors.WARNING_COLOR),
            Text("归纳法虽然强大，但使用不当会导致荒谬的结论", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.2)
        warning.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(warning))
        self.wait(1.5)
        
        # 三个陷阱预览
        pitfalls = VGroup(
            Text("① 忘记基础步骤", font_size=18, color=Colors.ACCENT),
            Text("② 逆转蕴含方向", font_size=18, color=Colors.ACCENT),
            Text("③ 归纳步骤有漏洞", font_size=18, color=Colors.ACCENT),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        pitfalls.next_to(warning, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(pitfalls))
        self.wait(1.5)
        
        self.play(FadeOut(section_title), FadeOut(warning), FadeOut(pitfalls), run_time=0.5)
    
    def pitfall_no_base(self):
        """陷阱一：忘记基础步骤"""
        section_title = Text("陷阱一：忘记基础步骤", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 错误命题
        fake_claim = VGroup(
            Text('错误"证明"：', font_size=18, color=Colors.ACCENT),
            Text("前 n 个正偶数的和是奇数", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        fake_claim.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(fake_claim))
        
        # 假归纳步骤
        induct_title = Text('归纳步骤"看似正确"：', font_size=16, color=Colors.INDUCT_COLOR)
        induct_title.next_to(fake_claim, DOWN, buff=0.4).align_to(fake_claim, LEFT)
        
        self.play(FadeIn(induct_title))
        
        induct_content = VGroup(
            Text("假设：前 m 个正偶数的和是奇数", font_size=16, color=Colors.GRAY),
            Text("推导：前 m+1 个正偶数的和", font_size=16, color=Colors.TEXT),
            Text("= (前 m 个的和) + (第 m+1 个偶数)", font_size=16, color=Colors.TEXT),
            Text("= 奇数 + 偶数 = 奇数 ✓", font_size=16, color=Colors.INDUCT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        induct_content.next_to(induct_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(FadeIn(induct_content))
        self.wait(1)
        
        # 但是！
        but = Text("但是！", font_size=24, color=Colors.ACCENT)
        but.next_to(induct_content, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(but, scale=1.5))
        
        # 基础步骤检验
        base_check = VGroup(
            Text("基础步骤 (n=1)：", font_size=16, color=Colors.BASE_COLOR),
            Text("第 1 个正偶数 = ", font_size=16, color=Colors.TEXT),
            MathTex(r"2", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        base_check.next_to(but, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(base_check))
        
        base_fail = VGroup(
            MathTex(r"2", font_size=22, color=Colors.ACCENT),
            Text(" 是偶数，不是奇数！", font_size=16, color=Colors.ACCENT),
            Text(" ✗", font_size=20, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.08)
        base_fail.next_to(base_check, DOWN, buff=0.15).set_x(0)
        
        self.play(FadeIn(base_fail))
        self.wait(1)
        
        # 地基崩塌动画
        warning_box = VGroup(
            Text("教训：", font_size=18, color=Colors.WARNING_COLOR),
            Text('没有正确的基础步骤，整个"证明"建立在虚假之上', font_size=16, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        warning_box.next_to(base_fail, DOWN, buff=0.4).set_x(0)
        
        warning_border = SurroundingRectangle(warning_box, color=Colors.WARNING_COLOR, buff=0.15)
        
        self.play(FadeIn(warning_box), Create(warning_border))
        
        # 简化的大厦崩塌效果
        building_blocks = VGroup()
        for i in range(4):
            block = Rectangle(height=0.4, width=0.8)
            block.set_stroke(Colors.GRAY, width=2)
            block.set_fill(Colors.GRAY, opacity=0.5)
            block.shift(UP * i * 0.45)
            building_blocks.add(block)
        
        building_blocks.to_edge(RIGHT, buff=1.5).shift(DOWN * 0.5)
        
        # 地基
        foundation = Rectangle(height=0.3, width=1.0)
        foundation.set_stroke(Colors.ACCENT, width=2)
        foundation.set_fill(Colors.ACCENT, opacity=0.3)
        foundation.next_to(building_blocks[0], DOWN, buff=0)
        
        foundation_label = Text("基础", font_size=12, color=Colors.TEXT)
        foundation_label.move_to(foundation.get_center())
        
        building = VGroup(foundation, foundation_label, building_blocks)
        
        self.play(FadeIn(building))
        self.wait(0.5)
        
        # 地基消失，大厦倾倒
        self.play(
            FadeOut(foundation), FadeOut(foundation_label),
            *[block.animate.shift(DOWN * 0.5 + RIGHT * np.random.uniform(-0.3, 0.3)).rotate(np.random.uniform(-0.5, 0.5))
              for block in building_blocks],
            run_time=1
        )
        
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(fake_claim),
            FadeOut(induct_title), FadeOut(induct_content),
            FadeOut(but), FadeOut(base_check), FadeOut(base_fail),
            FadeOut(warning_box), FadeOut(warning_border),
            FadeOut(building_blocks),
            run_time=0.5
        )
    
    def pitfall_wrong_direction(self):
        """陷阱二：逆转蕴含方向"""
        section_title = Text("陷阱二：逆转蕴含方向", font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 正确方向
        correct_title = Text("✓ 正确方向：", font_size=18, color=Colors.BASE_COLOR)
        correct_content = MathTex(
            r"P(m) \Rightarrow P(m+1)",
            font_size=26, color=Colors.BASE_COLOR
        )
        correct_explain = Text("从假设推出结论", font_size=16, color=Colors.GRAY)
        
        correct_group = VGroup(correct_title, correct_content, correct_explain).arrange(DOWN, buff=0.15)
        correct_box = SurroundingRectangle(correct_group, color=Colors.BASE_COLOR, buff=0.15)
        correct_full = VGroup(correct_group, correct_box)
        
        # 错误方向
        wrong_title = Text("✗ 错误方向：", font_size=18, color=Colors.ACCENT)
        wrong_content = MathTex(
            r"P(m+1) \Rightarrow P(m)",
            font_size=26, color=Colors.ACCENT
        )
        wrong_explain = Text("用结论推假设（循环论证）", font_size=16, color=Colors.GRAY)
        
        wrong_group = VGroup(wrong_title, wrong_content, wrong_explain).arrange(DOWN, buff=0.15)
        wrong_box = SurroundingRectangle(wrong_group, color=Colors.ACCENT, buff=0.15)
        wrong_full = VGroup(wrong_group, wrong_box)
        
        # 排列
        comparison = VGroup(correct_full, wrong_full).arrange(RIGHT, buff=0.8)
        comparison.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(correct_full))
        self.wait(0.8)
        self.play(FadeIn(wrong_full))
        self.wait(1)
        
        # 箭头动画展示方向重要性
        arrow_title = Text("箭头方向的重要性：", font_size=18, color=Colors.SECONDARY)
        arrow_title.next_to(comparison, DOWN, buff=0.5).align_to(comparison, LEFT)
        
        self.play(FadeIn(arrow_title))
        
        # 正确：从 P(1) 到 P(2) 到 P(3)...
        p_chain = VGroup()
        for i in range(1, 5):
            p = MathTex(f"P({i})", font_size=20, color=Colors.BASE_COLOR if i == 1 else Colors.TEXT)
            p_chain.add(p)
        
        arrows = VGroup()
        p_chain.arrange(RIGHT, buff=0.6)
        
        for i in range(3):
            arrow = Arrow(
                p_chain[i].get_right() + RIGHT * 0.1,
                p_chain[i+1].get_left() + LEFT * 0.1,
                color=Colors.BASE_COLOR, stroke_width=2, buff=0
            )
            arrows.add(arrow)
        
        chain_group = VGroup(p_chain, arrows)
        chain_group.next_to(arrow_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(p_chain[0]))
        for i in range(3):
            self.play(GrowArrow(arrows[i]), FadeIn(p_chain[i+1]), run_time=0.4)
        
        # 类比：多米诺骨牌只能向前推
        analogy = Text("类比：骨牌只能向前推，不能向后拉", font_size=16, color=Colors.GRAY)
        analogy.next_to(chain_group, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(comparison),
            FadeOut(arrow_title), FadeOut(chain_group),
            FadeOut(analogy),
            run_time=0.5
        )
    
    def pitfall_all_horses(self):
        """陷阱三：所有马都同色"""
        section_title = Text('陷阱三："所有马都同色"', font_size=26, color=Colors.ACCENT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 命题
        claim = VGroup(
            Text("著名诡辩：", font_size=18, color=Colors.WARNING_COLOR),
            Text('"证明"任意 n 匹马都是同一颜色', font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        claim.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(claim))
        self.wait(0.5)
        
        # P(1) 正确
        p1_title = Text("P(1)：1 匹马同色", font_size=18, color=Colors.BASE_COLOR)
        p1_title.next_to(claim, DOWN, buff=0.4).align_to(claim, LEFT)
        
        horse1 = create_horse(Colors.DOMINO_COLOR, scale=0.8)
        horse1.next_to(p1_title, DOWN, buff=0.2)
        
        p1_check = Text("✓ 显然正确", font_size=16, color=Colors.BASE_COLOR)
        p1_check.next_to(horse1, RIGHT, buff=0.3)
        
        self.play(FadeIn(p1_title), FadeIn(horse1), FadeIn(p1_check))
        self.wait(0.5)
        
        # 归纳步骤的"逻辑"
        induct_title = Text('归纳步骤"逻辑"：', font_size=18, color=Colors.INDUCT_COLOR)
        induct_title.next_to(horse1, DOWN, buff=0.4).align_to(p1_title, LEFT)
        
        self.play(FadeIn(induct_title))
        
        induct_logic = VGroup(
            Text("假设任意 m 匹马同色", font_size=16, color=Colors.GRAY),
            Text("对于 m+1 匹马，去掉第一匹，剩下 m 匹同色", font_size=16, color=Colors.TEXT),
            Text("去掉最后一匹，剩下 m 匹也同色", font_size=16, color=Colors.TEXT),
            Text('中间有"公共马"，所以 m+1 匹都同色', font_size=16, color=Colors.INDUCT_COLOR),
        ).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        induct_logic.next_to(induct_title, DOWN, buff=0.2).shift(RIGHT * 0.3)
        
        self.play(FadeIn(induct_logic))
        self.wait(1)
        
        # 关键错误：P(2) 的情况
        self.play(
            FadeOut(p1_title), FadeOut(horse1), FadeOut(p1_check),
            FadeOut(induct_title), FadeOut(induct_logic),
            run_time=0.5
        )
        
        error_title = VGroup(
            Text("问题出在哪？", font_size=22, color=Colors.ACCENT),
            Text("看 P(1) → P(2) 这一步！", font_size=18, color=Colors.TEXT),
        ).arrange(DOWN, buff=0.1)
        error_title.next_to(claim, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(error_title))
        
        # 两匹马的情况
        horse_a = create_horse(Colors.BASE_COLOR, scale=0.8)
        horse_a_label = Text("马A", font_size=14, color=Colors.TEXT)
        horse_a_label.next_to(horse_a, DOWN, buff=0.1)
        horse_a_group = VGroup(horse_a, horse_a_label)
        
        horse_b = create_horse(Colors.ACCENT, scale=0.8)
        horse_b_label = Text("马B", font_size=14, color=Colors.TEXT)
        horse_b_label.next_to(horse_b, DOWN, buff=0.1)
        horse_b_group = VGroup(horse_b, horse_b_label)
        
        two_horses = VGroup(horse_a_group, horse_b_group).arrange(RIGHT, buff=1.5)
        two_horses.next_to(error_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(two_horses))
        
        # 框选"去掉第一匹"和"去掉最后一匹"
        box_a = SurroundingRectangle(horse_a_group, color=Colors.INDUCT_COLOR, buff=0.15)
        box_a_label = Text("去掉B后", font_size=12, color=Colors.INDUCT_COLOR)
        box_a_label.next_to(box_a, UP, buff=0.1)
        
        box_b = SurroundingRectangle(horse_b_group, color=Colors.INDUCT_COLOR, buff=0.15)
        box_b_label = Text("去掉A后", font_size=12, color=Colors.INDUCT_COLOR)
        box_b_label.next_to(box_b, UP, buff=0.1)
        
        self.play(Create(box_a), FadeIn(box_a_label))
        self.wait(0.3)
        self.play(Create(box_b), FadeIn(box_b_label))
        self.wait(0.5)
        
        # 关键：没有公共马！
        no_common = VGroup(
            Text("关键问题：", font_size=18, color=Colors.ACCENT),
            Text("两个集合没有", font_size=18, color=Colors.TEXT),
            Text('"公共马"', font_size=18, color=Colors.ACCENT),
            Text("！", font_size=18, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        no_common.next_to(two_horses, DOWN, buff=0.5).set_x(0)
        
        no_common_box = SurroundingRectangle(no_common, color=Colors.ACCENT, buff=0.15)
        
        self.play(FadeIn(no_common), Create(no_common_box))
        self.wait(1)
        
        # 教训
        lesson = VGroup(
            Text("教训：", font_size=18, color=Colors.WARNING_COLOR),
            Text("归纳步骤必须对", font_size=16, color=Colors.TEXT),
            Text("所有 m ≥ 1", font_size=16, color=Colors.INDUCT_COLOR),
            Text(" 都成立", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        lesson.next_to(no_common_box, DOWN, buff=0.4).set_x(0)
        
        lesson2 = Text("这里 m=1 时归纳步骤就失效了！", font_size=16, color=Colors.ACCENT)
        lesson2.next_to(lesson, DOWN, buff=0.15)
        
        self.play(FadeIn(lesson), FadeIn(lesson2))
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(claim),
            FadeOut(error_title), FadeOut(two_horses),
            FadeOut(box_a), FadeOut(box_a_label),
            FadeOut(box_b), FadeOut(box_b_label),
            FadeOut(no_common), FadeOut(no_common_box),
            FadeOut(lesson), FadeOut(lesson2),
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_04_pitfalls.py InductionPitfalls
    pass
