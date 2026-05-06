import json
import re
from pathlib import Path
from collections import defaultdict, Counter
from urllib.parse import urlparse

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
SKILLS = ROOT / 'skills'
PLAN = ROOT / 'plan'
EXAMPLES = ROOT / 'examples'
README = ROOT / 'README.md'
README_EN = ROOT / 'README_EN.md'
MANIFEST_PATH = SKILLS / 'x-skills-manifest.json'
EXAMPLES_MANIFEST = EXAMPLES / 'examples-manifest.json'
PLAN_MANIFEST = PLAN / 'manifest.json'

cat_map = {
    '3D 渲染器': '3d-renderer', '增强现实（AR）': 'augmented-reality', 'BitTorrent 客户端': 'bittorrent-client',
    '区块链 / 加密货币': 'blockchain-cryptocurrency', '机器人（Bot）': 'bot', '命令行工具': 'command-line-tool',
    '数据库': 'database', 'Docker': 'docker', '模拟器 / 虚拟机': 'emulator-virtual-machine', '前端框架 / 库': 'frontend-framework-library',
    '游戏': 'game', 'Git': 'git', '网络协议栈': 'network-stack', '神经网络': 'neural-network', '操作系统': 'operating-system',
    '物理引擎': 'physics-engine', '编程语言': 'programming-language', '正则表达式引擎': 'regex-engine', '搜索引擎': 'search-engine',
    'Shell': 'shell', '模板引擎': 'template-engine', '文本编辑器': 'text-editor', '视觉识别系统': 'visual-recognition-system',
    '体素引擎（Voxel Engine）': 'voxel-engine', '网页浏览器': 'web-browser', 'Web 服务器': 'web-server', '未分类': 'misc'
}
cat_re = re.compile(r'^#### 构建你自己的 `(?P<name>.+?)`')
uncat_re = re.compile(r'^#### 未分类')
entry_re = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?:\*\*)?(?P<lang>.*?)(?:\*\*)?: _(?P<title>.*?)_\]\((?P<url>.*?)\)(?P<suffix>.*)$')
plain_re = re.compile(r'^- \[(?P<done>[ Xx])\] \[(?P<title>.*?)\]\((?P<url>.*?)\)(?P<suffix>.*)$')

def clean(s):
    return re.sub(r'\s+', ' ', s.replace('**', '')).strip()

def ascii_slug(s):
    s = s.lower().replace('c++', 'cpp').replace('c#', 'csharp').replace('node.js', 'nodejs')
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')

keyword_map = {
    'physically based rendering': 'pbr', 'pbr': 'pbr', 'rasterization': 'rasterization', 'computer graphics': 'computer-graphics',
    '区块链': 'blockchain', 'blockchain': 'blockchain', 'cryptocurrency': 'cryptocurrency', 'telegram': 'telegram', 'discord': 'discord',
    'reddit': 'reddit', 'twitter': 'twitter', 'slack': 'slack', 'database': 'database', 'redis': 'redis', 'virtual machine': 'virtual-machine',
    'lc3': 'lc3', 'react': 'react', 'redux': 'redux', 'sudoku': 'sudoku', 'tetris': 'tetris', 'git': 'git', 'neural': 'neural-network',
    'cnn': 'cnn', 'traffic': 'traffic-signs', 'zero to hero': 'zero-to-hero', 'os': 'os', 'operating system': 'operating-system',
    'kernel': 'kernel', 'physics': 'physics', 'compiler': 'compiler', 'interpreter': 'interpreter', 'lisp': 'lisp', 'garbage': 'garbage-collector',
    'parser': 'parser', 'regex': 'regex', 'search': 'search', 'shell': 'shell', 'template': 'template', 'text editor': 'text-editor',
    'voxel': 'voxel', 'web server': 'web-server', 'web app': 'web-app', 'same-origin': 'same-origin-policy', 'terminal': 'terminal-emulator',
    'system call': 'system-call', 'game engine': 'game-engine', 'spell': 'spellchecker', 'load balancer': 'load-balancer', 'video': 'video-codec',
    'cache': 'cache', 'build system': 'build-system', 'link checker': 'link-checker', 'blog': 'blog', 'deep learning': 'deep-learning',
    'ci': 'ci', 'continuous integration': 'ci', 'recommendation': 'recommendation', 'decision tree': 'decision-tree', 'pedometer': 'pedometer', 'chat': 'chat-server',
    '渲染': 'rendering', '光栅化': 'rasterization', '图形学': 'computer-graphics', '机器人': 'bot', '数据库': 'database', '神经网络': 'neural-network',
    '操作系统': 'operating-system', '内核': 'kernel', '编译器': 'compiler', '解释器': 'interpreter', '正则': 'regex', '搜索': 'search', '模板': 'template',
    '文本': 'text-editor', '体素': 'voxel', '浏览器': 'browser', '负载均衡': 'load-balancer', '缓存': 'cache'
}

