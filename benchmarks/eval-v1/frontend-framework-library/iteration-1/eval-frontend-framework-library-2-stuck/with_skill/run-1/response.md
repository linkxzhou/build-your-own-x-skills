The user is asking about a React-like useState implementation they wrote themselves. They say: "I wrote my own useState, every time I click the button the state resets to initial value. I declared `let state = initial` inside the component function."

This is a classic learning-by-building question — implementing useState from scratch. The issue: state is declared inside the component function body, so every render re-initializes it. The fix: move state outside the component (closure/module scope), or use a hook index / fiber-like storage.

There's a skill available: build-your-own-x — "an interpreter/compiler/programming language... Use it whenever someone wants to understand how a tool works by building their own... 手写..." The user is building their own useState (a React hook). This matches "build your own x" — building your own React hooks. The skill says to read SKILL.md BEFORE doing anything else when the task matches.

Hmm, does this match? The user isn't asking for a project recommendation; they have a concrete bug in their own useState implementation. The skill description: "Entry point for learning by rebuilding real software from scratch (build-your-own-x): Git, Redis/databases, a shell, ... an interpreter/compiler/programming language..." React hooks would fall under building your own React-ish thing. The Chinese triggers include "自己动手写一个 X、手写 Redis/Git/Shell/Docker/解释器/操作系统、造轮子学原理、build your own x、项目式学习". The user said "我自己写的 useState" — they're building their own React hook. This is arguably a match: they're learning by rebuilding React's useState.

The instruction says: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it."

The user's task is debugging their own useState implementation — a hands-on build-your-own-x style learning task. I think reading the skill is appropriate. It says it "hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution."

Let me read the SKILL.md first.

Actually, let me think about whether this is really a match. The user has a specific bug: state resets on every click because `let state = initial` is inside the component function. The core answer: useState must persist state across renders — store it outside the render closure (module-level variable, or an array indexed by hook order, like React's fiber hooks). Each render call re-executes the component function, so local variables are re-created.

The skill coaching approach would be to guide them rather than dump a solution. Let me read the skill to see what it says.

I should read the SKILL.md first per instructions. Then decide.

Let me do that.The skill is a router for build-your-own-x projects. The user is debugging their own useState implementation. Let me see the category map — there's likely a "framework" or "react" category. Let me read the rest of the file to find the right slug.这对应到 `frontend-framework-library` (react/hooks)。根据技能要求，我必须在指导前先阅读 track skill。Let me read the rest of the file (truncated 669 chars).用户处于里程碑 4（组件 + 状态）。在指导之前，让我先检查一下他们的代码是否在工作区中。工作区里没有代码，所以我直接根据你的描述进行指导。让我先从教程列表中获取规范的参考链接。**位置：** milestone 4/7（Components + state），你卡住的正是这一步的核心概念。

**根因：** 组件函数每次渲染都会被重新调用。函数一执行，`let state = initial` 就重新声明并赋回初始值，上一次的值随旧的作用域一起被丢弃。于是每次点击 → setState 触发重渲染 → 组件函数重新跑一遍 → state 归零。

React 自己也是这么解决的：hooks 的状态存在组件函数外面（fiber 节点上），你的函数组件每次渲染只是被重新调用。参考 [Build your own React](https://pomb.us/build-your-own-react/) 的 useState 章节。

**修法骨架（核心留给你写）：** 状态放到渲染闭包外面，用「hooks 数组 + 调用顺序索引」存取——这正是 React hooks 的模型：

```js
let hooks = [];      // 跨渲染存活
let hookIndex = 0;

function useState(initial) {
  // TODO 1: 读 hooks[hookIndex]，槽位为空时写入 initial
  // TODO 2: setState = (newVal) => { 写回本槽位; scheduleRender(); }
  // TODO 3: 返回 [state, setState]，并把 hookIndex++
}

function render() {
  hookIndex = 0;     // 每次渲染前必须归零
  // ...再调用组件函数
}
```

`render()` 里归零那行是关键：组件里第 N 个 `useState` 永远对应槽位 N，靠的是调用顺序。

**检查点：** 点击 3 次，界面依次显示 1、2、3；`console.log(hooks)` 里只有对应槽位在变。再加第二个 `useState` 验证两个槽位互不干扰；然后试着把一个 `useState` 放进 `if` 分支里，看槽位怎么串——你就明白 React 为什么禁止条件调用 hooks 了。