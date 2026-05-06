# 构建你自己的 增强现实（AR）：skill 转换计划

- **分类 slug**：`augmented-reality`
- **项目数量**：6
- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）

## 分类级转换策略

将 `增强现实（AR）` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。

## 项目计划

### 1. 入门教程：使用 Vuforia 与 Unity 3D 的增强现实应用

- **原始语言/技术栈**：C#
- **原始资源**：https://www.youtube.com/watch?v=uXNjNcqW4kY
- **建议 skill 名称**：`augmented-reality-vuforia-unity-3d`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`入门教程：使用 Vuforia 与 Unity 3D 的增强现实应用`、`C#` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。

### 2. Unity ARCore 教程

- **原始语言/技术栈**：C#
- **原始资源**：https://www.youtube.com/playlist?list=PLKIKuXdn4ZMjuUAtdQfK1vwTZPQn_rgSv
- **建议 skill 名称**：`augmented-reality-unity-arcore`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`Unity ARCore 教程`、`C#` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。

### 3. Unity AR 传送门（Portal）教程

- **原始语言/技术栈**：C#
- **原始资源**：https://www.youtube.com/playlist?list=PLPCqNOwwN794Gz5fzUSi1p4OqLU0HTmvn
- **建议 skill 名称**：`augmented-reality-unity-ar-portal`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`Unity AR 传送门（Portal）教程`、`C#` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。

### 4. 如何在 Unity ARCore 中创建一条 AR 龙

- **原始语言/技术栈**：C#
- **原始资源**：https://www.youtube.com/watch?v=qTSDPkPyPqs
- **建议 skill 名称**：`augmented-reality-unity-arcore-ar`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`如何在 Unity ARCore 中创建一条 AR 龙`、`C#` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。

### 5. AR 教程：ARKit 传送门通往“颠倒世界”

- **原始语言/技术栈**：C#
- **原始资源**：https://www.youtube.com/watch?v=Z5AmqMuNi08
- **建议 skill 名称**：`augmented-reality-ar-arkit`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`AR 教程：ARKit 传送门通往“颠倒世界”`、`C#` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
- **特殊处理**：该资源包含视频/PDF标记，需先生成文字大纲或章节摘要，再转换为渐进式 `references/`。

### 6. 用 Python 与 OpenCV 实现增强现实

- **原始语言/技术栈**：Python
- **原始资源**：https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/
- **建议 skill 名称**：`augmented-reality-python-opencv`
- **触发场景**：用户想从零实现、学习、调试或扩展 `增强现实（AR）` 相关项目，尤其提到“augmented-reality”、`用 Python 与 OpenCV 实现增强现实`、`Python` 实现时。
- **转换目标**：把教程转化为 Claude Code 可执行的项目教练技能，能够分阶段引导用户理解原理、搭建工程、实现核心模块、运行测试并迭代改进。
- **SKILL.md 规划**：
  - 说明适用人群、前置知识、环境依赖与推荐学习节奏。
  - 将原教程拆成 4-8 个里程碑，每个里程碑包含目标、关键概念、待实现文件、验证命令。
  - 提供“从空目录开始”“接手半成品项目”“排查失败测试”三种工作流。
  - 明确不要直接代写完整答案，优先用提示、最小补丁和测试驱动帮助学习。
- **附带资源规划**：
  - `references/tutorial-map.md`：原教程章节到 skill 里程碑的映射。
  - `references/concepts.md`：核心概念、数据结构、协议/算法说明。
  - `examples/minimal/`：最小可运行示例或项目骨架。
  - `evals/evals.json`：至少 3 个测试 prompt，覆盖新建项目、实现功能、修复 bug。
- **验收标准**：
  - 用户能在空目录生成项目骨架并通过第一阶段测试。
  - 每个里程碑都有可运行命令或可观察输出。
  - skill 能根据用户选择的语言/平台调整指导，不强行覆盖用户已有代码。