def source_slug(url):
    u = urlparse(url)
    parts = [p for p in (u.netloc + '/' + u.path).lower().split('/') if p]
    tokens = []
    for p in parts:
        p = p.replace('www.', '').replace('.com', '').replace('.org', '').replace('.io', '').replace('.net', '')
        for t in re.split(r'[^a-z0-9]+', p):
            if t and t not in {'github','medium','blog','posts','articles','watch','playlist','readme','html','index','part','tutorial','build','your','own','from','scratch','how','to','the','and','with'}:
                tokens.append(t)
    return '-'.join(tokens[:4]) or 'source'

def key_slug(title, url):
    low = title.lower()
    hits = []
    for k, v in keyword_map.items():
        if k.lower() in low and v not in hits:
            hits.append(v)
    if hits:
        return '-'.join(hits[:3])
    a = ascii_slug(title)
    if a:
        return '-'.join(a.split('-')[:5])
    return source_slug(url)

def lang_slug(lang):
    return ascii_slug(lang.replace('/', ' ')) or 'any'

items=[]; cur=None
for line in README.read_text(encoding='utf-8').splitlines():
    m=cat_re.match(line)
    if m:
        cur={'category':m.group('name'), 'category_slug':cat_map[m.group('name')]}; continue
    if uncat_re.match(line):
        cur={'category':'未分类', 'category_slug':'misc'}; continue
    if cur and line.startswith('- [ ]'):
        m=entry_re.match(line) or plain_re.match(line)
        if m:
            gd=m.groupdict(); title=clean(gd.get('title','')); lang=clean(gd.get('lang') or ('(any)' if 'NAND' in title or 'vibe' in title else 'General'))
            items.append({**cur, 'done': True, 'language': lang, 'title': title, 'url': gd['url'], 'suffix': clean(gd.get('suffix') or '')})

manifest=json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
existing_urls={x['url'] for x in manifest['created']}
existing_names={x['name'] for x in manifest['created']} | {p.name for p in SKILLS.iterdir() if p.is_dir()}
new_items=[x for x in items if x['url'] not in existing_urls]

def unique_name(item):
    base=f"{item['category_slug']}-{key_slug(item['title'], item['url'])}".strip('-')
    candidates=[base, f"{base}-{lang_slug(item['language'])}", f"{base}-{source_slug(item['url'])}", f"{base}-{lang_slug(item['language'])}-{source_slug(item['url'])}"]
    for c in candidates:
        c=c[:95].strip('-')
        if c and c not in existing_names:
            existing_names.add(c); return c
    i=2
    while True:
        c=f"{base}-variant-{i}"[:110].strip('-')
        if c not in existing_names:
            existing_names.add(c); return c
        i+=1

def skill_md(name,item):
    media='\n- Source is marked as video/PDF-like material; first create a transcript or structured outline before implementation.\n' if '[video]' in item['suffix'] or '[pdf]' in item['suffix'] else ''
    return f'''---
name: {name}
description: |
  Trigger when the user wants to learn, implement, debug, or extend "{item['title']}" or a {item['category']} build-your-own project using {item['language']}. Use this skill for staged Claude Code guidance, milestone planning, minimal implementation, and troubleshooting.
---

# {item['title']}

Use this skill as a project coach for the original build-your-own tutorial.

## Source

- **Category**: {item['category']}
- **Language / stack**: {item['language']}
- **Original resource**: {item['url']}
{media}
## Workflow

1. Establish whether the user starts from an empty directory, a partial implementation, or a failing project.
2. Default to `{item['language']}` unless the user chooses another stack.
3. Read `references/tutorial-map.md` and convert the source into 4-8 implementation milestones.
4. Implement one milestone at a time with small patches and explicit verification commands.
5. Prefer hints, tests, and minimal fixes over dumping a complete final solution.
6. Preserve the user's existing files and style.

## Milestone template

1. Project skeleton and first runnable command.
2. Core data model and invariants.
3. Input/parser/protocol/UI boundary.
4. Main algorithm or runtime engine.
5. Integration and end-to-end behavior.
6. Diagnostics, tests, and extensions.

## Expected outputs

- A staged implementation plan.
- A minimal project scaffold.
- A focused code patch for the current milestone.
- A debugging explanation and regression test.
'''

def ref_map(item):
    return f'''# Tutorial map: {item['title']}

- Source: {item['url']}
- Category: {item['category']}
- Language / stack: {item['language']}

## Suggested milestones

| Milestone | Deliverable | Verification |
|---|---|---|
| Skeleton | Minimal runnable project | Build/run command succeeds |
| Core model | Main types and invariants | Unit tests or assertions |
| Input layer | Parser/loader/protocol/UI input | Fixture or sample input test |
| Engine | Main algorithm/runtime behavior | Golden output or demo |
| Integration | End-to-end flow | Integration command |
| Hardening | Errors, edge cases, docs | Regression tests |
'''

def concepts(item):
    return f'''# Concepts checklist: {item['title']}

- Confirm target stack: `{item['language']}`.
- Identify the smallest observable behavior.
- Define core state and invariants before adding features.
- Add verification after every milestone.
- Explain tradeoffs and failure modes while coding.
'''

