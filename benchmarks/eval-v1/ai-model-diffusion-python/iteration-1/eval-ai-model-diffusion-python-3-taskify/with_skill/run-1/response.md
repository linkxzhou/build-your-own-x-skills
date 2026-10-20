The user wants me to convert the Hugging Face diffusion course Unit 1, section 3 tutorial into a Claude Code executable learning task list. Let me first fetch the tutorial content to understand what it covers.

Let me fetch the page first.页面内容被截断了。这个教程对应的 notebook 在 GitHub 上，我拉取原始 notebook 获取完整内容。Notebook 很长，继续拉取剩余部分。web_fetch 有截断限制，改用 curl 下载完整 notebook 到本地再解析。拿到完整结构了。提取全部正文和代码，整理成参考文本。I now have the full notebook content. Let me also check the remaining cells I haven't fully read (cells 17-24, the BasicUNet code and training section start). Let me read lines 100-160.I now have the complete notebook content. Let me also read cells 11-13 (corruption visualization) and cell 12 to be complete.

Actually I've read lines 72-87 partially. Let me check lines 72-100.教程内容已完整提取。这个任务匹配 build-your-own-x skill（从零实现扩散模型），先读取 skill。主题是 diffusion → `ai-model` track。按 skill 要求读取 track skill。Skill 与教程内容都已就位。先记录探索结论，再产出任务清单。Now let me plan the deliverable. The user wants: "把这个教程转换成 Claude Code 可执行的学习任务清单" — convert the tutorial into a Claude Code executable learning task list.

The deliverable is a task list document (likely a TASKS.md or similar file in the workspace) that Claude Code can execute milestone by milestone. Per the skill:
- 4-8 milestones, each with a runnable checkpoint
- Teaching loop per milestone
- Don't dump full solutions
- Progress tracked in PROGRESS.md
- Install commands printed for learner
- Credit upstream tutorial with exact link

The task list should be structured so that a Claude Code session can pick up milestone by milestone. It should include:
- Project context and goal
- Prerequisites (env setup, installs the learner runs)
- Milestones M1-M7 with: goal, concepts, files to create, what the learner writes vs what's scaffolded, checkpoint commands with expected outputs, reference cells in .ref/notebook_text.txt
- Stretch goals
- Progress tracking convention

Let me design the milestones based on the notebook structure:

M0/M1: Environment + data — install diffusers/torch, download MNIST, verify batch shape (8,1,28,28), plot grid. Checkpoint: python script prints shape and saves grid image.

M2: Corruption process — implement corrupt(x, amount) with torch.rand_like, verify: amount=0 returns x, amount=1 returns noise in [0,1], output range stays [0,1], broadcasting works with per-sample amounts. Checkpoint: pytest or assert script + visualization.

M3: BasicUNet — implement minimal UNet (3 down conv layers, 3 up, skip connections, MaxPool2d down, nn.Upsample up, SiLU). Checkpoint: output shape == input shape for (8,1,28,28); param count ~309k (309,057 exactly with the notebook config). Learner writes forward pass.

M4: Training — training loop: random noise amounts, MSE against clean x, Adam lr=1e-3, batch 128, 3 epochs (CPU smoke: 1 epoch or subset). Checkpoint: loss curve saved, avg loss decreasing; prediction visualization at different noise amounts.

M5: Naive sampling — iterative sampling with mix_factor = 1/(n_steps - i), 5 steps then 40 steps. Checkpoint: generates 64 images grid, recognizable digits (qualitative), plus deterministic checks (output range [0,1], shape).

M6: DDPM comparison — UNet2DModel config, DDPMScheduler(1000), plot alphas_cumprod curves, add_noise visualization with randn and (-1,1) mapping. Checkpoint: scheduler tests (t=0 ≈ x, t=999 ≈ noise), param count ~1.7M.

M7: DDPM training objective + sampling — train UNet2DModel predicting noise (eps) with timestep conditioning, loss vs noise target; sample with scheduler.step loop. Checkpoint: loss ≈ 1.0 baseline dropping below ~0.5 (on CPU maybe fewer steps), generated samples via DDPM sampling look like digits.

