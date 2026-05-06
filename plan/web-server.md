# 构建你自己的 Web 服务器：skill 转换计划

- **分类 slug**：`web-server`
- **项目数量**：11
- **目标平台**：Claude Code skills（同时兼容本仓库 `skills/` 目录约定）

## 分类级转换策略

将 `Web 服务器` 分类下的每个教程转换为面向实践学习的开发技能。优先保持“一教程一 skill”，后续可按语言或共同核心抽象合并。

## 项目计划

### 1. 从零编写 Web 服务器

- **原始语言/技术栈**：C#
- **原始资源**：https://www.codeproject.com/Articles/859108/Writing-a-Web-Server-from-Scratch
- **建议 skill 名称**：`web-server-web`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`从零编写 Web 服务器`、`C#` 实现时。
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

### 2. 用 JavaScript 从零构建你自己的 Web 服务器

- **原始语言/技术栈**：Node.js
- **原始资源**：https://build-your-own.org/webserver/
- **建议 skill 名称**：`web-server-javascript-web`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用 JavaScript 从零构建你自己的 Web 服务器`、`Node.js` 实现时。
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

### 3. 用 NodeJS Streams 从零写 Web 服务器

- **原始语言/技术栈**：Node.js
- **原始资源**：https://www.codementor.io/@ziad-saab/let-s-code-a-web-server-from-scratch-with-nodejs-streams-h4uc9utji
- **建议 skill 名称**：`web-server-nodejs-streams-web`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用 NodeJS Streams 从零写 Web 服务器`、`Node.js` 实现时。
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

### 4. lets-build-express

- **原始语言/技术栈**：Node.js
- **原始资源**：https://github.com/antoaravinth/lets-build-express
- **建议 skill 名称**：`web-server-lets-build-express`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`lets-build-express`、`Node.js` 实现时。
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

### 5. 用纯 PHP 编写 Web 服务器

- **原始语言/技术栈**：PHP
- **原始资源**：http://station.clancats.com/writing-a-webserver-in-pure-php/
- **建议 skill 名称**：`web-server-php-web`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用纯 PHP 编写 Web 服务器`、`PHP` 实现时。
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

### 6. 一个简单的 Web 服务器

- **原始语言/技术栈**：Python
- **原始资源**：http://aosabook.org/en/500L/a-simple-web-server.html
- **建议 skill 名称**：`web-server-web-python`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`一个简单的 Web 服务器`、`Python` 实现时。
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

### 7. 让我们构建一个 Web 服务器

- **原始语言/技术栈**：Python
- **原始资源**：https://ruslanspivak.com/lsbaws-part1/
- **建议 skill 名称**：`web-server-web-ruslanspivak-lsbaws-part1`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`让我们构建一个 Web 服务器`、`Python` 实现时。
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

### 8. 从零构建 Web 应用

- **原始语言/技术栈**：Python
- **原始资源**：https://defn.io/2018/02/25/web-app-from-scratch-01/
- **建议 skill 名称**：`web-server-web-defn-2018-02-25`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`从零构建 Web 应用`、`Python` 实现时。
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

### 9. 用 Python 从零构建基础 HTTP Server

- **原始语言/技术栈**：Python
- **原始资源**：http://joaoventura.net/blog/2017/python-webserver/
- **建议 skill 名称**：`web-server-http`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用 Python 从零构建基础 HTTP Server`、`Python` 实现时。
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

### 10. 用 Python + Flask 实现 RESTful Web API

- **原始语言/技术栈**：Python
- **原始资源**：http://blog.luisrei.com/articles/flaskrest.html
- **建议 skill 名称**：`web-server-python-flask-restful-web-api`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用 Python + Flask 实现 RESTful Web API`、`Python` 实现时。
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

### 11. 用 Ruby 从零构建简单 websockets 服务器

- **原始语言/技术栈**：Ruby
- **原始资源**：http://blog.honeybadger.io/building-a-simple-websockets-server-from-scratch-in-ruby/
- **建议 skill 名称**：`web-server-ruby-websockets`
- **触发场景**：用户想从零实现、学习、调试或扩展 `Web 服务器` 相关项目，尤其提到“web-server”、`用 Ruby 从零构建简单 websockets 服务器`、`Ruby` 实现时。
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
