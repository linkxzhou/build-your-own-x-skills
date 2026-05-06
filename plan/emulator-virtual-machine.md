# 构建你自己的 模拟器 / 虚拟机：skill 转换计划

- **分类 slug**：`emulator-virtual-machine`
- **项目数量**：13
- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）

## 分类级转换策略

将 `模拟器 / 虚拟机` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。

## 项目计划

### 1. 自制字节码解释器

- **原始语言/技术栈**：C
- **原始资源**：https://medium.com/bumble-tech/home-grown-bytecode-interpreters-51e12d59b25c
- **建议 skill 名称**：`emulator-virtual-machine`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`自制字节码解释器`、`C` 实现时。
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

### 2. 用 C 写虚拟机

- **原始语言/技术栈**：C
- **原始资源**：http://web.archive.org/web/20200121100942/https://blog.felixangell.com/virtual-machine-in-c/
- **建议 skill 名称**：`emulator-virtual-machine-c`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`用 C 写虚拟机`、`C` 实现时。
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

### 3. 编写你自己的虚拟机

- **原始语言/技术栈**：C
- **原始资源**：https://justinmeiners.github.io/lc3-vm/
- **建议 skill 名称**：`emulator-virtual-machine`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`编写你自己的虚拟机`、`C` 实现时。
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

### 4. 用 Cinoop 编写 Game Boy 模拟器

- **原始语言/技术栈**：C
- **原始资源**：https://cturt.github.io/cinoop.html
- **建议 skill 名称**：`emulator-virtual-machine-cinoop-game-boy`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`用 Cinoop 编写 Game Boy 模拟器`、`C` 实现时。
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

### 5. 如何写一个模拟器（CHIP-8 解释器）

- **原始语言/技术栈**：C++
- **原始资源**：http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/
- **建议 skill 名称**：`emulator-virtual-machine-chip-8`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`如何写一个模拟器（CHIP-8 解释器）`、`C++` 实现时。
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

### 6. 模拟器教程（CHIP-8 解释器）

- **原始语言/技术栈**：C++
- **原始资源**：http://www.codeslinger.co.uk/pages/projects/chip8.html
- **建议 skill 名称**：`emulator-virtual-machine-chip-8`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`模拟器教程（CHIP-8 解释器）`、`C++` 实现时。
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

### 7. 模拟器教程（GameBoy 模拟器）

- **原始语言/技术栈**：C++
- **原始资源**：http://www.codeslinger.co.uk/pages/projects/gameboy.html
- **建议 skill 名称**：`emulator-virtual-machine-gameboy`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`模拟器教程（GameBoy 模拟器）`、`C++` 实现时。
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

### 8. 模拟器教程（Master System 模拟器）

- **原始语言/技术栈**：C++
- **原始资源**：http://www.codeslinger.co.uk/pages/projects/mastersystem/memory.html
- **建议 skill 名称**：`emulator-virtual-machine-master-system`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`模拟器教程（Master System 模拟器）`、`C++` 实现时。
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

### 9. 从零构建 NES 模拟器

- **原始语言/技术栈**：C++
- **原始资源**：https://www.youtube.com/playlist?list=PLrOv9FMX8xJHqMvSGB_9G9nZZ_4IgteYf
- **建议 skill 名称**：`emulator-virtual-machine-nes`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`从零构建 NES 模拟器`、`C++` 实现时。
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

### 10. 用 Common Lisp 实现 CHIP-8

- **原始语言/技术栈**：Common Lisp
- **原始资源**：http://stevelosh.com/blog/2016/12/chip8-cpu/
- **建议 skill 名称**：`emulator-virtual-machine-common-lisp-chip-8`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`用 Common Lisp 实现 CHIP-8`、`Common Lisp` 实现时。
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

### 11. 用 JavaScript 做 GameBoy 模拟

- **原始语言/技术栈**：JavaScript
- **原始资源**：http://imrannazar.com/GameBoy-Emulation-in-JavaScript
- **建议 skill 名称**：`emulator-virtual-machine-javascript-gameboy`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`用 JavaScript 做 GameBoy 模拟`、`JavaScript` 实现时。
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

### 12. 模拟器基础：编写你自己的 Chip-8 模拟器/解释器

- **原始语言/技术栈**：Python
- **原始资源**：http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8.html
- **建议 skill 名称**：`emulator-virtual-machine-chip-8`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`模拟器基础：编写你自己的 Chip-8 模拟器/解释器`、`Python` 实现时。
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

### 13. 0dmg：通过构建部分 Game Boy 模拟器学习 Rust

- **原始语言/技术栈**：Rust
- **原始资源**：https://jeremybanks.github.io/0dmg/
- **建议 skill 名称**：`emulator-virtual-machine-0dmg-game-boy-rust`
- **触发场景**：用户想从零实现、学习、调试或扩展 `模拟器 / 虚拟机` 相关项目，尤其提到“emulator-virtual-machine”、`0dmg：通过构建部分 Game Boy 模拟器学习 Rust`、`Rust` 实现时。
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
