The user wants to learn by building "Docker in ~100 lines of bash" from scratch. This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it.主题映射到 `docker` 轨道。正在读取轨道技能，并检查是否有针对特定教程的技能。The docker track skill is at `.agents/skills/build-your-own-x/skills/docker/SKILL.md`. There's also `docker-go` and `docker-docker-python` per-tutorial skills. The user wants bash — let me read the docker track skill first (mandatory), then check the per-tutorial ones. The famous "100 lines of bash docker" is likely "Docker in 100 lines of bash" — there's a known article "Build your own Docker with Bash" or the one by "docker in 100 lines of bash" (e.g., https://github.com/p8952/... no). Actually there's a well-known one: "Docker in 100 lines of bash" by... Let me read the track skill first.现在我来查看教程列表，以寻找 bash 相关的教程（即著名的 "bocker"）。Shell 轨道对应的上游教程是 **bocker**（p8952/bocker，"Docker implemented in around 100 lines of bash"），没有单独的 per-tutorial skill，直接按 docker track 的里程碑表来。先确认一下当前环境（bocker 需要 Linux + root）：环境是 macOS (arm64, bash 3.2, 非 root)——这决定了里程碑的验证方式，稍后详述。先记录探索结论并制定计划：骨架已建好并通过验证（`bash -n` OK，usage 和 stub 路径都能跑）。项目在 `bocker/` 下：`bocker`（唯一实现文件，case 分发 + 每个里程碑一个 TODO 函数）、`PROGRESS.md`（里程碑表 + 检查点日志）、`README.md`、`scratch/`。

**先说环境限制**：namespace/cgroup/chroot 全部需要 Linux + root。你现在的 Mac 只能用来写代码和 `bash -n` 语法检查，所有检查点要在 Linux VM 里跑（Ubuntu 22.04+，multipass/Lima/UTM 都行，命令见 README）。

**里程碑路线**（跟 upstream [p8952/bocker](https://github.com/p8952/bocker) 对齐，细节在 `PROGRESS.md`）：

1. **run 一条命令** — 父子 re-exec 模式
2. **UTS + PID namespace** — 主机名隔离、容器内 PID 1
3. **文件系统隔离** — mount ns + pivot_root + alpine rootfs（`bocker pull`）
4. **cgroups v2** — memory/pids 限制
5. **网络**（stretch）— veth pair + bridge + NAT
6. **镜像层**（stretch）— overlayfs + `ps/images/rm/log`

**Milestone 1/6 — re-exec 模式**

概念：`bocker run` 本身是父进程，它用 `unshare --fork` 创建带新 namespace 的子进程，并让子进程**重新执行 bocker 自己**（`exec "$0" _init ...`）。子进程从 `case` 里的 `_init` 分支进入，从此它就是容器里的 PID 1。这个「自己 exec 自己」的技巧让一个 bash 文件同时扮演 docker CLI 和容器 init。

你要写的：`bocker/bocker` 里的 `bocker_run()`（第 24 行附近），把 TODO 换成：解析参数 → `exec unshare --fork "$0" _init <cmd...>`。M2 再往 unshare 加 namespace 标志，所以 M1 先只用 `--fork` 验证管道通。

**检查点**（在 Linux VM 里，项目目录下）：

```
sudo ./bocker run alpine /bin/echo hi
# 期望输出：hi        （当前 stub 会打印 TODO(m1) 并 exit 1）
```

写完 `bocker_run` 后跑上面这条命令，把实际输出贴给我——过了就进 M2。