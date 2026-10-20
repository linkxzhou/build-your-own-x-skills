The user says "Something not in your list: I want to build my own spreadsheet engine." This looks like a reference to the "build-your-own-x" repository — the workspace is named "build-your-own-x-misc-3". The user wants to build their own spreadsheet engine, and presumably wants guidance/resources on how to do it, possibly similar to the "build your own X" list format.

Let me explore the workspace to understand the context. There may be a README listing things, and the user is saying "spreadsheet engine" is something not in the list. Maybe they want me to add it to the list, or create a guide for building a spreadsheet engine.

Let me look at the workspace first.The workspace is empty. So the user wants to build their own spreadsheet engine — this is a "build your own X" style request. The workspace name suggests "build-your-own-x-misc-3" — likely an eval scenario where the user asks for a guide on building something (like the build-your-own-x list). Since the workspace is empty, I should create a guide/tutorial for building a spreadsheet engine.

Given the context ("Something not in your list"), the user probably wants a "Build your own Spreadsheet Engine" guide — a tutorial document explaining how to build a spreadsheet engine from scratch, similar to the build-your-own-x repo style (which links to tutorials). But since this is "misc-3" and empty, the best deliverable is probably a comprehensive guide document in the workspace.

Let me think about what a good deliverable is:
1. A README.md guide: "Build your own Spreadsheet Engine" — covering architecture, formula parsing, dependency graph, recalculation, etc.
2. Possibly a working minimal implementation in code (e.g., Python or TypeScript) demonstrating the engine.

The user said "I want to build my own spreadsheet engine." The most helpful response: provide a structured guide + a minimal working implementation they can build on. Given the "build-your-own-x" theme, a tutorial-style README with a working reference implementation would be ideal.

Let me plan:
- Create a plan
- Write a README.md with the guide (architecture, steps)
- Implement a minimal but real spreadsheet engine (e.g., Python) with:
  - Cell addressing (A1 notation)
  - Formula parser (tokenizer + recursive descent / Pratt parser)
  - Dependency graph (DAG), topological sort for evaluation order
  - Cycle detection
  - Recalculation on edit (dirty marking)
  - Functions: SUM, AVG, MIN, MAX, COUNT
  - Ranges (A1:B3)
  - Tests

That's a solid deliverable. Let me check the build-your-own-x repo conventions — it's a list of links to tutorials. But since the user says "I want to build my own spreadsheet engine", they want to actually build one. I'll create a guide + working code.

Let me use the explore/plan tools as instructed. First explore (record), then plan, then execute.

Actually the instructions say: "Before modifying code, call `explore` once to record the files you have read (or intend to read)". The workspace is empty, so exploration is trivial. Let me call explore, then plan, then implement.

Design of the engine (Python, single file + tests, or small package):

Core concepts:
1. **Model**: `Sheet` holds cells keyed by (row, col) or "A1" string. Each cell has either a literal (number/string) or a formula (string starting with `=`).
2. **Tokenizer**: numbers, identifiers (cell refs, function names), operators (+ - * / ^ % & = <> < > <= >=), parens, commas, colons, strings.
3. **Parser**: Pratt/recursive-descent producing AST: Number, String, CellRef, Range, Unary, Binary, Call.
4. **Dependency extraction**: walk AST to collect CellRef/Range deps.
5. **Graph**: deps map cell -> set of dependents. On set(), mark dirty (transitively), recompute in topological order, detect cycles.
6. **Evaluation**: evaluate AST; ranges expand to cell values; functions SUM/AVERAGE/MIN/MAX/COUNT/COUNTA/IF/ABS/ROUND. Error values: #REF!, #CYCLE!, #DIV/0!, #VALUE!, #NAME?.
7. **API**: `sheet.set("A1", "10")`, `sheet.set("A2", "=A1*2")`, `sheet.get("A2")` -> 20. `sheet.display()` grid.

Also handle:
- String literals in formulas ("hello")
- Comparison operators returning TRUE/FALSE
- Empty cell = 0 in arithmetic
- Cycle detection: mark cells in cycle with #CYCLE!

Tests: pytest or plain asserts. I'll write a test file with plain asserts runnable via python, or use pytest style. Plain `python -m unittest` or simple asserts with a main runner keeps dependencies zero. I'll use pytest-style functions but with a simple runner fallback... Better: use `unittest` so it runs with zero deps.

Deliverables:
- `README.md` — the guide: how to build it, architecture, step-by-step, extension ideas.
- `spreadsheet.py` — the engine (single file, ~300-400 lines, well commented).
- `test_spreadsheet.py` — unittest tests.
- Maybe `demo.py` — small demo. Could fold into README examples. Keep it minimal: README + engine + tests.

Let me write the plan and execute. I should keep the code high quality and correct. Let me carefully design the implementation.

Key implementation details:

```python
# Cell reference parsing: A1, $A$1 (support $ optionally), ranges A1:B2
```

Tokenizer tokens: NUMBER, STRING, IDENT (could be cell ref or func name or TRUE/FALSE), OP, LPAREN, RPAREN, COMMA, COLON.

Distinguishing cell refs from identifiers: regex `^\$?[A-Za-z]{1,3}\$?[0-9]+$` → cell ref. TRUE/FALSE → boolean literals. Otherwise function name (must be followed by `(`).

