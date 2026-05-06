# Concepts checklist: 让我们构建一个 Shell！

## Before coding

- Confirm the user's target language and runtime.
- Confirm whether the user wants a learning scaffold, production-quality implementation, or bug fix.
- Inspect existing files if the project is not empty.

## Core concept prompts

Use these questions to guide explanations:

1. What minimal observable behavior proves the project is alive?
2. What are the main domain objects and their invariants?
3. What input format or protocol must be understood?
4. What algorithm, runtime loop, or state transition makes the project useful?
5. What failure modes are common for beginners?
6. What tests can catch regressions without overcomplicating the project?

## Implementation checklist

- [ ] Project builds or runs on the user's machine.
- [ ] First milestone has a visible result.
- [ ] Core data model is documented in code comments or README.
- [ ] At least one automated or scripted verification exists.
- [ ] Debugging guidance explains causes, not only fixes.

## Domain

- Category: Shell
- Language / stack: C
- Source: https://github.com/kamalmarhubi/shell-workshop
