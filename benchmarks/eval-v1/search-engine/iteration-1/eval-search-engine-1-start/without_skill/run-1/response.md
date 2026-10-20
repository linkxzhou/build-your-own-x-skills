The user wants to build a small search engine with an inverted index, and they want coaching. Let me first look at the workspace to understand the context — the cwd is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-search-engine-1`, which suggests this is a "build your own X" style project directory. Let me explore what's there first.

The user said "Coach me" — so they want guidance, not for me to write all the code for them. I should act as a coach: explain the concepts, lay out a roadmap, and guide them through building it themselves.

Let me check the workspace first to see if there's existing code or a README.Empty workspace — clean slate. Let's do this properly.

## The mental model

A search engine flips your data around:

- **Forward index** (what you have naturally): `doc → [words]`
- **Inverted index** (what search needs): `word → [docs containing it]`

Each term maps to a **posting list** — a sorted list of entries, one per doc that contains the term. The whole game is: build those lists, then answer queries by merging them.

```
"the cat sat"  →  cat  → [doc1]
                  sat  → [doc1]
                  the  → [doc1, doc2]   ← posting list
```

A query like `cat AND sat` = intersect the two posting lists. Ranking = score each surviving doc (TF-IDF or BM25).

## Roadmap (5 milestones)

1. **Tokenizer** — text → normalized tokens (lowercase, strip punctuation). Deceptively subtle; this defines what "a word" even is.
2. **Indexer** — assign integer docIDs, build `term → posting list`. Print your index and eyeball it.
3. **Boolean queries** — `AND` (merge-intersect two sorted lists), `OR`, `NOT`. This is where the inverted index pays off: you touch only docs that match.
4. **Ranking** — score docs with TF-IDF, then upgrade to BM25. Now queries return "best first" instead of "any order".
5. **Phrase search** — store word *positions* in postings, so `"cat sat"` matches adjacent words only. Optional but satisfying.

## Your first exercise (Milestone 1+2, ~30 min)

Write a program that:

1. Has 5–10 hardcoded documents (just strings).
2. Tokenizes each one.
3. Builds the index as `dict[str, list[int]]` — term → sorted docIDs.
4. Prints the whole index.

Then hand-write a query or two and intersect lists manually to sanity-check.

Pick a language and tell me when it's done — paste the index output and I'll review it, then we'll do posting-list intersection properly (the merge algorithm matters: it's O(n+m) on sorted lists, and it's the heart of the engine).

Three questions to calibrate:

1. **Language?** Python is fine for learning the concepts. Go/Rust/C if you also want the performance story (memory layout, compression).
2. **Corpus?** Toy strings first, but what's the fun target — local files, Project Gutenberg books, your own notes?
3. **Depth?** Stop at a working ranked search, or push into the fun stuff (skip pointers, delta-encoded postings, disk-based index)?