Parser precedence (Excel-like):
1. `:` range (handled in primary)
2. unary minus/plus
3. `%` postfix (maybe skip percent to keep simple — but nice to have; I'll include postfix %)
4. `^` (right assoc in Excel; actually Excel is left-assoc for ^... Excel treats ^ as left-associative. I'll do left-assoc.)
5. `* /`
6. `+ -`
7. `&` concat
8. comparisons `= <> < > <= >=`

Evaluation:
- Values: float/int, str, bool, error objects (ErrorVal), None (empty).
- Arithmetic: coerce empty→0, bool→1/0, numeric string→number else #VALUE!.
- `&` concat: coerce to text.
- Comparisons: numbers compare numerically, strings lexicographically (case-insensitive like Excel? keep case-sensitive simple... Excel is case-insensitive for =. I'll do case-insensitive for string equality to match Excel, or keep simple. I'll do case-insensitive since it's Excel-like, note in README).

Hmm, keep it simple but correct. I'll implement case-insensitive string comparison like Excel.

Dependency graph & recalculation:
- `self._formulas: dict[key, str]` raw formula text
- `self._ast: dict[key, Node]`
- `self._deps: dict[key, set[key]]` — cells this cell depends on (expand ranges to concrete cells? Ranges can be large; for a toy engine, expand ranges to concrete cells but cap... For simplicity expand ranges; note limitation in README).
- `self._dependents: dict[key, set[key]]` reverse edges.
- `self._values: dict[key, value]` cached evaluated values.
- `set(addr, raw)`: parse; update deps; mark dirty: the cell + all transitive dependents; recompute dirty set in topo order (Kahn on subgraph induced by dirty set); if cycle remains (nodes with indegree>0), evaluate them to #CYCLE!.
- `get(addr)`: return value (error object or python value).
- `display()`: grid of formatted values.

Cycle detection nuance: a cell that references itself directly or indirectly. Kahn's algorithm on the dirty subgraph: compute in-degrees from deps within dirty set; process; leftover nodes are in cycles → set #CYCLE!.

Also cells depending on a cycle cell: they're also leftover (since their dep never resolves) → they'd also get #CYCLE!? In Excel, dependents of circular refs show 0. Simpler: leftover nodes all get #CYCLE!. That's acceptable and documented.

Edge: when a formula is replaced by a literal, remove old deps.

Edge: setting a cell to empty string "" clears the cell.

Functions: SUM, AVERAGE, MIN, MAX, COUNT, COUNTA, IF, ABS, ROUND, SQRT, POWER, CONCAT? Keep: SUM, AVERAGE, MIN, MAX, COUNT, COUNTA, IF, ABS, ROUND. Range args flatten to values of cells in range (skip empties for SUM etc.; COUNTA counts non-empty).

Errors propagate: any error argument → return that error (except COUNT/COUNTA? In Excel COUNT ignores errors... keep simple: propagate errors except IF condition error propagates too. I'll propagate for all — document it).

Number formatting in display: ints without decimal point, floats as-is, errors as their code.

A1 parsing: `parse_addr("B3") -> (row, col)` 0-indexed internally. `format_addr((row,col))`.

Column letters: A=0... Z=25, AA=26...

Now the README guide structure (build-your-own-x style):
1. What we're building (features list)
2. Core concepts: model, parser, dependency graph, recalculation
3. Step-by-step: each step maps to code sections
4. Architecture diagram (ASCII)
5. How to run tests / demo
6. Exercises / extensions (undo/redo, VLOOKUP, iterative calc, lazy dirty propagation, spill ranges, multi-sheet)

Let me now write the code carefully.

```python
"""A minimal but real spreadsheet engine.

... docstring ...
"""
from __future__ import annotations
import re

class SpreadsheetError(Exception): ...
```

Error values as sentinel class:

```python
class ErrorVal:
    __slots__ = ("code",)
    def __init__(self, code): self.code = code
    def __repr__(self): return self.code
    def __eq__(self, other): return isinstance(other, ErrorVal) and other.code == self.code
    def __hash__(self): return hash(("ErrorVal", self.code))

ERR_REF = lambda: ErrorVal("#REF!")  # or just instances
```

Simpler: module-level singletons `ERR_VALUE = ErrorVal("#VALUE!")` etc. Errors are immutable so singletons fine.

Tokenizer:

```python
TOKEN_RE = re.compile(r"""
    \s*(?:
      (?P<number>\d+(\.\d+)?([eE][+-]?\d+)?)
    | (?P<string>"(?:[^"]|"")*")
    | (?P<ident>[A-Za-z_][A-Za-z0-9_.]*)
    | (?P<op><>|<=|>=|[=<>+\-*/^%&(),:])
    )""", re.VERBOSE)
```

Wait: cell refs like `A1` match ident (starts with letter, contains digits) — fine, classify later. `$A$1` — `$` not in ident pattern. Support `$`? Skip `$` absolute refs to keep tokenizer simple; document as extension. Actually many users type $A$1... but for a teaching engine, plain A1 is fine; note in README.

Token stream: list of (kind, value). Kinds: NUMBER, STRING, IDENT, OP, LPAREN, RPAREN, COMMA, COLON. Actually LPAREN etc. are in op group; classify by value.

Parser (recursive descent):

```
expr        := comparison
comparison  := concat (( = | <> | < | > | <= | >= ) concat)*
concat      := additive ( & additive )*
additive    := multiplicative (( + | - ) multiplicative)*
multiplicative := power (( * | / ) power)*
power       := unary ( ^ unary )*        # left-assoc like Excel
unary       := ( + | - ) unary | postfix
postfix     := primary ( % )*
primary     := NUMBER | STRING | TRUE | FALSE | funcall | cellref[:cellref] | ( expr )
funcall     := IDENT ( arglist? )
arglist     := expr (, expr)*
```

Range in primary: after parsing a cellref, if next token is `:`, parse another cellref → Range node. (Excel allows ranges only in specific spots; this is fine.)

AST nodes as tuples or small classes. Tuples are compact: `("num", 3.0)`, `("str", "x")`, `("bool", True)`, `("cell", (row,col))`, `("range", (r1,c1), (r2,c2))`, `("un", op, node)`, `("bin", op, l, r)`, `("call", name, [args])`, `("post", "%", node)`. Tuples keep it short; classes are clearer. I'll use tuples with a comment header — teaching code, tuples with doc are fine and compact. Hmm, readability... I'll use small dataclass-free classes? Tuples are fine and idiomatic for toy interpreters. Go with tuples.

Deps extraction: walk tuple tree; for "cell" add addr; for "range" add all cells in rectangle.

Evaluation:

```python
def _eval(self, node, visiting) -> value
```

Cell eval: check cache `self._values`; if missing compute. But we precompute in topo order on set(), so eval only walks AST with `self._values.get(addr)` for cell refs; if a referenced cell has no value (empty), return None (empty). If referenced cell is a formula whose value is an error, propagate.

Wait — during recalc we compute all dirty cells in topo order, so deps are fresh. Cell ref eval = `self._values.get(addr)` (None if empty). Good, no recursion needed. But careful: a formula referencing a cell that was never set → None → coerced to 0 in arithmetic, "" in concat, skipped in SUM.

Coercions:

```python
def to_number(v):
    if v is None: return 0.0
    if isinstance(v, bool): return 1.0 if v else 0.0
    if isinstance(v, (int, float)): return float(v)
    if isinstance(v, str):
        try: return float(v.strip())  # Excel would need parseable; else #VALUE!
        except ValueError: return ERR_VALUE
    if isinstance(v, ErrorVal): return v
    return ERR_VALUE

def to_text(v):
    if v is None: return ""
    if isinstance(v, bool): return "TRUE" if v else "FALSE"
    if isinstance(v, ErrorVal): return v.code
    if isinstance(v, float) and v.is_integer(): return str(int(v))
    return str(v)
```

Binary ops:
- `+ - * / ^`: to_number both; error → return it; `/` zero → #DIV/0!; `^` 0^0? Excel returns #NUM!. Use `**` and catch. Negative base fractional exponent → complex → #NUM!.
- `&`: to_text both.
- comparisons: if both numeric-ish (numbers/bools/None?) — Excel: empty compares as 0 vs numbers, "" vs strings. Simplify: coerce: if both sides can be numbers (number, bool, None, numeric string?) hmm. Excel: "10" (text) > 9 (number) is TRUE because text > number always. That's subtle. Simplify: try to_number both; if both succeed → numeric compare; else to_text both → case-insensitive compare. Document simplification. `=`/`<>` same path.

Functions:
- SUM(args...): flatten; each arg: range → iterate cells (skip None); scalar → include. Sum numbers; strings that look numeric? Excel SUM ignores text in ranges but coerces direct args. Simplify: skip non-numeric (None, strings, bools? Excel coerces bools in direct args). Keep: skip None and non-numeric strings; include numbers; bools→1/0? Excel SUM(TRUE)=1 direct. Simplify: include numbers only, skip everything else, propagate errors. Document.
- AVERAGE: sum/count of included numbers; count==0 → #DIV/0!.
- MIN/MAX: over included numbers; empty → 0.
- COUNT: count numbers (in ranges: numbers only; direct numeric args count).
- COUNTA: count non-empty.
- IF(cond, a, b=FALSE?): cond to_number != 0 → a else b; lazy eval? Eager is simpler; but IF with error in untaken branch would propagate — Excel doesn't. Implement IF lazily: special-case in eval before evaluating args. Yes, special-case IF for lazy branches — good teaching point.
- ABS, ROUND(x, digits=0), SQRT (neg → #NUM!), POWER.

Range expansion: `iter_range((r1,c1),(r2,c2))` normalize min/max.

Sheet API:

```python
class Sheet:
    def __init__(self): ...
    def set(self, addr, raw): ...
    def get(self, addr): ...   # returns value or None
    def get_raw(self, addr): ...
    def display(self, rows=?, cols=?) -> str
```

`set`:
1. key = parse_addr
2. raw None or "" → clear: remove formula/ast/deps/value; propagate to dependents (mark dirty & recompute).
3. raw starts with "=" → formula: parse (raise on syntax error? Excel rejects the entry. For engine: raise FormulaError with message — good teaching). Update deps diff, store ast, mark dirty cell+dependents, recompute.
4. else literal: try number → float/int; TRUE/FALSE → bool; else string. Store, remove deps, mark dirty+dependents, recompute.

Recompute:

```python
def _recalc(self, dirty: set):
    # subgraph: nodes in dirty; edges dep->dependent where both in dirty
    indeg = {n: 0 for n in dirty}
    for n in dirty:
        for d in self._deps.get(n, ()):
            if d in indeg: indeg[n] += 1  # wait direction
```

Careful: edge from dep to dependent. n depends on d. Topo order: evaluate d before n. Kahn: indegree[n] = number of deps of n that are in dirty. Queue nodes with 0. Pop u, for each dependent v of u in dirty: indeg[v] -= 1; if 0 → push. Evaluate u when popped: `self._values[u] = self._eval(self._ast[u])` if formula else keep literal (literals already stored in _values).

Leftover (indeg>0 after loop): in cycle or downstream of cycle → set value ERR_CYCLE for formula cells.

Need `self._dependents` reverse map maintained on dep changes.

Dep update diff:

```python
new_deps = collect(ast)
old = self._deps.get(key, set())
for d in old - new_deps: self._dependents[d].discard(key)
for d in new_deps - old: self._dependents[d].add(key)
self._deps[key] = new_deps
```

Dirty marking:

```python
def _mark_dirty(self, key):
    seen = set(); stack=[key]
    while stack:
        k = stack.pop()
        if k in seen: continue
        seen.add(k)
        stack.extend(self._dependents.get(k, ()))
    return seen
```

Also when clearing deps of a cell (literal now), dependents still need recompute — they're in dirty via _dependents of key (key may have no dependents entry; fine).

get(addr): parse; return self._values.get(key) — None for empty. For display, format.

display(): compute used bounding box of set cells (or given rows/cols), print grid with column letters header, values via to_text-ish formatting; errors as code; empty as "".

Formula parse errors: raise `FormulaError("...")` from set() — user sees message. Document.

Also `parse_addr` raising on bad address: `ValueError`.

Number literal in cell: "10" → 10 (int? float). Store numbers as float internally, display ints without .0. Actually keep int when integral for cleaner display; simpler: store float, format on display. But get() returning 20.0 vs 20 — tests use == so 20.0 == 20 fine. Display formats integral floats as int. OK.

Percent postfix: `50%` → 0.5. Implement in eval: ("post","%",node) → to_number/100.

Unary minus: to_number, negate.

Now tests (unittest):
- literals & arithmetic
- precedence: =2+3*4 → 14; =(2+3)*4 → 20; =2^3^2 → 64 (left-assoc: (2^3)^2=64)
- unary: =-A1
- percent: =50% → 0.5
- strings & concat: ="a"&"b" → "ab"; =A1&"!" 
- comparisons: =1<2 → TRUE; ="abc"="ABC" → TRUE (case-insensitive)
- refs: chain A1→A2→A3; recompute on change
- ranges: =SUM(A1:A3); =AVERAGE, MIN, MAX, COUNT, COUNTA
- functions: IF lazy (IF(TRUE,1,1/0) → 1), ABS, ROUND, SQRT, POWER
- errors: =1/0 → #DIV/0!; =SQRT(-1) → #NUM!; =foo(1) → #NAME?; =A1+... unknown? unknown cell is empty→0, fine. =NOPE+1 → #NAME?.
- error propagation: B1==1/0, C1==B1+1 → #DIV/0!
- cycles: A1==A1; A1==B1, B1==A1; dependent of cycle → #CYCLE!
- recovery: fix cycle → values correct
- dep updates: A2==A1*2; change A2 to literal; change A1 → A2 unchanged
- clear cell: set("") → dependents recompute to 0-based
- parse error: set("A1", "=1+") raises FormulaError
- display: grid output contains header and values

Demo in README.

Also a `demo.py`? README examples suffice; but a tiny `demo.py` is nice for instant gratification. I'll include a short one — actually keep file count minimal: README.md, spreadsheet.py, test_spreadsheet.py. README includes a REPL/demo snippet. Good.

Now write everything. Let me be careful with the parser code.

Tokenizer detail: `<>` before `<`; `<=` before `<`. In regex alternation order: `<>|<=|>=|[=<>+\-*/^%&(),:]` — good.

Number regex: `\d+(\.\d+)?([eE][+-]?\d+)?` — also `.5`? Excel accepts `.5`. Add `(\d+(\.\d+)?|\.\d+)`. Keep `\d+\.?\d*` simpler: `\d+(?:\.\d+)?(?:[eE][+-]?\d+)?`. Fine.

Ident: `[A-Za-z_][A-Za-z0-9_]*` — cell refs A1, functions SUM, TRUE/FALSE. Dots not needed.

Classify ident: upper == TRUE/FALSE → bool literal; cell-ref regex → cell; else function name (expect LPAREN next, else #NAME? at eval — better: parser error "unknown name"? Excel parses =foo as name error at eval. Parser: if ident not followed by `(` and not cell/bool → parse error "Unknown name". Simpler and clearer. But then =foo+1 raises on set. Excel would accept and show #NAME?. For teaching, raising FormulaError("Unknown name 'foo'") at set() is fine and testable. Hmm, but I listed test "=foo(1) → #NAME?" — function call to unknown function: parse OK (IDENT + LPAREN), eval → #NAME?. Keep that. Bare unknown ident → FormulaError at set. Both documented.

Wait, careful: cell-ref regex `^[A-Za-z]{1,3}\d+$` — "SUM" no digits → not cell. "A1" yes. "LOG10"? has digits at end → LOG10 matches cell-ref regex? L-O-G = 3 letters, "10" digits → yes! LOG10 would parse as cell ref LOG10 (col LOG, row 10). That's actually how Excel works too (LOG10 without parens is a #NAME?... actually Excel treats LOG10 as name). Edge case, ignore — document that 1-3-letter+digit idents are cell refs.

Column letters to index: 

```python
def col_to_index(letters):
    n = 0
    for ch in letters.upper(): n = n*26 + (ord(ch)-64)
    return n-1
```

parse_addr: regex `^([A-Za-z]{1,3})(\d+)$` → (int(row)-1, col). Row 1-indexed input.

format_addr: col → letters reverse.

Range node stores normalized (r1,c1,r2,c2)? Store two corners; normalize at use.

Eval of "cell": `self._values.get(addr)` — but what if addr refers to a formula cell not yet computed? In our design all formulas computed at set-time in topo order, so values always current. Except: formula referencing cell whose value is ERR_CYCLE — stored, propagates. Good.

One subtlety: during _recalc we evaluate in topo order; when evaluating node for cell u, its deps' values are already updated (deps in dirty processed first; deps outside dirty unchanged & valid). 

Another subtlety: literal cells: store value directly in _values at set(). Formula cells: _values updated at recalc. Cleared cells: _values.pop.

IF lazy: in _eval, "call" with name IF: evaluate arg0; if error → return; truthy = to_number != 0; pick arg1 or arg2 (missing else → FALSE). Evaluate only chosen branch.

ROUND(x, d): Python round is banker's rounding; Excel rounds half away from zero. Implement: `math.floor(x*10**d + 0.5)/10**d` for positive; sign-aware: `math.copysign(math.floor(abs(x)*m+0.5), x)/m`. Nice teaching detail; include.

POWER/SQRT: math.sqrt raises ValueError → #NUM!.

Division by zero → ERR_DIV0.

`^`: result complex or overflow → #NUM!. `0^0` → Excel #NUM!. Python 0**0=1; check: if base==0 and exp==0 → #NUM!. Negative base non-integer exp → complex → #NUM!. Overflow → #NUM!.

Comparison: 

```python
def _compare(op, a, b):
    # numbers (incl bool/None) vs text
    na, nb = to_number(a), to_number(b)
    if not isinstance(na, ErrorVal) and not isinstance(nb, ErrorVal):
        x, y = na, nb
    else:
        x, y = to_text(a).lower(), to_text(b).lower()
    ...
```

Hmm: to_number("abc") → ERR_VALUE, so falls to text path. to_number("10") → 10.0 numeric path — Excel would treat "10" text vs 10 number as text>number, but our simplification compares numerically. Document.

But careful: to_number(None)=0 numeric. to_number(True)=1. So =TRUE>0 → TRUE. Fine.

Empty vs empty: = → TRUE. Good.

`&` with error → propagate.

Now _eval returns python value: float | str | bool | ErrorVal | None.

Arithmetic helper:

```python
def _num2(self, a, b):
    x, y = to_number(a), to_number(b)
    if isinstance(x, ErrorVal): return x, None
    if isinstance(y, ErrorVal): return y, None
    return x, y
```

Write it inline per op; fine.

Now the recalc and dirty logic — write carefully.

```python
def set(self, addr, raw):
    key = parse_addr(addr)
    raw = "" if raw is None else str(raw)
    if raw == "":
        self._cells.pop(key, None)
        self._ast.pop(key, None)
        self._set_deps(key, set())
        self._values.pop(key, None)
        self._recalc(self._dirty_from(key))
        return
    if raw.startswith("="):
        ast = parse_formula(raw[1:])   # raises FormulaError
        self._cells[key] = raw
        self._ast[key] = ast
        self._set_deps(key, collect_deps(ast))
    else:
        self._cells[key] = raw
        self._ast.pop(key, None)
        self._set_deps(key, set())
        self._values[key] = parse_literal(raw)
    self._recalc(self._dirty_from(key))
```

Wait: for formula cells, _values gets set in _recalc. For literal, set directly. For formula parse error: raise before mutating anything — good (parse first).

_dirty_from(key): key + transitive dependents.

_recalc(dirty):

```python
def _recalc(self, dirty):
    if not dirty: return
    indeg = {}
    for n in dirty:
        indeg[n] = sum(1 for d in self._deps.get(n, ()) if d in dirty)
    ready = [n for n, d in indeg.items() if d == 0]
    order = []
    while ready:
        u = ready.pop()
        order.append(u)
        for v in self._dependents.get(u, ()):
            if v in indeg:
                indeg[v] -= 1
                if indeg[v] == 0: ready.append(v)
    for u in order:
        if u in self._ast:
            self._values[u] = self._eval(self._ast[u])
        # literals already have values
    for n in dirty:
        if n not in ... # leftover
```

Leftover = dirty - set(order) → these are in/downstream of cycles:

```python
    cycled = dirty - set(order)  # careful: order includes literals too
    for n in cycled:
        if n in self._ast:
            self._values[n] = ERR_CYCLE
```

Hmm wait: order includes all dirty nodes that got indeg 0 — including literals. Leftover are exactly nodes in cycles or depending on cycles. Set ERR_CYCLE for formula cells among them. But a literal can't be in a cycle (no deps). OK.

Edge: self._dependents may contain stale entries? We maintain on _set_deps. When cell cleared, deps removed, dependents updated. Dependents map entries for removed edges discarded. Fine.

Also `_dirty_from` uses _dependents — includes cells that depend on key even if those dependents are literals? Literals have no deps so never in dependents. Good.

get:

```python
def get(self, addr):
    return self._values.get(parse_addr(addr))
```

display:

```python
def display(self):
    if not self._cells: return "(empty sheet)"
    maxr = max(r for r,_ in self._cells); maxc = max(c for _,c in self._cells)
    width = ... compute per column max len of formatted value and header
    lines: header row of col letters, then each row: row number + cells
```

Format value: None→"", ErrorVal→code, bool→TRUE/FALSE, float integral→int str, str→as-is.

Column width: max(len(header), max len of formatted values in that column), min 4? Keep simple: width = max(4, ...). Left-align text, right-align numbers? Keep simple: right-align everything except strings left-align. Simple: right-align all, pad. Fine.

Now the parser code:

```python
class FormulaError(Exception): pass

class Tokenizer: ... or function tokenize(text) -> list[tuple[kind, value]]
```

I'll write tokenize as a function using the master regex, raising FormulaError on bad char.

Parser class with pos, peek, eat.

```python
CELL_RE = re.compile(r"^[A-Za-z]{1,3}[0-9]+$")

def parse_formula(text):
    toks = tokenize(text)
    p = Parser(toks)
    node = p.parse_expr()
    if not p.at_end(): raise FormulaError(f"Unexpected {p.peek()!r}")
    return node
```

Parser methods as designed. Primary:

```python
def primary(self):
    kind, val = self.peek()
    if kind == "NUMBER": advance; return ("num", float(val))
    if kind == "STRING": advance; return ("str", unescape(val))
    if kind == "IDENT":
        advance
        u = val.upper()
        if u in ("TRUE","FALSE") and not self.match("("): return ("bool", u=="TRUE")
        if CELL_RE.match(val) and not self.match("("): 
            a = parse_addr(val)
            if self.match(":"):
                b = self.expect_cellref()
                return ("range", a, b)
            return ("cell", a)
        # function call
        self.expect("(")
        args = []
        if not self.check(")"):
            args.append(self.parse_expr())
            while self.match(","): args.append(self.parse_expr())
        self.expect(")")
        return ("call", u, args)
    if self.match("("): node = self.parse_expr(); self.expect(")"); return node
    raise FormulaError(...)
```

expect_cellref: peek must be IDENT matching CELL_RE.

Hmm: `A1:B2` — after cell A1, match ":" then cellref. But what about `SUM(A1:A3, 5)`? arglist parse_expr → ... → primary handles. Good.

Range with reversed corners (B2:A1) → normalize in eval/iter.

collect_deps(ast):

```python
def collect_deps(node, out):
    if node[0] == "cell": out.add(node[1])
    elif node[0] == "range":
        out.update(iter_range_addrs(node[1], node[2]))
    elif node[0] in ("un","post"): collect_deps(node[2], out)
    elif node[0] == "bin": collect_deps(node[2], out); collect_deps(node[3], out)
    elif node[0] == "call":
        for a in node[2]: collect_deps(a, out)
```

Tuple shapes: ("un", op, x), ("post", op, x), ("bin", op, l, r), ("call", NAME, args). Consistent.

iter_range: normalize corners, yield (r,c) for r in range(r1,r2+1) for c... — could be huge for A1:A100000; cap? Document limitation. Fine.

_eval:

```python
def _eval(self, node):
    tag = node[0]
    if tag == "num": return node[1]
    if tag == "str": return node[1]
    if tag == "bool": return node[1]
    if tag == "cell": return self._values.get(node[1])
    if tag == "range": raise? 
```

Range as bare value: Excel → #VALUE!. Return ERR_VALUE.

```python
    if tag == "un":
        v = self._eval(node[2]); n = to_number(v)
        return n if isinstance(n, ErrorVal) else (-n if node[1]=="-" else n)
    if tag == "post":  # %
        v = self._eval(node[2]); n = to_number(v)
        return n if isinstance(n, ErrorVal) else n/100.0
    if tag == "bin": return self._eval_bin(node[1], node[2], node[3])
    if tag == "call": return self._eval_call(node[1], node[2])
```

_eval_bin:

```python
op = ...
if op in ("+","-","*","/","^"):
    x = self._eval(l); y = self._eval(r)
    a, b = to_number(x), to_number(y)
    if isinstance(a, ErrorVal): return a
    if isinstance(b, ErrorVal): return b
    if op=="+": return a+b
    ...
    if op=="/":
        if b == 0: return ERR_DIV0
        return a/b
    if op=="^": return self._power(a,b)
if op == "&":
    x = self._eval(l); y = self._eval(r)
    if isinstance(x, ErrorVal): return x
    if isinstance(y, ErrorVal): return y
    return to_text(x) + to_text(y)
# comparisons
x = self._eval(l); y = self._eval(r)
if isinstance(x, ErrorVal): return x
if isinstance(y, ErrorVal): return y
a, b = to_number(x), to_number(y)
if isinstance(a, ErrorVal) or isinstance(b, ErrorVal):
    a, b = to_text(x).lower(), to_text(y).lower()
return {"=": a==b, "<>": a!=b, "<": a<b, ...}[op]
```

_eval_call:

```python
name = ...
if name == "IF":
    if not 2 <= len(args) <= 3: return ERR_VALUE  # Excel: #N/A-ish; keep ERR_VALUE
    cond = to_number(self._eval(args[0]))
    if isinstance(cond, ErrorVal): return cond
    if cond != 0: return self._eval(args[1])
    return self._eval(args[2]) if len(args)==3 else False
# eager for the rest
vals = []
for a in args:
    v = self._eval(a)
    if isinstance(v, ErrorVal): return v   # propagate
    vals.append(v)
fn = FUNCTIONS.get(name)
if fn is None: return ERR_NAME
return fn(self, vals)  # needs range access → pass sheet
```

Functions need to expand range args into cell values → they need sheet access. Make functions methods or pass sheet. I'll implement FUNCTIONS as dict name → method name, or a single `_call_function(name, vals)` with if/elif — clearest for teaching. Range arg in vals: represent as ("rangevals", [values])? Better: expand ranges before calling: for each arg, if it was a range node... but vals are evaluated values, range evaluates to ERR_VALUE. Hmm.

Fix: in _eval_call, handle range args specially: evaluate each arg node; if node tag == "range" → list of cell values wrapped as RangeValues(list). Define:

```python
class RangeValues:
    def __init__(self, values): self.values = values
```

Then aggregators flatten: for v in vals: if RangeValues → extend with its values (skip None? keep, functions decide); else append v.

SUM: numbers = [to_number-ish...]. Excel SUM over range: sums numbers only, ignores text/bools/empty. Direct args: coerces "5" and TRUE. Simplify uniformly: include only int/float (bool excluded? bool is int subclass — careful!). isinstance(True, int) is True — must check bool first. Rule: include if isinstance(v,(int,float)) and not isinstance(v,bool). Skip strings/None/bools in ranges AND direct args (simpler uniform rule, document deviation).

COUNT: count of those numbers. COUNTA: count of v not None and not RangeValues-empty... COUNTA counts non-empty cells: for RangeValues count non-None; direct args count if not None. 

AVERAGE: sum/count; count 0 → ERR_DIV0.
MIN/MAX: over numbers; none → 0.
ABS: 1 arg number.
ROUND(x[,d]).
SQRT: neg → ERR_NUM.
POWER(x,y) = _power.

_power(a,b):
```python
try:
    if a == 0 and b == 0: return ERR_NUM
    r = a ** b
    if isinstance(r, complex): return ERR_NUM
    if math.isinf(r) or math.isnan(r): return ERR_NUM  # overflow
    return r
except (OverflowError, ValueError): return ERR_NUM
```

a**b with negative a and fractional b returns complex in Python 3 (no exception). Check isinstance complex. Also huge: 10**10000 raises OverflowError? For floats, `1e308*10` → inf (no exception) — float ** returns inf. Check isinf. int ** int huge → big int, fine but slow; we keep floats everywhere (to_number returns float) so OK.

to_number returns float always. Good — all arithmetic float. Display formats integral floats.

parse_literal(raw):
```python
s = raw.strip()
if s == "": return ""?  # handled earlier
try: return float(s)  # "10" → 10.0 ; "abc" fails
except ValueError: pass
u = s.upper()
if u == "TRUE": return True
if u == "FALSE": return False
return raw  # keep original string (unstripped)
```

Hmm "10.5", "1e3" → float ok. "nan"/"inf" → float("nan") parses! Guard: if math.isnan/isinf → treat as string. Add check.

Now display formatting:

```python
def format_value(v):
    if v is None: return ""
    if isinstance(v, ErrorVal): return v.code
    if isinstance(v, bool): return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        if v.is_integer() and abs(v) < 1e15: return str(int(v))
        return repr(v)?  # str(v) fine
    return str(v)
```

display():

```python
def display(self):
    if not self._cells: return "(empty)"
    maxr = max(r for r, c in self._cells) + 1
    maxc = max(c for r, c in self._cells) + 1
    grid = [[format_value(self._values.get((r, c))) for c in range(maxc)] for r in range(maxr)]
    headers = [format_addr((0, c)) ... wait col letters only
```

Header: column letters "A","B",... Row labels 1..maxr. Widths: max(len(header), max(len(cell))) per column, min 3? Let widths = max over column of len. Build lines with padding, " | " separators? Simple fixed-width with two spaces. I'll do:

```
     A      B      C
1   10    =... no, values only
```

Row label width = len(str(maxr)). Fine.

Now README: build-your-own-x style guide. Structure:

# Build Your Own Spreadsheet Engine

- Intro: what & why; features of ours
- How to run (tests, demo snippet)
- Architecture (ASCII diagram)
- Part 1: The data model (addresses, cells, literals)
- Part 2: Tokenizer
- Part 3: Parser → AST (precedence table)
- Part 4: Evaluation (coercions, operators, functions, lazy IF)
- Part 5: The dependency graph (deps, reverse deps)
- Part 6: Recalculation (dirty marking, topological order, cycle detection)
- Part 7: Display
- Where to go next (extensions): undo/redo, $ refs, multi-sheet, VLOOKUP/INDEX-MATCH, iterative calculation, lazy eval / incremental, persistence, formula bar UI, web UI
- Design decisions & Excel deviations (documented simplifications)
- Further reading (build-your-own-x links: e.g., "Build your own Excel" tutorials? I shouldn't fabricate links. I can mention known resources generically: engineering blog posts about spreadsheet recalculation (e.g., "How to build a spreadsheet" articles). Avoid fake URLs. I can reference real well-known ones I'm confident about: Excel's docs on operator precedence? Risky. I'll keep further reading minimal and generic, or link the build-your-own-x repo itself (github.com/codecrafters-io/build-your-own-x) which is real.)

Keep README focused and accurate to the code.

Order of writing: spreadsheet.py, test_spreadsheet.py, README.md, then run tests, fix, done. Also run a quick demo sanity check via bash python.

Let me also double check operator precedence order in parser methods chain: parse_expr → comparison → concat → additive → term(multiplicative) → power → unary → postfix → primary. Excel precedence: unary minus > % > ^ > * / > + - > & > comparisons. Note Excel: -2^2 = 4 (unary binds tighter than ^)! Our grammar: power := unary (^ unary)*, so -2^2 parses as (-2)^2 = 4. Matches Excel. 

Left-assoc ^: 2^3^2 = (2^3)^2 = 64. Excel is left-assoc. Good.

Percent postfix: 50%^2 → (50%)^2 = 0.25. postfix binds tighter than ^: power := unary (^ unary)*, unary := (+|-) unary | postfix, postfix := primary (%)*. So 50%^2: unary → postfix → primary 50, then % → 0.5; back in power: sees ^ → 0.5^2. Good.

Now write the code. Also `__all__`, docstrings. Let me write spreadsheet.py fully:

```python
"""
spreadsheet.py — a minimal but real spreadsheet engine.

Features
--------
* A1-style addresses ("B3"), literals (numbers, text, TRUE/FALSE)
* Formulas: "=2+3*4", "=SUM(A1:A3)", "=IF(A1>10, "big", "small")"
* Operators: + - * / ^ % (postfix percent) & (concat) = <> < > <= >=
* Functions: SUM AVERAGE MIN MAX COUNT COUNTA IF ABS ROUND SQRT POWER
* Automatic recalculation via a dependency graph
* Cycle detection (#CYCLE!) and Excel-style error values
  (#DIV/0! #VALUE! #NAME? #NUM! #REF!)

Run the tests:  python -m unittest test_spreadsheet -v
"""
```

Full code below (I'll write it in the write call). Let me draft carefully.

```python
from __future__ import annotations

import math
import re

__all__ = ["Sheet", "FormulaError", "ErrorVal", "parse_addr", "format_addr"]


# --------------------------------------------------------------------------
# Errors
# --------------------------------------------------------------------------

class ErrorVal:
    """An Excel-style error value (a *value*, not an exception)."""
    __slots__ = ("code",)
    def __init__(self, code: str):
        self.code = code
    def __repr__(self):
        return self.code
    def __eq__(self, other):
        return isinstance(other, ErrorVal) and other.code == self.code
    def __hash__(self):
        return hash(("ErrorVal", self.code))

ERR_DIV0  = ErrorVal("#DIV/0!")
ERR_VALUE = ErrorVal("#VALUE!")
ERR_NAME  = ErrorVal("#NAME?")
ERR_NUM   = ErrorVal("#NUM!")
ERR_REF   = ErrorVal("#I was cut off mid-way through writing spreadsheet.py. I need to continue: write the full spreadsheet.py, test_spreadsheet.py, README.md, run tests, and verify. Let me continue from where I left off — I had drafted the design in my head; the last output was truncated during the draft of spreadsheet.py content (it was part of my thinking/answer text, not an actual write call). So nothing has been written to disk yet.

Let me now actually create the files. I should use the explore/plan tools per instructions, but the previous segment already did exploration (workspace empty). Given the truncation, I should be efficient: call plan (or just proceed). The instructions say for multi-step changes call plan. Let me do a quick plan with seed_todos, then write files.

Actually, to keep it efficient and avoid another truncation, I'll write the files directly with the write tool, keeping each write reasonably sized. spreadsheet.py will be ~400 lines. Let me write it carefully and completely this time.

Let me finalize the design decisions from part 1:

- ErrorVal class with singletons ERR_DIV0, ERR_VALUE, ERR_NAME, ERR_NUM, ERR_REF, ERR_CYCLE
- FormulaError exception for parse errors
- parse_addr / format_addr
- tokenize with master regex
- Parser (recursive descent) with precedence: comparison < concat < additive < multiplicative < power < unary < postfix < primary
- AST as tuples: ("num", v), ("str", v), ("bool", v), ("cell", (r,c)), ("range", a, b), ("un", op, x), ("post", op, x), ("bin", op, l, r), ("call", NAME, args)
- collect_deps
- Sheet: set/get/get_raw/display, _set_deps, _dirty_from, _recalc (Kahn topo + cycle leftover → ERR_CYCLE)
- Coercions: to_number, to_text
- _eval, _eval_bin, _eval_call with lazy IF
- Functions: SUM AVERAGE MIN MAX COUNT COUNTA ABS ROUND SQRT POWER (IF handled lazily)
- RangeValues wrapper for range args
- parse_literal for cell literals

Now write the code. I'll be careful about:
- bool check before int/float checks (isinstance(True, int))
- float("nan"/"inf") guard in parse_literal
- ROUND half away from zero
- power edge cases
- case-insensitive string comparison
- display grid formatting

Let me write spreadsheet.py now. I'll aim for complete, correct code in one write call. Then test file, then README, then run tests.

One detail on _recalc: dirty set includes the changed cell and all transitive dependents. Kahn on subgraph induced by dirty: indeg[n] = number of deps of n within dirty. Ready queue = indeg 0. Pop u → order.append(u) → for v in dependents[u] if v in indeg: decrement. After: evaluate formula cells in order. Leftover = dirty - order → formula cells get ERR_CYCLE.

Wait, there's a subtle bug: order includes literal cells too (they have no deps, indeg 0). When evaluating formula cells in `order`, referenced cells outside dirty use cached _values — fine.

Another subtlety: when a formula cell's value is computed, store in _values. Literal cells already have _values set at set() time. Cleared cells popped.

Edge: _dirty_from(key) — key itself plus transitive dependents via _dependents. When we clear a cell, we pop its _values before recalc — dependents reading it get None (empty). Good.

Edge: set() with formula parse error → raise before any mutation. Good.

Edge: deps diff update in _set_deps.

Now the tokenizer regex:

```python
_TOKEN_RE = re.compile(
    r"""\s*(?:
        (?P<number>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)
      | (?P<string>"(?:[^"]|"")*")
      | (?P<ident>[A-Za-z_][A-Za-z0-9_]*)
      | (?P<op><>|<=|>=|[=<>+\-*/^%&(),:])
    )""",
    re.VERBOSE,
)
```

tokenize(text): pos=0; while pos < len: m = _TOKEN_RE.match(text, pos); if not m or m.end()==pos → check trailing whitespace; raise FormulaError. Classify: number → ("num", float(text)); string → ("str", value[1:-1].replace('""','"')); ident → ("ident", value); op → char in "()," ":" → ("punct", ch) else ("op", ch).

Hmm, simpler: keep kinds: "num", "str", "ident", "op" (ops include parens/comma/colon as single-char ops). Parser checks op values. Let me unify: all ops (multi-char and single) → ("op", s). Parser: self._at("(", ...) checks kind=="op" and value=="(".

Trailing whitespace: after loop, if remaining text is whitespace only, done. Handle: m matches leading \s*; if m.end() == pos (no progress) → if text[pos:].strip()=="" break else raise.

Parser:

```python
class _Parser:
    def __init__(self, tokens):
        self.toks = tokens
        self.i = 0

    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else ("end", "")

    def advance(self):
        tok = self.peek()
        self.i += 1
        return tok

    def match_op(self, *ops):
        kind, val = self.peek()
        if kind == "op" and val in ops:
            self.i += 1
            return val
        return None

    def expect_op(self, op):
        if not self.match_op(op):
            raise FormulaError(f"Expected '{op}' but found '{self.peek()[1] or 'end of formula'}'")
```

parse_expr → parse_comparison chain as designed.

parse_primary: as designed. Cell ref: ident matching CELL_RE and next token is not "(" — actually function names never match CELL_RE unless like "LOG10" — treat ident followed by "(" as function call regardless. So: if next is "(" → function call; elif CELL_RE match → cell/range; elif TRUE/FALSE → bool; else raise FormulaError(f"Unknown name '{val}'").

Wait order: check "(" first (function call), then TRUE/FALSE, then CELL_RE, else error. But "A1(" — weird, treat as function call A1 → unknown function at eval → ERR_NAME. Fine.

collect_deps(node, out:set).

RangeValues class.

Sheet class:

```python
class Sheet:
    def __init__(self):
        self._cells: dict[tuple[int,int], str] = {}   # raw content
        self._ast: dict = {}
        self._deps: dict = {}        # key -> set of keys it depends on
        self._dependents: dict = {}  # key -> set of keys that depend on it
        self._values: dict = {}      # key -> computed value
```

set/get/get_raw/display as designed.

Functions implementation:

```python
def _flatten(self, vals):
    out = []
    for v in vals:
        if isinstance(v, RangeValues):
            out.extend(v.values)
        else:
            out.append(v)
    return out

def _numbers(self, vals):
    return [v for v in self._flatten(vals)
            if isinstance(v, (int, float)) and not isinstance(v, bool)]
```

SUM: sum(numbers) → 0.0 if empty. AVERAGE: div0 check. MIN/MAX: 0 if empty. COUNT: len(numbers). COUNTA: count of flattened v where v is not None (RangeValues already flattened; note empty string counts as non-empty — Excel counts "" as non-empty. OK).

ABS/ROUND/SQRT/POWER: to_number arg; error → return.

ROUND: 

```python
m = 10 ** digits
x = x * m
r = math.copysign(math.floor(abs(x) + 0.5), x) / m
```

digits = int(to_number) — if digits arg error → return. Negative digits allowed.

_eval_call:

```python
def _eval_call(self, name, arg_nodes):
    if name == "IF":
        if not 2 <= len(arg_nodes) <= 3:
            return ERR_VALUE
        cond = to_number(self._eval(arg_nodes[0]))
        if isinstance(cond, ErrorVal):
            return cond
        if cond != 0:
            return self._eval(arg_nodes[1])
        return self._eval(arg_nodes[2]) if len(arg_nodes) == 3 else False
    args = []
    for node in arg_nodes:
        if node[0] == "range":
            args.append(RangeValues(self._range_values(node[1], node[2])))
        else:
            v = self._eval(node)
            if isinstance(v, ErrorVal):
                return v
            args.append(v)
    fn = getattr(self, "_fn_" + name, None)  # hmm, or dict
```

Better: dict FUNCTIONS mapping name → unbound method? I'll use a dict of lambdas taking (sheet, vals)? For teaching clarity, use if/elif chain in _eval_call? A dict `_FUNCTIONS` of name → method name string, then `getattr(self, meth)`. Simplest readable: 

```python
handler = _FUNCTIONS.get(name)
if handler is None:
    return ERR_NAME
return handler(self, args)
```

with module-level `_FUNCTIONS = {"SUM": _fn_sum, ...}` where each _fn_sum(sheet, vals). That's clean. Define functions as module-level functions taking (sheet, vals).

_range_values(a, b): normalize corners; return [self._values.get((r,c)) for r,c in iter]. Cap size? Add guard: if area > 1_000_000 raise FormulaError? At eval time raising is bad; return ERR_REF? Keep simple, no cap, document.

Comparison eval: as designed.

to_number:

```python
def to_number(v):
    if v is None: return 0.0
    if isinstance(v, bool): return 1.0 if v else 0.0
    if isinstance(v, (int, float)): return float(v)
    if isinstance(v, str):
        try:
            return float(v.strip())
        except ValueError:
            return ERR_VALUE
    if isinstance(v, ErrorVal): return v
    return ERR_VALUE
```

Wait: float("nan") from string "nan" — "nan" parses to nan. Guard: after parse, if math.isnan or isinf → ERR_VALUE. Add.

to_text:

```python
def to_text(v):
    if v is None: return ""
    if isinstance(v, ErrorVal): return v.code
    if isinstance(v, bool): return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        if v.is_integer() and abs(v) < 1e16: return str(int(v))
        return str(v)
    return str(v)
```

format_value same as to_text basically — reuse to_text for display. Yes, to_text is the display formatter too.

parse_literal:

```python
def parse_literal(raw):
    s = raw.strip()
    u = s.upper()
    if u == "TRUE": return True
    if u == "FALSE": return False
    try:
        x = float(s)
    except ValueError:
        return raw
    if math.isnan(x) or math.isinf(x):
        return raw
    return x
```

display():

```python
def display(self):
    if not self._cells:
        return "(empty sheet)"
    max_row = max(r for r, _ in self._cells)
    max_col = max(c for _, c in self._cells)
    col_labels = [col_letter(c) for c in range(max_col + 1)]
    grid = []
    for r in range(max_row + 1):
        grid.append([to_text(self._values.get((r, c))) for c in range(max_col + 1)])
    widths = []
    for c in range(max_col + 1):
        w = len(col_labels[c])
        for r in range(max_row + 1):
            w = max(w, len(grid[r][c]))
        widths.append(max(w, 3))
    label_w = len(str(max_row + 1))
    lines = [" " * label_w + " | " + " | ".join(lbl.ljust(widths[c]) ... )]
```

Hmm alignment: numbers right-aligned, text left-aligned? Keep simple: right-align all cells, header centered-ish (rjust). Let me do: header labels rjust, cells rjust. Row label ljust. Separator " | ". Fine.

Actually simpler and prettier: right-justify everything.

```python
header = " " * label_w + " |" + "|".join(lbl.rjust(widths[c]+1) for ...)
```

Let me just do:

```python
def _row(cells): return " | ".join(cells)
lines = []
lines.append(" " * label_w + " | " + _row([col_labels[c].rjust(widths[c]) for c in ...]))
for r in ...:
    lines.append(str(r+1).rjust(label_w) + " | " + _row([grid[r][c].rjust(widths[c]) ...]))
return "\n".join(lines)
```

Good enough.

col_letter(c): 

```python
def col_letter(c):
    s = ""
    c += 1
    while c:
        c, rem = divmod(c - 1, 26)
        s = chr(65 + rem) + s
    return s
```

parse_addr:

```python
_ADDR_RE = re.compile(r"^([A-Za-z]{1,3})([0-9]+)$")

def parse_addr(addr):
    m = _ADDR_RE.match(addr.strip())
    if not m:
        raise ValueError(f"Invalid cell address: {addr!r}")
    col = 0
    for ch in m.group(1).upper():
        col = col * 26 + (ord(ch) - 64)
    return (int(m.group(2)) - 1, col - 1)
```

format_addr(key): col_letter(c) + str(r+1).

Tokenizer string unescape: value[1:-1].replace('""', '"').

Now the tests — unittest:

```python
import unittest
from spreadsheet import Sheet, FormulaError, ErrorVal, parse_addr, format_addr

class AddrTests(unittest.TestCase):
    def test_parse_format_roundtrip(self): ...
    def test_invalid_address(self): ...

class LiteralTests: set/get numbers, strings, bools
class FormulaTests: arithmetic, precedence, unary, percent, concat, comparisons
class FunctionTests: SUM range, AVERAGE, MIN/MAX, COUNT/COUNTA, IF lazy, ABS/ROUND/SQRT/POWER, unknown function → ERR_NAME
class RecalcTests: chain recompute, dep update when formula replaced by literal, clear cell, multi-dependent
class CycleTests: self-loop, two-cell, dependent of cycle, recovery
class ErrorTests: div0, propagation, sqrt(-1), parse error raises, unknown name raises
class DisplayTests: display contains headers and values
```

Check: unknown bare name "=foo+1" → FormulaError at set (parser raises "Unknown name"). Unknown function "=FOO(1)" → parses, eval → ERR_NAME. Test both.

Test IF lazy: sheet.set("A1", '=IF(TRUE, 1, 1/0)') → get 1.0 (not error).

Test percent: "=50%*2" → 1.0? 50% → 0.5, *2 → 1.0. Wait precedence: 50%*2 → multiplicative: power → unary → postfix → primary 50 then % → 0.5; then *2 → 1.0. Good.

Test "=2^3^2" → 64.0 (left assoc).

Test "=-2^2" → 4.0 (Excel behavior).

Test concat: '="a"&"b"' → "ab"; '=1&2' → "12"; '=A1&"!"' with A1=5 → "5!".

Test comparisons: '=1<2' → True; '="abc"="ABC"' → True; '=2>=3' → False.

Test SUM with mixed: A1=1, A2="x" (text), A3=3, A4 empty, B1="=SUM(A1:A4)" → 4.0. COUNT → 2. COUNTA → 3 (A1,A2,A3 non-empty; A4 empty).

Wait: A2 set to "x" — literal string. SUM over range skips strings → 1+3=4. COUNT counts numbers → 2. COUNTA counts non-None → A1(1.0), A2("x"), A3(3.0) → 3. Good.

Test error propagation: A1="=1/0", B1="=A1+1" → ERR_DIV0. get returns ErrorVal; compare code.

Test cycles: A1="=A1" → ERR_CYCLE. A1="=B1", B1="=A1" → both ERR_CYCLE. C1="=A1+1" → ERR_CYCLE (downstream). Recovery: set B1 to 5 → A1=5, C1=6.

Test recompute: A1=1, A2="=A1*2" → 2; set A1=5 → 10. Replace A2 with literal 7 → 7; set A1=100 → A2 stays 7.

Test clear: A1=5, A2="=A1*2" → 10; set A1="" → A2=0.

Test display: build small sheet, check "A" "B" header and "10" present, row labels.

Test get_raw: returns "=A1*2" and "5".

Test parse error: with self.assertRaises(FormulaError): sheet.set("A1", "=1+"); also "=)" etc. And state unchanged: get_raw("A1") is None.

Also test string with escaped quotes: '="say ""hi"""' → 'say "hi"'.

Test number in scientific notation: "=1e2" → 100.0.

Test range reversed: "=SUM(B1:A1)"? corners reversed — normalize. A1=1,B1=2 → SUM(B1:A1)=3. Wait parse: primary ident "B1" cell, match ":", expect cellref "A1" → range ((0,1),(0,0)) normalized → both. Good.

Test function call with range + scalar: "=SUM(A1:A2, 10)".

Now README.md — build-your-own-x style guide. Sections:

# Build your own Spreadsheet Engine
- intro, what you'll build (feature list), how to run
- Architecture diagram
- Step 1: cells and addresses
- Step 2: tokenizer
- Step 3: parser & AST (precedence table)
- Step 4: evaluation (coercion rules, operators, functions, lazy IF)
- Step 5: dependency graph
- Step 6: recalculation & cycle detection (Kahn's algorithm)
- Step 7: display
- Documented deviations from Excel
- Exercises
- Further reading (link to build-your-own-x repo — real URL: https://github.com/codecrafters-io/build-your-own-x)

Keep README concise but complete. Include a demo snippet:

```python
from spreadsheet import Sheet
s = Sheet()
s.set("A1", "3")
s.set("A2", "4")
s.set("A3", "=SUM(A1:A2)")
s.set("A4", "=A3*2")
print(s.get("A3"))   # 7.0
s.set("A1", "10")
print(s.get("A4"))   # 28.0
print(s.display())
```

Now, per instructions I should call plan before editing. The previous segment already did exploration implicitly (empty workspace). To be compliant and quick, I'll call plan with seed_todos=true, then write files, run tests, fix issues, verify, done. Keep responses tight to avoid truncation: write files via tool calls (tool call content doesn't count against my visible answer tokens? Actually it does count toward output tokens... the truncation happened at max_tokens. I must be careful: write spreadsheet.py in one call (~450 lines) — that's large but necessary. Maybe split into two writes? write overwrites whole file; can't append. I could write the file in one go — it's the safest for correctness. Keep code tight, avoid excessive comments to reduce size. Aim ~380 lines.

Let me also double-check _recalc handles the case where dirty contains a formula cell whose deps include cells NOT in dirty — fine, uses cached values.

One more check on _set_deps and _dirty_from ordering in set(): for formula: store ast, _set_deps(key, new_deps), then _recalc(_dirty_from(key)). _dirty_from includes key + dependents. Good.

For literal: _set_deps(key, set()) removes old edges; _values[key] = literal; recalc dirty from key. Good.

For clear: pop everything, _set_deps(key, set()), _values.pop, recalc. Good.

Potential issue: _dependents entries for key itself when key has dependents — _dirty_from uses self._dependents.get(key, ()) — fine.

Kahn: indeg counts deps within dirty. But note: deps of n include cells n depends on; edge direction dep → n. Processing order: ready = no unresolved deps. When u processed, decrement dependents. Correct.

Leftover → ERR_CYCLE for formula cells. But also: what about formula cells in dirty that are in `order` but reference a cycle cell outside dirty? Can't happen: if n references cycle cell c, then c is a dep of n; if c not in dirty... c's value would be ERR_CYCLE already from earlier set, and n would have been marked dirty when c was set (n is a dependent of c). So within this set() call, if n depends on c and c is in a cycle, c ∈ dirty (since dirty includes all transitive dependents of the changed cell — wait, is the cycle necessarily downstream of the changed cell?).

Hmm, careful: cycles can only be *created* by the current set() (adding an edge). If the new edge creates a cycle, all cycle members are dependents-of/depend-on the changed cell... Let me think: set() on key K with formula referencing... cycle through K: K → ... → K. All cycle members are on a path from K's deps to K's dependents. Are all cycle members in _dirty_from(K)? _dirty_from = K + transitive dependents of K. Cycle members: K, and cells that depend on K (transitively) — yes, every cycle member must reach K via dependency edges, i.e., is a transitive dependent of K. So all in dirty. 

But wait — could a cycle exist that doesn't involve K? Only if it existed before, which can't since previous state was acyclic (invariant maintained: every set() resolves cycles to ERR_CYCLE values but the *graph* still contains cycle edges!). Hmm: A1="=B1", B1="=A1" → both ERR_CYCLE, but deps remain. Now set C1="=A1". C1 depends on A1; dirty = {C1, dependents of C1}. A1 not in dirty. A1's value is ERR_CYCLE (cached). C1 = A1+1 → to_number(ERR_CYCLE) → returns ERR_CYCLE → propagates. Good — cached error propagates. No re-derivation needed. Invariant: any cell whose value is ERR_CYCLE keeps it until edited. Dependents propagate the error value. OK.

But subtle: leftover in Kahn within dirty — if dirty contains a cycle among themselves. When could dirty contain a cycle not involving K? If cycle members are all transitive dependents of K but the cycle formed earlier... e.g., A1="=B1", B1="=A1" (cycle, both ERR_CYCLE). Now set A1=5 (literal). Dirty = {A1, B1, dependents...}. B1="=A1" → dep A1 in dirty, indeg 1 → after A1 processed, B1 → 5. Cycle broken by literal. Good.

Another: A1="=B1+C1", B1="=A1", C1=3. Dirty from setting... say set C1=4: dirty={C1, A1, B1}. indeg: A1: deps B1(in dirty), C1(in dirty) → 2. B1: dep A1 → 1. C1: 0. Order: C1, then A1? A1 indeg 2 → after C1 processed → 1 (B1 unresolved). B1 never ready → leftover {A1, B1} → ERR_CYCLE. Correct — there IS a cycle A1↔B1. Good.

And setting B1=7 (literal): dirty={B1, A1}. A1 deps B1, C1; C1 not in dirty (C1 has no dependents... wait C1=3 literal, A1 depends on C1 but C1 not dirty). indeg A1 = 1 (B1 in dirty). B1 ready → 7; A1 → 7+3=10. Good.

Edge: formula referencing itself via range: A1="=SUM(A1:A2)" → dep includes A1 → cycle → ERR_CYCLE. Good.

Now — one more design point: `get` on a cell that's part of a cycle returns ErrorVal ERR_CYCLE. Tests compare `sheet.get("A1") == ERR_CYCLE`? ErrorVal __eq__ compares code. Export ERR_CYCLE from module. Or compare .code. I'll export the singletons.

Also `__repr__` of ErrorVal returns code — nice for debugging.

Let me also add `values()` or `cells()`? Not needed. Keep API minimal: set, get, get_raw, display. Maybe `is_empty`? No.

Alright, also `__eq__` on Sheet? No.

Write the files now. First plan call (quick), then writes, then run tests.

Actually — the plan tool: "Write a structured action plan BEFORE editing code". I'll do one compact plan call, then execute. Given token budget concerns, keep plan brief.

Let me now write out the complete spreadsheet.py mentally one more time to ensure correctness, then emit.

```python
"""A minimal but real spreadsheet engine..."""

from __future__ import annotations

import math
import re

__all__ = [
    "Sheet", "FormulaError", "ErrorVal",
    "ERR_DIV0", "ERR_VALUE", "ERR_NAME", "ERR_NUM", "ERR_REF", "ERR_CYCLE",
    "parse_addr", "format_addr",
]


class ErrorVal:
    """An Excel-style error value. These are *values*, not exceptions, so a
    formula like =A1+1 where A1 is #DIV/0! evaluates to #DIV/0! itself."""
    __slots__ = ("code",)

    def __init__(self, code: str) -> None:
        self.code = code

    def __repr__(self) -> str:
        return self.code

    def __eq__(self, other: object) -> bool:
        return isinstance(other, ErrorVal) and other.code == self.code

    def __hash__(self) -> int:
        return hash(("ErrorVal", self.code))


ERR_DIV0 = ErrorVal("#DIV/0!")
ERR_VALUE = ErrorVal("#VALUE!")
ERR_NAME = ErrorVal("#NAME?")
ERR_NUM = ErrorVal("#NUM!")
ERR_REF = ErrorVal("#REF!")
ERR_CYCLE = ErrorVal("#CYCLE!")


class FormulaError(Exception):
    """Raised by Sheet.set when a formula cannot be parsed."""


# ---------------------------------------------------------------------------
# Addresses
# ---------------------------------------------------------------------------

_ADDR_RE = re.compile(r"^([A-Za-z]{1,3})([0-9]+)$")


def parse_addr(addr: str) -> tuple[int, int]:
    """'B3' -> (row=2, col=1), both 0-based."""
    m = _ADDR_RE.match(addr.strip())
    if not m:
        raise ValueError(f"invalid cell address: {addr!r}")
    col = 0
    for ch in m.group(1).upper():
        col = col * 26 + (ord(ch) - ord("A") + 1)
    return int(m.group(2)) - 1, col - 1


def col_letter(col: int) -> str:
    letters = ""
    col += 1
    while col:
        col, rem = divmod(col - 1, 26)
        letters = chr(ord("A") + rem) + letters
    return letters


def format_addr(key: tuple[int, int]) -> str:
    row, col = key
    return f"{col_letter(col)}{row + 1}"
```

Tokenizer:

```python
_TOKEN_RE = re.compile(
    r"""\s*(?:
        (?P<number>\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)
      | (?P<string>"(?:[^"]|"")*")
      | (?P<ident>[A-Za-z_][A-Za-z0-9_]*)
      | (?P<op><>|<=|>=|[=<>+\-*/^%&(),:])
    )""",
    re.VERBOSE,
)


def _tokenize(text: str) -> list[tuple[str, object]]:
    tokens: list[tuple[str, object]] = []
    pos = 0
    while pos < len(text):
        m = _TOKEN_RE.match(text, pos)
        if m is None or m.end() == pos:
            if text[pos:].strip() == "":
                break
            raise FormulaError(f"unexpected character {text[pos:].lstrip()[0]!r} in formula")
        pos = m.end()
        if m.group("number") is not None:
            tokens.append(("num", float(m.group("number"))))
        elif m.group("string") is not None:
            tokens.append(("str", m.group("string")[1:-1].replace('""', '"')))
        elif m.group("ident") is not None:
            tokens.append(("ident", m.group("ident")))
        else:
            tokens.append(("op", m.group("op")))
    return tokens
```

Wait bug: if m matches only whitespace (m.end() > pos but no group) — the op alternation requires one of the groups... The regex `\s*(?:...)` — if only whitespace remains, the `(?:...)` fails → m is None → check strip → break. If m.end()==pos can't happen since \s* could match empty and group fails → whole match fails → None. Actually if text[pos:] = "   " → match fails (None) → strip → break. If "  1" → matches. OK. But m.end()==pos case: can't occur when m is not None because some group must match (non-empty). Keep the guard anyway harmless.

Hmm wait, one more: `m.end() == pos` — if regex matched empty string? Groups all require ≥1 char, so no. Fine.

Parser:

```python
_CELL_RE = re.compile(r"^[A-Za-z]{1,3}[0-9]+$")


class _Parser:
    """Recursive-descent parser producing tuple-based AST nodes:

        ("num", 3.0)                ("str", "hi")           ("bool", True)
        ("cell", (row, col))        ("range", a, b)
        ("un", "-", x)              ("post", "%", x)
        ("bin", "+", l, r)          ("call", "SUM", [args])
    """

    def __init__(self, tokens):
        self.toks = tokens
        self.i = 0

    # -- token helpers ------------------------------------------------
    def peek(self):
        return self.toks[self.i] if self.i < len(self.toks) else ("end", "")

    def advance(self):
        tok = self.peek()
        self.i += 1
        return tok

    def match(self, *ops):
        kind, val = self.peek()
        if kind == "op" and val in ops:
            self.i += 1
            return val
        return None

    def expect(self, op):
        if not self.match(op):
            found = self.peek()[1] or "end of formula"
            raise FormulaError(f"expected {op!r}, found {found!r}")

    # -- grammar ------------------------------------------------------
    def parse(self):
        node = self.expr()
        kind, val = self.peek()
        if kind != "end":
            raise FormulaError(f"unexpected {val!r} after expression")
        return node

    def expr(self):
        return self.comparison()

    def comparison(self):
        node = self.concat()
        while True:
            op = self.match("=", "<>", "<", ">", "<=", ">=")
            if not op:
                return node
            node = ("bin", op, node, self.concat())

    def concat(self):
        node = self.additive()
        while self.match("&"):
            node = ("bin", "&", node, self.additive())
        return node

    def additive(self):
        node = self.multiplicative()
        while True:
            op = self.match("+", "-")
            if not op:
                return node
            node = ("bin", op, node, self.multiplicative())

    def multiplicative(self):
        node = self.power()
        while True:
            op = self.match("*", "/")
            if not op:
                return node
            node = ("bin", op, node, self.power())

    def power(self):
        node = self.unary()
        while self.match("^"):
            node = ("bin", "^", node, self.unary())
        return node

    def unary(self):
        op = self.match("+", "-")
        if op:
            return ("un", op, self.unary())
        return self.postfix()

    def postfix(self):
        node = self.primary()
        while self.match("%"):
            node = ("post", "%", node)
        return node

    def primary(self):
        kind, val = self.peek()
        if kind == "num":
            self.advance()
            return ("num", val)
        if kind == "str":
            self.advance()
            return ("str", val)
        if kind == "op" and val == "(":
            self.advance()
            node = self.expr()
            self.expect(")")
            return node
        if kind == "ident":
            self.advance()
            if self.peek() == ("op", "("):
                return self.call(val.upper())
            upper = val.upper()
            if upper in ("TRUE", "FALSE"):
                return ("bool", upper == "TRUE")
            if _CELL_RE.match(val):
                a = parse_addr(val)
                if self.match(":"):
                    return ("range", a, self.cellref())
                return ("cell", a)
            raise FormulaError(f"unknown name {val!r}")
        raise FormulaError(f"unexpected {val or 'end of formula'!r}")

    def call(self, name):
        self.expect("(")
        args = []
        if self.peek() != ("op", ")"):
            args.append(self.expr())
            while self.match(","):
                args.append(self.expr())
        self.expect(")")
        return ("call", name, args)

    def cellref(self):
        kind, val = self.advance()
        if kind == "ident" and _CELL_RE.match(val):
            return parse_addr(val)
        raise FormulaError(f"expected cell reference, found {val!r}")


def parse_formula(text: str):
    return _Parser(_tokenize(text)).parse()
```

Wait: `self.peek() == ("op", "(")` — peek returns tuple ("op", "("). OK.

Issue: `("end", "")` — in primary, `raise FormulaError(f"unexpected {val or 'end of formula'!r}")` — f-string with `val or 'end of formula'!r` — precedence: `!r` applies to the whole `val or 'end of formula'`? In f-strings, `{val or 'end of formula'!r}` — conversion applies to entire expression. Yes valid. But val="" → "" or '...' → 'end of formula' → repr. OK.

Deps:

```python
def _collect_deps(node, out):
    tag = node[0]
    if tag == "cell":
        out.add(node[1])
    elif tag == "range":
        out.update(_iter_range(node[1], node[2]))
    elif tag == "un" or tag == "post":
        _collect_deps(node[2], out)
    elif tag == "bin":
        _collect_deps(node[2], out)
        _collect_deps(node[3], out)
    elif tag == "call":
        for arg in node[2]:
            _collect_deps(arg, out)


def _iter_range(a, b):
    r1, c1 = a
    r2, c2 = b
    for r in range(min(r1, r2), max(r1, r2) + 1):
        for c in range(min(c1, c2), max(c1, c2) + 1):
            yield (r, c)
```

Coercions:

```python
def to_number(v):
    """Coerce a cell value to float, Excel-style. Returns ErrorVal on failure."""
    if v is None:
        return 0.0
    if isinstance(v, bool):
        return 1.0 if v else 0.0
    if isinstance(v, float):
        return v
    if isinstance(v, int):
        return float(v)
    if isinstance(v, str):
        try:
            x = float(v.strip())
        except ValueError:
            return ERR_VALUE
        if math.isnan(x) or math.isinf(x):
            return ERR_VALUE
        return x
    if isinstance(v, ErrorVal):
        return v
    return ERR_VALUE


def to_text(v):
    """Coerce a cell value to its display text."""
    if v is None:
        return ""
    if isinstance(v, ErrorVal):
        return v.code
    if isinstance(v, bool):
        return "TRUE" if v else "FALSE"
    if isinstance(v, float):
        if v.is_integer() and abs(v) < 1e16:
            return str(int(v))
        return str(v)
    return str(v)
```

parse_literal:

```python
def _parse_literal(raw: str):
    s = raw.strip()
    if s.upper() == "TRUE":
        return True
    if s.upper() == "FALSE":
        return False
    try:
        x = float(s)
    except ValueError:
        return raw
    if math.isnan(x) or math.isinf(x):
        return raw
    return x
```

RangeValues:

```python
class RangeValues:
    """Marker wrapper so aggregate functions can tell range arguments
    (ignore text/empties) from direct arguments."""
    __slots__ = ("values",)
    def __init__(self, values):
        self.values = values
```

Functions (module-level, take (sheet, args)):

```python
def _flatten(args):
    out = []
    for a in args:
        if isinstance(a, RangeValues):
            out.extend(a.values)
        else:
            out.append(a)
    return out


def _numbers(args):
    return [v for v in _flatten(args)
            if isinstance(v, (int, float)) and not isinstance(v, bool)]


def _fn_sum(sheet, args):
    return float(sum(_numbers(args)))


def _fn_average(sheet, args):
    nums = _numbers(args)
    if not nums:
        return ERR_DIV0
    return sum(nums) / len(nums)


def _fn_min(sheet, args):
    nums = _numbers(args)
    return float(min(nums)) if nums else 0.0


def _fn_max(sheet, args):
    nums = _numbers(args)
    return float(max(nums)) if nums else 0.0


def _fn_count(sheet, args):
    return float(len(_numbers(args)))


def _fn_counta(sheet, args):
    return float(sum(1 for v in _flatten(args) if v is not None))


def _fn_abs(sheet, args):
    x = _need_number(args, 1)
    if isinstance(x, ErrorVal):
        return x
    return abs(x)


def _need_number(args, n):
    if len(args) < n:
        return ERR_VALUE
    return to_number(args[0])  # hmm for multi-arg need index
```

Let me simplify: helper `_num(args, i)` returns to_number(args[i]) or ERR_VALUE if missing:

```python
def _num(args, i):
    if i >= len(args):
        return ERR_VALUE
    return to_number(args[i])


def _fn_abs(sheet, args):
    x = _num(args, 0)
    return x if isinstance(x, ErrorVal) else abs(x)


def _fn_round(sheet, args):
    x = _num(args, 0)
    if isinstance(x, ErrorVal):
        return x
    d = _num(args, 1) if len(args) > 1 else 0.0
    if isinstance(d, ErrorVal):
        return d
    m = 10.0 ** int(d)
    return math.copysign(math.floor(abs(x) * m + 0.5), x) / m


def _fn_sqrt(sheet, args):
    x = _num(args, 0)
    if isinstance(x, ErrorVal):
        return x
    if x < 0:
        return ERR_NUM
    return math.sqrt(x)


def _fn_power(sheet, args):
    x = _num(args, 0)
    if isinstance(x, ErrorVal):
        return x
    y = _num(args, 1)
    if isinstance(y, ErrorVal):
        return y
    return _power(x, y)


_FUNCTIONS = {
    "SUM": _fn_sum, "AVERAGE": _fn_average, "MIN": _fn_min, "MAX": _fn_max,
    "COUNT": _fn_count, "COUNTA": _fn_counta, "ABS": _fn_abs,
    "ROUND": _fn_round, "SQRT": _fn_sqrt, "POWER": _fn_power,
}
```

_power:

```python
def _power(a, b):
    if a == 0 and b == 0:
        return ERR_NUM
    try:
        r = a ** b
    except (OverflowError, ValueError, ZeroDivisionError):
        return ERR_NUM
    if isinstance(r, complex) or math.isnan(r) or math.isinf(r):
        return ERR_NUM
    return r
```

a**b with a<0, b fractional → Python returns complex (no exception) since 3.x? Actually `(-8) ** (1/3)` → complex? In Python 3, float ** float with negative base and non-integer exponent raises... no wait: `(-8.0) ** 0.333` raises ValueError? Let me recall: `(-8.0) ** 0.5` → Python 3 returns complex? No — for floats, `(-8.0) ** 0.5` raises ValueError: "negative number cannot be raised to a fractional power"? Hmm, actually in Python 3, `(-8.0) ** 0.5` returns a complex number? Testing memory: `(-8) ** 0.5` → `(1.7319121124709868e-16+2.8284271247461903j)` — yes, Python 3 returns complex for negative base ** fractional float. int ** returns complex too. So isinstance complex check handles it. OverflowError for huge int exponent... floats: `1e308 ** 2` → inf (OverflowError? For float ** float, Python returns inf? `1e308 ** 2.0` → OverflowError: (34, 'Numerical result out of range')! Yes float pow raises OverflowError, doesn't return inf. Caught. Good.

ZeroDivisionError: 0 ** negative → ZeroDivisionError. Caught → ERR_NUM. But a==0,b==0 checked first (Excel #NUM!). 0^-1 → ZeroDivisionError → ERR_NUM. Excel gives #DIV/0! for 0^-1. Minor, fine.

Sheet:

```python
class Sheet:
    """An in-memory spreadsheet with formulas and automatic recalculation."""

    def __init__(self) -> None:
        self._raw = {}        # key -> raw cell content (as entered)
        self._ast = {}        # key -> formula AST (formulas only)
        self._deps = {}       # key -> set of keys this cell depends on
        self._dependents = {} # key -> set of keys that depend on this cell
        self._values = {}     # key -> last computed value

    # -- public API ----------------------------------------------------
    def set(self, addr: str, raw: str | None) -> None:
        """Set a cell. raw starting with '=' is a formula; '' clears it."""
        key = parse_addr(addr)
        raw = "" if raw is None else str(raw)
        if raw == "":
            self._raw.pop(key, None)
            self._ast.pop(key, None)
            self._values.pop(key, None)
            self._set_deps(key, set())
        elif raw.startswith("="):
            ast = parse_formula(raw[1:])  # may raise FormulaError; mutates nothing
            self._raw[key] = raw
            self._ast[key] = ast
            self._set_deps(key, _collect_deps_into(ast))
        else:
            self._raw[key] = raw
            self._ast.pop(key, None)
            self._values[key] = _parse_literal(raw)
            self._set_deps(key, set())
        self._recalc(self._dirty_from(key))

    def get(self, addr: str):
        """Computed value: float | str | bool | ErrorVal | None (empty)."""
        return self._values.get(parse_addr(addr))

    def get_raw(self, addr: str):
        return self._raw.get(parse_addr(addr))

    def display(self) -> str:
        ...
```

_collect_deps_into(ast) → returns set. Define:

```python
def _deps_of(ast):
    out = set()
    _collect_deps(ast, out)
    return out
```

_set_deps:

```python
    def _set_deps(self, key, new_deps):
        old = self._deps.get(key, set())
        for dep in old - new_deps:
            self._dependents[dep].discard(key)
        for dep in new_deps - old:
            self._dependents.setdefault(dep, set()).add(key)
        if new_deps:
            self._deps[key] = new_deps
        else:
            self._deps.pop(key, None)
```

_dirty_from:

```python
    def _dirty_from(self, key):
        dirty = set()
        stack = [key]
        while stack:
I keep getting truncated because I'm drafting the entire file in my thinking/output. I need to stop drafting in the response and just make the tool calls. The files haven't been written to disk yet. Let me write spreadsheet.py via the write tool now — the tool call content is what matters, and I should keep my visible prose minimal.

Let me write the complete file in one write call, keeping it tight. Then tests, README, run tests.

I'll write the full spreadsheet.py now. Keep comments concise to fit within token limits. Maybe split: write core file first (~400 lines is fine in a tool call — tool call content counts toward output tokens, so I must be economical). Let me write it compactly but completely.Now the test suite:Two failures: a wrong test assertion (row label line index) and a real bug — `SUM` over a range containing an error cell returned 0.0 instead of propagating the error. Fixing both:Now update the aggregate functions to flatten + check errors first:All 34 tests pass. Now the guide:The engine is right — `ErrorVal == "#DIV/0!"` is False because `ErrorVal` only equals other `ErrorVal`s. My smoke test compared against a string. Verifying:All green. Final state of the deliverables:Done — a working spreadsheet engine, built from scratch in the workspace:

- **`spreadsheet.py`** (727 lines) — the engine: A1 addresses, tokenizer, recursive-descent parser with Excel precedence (`-2^2 = 4`, `2^3^2 = 64`, postfix `%`), ranges, 11 functions (`SUM AVERAGE MIN MAX COUNT COUNTA IF ABS ROUND SQRT POWER`), lazy `IF`, Excel-style error values (`#DIV/0! #VALUE! #NAME? #NUM!`), and automatic recalculation via a dependency graph with Kahn's topological sort — cycle detection falls out of the topo sort for free as `#CYCLE!`.
- **`test_spreadsheet.py`** — 34 tests, all passing: precedence, coercion rules, error propagation, diamond dependencies, dep-edge cleanup when formulas are replaced, cycle creation/recovery, display grid.
- **`README.md`** — a build-your-own-x style guide: architecture diagram, the six steps (addresses → tokenizer → parser → evaluation → dependency graph → recalculation), documented deviations from Excel, and extension exercises (undo/redo, `$` refs, VLOOKUP, iterative calculation, range-granular deps).

Two bugs caught and fixed during verification: aggregates originally skipped error values inside ranges (`=SUM(A1:A1)` over a `#DIV/0!` cell returned 0.0 instead of propagating), and one test asserted the wrong display row.

```python
from spreadsheet import Sheet
s = Sheet()
s.set("A1", "3"); s.set("A2", "4")
s.set("A3", "=SUM(A1:A2)"); s.set("A4", "=A3*2")
s.set("A1", "10")
s.get("A4")   # 28.0 — everything downstream recalculated
```