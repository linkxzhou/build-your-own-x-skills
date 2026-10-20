The user has a computer vision problem: homography estimation is unstable, projected rectangle jumps around. They're using ORB features + brute force matching + findHomography on all matches.

The classic issues here:
1. No ratio test (Lowe's ratio test) — brute force matching without filtering gives tons of bad matches
2. No cross-check filtering
3. findHomography on all matches without RANSAC (or with RANSAC but feeding garbage matches)
4. Possibly not using cv2.findHomography's RANSAC flag
5. ORB descriptor matching with NORM_HAMMING vs default L2
6. Not enough good matches / degenerate configurations

The user hasn't shown code. I'm in a workspace — let me check what's in the working directory. The cwd is "build-your-own-x-augmented-reality-2" which suggests this is an AR project — projecting a rectangle (like a marker or virtual plane) onto a scene. So there's likely code in the workspace I should look at.

Per my instructions: "When given an unclear or generic instruction, consider it in the context of software engineering tasks and the current working directory." And "Do not propose changes to code you haven't read."

So I should explore the workspace first to find their matching/homography code. Let me glob for Python files and grep for findHomography / ORB / BFMatcher.

Let me do parallel reads: glob for *.py, grep for findHomography.

Then I can give concrete fixes based on their actual code. The likely fix:
- Use BFMatcher with NORM_HAMMING, crossCheck=True OR knnMatch + Lowe ratio test (0.7-0.75)
- Need >= 4 good matches, ideally 50+
- cv2.findHomography(src, dst, cv2.RANSAC, 5.0) — with RANSAC
- Sort matches by distance, take top N
- Possibly use cv2.descriptorMatcher or FLANN with LSH index

Also the "jumps around wildly" suggests temporal instability — could add temporal smoothing, but the root cause is bad matches feeding the estimator.

Let me explore the workspace first.Empty workspace — no code yet. So the user is describing their approach and wants help. The workspace is "build-your-own-x-augmented-reality-2" — likely a CodeCrafters-style "Build your own Augmented Reality" challenge. The user is probably starting out or their code isn't in this workspace yet.

Let me check what IS in the workspace.Empty workspace, so here's the diagnosis on the pipeline you described. Ranked by likelihood:

1. **Wrong distance norm.** `cv2.BFMatcher()` defaults to L2, which is meaningless for ORB's binary descriptors — matches come out near-random. Use `cv2.NORM_HAMMING`.
2. **Feeding all matches to `findHomography`.** Brute-force ORB matching is full of outliers; with a high outlier ratio RANSAC latches onto a wrong consensus and flickers frame to frame. Filter first (Lowe ratio test), then run RANSAC.
3. **Accepting every frame's result.** Check the inlier mask; if it's too small, keep the last good H instead of letting the rectangle teleport.
4. **Swapped point sets.** `queryIdx` belongs to the first (target) image, `trainIdx` to the frame — passing them backwards gives a homography that maps the wrong direction and the rectangle lands anywhere.

Fixed core:

```python
orb = cv2.ORB_create(nfeatures=2000)
kp_t, des_t = orb.detectAndCompute(target_img, None)   # target/reference
kp_f, des_f = orb.detectAndCompute(frame, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING)
matches = bf.knnMatch(des_t, des_f, k=2)
good = [m for m, n in matches if m.distance < 0.75 * n.distance]

if len(good) >= 15:
    src = np.float32([kp_t[m.queryIdx].pt for m in good]).reshape(-1, 1, 2)
    dst = np.float32([kp_f[m.trainIdx].pt for m in good]).reshape(-1, 1, 2)
    H, mask = cv2.findHomography(src, dst, cv2.RANSAC, 4.0)
    if H is not None and mask.sum() >= 15:
        last_H = H  # accept
# else / on rejection: reuse last_H for this frame
```

Then project the rectangle with `cv2.perspectiveTransform(corners, last_H)`.

Two more things that help once the above is in: raise `nfeatures` and make sure the target image has real texture (ORB dies on flat/low-contrast covers), and if the rectangle still jitters a pixel or two per frame, smooth the four projected corners with an exponential moving average — per-frame homographies are noisy even when correct.