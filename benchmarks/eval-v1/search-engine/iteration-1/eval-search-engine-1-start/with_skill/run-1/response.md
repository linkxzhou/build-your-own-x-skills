The user wants to build a small search engine with an inverted index and wants coaching. This matches the build-your-own-x skill — "build your own search engine" / inverted index. The skill description says: use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project... It picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution.

So I must read the SKILL.md first before doing anything else.The file was truncated. I need to see the category map to find the right slug for a search engine / inverted index. Let me read more of the file.The topic maps to the `search-engine` track. Reading the track skill now — it's mandatory before coaching.Now let me read the tutorials reference file to know what upstream tutorials exist for search engines, so I can credit and link one.Typo in my path. Correcting:I have the track skill and tutorials. Now, per the coaching workflow:

1. Agree on scope: language, target, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide — Python default. The best matches for "small search engine with an inverted index":
   - "Building a Vector Space Indexing Engine in Python" (boyter.org) — classic, builds inverted index + vector space ranking.
   - "Finding Important Words in Text Using TF-IDF" (stevenloria.com) — TF-IDF focused.
   - Redis-based one — needs Redis server, extra dependency.

The learner said "small search engine with an inverted index" — the vector space one covers inverted index + ranking nicely. But per skill: ask at most 2 short questions (language, and maybe scope), suggest defaults.

The skill says: "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care."

So my first turn should:
- State where we are (milestone plan overview).
- Ask up to 2 questions: language (default Python), corpus choice (default: a folder of markdown/text files).
- Propose the milestone list and the tutorial link.
- Give them milestone 1 to start? The skill says agree on scope first, then start milestone 1. I can propose the plan and ask the 2 questions, and optionally give them a head start on milestone 1 with the tokenizer concept so they can begin immediately. That's good coaching: give the concept + skeleton for milestone 1 so they can start while answering.

Actually, to keep it tight: ask the 2 questions, present the milestone table (7 milestones, maybe trimmed), credit the tutorial, and give milestone 1's concept + skeleton + checkpoint so they can start right away with the default. If they answer differently, we adjust.

Also per output format for each turn:
- Where we are: milestone N/total
- The concept: short
- What to write next: skeleton or TODO list, not full answer
- How to check it: command + expected output
- Stuck? One hint at a time.

I should also check the workspace — is there an existing project? Let me glob quickly to see what's in the workspace. That's a read-only action, fine to do. Let me check for existing files.

Also should I use explore/plan tools? The developer instructions say: before modifying code, call explore once. I'm not modifying code yet — coaching. The plan tool is for multi-step changes. This is a coaching conversation; the skill defines the workflow. I'll keep it light: a quick glob to see the workspace, then respond. No code edits yet.

Let me glob the workspace root.Workspace is empty apart from the skill files, so we start fresh. Here's the setup.

## The plan

Following the build-your-own-x search-engine track. Primary reference: [_Building a Vector Space Indexing Engine in Python_](https://boyter.org/2010/08/build-vector-space-search-engine-python/) (Python is the default language for all guides in this track; the TF-IDF article [stevenloria.com/tf-idf](https://stevenloria.com/tf-idf/) is a good second reference when we hit ranking).

| # | Milestone | You'll learn | Checkpoint |
|---|---|---|---|
| 1 | Corpus + tokenizer | normalization, stopwords, stemming | `tokenize("Running dogs!") == ["run", "dog"]` |
| 2 | Inverted index | postings lists, doc ids | index of 3 tiny docs matches a hand-written expectation |
| 3 | Boolean queries | postings intersection/union | `cat AND dog` returns exactly the right doc ids |
| 4 | Ranking | TF-IDF or BM25 | fixture query's top hit is the doc you judged best |
| 5 | Persistence + speed | save/reload index | query over 10k docs in < 100 ms |
| 6 | Interface | CLI, snippets, highlighting | `search "query"` prints top 5 with highlighted snippets |
| 7 | Stretch | vectors / click feedback | precision@5 improves on a judged set |

Each milestone ends in a runnable check before we move on. You write the core; I scaffold, review, and debug with you.

## Two questions (defaults in parentheses)

1. **Language** — Python? (default: Python 3, stdlib only)
2. **Corpus** — what do you want to search? (default: a folder of `.md`/`.txt` files; a Wikipedia abstract dump is a fun upgrade later)

Say "go with the defaults" or override, and we start.

## Milestone 1 — you can start now

**Concept.** A search engine never scans documents at query time; it looks words up in an index. Everything downstream depends on how text becomes terms: lowercase, strip punctuation, optionally drop stopwords and stem. Consistency matters more than cleverness — the same function must run at index time and query time, or lookups miss.

**Skeleton** — create `search/tokenizer.py`:

```python
import re

STOPWORDS = set()  # fill in later

def tokenize(text: str) -> list[str]:
    # TODO 1: lowercase
    # TODO 2: split on non-alphanumeric (hint: re.findall(r"[a-z0-9]+", ...))
    # TODO 3: remove stopwords
    # TODO 4 (stretch): naive stemming — strip trailing "ing", "ed", "s"
    raise NotImplementedError
```

**Check** — `python -c "from search.tokenizer import tokenize; print(tokenize('Running dogs!'))"` should print `['run', 'dog']`.

Write it, run the check, and paste the output — pass or fail, we debug from there. First hint if you get stuck on stemming: order matters, strip `"ing"` before `"s"` or "dogs" → "dog" still works but "running" → "runn" needs a doubled-consonant fix.Scaffolding milestone 1 in your workspace now — skeleton only, TODOs intact.Skeleton is in place at `search/tokenizer.py` — milestone 1/7, with a self-checking harness at the bottom.

**Your move:** fill in the four TODOs. The `...` placeholders are the only spots to touch.

**Check:** `python3 search/tokenizer.py` — done when all three lines print `ok` and the exit code is 0. The cases cover lowercasing, punctuation stripping, and stem-order (`jumped jumps jump` → three identical terms).

**If stuck, ask for one hint at a time** — first one is free: for TODO 2, `re.findall` with a class like `[a-z0-9]+` after lowercasing handles both splitting and punctuation in one pass.

Paste the output when you run it — pass or fail, we debug from the real result, then log the milestone in `PROGRESS.md` and move to the inverted index.