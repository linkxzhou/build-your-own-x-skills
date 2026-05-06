---
name: manim-composer
description: |
  Trigger when: (1) The user wants to create an educational/explainer video, (2) The user has a vague concept they want visualized, (3) The user mentions "3b1b style" or "explain like 3Blue1Brown", (4) The user wants to plan a Manim video or animation sequence, (5) The user asks to "compose" or "plan" a math/science visualization.

  Transforms vague video ideas into detailed scene-by-scene plans (scenes.md). Conducts research, asks clarifying questions about audience/scope/focus, and outputs comprehensive scene specifications ready for implementation with ManimCE or ManimGL.

  Use this BEFORE writing any Manim code. This skill plans the video; use manimce-best-practices or manimgl-best-practices for implementation.
---

## Workflow

### Phase 1: Understand the Concept

1. **Research the topic** deeply before asking questions
   - Use web search to understand the core concepts
   - Identify the key insights that make this topic interesting
   - Find the "aha moment" — what makes this click for learners
   - Note common misconceptions to address

2. **Identify the narrative hook**
   - What question does this video answer?
   - Why should the viewer care?
   - What's the surprising or counterintuitive element?

### Phase 2: Clarify with User

Ask targeted questions (not all at once — adapt based on responses):

**Audience & Scope**
- What math/science background should I assume? (e.g., "knows calculus" or "high school algebra")
- Target video length? (short: 5–10min, medium: 15–20min, long: 30min+)
- Should this be self-contained or part of a series?

**Focus & Depth**
- Any specific aspects to emphasize or skip?
- Proof-heavy or intuition-focused?
- Real-world applications to include?

**Style Preferences**
- Color scheme preferences?
- Narration style? (casual, formal, playful)
- Any specific visual metaphors you have in mind?

### Phase 3: Create scenes.md

Output a comprehensive `scenes.md` file with this structure:

```markdown
# [Video Title]

## Overview
- **Topic**: [Core concept]
- **Hook**: [Opening question/mystery]
- **Target Audience**: [Prerequisites]
- **Estimated Length**: [X minutes]
- **Key Insight**: [The "aha moment"]

## Narrative Arc
[5-10 sentences describing the journey from confusion to understanding]

---

## Scene 1: [Scene Name]
**Duration**: ~X seconds
**Purpose**: [What this scene accomplishes; be as detailed as possible]

### Visual Elements
- [List of mobjects needed]
- [Animations to use]
- [Camera movements]

### Content
[Detailed description of what happens, what's shown, what's explained]

### Narration Notes
[Key points to convey, tone, pacing notes]

### Technical Notes
- [Specific Manim classes/methods to use]
- [Any tricky implementations to note]

---

## Scene 2: [Scene Name]
...

---

## Transitions & Flow
[Notes on how scenes connect, recurring visual motifs]

## Color Palette
- Primary: [color] - used for [purpose]
- Secondary: [color] - used for [purpose]
- Accent: [color] - used for [purpose]
- Background: [color]

## Mathematical Content
[List of equations, formulas, or mathematical objects that need to be rendered]

## Implementation Order
[Suggested order for implementing scenes, noting dependencies]
```

## 3b1b Style Principles

Apply these principles when composing scenes:

### Visual Storytelling
- **Show, don't just tell** - Every concept needs a visual representation
- **Progressive revelation** - Build complexity gradually, don't show everything at once
- **Visual continuity** - Transform objects rather than replacing them when possible

### Pacing & Rhythm
- **Pause for insight** - Give viewers time to absorb key moments
- **Vary the pace** - Mix quick sequences with slower explanations
- **End scenes with resolution** - Each scene should feel complete

### Mathematical Beauty
- **Emphasize elegance** - Highlight when math is surprisingly simple or beautiful
- **Connect representations** - Show the same concept multiple ways (algebraic, geometric, intuitive)
- **Embrace abstraction gradually** - Start concrete, then generalize

### Engagement Techniques
- **Pose questions** - Make viewers curious before revealing answers
- **Acknowledge difficulty** - "This might seem confusing at first..."
- **Celebrate insight** - Make the "aha moment" feel earned

## Notes / Pitfalls

### 1) Chinese text & LaTeX

#### 1.1 Do NOT put Chinese in MathTex

LaTeX does not support Chinese characters by default. If you put Chinese inside `MathTex`, it will fail to compile:

```
LaTeX Error: Unicode character 位 (U+4F4D)
ValueError: latex error converting to dvi
```

**Solution**: render Chinese with `Text`, render formulas with `MathTex`, and combine them using `VGroup`:

```python
# ❌ Wrong: MathTex contains Chinese
formula = MathTex(r"8\text{位范围}: [0, 2^8-1] = [0, 255]")
formula = MathTex(r"\text{值} = (-1)^S \times 1.M \times 2^{E-127}")

# ✅ Correct: separate Chinese text and MathTex
formula = VGroup(
    Text("8-bit range: ", font_size=22),
    MathTex(r"[0, 2^8-1] = [0, 255]", font_size=26)
).arrange(RIGHT, buff=0.1)

formula = VGroup(
    Text("Value = ", font_size=24),
    MathTex(r"(-1)^S \times 1.M \times 2^{E-127}", font_size=28)
).arrange(RIGHT, buff=0.1)

# ✅ When the Chinese/annotation is after the formula
result = VGroup(
    MathTex(r"10^{1000} = +\infty", font_size=28),
    Text(" (overflow)", font_size=22)
).arrange(RIGHT, buff=0.1)
```

**Note**: the LaTeX `\text{}` command only supports ASCII characters. Any Chinese/Japanese/Korean Unicode characters will cause compilation to fail.

#### 1.2 Pure English text is OK via `\textrm{}`

If you only need English text (e.g., NaN/Inf), you can use `\textrm{}` inside `MathTex`:

```python
# ✅ English text can use \textrm{}
MathTex(r"\sqrt{-1} = \textrm{NaN}", font_size=28)
MathTex(r"0 / 0 = \textrm{NaN}", font_size=28)
```

#### 1.3 Avoid Chinese quotation marks that conflict with Python strings

Using Chinese double quotes like `“”` (or mixing quote styles) inside Python strings can easily lead to syntax issues.

```python
# ❌ Wrong: quotes conflict
explain = Text(
    "n elements, each has two choices: "in"/"out"",  # SyntaxError!
    font_size=18
)

# ✅ Option 1: use single quotes inside
explain = Text(
    "n elements, each has two choices: 'in/out'",
    font_size=18
)

# ✅ Option 2: escape quotes
explain = Text(
    "n elements, each has two choices: \"in/out\"",
    font_size=18
)

# ✅ Option 3: use single-quoted outer string
explain = Text(
    'n elements, each has two choices: "in/out"',
    font_size=18
)
```

**Best practice**: consistently use ASCII punctuation in code to avoid subtle parsing issues.

### 2) Layout & Positioning

#### 2.1 Keep groups horizontally centered

If your content ends up drifting left/right, `.set_x(0)` can force horizontal centering:

```python
# ❌ Wrong: positioning relative to a left-aligned object drifts everything left
switch_label = Text("Switch", font_size=24).to_edge(LEFT)
bulb_label = Text("Bulb", font_size=24).next_to(switch_label, RIGHT, buff=2)
# The whole group drifts left!

# ✅ Option 1: VGroup + arrange + set_x(0)
labels = VGroup(
    Text("Switch", font_size=24),
    Text("Bulb", font_size=24)
).arrange(RIGHT, buff=2).set_x(0)  # centered as a whole

# ✅ Option 2: center a single element
title = Text("Boolean Algebra", font_size=36)
title.to_edge(UP, buff=0.5).set_x(0)

# ✅ Option 3: center after relative layout
content = VGroup(title, subtitle).arrange(DOWN, buff=0.3)
content.next_to(header, DOWN, buff=0.5).set_x(0)
```

**Common issue**: once you use `.to_edge(LEFT)` or `.align_to(..., LEFT)`, anything positioned relative to that object will also shift left.

#### 2.2 When side-by-side content gets too wide

If multiple items arranged horizontally exceed the frame width, split into sequential reveals:

```python
# ❌ Wrong: three tables side-by-side overflow the screen
and_table = create_table("AND")
or_table = create_table("OR")
not_table = create_table("NOT")
tables = VGroup(and_table, or_table, not_table).arrange(RIGHT, buff=0.5)

# ✅ Correct: show them one by one
and_group = create_operation_display("AND").set_x(0)
self.play(FadeIn(and_group))
self.wait(2)
self.play(FadeOut(and_group), run_time=0.5)

or_group = create_operation_display("OR").set_x(0)
self.play(FadeIn(or_group))
self.wait(2)
self.play(FadeOut(or_group), run_time=0.5)

not_group = create_operation_display("NOT").set_x(0)
self.play(FadeIn(not_group))
self.wait(2)
self.play(FadeOut(not_group), run_time=0.5)
```

**Applies to**:
- multiple truth tables / formulas / charts
- comparisons across multiple concepts
- vertical mobile layouts (9:16) with limited width

#### 2.3 Prefer `next_to()` over absolute `move_to()` offsets

```python
# ❌ Wrong: absolute offsets can cause overlaps when text changes
name_text.move_to(box.get_left() + RIGHT * 0.7)
formula_text.move_to(box.get_center() + RIGHT * 0.5)

# ✅ Correct: relative positioning adapts automatically
name_text.next_to(box.get_left(), RIGHT, buff=0.3)
formula_text.next_to(name_text, RIGHT, buff=0.3)
```