Stretch: FashionMNIST swap, train longer, timestep conditioning fed as amount*1000, v-prediction reading, DDIM scheduler comparison.

That's 7 milestones + stretch — fits the 4-8 requirement.

Each milestone needs:
- 概念 (3-6 sentence explanation pointer)
- 学习者写什么 (the core the learner implements)
- 参考教程段落 (cell numbers)
- 检查点命令 + 预期输出
- 常见坑 (broadcasting, rand vs randn, .sample, clip)

Also project structure:

```
diffusion-from-scratch/
  README.md
  PROGRESS.md
  requirements.txt
  data/            (MNIST auto-download)
  src/
    corrupt.py
    unet.py
    train.py
    sample.py
    ddpm_compare.py
  tests/
    test_corrupt.py
    test_unet.py
    test_scheduler.py
  outputs/         (png artifacts)
```

The task list file itself should be executable by Claude Code: each task has clear "definition of done" with commands Claude Code can run and verify. Also include the coaching rules so a future Claude Code session follows the skill (don't dump solutions, learner writes core).

Where to put it? The workspace root. Let me check what's in the workspace currently.

Also per skill: "Stay in the learner's workspace. Never run install commands yourself" — the task list should note that installs are run by the learner.

Let me check the workspace structure first, then write the file. I should also create a plan since this is a multi-step deliverable? The deliverable is a single document file. The plan tool is for code changes; here it's one file write. I'll skip `plan` (single-file deliverable, no code modification) — actually the instructions say for any multi-step change call plan. This is a single file write, so it's fine without. But I did explore. Let me just write the file.

Let me check workspace contents first.环境确认：Python 3.14、无 torch，工作区为空项目。现在写任务清单文件。验证清单中的关键数值断言（参数量、调度器边界值）：数值断言全部验证通过（309057 参数、ᾱ₀=0.9999、ᾱ₉₉₉≈4e-5）。修正 M3 常见坑里一处误导性描述：任务清单已生成：`TASKS.md`（工作区根目录），配套参考材料在 `.ref/notebook_text.txt`（教程全文按 CELL 分段）。

**转换方式**：拉取了教程对应的完整 notebook（51 cells）作为事实来源，按 build-your-own-x 的 ai-model/diffusion track 规范，映射成 8 个里程碑（M0–M7），每个都有可运行检查点：

| 里程碑 | 内容 | 检查点核心 |
|---|---|---|
| M0 | 环境 + 项目骨架 | import 四件套无报错 |
| M1 | MNIST 数据加载 | shape `(8,1,28,28)`、值域 [0,1]、网格图 |
| M2 | `corrupt()` 线性加噪 | 5 条断言（amount=0 恒等、广播正确、值域）+ 可视化 |
| M3 | BasicUNet | 输出形状一致、参数量 `== 309057`（已手算验证）、backward 通过 |
| M4 | 训练预测干净图 | loss 下降、低噪声区预测好、amount→1 退化为均值 |
| M5 | 朴素迭代采样 | 5 步过程图 + 40 步 64 张可辨认数字 |
| M6 | DDPM 对照：UNet2DModel + DDPMScheduler | ᾱ 边界断言（0.9999 / 4e-5，已验证）、add_noise 端点行为 |
| M7 | eps 预测目标 + scheduler 采样 | loss 起点 ≈1.0（方差基线）、生成质量优于 M5 |

**清单内置的执行协议**让任何 Claude Code 会话都能直接接手：一次一个里程碑、教学循环（概念→骨架→学习者写核心→检查→复盘）、不给全量代码、安装命令由学习者执行、通过后记入 `PROGRESS.md`、只读当前里程碑标注的 CELL 区段。每个里程碑都标注了对应的 notebook CELL 编号和常见坑（广播、`rand` vs `randn`、`.sample`、(-1,1) 归一化）。

所有数值断言（参数量 309057、调度器边界）都经过本地计算验证，CPU 环境通过 `--smoke` 模式可在几分钟内跑完每个检查点。从 M0 开始逐条执行即可。