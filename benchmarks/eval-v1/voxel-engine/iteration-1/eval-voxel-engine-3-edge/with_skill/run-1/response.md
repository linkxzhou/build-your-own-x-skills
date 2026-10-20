The user wants to build a Minecraft-like voxel engine and only knows JavaScript. This matches the build-your-own-x skill — "build your own Docker/containers, interpreter, OS, emulator, web server, browser, game, neural network..." — a voxel engine is a game/graphics project. The skill description says to read the SKILL.md BEFORE doing anything else when the task matches.

Let me read the skill file first.The file is truncated — I need the full category map to find the right track skill for a voxel engine.The map routes "minecraft-like voxel" to the `voxel-engine` track. Reading that track skill now — it's mandatory before anything else.The tutorials list is short. Let me check the per-tutorial skills and manifest for JS-relevant options.The upstream catalog has only one voxel tutorial (C++). The track skill says: "Rust (wgpu) or JS (WebGL/three.js) are fine alternatives if the learner prefers." So JS is explicitly endorsed by the track skill.

The learner only knows JavaScript. The track skill says JS (WebGL/three.js) is a fine alternative. So the answer: yes, absolutely. I should coach per the skill workflow:

1. Agree on scope: language (JS — given), target, milestone list, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide — the upstream list only has the C++ one; for JS I should note the track skill endorses WebGL/three.js. I could mention well-known JS voxel resources. The skill says "Credit the upstream tutorial you are following, using its exact link." The upstream catalog only has the C++ one for voxel. I can say the upstream catalog's voxel entry is C++, but the track skill explicitly allows JS with WebGL/three.js, and I can coach the same milestones in JS.

Per the coaching rules: ask at most 2 short questions and suggest defaults. The learner said "I only know JavaScript" — language is settled. What remains: environment (browser + three.js vs raw WebGL vs Node + regl?) and scope. I should propose the default: browser + WebGL (raw WebGL teaches more; three.js is faster to results). The milestone table is already defined by the track skill — I should present it adapted to JS.

Also per skill: "Stay in the learner's workspace. Never run install commands yourself." I shouldn't scaffold code yet — agree scope first. The output format per turn: where we are, concept, what to write next, how to check.

I shouldn't dump a full solution. I should answer the question ("Can I do this?") — yes — and set up milestone 1 with a skeleton, plus ask the 1-2 scoping questions with defaults.

Let me also check the workspace to see if there's an existing project. Let me glob quickly.Yes — JavaScript is a fine language for this. The voxel-engine track explicitly lists JS with WebGL/three.js as a supported path alongside the C++ original. The concepts you'll learn (chunk data structures, mesh generation, face culling, raycasting) are language-agnostic; WebGL gives you the same GPU pipeline as OpenGL, just through a browser API. The upstream catalog's reference tutorial is [_Let's Make a Voxel Engine_ (C++)](https://sites.google.com/site/letsmakeavoxelengine/home) — worth skimming for its meshing chapters even though we'll build in JS.

**Where we are:** milestone 0/7 — agreeing on scope.

**The plan** (each milestone ends with a runnable check):

| # | Milestone | Checkpoint |
|---|---|---|
| 1 | Window + triangle | a coloured triangle renders |
| 2 | Camera | you can fly around a cube with mouse look + WASD |
| 3 | Chunk data | unit test: get/set block and 3D indexing are correct |
| 4 | Meshing | a solid 16³ chunk emits exactly 6·16² = 1536 faces |
| 5 | Terrain | 8×8 chunks of noise terrain render above 30 fps |
| 6 | Interaction | clicking breaks the block you're looking at |
| 7 | Stretch | ambient occlusion, chunk streaming — memory stays flat walking 500 blocks |

**Two choices before we start** (defaults in bold):

1. **Raw WebGL or three.js?** Default: **raw WebGL**. three.js would mesh and shade for you, which is exactly the part you're trying to learn. Raw WebGL is more boilerplate but milestone 1 is the only place you'll feel it.
2. **How far?** Default: **milestones 1–6**, treat 7 as a stretch goal. That's a real Minecraft-like: walkable terrain you can dig and build in.

**What to write next (milestone 1):** one folder, three files, no build tools:

```
voxel/
  index.html   <!-- <canvas>, <script type="module" src="main.js"> -->
  main.js      <!-- TODO: get WebGL context, compile 2 shaders, draw 3 vertices -->
  shaders.js   <!-- export vertex + fragment shader source strings -->
```

TODOs in `main.js`:
1. `canvas.getContext('webgl2')` (fall back to `'webgl'`)
2. Compile a vertex shader that passes a hardcoded triangle's positions through, and a fragment shader that outputs a solid colour
3. Upload the triangle to a VBO, issue one `gl.drawArrays(gl.TRIANGLES, 0, 3)` per frame

**How to check it:** run a local server (`npx serve` or `python3 -m http.server`) and open the page — you should see a single coloured triangle on a black background. Open devtools console: zero errors.

Answer the two choices (or say "defaults") and start on the TODOs. When the triangle renders, we log it in `PROGRESS.md` and move to the camera.