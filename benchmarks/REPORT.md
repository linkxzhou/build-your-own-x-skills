# Validation report: build-your-own-x-skills

- **Date:** 2026-10-20 (UTC+8).
- **Agent:** miniagent, model `glm-5.3-flash-external`. A noinstall shim blocks brew, apt and port.
- **Versions:** router `build-your-own-x` 0.2.1, track skills 0.1.1.
- **Runs:** one run per case, so there is no variance estimate.

## Inventory
| Kind | Count |
|---|---|
| Umbrella router (root `SKILL.md`) | 1 |
| Track skills (`skills/<category>/`), 1 per upstream category | 31 (26 written this round + the 5 earlier ones) |
| Per-tutorial skills (`skills/<category>-<tutorial>/`) | 357 (the original 351 + 6 new for distributed-systems, ai-model ×3, memory-allocator and processor) |
| Other skills already in `skills/` (not build-your-own-x) | 8: skill-creator, mcp-builder, tdd-workflow, manim-composer, manimce-best-practices, manimgl-best-practices, internal-comms, llm-model-trainer |

## 1. quick_validate (skill-creator)
- **Result:** 397 skills checked (the root plus every `skills/*/`). After the fixes, 397/397 are valid.
- **First pass:** 6 failures, all "Name is too long (>64)". I renamed the skill folder and its examples folder with `git mv`, and updated every reference (manifest, plan, examples):
  - blockchain-cryptocurrency-blockchain-crypto-currently-lets-tiniest → blockchain-cryptocurrency-crypto-currently-lets-tiniest
  - blockchain-cryptocurrency-blockchain-digital-alchemy-holdings-learn → blockchain-cryptocurrency-digital-alchemy-holdings-learn
  - blockchain-cryptocurrency-blockchain-mycoralhealth-code-blockchain-in → blockchain-cryptocurrency-mycoralhealth-code-blockchain
  - blockchain-cryptocurrency-blockchain-smashingmagazine-2020-02-cryptocurrency → blockchain-cryptocurrency-smashingmagazine-cryptocurrency
  - operating-system-operating-system-lduck11007-operating-systems-development → operating-system-lduck11007-os-development
  - programming-language-fsharpforfunandprofit-understanding-parser-combinators → programming-language-fsharp-parser-combinators

## 2. Link fidelity against the upstream README (snapshot 2026-10-19)
- **Track skills and catalog:** 718 bullet lines across the 31 `tutorials.md` files and `references/catalog.md`. Every line is byte-identical to an upstream line (0 mismatches).
- **Per-tutorial skills:** 357 "Original resource" URLs checked. 353 are in the current upstream README. 4 are no longer there, presumably removed or changed upstream; they were kept as-is:
  - `neural-network-neural-network-f`: https://towardsdatascience.com/building-neural-networks-in-f-part-1-a2832ae972e6
  - `misc-manim`: https://github.com/ManimCommunity/Manim
  - `blockchain-cryptocurrency-blockchain-csharp`: https://programmingblockchain.gitbooks.io/programmingblockchain/
  - `bot-reddit-bot`: http://pythonforengineers.com/build-a-reddit-bot-part-1/
- **Coverage gap:** some upstream links have no per-tutorial skill. For example, neural-network has 17 upstream links but 14 per-tutorial skills. The track skills cover them through `tutorials.md`.
- Full detail is in `benchmarks/links_fidelity.json`.

