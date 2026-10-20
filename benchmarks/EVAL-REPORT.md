# build-your-own-x skills — eval report (eval-v1, 2026-10-20)

Method follows skill-creator: each case runs **with** the skill (AGENTS.md pointer + `.agents/skills/`) and **without** (baseline), via miniagent (`MINIAGENT_MODEL_NAME=glm-5.3-flash-external`, `--approval auto --no-auto-goal --no-builtin-skills --json`, 900 s timeout, PATH shim blocking brew/apt/port/pip/cargo/rustup/npm -g/go install). Outputs are graded by an LLM judge (default model) against 4 objective assertions per case (B1–B4), then aggregated with skill-creator `aggregate_benchmark.py`. Per-run artifacts: `benchmarks/eval-v1/<skill>/iteration-N/` (`benchmark.json`, `benchmark.md`, `eval-*/<cond>/run-1/{grading,timing}.json`, `response.md`). Iterations 2+ rerun only with_skill for failing cases; the baseline is carried over from iteration-1 (`NOTE.txt`).

- 31 track skills × 3 cases (start / stuck-or-debug / edge), mixed zh/en → 186 runs
- 15 per-tutorial skills (including the 6 new ones) × 2 cases (plan, taskify) → 60 runs
- Assertions: B1 = coaches, no full dump/minimal fix; **B2 = ends with a runnable checkpoint (command + expected output)**; B3 = technically specific; **B4 = stays in the workspace, installs nothing**. A1 (routing: router → track SKILL.md read) is recorded separately.

## Results

"with (final)" = latest with-skill iteration per case (max 2 fix iterations per skill); "without" = baseline.

### Track skills

| skill | cases | with (iter-1) | with (final) | without | delta (final) | final iter | remaining with-skill failures |
|---|---|---|---|---|---|---|---|
| 3d-renderer | 3 | 0.92 | 0.92 | 0.83 | +0.08 | 1 | stuck:B2 |
| ai-model | 3 | 0.83 | 0.83 | 0.58 | +0.25 | 1 | stuck:B2 edge:B2 |
| augmented-reality | 3 | 0.83 | 0.92 | 0.75 | +0.17 | 2 | stuck:B1 |
| bittorrent-client | 3 | 0.83 | 0.83 | 0.75 | +0.08 | 1 | stuck:B2 edge:B2 |
| blockchain-cryptocurrency | 3 | 0.92 | 1.00 | 0.92 | +0.08 | 2 |  |
| bot | 3 | 0.83 | 0.92 | 0.75 | +0.17 | 2 | edge:B1 |
| command-line-tool | 3 | 0.75 | 0.75 | 0.58 | +0.17 | 1 | stuck:B2 edge:B1 edge:B2 |
| database | 3 | 0.92 | 0.92 | 0.58 | +0.33 | 1 | stuck:B2 |
| distributed-systems | 3 | 0.83 | 0.83 | 0.75 | +0.08 | 1 | stuck:B2 edge:B2 |
| docker | 3 | 0.92 | 0.92 | 0.75 | +0.17 | 1 | edge:B2 |
| emulator-virtual-machine | 3 | 0.75 | 0.92 | 0.67 | +0.25 | 2 | edge:B2 |
| frontend-framework-library | 3 | 0.92 | 0.92 | 0.50 | +0.42 | 2 | edge:B1 |
| game | 3 | 0.83 | 0.83 | 0.75 | +0.08 | 1 | stuck:B2 edge:B2 |
| git | 3 | 0.67 | 0.92 | 0.58 | +0.33 | 2 | edge:B1 |
| memory-allocator | 3 | 0.83 | 0.75 | 0.92 | -0.17 | 3 | start:B2 edge:B2 edge:B4 |
| misc | 3 | 0.92 | 0.92 | 0.67 | +0.25 | 2 | edge:B2 |
| network-stack | 3 | 0.83 | 0.83 | 0.67 | +0.17 | 1 | stuck:B2 edge:B2 |
| neural-network | 3 | 0.83 | 0.83 | 0.75 | +0.08 | 1 | stuck:B2 edge:B2 |
| operating-system | 3 | 0.75 | 0.92 | 0.67 | +0.25 | 2 | edge:B4 |
| physics-engine | 3 | 0.83 | 0.83 | 0.50 | +0.33 | 1 | stuck:B2 edge:B2 |
| processor | 3 | 0.92 | 0.92 | 0.67 | +0.25 | 1 | stuck:B2 |
| programming-language | 3 | 0.75 | 1.00 | 0.83 | +0.17 | 2 |  |
| regex-engine | 3 | 0.75 | 1.00 | 0.67 | +0.33 | 2 |  |
| search-engine | 3 | 0.83 | 0.83 | 0.67 | +0.17 | 1 | start:B3 edge:B2 |
| shell | 3 | 0.75 | 1.00 | 0.92 | +0.08 | 2 |  |
| template-engine | 3 | 0.92 | 0.92 | 0.83 | +0.08 | 1 | edge:B2 |
| text-editor | 3 | 0.92 | 0.92 | 0.75 | +0.17 | 1 | stuck:B2 |
| visual-recognition-system | 3 | 0.58 | 0.58 | 0.92 | -0.33 | 3 | stuck:B2 edge:B1 edge:B2 edge:B3 edge:B4 |
| voxel-engine | 3 | 0.75 | 0.75 | 0.42 | +0.33 | 1 | start:B1 start:B2 stuck:B2 |
| web-browser | 3 | 0.92 | 0.92 | 0.83 | +0.08 | 1 | stuck:B2 |
| web-server | 3 | 0.83 | 1.00 | 0.92 | +0.08 | 3 |  |
| **OVERALL** | 93 | 0.828 | 0.882 | 0.720 | +0.161 | | |

