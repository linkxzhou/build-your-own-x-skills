The user wants to build their own spreadsheet engine. This matches the build-your-own-x skill. Let me read the skill file first.The skill file was truncated. Let me read the rest of it.Spreadsheet maps to the `misc` track. Reading that track skill now, as the workflow requires.Now let me find spreadsheet tutorials in the references and check for a matching per-tutorial skill.No spreadsheet entry in the upstream list. Let me check for adjacent keywords to be thorough.No spreadsheet entry exists in the upstream catalog (only a hash-table tutorial matches loosely), so the misc track's generic milestone frame applies. Let me find a real, existing tutorial to anchor the track instead of inventing one.Search is returning nothing in this environment. The misc skill description explicitly names "spreadsheet" as one of its 62 uncategorized entries, so let me check the manifest and catalog directly.The upstream catalog has no spreadsheet entry — closest cousins are data-structure and interpreter tutorials. Since a spreadsheet's formula language is a small interpreter, let me check the programming-language track so I can borrow its coaching when we hit parsing.Spreadsheet engine it is — that's a great one. It's in the skill's map under the `misc` track (package managers, DNS servers, spreadsheets, promises…). I've read the track skill; one honest caveat: the upstream catalog has no spreadsheet-specific tutorial, so we'll use the misc track's milestone frame and borrow the interpreter track's method for the formula language (that part is a small tokenizer → parser → evaluator, same shape as [Crafting Interpreters](https://craftinginterpreters.com/)).

**Where we are:** milestone 1/7 — pick + scope.

**The concept:** a spreadsheet engine is three layers stacked: a cell store (map of `A1` → raw content), a formula interpreter (`=SUM(A1:A3)*2` → value), and a dependency graph that figures out which cells must recompute when one changes, in the right order, detecting cycles. The graph is the part spreadsheets have that plain interpreters skip — it's where the real learning is.

**Proposed target** (default, tell me if you want it different): a headless engine with a REPL/CLI — no GUI at first. It supports numbers, strings, `=formulas` with `+ - * / ^` and comparisons, cell refs (`A1`) and ranges (`A1:B3`), functions `SUM AVG MIN MAX COUNT`, automatic recalculation on edit, and errors `#DIV/0! #REF! #NAME? #CIRC!`.

**Milestones:**

1. Scope + skeleton — project layout, `run` and `test` commands with a placeholder test
2. Cell model + formula tokenizer
3. Parser → AST with correct precedence (`1+2*3` parses as `1+(2*3)`)
4. Evaluator — literals, operators, cell refs (no propagation yet)
5. Dependency graph — topological recompute, cycle detection → `#CIRC!` (the heart)
6. Range functions + edge cases — `#DIV/0!`, `#REF!`, bad names, empty cells
7. Parity check vs a real spreadsheet on a fixture + stretch (incremental recalc, CSV import, or a tiny TUI grid)

Two questions, defaults in parentheses:

1. Which language? (Python — zero setup, or TypeScript if you eventually want a web grid)
2. What do you most want to understand: the formula interpreter, the dependency/recalc engine, or both equally? (both, interpreter first)

**How to check this milestone:** reply with your language pick and a one-sentence definition of done you're happy with — mine would be: *"editing any cell in a 10×10 sheet with chained formulas and one cycle prints correct values for all cells and `#CIRC!` for the cycle."* Once you confirm, I'll scaffold the skeleton and give you the first TODO list.