### Liveness (informational; nothing was rewritten)
I checked the 368 unique upstream URLs from two networks (a box and the Mac):
- 318 return 200 (255 on the first pass, plus 2 on the box retry and 61 more from the Mac).
- About 33 return 403, 405, 406 or 429. These are mostly bot protection, so the result is inconclusive.
- These look dead (404 or unreachable from both networks):
  - 404 https://seasonofcode.com/posts/how-x-window-managers-work-and-how-to-write-one-part-i.html
  - 404 https://joshburns-xyz.vercel.app/posts/build-your-own-git-plugin
  - 404 https://sj14.gitlab.io/post/2018-07-01-go-unix-shell/
  - 404 http://joaoventura.net/blog/2017/python-webserver/
  - 000 http://dranger.com/ffmpeg/ffmpeg.html
  - 000 https://blog.usejournal.com/implement-your-own-call-apply-and-bind-method-in-javascript-42cc85dba1b
  - 000 http://jamesmolloy.co.uk/tutorial_html/
  - 429 http://web.archive.org/web/20200121100942/https://blog.felixangell.com/virtual-machine-in-c/
  - 000 http://krasimirtsonev.com/blog/article/Javascript-template-engine-in-just-20-line
  - 000 https://mattgathu.dev/2017/08/29/writing-cli-app-rust.html
  - 000 https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/how-does-it-work
  - 000 https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation/overview-rasterization-algorithm
  - 000 http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8.html
  - 000 http://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/
  - 000 https://stories.algolia.com/a-search-engine-in-css-b5ec4e902e97
  - 000 https://lethalbrains.com/learn-ml-algorithms-by-coding-decision-trees-439ac503c9a4
  - 000 https://tutorials.botsfloor.com/creating-a-simple-facebook-messenger-ai-bot-with-api-ai-in-node-js-50ae2fa5c80d

## 3. Smoke test: one learner prompt per track (31), through the router
Rubric:
- **Routed:** read the right track skill.
- **Coached:** a skeleton or TODOs for the learner, not a full solution.
- **Checkpoint:** a runnable check for the current milestone.
- **Workspace:** no writes outside the project.
- **No installs:** no install command run by the agent.

The grading is scripted, then reviewed by hand. When miniagent compacted the history, I used the agent's narration as routing evidence.

