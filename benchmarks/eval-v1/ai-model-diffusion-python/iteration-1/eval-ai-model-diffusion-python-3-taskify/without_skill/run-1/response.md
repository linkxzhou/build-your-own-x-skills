The user wants me to fetch the Hugging Face diffusion course Unit 1, part 3, and convert it into a Claude Code executable learning task list. Let me fetch the page first.页面被截断了，我去拉取对应的原始 notebook 获取完整内容。先看工作区现状，并把完整 notebook 下载到本地以便提取全部任务点。I now have a complete picture of the notebook. Let me also check the remaining part of cell 39 and cell 50 (conclusions), plus the truncated part of cell 49. Actually I have enough. Let me also check the truncated cell 49 ending and cell 50.

Let me get the last bits quickly.Notebook 内容已完整提取。工作区为空，我将教程转换为一份 Claude Code 可逐任务执行、每步带验收命令的任务清单，写入 `TASKS.md`。Let me verify the file is written correctly and check the final acceptance criteria works.已生成 `TASKS.md`，将 Unit 1.3 教程（notebook `02_diffusion_models_from_scratch.ipynb`，已完整拉取原文）转换为 11 个可执行任务：

**结构**
- **T0–T5（from scratch 部分）**：环境 → MNIST 数据 → `corrupt` 线性加噪 → ~309k 参数的 `BasicUNet` → 训练（MSE 预测干净图）→ 手写迭代采样（5 步 / 40 步）。此阶段限制只用 `torch`/`torchvision`。
- **T6–T9（DDPM 对比部分）**：`UNet2DModel`（~1.7M，含 attention）→ `DDPMScheduler` 加噪调度（高斯噪声、(-1,1) 归一化）→ 噪声预测目标 + timestep conditioning → `scheduler.step` 标准采样。教程中这两节只有理论，代码标注为“实现题”，按讲义给出的伪代码自行补全。
- **T10**：toy vs DDPM 六维度对比笔记。

**每个任务包含**：对应教程小节、具体步骤（含教程原版代码片段）、可直接运行的验收命令（shape/参数量断言、产物文件检查）、需记入 `NOTES.md` 的观察结论。

**使用方式**：把单个任务作为 Claude Code prompt，例如“执行 TASKS.md 中的 T3，完成后运行其验收命令”。产物约定：代码进 `src/`，图片进 `outputs/`，权重进 `checkpoints/`。

两处适配说明：设备选择改为 `cuda→mps→cpu` 回退（本机 macOS）；T2 验收中的断言基于同 seed 下噪声项一致性，比教程的纯目视检查更可自动化。