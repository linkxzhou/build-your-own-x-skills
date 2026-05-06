import json
from pathlib import Path
from collections import defaultdict

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
SKILLS = ROOT / 'skills'
EXAMPLES = ROOT / 'examples'
MANIFEST = SKILLS / 'x-skills-manifest.json'

manifest = json.loads(MANIFEST.read_text(encoding='utf-8'))
items = manifest['created']

by_cat = defaultdict(list)
for item in items:
    by_cat[item['category_slug']].append(item)

def safe_text(s):
    return s.replace('|', '\\|')

def example_readme(item):
    skill = item['name']
    title = item['title']
    lang = item['language']
    category = item['category']
    url = item['url']
    return f'''# {title}

> Example for skill: `{skill}`

## 场景

你想通过 Claude Code 学习并逐步实现 **{title}**，而不是一次性拿到完整答案。

## 推荐 Prompt

```text
[使用Skills: {skill}]
我想用 {lang} 从零实现「{title}」。
请先检查当前目录是否为空，然后给我一个 4-8 个里程碑的学习计划。
从第一个最小可运行版本开始，只实现第一阶段，并提供验证命令。
```

## 预期交互

1. skill 先确认项目状态、语言栈和运行环境。
2. 输出阶段化路线图，而不是直接生成完整最终项目。
3. 创建最小项目骨架或指出需要的文件结构。
4. 实现第一阶段的最小功能。
5. 运行或给出验证命令。
6. 如果失败，解释失败原因并给出最小修复。

## 学习目标

- 理解 `{category}` 项目的核心模型和关键约束。
- 能独立运行第一阶段的最小版本。
- 通过测试或可观察输出验证每个里程碑。
- 在后续阶段逐步扩展，而不是复制粘贴完整实现。

## 原始资源

- 技术栈：`{lang}`
- 链接：{url}

## 适合测试的变体 Prompt

```text
[使用Skills: {skill}]
我已经按照「{title}」做到一半，但测试失败了。请先阅读项目文件，定位当前处于哪个里程碑，再做最小修复并解释原因。
```

```text
[使用Skills: {skill}]
请基于这个教程资源：{url}
把它整理成 Claude Code 可执行的学习任务清单，每个任务都要有交付物和验收命令。
```
'''

def category_readme(cat_slug, cat_items):
    cat_name = cat_items[0]['category'] if cat_items else cat_slug
    lines = [
        f'# {cat_name} examples',
        '',
        f'本目录收集 `{cat_name}` 大类型下的 skill 使用示例。',
        '',
        '## 使用方式',
        '',
        '进入任一子目录，复制 `README.md` 中的推荐 Prompt 到支持 skills 的 AI 编程工具中执行。',
        '',
        '## 示例列表',
        '',
        '| Skill | 技术栈 | 原始项目 |',
        '|---|---|---|',
    ]
    for item in sorted(cat_items, key=lambda x: x['name']):
        lines.append(f"| [`{item['name']}`](./{item['name']}/) | {safe_text(item['language'])} | {safe_text(item['title'])} |")
    lines.append('')
    return '\n'.join(lines)

def root_readme(by_cat):
    lines = [
        '# build-your-own-x skill examples',
        '',
        '本目录按大类型组织每个 skill 的使用示例。结构类似 `examples/manim/`：先按主题分类，再进入具体示例目录。',
        '',
        '## 分类索引',
        '',
        '| 分类 | 示例数 |',
        '|---|---:|',
    ]
    for cat_slug in sorted(by_cat):
        cat_name = by_cat[cat_slug][0]['category']
        lines.append(f'| [{cat_name}](./{cat_slug}/) | {len(by_cat[cat_slug])} |')
    lines.append('')
    return '\n'.join(lines)

created = []
for cat_slug, cat_items in by_cat.items():
    cat_dir = EXAMPLES / cat_slug
    cat_dir.mkdir(parents=True, exist_ok=True)
    (cat_dir / 'README.md').write_text(category_readme(cat_slug, cat_items), encoding='utf-8')
    for item in cat_items:
        d = cat_dir / item['name']
        d.mkdir(parents=True, exist_ok=True)
        (d / 'README.md').write_text(example_readme(item), encoding='utf-8')
        created.append(str(d.relative_to(EXAMPLES)))

(EXAMPLES / 'README.md').write_text(root_readme(by_cat), encoding='utf-8')

summary = {
    'category_count': len(by_cat),
    'example_count': len(created),
    'examples': created,
}
(EXAMPLES / 'examples-manifest.json').write_text(json.dumps(summary, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'category_count': len(by_cat), 'example_count': len(created), 'manifest': str(EXAMPLES / 'examples-manifest.json')}, ensure_ascii=False, indent=2))
