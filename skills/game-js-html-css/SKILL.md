---
name: game-js-html-css
description: |
  Trigger when the user wants to learn, implement, debug, or extend a build-your-own project for 游戏 using JavaScript. Use when they mention "build your own game", "像程序员一样思考：只用 JS/HTML/CSS 做贪吃蛇", the source URL, or ask for a Claude Code guided implementation plan.

  Guides the user through a project-based learning workflow: inspect prerequisites, create or adapt a minimal project, implement milestones, run verification commands, and debug failures without simply dumping a full finished solution.
---

# 像程序员一样思考：只用 JS/HTML/CSS 做贪吃蛇

Use this skill as a Claude Code project coach for converting the original build-your-own tutorial into an interactive implementation experience.

## Source

- **Category**: 游戏
- **Language / stack**: JavaScript
- **Original resource**: https://medium.freecodecamp.org/think-like-a-programmer-how-to-build-snake-using-only-javascript-html-and-css-7b1479c3339e
- **Original status**: not yet converted in README

## Operating principles

- Prefer learning-by-building: explain the next small concept, then make the smallest useful code change.
- Preserve the user's existing project structure. Inspect files before editing and avoid replacing working code wholesale.
- Use tests, executable examples, or observable outputs at every milestone.
- If the user asks for a full implementation, first offer a staged path and provide complete code only for the current milestone.
- For long tutorials, load only the relevant reference section for the current milestone.

## Workflow

### 1. Establish context

1. Identify whether the user is starting from an empty directory, continuing a partial implementation, or debugging a failing project.
2. Detect the target language/toolchain. Default to **JavaScript** when the user does not specify another stack.
3. Check available build tools and create a minimal runnable project only when needed.
4. Read `references/tutorial-map.md` for the milestone map before planning detailed work.

### 2. Plan milestones

Guide the project through these generic milestones and adapt them to the tutorial:

1. **Project skeleton** — files, build command, first runnable program.
2. **Core data model** — key structs/classes/types and invariants.
3. **Parser or input layer** — commands, file formats, protocol frames, or scene/input handling.
4. **Core algorithm / engine** — the central behavior of the project.
5. **Persistence / networking / rendering / runtime integration** — domain-specific integration.
6. **Testing and diagnostics** — unit tests, golden outputs, fixtures, or manual verification.
7. **Extensions** — performance, robustness, UX, and production-readiness improvements.

### 3. Implement with guardrails

- Before edits, summarize the intended change and files affected.
- Keep patches small enough for the user to understand.
- Explain important design choices and tradeoffs at the point they matter.
- After each edit, run the relevant verification command when available.
- When a command fails, diagnose from the error message and fix the smallest likely cause.

### 4. Debugging mode

When the user provides failing tests, logs, or code:

1. Reproduce or reason about the failure.
2. Identify the milestone and concept involved.
3. Explain the invariant being violated.
4. Apply a minimal fix.
5. Add or update a regression test if appropriate.

## References

- `references/tutorial-map.md` — source-to-milestone conversion map.
- `references/concepts.md` — core concepts and implementation checklist.
- `examples/minimal/README.md` — minimal project scaffold guidance.
- `evals/evals.json` — prompts for validating this skill.

## Expected outputs

Depending on the user's request, produce one of:

- A staged implementation plan.
- A minimal project scaffold.
- A focused code patch for the current milestone.
- A debugging explanation plus fix.
- A test plan and verification commands.
