The user says: "My classifier gets 99% on training data but 40% on new photos." This is a classic overfitting / data leakage / distribution shift problem. This is a conversational question, not a code task in the workspace. Let me check if there's a workspace context — maybe there are files. The user hasn't pointed to any files. This seems like a general ML debugging question.

I should respond directly with high-signal diagnosis. No need for tools really — there's no code to look at. But maybe I should check if there's a project in the workspace? The instructions say to use explore before modifying code, but there's no code modification requested. This is a question. I could quickly glob to see if there's relevant code in the workspace, but the user's message reads like a general question. Let me do a quick check of the workspace to see if there's anything relevant — actually, a quick glob is cheap and could reveal their project. But if the workspace is empty or unrelated, I just answer generally.

Let me think about what the answer should contain:

99% train vs 40% test = massive generalization gap. Causes ranked by likelihood:

1. **Data leakage / duplicated near-duplicate images across train/test splits** — e.g., random split of frames from the same video, or same scene photographed multiple times, or augmented copies of test images in training. Actually leakage usually inflates test accuracy, not train. Wait — leakage inflates test. Here test is low, so leakage isn't the cause of the gap; the gap is overfitting. But near-duplicates across splits would make test look better, so if test is still 40% despite possible duplicates, the real situation is worse.

2. **Overfitting**: model memorized training set. 99% train is suspicious — likely model capacity too high, too few samples, no regularization/augmentation.

3. **Distribution shift between training photos and "new photos"**: different camera, lighting, resolution, preprocessing mismatch (e.g., normalization constants, resize/crop, channel order RGB/BGR, train/eval mode, preprocessing pipeline differences between training and inference).

4. **Evaluation bug**: model in train() mode at inference (BatchNorm/Dropout active), wrong preprocessing at inference, label mapping mismatch (class index ordering differs), comparing against different label set.

5. **Label noise or trivially leaky features in training data** (e.g., watermark, timestamp, filename artifacts).

Diagnostic steps:
- Check a held-out validation set drawn from the training distribution with the same preprocessing: if val ≈ 99%, the model is fine on-distribution and the problem is shift/preprocessing at inference. If val ≈ 40%, it's overfitting.
- Verify preprocessing identical: same resize, normalization, channel order, dtype scale [0,1] vs [0,255].
- Check model.eval() (if PyTorch) / dropout off.
- Sanity check: run inference on some training images through the *inference* pipeline. If accuracy drops there, it's a preprocessing/eval bug, not generalization.
- Look at confusion matrix on new photos — is it predicting one class (collapse) or scattered?
- Check class balance in new photos vs training.

Fixes if overfitting: more data, augmentation, regularization (weight decay, dropout), smaller model, early stopping, transfer learning (pretrained backbone + freeze), cross-validation with group-aware splits (GroupShuffleSplit by scene/session) to measure true generalization.

The most decisive first test: evaluate on a validation split from training data using the exact inference pipeline. That splits the problem into "overfitting" vs "pipeline/shift".

Format: This is a conversational debugging question. Keep it tight. Lead with the answer: that gap means the model memorized the training set or the inference pipeline differs. Give the decisive test first, then likely causes, then fixes. Use a short structure. Per tone guidance: a few lines of prose, bullets only where genuinely parallel. This genuinely needs a small structure: one decisive test + causes + fixes. Keep to maybe 12-20 lines.

Should I check the workspace for their code? The user gave no file references. A quick glob costs little and if there's a training script I could be concrete. Let me do one glob for python files. Actually the instruction says make independent calls in parallel. I'll do a quick glob to see if there's a project. If empty, answer generally.

Let me do glob '**/*.py' and maybe '**/*.ipynb'. If nothing, answer generally.

I'll keep the answer focused:

1. Decisive test: score a held-out slice of the training distribution through the exact inference path.
   - If it's ~99%: generalization is fine; the new photos differ (shift or preprocessing mismatch).
   - If it's ~40%: overfitting (or leakage in the 99%).
2. Common concrete culprits:
   - Preprocessing mismatch at inference: resize/interpolation, normalization stats, RGB vs BGR, [0,1] vs [0,255] scaling.
   - model.eval() forgotten — BatchNorm/Dropout still active.
   - Label index mapping differs between training and deployment.
   - Split not group-aware: same scene/session in train and val inflates val; real new scenes are harder.
   - 99% train accuracy itself signals memorization: too little data / too much capacity / no augmentation.
3. Fixes: pretrained backbone + augmentation + weight decay + early stopping; collect data matching deployment conditions; group-aware splits.

Also mention: check confusion matrix on new photos — constant prediction indicates preprocessing collapse.

Keep it high-signal. No filler. No "In summary". No conditional next-step menus. I can end with the recommendation.

Length: moderate. Let me write it.That gap means one of two things: the model memorized the training set, or the inference path differs from the training path. One test separates them.

**Decisive test:** take a held-out slice of your *training* data (images the model never saw, same collection, same camera conditions) and score it through the exact inference pipeline you use on new photos.

- If it comes back ~99% → generalization is fine; the new photos differ in distribution or preprocessing.
- If it comes back ~40% → the model overfit, and the 99% train accuracy is memorization.

**If it's the pipeline (val high, new photos low), check in this order:**

1. Preprocessing mismatch: resize/interpolation, normalization stats, `[0,1]` vs `[0,255]` scaling, RGB vs BGR channel order. Run a few training images through the inference preprocessing and diff against the training tensors.
2. Eval mode: in PyTorch, `model.eval()` forgotten leaves BatchNorm using batch stats and Dropout active — this alone can crater accuracy.
3. Label mapping: class index order at inference differing from training (e.g., `ImageFolder` sorted alphabetically vs your hardcoded list).
4. Confusion matrix on the new photos: a single dominant predicted class means the inputs look like noise to the model — almost always preprocessing.

**If it's overfitting (val also ~40%):**

- The 99% train accuracy is the tell: too much capacity for too little data. Switch to a pretrained backbone (ResNet/EffNet/ViT) with a small head, freeze early layers.
- Add augmentation matched to real variation (brightness, crop, flip, color jitter), weight decay, early stopping on val accuracy.
- Check your split for leakage: if photos from the same scene/session/subject land in both train and val, your val score is inflated and true generalization is worse than it looks. Split by group (`GroupShuffleSplit` on session/scene ID), not randomly.
- Collect or augment data that matches deployment conditions — lighting, camera, background — since that's where the model fails.

Run the decisive test first; it tells you which branch you're on in ten minutes.