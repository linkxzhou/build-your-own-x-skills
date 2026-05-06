"""
Scene 2: 进制转换 - 数字的多种语言
解释十进制、二进制、十六进制的原理与转换
"""

from manim import *


# 配色方案
class Colors:
    PRIMARY = "#00D4FF"      # 科技蓝
    SECONDARY = "#FF6B6B"    # 警示红
    ACCENT = "#4ECDC4"       # 青绿
    BG = "#1a1a2e"           # 深蓝黑
    TEXT = "#FFFFFF"         # 白色
    GRAY = "#888888"         # 灰色
    BINARY_0 = "#2C3E50"     # 0的颜色
    BINARY_1 = "#F39C12"     # 1的颜色
    HIGHLIGHT = "#9B59B6"    # 紫色高亮


def create_chapter_title(text, font_size=32):
    """创建章节标题"""
    title = Text(text, font_size=font_size, color=Colors.PRIMARY)
    return title


def create_digit_box(digit, color=Colors.PRIMARY, size=0.7):
    """创建一个数字方框"""
    box = Square(side_length=size)
    box.set_stroke(color, width=2)
    box.set_fill(color, opacity=0.2)
    
    text = Text(str(digit), font_size=int(size * 35), color=Colors.TEXT)
    text.move_to(box.get_center())
    
    return VGroup(box, text)


def create_power_label(base, power, font_size=18):
    """创建幂次标签"""
    return MathTex(f"{base}^{{{power}}}", font_size=font_size, color=Colors.GRAY)


def clear_scene(scene):
    """清理场景中所有元素"""
    if len(scene.mobjects) > 0:
        scene.play(*[FadeOut(m) for m in scene.mobjects], run_time=0.5)
    scene.wait(0.1)