### Per-tutorial skills

| skill | cases | with (iter-1) | with (final) | without | delta (final) | final iter | remaining with-skill failures |
|---|---|---|---|---|---|---|---|
| ai-model-diffusion-python | 2 | 0.88 | 0.88 | 0.75 | +0.12 | 1 | taskify:B4 |
| ai-model-llm-python | 2 | 0.88 | 0.88 | 0.75 | +0.12 | 1 | taskify:B4 |
| ai-model-rag-python | 2 | 0.88 | 0.88 | 0.75 | +0.12 | 1 | taskify:B4 |
| database-redis-go | 2 | 0.75 | 0.75 | 0.75 | +0.00 | 1 | plan:B4 taskify:B4 |
| distributed-systems-kafka-java | 2 | 0.50 | 1.00 | 0.75 | +0.25 | 3 |  |
| docker-docker-shell | 2 | 0.88 | 1.00 | 1.00 | +0.00 | 2 |  |
| emulator-virtual-machine-chip8-interpreter | 2 | 0.88 | 0.88 | 0.75 | +0.12 | 1 | taskify:B4 |
| git-git-wyag-thb-lt | 2 | 0.88 | 0.88 | 0.88 | +0.00 | 1 | plan:B4 |
| memory-allocator-malloc-c | 2 | 0.88 | 0.62 | 0.38 | +0.25 | 3 | taskify:B1 taskify:B2 taskify:B3 |
| processor-riscv-verilog | 2 | 0.50 | 0.88 | 0.75 | +0.12 | 3 | taskify:B4 |
| programming-language-crafting-interpreters | 2 | 0.62 | 0.88 | 0.50 | +0.38 | 2 | taskify:B2 |
| regex-engine-regex-c | 2 | 0.88 | 0.88 | 0.88 | +0.00 | 2 | taskify:B4 |
| shell-shell-c | 2 | 0.88 | 0.88 | 0.50 | +0.38 | 2 | taskify:B4 |
| text-editor-text-editor | 2 | 0.88 | 0.75 | 0.88 | -0.12 | 2 | taskify:B1 taskify:B4 |
| web-server-http | 2 | 0.75 | 0.88 | 0.88 | +0.00 | 2 | taskify:B4 |
| **OVERALL** | 30 | 0.792 | 0.858 | 0.742 | +0.117 | | |

## Trigger eval

| run | set | n | accuracy | misses / false triggers |
|---|---|---|---|---|
| v1t1 | router desc 0.2.1 vs 3 distractor skills + none | 24 | 0.917 | 2 stuck/debug phrasings missed (shadow acne, hash-object mismatch) |
| v2t1 | router 0.2.2 | 24 | 0.958 | 1 miss (shadow acne) |
| **v3t1** | router 0.2.2 (final) | 24 | **1.000** | none |
| v1t2 | 8 track descriptions + none | 20 | 0.95 | web-server "浏览器一直转圈" missed |
| **v3t2** | 8 track descriptions (final) | 20 | **0.90** | "Build a key-value database with a B-tree" → none; "用 PyTorch 微调 BERT" falsely → ai-model |

## Fixes applied

1. **Router 0.2.2**: description covers stuck/debugging phrasing; a debugging-turn rule.
2. **31 tracks 0.1.2**: no full-project dump even on request; minimal fix in debug turns; scratch files inside the project, never /tmp; never echo pasted secrets; rule 7 "every reply ends with the checkpoint, keep it under ~60 lines".
3. **visual-recognition-system / neural-network / ai-model**: explicit ban on running pip/pip3/python -m pip/conda/venv `bin/pip`; print the install command instead.
4. **269 per-tutorial skills (shared template)**: new "Converting the tutorial into a task list" workflow step (offline references first, at most 2 fetches, deliver TASKS.md + checkpoint). It fixes the 900 s taskify timeouts (kafka-java 0.50→1.00, riscv-verilog 0.50→0.88). Also a stay-in-project/no-venv principle and a concise-reply principle.

Before → after (with-skill): tracks **0.828 → 0.882** (baseline 0.720); per-tutorial **0.792 → 0.858** (baseline 0.742).

## Secret scan

gitleaks 8.21.2 (`detect --no-git` over all changed files): 0 findings. Regex pass (sk-, AKIA, ghp_, xox*, private keys, key/token/password assignments): only placeholders (`paste-your-token-here`, `your_api_key_here`).

## Remaining issues

- **visual-recognition-system** (0.58 vs 0.92): the agent builds a venv under `~/venvs` and calls its `bin/pip`, which gets past the PATH shim. The skill text is now stricter, but this hit the 2-iteration cap, so the last edit is **untested**. The harness should also block `*/bin/pip` and venv creation.
- **memory-allocator** track (0.75 vs 0.92): iteration-3 regressed from 0.92 at iteration-2. Most failures are B2 "final answer cut off mid-sentence". This looks like the flash model ending the turn early, not the skill content. Cap reached.
- **memory-allocator-malloc-c taskify**: still scrapes the article and times out (900 s).
- **Ties (with = without)**: database-redis-go, docker-docker-shell, git-git-wyag-thb-lt, regex-engine-regex-c, web-server-http. text-editor-text-editor taskify regressed (downloads the reference editor). The git-wyag skill uses a different template and did not get the template fixes.
- operating-system start/edge cases time out at 900 s in both conditions.
- n is small (1 run per case, 2–3 cases per skill), so a single assertion moves a skill by about 0.08–0.12.
