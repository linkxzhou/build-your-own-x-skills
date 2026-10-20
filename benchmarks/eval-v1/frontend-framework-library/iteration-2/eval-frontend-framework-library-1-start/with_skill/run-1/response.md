The user wants to build their own tiny React to understand it. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.The SKILL.md is truncated. Let me read the rest of it.Topic mapped: react → `frontend-framework-library`. Reading the track skill now (mandatory).There's no `frontend-framework-library/SKILL.md` directly, but there is `frontend-framework-library-jsx-jsx/SKILL.md` which is a per-tutorial skill. Let me check the manifest and see if there's a track skill for frontend-framework-library. Let me glob more specifically.The glob output was truncated. Let me check for the exact track skill directory.Now let me read the tutorials.md reference to pick a guide.The track skill points to pomb.us "Build your own React" as the canonical guide, and there's a per-tutorial skill for it. Let me read that plus check what's available in the environment.Scope is clear from the track skill: JavaScript, no build step, guided by the canonical upstream tutorial [pomb.us — Build your own React](https://pomb.us/build-your-own-react/). Recording the exploration and plan, then scaffolding milestone 1.Directory arg didn't glob. Trying the default discovery mode.**Where we are:** milestone 1/6 — `createElement`. Project scaffolded in `tiny-react/`, following [pomb.us — Build your own React](https://pomb.us/build-your-own-react/).

**The concept:** JSX is sugar. `<div id="a">hi</div>` compiles to a function call `createElement("div", { id: "a" }, "hi")`, and that call's whole job is to return a plain JS object describing the node — type, props, children. React's entire runtime is built on walking these objects. One wrinkle: raw text (`"hi"`, `42`) gets wrapped in a synthetic `TEXT_ELEMENT` so the renderer only ever handles one shape.

**What to write:** the body of `createElement` in `tiny-react/src/createElement.js:21`. Three steps:

1. Build `children` by mapping each argument: string/number → `{ type: TEXT_ELEMENT, props: { nodeValue: child, children: [] } }`, objects pass through as-is.
2. Return `{ type, props: { ...props, children } }`.

**How to check it:**

```
cd tiny-react && node --test
```

Currently 0/3 pass (all fail with `TODO: implement createElement`). You're done when it prints `pass 3`. The tests in `src/createElement.test.js` show the exact expected objects — including the `props: null` case, where JSX passes `null` and your function should still produce a `children` array.

When it's green, tell me and we'll move to milestone 2: `render` — turning that object tree into real DOM nodes.