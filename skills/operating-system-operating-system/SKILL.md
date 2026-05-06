---
name: operating-system-operating-system
description: |
  Trigger when the user wants to learn, implement, debug, or extend "操作系统开发小书" or a 操作系统 build-your-own project using C. Use this skill for staged Claude Code guidance, milestone planning, minimal implementation, and troubleshooting.
---

# 操作系统开发小书

Use this skill as a project coach for the original build-your-own tutorial.

## Source

- **Category**: 操作系统
- **Language / stack**: C
- **Original resource**: https://littleosbook.github.io/

## Workflow

1. Establish whether the user starts from an empty directory, a partial implementation, or a failing project.
2. Default to `C` unless the user chooses another stack.
3. Read `references/tutorial-map.md` and convert the source into 4-8 implementation milestones.
4. Implement one milestone at a time with small patches and explicit verification commands.
5. Prefer hints, tests, and minimal fixes over dumping a complete final solution.
6. Preserve the user's existing files and style.

## Milestone template

1. Project skeleton and first runnable command.
2. Core data model and invariants.
3. Input/parser/protocol/UI boundary.
4. Main algorithm or runtime engine.
5. Integration and end-to-end behavior.
6. Diagnostics, tests, and extensions.

## Expected outputs

- A staged implementation plan.
- A minimal project scaffold.
- A focused code patch for the current milestone.
- A debugging explanation and regression test.
