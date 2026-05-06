# 构建你自己的 神经网络：skill 转换计划

- **分类 slug**：`neural-network`
- **项目数量**：14
- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）

## 分类级转换策略

将 `神经网络` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。

## 项目计划

### 1. 神经网络 OCR

- **原始语言/技术栈**：C#
- **原始资源**：https://www.codeproject.com/Articles/11285/Neural-Network-OCR
- **建议 skill 名称**：`neural-network-neural-network`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`神经网络 OCR`、`C#` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 2. 用 F# 构建神经网络

- **原始语言/技术栈**：F#
- **原始资源**：https://towardsdatascience.com/building-neural-networks-in-f-part-1-a2832ae972e6
- **建议 skill 名称**：`neural-network-neural-network-f`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`用 F# 构建神经网络`、`F#` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 3. 用 Go 构建多层感知机

- **原始语言/技术栈**：Go
- **原始资源**：https://made2591.github.io/posts/neuralnetwork
- **建议 skill 名称**：`neural-network-go`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`用 Go 构建多层感知机`、`Go` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 4. 如何用 Go 构建一个简单的人工神经网络

- **原始语言/技术栈**：Go
- **原始资源**：https://sausheong.github.io/posts/how-to-build-a-simple-artificial-neural-network-with-go/
- **建议 skill 名称**：`neural-network-neural-network-go`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`如何用 Go 构建一个简单的人工神经网络`、`Go` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 5. 用 Go 从零构建神经网络

- **原始语言/技术栈**：Go
- **原始资源**：https://datadan.io/blog/neural-net-with-go
- **建议 skill 名称**：`neural-network-neural-network-datadan-neural-net-go`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`用 Go 从零构建神经网络`、`Go` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 6. 神经网络：《代码本色》

- **原始语言/技术栈**：JavaScript / Java
- **原始资源**：https://www.youtube.com/playlist?list=PLRqwX-V7Uu6aCibgK1PTWWu9by6XFdCfh
- **建议 skill 名称**：`neural-network-neural-network-javascript-java`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`神经网络：《代码本色》`、`JavaScript / Java` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 7. 面向 JavaScript 语言学家的神经网络从零开始（第 1 部分：感知机）

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://hackernoon.com/neural-networks-from-scratch-for-javascript-linguists-part1-the-perceptron-632a4d1fbad2
- **建议 skill 名称**：`neural-network-neural-network-javascript`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`面向 JavaScript 语言学家的神经网络从零开始（第 1 部分：感知机）`、`JavaScript` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 8. 11 行 Python 的神经网络

- **原始语言/技术栈**：Python
- **原始资源**：https://iamtrask.github.io/2015/07/12/basic-python-network/
- **建议 skill 名称**：`neural-network-neural-network-python`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`11 行 Python 的神经网络`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 9. 从零实现神经网络

- **原始语言/技术栈**：Python
- **原始资源**：https://victorzhou.com/blog/intro-to-neural-networks/
- **建议 skill 名称**：`neural-network-neural-network-victorzhou-intro-neural-networks`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`从零实现神经网络`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 10. 光学字符识别（OCR）

- **原始语言/技术栈**：Python
- **原始资源**：http://aosabook.org/en/500L/optical-character-recognition-ocr.html
- **建议 skill 名称**：`neural-network-ocr`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`光学字符识别（OCR）`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 11. 用卷积网络进行交通标志分类

- **原始语言/技术栈**：Python
- **原始资源**：https://navoshta.com/traffic-signs-classification/
- **建议 skill 名称**：`neural-network-navoshta-traffic-signs-classification`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`用卷积网络进行交通标志分类`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 12. 用 Keras 的 LSTM 生成音乐

- **原始语言/技术栈**：Python
- **原始资源**：https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5
- **建议 skill 名称**：`neural-network-keras-lstm`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`用 Keras 的 LSTM 生成音乐`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 13. 卷积神经网络（CNN）入门

- **原始语言/技术栈**：Python
- **原始资源**：https://victorzhou.com/blog/intro-to-cnns-part-1/
- **建议 skill 名称**：`neural-network-cnn-neural-network`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`卷积神经网络（CNN）入门`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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

### 14. 神经网络：从零到英雄（Zero to Hero）

- **原始语言/技术栈**：Python
- **原始资源**：https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ
- **建议 skill 名称**：`neural-network-zero-to-hero-neural-network`
- **触发场景**：用户想从零实现、学习、调试或扩展 `神经网络` 相关项目，尤其提到“neural-network”、`神经网络：从零到英雄（Zero to Hero）`、`Python` 实现时。
- **当前状态**：已完成 skill 与 example 生成。
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
