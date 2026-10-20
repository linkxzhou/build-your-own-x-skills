The user is asking about building an LLM from scratch without a GPU. This matches the build-your-own-x skill — specifically the LLM category. The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md BEFORE doing anything else, then follow it.

The trigger: "building an LLM from scratch" — this is a build-your-own-x question. Chinese triggers listed include 从零实现 etc. English: "building an LLM from scratch" clearly matches.

So I should read .agents/skills/build-your-own-x/SKILL.md first.The file was truncated. I need to see the category map to find the LLM slug. Let me read more of the file.The topic maps to the `ai-model` track. Reading the track skill now, as required.Truncated again. Let me read the rest of the file (lines 43 onward).Now let me read the tutorials reference to pick a guide that works on CPU.Yes — CPU is enough for the whole from-scratch learning path. The skill track for this (`ai-model`) states it up front: CPU is enough for tiny models; a GPU is an optional accelerator. The upstream guide we'd follow, [rasbt/LLMs-from-scratch](https://github.com/rasbt/LLMs-from-scratch), is explicitly designed to run on a laptop CPU.

What that means concretely:

- **Feasible on CPU:** a char-level or small-BPE GPT with ~1–10M parameters (2–6 layers, 128–384 embedding dim) trained on a ~1MB corpus like TinyShakespeare. Training runs take minutes to tens of minutes, and you'll see the loss curve drop and the model generate plausible text. This covers every concept that matters: tokenization, self-attention, transformer blocks, training loops, sampling, evaluation.
- **Out of reach on CPU:** pretraining anything GPT-2-sized (124M params on web-scale data). That's a GPU-cluster job. Loading pretrained weights and fine-tuning on CPU is possible but slow, and it's a stretch goal at most.

The milestone path (each ends with a runnable check):

1. Data + tokenizer — encode/decode round-trips, vocab size reported
2. Baseline model — a bigram model, val loss recorded
3. Core architecture — self-attention + transformer block; one batch overfits to near-zero loss
4. Training loop — val loss beats the baseline; checkpoint reloads
5. Sampling — temperature/top-k, generated text looks plausible
6. Evaluation — perplexity table vs. the baseline
7. Stretch — KV cache with a measured speed-up

Two scoping questions before we start milestone 1:

1. **Language:** Python + PyTorch is the default (all three upstream guides use it). OK, or do you prefer something else?
2. **Target:** default is a char-level GPT, ~10M params, trained on TinyShakespeare. Fine, or would you rather train on your own text corpus (code, lyrics, a book you like)?

One ground rule from the coaching workflow: I never run install commands for you. When we reach milestone 1 you'll run `pip install torch` yourself (CPU build is the default on machines without CUDA), and I'll give the exact command when it's needed.