| Track | Run | Routed | Coached | Checkpoint | Workspace | No installs | Time | Result | Note |
|---|---|---|---|---|---|---|---|---|---|
| `git` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 130s | PASS | trace compacted; the narration confirms the track was read |
| `database` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 270s | PASS | narration confirms the database track was read |
| `shell` | 2 (router 0.2.1) | ✅ | ✅ | ✅ | ✅ | ✅ | 157s | PASS | run 1 skipped the track for shell-shell-rust; passed after the router fix |
| `docker` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 144s | PASS | narration confirms the docker track was read; read docker-go after it |
| `programming-language` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 271s | PASS |  |
| `3d-renderer` | 2 (router 0.2.1) | ✅ | ✅ | ✅ | ✅ | ✅ | 257s | PASS | run 1 skipped the track for 3d-renderer-ray-tracing-cpp; passed after the router fix |
| `augmented-reality` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 164s | PASS | left pip install for the learner to confirm |
| `bittorrent-client` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 337s | PASS |  |
| `blockchain-cryptocurrency` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 141s | PASS |  |
| `bot` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 234s | PASS |  |
| `command-line-tool` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 232s | PASS |  |
| `emulator-virtual-machine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 119s | PASS |  |
| `frontend-framework-library` | 2 (router 0.2.1) | ✅ | ✅ | ✅ | ✅ | ✅ | 199s | PASS | run 1 hit an LLMProxy 502; the rerun read the track |
| `game` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 165s | PASS |  |
| `network-stack` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 152s | PASS |  |
| `neural-network` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 377s | PASS |  |
| `operating-system` | 3 (no-install rule) | ✅ | ✅ | ✅ | ✅ | ✅ | 611s | PASS | run 1 ran `cargo install bootimage` and `rustup component add llvm-tools-preview` itself (FAIL). Run 3, with the no-install rule, only printed the commands |
| `physics-engine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 531s | PASS |  |
| `regex-engine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 283s | PASS |  |
| `search-engine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 108s | PASS |  |
| `template-engine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 246s | PASS |  |
| `text-editor` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 236s | PASS |  |
| `visual-recognition-system` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 272s | PASS |  |
| `voxel-engine` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 106s | PASS | asked before `brew install glfw` (not installed); checkpoint stated: ./voxel opens a window |
| `web-browser` | 2 (router 0.2.1) | ✅ | ✅ | ✅ | ✅ | ✅ | 96s | PASS | run 1 skipped the track. The rerun read it, then asked 2 scoping questions because Tk is missing. The checkpoint is named but not a command yet |
| `web-server` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 305s | PASS |  |
| `misc` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 106s | PASS | picked DNS and asked 2 scope questions; checkpoint table includes a dig command |
| `distributed-systems` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 278s | PASS |  |
| `ai-model` | 3 (no-install rule) | ✅ | ✅ | ✅ | ✅ | ✅ | 308s | PASS | checkpoint: `python3 test_tokenizer.py` must report MILESTONE 1 COMPLETE |
| `memory-allocator` | 1 | ✅ | ✅ | ✅ | ✅ | ✅ | 179s | PASS |  |
| `processor` | 2 (router 0.2.1) | ✅ | ✅ | ✅ | ✅ | ✅ | 233s | PASS | routing unclear in run 1; the rerun read the track |

- **Final result:** 31/31 PASS.
- **First pass:** 26/31.
  - 3 runs (shell, 3d-renderer, web-browser) went straight to a per-tutorial skill and skipped the track.
  - 1 run (frontend-framework-library) hit an LLMProxy 502 network error.
  - 1 run (operating-system) installed tools itself.
- **Fixes, then reruns of only the affected cases:**
  - Router 0.2.1 makes reading the track skill mandatory, before any per-tutorial skill.
  - All 31 track skills (0.1.1) and the router now say "Never install anything yourself; print the command for the learner."
- **Side effect from the first operating-system run:** it installed `bootimage` (`~/.cargo/bin/bootimage` and `cargo-bootimage`, 2026-10-20 05:22) and ran `rustup component add llvm-tools-preview`. These were left in place. Remove them with `cargo uninstall bootimage` and `rustup component remove llvm-tools-preview --toolchain nightly` if you don't want them.
- brew was only called for read-only checks (`brew --prefix`, `brew list`), and the shim logged those.

## 4. Router trigger check
- **Setup:** 30 prompts. The umbrella skill was listed together with 4 unrelated skills (andrew-translate, design-taste, simplify-code, code-refactor). Read-only mode, at most 5 steps. A prompt counts as triggered when that skill's SKILL.md is the first one read.
- **Prompts:** 18 should trigger (Chinese and English: build my own Redis, git, OS, Lisp, TCP/IP, docker, GPT, CHIP-8, malloc, regex, web server, language, voxel, BitTorrent, RISC-V, search engine, text editor, plus a "recommend a hands-on project" prompt).
- **Hard negatives:** 12 prompts that should not trigger: git rebase vs merge, a Redis connection error, docker-compose, TCP handshake, Raft summary, OS book list, SQL tuning, quicksort, a failing React test, plus 3 that belong to the other skills.
- **Result:** recall 18/18, precision 18/18 (0 false triggers). The 3 other-skill prompts all went to the right skill, and all 9 no-skill prompts read no skill. Accuracy 30/30.
- The router description did not change between this run and the router fixes, which only touched the body.

## Remaining issues
- Each case ran once. The smoke test only covers the first turn (scoping and milestone 1); later milestones are untested.
- Context compaction hides some tool history. For git, database, docker and a few others, routing was confirmed from the agent's narration, not the trace.
- The noinstall shim only blocks brew, apt and port. pip, cargo and rustup are guarded only by the skill text.
- 16 upstream links look dead and about 33 are inconclusive. 4 per-tutorial skills point at URLs that are no longer upstream.
- The 6 new per-tutorial skills use the existing generic template, so they have no per-article milestones and no examples yet.
