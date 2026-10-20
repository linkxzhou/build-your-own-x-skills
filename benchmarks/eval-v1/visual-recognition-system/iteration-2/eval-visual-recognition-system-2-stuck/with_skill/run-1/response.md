The user says: "My classifier gets 99% on training data but 40% on new photos." This is a classic overfitting / data leakage / distribution shift problem. There's a skill "build-your-own-x" — but this doesn't match that skill. The skill is about learning by rebuilding software from scratch. This is a debugging question about a classifier. The skill description says: "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems skills, asks which build-your-own project to start with, OR is stuck/debugging midway through their own from-scratch implementation (e.g. 'my own git's hash differs from real git', ...)". This is a classifier — could be their own from-scratch implementation? The examples are about from-scratch implementations of tools (git, CHIP-8, ray tracer). A classifier getting 99% train / 40% test is a standard ML debugging question, likely using sklearn or similar. The skill is about build-your-own-x projects — building Git, Redis, etc. A classifier isn't really in that list (neural network is mentioned: "a neural network"). Hmm, "a neural network" is in the list. But the user's question is about debugging model performance, which is a standard ML question. The skill says it's for "stuck/debugging midway through their own from-scratch implementation". If the user built their own neural network from scratch, this could match. But we don't know. The question is generic — "My classifier gets 99% on training data but 40% on new photos." This is most likely a standard ML debugging question about overfitting/data leakage/distribution shift.

I think the skill doesn't match well enough — the user isn't asking to build something from scratch or learn how a tool works by rebuilding it. They have a performance gap problem. I'll skip the skill.

Should I explore the workspace? The user might have code in the workspace. Let me check if there are files. The instruction says "Before modifying code, call explore once" — but I'm not modifying code. Still, it could be useful to look at the workspace to see if there's a project. Let me do a quick glob to see what's in the workspace.

Actually, the user gave a one-line problem statement with no code. The best response is a diagnostic answer: this is overfitting or train/test mismatch. Key causes:

1. Overfitting — model memorized training data.
2. Data leakage — e.g., duplicates between train and test, or preprocessing fit on full dataset.
3. Distribution shift — new photos differ from training photos (different camera, lighting, preprocessing).
4. Train/test split issues — random split on images from same session, or normalization stats computed on test set.
5. Label errors or class imbalance.

Diagnostic steps:
- Evaluate on a held-out validation set that was properly split (no leakage).
- Check accuracy on the training set with augmentation/dropout off vs on.
- Plot learning curves.
- Check per-class accuracy on new photos — maybe one class dominates errors.
- Visually inspect misclassified new photos.
- Check preprocessing consistency (resize, normalization, color channel order RGB/BGR).
- Check whether new photos come from a different source.

Fixes:
- Regularization: dropout, weight decay, augmentation, early stopping, smaller model.
- More data / better augmentation matching the new photo distribution.
- Recalibrate preprocessing.
- Cross-validation.

The tone guidelines: lead with the answer, tight structure, no filler. Match depth to complexity — this is a moderately complex debugging question, so a tight structure with a few bullets is fine.

Should I check the workspace for their code? A quick glob costs little and could ground the answer. Let me do a glob for Python files and maybe notebooks. If nothing, answer generically.

Let me run glob for '**/*.py' and '**/*.ipynb' in parallel.

Then answer. Keep it high-signal: the gap means the model learned training-set-specific patterns. Three usual culprits: overfitting, leakage, distribution shift. Then a short diagnostic checklist ordered by likelihood/effort.

Also note: 40% on new photos — if 10 classes, 40% is way above chance but far below 99%. Ask what the val split accuracy is — that's the key discriminator: if val accuracy is also ~99% but new photos are 40%, it's distribution shift or preprocessing mismatch. If val is also ~40%, it's overfitting or leakage in the split.

That's the crucial diagnostic fork. Lead with that.

Format: short intro line, then the fork, then checklist. Keep it compact. No emojis. No "If you want, I can also..." endings.

Let me check workspace first.That gap means the model learned training-set-specific patterns. The single most useful number you're missing: accuracy on your held-out validation split. It splits the diagnosis in two:

**Val split is also ~40%** → classic overfitting, or leakage that made the split useless.
**Val split is ~99% but new photos are 40%** → distribution shift or preprocessing mismatch between training photos and new photos.

Work through these in order — the first three are the usual culprits for photo classifiers:

1. **Leakage in the split.** Random frame-level splits leak when photos come in bursts or share subjects/backgrounds. Split by session/subject instead. Also check for near-duplicate images across train and val (perceptual hash them), and confirm normalization stats, resizing parameters, and any augmentation were fit on train only.
2. **Preprocessing mismatch at inference.** Compare the exact pipeline on new photos against training: resize/crop interpolation, RGB vs BGR channel order, pixel scale (0–1 vs 0–255), mean/std values. A single mismatch here produces exactly this symptom — near-perfect on data that went through the training pipeline, garbage on anything else.
3. **Distribution shift.** New photos from a different camera, lighting, or background. The model may have memorized background/context instead of the object. Eyeball 20 misclassified new photos and 20 correctly classified training photos side by side — memorization is usually obvious.
4. **If it's genuine overfitting:** stronger augmentation matched to the new photos' conditions, weight decay/dropout, early stopping on val loss, a smaller model, or more data.

Two quick diagnostics that narrow it further: per-class accuracy on the new photos (one collapsed class points at label or preprocessing issues; uniform failure points at shift), and confidence distribution — confidently wrong predictions indicate memorization, uniformly uncertain predictions indicate the inputs look out-of-distribution to the model.

If you share the training script and how you load the new photos, I can pinpoint which of these it is.