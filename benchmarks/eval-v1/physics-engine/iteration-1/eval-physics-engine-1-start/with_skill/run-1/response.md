The user wants to build a 2D physics engine in JavaScript. This matches the build-your-own-x skill — specifically "build your own physics engine" category. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read the rest to find the physics engine category slug.The category maps to `physics-engine`. Reading the track skill now — it's mandatory before anything else.The track skill is loaded. The learner named JavaScript + 2D, so language is settled. Let me check the workspace state before scaffolding.Node v25.8.0 is available and the workspace is empty — no installs needed, `node:test` runs the checkpoints natively. Let me check AGENTS.md for workspace rules, then record the exploration and plan.The runner choked on the directory argument. Let me check the exact invocation.Two fixes: the test file is missing the `Vec2` import, and the `tests/` directory form of `--test` fails on this Node — auto-discovery (`node --test`) works.Checkpoint is wired: 3 red tests are exactly the parts you'll implement, 2 green ones pass trivially.Project is scaffolded in `physics-engine/` — no installs needed, Node 25 runs the tests natively. Following [How Physics Engines Work](http://buildnewgames.com/gamephysics/) as the primary reference (credited in the README).

**Where we are:** milestone 1/7 — the integrator.

**The concept.** Two ideas carry this milestone:

1. **Semi-implicit Euler** — update velocity first, then position with the *new* velocity. That one ordering choice is what makes simple engines stable where naive Euler ("position first") explodes on springs and stiff contacts. Per step: `a = F/m + g`, then `v += a·dt`, then `x += v·dt`.
2. **Fixed timestep with an accumulator** — real frame times jitter (16.6, 14.2, 33.1 ms…), and feeding those straight into physics makes the simulation non-deterministic and unstable. Instead, bank the frame time and run as many fixed `dt = 1/120 s` steps as the bank covers, carrying the remainder to the next frame. Every engine you've heard of (Box2D, Matter, Rapier) does this.

**What to write next** — five TODOs, all in `src/`:

- `src/body.js` — TODO 1: `invMass` (remember `1/Infinity = 0`, which is exactly why static bodies work for free); TODO 2: accumulate force; TODO 3: the three-line integrator in the order above.
- `src/world.js` — TODO 4: the accumulator loop in `step()` (clamp `frameTime` first); TODO 5: `fixedStep()` applies gravity as a force, then integrates each body.

**How to check it:**

```
cd physics-engine && node --test
```

Right now it's 2 pass / 3 fail. Done means 5 pass — the tests pin the physics (free fall 1 s → 0.5·g within 1%), the step count (exactly 120 per simulated second), remainder carry-over, static bodies, and spike clamping.

Stuck? Ask and you get one hint at a time — first one is free: the accumulator test that expects 0 steps then 1 is the one that catches people.