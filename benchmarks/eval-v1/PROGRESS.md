# eval-v1 progress (auto-updated 2026-10-20 13:02:27 UTC+8)

Work dir: ~/skev/byox-eval/v1 (runs/, runspt/, trig/). Resume: drive.sh / drivept.sh skip runs with timing.json; jl.py grades runs missing grading.json.
- track runs:      186/186, graded      237
- per-tutorial runs:       60/60, graded       78
- trigger: trig/v1t1/summary.json trig/v1t2/summary.json trig/v2t1/summary.json trig/v3t1/summary.json trig/v3t2/summary.json 
- rerun of 8 runs (5 timeouts at 900s, 3 LLMProxy errors) started 10:42:41; first attempts saved in attempt1/
- 10:55 fixes applied in repo (not yet in staging): router 0.2.2 (description covers stuck/debugging; debugging-turn rule), 31 tracks 0.1.2 (no full dump even on request, minimal fix, scratch inside project not /tmp, never echo pasted secrets, every reply ends with a checkpoint). Next: after iteration-1 finishes, stage skill2 and run iteration-2 for failing skills.
- trigger v1t1 (router, old desc): 22/24, misses = 2 stuck/debug phrasings; v1t2 (8 tracks): 19/20. v2t1 = router 0.2.2 rerun.
- 10:59 iteration-2 (with_skill only, staged skill2 = fixed repo) started for: blockchain-cryptocurrency bot emulator-virtual-machine frontend-framework-library git memory-allocator misc operating-system programming-language regex-engine shell visual-recognition-system web-server augmented-reality
- 11:45 fix: per-tutorial template (269 skills) gets '### 5. Converting the tutorial into a task list' (offline refs first, ≤2 fetches, no /tmp, deliver TASKS.md + checkpoint) after 7 taskify with_skill timeouts at 900s. iteration-2 (skill3) for taskify of kafka/riscv/malloc/crafting-interpreters/regex-c started.
- 11:52 7 it2 runs failed (4×LLMProxy 429 rate limit, 3×timeout) → moved to attempt1/it2, rerunning with skill3. VRS ran pip itself → explicit no-pip rule added to visual-recognition-system/neural-network/ai-model tracks; VRS iteration-3 running.
- pt iteration-2 also queued (drivept3, after PT2DONE): regex-c plan, shell-c plan, text-editor taskify (with_skill timeouts).
- 12:30 round-2 fixes (skill4): per-tutorial template (269) adds stay-in-project/no-venv-pip + concise-reply-with-checkpoint principles; 31 tracks add rule 7 'every reply ends with the checkpoint, ≤~60 lines'. Running: tracks memory-allocator, web-server → iteration-3; pt kafka/riscv/malloc-c → iteration-3, docker-docker-shell/web-server-http → iteration-2. VRS hit 2-iteration cap (it2/it3 0.58) – latest VRS edit untested. programming-language/shell/blockchain fixed at it2 (1.00).
- 12:33 trigger v3 (router 0.2.2 + current track descriptions) running → trig/v3t1, v3t2
- 13:20 round-2 done; final tables via final.py; trigger v3t1 24/24, v3t2 18/20. Writing EVAL-REPORT.md + commit.

