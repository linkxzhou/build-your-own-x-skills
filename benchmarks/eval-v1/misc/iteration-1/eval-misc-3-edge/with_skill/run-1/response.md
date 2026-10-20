The user wants to build their own spreadsheet engine. This matches the build-your-own-x skill. Let me read the skill first.The skill file is truncated. Let me read the rest of it, and also check the skills directory for a spreadsheet-related track.Spreadsheet maps to the `misc` track. Reading that skill now.No spreadsheet entry in the misc tutorial list. Let me check the manifest and the full tutorials list to confirm what's available.The misc track has 62 upstream entries and none is a spreadsheet engine, so I'll structure the milestones myself. Let me find a credible tutorial to anchor the track.Web search is returning nothing. Let me try fetching a search endpoint directly.DuckDuckGo HTML is bot-gated. Trying the lite endpoint and Bing.Two promising hits. Let me verify their content quality.The blogspot one is a LeetCode-style toy; the paulserban.eu one is a design overview. Let me check the `programming-language` track (a spreadsheet engine is an interpreter plus a dependency graph) and try one more search for a stronger anchor.The hjalli.com post looks like the strongest anchor. Verifying its content.Spreadsheet engine it is — good pick: it's an interpreter (formula language) fused with a live dependency graph, so you learn parsing, evaluation, and incremental recomputation in one project.

**Where we are:** milestone 1/7 — scope.

**The track:** spreadsheets sit in the `misc` category of build-your-own-x, which has no dedicated spreadsheet tutorial. The best anchor I found is from people who actually shipped one: **"We built a spreadsheet engine from scratch. Here's what we learned."** — Hjálmar Gíslason (GRID), https://hjalli.com/posts/we-built-a-spreadsheet-engine-from-scratch-heres-what-we-learned/ — plus the parser/evaluator coaching frame from the `programming-language` track. We'll follow the article's architecture: sparse cell store → formula parser → dependency graph → recalculation.

**The plan** (each milestone ends with a runnable check):

| # | Milestone | Checkpoint |
|---|---|---|
| 1 | Scope + skeleton: REPL, test harness | `set A1 5` / `get A1` → 5; `test` runs |
| 2 | Core data model: sparse cells, raw content (number / text / `=formula`) | unit tests for set/get/reset pass |
| 3 | Tokenizer + parser for `=A1+B2*3` (precedence, refs, ranges) | `=1+2*3` parses as `1+(2*3)`; round-trip prints back |
| 4 | Evaluator: literals, refs, `+ - * /`, `SUM`, `IF` | end-to-end: `=A1+B1*2` computes |
| 5 | Dependency graph + recalculation: extract refs, topo order, dirty propagation | change `A1` → `B1==A1+1` and `C1==B1*2` update |
| 6 | Edge cases: circular refs → `#CYCLE!`, syntax errors → `#ERROR`, div/0 | 3 failure-mode tests pass |
| 7 | Parity + stretch: match Excel on a fixture; ranges, incremental recalc | fixture output matches Excel/Sheets |

Two questions before we start, with defaults so you can just say "go":

1. **Language?** Default: Python — zero setup, and the parser concepts transfer anywhere. Tell me if you'd rather use Go, Rust, JS, or C.
2. **Headless or UI?** Default: headless engine with a REPL — the interesting parts are the parser and the dependency graph; a grid UI is a stretch goal, not the core.

Confirm (or override) and I'll scaffold milestone 1 in your workspace.