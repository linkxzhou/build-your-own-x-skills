The user says their HTML parser loses text when the page has unclosed `<p>` tags. This is a debugging task. I need to look at their code first. Let me explore the workspace to find the parser.

Let me start by looking at the workspace structure.The workspace only contains the skills directory and AGENTS.md. There's no user HTML parser code in the workspace. Let me check AGENTS.md to see if there's context.

The user says "My HTML parser loses text when the page has unclosed <p> tags." But there's no parser code in the workspace. Let me read AGENTS.md to see what's there.Unclosed `<p>` is valid HTML — the end tag is optional. Browsers close a `<p>` implicitly when the next block-level start tag appears (`<div>`, `<h1>`–`<h6>`, `<ul>`, `<table>`, another `<p>`, …) or when the parent element ends. A parser that only closes elements on an explicit `</p>` breaks here, and text loss almost always comes from one of three spots:

1. **Text buffered until a close tag.** If character data accumulates in a pending buffer that only flushes when `</tag>` is seen, an unclosed element's text never gets committed. Fix: append text to the current open node immediately on `handle_data`.

2. **EOF teardown drops content.** At end of input, walk the open-element stack top-down and close each element properly so its subtree (including text) attaches to the parent. Clearing the stack or bailing out on "unclosed tag" errors discards everything inside.

3. **Missing implied-end-tag rule.** Per the HTML5 "in body" insertion mode, a start tag in the block set must first close an open `<p>` (the "close a p element" step). If that rule is missing, the second `<p>` nests inside the first and text lands in the wrong node — or gets skipped entirely if the parser rejects nested `<p>`.

Sketch of the fix (Python-ish):

```python
BLOCK_CLOSES_P = {"address","article","aside","blockquote","details","div","dl",
                  "fieldset","figcaption","figure","footer","form","h1","h2","h3",
                  "h4","h5","h6","header","hgroup","hr","main","menu","nav","ol",
                  "p","pre","section","table","ul"}

def handle_starttag(self, tag, attrs):
    if tag in BLOCK_CLOSES_P and self.p_in_button_scope():
        self.close_element("p")           # implied end tag
    self.push(Node(tag, attrs))

def handle_data(self, text):
    self.current().append_text(text)      # commit immediately, no buffering

def finish(self):                          # call at EOF
    while self.open_elements:
        self.close_element(self.open_elements[-1].tag)
```

`p_in_button_scope()` is the HTML5 scoping check: walk the stack from the top, stop at scope boundaries (`html`, `table`, `td`, `th`, `caption`, `button`, `template`, …), return whether a `p` was seen. A plain "is there a `p` above the nearest boundary" walk is fine for a hand-rolled parser.

Paste the parser's tag-handling and EOF code and I'll point at the exact line that's dropping the text.