---
name: web-server-web-defn-2018-02-25
description: |
  Trigger when the user wants to learn, implement, debug, or extend "从零构建 Web 应用" or a Web 服务器 build-your-own project using Python. Use this skill for staged Claude Code guidance, milestone planning, minimal implementation, and troubleshooting.
---

# 从零构建 Web 应用

Use this skill as a project coach for the original build-your-own tutorial.

## Source

- **Category**: Web 服务器
- **Language / stack**: Python
- **Original resource**: https://defn.io/2018/02/25/web-app-from-scratch-01/

## Workflow

1. Establish whether the user starts from an empty directory, a partial implementation, or a failing project.
2. Default to `Python` unless the user chooses another stack.
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
