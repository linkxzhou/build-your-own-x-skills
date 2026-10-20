The user wants me to convert the bocker tutorial (https://github.com/p8952/bocker) into a Claude Code executable learning task list. This matches the build-your-own-x skill — "build your own Docker/containers" category. Let me read the skill first.

Let me start by reading the SKILL.md file.GitHub 页面抓取到的主要是导航栏。让我获取原始 README 并读完 skill 文件。主题映射到 `docker` track。按 skill 要求，先读 track skill，并检查是否有 bocker 专属的 per-tutorial skill。存在 `docker-docker-shell` per-tutorial skill，很可能就是 bocker。读一下。这个 per-tutorial skill 正是 bocker。读它的两个 reference 文件。Skill 链路已确认：`build-your-own-x` → `docker` track → `docker-docker-shell`（正是 bocker）。再抓一下 bocker 源码，让任务清单能落到真实函数名上。工作区是 macOS (arm64)——bocker 需要 Linux + root + btrfs，任务清单必须包含 Linux VM 环境。源码文件名 404 了，用 GitHub API 查实际结构。Readability extraction is dominated by GitHub chrome. Let me try fetching the repo as HTML with a different approach — maybe use the github.com HTML page and grep for file names, or try common filenames: bocker, bocker.sh, bocker.bash. The README says "a Vagrantfile is included". Let me try raw for likely names: `bocker`, `bocker.sh` failed. Try `bocker.sh` on master... failed. Maybe the file is just `bocker`. Let me try raw.githubusercontent.com/p8952/bocker/master/bocker.拿到大部分源码，还差尾部。用 curl 拉全量到临时文件读取。源码全部拿到（119 行，函数齐全）。写文件前先看下工作区的 AGENTS.md 约定。材料齐了。先记录探索结论，再定计划。函数名 11/11 全覆盖，无核心逻辑泄漏（`cgcreate` 是单条环境命令，属允许的骨架提示）。发现一处内部不一致：M1 阶段函数还没有 `#HELP` 注释，`./bocker` 会打印空内容，验收却要求「打印用法」。修正 1.4 的提示。已生成 `bocker-tasks.md`（工作区根目录），把 bocker 教程转成了 8 个里程碑的可执行任务清单，每个里程碑带概念讲解、TODO 列表和可运行的验收命令。

**清单结构**

| 里程碑 | 内容 | 验收 |
|---|---|---|
| M0 | Linux VM + btrfs/bridge/ip_forward/NAT 环境 | 4 条自检命令 |
| M1 | 脚本骨架、case 分发、`--KEY=VAL` 解析 | `./bocker help` |
| M2 | btrfs subvolume 镜像层 + 最小 run | `bocker run img_x cat /etc/alpine-release` |
| M3 | `unshare -fmuip` + chroot 隔离 | 容器内 `ps` 只见 PID 1 |
| M4 | cgroup CPU/内存配额 | `/proc/1/cgroup` 与 limit 文件核对 |
| M5 | veth + bridge + netns 网络 | 容器 `ping 10.0.0.1` / `8.8.8.8` |
| M6 | exec / logs / commit | 复现上游 README 完整示例流 |
| M7 | help 自描述、边界、回归、PROGRESS.md | 全流程回归 |

**转换时处理的三个现实问题**

1. **环境**：当前机器是 macOS arm64，bocker 需要 Linux + root + btrfs，M0 专门搭环境（推荐 OrbStack，备选 multipass/Vagrant），安装命令列出但由你自己执行。
2. **`bocker pull` 已失效**：上游走的是已下线的 Docker Registry v1 API。清单改用 `bocker init` + alpine minirootfs 造镜像走通主线，Registry v2 改写留作 M7 后的扩展任务（附录 A）。
3. **cgroup 版本**：新版 Ubuntu 默认 cgroup v2，`cpu.shares`/`memory.limit_in_bytes` 要换成 `cpu.weight`/`memory.max`，差异写在附录 B，M4 任务里带检测命令。

**自检结果**：11 个上游函数名全部覆盖且与源码一致；11 个 bash 代码块全部通过 `bash -n` 语法检查；无成品代码泄漏（只给函数骨架提示，核心逻辑留给学习者写）。

用法：新会话里把 `bocker-tasks.md` 交给 Claude Code，说「执行 M0」或「继续下一个里程碑」即可。