# 从零实现 Promise（TDD 风格）

> Example for skill: `misc-promise-tdd`

## 场景

你想通过 Claude Code 学习并逐步实现 **从零实现 Promise（TDD 风格）**，而不是一次性拿到完整答案。

## 推荐 Prompt

```text
[使用Skills: misc-promise-tdd]
我想用 JavaScript 从零实现「从零实现 Promise（TDD 风格）」。
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

- 理解 `未分类` 项目的核心模型和关键约束。
- 能独立运行第一阶段的最小版本。
- 通过测试或可观察输出验证每个里程碑。
- 在后续阶段逐步扩展，而不是复制粘贴完整实现。

## 原始资源

- 技术栈：`JavaScript`
- 链接：https://www.mauriciopoppe.com/notes/computer-science/computation/promises/

## 适合测试的变体 Prompt

```text
[使用Skills: misc-promise-tdd]
我已经按照「从零实现 Promise（TDD 风格）」做到一半，但测试失败了。请先阅读项目文件，定位当前处于哪个里程碑，再做最小修复并解释原因。
```

```text
[使用Skills: misc-promise-tdd]
请基于这个教程资源：https://www.mauriciopoppe.com/notes/computer-science/computation/promises/
把它整理成 Claude Code 可执行的学习任务清单，每个任务都要有交付物和验收命令。
```
