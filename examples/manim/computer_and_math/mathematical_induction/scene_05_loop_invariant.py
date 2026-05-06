"""
数学归纳法 - Scene 5: 循环不变量
展示循环不变量如何与归纳法结合，用于程序正确性证明

渲染命令: manim -pqh scene_05_loop_invariant.py LoopInvariant
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
    INVARIANT_COLOR = "#9B59B6" # 不变量紫


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


def create_code_block(code_lines, font_size=14, highlight_line=None):
    """创建代码块"""
    code_group = VGroup()
    
    for i, line in enumerate(code_lines):
        # 处理缩进
        indent = len(line) - len(line.lstrip())
        line_text = Text(line, font_size=font_size, font="Menlo")
        
        if highlight_line is not None and i == highlight_line:
            line_text.set_color(Colors.LOOP_COLOR)
        else:
            line_text.set_color(Colors.CODE_COLOR)
        
        code_group.add(line_text)
    
    code_group.arrange(DOWN, buff=0.08, aligned_edge=LEFT)
    
    # 背景框
    bg = RoundedRectangle(
        width=code_group.width + 0.4,
        height=code_group.height + 0.3,
        corner_radius=0.1
    )
    bg.set_stroke(Colors.CODE_COLOR, width=1)
    bg.set_fill(Colors.BG, opacity=0.8)
    bg.move_to(code_group.get_center())
    
    return VGroup(bg, code_group)


# ========== Scene 5: 循环不变量 ==========
class LoopInvariant(Scene):
    """循环不变量与程序验证"""
    
    CHAPTER_TITLE = "第五章：数学归纳法"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        # 各部分
        self.loop_invariant_intro()
        self.three_step_proof()
        self.sum_loop_example()
        
        clear_scene(self)
    
    def loop_invariant_intro(self):
        """循环不变量介绍"""
        section_title = Text("循环不变量", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 问题
        question = VGroup(
            Text("问题：", font_size=20, color=Colors.PRIMARY),
            Text("如何保证循环代码是正确的？", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        question.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(question))
        self.wait(0.8)
        
        # 定义
        definition_title = Text("循环不变量定义：", font_size=18, color=Colors.INVARIANT_COLOR)
        definition_title.next_to(question, DOWN, buff=0.5).align_to(question, LEFT)
        
        definition = VGroup(
            Text("在循环执行过程中", font_size=16, color=Colors.TEXT),
            Text("始终保持为真", font_size=16, color=Colors.INVARIANT_COLOR),
            Text("的条件", font_size=16, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.08)
        definition.next_to(definition_title, DOWN, buff=0.15)
        
        definition_box = SurroundingRectangle(VGroup(definition_title, definition), color=Colors.INVARIANT_COLOR, buff=0.15)
        
        self.play(FadeIn(definition_title), FadeIn(definition), Create(definition_box))
        self.wait(1)
        
        # 与归纳法的联系
        connection_title = Text("与归纳法的联系：", font_size=18, color=Colors.SECONDARY)
        connection_title.next_to(definition_box, DOWN, buff=0.5).align_to(definition_title, LEFT)
        
        self.play(FadeIn(connection_title))
        
        connection_content = VGroup(
            VGroup(
                Text("循环迭代 ", font_size=16, color=Colors.TEXT),
                MathTex(r"\Leftrightarrow", font_size=20, color=Colors.GRAY),
                Text(" 归纳过程", font_size=16, color=Colors.INDUCT_COLOR),
            ).arrange(RIGHT, buff=0.1),
            VGroup(
                Text("不变量保持 ", font_size=16, color=Colors.TEXT),
                MathTex(r"\Leftrightarrow", font_size=20, color=Colors.GRAY),
                Text(" 归纳步骤", font_size=16, color=Colors.INDUCT_COLOR),
            ).arrange(RIGHT, buff=0.1),
        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT)
        connection_content.next_to(connection_title, DOWN, buff=0.15).shift(RIGHT * 0.2)
        
        self.play(FadeIn(connection_content))
        self.wait(1.5)
        
        self.play(
            FadeOut(section_title), FadeOut(question),
            FadeOut(definition_title), FadeOut(definition), FadeOut(definition_box),
            FadeOut(connection_title), FadeOut(connection_content),
            run_time=0.5
        )
    
    def three_step_proof(self):
        """三步证明法"""
        section_title = Text("三步证明法", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 三个步骤
        step1 = VGroup(
            Text("① 初始化", font_size=20, color=Colors.BASE_COLOR),
            Text("（基础步骤）", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        step1_content = Text("循环开始前，不变量成立", font_size=16, color=Colors.TEXT)
        step1_group = VGroup(step1, step1_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        step1_box = SurroundingRectangle(step1_group, color=Colors.BASE_COLOR, buff=0.15)
        step1_full = VGroup(step1_group, step1_box)
        
        step2 = VGroup(
            Text("② 保持", font_size=20, color=Colors.INDUCT_COLOR),
            Text("（归纳步骤）", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        step2_content = Text("每次迭代后，不变量仍成立", font_size=16, color=Colors.TEXT)
        step2_group = VGroup(step2, step2_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        step2_box = SurroundingRectangle(step2_group, color=Colors.INDUCT_COLOR, buff=0.15)
        step2_full = VGroup(step2_group, step2_box)
        
        step3 = VGroup(
            Text("③ 终止", font_size=20, color=Colors.LOOP_COLOR),
            Text("（结论）", font_size=16, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        step3_content = Text("循环结束时，目标达成", font_size=16, color=Colors.TEXT)
        step3_group = VGroup(step3, step3_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        step3_box = SurroundingRectangle(step3_group, color=Colors.LOOP_COLOR, buff=0.15)
        step3_full = VGroup(step3_group, step3_box)
        
        steps = VGroup(step1_full, step2_full, step3_full).arrange(DOWN, buff=0.3)
        steps.next_to(section_title, DOWN, buff=0.5).set_x(0)
        
        for step in [step1_full, step2_full, step3_full]:
            self.play(FadeIn(step, shift=RIGHT * 0.2), run_time=0.6)
            self.wait(0.5)
        
        # 流程图
        flow_title = Text("流程图：", font_size=16, color=Colors.SECONDARY)
        flow_title.to_edge(RIGHT, buff=1.5).align_to(steps, UP)
        
        # 简化流程图
        init_box = RoundedRectangle(height=0.5, width=1.2, corner_radius=0.1)
        init_box.set_stroke(Colors.BASE_COLOR, width=2)
        init_label = Text("初始化", font_size=12, color=Colors.BASE_COLOR)
        init_label.move_to(init_box.get_center())
        init = VGroup(init_box, init_label)
        
        loop_box = RoundedRectangle(height=0.5, width=1.2, corner_radius=0.1)
        loop_box.set_stroke(Colors.INDUCT_COLOR, width=2)
        loop_label = Text("循环体", font_size=12, color=Colors.INDUCT_COLOR)
        loop_label.move_to(loop_box.get_center())
        loop = VGroup(loop_box, loop_label)
        
        end_box = RoundedRectangle(height=0.5, width=1.2, corner_radius=0.1)
        end_box.set_stroke(Colors.LOOP_COLOR, width=2)
        end_label = Text("终止", font_size=12, color=Colors.LOOP_COLOR)
        end_label.move_to(end_box.get_center())
        end = VGroup(end_box, end_label)
        
        flow = VGroup(init, loop, end).arrange(DOWN, buff=0.5)
        flow.next_to(flow_title, DOWN, buff=0.2)
        
        # 箭头
        arrow1 = Arrow(init.get_bottom(), loop.get_top(), color=Colors.GRAY, buff=0.1)
        arrow2 = Arrow(loop.get_bottom(), end.get_top(), color=Colors.GRAY, buff=0.1)
        
        # 循环箭头
        loop_arrow = CurvedArrow(
            loop.get_right() + RIGHT * 0.1,
            loop.get_right() + RIGHT * 0.1 + UP * 0.3,
            color=Colors.INDUCT_COLOR, angle=-PI
        )
        
        self.play(FadeIn(flow_title), FadeIn(init))
        self.play(GrowArrow(arrow1), FadeIn(loop))
        self.play(FadeIn(loop_arrow))
        self.play(GrowArrow(arrow2), FadeIn(end))
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(steps),
            FadeOut(flow_title), FadeOut(flow),
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(loop_arrow),
            run_time=0.5
        )
    
    def sum_loop_example(self):
        """求和循环示例"""
        section_title = Text("示例：求和循环", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        
        # 代码
        code_lines = [
            "sum = 0",
            "for i in range(1, n+1):",
            "    sum += i",
            "# 结果：sum = 1+2+...+n"
        ]
        
        code_texts = VGroup()
        for line in code_lines:
            text = Text(line, font_size=16, font="Menlo", color=Colors.CODE_COLOR)
            code_texts.add(text)
        code_texts.arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        
        code_bg = RoundedRectangle(
            width=code_texts.width + 0.4,
            height=code_texts.height + 0.3,
            corner_radius=0.1
        )
        code_bg.set_stroke(Colors.CODE_COLOR, width=1)
        code_bg.set_fill("#0a0a1a", opacity=0.9)
        code_bg.move_to(code_texts.get_center())
        
        code_block = VGroup(code_bg, code_texts)
        code_block.next_to(section_title, DOWN, buff=0.4).set_x(0).shift(LEFT * 1)
        
        self.play(FadeIn(code_block))
        self.wait(0.5)
        
        # 不变量定义
        invariant_title = Text("循环不变量：", font_size=18, color=Colors.INVARIANT_COLOR)
        invariant_title.next_to(code_block, RIGHT, buff=0.5).align_to(code_block, UP)
        
        invariant = MathTex(
            r"\text{sum} = 0 + 1 + \cdots + (i-1)",
            font_size=22, color=Colors.INVARIANT_COLOR
        )
        # 修复：中文用 Text，公式用 MathTex
        invariant_fixed = VGroup(
            Text("sum = 0+1+...+(i-1)", font_size=18, color=Colors.INVARIANT_COLOR),
        )
        invariant_fixed.next_to(invariant_title, DOWN, buff=0.15)
        
        invariant_box = SurroundingRectangle(VGroup(invariant_title, invariant_fixed), color=Colors.INVARIANT_COLOR, buff=0.15)
        
        self.play(FadeIn(invariant_title), FadeIn(invariant_fixed), Create(invariant_box))
        self.wait(1)
        
        # 三步验证
        verify_title = Text("三步验证：", font_size=18, color=Colors.SECONDARY)
        verify_title.next_to(code_block, DOWN, buff=0.5).align_to(code_block, LEFT)
        
        self.play(FadeIn(verify_title))
        
        # 初始化
        init_verify = VGroup(
            Text("① 初始化", font_size=16, color=Colors.BASE_COLOR),
            Text("（i=1 前）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        init_content = VGroup(
            Text("sum = 0 = 空和 ✓", font_size=14, color=Colors.TEXT),
        )
        init_group = VGroup(init_verify, init_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        init_group.next_to(verify_title, DOWN, buff=0.2).shift(RIGHT * 0.2)
        
        self.play(FadeIn(init_group))
        self.wait(0.5)
        
        # 保持
        maintain_verify = VGroup(
            Text("② 保持", font_size=16, color=Colors.INDUCT_COLOR),
            Text("（每次迭代后）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        maintain_content = VGroup(
            Text("迭代前：sum = 0+1+...+(i-1)", font_size=14, color=Colors.GRAY),
            Text("执行：sum += i", font_size=14, color=Colors.CODE_COLOR),
            Text("迭代后：sum = 0+1+...+i ✓", font_size=14, color=Colors.INDUCT_COLOR),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        maintain_group = VGroup(maintain_verify, maintain_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        maintain_group.next_to(init_group, DOWN, buff=0.2).align_to(init_group, LEFT)
        
        self.play(FadeIn(maintain_group))
        self.wait(0.5)
        
        # 终止
        term_verify = VGroup(
            Text("③ 终止", font_size=16, color=Colors.LOOP_COLOR),
            Text("（i = n+1 时）", font_size=14, color=Colors.GRAY),
        ).arrange(RIGHT, buff=0.1)
        term_content = VGroup(
            Text("sum = 0+1+...+n", font_size=14, color=Colors.LOOP_COLOR),
            Text("目标达成 ✓", font_size=14, color=Colors.BASE_COLOR),
        ).arrange(DOWN, buff=0.05, aligned_edge=LEFT)
        term_group = VGroup(term_verify, term_content).arrange(DOWN, buff=0.1, aligned_edge=LEFT)
        term_group.next_to(maintain_group, DOWN, buff=0.2).align_to(maintain_group, LEFT)
        
        self.play(FadeIn(term_group))
        self.wait(1)
        
        # 动态演示
        self.play(
            FadeOut(verify_title),
            FadeOut(init_group), FadeOut(maintain_group), FadeOut(term_group),
            run_time=0.5
        )
        
        demo_title = Text("动态演示（n=4）：", font_size=18, color=Colors.SECONDARY)
        demo_title.next_to(code_block, DOWN, buff=0.4).align_to(code_block, LEFT)
        
        self.play(FadeIn(demo_title))
        
        # 变量状态表
        header = VGroup(
            Text("i", font_size=14, color=Colors.CODE_COLOR),
            Text("sum", font_size=14, color=Colors.CODE_COLOR),
            Text("不变量", font_size=14, color=Colors.INVARIANT_COLOR),
        ).arrange(RIGHT, buff=0.8)
        header.next_to(demo_title, DOWN, buff=0.2)
        
        self.play(FadeIn(header))
        
        states = [
            ("初始", "0", "0 = 空和 ✓"),
            ("1", "1", "1 = 0+1 ✓"),
            ("2", "3", "3 = 0+1+2 ✓"),
            ("3", "6", "6 = 0+1+2+3 ✓"),
            ("4", "10", "10 = 0+1+2+3+4 ✓"),
        ]
        
        prev_row = None
        for i, (idx, sum_val, inv) in enumerate(states):
            row = VGroup(
                Text(idx, font_size=14, color=Colors.TEXT),
                Text(sum_val, font_size=14, color=Colors.LOOP_COLOR),
                Text(inv, font_size=14, color=Colors.BASE_COLOR),
            ).arrange(RIGHT, buff=0.6)
            row.next_to(header if prev_row is None else prev_row, DOWN, buff=0.1)
            row.align_to(header, LEFT)
            
            self.play(FadeIn(row), run_time=0.4)
            prev_row = row
        
        self.wait(2)
        
        self.play(
            FadeOut(section_title), FadeOut(code_block),
            FadeOut(invariant_title), FadeOut(invariant_fixed), FadeOut(invariant_box),
            FadeOut(demo_title), FadeOut(header),
            *[FadeOut(m) for m in self.mobjects if m != self.chapter_title],
            run_time=0.5
        )


if __name__ == "__main__":
    # 渲染命令: manim -pqh scene_05_loop_invariant.py LoopInvariant
    pass
