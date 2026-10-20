The user wants to learn and implement Diffusion Models for Image Generation from scratch in Python. They ask me to first plan milestones and create a minimal project skeleton.

This matches the `build-your-own-x` skill — "从零实现" (implement from scratch), and diffusion models fall under "a neural network" / LLM-ish category. The skill description explicitly mentions Chinese triggers: 从零实现、想通过做项目学底层原理. So I MUST read the skill's SKILL.md first before doing anything else.

Let me read the skill file first.The file is truncated. Let me read the rest of it, and also look at the skills directory to find the relevant track skill for diffusion models / neural networks.The topic maps to the `ai-model` track, and there's an exact per-tutorial skill: `ai-model-diffusion-python`. Reading both now (track first, then the tutorial skill).Both files are truncated. Reading the remaining parts plus the mandated `references/tutorial-map.md`.Now let me check the minimal example scaffold guidance and the tutorials.md for the exact upstream link. Also check the workspace state (is it empty?).Workspace is empty (fresh start), and the upstream tutorial is the Hugging Face diffusion course. Let me check the local Python environment before scaffolding.Python 3.14.7, pytest available, but no torch/torchvision/matplotlib. Per the skill rules: never install anything myself; print the exact command for the learner and ask before installing torch. Python 3.14 is very new — torch may not have wheels for 3.14 yet (torch supports up to 3.13 as of late 2025; 3.14 support is likely missing). I should flag this: the learner may need Python 3.11–3.13 for torch. Let me check if other pythons are available.Environment findings: Python 3.14 (default, no torch wheels yet), python3.12 available (torch-compatible), uv present, pytest only on 3.14. Per the coaching rules I won't run any installs — I'll hand you the exact commands. Recording the exploration note and the plan now.Plan is set. Now writing the skeleton files.Now verifying the M0 checkpoint: run the tests and the noise module demo.All green. One cosmetic fix: the package `__init__` re-imports `noise`, which triggers a RuntimeWarning under `python3 -m`. Simplifying it.骨架已就绪，M0 检查点全绿。项目跟着 build-your-own-x 收录的 [Hugging Face Diffusion Course — Unit 1](https://huggingface.co/learn/diffusion-course/en/unit1/3) 走，里程碑规划在 `README.md`，进度记录在 `PROGRESS.md`。

**当前位置：M0 / M6 完成**（骨架 + 噪声调度数学）。

**M0 概念（3 句）**：DDPM 的前向过程按 `beta_t` 逐步给图像加高斯噪声，1000 步后变成纯噪声；`alpha_bar_t = prod(1-beta)` 是闭式解里「原始信号还剩多少」的系数。`diffusion_lab/noise.py` 已实现调度查表，运行 `python3 -m diffusion_lab.noise` 可以看到：t=500 时信号只剩 27.9%，t=999 只剩 0.006% —— 这就是「噪声吞掉图像」的数值直觉，M2 的 `q_sample` 会直接用到这两个系数。

**你需要自己跑的环境命令**（torch 没有 3.14 的包，本机已有 3.12；我按规则不代跑安装）：

```bash
uv venv --python 3.12 .venv && source .venv/bin/activate && uv pip install -r requirements.txt
```

**下一步 M1（数据管线）**：打开 `diffusion_lab/data.py`，按里面的接口提示实现 `get_dataloader` —— 加载 MNIST、归一化到 [-1,1]、下载失败时用合成数据兜底。检查命令：

```bash
python3 -c "from diffusion_lab.data import get_dataloader; b,_ = next(iter(get_dataloader(4))); print(b.shape, b.min().item(), b.max().item())"
```

预期输出 `torch.Size([4, 1, 28, 28])` 和约 `-1.0` / `1.0`。写完贴给我或直接说卡住了，我们从真实输出开始调。