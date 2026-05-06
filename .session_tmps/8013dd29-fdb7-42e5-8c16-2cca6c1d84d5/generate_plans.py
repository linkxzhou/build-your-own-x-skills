import re
import os
import json
from pathlib import Path

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
README = ROOT / 'README.md'
PLAN_DIR = ROOT / 'plan'

text = README.read_text(encoding='utf-8')
lines = text.splitlines()

categories = []
current = None
entry_re = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?:\*\*)?(?P<lang>.*?)(?:\*\*)?: _(?P<title>.*?)_\]\((?P<url>.*?)\)(?P<suffix>.*)$')
entry_re_plain = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?P<title>.*?)\]\((?P<url>.*?)\)(?P<suffix>.*)$')
cat_re = re.compile(r'^#### 构建你自己的 `(?P<name>.+?)`')
uncat_re = re.compile(r'^#### 未分类')

def slugify(s):
    mapping = {
        '3D 渲染器': '3d-renderer',
        '增强现实（AR）': 'augmented-reality',
        'BitTorrent 客户端': 'bittorrent-client',
        '区块链 / 加密货币': 'blockchain-cryptocurrency',
        '机器人（Bot）': 'bot',
        '命令行工具': 'command-line-tool',
        '数据库': 'database',
        'Docker': 'docker',
        '模拟器 / 虚拟机': 'emulator-virtual-machine',
        '前端框架 / 库': 'frontend-framework-library',
        '游戏': 'game',
        'Git': 'git',
        '网络协议栈': 'network-stack',
        '神经网络': 'neural-network',
        '操作系统': 'operating-system',
        '物理引擎': 'physics-engine',
        '编程语言': 'programming-language',
        '正则表达式引擎': 'regex-engine',
        '搜索引擎': 'search-engine',
        'Shell': 'shell',
        '模板引擎': 'template-engine',
        '文本编辑器': 'text-editor',
        '视觉识别系统': 'visual-recognition-system',
        '体素引擎（Voxel Engine）': 'voxel-engine',
        '网页浏览器': 'web-browser',
        'Web 服务器': 'web-server',
        '未分类': 'misc',
    }
    if s in mapping:
        return mapping[s]
    out = re.sub(r'[^a-zA-Z0-9]+', '-', s.lower()).strip('-')
    return out or 'misc'

def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

for line in lines:
    m = cat_re.match(line)
    if m:
        current = {'name': m.group('name'), 'slug': slugify(m.group('name')), 'items': []}
        categories.append(current)
        continue
    if uncat_re.match(line):
        current = {'name': '未分类', 'slug': 'misc', 'items': []}
        categories.append(current)
        continue
    if current and line.startswith('- ['):
        m = entry_re.match(line)
        if m:
            current['items'].append({
                'done': m.group('done').strip().upper() == 'X',
                'language': clean(m.group('lang').replace('**', '')),
                'title': clean(m.group('title')),
                'url': m.group('url'),
                'media': '[video]' in m.group('suffix') or '[pdf]' in m.group('suffix'),
                'suffix': clean(m.group('suffix')),
            })
            continue
        m = entry_re_plain.match(line)
        if m:
            title = clean(m.group('title'))
            current['items'].append({
                'done': m.group('done').strip().upper() == 'X',
                'language': '(any)' if title.startswith('从 NAND') or 'vibe-coding' in title else 'General',
                'title': title,
                'url': m.group('url'),
                'media': '[video]' in m.group('suffix') or '[pdf]' in m.group('suffix'),
                'suffix': clean(m.group('suffix')),
            })

PLAN_DIR.mkdir(exist_ok=True)

total = sum(len(c['items']) for c in categories)

index_lines = [
    '# build-your-own-x skills 转换计划索引',
    '',
    '本目录用于把 `codecrafters-io/build-your-own-x` 中的项目逐步转换为 Claude Code 可使用的 skills。',
    '',
    '## 总体转换原则',
    '',
    '- 每个原始项目优先转换为一个独立 skill；同一主题下高度相似的多语言教程可在后续合并为一个多语言 skill。',
    '- 每个 skill 至少包含 `SKILL.md`、`references/`、`examples/`、`evals/` 四类规划。',
    '- `SKILL.md` 负责触发条件、学习路径、实现步骤、验证方式；长教程内容放入 `references/` 渐进式加载。',
    '- 视频/PDF/外部长文需先整理为结构化学习大纲，再抽取可执行里程碑与测试任务。',
    '- 每个 skill 都应提供最小可运行项目、阶段性练习、验收测试和常见故障处理。',
    '',
    f'## 统计',
    '',
    f'- 分类数：{len(categories)}',
    f'- 原始项目条目数：{total}',
    '',
    '## 分类计划文件',
    '',
]

for c in categories:
    fn = f"{c['slug']}.md"
    index_lines.append(f"- [{c['name']}](./{fn})：{len(c['items'])} 个项目")

(PLAN_DIR / 'README.md').write_text('\n'.join(index_lines) + '\n', encoding='utf-8')

def plan_for_item(category, item, idx):
    raw_name = item['title']
    skill_base = f"build-your-own-{category['slug']}"
    if len(category['items']) > 1:
        suffix = re.sub(r'[^a-zA-Z0-9]+', '-', raw_name.lower()).strip('-')[:48].strip('-')
        if suffix:
            skill_base = f"{skill_base}-{suffix}"
    lines = []
    lines.append(f"### {idx}. {raw_name}")
    lines.append('')
    lines.append(f"- **原始语言/技术栈**：{item['language']}")
    lines.append(f"- **原始资源**：{item['url']}")
    lines.append(f"- **建议 skill 名称**：`{skill_base}`")
    lines.append(f"- **触发场景**：用户想从零实现、学习、调试或扩展 `{category['name']}` 相关项目，尤其提到“build your own {category['slug']}”、`{raw_name}`、`{item['language']}` 实现时。")
    lines.append('- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。')
    lines.append('- **SKILL.md 规划**：')
    lines.append('  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。')
    lines.append('  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。')
    lines.append('  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。')
    lines.append('  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。')
    lines.append('- **附带资源规划**：')
    lines.append('  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。')
    lines.append('  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。')
    lines.append('  - `examples/minimal/`：最小可运行示例或项目骨架。')
    lines.append('  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。')
    lines.append('- **验收标准**：')
    lines.append('  - 用户能在空目录生成项目骨架并通过第一阶段测试。')
    lines.append('  - 每个里程碑都有可运行命令或可观察输出。')
    lines.append('  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。')
    if item['media']:
        lines.append('- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。')
    if item['done']:
        lines.append('- **当前状态**：README 中已标记完成，优先复用现有 `skills/` 目录中的实现经验。')
    lines.append('')
    return '\n'.join(lines)

for c in categories:
    lines = [
        f"# 构建你自己的 {c['name']}：skill 转换计划",
        '',
        f"- **分类 slug**：`{c['slug']}`",
        f"- **项目数量**：{len(c['items'])}",
        '- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）',
        '',
        '## 分类级转换策略',
        '',
        f"将 `{c['name']}` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。",
        '',
        '## 项目计划',
        '',
    ]
    for i, item in enumerate(c['items'], 1):
        lines.append(plan_for_item(c, item, i))
    (PLAN_DIR / f"{c['slug']}.md").write_text('\n'.join(lines), encoding='utf-8')

manifest = {'category_count': len(categories), 'project_count': total, 'categories': [{'name': c['name'], 'slug': c['slug'], 'count': len(c['items'])} for c in categories]}
(PLAN_DIR / 'manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(manifest, ensure_ascii=False, indent=2))