class Scene02NumberSystems(Scene):
    """Scene 2: 进制转换"""
    
    CHAPTER_TITLE = "第一章：计算机与数字"
    
    def construct(self):
        self.camera.background_color = Colors.BG
        
        # 创建共享的章节标题
        self.chapter_title = create_chapter_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.5)
        self.add(self.chapter_title)
        
        self.section_decimal_intro()
        self.section_binary_conversion()
        self.section_hexadecimal()
        self.section_comparison()
        
        clear_scene(self)
    
    def section_decimal_intro(self):
        """十进制介绍"""
        # 小节标题
        section_title = Text("十进制 - 我们熟悉的语言", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 展示数字 1234
        example_num = Text("1234", font_size=48, color=Colors.PRIMARY)
        example_num.next_to(section_title, DOWN, buff=0.6).set_x(0)
        
        self.play(Write(example_num))
        self.wait(0.5)
        
        # 拆解每一位
        digits = ["1", "2", "3", "4"]
        digit_boxes = VGroup()
        for d in digits:
            box = create_digit_box(d, color=Colors.PRIMARY)
            digit_boxes.add(box)
        digit_boxes.arrange(RIGHT, buff=0.3)
        digit_boxes.next_to(example_num, DOWN, buff=0.5).set_x(0)
        
        self.play(
            FadeOut(example_num),
            LaggedStart(
                *[FadeIn(db, scale=0.8) for db in digit_boxes],
                lag_ratio=0.15
            ),
            run_time=1
        )
        
        # 添加位权标签
        powers = [3, 2, 1, 0]
        power_labels = VGroup()
        for i, p in enumerate(powers):
            label = create_power_label(10, p)
            label.next_to(digit_boxes[i], UP, buff=0.2)
            power_labels.add(label)
        
        self.play(
            LaggedStart(
                *[FadeIn(pl, shift=DOWN * 0.2) for pl in power_labels],
                lag_ratio=0.1
            ),
            run_time=0.8
        )
        self.wait(0.5)
        
        # 展示计算公式
        calc_parts = VGroup(
            MathTex(r"1 \times 10^3", font_size=24, color=Colors.TEXT),
            MathTex(r"+ 2 \times 10^2", font_size=24, color=Colors.TEXT),
            MathTex(r"+ 3 \times 10^1", font_size=24, color=Colors.TEXT),
            MathTex(r"+ 4 \times 10^0", font_size=24, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.2)
        calc_parts.next_to(digit_boxes, DOWN, buff=0.6).set_x(0)
        
        self.play(Write(calc_parts), run_time=1)
        self.wait(0.5)
        
        # 计算结果
        result_parts = VGroup(
            MathTex(r"= 1000", font_size=24, color=Colors.ACCENT),
            MathTex(r"+ 200", font_size=24, color=Colors.ACCENT),
            MathTex(r"+ 30", font_size=24, color=Colors.ACCENT),
            MathTex(r"+ 4", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.2)
        result_parts.next_to(calc_parts, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(result_parts, shift=UP * 0.2))
        self.wait(0.3)
        
        # 最终结果
        final = MathTex(r"= 1234", font_size=32, color=Colors.PRIMARY)
        final.next_to(result_parts, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(final))
        self.wait(0.5)
        
        # 关键点
        key_point = Text("关键: 满十进一", font_size=22, color=Colors.GRAY)
        key_point.next_to(final, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(key_point))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(digit_boxes),
            FadeOut(power_labels),
            FadeOut(calc_parts),
            FadeOut(result_parts),
            FadeOut(final),
            FadeOut(key_point),
            run_time=0.5
        )
    
    def section_binary_conversion(self):
        """二进制转换详解"""
        # 小节标题
        section_title = Text("二进制 - 计算机的语言", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 核心概念
        concept = VGroup(
            Text("只用 0 和 1", font_size=24, color=Colors.ACCENT),
            Text("满二进一", font_size=24, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=1)
        concept.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(concept))
        self.wait(0.5)
        
        # 例子: 1011₂
        example_title = VGroup(
            Text("例: ", font_size=24, color=Colors.TEXT),
            MathTex(r"1011_2", font_size=28, color=Colors.PRIMARY),
            Text(" 等于多少?", font_size=24, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(concept, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_title))
        self.wait(0.5)
        
        # 创建数字方框
        digits = ["1", "0", "1", "1"]
        digit_boxes = VGroup()
        for d in digits:
            color = Colors.BINARY_1 if d == "1" else Colors.BINARY_0
            box = create_digit_box(d, color=color)
            digit_boxes.add(box)
        digit_boxes.arrange(RIGHT, buff=0.3)
        digit_boxes.next_to(example_title, DOWN, buff=0.5).set_x(0)
        
        self.play(
            LaggedStart(
                *[FadeIn(db, scale=0.8) for db in digit_boxes],
                lag_ratio=0.15
            ),
            run_time=0.8
        )
        
        # 添加位权标签
        powers = [3, 2, 1, 0]
        power_labels = VGroup()
        for i, p in enumerate(powers):
            label = create_power_label(2, p)
            label.next_to(digit_boxes[i], UP, buff=0.2)
            power_labels.add(label)
        
        self.play(
            LaggedStart(
                *[FadeIn(pl, shift=DOWN * 0.2) for pl in power_labels],
                lag_ratio=0.1
            ),
            run_time=0.6
        )
        self.wait(0.5)
        
        # 逐步计算
        calc_steps = VGroup(
            MathTex(r"1 \times 2^3", font_size=22, color=Colors.TEXT),
            MathTex(r"+ 0 \times 2^2", font_size=22, color=Colors.GRAY),
            MathTex(r"+ 1 \times 2^1", font_size=22, color=Colors.TEXT),
            MathTex(r"+ 1 \times 2^0", font_size=22, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.15)
        calc_steps.next_to(digit_boxes, DOWN, buff=0.5).set_x(0)
        
        self.play(Write(calc_steps), run_time=1)
        self.wait(0.3)
        
        # 计算结果
        result_steps = VGroup(
            MathTex(r"= 8", font_size=22, color=Colors.ACCENT),
            MathTex(r"+ 0", font_size=22, color=Colors.GRAY),
            MathTex(r"+ 2", font_size=22, color=Colors.ACCENT),
            MathTex(r"+ 1", font_size=22, color=Colors.ACCENT),
        ).arrange(RIGHT, buff=0.15)
        result_steps.next_to(calc_steps, DOWN, buff=0.25).set_x(0)
        
        self.play(FadeIn(result_steps, shift=UP * 0.2))
        self.wait(0.3)
        
        # 最终结果
        final = MathTex(r"= 11", font_size=36, color=Colors.PRIMARY)
        final.next_to(result_steps, DOWN, buff=0.25).set_x(0)
        
        self.play(Write(final))
        
        # 高亮结果
        box_around = SurroundingRectangle(final, color=Colors.ACCENT, buff=0.15)
        self.play(Create(box_around))
        self.wait(1.5)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(concept),
            FadeOut(example_title),
            FadeOut(digit_boxes),
            FadeOut(power_labels),
            FadeOut(calc_steps),
            FadeOut(result_steps),
            FadeOut(final),
            FadeOut(box_around),
            run_time=0.5
        )
    
    def section_hexadecimal(self):
        """十六进制介绍"""
        # 小节标题
        section_title = Text("十六进制 - 程序员的缩写", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 字符映射表
        mapping_title = Text("使用 0-9 和 A-F (共16个符号)", font_size=22, color=Colors.GRAY)
        mapping_title.next_to(section_title, DOWN, buff=0.4).set_x(0)
        
        self.play(FadeIn(mapping_title))
        
        # 创建映射表
        hex_chars = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
        dec_vals = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"]
        
        # 显示部分映射（A-F）
        special_mapping = VGroup()
        for i in range(10, 16):
            item = VGroup(
                Text(hex_chars[i], font_size=22, color=Colors.PRIMARY),
                Text(" = ", font_size=18, color=Colors.GRAY),
                Text(dec_vals[i], font_size=22, color=Colors.ACCENT),
            ).arrange(RIGHT, buff=0.1)
            special_mapping.add(item)
        
        special_mapping.arrange_in_grid(rows=2, cols=3, buff=(0.5, 0.2))
        special_mapping.next_to(mapping_title, DOWN, buff=0.4).set_x(0)
        
        self.play(
            LaggedStart(
                *[FadeIn(m, scale=0.9) for m in special_mapping],
                lag_ratio=0.1
            ),
            run_time=1
        )
        self.wait(0.8)
        
        # 例子: A3₁₆
        example_title = VGroup(
            Text("例: ", font_size=24, color=Colors.TEXT),
            MathTex(r"A3_{16}", font_size=28, color=Colors.PRIMARY),
            Text(" 转十进制", font_size=24, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.1)
        example_title.next_to(special_mapping, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(example_title))
        self.wait(0.5)
        
        # 计算过程
        calc = VGroup(
            MathTex(r"A \times 16^1 + 3 \times 16^0", font_size=24, color=Colors.TEXT),
        )
        calc.next_to(example_title, DOWN, buff=0.3).set_x(0)
        
        self.play(Write(calc))
        self.wait(0.3)
        
        # 替换A为10
        calc2 = VGroup(
            MathTex(r"= 10 \times 16 + 3 \times 1", font_size=24, color=Colors.ACCENT),
        )
        calc2.next_to(calc, DOWN, buff=0.2).set_x(0)
        
        self.play(FadeIn(calc2))
        self.wait(0.3)
        
        # 结果
        calc3 = VGroup(
            MathTex(r"= 160 + 3 = 163", font_size=28, color=Colors.PRIMARY),
        )
        calc3.next_to(calc2, DOWN, buff=0.2).set_x(0)
        
        self.play(Write(calc3))
        
        # 高亮
        box = SurroundingRectangle(calc3, color=Colors.ACCENT, buff=0.1)
        self.play(Create(box))
        self.wait(1)
        
        # 清除
        self.play(
            FadeOut(section_title),
            FadeOut(mapping_title),
            FadeOut(special_mapping),
            FadeOut(example_title),
            FadeOut(calc),
            FadeOut(calc2),
            FadeOut(calc3),
            FadeOut(box),
            run_time=0.5
        )
    
    def section_comparison(self):
        """进制对照表"""
        # 小节标题
        section_title = Text("同一个数, 不同的表达", font_size=26, color=Colors.TEXT)
        section_title.next_to(self.chapter_title, DOWN, buff=0.6).set_x(0)
        
        self.play(FadeIn(section_title, shift=DOWN * 0.2))
        self.wait(0.5)
        
        # 类比
        analogy = Text(
            "就像 '15个苹果' 可以说成 'fifteen' 或 'XV'",
            font_size=20,
            color=Colors.GRAY
        )
        analogy.next_to(section_title, DOWN, buff=0.3).set_x(0)
        
        self.play(FadeIn(analogy))
        self.wait(0.5)
        
        # 对照表数据
        data = [
            ("十进制", "二进制", "十六进制"),
            ("0", "0000", "0"),
            ("5", "0101", "5"),
            ("10", "1010", "A"),
            ("15", "1111", "F"),
            ("255", "11111111", "FF"),
        ]
        
        # 创建表格
        table_group = VGroup()
        
        # 表头
        header = VGroup()
        for i, h in enumerate(data[0]):
            cell = VGroup(
                Rectangle(width=2.2, height=0.5, stroke_color=Colors.PRIMARY, fill_opacity=0.2, fill_color=Colors.PRIMARY),
                Text(h, font_size=18, color=Colors.PRIMARY)
            )
            cell[1].move_to(cell[0].get_center())
            header.add(cell)
        header.arrange(RIGHT, buff=0.1)
        table_group.add(header)
        
        # 数据行
        for row_data in data[1:]:
            row = VGroup()
            for j, val in enumerate(row_data):
                cell = VGroup(
                    Rectangle(width=2.2, height=0.45, stroke_color=Colors.GRAY, stroke_width=1),
                    Text(val, font_size=16, color=Colors.TEXT)
                )
                cell[1].move_to(cell[0].get_center())
                row.add(cell)
            row.arrange(RIGHT, buff=0.1)
            table_group.add(row)
        
        table_group.arrange(DOWN, buff=0.05)
        table_group.next_to(analogy, DOWN, buff=0.5).set_x(0)
        
        # 动画显示表格
        self.play(FadeIn(header), run_time=0.5)
        for row in table_group[1:]:
            self.play(FadeIn(row, shift=UP * 0.1), run_time=0.3)
        
        self.wait(1)
        
        # 关键总结
        summary = VGroup(
            Text("关键理解:", font_size=22, color=Colors.ACCENT),
            Text("数值本身不变, 只是表示方式不同", font_size=20, color=Colors.TEXT),
        ).arrange(RIGHT, buff=0.3)
        summary.next_to(table_group, DOWN, buff=0.5).set_x(0)
        
        self.play(FadeIn(summary, shift=UP * 0.2))
        self.wait(2)


if __name__ == "__main__":
    # 渲染命令: manim -pql scene_02_number_systems.py Scene02NumberSystems
    pass
