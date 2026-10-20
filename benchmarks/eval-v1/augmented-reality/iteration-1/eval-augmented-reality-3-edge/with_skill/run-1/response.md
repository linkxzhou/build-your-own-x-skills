The user wants to build their own AR marker demo (overlay a cube on a printed marker) but doesn't have a webcam. This matches the build-your-own-x skill — specifically AR is a category in build-your-own-x ("Augmented Reality"). I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated — let me read the rest, especially the category map to find the AR track.The topic maps to the `augmented-reality` track. Reading that track skill now, as required.The file was truncated again. Let me read the rest of the file (lines 43+).The track skill explicitly addresses the webcam question ("the OpenCV track needs a webcam or test images"). Let me check the curated tutorial list to pick one that fits a no-webcam setup.There's a Python + OpenCV tutorial that fits. Let me check for a per-tutorial skill for it.The Python + OpenCV tutorial has a per-tutorial skill. Reading it for article-specific details relevant to the no-webcam situation.Let me also check the tutorial-map.md reference to see how the tutorial maps to milestones, and whether it mentions the no-webcam / still-image path.Yes — a webcam is optional for this project. The marker-AR pipeline (feature detection → matching → homography → pose → cube projection) is camera-agnostic. The webcam shows up in exactly one line, `cv2.VideoCapture(0)`, and everything after it works identically on any frame source.

**Where we are:** scoping for the Python + OpenCV track, milestone 1 of 6. Upstream tutorial we'll follow: [Augmented Reality with Python and OpenCV](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/).

**Three ways to get frames with zero webcam:**

1. **Phone as capture device** (recommended). Photograph the printed marker once (that's your reference image), then record a 10–15s clip moving around it. `cv2.VideoCapture('clip.mp4')` reads it exactly like a live feed. Apps like DroidCam/Iriun can even stream the phone as a live webcam later if you want the real-time loop.
2. **Still images only.** One marker photo + a few scene photos containing it. Covers milestones 1–5 fully; milestone 6 becomes "overlay consistent across all scene photos."
3. **Fully synthetic.** Composite the marker onto background images with a slight perspective warp to generate test scenes. Deterministic, good for debugging the math.

**Milestones** (each ends with a runnable check):

| # | Milestone | Check |
|---|---|---|
| 1 | Image input: load marker + scene/video | script displays both |
| 2 | Feature detection (ORB) | >100 keypoints drawn on the marker |
| 3 | Matching (brute-force + ratio test) | match visualization shows mostly correct lines |
| 4 | Homography + pose (RANSAC, camera intrinsics) | marker outline drawn as a correct quadrilateral on the scene |
| 5 | Render the cube with the estimated pose | cube sits on the marker and looks 3D |
| 6 | Stability over a saved clip | overlay stays attached for 10s of video |

**Setup** (you run these, I never install): `pip install opencv-python numpy`, and print the marker — the tutorial's pattern or any high-contrast asymmetric pattern works.

Two things to confirm before we start milestone 1:

1. Do you have a phone or any camera to capture the marker and a short clip? Default: yes → path 1, with path 3 as backup for tests.
2. Python OK? Default: yes.