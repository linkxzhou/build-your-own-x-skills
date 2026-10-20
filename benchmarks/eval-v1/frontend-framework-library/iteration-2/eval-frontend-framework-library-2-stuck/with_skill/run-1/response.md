The user is asking about their own useState implementation. They wrote `let state = initial` inside the component function, so every render the state resets to initial. This is a classic build-your-own-x React hooks question — the skill "build-your-own-x" matches: "my own X is buggy" — specifically "我自己写的 useState" — this is a from-scratch implementation debugging question. The skill instructions say: when the task matches a skill's description, read that skill's SKILL.md BEFORE doing anything else.

So I should read `.agents/skills/build-your-own-x/SKILL.md` first.The file is truncated. Let me read the rest of it, and also find the track skill for React/hooks. The topic is "自己写的 useState" — a React hooks implementation. Let me check the skills directory for a matching track.主题映射到 `frontend-framework-library`。正在读取轨道技能（入口技能要求必读）：The learner is stuck mid-way (debugging turn). The skill says: "When the learner is stuck mid-way, still read the track skill first, give the minimal fix, and end with a runnable check (command + expected output)."

The bug: they wrote `let state = initial` inside the component function. Every render re-executes the component function, so `state` is re-initialized to `initial`. The fix: move state outside the component function — a closure/module-level variable (or index-based hooks array). Minimal fix: hoist the state variable outside the component so it persists across renders.

The coaching rules: give the minimal fix, one hint at a time, end with a runnable check (command + expected output). Don't dump a full solution. The learner has tried (they have code). Debugging turn: minimal fix is fine.

Should I look at their workspace code? The user didn't give a file path. Let me check if there's code in the workspace. Let me glob for js/jsx/html files. That would let me give a precise minimal fix. Let me search.

Also per output format for each turn:
- Where we are: milestone 4/7 (Components + state)
- The concept: short
- What to write next: skeleton/TODO, not full answer
- How to check it: command + expected output
- Stuck? One hint at a time.

Let me look for their code in the workspace first.**进度：里程碑 4/7（Components + state）— 调试回合**

**概念（为什么会重置）：** 组件函数每次渲染都会重新执行。函数里的 `let state = initial` 是局部变量，每次执行都重新创建并赋回 `initial`，所以 setState 后虽然触发了重渲染，新渲染里读到的又是初始值。状态必须存在组件函数之外、能跨渲染存活的地方——React 自己就是把 hook 状态挂在 fiber 节点上（在你的函数外面）。

**最小修复（一个提示）：** 把 `state` 提到组件函数外面（模块作用域或闭包），只在第一次初始化：

```js
// 组件函数外面
let state;
let initialized = false;

function useState(initial) {
  if (!initialized) {
    state = initial;      // 只在首次渲染赋值
    initialized = true;
  }
  const setState = (next) => {
    state = next;
    render();             // TODO: 接上你已有的重渲染入口
  };
  return [state, setState];
}
```

你的组件函数保持原样，只把 `let state = initial` 那行删掉，改用 `const [count, setCount] = useState(0)`。

**怎么验证：** 打开你的 `index.html`，点按钮 3 次，并在 `setState` 里临时加一行 `console.log(state)`。

预期输出：

```
1
2
3
```

页面上计数器显示 `3` 且继续递增。如果 console 输出对了但页面不变，问题在 `render()` 没被调用——那是下一个要查的点。

一个预告：这个写法只支持单个 `useState`。多个 hook 时要换成「hooks 数组 + 游标 index」的存法，那是本里程碑的下一步。