The user wants me to look at the bocker repository (a Docker implementation in ~100 lines of bash) and convert it into a learning task checklist that Claude Code can execute.

First, I should check the build-your-own-x skill since this matches its description — someone wants to learn by rebuilding real software from scratch (Docker/containers). Let me read that skill first.

Then I should fetch the bocker repo to understand its content, and produce a learning task list (probably as a markdown file) that Claude Code can execute step by step.

Let me start by reading the skill.GitHub 页面抓取效果不佳。我来获取原始的 README 和脚本，并检查 docker 跟踪技能。该技能要求读取 docker track skill。我正在读取它，以及 bocker 脚本的其余部分。有一个针对每个教程的 `docker-docker-shell` 技能——很可能是 bocker。我正在阅读它以及 docker track skill 的其余部分。Let me read the rest of docker-docker-shell/SKILL.md (it was truncated) and check references/tutorial-map.md.我已经准备好所需的一切：完整的 bocker 脚本、README 以及技能的转换规则。在写入 `TASKS.md` 之前，我正在检查工作区根目录。工作区为空。正在写入 `TASKS.md` —— 转换后的学习任务清单。`TASKS.md` 已生成。转换基于 bocker 原版脚本和 README 逐函数核对，并按 docker-docker-shell 技能的教练模式组织。

结构：9 个里程碑，每个含目标、核心概念、涉及文件、任务、验证命令与期望输出。

- **M0** 环境搭建 + 命令分发骨架（btrfs/bridge0/ip_forward/NAT、`case` 分发、`#HELP` 自文档）
- **M1** 镜像存储层：`init`/`check`/`images`，btrfs subvolume + CoW 快照
- **M2** 拉取镜像：原版依赖已停服的 Registry v1 API，清单里给了 2025 年可用的两条替代路径（Alpine minirootfs 简化版 → Registry v2 拉伸版）
- **M3** chroot 文件系统隔离（镜像 snapshot → 容器）
- **M4** `unshare -fmuip --mount-proc` 四 namespace 进程隔离
- **M5** cgroups 资源限制（`cgcreate/cgset/cgexec`，`--CPU_SHARE=` 参数解析）
- **M6** veth + bridge + netns 网络
- **M7** `ps`/`logs`/`exec`/`rm`/`commit` 生命周期闭环，验证对应原 README 完整示例流程
- **M8** 拉伸任务：端口转发、数据卷（原版未实现的两项）、overlayfs、cgroup v2

使用方式：每个里程碑开工时对 Claude Code 说 `读取 TASKS.md，开始 M<N>`，它会按「讲概念 → 给骨架 → 你写核心 → 跑验证」推进，通过后记入 `PROGRESS.md`。

两个前置提醒已写进 M0：必须在 Linux VM 里跑（脚本以 root 改网络和防火墙），且需选 cgroup v1 发行版（CentOS 7 / Ubuntu 18.04），否则 M5 要按拉伸任务改写。

---

**M0 检查点**（环境就绪后运行）：

```
$ ./bocker help
```

期望输出：列出 `pull init rm images ps run exec logs commit` 全部子命令及用法；同时 `ip addr show bridge0` 显示 `10.0.0.1/24`。