## Track scores (B1–B4 pass rate)
```
skill                                      n  with  w/o  delta  A1   with-fails
3d-renderer                                3/3 0.92 0.83 +0.08 2/3 stuck:B2
ai-model                                   3/3 0.83 0.58 +0.25 2/3 stuck:B2 edge:B2
augmented-reality                          3/3 0.83 0.75 +0.08 2/3 edge:B2 stuck:B1
bittorrent-client                          3/3 0.83 0.75 +0.08 2/3 stuck:B2 edge:B2
blockchain-cryptocurrency                  3/3 0.92 0.92 +0.00 2/3 stuck:B1
bot                                        3/3 0.83 0.75 +0.08 1/3 edge:B1 edge:B2
command-line-tool                          3/3 0.75 0.58 +0.17 1/3 edge:B1 edge:B2 stuck:B2
database                                   3/3 0.92 0.58 +0.33 2/3 stuck:B2
distributed-systems                        3/3 0.83 0.75 +0.08 2/3 edge:B2 stuck:B2
docker                                     3/3 0.92 0.75 +0.17 1/3 edge:B2
emulator-virtual-machine                   3/3 0.75 0.67 +0.08 2/3 stuck:B2 stuck:B4 edge:B2
frontend-framework-library                 3/3 0.92 0.50 +0.42 2/3 edge:B4
game                                       3/3 0.83 0.75 +0.08 2/3 stuck:B2 edge:B2
git                                        3/3 0.67 0.58 +0.08 3/3 edge:B1 edge:B2 edge:B4 stuck:B4
memory-allocator                           3/3 0.83 0.92 -0.08 3/3 stuck:B4 edge:B4
misc                                       3/3 0.92 0.67 +0.25 2/3 start:B1
network-stack                              3/3 0.83 0.67 +0.17 2/3 stuck:B2 edge:B2
neural-network                             3/3 0.83 0.75 +0.08 2/3 edge:B2 stuck:B2
operating-system                           3/3 0.75 0.67 +0.08 2/3 edge:B1 edge:B2 edge:B3
physics-engine                             3/3 0.83 0.50 +0.33 2/3 edge:B2 stuck:B2
processor                                  3/3 0.92 0.67 +0.25 2/3 stuck:B2
programming-language                       3/3 0.75 0.83 -0.08 2/3 stuck:B1 edge:B2 edge:B4
regex-engine                               3/3 0.75 0.67 +0.08 2/3 stuck:B2 edge:B2 edge:B3
search-engine                              3/3 0.83 0.67 +0.17 1/3 edge:B2 start:B3
shell                                      3/3 0.75 0.92 -0.17 2/3 stuck:B1 stuck:B2 edge:B2
template-engine                            3/3 0.92 0.83 +0.08 2/3 edge:B2
text-editor                                3/3 0.92 0.75 +0.17 2/3 stuck:B2
visual-recognition-system                  3/3 0.58 0.92 -0.33 1/3 stuck:B2 edge:B1 edge:B2 edge:B3 edge:B4
voxel-engine                               3/3 0.75 0.42 +0.33 2/3 start:B1 start:B2 stuck:B2
web-browser                                3/3 0.92 0.83 +0.08 2/3 stuck:B2
web-server                                 3/3 0.83 0.92 -0.08 0/3 edge:B2 stuck:B2
OVERALL 93 93 0.828 0.72
```
## Per-tutorial scores
```
skill                                      n  with  w/o  delta  A1   with-fails
ai-model-diffusion-python                  2/2 0.88 0.75 +0.12 2/2 taskify:B4
ai-model-llm-python                        2/2 0.88 0.75 +0.12 2/2 taskify:B4
ai-model-rag-python                        2/2 0.88 0.75 +0.12 2/2 taskify:B4
database-redis-go                          2/2 0.75 0.75 +0.00 2/2 plan:B4 taskify:B4
distributed-systems-kafka-java             2/2 0.50 0.75 -0.25 2/2 taskify:B1 taskify:B2 taskify:B3 taskify:B4
docker-docker-shell                        2/2 0.88 1.00 -0.12 2/2 taskify:B4
emulator-virtual-machine-chip8-interpreter 2/2 0.88 0.75 +0.12 2/2 taskify:B4
git-git-wyag-thb-lt                        2/2 0.88 0.88 +0.00 2/2 plan:B4
memory-allocator-malloc-c                  2/2 0.88 0.38 +0.50 2/2 taskify:B4
processor-riscv-verilog                    2/2 0.50 0.75 -0.25 2/2 taskify:B1 taskify:B2 taskify:B3 taskify:B4
programming-language-crafting-interpreters 2/2 0.62 0.50 +0.12 2/2 taskify:B1 taskify:B2 taskify:B3
regex-engine-regex-c                       2/2 0.88 0.88 +0.00 2/2 taskify:B4
shell-shell-c                              2/2 0.88 0.50 +0.38 1/2 taskify:B4
text-editor-text-editor                    2/2 0.88 0.88 +0.00 2/2 taskify:B4
web-server-http                            2/2 0.75 0.88 -0.12 2/2 taskify:B4 plan:B4
OVERALL 30 30 0.792 0.742
```
