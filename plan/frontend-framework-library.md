# 构建你自己的 前端框架 / 库：skill 转换计划

- **分类 slug**：`frontend-framework-library`
- **项目数量**：14
- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）

## 分类级转换策略

将 `前端框架 / 库` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。

## 项目计划

### 1. JSX 到底是什么（让我们构建一个 JSX 渲染器）

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://jasonformat.com/wtf-is-jsx/
- **建议 skill 名称**：`frontend-framework-library-jsx-jsx`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`JSX 到底是什么（让我们构建一个 JSX 渲染器）`、`JavaScript` 实现时。
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

### 2. 从零构建你自己的 React（DIY 指南）

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://github.com/hexacta/didact
- **建议 skill 名称**：`frontend-framework-library-react`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`从零构建你自己的 React（DIY 指南）`、`JavaScript` 实现时。
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

### 3. 从零构建 React

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://www.youtube.com/watch?v=_MAD4Oly9yg
- **建议 skill 名称**：`frontend-framework-library-react-javascript`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`从零构建 React`、`JavaScript` 实现时。
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

### 4. Gooact：160 行 JavaScript 的 React

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://medium.com/@sweetpalma/gooact-react-in-160-lines-of-javascript-44e0742ad60f
- **建议 skill 名称**：`frontend-framework-library-react-sweetpalma-gooact-react-in`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`Gooact：160 行 JavaScript 的 React`、`JavaScript` 实现时。
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

### 5. 通过构建轻量 React DOM 来理解 React Reconciler 如何工作

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://hackernoon.com/learn-you-some-custom-react-renderers-aed7164a4199
- **建议 skill 名称**：`frontend-framework-library-react-ci`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`通过构建轻量 React DOM 来理解 React Reconciler 如何工作`、`JavaScript` 实现时。
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

### 6. 自己写一个 Redux

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://zapier.com/engineering/how-to-build-redux/
- **建议 skill 名称**：`frontend-framework-library-redux`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`自己写一个 Redux`、`JavaScript` 实现时。
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

### 7. 让我们写 Redux！

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://www.jamasoftware.com/blog/lets-write-redux/
- **建议 skill 名称**：`frontend-framework-library-redux-javascript`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`让我们写 Redux！`、`JavaScript` 实现时。
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

### 8. Redux：从零实现 Store

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://egghead.io/lessons/react-redux-implementing-store-from-scratch
- **建议 skill 名称**：`frontend-framework-library-redux-egghead-lessons-react-redux`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`Redux：从零实现 Store`、`JavaScript` 实现时。
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

### 9. 200 行 JavaScript 实现一个简化版 AngularJS

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://blog.mgechev.com/2015/03/09/build-learn-your-own-light-lightweight-angularjs/
- **建议 skill 名称**：`frontend-framework-library-angular`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`200 行 JavaScript 实现一个简化版 AngularJS`、`JavaScript` 实现时。
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

### 10. 自己做一个 AngularJS

- **原始语言/技术栈**：JavaScript
- **原始资源**：http://teropa.info/blog/2013/11/03/make-your-own-angular-part-1-scopes-and-digest.html
- **建议 skill 名称**：`frontend-framework-library-angular-javascript`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`自己做一个 AngularJS`、`JavaScript` 实现时。
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

### 11. 如何实现你自己的 Virtual DOM

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060
- **建议 skill 名称**：`frontend-framework-library-virtual-dom`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`如何实现你自己的 Virtual DOM`、`JavaScript` 实现时。
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

### 12. 从零构建前端框架（组件、模板、状态、VDOM）

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://mfrachet.github.io/create-frontend-framework/
- **建议 skill 名称**：`frontend-framework-library-template`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`从零构建前端框架（组件、模板、状态、VDOM）`、`JavaScript` 实现时。
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

### 13. 构建你自己的 React

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://pomb.us/build-your-own-react/
- **建议 skill 名称**：`frontend-framework-library-react-pomb-us-react`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`构建你自己的 React`、`JavaScript` 实现时。
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

### 14. 构建一个自定义 React Renderer

- **原始语言/技术栈**：JavaScript
- **原始资源**：https://youtu.be/CGpMlWVcHok
- **建议 skill 名称**：`frontend-framework-library-react-youtu-be-cgpmlwvchok`
- **触发场景**：用户想从零实现、学习、调试或扩展 `前端框架 / 库` 相关项目，尤其提到“frontend-framework-library”、`构建一个自定义 React Renderer`、`JavaScript` 实现时。
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
