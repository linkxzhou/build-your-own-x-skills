import re
import json
import hashlib
from pathlib import Path

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
README = ROOT / 'README.md'
SKILLS_DIR = ROOT / 'skills'
MANIFEST = ROOT / 'plan' / 'manifest.json'

text = README.read_text(encoding='utf-8')
lines = text.splitlines()

cat_map = {
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

keyword_map = {
    'redis': 'redis', 'nosql': 'nosql', 'sql': 'sql', 'b+tree': 'btree', 'bencode': 'bencode',
    'react': 'react', 'redux': 'redux', 'angular': 'angular', 'virtual dom': 'virtual-dom',
    'chip-8': 'chip8', 'game boy': 'gameboy', 'nes': 'nes', 'lisp': 'lisp', 'scheme': 'scheme',
    'compiler': 'compiler', '解释器': 'interpreter', '编译器': 'compiler', '内核': 'kernel',
    'bootloader': 'bootloader', 'shell': 'shell', 'web server': 'web-server', 'http': 'http',
    'git': 'git', 'docker': 'docker', 'blockchain': 'blockchain', '区块链': 'blockchain',
    'ray tracing': 'ray-tracing', '光线追踪': 'ray-tracing', 'regex': 'regex', '正则': 'regex',
    '搜索': 'search', 'neural': 'neural-network', '神经网络': 'neural-network', '操作系统': 'os',
    '文本编辑器': 'text-editor', 'bittorrent': 'bittorrent', 'bot': 'bot', '机器人': 'bot',
    '浏览器': 'browser', 'browser': 'browser', '模板': 'template', 'template': 'template',
}

cat_re = re.compile(r'^#### 构建你自己的 `(?P<name>.+?)`')
uncat_re = re.compile(r'^#### 未分类')
entry_re = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?:\*\*)?(?P<lang>.*?)(?:\*\*)?: _(?P<title>.*?)_\]\((?P<url>.*?)\)(?P<suffix>.*)$')
entry_re_plain = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?P<title>.*?)\]\((?P<url>.*?)\)(?P<suffix>.*)$')

def clean(s):
    return re.sub(r'\s+', ' ', s).strip()

def ascii_slug(s):
    s = s.lower()
    s = s.replace('c++', 'cpp').replace('c#', 'csharp').replace('node.js', 'nodejs').replace('javascript', 'javascript')
    out = re.sub(r'[^a-z0-9]+', '-', s).strip('-')
    return out

def keyword_slug(title, fallback='project'):
    lower = title.lower()
    hits = []
    for k, v in keyword_map.items():
        if k.lower() in lower and v not in hits:
            hits.append(v)
    if hits:
        return '-'.join(hits[:3])
    ascii_part = ascii_slug(title)
    if ascii_part:
        return '-'.join(ascii_part.split('-')[:6])
    digest = hashlib.sha1(title.encode('utf-8')).hexdigest()[:8]
    return f'{fallback}-{digest}'

def lang_slug(lang):
    return ascii_slug(lang.replace('(any)', 'any').replace('/', ' ')) or 'any'

items = []
current = None
for line in lines:
    m = cat_re.match(line)
    if m:
        name = m.group('name')
        current = {'name': name, 'slug': cat_map.get(name, keyword_slug(name, 'category'))}
        continue
    if uncat_re.match(line):
        current = {'name': '未分类', 'slug': 'misc'}
        continue
    if current and line.startswith('- ['):
        m = entry_re.match(line)
        if m:
            items.append({
                'category': current['name'], 'category_slug': current['slug'],
                'done': m.group('done').strip().upper() == 'X',
                'language': clean(m.group('lang').replace('**', '')),
                'title': clean(m.group('title')),
                'url': m.group('url'),
                'suffix': clean(m.group('suffix')),
            })
            continue
        m = entry_re_plain.match(line)
        if m:
            title = clean(m.group('title'))
            items.append({
                'category': current['name'], 'category_slug': current['slug'],
                'done': m.group('done').strip().upper() == 'X',
                'language': '(any)' if title.startswith('从 NAND') or 'vibe-coding' in title else 'General',
                'title': title,
                'url': m.group('url'),
                'suffix': clean(m.group('suffix')),
            })

existing = {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}
used = set(existing)
created = []
skipped = []

