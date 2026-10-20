The user wants to learn backpropagation by building a neural net from scratch with numpy. This matches the build-your-own-x skill — "build a neural network from scratch" is a classic build-your-own-x category. The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it.

Let me read the skill first.The file is truncated. Let me read the rest to find the neural network track slug.The track is `neural-network`. Reading the track skill now — it's mandatory before anything else.Let me check the tutorial list and any per-tutorial skills for numpy.The track skill points to a numpy-friendly guide. Since the learner named numpy, I'll check the victorzhou per-tutorial skill (closest match) and inspect the workspace + numpy availability in parallel.Scope is clear from your ask: Python + numpy (2.5.3 is already installed), and the closest upstream guide is [victorzhou.com — Intro to Neural Networks](https://victorzhou.com/blog/intro-to-neural-networks/). Recording the exploration note and project plan, then scaffolding milestone 1.Scaffolding milestone 1 now. First, computing the hand-check reference values with independent scalar math so the checkpoint literals are exact.Scaffold verified — the checkpoint fails cleanly on the TODO. Setting up progress tracking, then handing it to you.**Where we are:** milestone 1/7 — neuron + forward pass. Guide: [victorzhou.com — Intro to Neural Networks](https://victorzhou.com/blog/intro-to-neural-networks/).

**The concept.** A neuron is the atom of every network. It takes an input vector `x`, multiplies each feature by a learned weight `w`, adds them up with a learned offset `b`, and squashes the result through an activation:

```
z = w·x + b          # weighted sum + bias
y = sigmoid(z) = 1 / (1 + e^(-z))   # squashes any real number into (0, 1)
```

The weights decide how much each input matters; the bias shifts the firing threshold; sigmoid turns the raw score into something you can read as a probability. Everything later — layers, backprop, training — is just many of these wired together, so getting this line of math solid in your head pays off for the whole project.

**Your workspace is ready:**
- `neuron.py` — two TODOs: implement `sigmoid`, then `Neuron.forward`. That's the entire milestone, ~2 lines each.
- `check_m1.py` — the checkpoint. It compares your neuron against values I computed by hand with plain scalar math (e.g. case A: `w=[0.5,-0.6]`, `b=0.1`, `x=[1,2]` → `z = 0.5 − 1.2 + 0.1 = −0.6` → `sigmoid(−0.6) ≈ 0.354343693774…`), so it can't be fooled by hardcoding.

**How to check it:**

```
python3 check_m1.py
```

Expected when done: three `PASS case …` lines, then `MILESTONE 1 PASSED`.

Hand-compute case A on paper first — predict the number before running the check. That prediction is the actual lesson of milestone 1. If you get stuck, ask and I'll give one hint at a time.