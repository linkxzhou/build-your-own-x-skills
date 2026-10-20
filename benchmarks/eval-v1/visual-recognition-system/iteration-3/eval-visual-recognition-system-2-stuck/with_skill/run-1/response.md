The user says: "My classifier gets 99% on training data but 40% on new photos." This is a classic overfitting / distribution shift problem. The skill "build-your-own-x" mentions it handles debugging midway through their own from-scratch implementation — e.g., "my ray tracer has shadow acne", "my CHIP-8 draws garbage". Is a classifier a from-scratch implementation? Possibly — the user says "my classifier", which could be a hand-built neural network or a scikit-learn model. The skill description says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems skills, asks which build-your-own project to start with, OR is stuck/debugging midway through their own from-scratch implementation (e.g. 'my own git's hash differs from real git', 'my ray tracer has shadow acne', 'my CHIP-8 draws garbage', 'my toy kernel triple-faults')."

"My classifier gets 99% on training data but 40% on new photos" — this could be someone building their own neural network from scratch (a common build-your-own-x project: neural networks). The trigger includes "我自己写的 X 出 bug/卡在第 N 步" (my own X has a bug / stuck at step N). A classifier with 99% train / 40% test is a classic symptom of overfitting OR a bug in a from-scratch implementation.

Hmm, but it could also just be a generic ML question about a scikit-learn/tensorflow classifier. The skill says to read SKILL.md before doing anything else when the task matches. The match is plausible but uncertain. The skill is about learning by rebuilding real software. "My classifier" — if they built it themselves, this matches "stuck/debugging midway through their own from-scratch implementation". A neural network classifier is one of the listed topics ("a neural network").

Given the ambiguity, I think the safe move is to read the SKILL.md first (it's cheap) and see whether it applies. The instruction says: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else". The task plausibly matches (debugging their own from-scratch classifier). Let me read it.

Actually, let me think about whether this is really a build-your-own-x situation. The user gives one line: "My classifier gets 99% on training data but 40% on new photos." There's no workspace context mentioned. Let me check the workspace for files — maybe there's a project. I should glob for Python files etc. But first, per instructions, read the skill if it matches.

The skill's debugging trigger: "my ray tracer has shadow acne", "my CHIP-8 draws garbage" — these are from-scratch implementations. "My classifier gets 99% train but 40% on new photos" is analogous: a symptom report from their own ML project. If they built the classifier from scratch (e.g., a neural net), the skill applies. If they're using sklearn, it's a generic ML debugging question.

I'll read the SKILL.md to decide, and also glob the workspace to see if there's any code. These are independent read-only calls, so I can do them in parallel.

Then I'll respond with a diagnosis: overfitting vs. data leakage vs. distribution shift vs. preprocessing mismatch (train/test augmentation differences), and concrete debugging steps. Keep it tight per tone guidelines.

Let me do: read SKILL.md + glob for code files in parallel.The workspace only contains skill files — no user project code. So the user is asking a general ML debugging question: "My classifier gets 99% on training data but 40% on new photos."

Does the build-your-own-x skill apply? The skill is about learning by rebuilding real software from scratch. The user's message is a symptom report about a classifier — could be a from-scratch neural net, could be sklearn. There's no workspace code. The skill's debugging trigger is for "stuck/debugging midway through their own from-scratch implementation". A classifier trained on photos could be a hand-built CNN. But I don't know that they built it from scratch. The skill says to read the track skill first if mapped. The topic would be "neural network" — there's a skills/ directory with tracks. But before committing to the tutor workflow, I should consider: the user hasn't said they built it from scratch. The message is a one-line symptom.

Hmm. The skill instruction says "Use it whenever someone ... is stuck/debugging midway through their own from-scratch implementation". "My classifier" — ambiguous. The phrase "new photos" suggests an image classifier. If they built it themselves (e.g., a from-scratch CNN), the skill applies and I should read the neural-network track skill. If they're using a library, it's a generic ML debugging question and the skill doesn't apply.

Given ambiguity, the skill workflow says: "If they are unsure, ask at most 2 short questions". But the user isn't asking to start a project; they're reporting a bug. The skill's debugging rule: "When the learner is stuck mid-way, still read the track skill first, give the minimal fix, and end with a runnable check."

I think the right move: this is plausibly a from-scratch classifier (the skill covers "a neural network" as a topic). But honestly, the most common interpretation of "my classifier gets 99% on training data but 40% on new photos" is a general ML question about overfitting/data issues. The skill is for build-your-own-x learning projects. Without evidence the user built the classifier from scratch, invoking the full tutor workflow would be presumptuous.

However, the system prompt says to read the skill BEFORE doing anything else when the task matches — I did read it. Now I need to decide whether it matches. The match hinges on whether this is a from-scratch implementation. I can't verify from the workspace (no user code). The safest path: answer the ML debugging question directly (that's what any senior engineer would do), and since the skill might apply, I could check the neural-network track skill to see if it has debugging guidance relevant to a from-scratch classifier.

Actually, let me reconsider. The skill description explicitly lists debugging triggers like "my ray tracer has shadow acne" — symptom reports. "My classifier gets 99% train / 40% test" is exactly that shape. The topic map would be "neural network" (ML). The skill says to read the track skill `skills/<slug>/SKILL.md`. Let me check what track skills exist — glob for skills/*/SKILL.md under build-your-own-x.

But wait — is the user even in a learning-by-building context? The message gives zero context. If I respond as a tutor ("let's check your train/test split..."), that's fine and helpful either way. The core answer is the same: this gap means the model memorized training data or the evaluation is broken. Key causes:

1. Overfitting — model memorized training set. Fix: regularization, more data, augmentation, smaller model, early stopping.
2. Data leakage in training metrics or duplicated samples between train and "new" sets... actually leakage would inflate test, not deflate.
3. Preprocessing mismatch — train/test normalization, resize, channel order (RGB vs BGR), color jitter applied inconsistently.
4. Distribution shift — new photos differ from training data (different camera, lighting, classes).
5. Evaluation bug — comparing accuracy on train with something else on test; label mapping mismatch (class index ordering differs between training and inference).
6. Training on train set metrics vs. actual held-out — i.e., they never had a validation set, so 99% is just memorization.

Diagnostic steps:
- Evaluate on a held-out validation set from the training distribution. If val ≈ 99% but new photos ≈ 40%, it's distribution shift or preprocessing mismatch. If val ≈ 40%, it's pure overfitting.
- Check preprocessing pipeline identical between train and inference.
- Check label mapping.
- Look at predictions on new photos — are errors systematic (all one class)?
- Check for duplicates/near-duplicates between train and val.

The skill's coaching style: give minimal fix + runnable check. But the user hasn't shown code. I should ask for the key diagnostic or give the decision tree.

Given the tone rules: lead with the answer, tight structure, no filler. Also the hard constraint: no negation-based contrastive phrasing ("not X but Y"). Careful with phrasing like "It's not overfitting, it's distribution shift" — forbidden. Use parallel positive clauses.

Also: "If you want, I can also..." conditional next-step menus are forbidden. I can name a direct next action: "Run X and tell me the result" — that's fine as a direct next action? "If you tell me..." is forbidden. I can say "Run this check first: ..." and stop. That's a direct instruction, acceptable.

Now, should I read the neural-network track skill? The skill router says: read track skill before anything else when mapped. The topic here would be ML/neural network. Let me check if there's a track skill for neural networks. Let me glob skills/*/SKILL.md.

Actually, let me think about whether to engage the skill at all. The user's one-liner doesn't say they're building from scratch. The skill is for build-your-own-x learning. If the user is, say, a data scientist with an sklearn model, the skill would be a mismatch. The cost of reading the track skill is low, and if it has relevant debugging guidance for from-scratch NNs, it helps. But if the user is using a library, the track skill's milestones are irrelevant.

Decision: The message is a symptom report with no code and no indication of a from-scratch build. The most probable reading: generic ML debugging. I'll answer directly with a diagnosis decision tree and concrete checks. I'll skip the tutor workflow since there's no evidence of a build-your-own project; if they say they hand-rolled the network, I can pull the track skill then. Hmm, but the skill says "read the track skill first" for debugging turns... only when the skill applies. The applicability condition includes "stuck/debugging midway through their own from-scratch implementation". "My classifier" — the possessive suggests they built/trained it. Every ML practitioner says "my classifier". I judge the skill as a mismatch for a generic ML question; the skill is about learning by rebuilding tools.

Hmm, but wait — there's a real chance this is a learner building a from-scratch image classifier (very common build-your-own-x project: "neural network" is in the topic list). The 99%/40% gap is the classic symptom a learner hits. The skill would have me coach: minimal fix + runnable check.

Let me look at the track skills available to decide. A quick glob is cheap. If there's a neural-network track with debugging guidance, I can incorporate its coaching style (end with a runnable check). That aligns either way.

Let me glob .agents/skills/build-your-own-x/skills/*/SKILL.md.The `visual-recognition-system` track matches an image classifier. Reading it before answering, per the router.That gap means one of three things: the model memorized the training set, the inference path differs from training, or the new photos come from a different distribution. One cheap check tells you which.

**Check 1 — held-out validation from your own training data.** Split 10–20% of the training photos into a val set the model has never seen, run the exact training preprocessing, and evaluate:

```python
model.eval()                      # if PyTorch; disable dropout/augmentation
val_acc = evaluate(model, val_loader)
print(f"val_acc={val_acc:.2%}")
```

- **val ≈ 99%** → the model generalizes within its training distribution; the problem lives in the new photos or the inference path. Go to Check 2.
- **val ≈ 40%** → plain overfitting; the 99% was memorization. Go to Check 3.

**Check 2 — diff training vs. inference (val high, new photos low):**
- *Preprocessing parity:* push one training image through the inference pipeline and compare the resulting tensor against the training version. Usual culprits: RGB vs BGR, missing `/255` or normalization, different resize interpolation, augmentation accidentally active at inference.
- *Label mapping:* print the confusion matrix on the new photos. Errors piled into one class, or predictions shifted by a constant index, mean the class order at inference differs from training.
- *Leakage:* near-duplicate photos shared between train and val inflate val accuracy while real new photos fail — check for duplicates.
- *Distribution shift:* put 20 misclassified new photos next to training samples of the same class. Different camera, lighting, or background means you need training data (or augmentation) that matches deployment.

**Check 3 — fix overfitting (val low), in order of impact:**
1. More data plus aggressive augmentation (flips, random crops, color jitter).
2. Early stopping on val accuracy.
3. Weight decay / dropout, or a smaller model.
4. A pretrained backbone — training a CNN from scratch on a small photo dataset almost always lands here.

Also verify where the 99% came from: accuracy measured on data the model trained on measures memorization and says nothing about generalization.

Run Check 1 and the confusion matrix on the new photos, and the two numbers will localize the bug immediately.The internal message says my last reply contained no tool call and I must emit a real tool call this turn. The user's original question was a diagnostic question about their classifier. There's no project code in the workspace (only skill files). The instruction: take exactly ONE concrete action via a tool call.

What's the most useful concrete action? I could create a small diagnostic script in the workspace that the user can run against their model/data — a validation-split checker / preprocessing parity checker. That aligns with the coaching style (give a runnable check) and satisfies the tool-call requirement.

But wait — the skill says "Stay in the learner's workspace... Keep scratch files and experiments inside the project (for example ./scratch/)". There's no user project here; workspace root only has .agents. Creating a diagnostic script at workspace root or ./scratch/ is reasonable.

Let me write one self-contained script `scratch/diagnose_gap.py` that:
1. Splits existing training data into train/val and reports val accuracy (if given a model + data loader — but we don't know their framework).

Hmm, without knowing their stack, a generic script can't plug into their model. Better: a framework-agnostic checklist script? That's fluff.

Alternative concrete action: write a runnable diagnostic script that works with PyTorch (most common) with clearly marked TODO hooks where they wire in their model and data, implementing:
- Check 1: train/val split evaluation
- Check 2: preprocessing parity diff (tensor stats comparison)
- Confusion matrix on new photos

Actually, a cleaner single action: write `scratch/diagnose_gap.py` — a PyTorch diagnostic that takes their model + two DataLoaders (train, new_photos) via small editable config at top, then prints: val accuracy on a held-out split, per-class accuracy/confusion on new photos, and tensor stats (mean/std per channel) for both pipelines to expose preprocessing mismatch.

Keep it compact but real. Also per skill: never install anything; use only what's there — I can't verify torch is installed. I could check with bash... but I must take exactly ONE tool call. The instruction says exactly one concrete action. So: one `write`.

Let me write the script carefully.

Script design:

```python
"""Diagnose a 99%-train / 40%-new-photos gap.

Fill in MODEL, TRAIN_LOADER (or TRAIN_DS), NEW_LOADER below, then:
    python scratch/diagnose_gap.py
It prints three numbers that localize the bug:
  1. val_acc   — accuracy on a held-out slice of your own training data
  2. new_acc   — accuracy on the new photos
  3. per-channel input stats for both pipelines (preprocessing parity)
plus a confusion matrix on the new photos.
"""
```

Implementation with torch, numpy. Steps:

- config section: MODEL = None  # your nn.Module, already loaded with weights
- TRAIN_DS = None  # training dataset (pre-augmentation if possible)
- NEW_DS / NEW_LOADER
- CLASS_NAMES optional

Functions:
- `held_out_split(ds, frac=0.15, seed=0)` → random_split
- `evaluate(model, loader)` → accuracy, confusion matrix (num_classes inferred from preds/targets)
- `channel_stats(ds, n=200)` → mean/std per channel over samples, computed on the transformed tensors — exposes RGB/BGR, /255, normalization mismatches.

Main:
- build val loader from TRAIN_DS
- print val_acc
- print new_acc + confusion matrix + top confusions
- print stats for both datasets
- decision hints printed based on val_acc vs new_acc.

Keep code correct. Use torch.no_grad, model.eval(). Device: cpu default; try cuda if available.

Confusion matrix: N = max(num_classes, preds.max()+1, targets.max()+1).

Edge cases: if MODEL is None, exit with message telling them to wire it in.

Also print per-class accuracy on new photos to spot systematic class errors.

Write it to scratch/diagnose_gap.py. One tool call. Then a brief message: what it does, how to run, what the outputs mean. Keep short. No "if you want" menus.

Let me write the code carefully to be actually runnable once they fill in the three objects.

```python
#!/usr/bin/env python3
"""Diagnose a high-train / low-new-photos accuracy gap.

Wire in your model and datasets in the CONFIG block, then run:

    python scratch/diagnose_gap.py

It prints the three numbers that localize the bug:
  1. val_acc  -- accuracy on a held-out slice of your own training data
  2. new_acc  -- accuracy on the new photos (+ confusion matrix)
  3. per-channel input stats for both pipelines (exposes RGB/BGR,
     missing /255, normalization or resize mismatches)
"""

import numpy as np
import torch
from torch.utils.data import DataLoader, random_split

# ----------------------------- CONFIG --------------------------------------
MODEL = None        # e.g. torch.load("model.pt"); put model.eval() state
TRAIN_DS = None     # full training dataset (images + labels, WITH transform)
NEW_DS = None       # the new photos dataset (same label space as training)
CLASS_NAMES = None  # optional list[str]; falls back to "class_i"
BATCH_SIZE = 64
VAL_FRACTION = 0.15
SEED = 0
# ---------------------------------------------------------------------------

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")


def make_loader(ds, shuffle=False):
    return DataLoader(ds, batch_size=BATCH_SIZE, shuffle=shuffle,
                      num_workers=0)


@torch.no_grad()
def evaluate(model, loader):
    model.eval()
    preds_all, targets_all = [], []
    for batch in loader:
        x, y = batch[0].to(device), batch[1]
        logits = model(x)
        preds = logits.argmax(dim=-1).cpu()
        preds_all.append(preds)
        targets_all.append(y)
    preds = torch.cat(preds_all).numpy()
    targets = torch.cat(targets_all).numpy()
    acc = float((preds == targets).mean())
    return acc, preds, targets


def confusion(preds, targets):
    n = int(max(preds.max(), targets.max())) + 1
    cm = np.zeros((n, n), dtype=int)
    for t, p in zip(targets, preds):
        cm[t, p] += 1
    return cm


def print_confusion(cm, class_names):
    names = class_names or [f"class_{i}" for i in range(len(cm))]
    w = max(len(n) for n in names) + 1
    header = "true\\pred".ljust(w) + "".join(n[:10].rjust(11) for n in names)
    print(header)
    for i, row in enumerate(cm):
        print(names[i].ljust(w) + "".join(str(v).rjust(11) for v in row))


def per_class_accuracy(cm, class_names):
    names = class_names or [f"class_{i}" for i in range(len(cm))]
    for i, row in enumerate(cm):
        total = row.sum()
        if total:
            print(f"  {names[i]:<20} {row[i]}/{total} = {row[i]/total:.0%}")


@torch.no_grad()
def channel_stats(ds, n_samples=200):
    """Mean/std per channel over raw transformed tensors.

    Training and inference tensors of the same photo should produce
    near-identical stats; a large gap means the preprocessing differs.
    """
    n = min(n_samples, len(ds))
    idx = np.random.RandomState(SEED).choice(len(ds), size=n, replace=False)
    acc = []
    for i in idx:
        x, _ = ds[int(i)]
        x = x.float()
        if x.ndim == 2:
            x = x.unsqueeze(0)
        acc.append(x.flatten(1).mean(1))
        # need per-channel mean and std separately
    ...
```

Hmm, let me write channel_stats more carefully: accumulate sum and sumsq per channel.

```python
@torch.no_grad()
def channel_stats(ds, n_samples=200):
    n = min(n_samples, len(ds))
    idx = np.random.RandomState(SEED).choice(len(ds), size=n, replace=False)
    s = ss = cnt = None
    for i in idx:
        x, _ = ds[int(i)]
        x = x.float()
        if x.ndim == 2:
            x = x.unsqueeze(0)
        c = x.shape[0]
        flat = x.reshape(c, -1)
        s = flat.sum(1) if s is None else s + flat.sum(1)
        ss = (flat ** 2).sum(1) if ss is None else ss + (flat ** 2).sum(1)
        cnt = flat.shape[1] if cnt is None else cnt + flat.shape[1]
    mean = s / cnt
    std = (ss / cnt - mean ** 2).sqrt()
    return mean.numpy(), std.numpy()
```

Note: variable channels across samples would break; assume consistent. Fine for a diagnostic.

Main:

```python
def main():
    if MODEL is None or TRAIN_DS is None or NEW_DS is None:
        raise SystemExit("Fill in MODEL, TRAIN_DS and NEW_DS in the CONFIG block first.")

    model = MODEL.to(device)

    n_val = max(1, int(len(TRAIN_DS) * VAL_FRACTION))
    n_train = len(TRAIN_DS) - n_val
    gen = torch.Generator().manual_seed(SEED)
    _, val_ds = random_split(TRAIN_DS, [n_train, n_val], generator=gen)

    val_acc, _, _ = evaluate(model, make_loader(val_ds))
    new_acc, preds, targets = evaluate(model, make_loader(NEW_DS))

    print(f"val_acc (held-out from training data): {val_acc:.2%}")
    print(f"new_acc (new photos):                  {new_acc:.2%}")
    print()

    cm = confusion(preds, targets)
    names = CLASS_NAMES
    print("Confusion matrix on new photos (rows=true, cols=predicted):")
    print_confusion(cm, names)
    print()
    print("Per-class accuracy on new photos:")
    per_class_accuracy(cm, names)
    print()

    for label, ds in (("train pipeline", TRAIN_DS), ("new-photo pipeline", NEW_DS)):
        mean, std = channel_stats(ds)
        print(f"{label:<20} per-channel mean {np.round(mean, 3)}  std {np.round(std, 3)}")
    print()

    if val_acc >= 0.9 and new_acc < 0.6:
        print("Reading: model generalizes within its training distribution.")
        print("Compare the two stat lines above: a large mean/std gap means the")
        print("preprocessing differs (RGB vs BGR, /255, normalization, resize).")
        print("If stats match, inspect the confusion matrix for a label-mapping")
        print("offset, then compare misclassified photos against training samples.")
    elif val_acc < 0.6:
        print("Reading: overfitting. The 99% was memorization.")
        print("Fix in order of impact: more data + augmentation, early stopping")
        print("on val_acc, weight decay/dropout or a smaller model, then a")
        print("pretrained backbone.")
    else:
        print("Reading: mixed. Both numbers are mid-range; check the confusion")
        print("matrix for classes that dominate the errors and add data there.")


if __name__ == "__main__":
    main()
```

Wait — random_split returns subsets; DataLoader over Subset works. Good.

One issue: `evaluate` assumes batch is (x, y) tuple — batch[0], batch[1]. Fine.

Also `MODEL` may need `.eval()` — evaluate() calls model.eval(). Good.

Potential issue: if their dataset returns dict or (x, y) with extra items — fine.

Also note: TRAIN_DS with augmentation — val slice would include augmentation; mention in comment that if the transform includes augmentation, val_acc is slightly pessimistic. Add a note in the docstring or comment.

The script is a diagnostic scaffold; per the skill, don't dump whole solutions — but this is a debugging turn: "give the minimal fix for their bug... end with a runnable check (command + expected output)". This script IS the runnable check. Good.

Where to put it: skill says keep scratch files inside the project, e.g. ./scratch/. Workspace root is the project here. `scratch/diagnose_gap.py`.

After writing, brief message: what it does, how to wire it, run command, expected output interpretation. Keep tight. Also mention: if torch isn't installed, print install command — per skill, I must not install; I can mention the command. Actually I shouldn't run anything. Just note: requires torch+numpy; if missing run `pip install torch numpy` themselves.

One tool call only: write. Then final text.

Double-check the confusion printing width math: header "true\pred".ljust(w) + names truncated to 10 chars rjust(11). Rows: name.ljust(w) + values rjust(11). Consistent.

Edge: `preds.max()` on empty array would fail — if NEW_DS empty, whatever; acceptable.

In channel_stats, `cnt` is per-channel count — same for all channels; fine.

`np.random.RandomState(SEED).choice(len(ds), size=n, replace=False)` — fine.

One more: `x, _ = ds[int(i)]` — if dataset returns (x, y) fine.

Also guard: if x has 3 dims already (C,H,W) fine; if (H,W) unsqueeze. If (H,W,3)? Unlikely from torchvision. Fine.

Write it.Created `scratch/diagnose_gap.py` — a runnable check that localizes the 99%/40% gap. Wire three objects into the CONFIG block at the top (`MODEL`, `TRAIN_DS`, `NEW_DS`), then:

```bash
python scratch/diagnose_gap.py
```

It prints:

1. `val_acc` — accuracy on a 15% held-out slice of your own training data. This is the fork in the road: high val + low new-photos points at the inference path or distribution shift; low val confirms overfitting.
2. Confusion matrix + per-class accuracy on the new photos — a constant index shift means the label mapping differs at inference; errors piled into one class means distribution shift.
3. Per-channel mean/std of the raw input tensors for both pipelines — a mismatch between the two lines exposes RGB/BGR swaps, missing `/255`, or normalization/resize differences.

The script ends with a printed reading of the numbers and the matching fix, ordered by impact. Requires torch + numpy already present; if missing, run `pip install torch numpy` yourself.