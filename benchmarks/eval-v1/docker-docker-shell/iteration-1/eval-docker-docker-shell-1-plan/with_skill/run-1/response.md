The user wants to learn by building "Docker in ~100 lines of bash" from scratch. This matches the build-your-own-x skill. I must read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also find the Docker track skill. The category map was truncated. Let me read more lines.主题已映射到 `docker` 跟踪，并且存在一个与“~100 行 bash”匹配的针对特定教程的技能 `docker-docker-shell`。正在读取这两个文件（跟踪技能是必需的，然后是教程技能）。两个技能已加载。现在正在读取引用的文件：`tutorial-map`、`concepts`，以及 docker track skill 的末尾被截断的部分。技能已加载。在搭建骨架之前，我需要了解环境（Linux 内核、root 权限、工作区状态），因为 bocker 需要带有 namespace/cgroup 支持的 Linux 环境。环境检查完成，有一个关键发现：**当前机器是 macOS (Darwin/arm64)**，而 bocker 依赖 Linux 内核的 namespace/cgroup/chroot，这些在 macOS 上无法原生运行。这不影响今天建骨架（纯 bash 文件），但 M2 之后的验证需要 Linux 环境（ privileged 容器或 Linux VM），我会在计划里标注。

先记录探索结论并制定计划：计划已建。现在执行 s1：创建骨架文件。骨架已建好并通过冒烟测试。项目结构：

```
bocker/
├── bocker            # 主脚本：严格模式 + 路径约定 + case 分发 + 各里程碑 TODO 桩
├── README.md         # 里程碑表、环境要求、目录约定
├── PROGRESS.md       # 每个里程碑通过后记录检查命令与结果
└── tests/smoke.sh    # M1 冒烟测试（bash -n / help / 未知命令报错）
```

## 里程碑规划

| # | 里程碑 | 核心概念 | 检查点 |
|---|---|---|---|
| M1 ✅ | 骨架与命令分发 | 严格模式、路径约定、case 分发 | `./bocker help` 可用，smoke 全绿 |
| M2 | `bocker pull` | Registry v2 API：匿名 token → manifest → 逐层下载 blob → tar 解包 | `./bocker pull alpine 3.19` 后 `bocker_images/alpine_3.19/bin/sh` 存在 |
| M3 | `bocker run` 基础隔离 | unshare(mount/pid/uts/ipc) + chroot 进镜像目录 + 容器内挂 /proc | 容器内 `ls /` 是镜像根、`hostname` 与宿主机不同、`ps` 只见自己 |
| M4 | cgroups | cgroup v2 `memory.max` / `pids.max` | 内存大户被 OOM 杀掉，宿主机无恙 |
| M5 | 生命周期 | 容器目录即状态：psid 目录存在=容器存在，stdout 重定向即 logs | `ps`/`logs`/`rm`/`images`/`cleanup` 可用 |
| M6 | 网络（stretch） | veth pair + bridge + NAT | 容器内 ping 通宿主机 veth IP |

上游教程：[p8952/bocker](https://github.com/p8952/bocker)（约 100 行 bash，子命令 pull/run/ps/logs/rm/images/cleanup）。

## 环境提醒

当前机器是 macOS（Darwin arm64）。M1 骨架已在本地验证通过；**M2 起需要 Linux + root**（namespace/cgroup/chroot 是 Linux 内核设施）。到时用 privileged 容器或 Linux VM 跑即可：

```bash
docker run --privileged -it -v "$PWD":/bocker -w /bocker debian bash
```

## M2 起步：bocker pull

概念（30 秒版）：Docker 镜像就是「一堆 tar 层」。Registry v2 是纯 HTTP API——先向 `/token` 换匿名 token，再 GET `/manifests/<tag>` 拿到层的 digest 列表，逐个 GET `/blobs/<digest>` 下载 tar 并解包到 `$BOCKER_IMAGES/<repo>_<tag>/`。层按顺序解包，后层覆盖前层，这就是「镜像分层」的全部秘密。

你要写的核心（`bocker/bocker` 里的 `bocker_pull`，约 20 行）：

1. `curl` 拿 token（`auth.docker.io/token?service=registry.docker.io&scope=repository:<repo>:pull`）
2. 带 `Accept` 头 GET manifest（注意 manifest 本身可能是被引用的 index，需要再取一次）
3. 遍历 `layers[].digest`，逐个下载 blob 并 `tar -xf` 到镜像目录
4. 结束后 `ls` 一下镜像目录确认有 `/bin/sh`

先动手写，卡住了把报错贴给我，我们从真实输出开始调。