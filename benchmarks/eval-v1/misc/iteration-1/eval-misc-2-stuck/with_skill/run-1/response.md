The user is asking in Chinese: "I want to write my own package manager (like npm), where do I start?"

This matches the build-your-own-x skill — "自己动手写一个 X" (build your own X), specifically a package manager. The skill description says to read the SKILL.md BEFORE doing anything else.

Let me read the skill file first.The file was truncated. Let me read the rest of it to see the category map and find the right slug for a package manager.包管理器映射到 `misc` 轨道。正在读取该轨道技能：教程列表被截断了。让我搜索一下与包管理器相关的条目，并检查是否有针对特定教程的技能：有一个完全匹配的教程：**Tiny Package Manager** (TypeScript, 学习 npm/Yarn 的工作原理)。正在阅读其针对特定教程的辅导技能：推荐从 **Tiny Package Manager** 入手——一个专门演示 npm/Yarn 核心原理的 TypeScript 教程项目：
https://github.com/g-plane/tiny-package-manager

**npm 拆开就是 4 件事：**
1. 读 `package.json`，拿到依赖名和版本
2. 查 registry（一个 HTTP API），拿到 tarball 下载地址
3. 下载 tarball，解压到 `node_modules/<name>`
4. 递归处理“依赖的依赖”（版本解析）

当前进度：里程碑 1/7（定范围）。建议的里程碑和检查点：

| # | 里程碑 | 检查点 |
|---|---|---|
| 1 | 骨架：CLI 入口 + `install` 命令占位 | `mypm install left-pad` 能跑通到“尚未实现” |
| 2 | 解析 package.json 的依赖表 | 单测：fixture 解析出正确的依赖 map |
| 3 | 查 registry：`GET registry.npmjs.org/<name>` | 打印出某版本的 tarball URL |
| 4 | 下载 + 解压 tarball 到 node_modules | `node_modules/left-pad/package.json` 存在且内容正确 |
| 5 | 递归安装依赖（先只装最新版） | left-pad 的依赖也出现在 node_modules |
| 6 | semver 版本解析（^ ~ 精确版本） | 3 个失败用例通过：404、网络错误、非法版本号 |
| 7 | 与真 npm 对比同一 fixture | 两边 node_modules 结构 diff 一致 |

两个问题，都带默认值：

1. **语言**：用 TypeScript/Node 吗？默认是——教程就是这个栈，且 npm 本身是 JS 生态，概念直接对应。前置条件是 Node 18+（需要内置 fetch），你可以先跑 `node -v` 确认。
2. **目标范围**：把“完成”定义成 `mypm install left-pad` 能把 left-pad 及其全部依赖装进 node_modules，可以吗？这是最小可用版本，做完再谈锁文件、缓存、离线模式这些扩展。

确认后从里程碑 1 开始：建项目骨架。