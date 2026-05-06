import json
import re
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path('/Volumes/my/github/build-your-own-x-skills')
SKILLS_MANIFEST = ROOT / 'skills' / 'x-skills-manifest.json'
EXAMPLES_MANIFEST = ROOT / 'examples' / 'examples-manifest.json'
PLAN_MANIFEST = ROOT / 'plan' / 'manifest.json'

skills = json.loads(SKILLS_MANIFEST.read_text(encoding='utf-8'))
examples = json.loads(EXAMPLES_MANIFEST.read_text(encoding='utf-8'))
plans = json.loads(PLAN_MANIFEST.read_text(encoding='utf-8'))
created = skills['created']
converted_urls = {item['url'] for item in created}
by_cat = Counter(item['category_slug'] for item in created)
cat_name = {item['category_slug']: item['category'] for item in created}
progress = round(len(created) / plans['project_count'] * 100)
bar_len = 20
filled = round(progress / 100 * bar_len)
bar = '▓' * filled + '░' * (bar_len - filled)

cn_categories = '\n'.join(
    f"| [{cat_name[slug]}](./examples/{slug}/) | {count} |"
    for slug, count in sorted(by_cat.items())
)
en_categories = '\n'.join(
    f"| [{slug}](./examples/{slug}/) | {count} |"
    for slug, count in sorted(by_cat.items())
)

def mark_converted(text: str) -> str:
    def repl(m):
        line = m.group(0)
        url = m.group('url')
        if url in converted_urls:
            return line.replace('- [ ]', '- [X]', 1)
        return line
    return re.sub(r'^- \[(?: |X|x)\] \[.*?\]\((?P<url>[^)]+)\).*$', repl, text, flags=re.M)

cn_prefix = f'''# 背景
本项目的目标是将 `https://github.com/codecrafters-io/build-your-own-x` 中的项目逐步转换为 skills，让每个开发者都能通过 AI 技术，快速学习各种工程实践技能。

## 当前状态

- 原始 build-your-own-x 条目数：`{plans['project_count']}`
- 已保留可用 skills：`{len(created)}`
- 已生成 examples：`{examples['example_count']}`
- 分类数：`{examples['category_count']}`
- 转换计划：`plan/`
- skill 清单：`skills/x-skills-manifest.json`
- example 清单：`examples/examples-manifest.json`

> 说明：此前生成过带 8 位哈希后缀的临时 skill，因名称可读性差已删除；当前 README 中勾选的条目对应保留在 `skills/` 中的可用 skill。

## 目录结构

```
build-your-own-x-skills/
├── .claude/skills/          # Claude Code skills 目录，软链到 skills/
├── .codebuddy/skills/       # CodeBuddy skills 目录，软链到 skills/
├── .trae/skills/            # TRAE skills 目录，软链到 skills/
├── .gemini/skills/          # Gemini CLI skills 目录，软链到 skills/
├── skills/                  # skills 主目录，每个子目录是一个 skill
├── plan/                    # build-your-own-x 到 skill 的转换计划
├── examples/                # 按大类型组织的 skill 使用示例
├── tests/                   # 技能测试
├── README.md                # 中文说明
├── README_EN.md             # 英文说明
├── README_PROMPT.md         # Prompt 模板与测试提示词
└── init.sh                  # 初始化软链脚本
```

## 安装

1. 克隆项目到本地。
2. 运行 `./init.sh`，将 `skills/` 软链到各 AI 编程工具的技能目录。
3. 在支持 skills 的工具中使用 `[使用Skills: skill-name]` 或自动触发。

## 使用示例

每个可用 skill 都有一个对应 example，按大类型组织：

| 分类 | 示例数 |
|---|---:|
{cn_categories}

示例入口：

- 根索引：[`examples/README.md`](./examples/README.md)
- 数据库示例：[`examples/database/database-redis/`](./examples/database/database-redis/)
- 编程语言示例：[`examples/programming-language/`](./examples/programming-language/)

## 转换计划

- 总索引：[`plan/README.md`](./plan/README.md)
- 每个分类一个计划文件，例如 `plan/database.md`、`plan/programming-language.md`。
- 每个项目计划包含建议 skill 名称、触发场景、`SKILL.md` 规划、资源规划和验收标准。

## 完成进度

![Progress](https://img.shields.io/badge/进度-{progress}%25-yellow?style=flat-square)

{bar} {progress}%

## build-your-own-x 项目列表
'''