#### 2.4 Timing: position elements inside a VGroup after arranging

```python
# ❌ Wrong: using box position before arrange()
boxes = VGroup()
for data in items:
    box = Rectangle(...)
    text = Text(data)
    text.move_to(box.get_left() + RIGHT * 1)  # box not positioned yet!
    boxes.add(VGroup(box, text))
boxes.arrange(DOWN)  # too late, texts are already misaligned

# ✅ Correct: arrange first, then position internals
boxes = VGroup(*[Rectangle(...) for _ in items])
boxes.arrange(DOWN)

for i, data in enumerate(items):
    box = boxes[i]
    text = Text(data)
    text.next_to(box.get_left(), RIGHT, buff=0.3)
```

#### 2.5 `Text("")` does NOT create spacing

```python
# ❌ Wrong: empty Text won't create spacing
VGroup(
    Text("Title", font_size=20),
    Text("", font_size=8),
    Text("Body", font_size=16),
).arrange(DOWN, buff=0.1)

# ✅ Correct: use buff
VGroup(
    Text("Title", font_size=20),
    Text("Body", font_size=16),
).arrange(DOWN, buff=0.2)
```

#### 2.6 Standard “content inside a box” layout

```python
box = RoundedRectangle(width=7, height=2, ...)
box.next_to(previous, DOWN, buff=0.4)

content = VGroup(
    Text("Title", font_size=20),
    Text("Description", font_size=14),
).arrange(DOWN, buff=0.15)
content.move_to(box.get_center())

# or: use a relative chain
# title.next_to(box.get_top(), DOWN, buff=0.2)
# desc.next_to(title, DOWN, buff=0.15)
```

### 3) Scene Management

#### 3.1 Clear between sections

```python
def clear_scene(self):
    """Call at the end of each section to prevent mobject accumulation."""
    if len(self.mobjects) > 0:
        self.play(*[FadeOut(m) for m in self.mobjects], run_time=0.5)
    self.wait(0.1)
```

#### 3.2 Manage chapter titles centrally to avoid duplicates

If a `Scene` class contains multiple `section_*` methods, creating the same chapter title inside each section can lead to duplicated titles or layout glitches.

```python
# ❌ Wrong: each section creates its own chapter title
class MyScene(Scene):
    def construct(self):
        self.section1()
        self.section2()

    def section1(self):
        title = create_title("Chapter 1: ...")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        # ...
        self.play(FadeOut(title))

    def section2(self):
        title = create_title("Chapter 1: ...")
        title.to_edge(UP, buff=0.8)
        self.add(title)
        # ...

# ✅ Correct: define title text as a class constant, build it once in construct()
class MyScene(Scene):
    CHAPTER_TITLE = "Chapter 1: ..."

    def construct(self):
        self.chapter_title = create_title(self.CHAPTER_TITLE)
        self.chapter_title.to_edge(UP, buff=0.8)

        self.section1()
        self.section2()
        clear_scene(self)

    def section1(self):
        """Intro - write the shared chapter title once."""
        subtitle = Text("Subtitle", font_size=24)
        subtitle.next_to(self.chapter_title, DOWN, buff=0.5)

        self.play(Write(self.chapter_title))
        self.play(FadeIn(subtitle))
        self.wait(1)
        self.play(FadeOut(subtitle))

    def section2(self):
        """Later section - reuse the same chapter title."""
        section_title = Text("Section title", font_size=28)
        section_title.next_to(self.chapter_title, DOWN, buff=0.5)

        self.play(Write(section_title))
        # ...
```

**Key points**:
- Use a class attribute like `CHAPTER_TITLE` to define chapter title text (easy to maintain)
- Create `self.chapter_title` in `construct()` and reuse it across sections
- Only `Write()` the chapter title once; later sections simply reference it
- Call `clear_scene(self)` at the end to clean up

### 4) Vertical mobile format (9:16)

If you target vertical mobile video (`frame_width=9, frame_height=16`), width is limited; pay extra attention to layout.

#### Recommended font sizes

| Element type | Recommended size | Notes |
|---|---:|---|
| Scene title | 32–36 | `title.to_edge(UP, buff=0.6)` |
| Chapter title | 24–28 | secondary titles |
| Body text | 16–20 | main content |
| Captions | 12–14 | gray supportive text |
| Code/formulas | 14–18 | monospace or `MathTex` |

## References

- [references/narrative-patterns.md](references/narrative-patterns.md) - Common 3b1b narrative structures
- [references/visual-techniques.md](references/visual-techniques.md) - Effective visualization patterns
- [references/scene-examples.md](references/scene-examples.md) - Example scenes.md excerpts

## Templates

- [templates/scenes-template.md](templates/scenes-template.md) - Blank scenes.md template
