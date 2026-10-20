The user wants to build a tiny GPT from scratch to understand transformers. This matches the build-your-own-x skill — specifically the "interpreter/compiler/programming language... neural network, an LLM" category. The skill description explicitly says: "Use it whenever someone wants to understand how a tool works by building their own... Chinese triggers... It picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution."

So I must read the SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest of it, and also find the relevant track skill. The learner wants to build a tiny GPT — that maps to "LLM" or "neural network" category. Let me read the rest of the SKILL.md and check the skills directory.The learner named the topic: a tiny GPT → `ai-model` track. Reading the track skill now (mandatory per the router).The track points to the LLM guide (rasbt/LLMs-from-scratch) for a GPT. There's a per-tutorial skill for it — reading it for article-specific detail before I set up the workspace.The track is clear: `ai-model` → LLM path, upstream tutorial [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch). Workspace is empty, Python 3.14 is available, torch is not. Recording the exploration and plan, then scaffolding.Now execute s1–s4. First download the corpus. Try curl first; fallback to http_request.Corpus is in place (1,115,394 bytes). Now the skeleton files, plus verifying the unique-char count.Everything is set up. The checkpoint harness runs and fails at the TODO as expected pre-implementation. Corpus verified: 1,115,394 chars, 65 unique.

Update todos: s1–s4 completed, s5 in_progress (learner's turn). Then write the coaching turn per the skill's output format:
- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton/TODO list, not the full answer
- How to check it: command + expected output
- Stuck? one hint at a time

Keep it tight. Credit upstream tutorial with exact link. Mention pip install torch for milestone 2 (learner runs it themselves — I must not run installs).**Where we are:** Milestone 1 of 7 — data + tokenizer. Project scaffolded in `tinygpt/`, following the LLM path of the build-your-own-x AI-model track, based on [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch).

**The concept.** A GPT reads numbers, so the first layer of the whole system is a tokenizer: text → integer ids, and ids → text. We start character-level: the vocabulary is simply the 65 unique characters in tiny Shakespeare (already downloaded to `tinygpt/data/input.txt`, 1.1 MB). Every model decision later — embeddings, the output layer — is sized by this vocab.

**What to write next.** Open `tinygpt/tokenizer.py` and fill in 4 TODOs:

1. `CharTokenizer.__init__` — build `stoi` (char→id) and `itos` (id→char) from the sorted unique characters, plus `vocab_size`.
2. `encode` — map each character to its id.
3. `decode` — map ids back to a string.
4. `train_val_split` — hold out the last 10% as validation.

Two lines each, roughly. The point is to feel that "the model's world" is just these 65 integers.

**How to check it:**

```
cd tinygpt
python3 check_m1.py
```

Passes when every line shows `[PASS]` and it prints `MILESTONE 1 PASSED` — vocab size 65, encode/decode round-trips on samples and on the first 1000 chars, and a 90/10 split. When it passes, log the result in `PROGRESS.md`.

**Stuck?** Ask and you get one hint at a time. Once you pass, we go to milestone 2: a bigram baseline — the dumbest possible language model, whose val loss becomes the number your transformer has to beat. For that one you'll need PyTorch (CPU is fine): `pip install torch`.