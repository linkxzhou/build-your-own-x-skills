The user wants to learn Redux by building it from scratch, without React. This matches the build-your-own-x skill. Let me read the skill first.The skill file was truncated. Let me read the rest of it, and also look for the track skills directory to find the right category for Redux. Redux is a state management library — it might fall under a category like "Build your own React" or maybe there's a specific one. Let me check the skills directory.Redux maps to the `frontend-framework-library` track. Let me read that skill and check for a Redux-specific tutorial skill.There's a Redux-specific skill. Let me read it plus the rest of the track skill.Let me read the rest of the redux skill and the tutorial-map.md reference.The Redux track is clear. Let me check the workspace state and the tutorial list before proposing scope.Yes — Redux is a standalone library; React-Redux is just a binding layer on top. Building Redux alone is the cleaner way to learn it, and it's one of the curated tracks in this repo's build-your-own-x catalog (`frontend-framework-library-redux`, based on Zapier's [_Build Yourself a Redux_](https://zapier.com/engineering/how-to-build-redux/)).

Node v25 is already in your environment, so I propose this scope — zero installs, no build step:

**Target:** a mini-Redux in plain JavaScript with `createStore`, `combineReducers`, `applyMiddleware`, plus a vanilla-DOM todo app at the end to prove the store drives a UI with no React in sight.

**Milestones** (each ends with a runnable check via Node's built-in `node:test` runner):

| # | Milestone | Concepts | Checkpoint |
|---|---|---|---|
| 1 | `createStore` core | `getState`, `dispatch`, `subscribe`, listener set | counter test: dispatch increments state, listener fires |
| 2 | Reducer conventions | pure functions, initial state, unknown-action default | todo reducer unit tests |
| 3 | `combineReducers` | state slices, shape validation | two reducers merge into one state tree |
| 4 | `applyMiddleware` | middleware chain, `next`, thunks | logger middleware prints; async action resolves |
| 5 | Time travel | state history, undo | undo restores previous state |
| 6 | Vanilla-DOM app | subscribe → render, no framework | clicking a button updates the DOM via the store |

Two quick confirmations, with defaults so you can just say "go":

1. **JavaScript** (default) or TypeScript?
2. End with the vanilla-DOM app (default) or stop at the library + tests?

Once you confirm, we start milestone 1: I'll scaffold `mini-redux/` with a test file, and you write the ~15 lines of `createStore`. The check we'll run from then on:

```
node --test
```

Expected at milestone 1: `pass 3` — dispatch updates state, `getState` returns it, subscriber was called.