def unique_name(item):
    base = f"build-your-own-{item['category_slug']}-{keyword_slug(item['title'], item['category_slug'])}"
    base = base[:80].strip('-')
    candidates = [base, f"{base}-{lang_slug(item['language'])}"[:90].strip('-')]
    digest = hashlib.sha1((item['title'] + item['url']).encode('utf-8')).hexdigest()[:8]
    candidates.append(f"{base}-{digest}"[:100].strip('-'))
    for c in candidates:
        if c not in used:
            return c
    i = 2
    while True:
        c = f"{base}-{digest}-{i}"
        if c not in used:
            return c
        i += 1

def yaml_quote(s):
    return s.replace('"', '\\"')

def skill_md(name, item):
    media_note = '  This source is marked as video/PDF-like material; first create a structured outline before coding.\n' if '[video]' in item['suffix'] or '[pdf]' in item['suffix'] else ''
    return f'''---
name: {name}
description: |
  Trigger when the user wants to learn, implement, debug, or extend a build-your-own project for {item['category']} using {item['language']}. Use when they mention "build your own {item['category_slug']}", "{yaml_quote(item['title'])}", the source URL, or ask for a Claude Code guided implementation plan.

  Guides the user through a project-based learning workflow: inspect prerequisites, create or adapt a minimal project, implement milestones, run verification commands, and debug failures without simply dumping a full finished solution.
---

# {item['title']}

Use this skill as a Claude Code project coach for converting the original build-your-own tutorial into an interactive implementation experience.

## Source

- **Category**: {item['category']}
- **Language / stack**: {item['language']}
- **Original resource**: {item['url']}
- **Original status**: {'already marked complete in README' if item['done'] else 'not yet converted in README'}

## Operating principles

- Prefer learning-by-building: explain the next small concept, then make the smallest useful code change.
- Preserve the user's existing project structure. Inspect files before editing and avoid replacing working code wholesale.
- Use tests, executable examples, or observable outputs at every milestone.
- If the user asks for a full implementation, first offer a staged path and provide complete code only for the current milestone.
- For long tutorials, load only the relevant reference section for the current milestone.
{media_note}
## Workflow

### 1. Establish context

1. Identify whether the user is starting from an empty directory, continuing a partial implementation, or debugging a failing project.
2. Detect the target language/toolchain. Default to **{item['language']}** when the user does not specify another stack.
3. Check available build tools and create a minimal runnable project only when needed.
4. Read `references/tutorial-map.md` for the milestone map before planning detailed work.

### 2. Plan milestones

Guide the project through these generic milestones and adapt them to the tutorial:

1. **Project skeleton** — files, build command, first runnable program.
2. **Core data model** — key structs/classes/types and invariants.
3. **Parser or input layer** — commands, file formats, protocol frames, or scene/input handling.
4. **Core algorithm / engine** — the central behavior of the project.
5. **Persistence / networking / rendering / runtime integration** — domain-specific integration.
6. **Testing and diagnostics** — unit tests, golden outputs, fixtures, or manual verification.
7. **Extensions** — performance, robustness, UX, and production-readiness improvements.

### 3. Implement with guardrails

- Before edits, summarize the intended change and files affected.
- Keep patches small enough for the user to understand.
- Explain important design choices and tradeoffs at the point they matter.
- After each edit, run the relevant verification command when available.
- When a command fails, diagnose from the error message and fix the smallest likely cause.

### 4. Debugging mode

When the user provides failing tests, logs, or code:

1. Reproduce or reason about the failure.
2. Identify the milestone and concept involved.
3. Explain the invariant being violated.
4. Apply a minimal fix.
5. Add or update a regression test if appropriate.

## References

- `references/tutorial-map.md` — source-to-milestone conversion map.
- `references/concepts.md` — core concepts and implementation checklist.
- `examples/minimal/README.md` — minimal project scaffold guidance.
- `evals/evals.json` — prompts for validating this skill.

## Expected outputs

Depending on the user's request, produce one of:

- A staged implementation plan.
- A minimal project scaffold.
- A focused code patch for the current milestone.
- A debugging explanation plus fix.
- A test plan and verification commands.
'''