def evals(name,item):
    return {'skill_name': name, 'evals': [
        {'id':1,'prompt':f'我想用 {item["language"]} 从零实现「{item["title"]}」，请规划里程碑并只完成第一阶段。','expected_output':'Staged plan plus first milestone guidance.','files':[]},
        {'id':2,'prompt':f'我在实现「{item["title"]}」时测试失败，请阅读项目并做最小修复。','expected_output':'Diagnosis, minimal fix, and verification.','files':[]},
        {'id':3,'prompt':f'请基于 {item["url"]} 转换成 Claude Code 学习任务清单。','expected_output':'Milestone task list with deliverables and checks.','files':[]}
    ]}

def example_readme(item):
    return f'''# {item['title']}

> Example for skill: `{item['name']}`

## 推荐 Prompt

```text
[使用Skills: {item['name']}]
我想用 {item['language']} 从零实现「{item['title']}」。
请先检查当前目录是否为空，然后给我一个 4-8 个里程碑的学习计划。
从第一个最小可运行版本开始，只实现第一阶段，并提供验证命令。
```

## 原始资源

- 技术栈：`{item['language']}`
- 链接：{item['url']}
'''

created=[]
for item in new_items:
    name=unique_name(item); item['name']=name
    d=SKILLS/name
    (d/'references').mkdir(parents=True, exist_ok=True); (d/'examples'/'minimal').mkdir(parents=True, exist_ok=True); (d/'evals').mkdir(parents=True, exist_ok=True)
    (d/'SKILL.md').write_text(skill_md(name,item), encoding='utf-8')
    (d/'references'/'tutorial-map.md').write_text(ref_map(item), encoding='utf-8')
    (d/'references'/'concepts.md').write_text(concepts(item), encoding='utf-8')
    (d/'examples'/'minimal'/'README.md').write_text(f"# Minimal scaffold\n\nPlaceholder for `{name}`.\n", encoding='utf-8')
    (d/'evals'/'evals.json').write_text(json.dumps(evals(name,item), ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    ed=EXAMPLES/item['category_slug']/name; ed.mkdir(parents=True, exist_ok=True)
    (ed/'README.md').write_text(example_readme(item), encoding='utf-8')
    created.append(item)

manifest['created'].extend(created)
manifest['created_skills']=len(manifest['created'])
manifest.pop('removed_random_suffix_skills', None); manifest.pop('removed_random_suffix_count', None)
MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

# Update plan suggested names and status notes by URL.
url_to_name={x['url']:x['name'] for x in manifest['created']}
for p in PLAN.glob('*.md'):
    if p.name in {'README.md'}: continue
    s=p.read_text(encoding='utf-8')
    lines=s.splitlines(); out=[]; current_url=None
    for line in lines:
        if line.startswith('- **原始资源**：'):
            current_url=line.split('：',1)[1].strip()
            out.append(line); continue
        if current_url in url_to_name and line.startswith('- **建议 skill 名称**：'):
            out.append(f"- **建议 skill 名称**：`{url_to_name[current_url]}`")
            continue
        if current_url in url_to_name and line.startswith('- **转换目标**：'):
            out.append('- **当前状态**：已完成 skill 与 example 生成。')
            out.append(line)
            continue
        out.append(line)
    p.write_text('\n'.join(out)+'\n', encoding='utf-8')

# Regenerate examples indexes.
all_items=manifest['created']
by_cat=defaultdict(list)
for x in all_items: by_cat[x['category_slug']].append(x)
for slug, arr in by_cat.items():
    catdir=EXAMPLES/slug; catdir.mkdir(exist_ok=True)
    rows=['# '+arr[0]['category']+' examples','', '| Skill | 技术栈 | 原始项目 |','|---|---|---|']
    for x in sorted(arr, key=lambda z:z['name']): rows.append(f"| [`{x['name']}`](./{x['name']}/) | {x['language'].replace('|','/')} | {x['title'].replace('|','/')} |")
    (catdir/'README.md').write_text('\n'.join(rows)+'\n', encoding='utf-8')
root_rows=['# build-your-own-x skill examples','','| 分类 | 示例数 |','|---|---:|']
for slug in sorted(by_cat): root_rows.append(f"| [{by_cat[slug][0]['category']}](./{slug}/) | {len(by_cat[slug])} |")
(EXAMPLES/'README.md').write_text('\n'.join(root_rows)+'\n', encoding='utf-8')
(EXAMPLES/'examples-manifest.json').write_text(json.dumps({'category_count':len(by_cat),'example_count':len(all_items),'examples':[f"{x['category_slug']}/{x['name']}" for x in all_items]}, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

Path('/Volumes/my/github/build-your-own-x-skills/.session_tmps/8013dd29-fdb7-42e5-8c16-2cca6c1d84d5/new_skills.json').write_text(json.dumps(created, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
print(json.dumps({'missing_found':len(items),'new_created':len(created),'total_skills':len(all_items),'categories':len(by_cat)}, ensure_ascii=False, indent=2))
