The user wants to make a Minecraft-like voxel engine. This matches the build-your-own-x skill — "build your own" category, voxel engine / Minecraft clone. Let me check the skill first.

The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md BEFORE doing anything else, then follow it.

Let me read the skill file.The file is truncated. Let me read the rest to find the right category slug for a voxel engine.The category is `voxel-engine`. Reading the track skill now — it's mandatory before anything else.The tutorials list has one entry: C++ "Let's Make a Voxel Engine". Let me check if there are per-tutorial skills and the manifest.I've loaded the voxel-engine track. Before proposing a default stack, let me check what toolchains already exist in this environment.You're starting a **voxel engine** track — I coach this milestone by milestone, you write the code, each milestone ends with a runnable check. Here's the roadmap we'll follow (7 milestones, each one sitting):

| # | Milestone | What you learn | Checkpoint |
|---|---|---|---|
| 1 | Window + triangle | GL context, shaders, VBOs | a coloured triangle renders |
| 2 | Camera | view/projection matrices, mouse look, WASD | you can fly around a cube |
| 3 | Chunk data | 16×16×16 block array, block ids | unit test: get/set + indexing correct |
| 4 | Meshing | face culling between neighbouring solids | solid chunk emits exactly 6·16² faces |
| 5 | Terrain | noise heightmap, many chunks | 8×8 chunks render at > 30 fps |
| 6 | Interaction | raycast picking, break/place, remeshing | clicking removes the block you look at |
| 7 | Stretch | ambient occlusion, chunk streaming | walking 500 blocks keeps memory flat |

The upstream guide is **"Let's Make a Voxel Engine"** (C++): https://sites.google.com/site/letsmakeavoxelengine/home — from [build-your-own-x](https://github.com/codecrafters-io/build-your-own-x).

**Default stack** (my suggestion): C++20 + OpenGL 3.3 core + GLFW + GLAD, built with CMake. Your machine already has clang++ 21 and cmake 4.2.3. One OS note: you're on macOS, where OpenGL is capped at 4.1 — fine for everything above. You'll need GLFW, which I'd have you install yourself: `brew install glfw`.

Two questions before we start milestone 1:

1. **Stack** — C++/OpenGL as above, or would you rather Rust (wgpu) or JavaScript (WebGL/three.js)?
2. **Scope** — full 7 milestones, or a compressed 4 (merge camera into milestone 1, terrain+interaction into one) if your time is limited?

Answer those and we set up the project skeleton and get your first triangle on screen.