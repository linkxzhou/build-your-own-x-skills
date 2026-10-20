The user has a classic operator precedence bug in a hand-written parser. They parse left-to-right: parse a number, then while next is an operator, combine. So `1 + 2 * 3` becomes `(1 + 2) * 3 = 9` instead of `1 + (2 * 3) = 7`.

This matches the build-your-own-x skill trigger: "my own interpreter/parser" — stuck/debugging midway through their own from-scratch implementation. The skill description says: "OR is stuck/debugging midway through their own from-scratch implementation (e.g. 'my own git's hash differs from real git', 'my ray tracer has shadow acne', 'my CHIP-8 draws garbage', 'my toy kernel triple-faults')". A parser precedence bug fits this pattern — it's a from-scratch implementation debugging question. The skill says to read SKILL.md BEFORE doing anything else.

Let me read the skill first.

Actually, let me think about whether this matches. The skill is about "learning by rebuilding real software from scratch" and coaching step by step instead of dumping a finished solution. The user's question is a parser precedence bug — a classic. The trigger examples include debugging one's own from-scratch implementation. A hand-written expression parser is exactly the kind of thing in "an interpreter/compiler" track. So yes, I should read the skill.

Let me read it.The skill was truncated. Let me read the rest of it, and also check the track skills directory for an interpreter/compiler track skill.This maps to the `programming-language` track. The skill mandates reading the track skill before answering, even for debugging turns.The track skill is truncated. Let me read the rest.The track skill's debugging rule applies: minimal fix, then a runnable check. Let me grab the exact tutorial links for precedence parsing from the references so I can credit the right one.**Where we are:** milestone 2/7 (parser + precedence) of the programming-language track. Your bug is exactly the checkpoint case this milestone exists to catch.

**The concept:** a flat left-to-right loop has one precedence level, so every operator binds equally and `1 + 2 * 3` groups as `(1 + 2) * 3`. Precedence comes from layering the grammar: each tier parses only its own operators and delegates its operands to the next-higher tier. The `+` loop calls `parse_term()`, which greedily consumes `2 * 3` before returning — so the multiplication is already grouped when the addition sees it. This is the standard recursive-descent fix; Crafting Interpreters covers it in the parsing chapter (http://www.craftinginterpreters.com/).

**The minimal fix** — split your one loop into two functions, same shape in any language:

```python
def parse_expr():            # tier 1: + -
    left = parse_term()
    while peek() in ('+', '-'):
        op = advance()
        left = BinOp(op, left, parse_term())
    return left

def parse_term():            # tier 2: * /
    left = parse_factor()
    while peek() in ('*', '/'):
        op = advance()
        left = BinOp(op, left, parse_factor())
    return left

def parse_factor():          # tier 3: numbers, ( expr ), unary
    if match('('):
        e = parse_expr(); expect(')'); return e
    return Num(expect_number())
```

Your current code is `parse_expr` with the `parse_term` body inlined into it; the only change is extracting the `* /` loop into its own function and having `+ -` call it for the right operand. Entry point becomes `parse_expr()` instead of the flat loop.

When you later add comparisons, `&&`, etc., you'd keep adding tiers — at 4+ tiers, switch to precedence climbing / Pratt parsing (one loop driven by a binding-power table), which is the generalization of this same idea.

**How to check it:** run your parser on these four inputs:

```
1 + 2 * 3      → 7
(1 + 2) * 3    → 9
2 * 3 + 4      → 10
8 - 3 - 2      → 3   (left-associative within a tier)
```

If `8 - 3 - 2` gives 7, your tier-1 loop is building the tree right-associatively — the `left = BinOp(op, left, ...)` accumulation fixes that too.