en_prefix = f'''# Background

The goal of this project is to gradually convert projects from `https://github.com/codecrafters-io/build-your-own-x` into skills, enabling developers to learn engineering topics quickly with AI-assisted, project-based workflows.

## Current Status

- Original build-your-own-x entries: `{plans['project_count']}`
- Available generated skills kept: `{len(created)}`
- Generated examples: `{examples['example_count']}`
- Categories: `{examples['category_count']}`
- Conversion plans: `plan/`
- Skill manifest: `skills/x-skills-manifest.json`
- Example manifest: `examples/examples-manifest.json`

> Note: earlier temporary skills with 8-character hash suffixes were removed because their names were not readable. Checked items below correspond to skills currently kept under `skills/`.

## Directory Structure

```
build-your-own-x-skills/
├── .claude/skills/          # Claude Code skills directory, symlinked to skills/
├── .codebuddy/skills/       # CodeBuddy skills directory, symlinked to skills/
├── .trae/skills/            # TRAE skills directory, symlinked to skills/
├── .gemini/skills/          # Gemini CLI skills directory, symlinked to skills/
├── skills/                  # Main skills directory; each subdirectory is a skill
├── plan/                    # Conversion plans from build-your-own-x entries to skills
├── examples/                # Skill usage examples grouped by category
├── tests/                   # Skill tests
├── README.md                # Chinese README
├── README_EN.md             # English README
├── README_PROMPT.md         # Prompt templates and test prompts
└── init.sh                  # Symlink initialization script
```

## Installation

1. Clone this repository.
2. Run `./init.sh` to symlink `skills/` into supported AI coding tools.
3. Use `[使用Skills: skill-name]` or rely on automatic skill triggering.

## Examples

Each available generated skill has a corresponding example grouped by category:

| Category | Examples |
|---|---:|
{en_categories}

Entry points:

- Root index: [`examples/README.md`](./examples/README.md)
- Database example: [`examples/database/database-redis/`](./examples/database/database-redis/)
- Programming language examples: [`examples/programming-language/`](./examples/programming-language/)

## Conversion Plans

- Index: [`plan/README.md`](./plan/README.md)
- One plan file per category, e.g. `plan/database.md`, `plan/programming-language.md`.
- Each project plan includes suggested skill name, trigger scenarios, `SKILL.md` plan, resource plan, and acceptance criteria.

## Progress

![Progress](https://img.shields.io/badge/Progress-{progress}%25-yellow?style=flat-square)

{bar} {progress}%

## build-your-own-x Projects
'''

def update_main_readme(path: Path, prefix: str):
    text = path.read_text(encoding='utf-8')
    marker = '## build-your-own-x 项目列表' if path.name == 'README.md' else '## build-your-own-x Projects'
    idx = text.index(marker)
    project_list = text[idx + len(marker):]
    project_list = mark_converted(project_list)
    path.write_text(prefix + project_list.lstrip('\n'), encoding='utf-8')

update_main_readme(ROOT / 'README.md', cn_prefix)
update_main_readme(ROOT / 'README_EN.md', en_prefix)

prompt_path = ROOT / 'README_PROMPT.md'
old_prompt = prompt_path.read_text(encoding='utf-8')
byox_prompt = f'''# Prompt 模板与测试提示词

## build-your-own-x skills 使用模板

当前仓库已保留 `{len(created)}` 个 build-your-own-x 相关 skill，并为每个 skill 生成了一个 example。示例入口见 [`examples/README.md`](./examples/README.md)。

### 通用学习 Prompt

```text
[使用Skills: <skill-name>]
我想从零实现「<项目名称>」。
请先检查当前目录是否为空，然后给我一个 4-8 个里程碑的学习计划。
从第一个最小可运行版本开始，只实现第一阶段，并提供验证命令。
```

### 通用调试 Prompt

```text
[使用Skills: <skill-name>]
我已经做到一半，但测试失败了。
请先阅读项目文件，定位当前处于哪个里程碑，再做最小修复并解释原因。
```

### 通用教程转换 Prompt

```text
[使用Skills: <skill-name>]
请基于原始教程资源，把它整理成 Claude Code 可执行的学习任务清单。
每个任务都要包含交付物、关键概念、待修改文件和验收命令。
```

### 具体示例

```text
[使用Skills: database-redis]
我想用 C++ 从零实现「从零构建你自己的 Redis」。
请先检查当前目录是否为空，然后给我一个 4-8 个里程碑的学习计划。
从第一个最小可运行版本开始，只实现第一阶段，并提供验证命令。
```

```text
[使用Skills: programming-language-lisp]
我想实现一个 Lisp 解释器。请用测试驱动方式带我完成第一个可运行版本，不要一次性生成完整答案。
```

```text
[使用Skills: web-server-webserver]
我想从零实现一个 Web Server。请先规划 HTTP 请求解析、响应生成、连接处理和测试方式。
```

## examples 生成规则

- examples 按大类型分组，如 `examples/database/`、`examples/programming-language/`。
- 每个 skill 对应一个 `examples/<category>/<skill-name>/README.md`。
- 每个 example 包含推荐 Prompt、预期交互、学习目标、原始资源和变体测试 Prompt。

---

'''
# Preserve the historical Manim prompt section, but make it a separate section.
old_prompt = re.sub(r'^# 输出提示词\n+', '# 历史 Manim 输出提示词\n\n', old_prompt)
prompt_path.write_text(byox_prompt + old_prompt, encoding='utf-8')

print(json.dumps({'progress': progress, 'skills': len(created), 'examples': examples['example_count']}, ensure_ascii=False, indent=2))
