The user wants to learn Redux, not React. They want to build Redux from scratch. This matches the build-your-own-x skill — specifically the "build your own" category. Let me read the skill first as instructed.

The skill says: read SKILL.md BEFORE doing anything else when the task matches. The task matches: "build your own" a library (Redux is a state management library — likely there's a sub-skill or the entry point handles it).

Let me read the skill file.The file is truncated. Let me read the rest of it, and also check the category map for Redux. Redux is a state management library — likely falls under some category. Let me read the rest of the SKILL.md and check the skills directory.Redux maps to the `frontend-framework-library` track. Reading that skill now, plus checking for a Redux-specific tutorial skill.The track skill has a Redux-specific sub-skill. Reading it plus the rest of the track skill.Let me read the rest of the redux skill and the tutorial-map.md reference.Yes — Redux is fully decoupled from React. The core is a tiny, framework-agnostic state container (~50 lines in the real library), and it's a great standalone build. Let me check the workspace and available tooling before we agree on scope.Yes — Redux is a standalone state container; React-Redux is just an optional binding layer on top. The core (`createStore`, `dispatch`, `subscribe`, middleware) is ~50 lines of framework-agnostic JavaScript, so we can build all of it with zero React.

Let me record the exploration state and pull up the upstream tutorial we'll follow.The fetch caught mostly page chrome. Let me pull the article body with a larger window.Mostly nav chrome. Let me grab the full body with a bigger window.The extractor keeps grabbing nav. Let me pull the raw HTML and extract the article body directly.Good — got the article body. Let me see the rest to map the full tutorial structure.I have the full tutorial mapped now. Setting up the project plan before scaffolding.The empty test dir confuses Node's runner. I'll drop a placeholder test file so the scaffold runs clean.Interesting — Node v25.8.0 seems to treat `node --test test/` differently. In newer Node versions, `node --test <dir>` should work. But the error says "Cannot find module .../test" — it's trying to load `test` as a module entry point. Hmm, in Node 25, maybe the CLI arg parsing changed: `node --test test/` — the `test/` positional arg is being treated as the main module to run rather than a test glob?

Actually in newer Node versions, `node --test` runs test files found by default (matching `**/*.test.js` etc.), and positional args are entry points. Let me try `node --test` without the dir arg, or `node --test "test/*.test.js"` or `node --test test/scaffold.test.js`.

Actually the issue: `node --test test/` with trailing slash — Node tries to require the directory as a module? In older Node, `node --test <dir>` scans the dir. Let me just try variations.`node --test` with no args auto-discovers and passes. Updating the script.Scaffold is green. Now Milestone 1 — the concept, the skeleton, and the checkpoint. You write the core.

**Where we are:** Milestone 1/7 — Actions + pure reducer.

**The concept (short):** Redux state is a plain JS object. Changes happen through *actions* — plain objects with a `type` — and a *reducer*: a pure function `(state, action) → nextState` that never mutates. Same actions in, same state out; that's what makes replay/time-travel possible. The name "reducer" is literal: `actions.reduce(reducer, undefined)` produces the final state.

**Your task** — create two files:

`src/constants.js` — action type constants (constants over strings so typos throw instead of silently no-op):
```js
export const CREATE_NOTE = 'CREATE_NOTE';
export const UPDATE_NOTE = 'UPDATE_NOTE';
```

`src/reducer.js` — the note-app reducer, immutable updates only:
```js
import { CREATE_NOTE, UPDATE_NOTE } from './constants.js';

const initialState = {
  nextNoteId: 1,
  notes: {},
};

// TODO: implement. Rules:
// 1. state = initialState via default param (Redux passes undefined first)
// 2. CREATE_NOTE: add { id, content: '' } under state.nextNoteId, bump nextNoteId
// 3. UPDATE_NOTE: replace note action.id's content, keep everything else shared
// 4. default: return state unchanged
// Never mutate. Shallow-copy with spread: { ...state, notes: { ...state.notes, [id]: newNote } }
export const reducer = (state, action) => {
  // your code here
};
```

**Checkpoint:** I've written the tests — `test/reducer.test.js`:Scaffold is green (`npm test` passes). Milestone 1 is set up — now it's your turn.

**Where we are:** Milestone 1/7 — Actions + pure reducer.

**The concept:** Redux state is a plain JS object. Changes are described by *actions* (plain objects with a `type`), and a *reducer* — a pure function `(state, action) → nextState` — computes each new state from the old one. Purity is the whole trick: same actions in, same state out, which is what makes replay and time-travel possible later. The name is literal — `actions.reduce(reducer, undefined)` walks the whole history to the final state.

**What to write** — two files:

`src/constants.js`:
```js
export const CREATE_NOTE = 'CREATE_NOTE';
export const UPDATE_NOTE = 'UPDATE_NOTE';
```

`src/reducer.js` — implement the reducer:
```js
import { CREATE_NOTE, UPDATE_NOTE } from './constants.js';

const initialState = { nextNoteId: 1, notes: {} };

// Rules:
// 1. default param: state = initialState (Redux passes undefined on the first call)
// 2. CREATE_NOTE → add { id, content: '' } under state.nextNoteId, bump nextNoteId
// 3. UPDATE_NOTE → new note object with action.content, everything else shared
// 4. default → return state as-is
// Never mutate: shallow-copy with spread, e.g. { ...state, notes: { ...state.notes, [id]: newNote } }
export const reducer = (state, action) => {
  // your code here
};
```

**Checkpoint:** `npm test` — the 5 tests in `test/reducer.test.js` must pass. They cover boot-from-undefined, immutable update, identity-preservation on unknown actions, replay determinism, and no-mutation. Right now 1 fails (the reducer is empty) — that's your target.

Write the reducer, run `npm test`, and paste any failure output here. Once it's green I'll log it in `PROGRESS.md` and we move to Milestone 2: `createStore` — the object that actually holds the state and runs that reducer for you.