def tutorial_map(item):
    return f'''# Tutorial map: {item['title']}

## Original resource

- URL: {item['url']}
- Language / stack: {item['language']}
- Category: {item['category']}

## Conversion approach

Map the original tutorial into a Claude Code guided learning flow. If the source is unavailable, too long, or video-based, first ask the user whether to provide notes/transcript or allow web lookup, then build a local outline before implementation.

## Suggested milestone mapping

| Milestone | Goal | Typical deliverable | Verification |
|---|---|---|---|
| 1. Skeleton | Create the smallest runnable project | Build config, entry point, README | Build or run hello-world command |
| 2. Core model | Define domain types and invariants | Structs/classes/types | Unit tests for construction and validation |
| 3. Input layer | Parse user input, files, protocol, or scene data | Parser/loader module | Fixture-based parser tests |
| 4. Core engine | Implement the key algorithm or runtime behavior | Engine/interpreter/server/render loop | Golden output or behavior tests |
| 5. Integration | Connect I/O, storage, networking, rendering, or UI | End-to-end command/app | Manual demo or integration test |
| 6. Hardening | Improve errors, performance, edge cases | Diagnostics and optimizations | Regression and stress tests |

## Adaptation notes

- Keep the implementation idiomatic for {item['language']}.
- Prefer a small, working vertical slice before adding advanced features.
- Translate prose-heavy tutorial sections into concrete tasks with files and commands.
- Preserve links back to the source when citing concepts or next reading.
'''

def concepts(item):
    return f'''# Concepts checklist: {item['title']}

## Before coding

- Confirm the user's target language and runtime.
- Confirm whether the user wants a learning scaffold, production-quality implementation, or bug fix.
- Inspect existing files if the project is not empty.

## Core concept prompts

Use these questions to guide explanations:

1. What minimal observable behavior proves the project is alive?
2. What are the main domain objects and their invariants?
3. What input format or protocol must be understood?
4. What algorithm, runtime loop, or state transition makes the project useful?
5. What failure modes are common for beginners?
6. What tests can catch regressions without overcomplicating the project?

## Implementation checklist

- [ ] Project builds or runs on the user's machine.
- [ ] First milestone has a visible result.
- [ ] Core data model is documented in code comments or README.
- [ ] At least one automated or scripted verification exists.
- [ ] Debugging guidance explains causes, not only fixes.

## Domain

- Category: {item['category']}
- Language / stack: {item['language']}
- Source: {item['url']}
'''

def minimal_readme(item):
    return f'''# Minimal scaffold guidance

This directory is a placeholder for a future minimal scaffold for **{item['title']}**.

When implementing this skill further, add the smallest runnable project for `{item['language']}` that demonstrates milestone 1.

Suggested contents:

- Build/run instructions.
- One tiny executable entry point.
- One test or verification command.
- Notes about required external dependencies.
'''

def evals_json(name, item):
    return {
        'skill_name': name,
        'evals': [
            {
                'id': 1,
                'prompt': f'我想从零开始用 {item["language"]} 学习并实现「{item["title"]}」，请先帮我规划里程碑并创建最小项目骨架。',
                'expected_output': 'Produces a staged learning plan and minimal scaffold guidance without dumping a full final implementation.',
                'files': []
            },
            {
                'id': 2,
                'prompt': f'我已经做到「{item["title"]}」的一半，但测试失败了。请根据项目文件定位问题，解释原因，并做最小修复。',
                'expected_output': 'Inspects existing files, diagnoses the current milestone, applies a minimal fix, and suggests a regression test.',
                'files': []
            },
            {
                'id': 3,
                'prompt': f'基于 {item["url"]}，把这个教程转换成 Claude Code 可执行的学习任务清单。',
                'expected_output': 'Maps the source tutorial into milestones with deliverables, commands, and verification criteria.',
                'files': []
            }
        ]
    }

for item in items:
    name = unique_name(item)
    used.add(name)
    dest = SKILLS_DIR / name
    if dest.exists():
        skipped.append(name)
        continue
    (dest / 'references').mkdir(parents=True, exist_ok=True)
    (dest / 'examples' / 'minimal').mkdir(parents=True, exist_ok=True)
    (dest / 'evals').mkdir(parents=True, exist_ok=True)
    (dest / 'SKILL.md').write_text(skill_md(name, item), encoding='utf-8')
    (dest / 'references' / 'tutorial-map.md').write_text(tutorial_map(item), encoding='utf-8')
    (dest / 'references' / 'concepts.md').write_text(concepts(item), encoding='utf-8')
    (dest / 'examples' / 'minimal' / 'README.md').write_text(minimal_readme(item), encoding='utf-8')
    (dest / 'evals' / 'evals.json').write_text(json.dumps(evals_json(name, item), ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    created.append({'name': name, **item})

out = {
    'parsed_projects': len(items),
    'created_skills': len(created),
    'skipped': skipped,
    'created': created,
}
(ROOT / 'skills' / 'build-your-own-x-skills-manifest.json').write_text(json.dumps(out, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'parsed_projects': len(items), 'created_skills': len(created), 'skipped_count': len(skipped), 'manifest': str(ROOT / 'skills' / 'build-your-own-x-skills-manifest.json')}, ensure_ascii=False, indent=2))
