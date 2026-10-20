The user wants to learn and implement "Docker in ~100 lines of bash" from scratch, and asks me to first plan milestones and create a minimal project skeleton. This is a well-known tutorial concept (e.g., "Docker in 100 lines of bash" using Linux namespaces, chroot, etc.).

Let me think about what's needed:
1. Plan milestones for learning/implementing a mini Docker in bash
2. Create a minimal project skeleton

The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-docker-docker-shell-1` — interesting, the directory name suggests "build-your-own-x docker docker shell". Note: OS is Darwin (macOS), but Docker-in-bash relies on Linux namespaces (unshare, chroot, etc.). So the implementation will target Linux, and on macOS we can only develop/skeleton it, or test in a Docker container / Linux VM. That's an important consideration to note.

Let me first explore the workspace to see what's there.

Per my instructions: Before modifying code, call `explore` once. Then for multi-step change, call `plan`. Then create skeleton.

Let me check the workspace contents first.

Plan for milestones (learning path):
- M0: Environment & skeleton (project structure, README, Makefile, dev container for testing on macOS)
- M1: Filesystem isolation — rootfs preparation (busybox or debootstrap), chroot
- M2: Process isolation — unshare (PID, mount, UTS, IPC, network namespaces), pivot_root
- M3: Resource limits — cgroups v2 (memory, cpu, pids)
- M4: Networking — veth pair, NAT, port mapping (iptables)
- M5: Images & layers — overlayfs, image pull (docker registry API or tar-based), layer caching
- M6: CLI polish — run/exec/ps/rm/stop, container state dir, volumes
- M7: Tests & demo

~100 lines bash core: typically the famous "Docker in 100 lines" uses unshare + chroot + busybox. We'll structure so the core `minidocker` script stays ~100 lines, with helper scripts.

Skeleton:
```
minidocker/
├── README.md
├── Makefile
├── bin/
│   └── minidocker        # main CLI entry
├── lib/
│   ├── common.sh         # shared helpers (logging, state dirs)
│   ├── container.sh      # run/exec logic
│   ├── image.sh          # rootfs/image management
│   └── net.sh            # network setup
├── rootfs/               # built rootfs (gitignored)
├── state/                # container runtime state (gitignored)
├── tests/
│   └── smoke.sh
├── docs/
│   └── milestones.md
└── .gitignore
```

Wait — the workspace root itself is the project dir. Let me check what's in it first. The cwd is `.../build-your-own-x-docker-docker-shell-1`. Maybe it's empty or has some scaffolding. Let me explore.

Also note macOS: bash scripts using unshare won't run natively. I should include a dev container option (Dockerfile that runs the tests inside Linux) — ironic but practical. Or note that testing requires Linux (WSL2, VM, or Docker).

Let me start: explore workspace, then plan, then create files.

I'll do:
1. bash ls / glob to see workspace
2. explore note
3. plan
4. create skeleton files
5. verify (bash -n syntax check, tree listing)

Let me begin.Empty workspace, macOS (Apple Silicon). The mini-docker needs Linux namespaces — so runtime must be Linux. On macOS we can develop and test inside a Linux container (via Docker/OrbStack/colima) or a VM. I'll note that in README and provide a Makefile target to run tests in a Linux container.

Now record exploration, then plan, then create skeleton.现在我来创建骨架文件。Now write bin/minidocker, lib/common.sh, lib/image.sh, lib/container.sh, lib/net.sh, tests/smoke.sh.

Design of bin/minidocker: keep it lean, subcommand dispatch. Since lib modules are stubs for now, the CLI should dispatch to functions defined in those modules. Keep ≤100 lines.

Let me design:

```bash
#!/usr/bin/env bash
# minidocker — a tiny container runtime in ~100 lines of bash.
# Milestones: M1 chroot rootfs, M2 namespaces, M3 cgroups, M4 net, M5 images, M6 lifecycle.
set -euo pipefail

MINIDOCKER_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
STATE_DIR="${MINIDOCKER_ROOT}/state"
IMAGES_DIR="${MINIDOCKER_ROOT}/images"
LIB_DIR="${MINIDOCKER_ROOT}/lib"

# shellcheck source=lib/common.sh
source "${LIB_DIR}/common.sh"
source "${LIB_DIR}/image.sh"
source "${LIB_DIR}/container.sh"
source "${LIB_DIR}/net.sh"

usage() {
  cat <<'EOF'
minidocker — a tiny container runtime (learning project)

Usage:
  minidocker run [options] <image|rootfs-dir> [--] <cmd> [args...]
      options: -d (detached, M6)  --memory=... --cpus=... --pids=... (M3)
               -p host:container (M4)  -v host:container (M6)
  minidocker ps                      (M6)
  minidocker exec <id> <cmd> [args]  (M6)
  minidocker stop <id> [timeout]     (M6)
  minidocker rm <id>                 (M6)
  minidocker logs <id>               (M6)
  minidocker pull <image>            (M5)
  minidocker help
EOF
}

main() {
  local cmd="${1:-help}"
  shift || true
  case "$cmd" in
    run)   container_run "$@" ;;
    ps)    container_ps "$@" ;;
    exec)  container_exec "$@" ;;
    stop)  container_stop "$@" ;;
    rm)    container_rm "$@" ;;
    logs)  container_logs "$@" ;;
    pull)  image_pull "$@" ;;
    help|--help|-h) usage ;;
    *) log_err "unknown command: $cmd"; usage; return 1 ;;
  esac
}

main "$@"
```

That's about 40 lines. Good, leaves room for growth within 100.

lib/common.sh:

```bash
# common.sh — shared helpers: logging, env checks, paths.
# Sourced by bin/minidocker; expects MINIDOCKER_ROOT / STATE_DIR / IMAGES_DIR set.

log_info() { echo "[minidocker] $*" >&2; }
log_err()  { echo "[minidocker] error: $*" >&2; }

require_linux() {
  if [[ "$(uname -s)" != "Linux" ]]; then
    log_err "container runtime features need Linux (you are on $(uname -s))."
    log_err "run tests inside Linux: make test-linux (Docker/OrbStack/colima) or a VM/WSL2."
    return 1
  fi
}

require_root() {
  if [[ "$(id -u)" != "0" ]]; then
    log_err "need root (chroot/unshare/mount/cgroups). try: sudo"
    return 1
  fi
}

ensure_dirs() {
  mkdir -p "$STATE_DIR" "$IMAGES_DIR"
}

new_id() {
  # short random container id
  head -c 8 /dev/urandom | od -An -tx1 | tr -d ' \n'
}
```

Wait, `head -c 8 /dev/urandom | od` gives 16 hex chars. Fine.

lib/image.sh (stub):

```bash
# image.sh — M1 rootfs prep, M5 registry pull + overlayfs assembly.
# Status: skeleton stubs. Implement per docs/milestones.md M1/M5.

# M1: ensure a minimal busybox rootfs exists under $IMAGES_DIR/rootfs-busybox.
image_prepare_rootfs() {
  log_err "image_prepare_rootfs: TODO (M1) — build busybox rootfs"
  return 1
}

# M5: pull image layers from a Docker registry into $IMAGES_DIR.
image_pull() {
  log_err "image_pull: TODO (M5) — Registry API v2: token -> manifest -> layers"
  return 1
}

# M5: assemble overlayfs (lower=images layers, upper/work=container rw layer).
image_mount_overlay() {
  log_err "image_mount_overlay: TODO (M5) — mount -t overlay"
  return 1
}
```

Hmm, but bin/minidocker calls `image_pull "$@"` — name collision: in image.sh I named it image_pull, and dispatch calls image_pull. Good, keep consistent: dispatch calls `image_pull`.

lib/container.sh (stub):

```bash
# container.sh — M2 namespaces, M3 cgroups, M6 lifecycle.
# Status: skeleton stubs. Implement per docs/milestones.md M2/M3/M6.

container_run() {
  log_err "container_run: TODO (M2) — unshare + pivot_root + busybox init"
  return 1
}

container_ps()    { log_err "container_ps: TODO (M6)"; return 1; }
container_exec()  { log_err "container_exec: TODO (M6) — nsenter"; return 1; }
container_stop()  { log_err "container_stop: TODO (M6) — TERM then KILL"; return 1; }
container_rm()    { log_err "container_rm: TODO (M6)"; return 1; }
container_logs()  { log_err "container_logs: TODO (M6)"; return 1; }
```

lib/net.sh (stub):

```bash
# net.sh — M4 bridge + veth + NAT + port publishing.
# Status: skeleton stubs. Implement per docs/milestones.md M4.

net_setup_bridge() { log_err "net_setup_bridge: TODO (M4)"; return 1; }
net_attach_veth()  { log_err "net_attach_veth: TODO (M4)"; return 1; }
net_publish_port() { log_err "net_publish_port: TODO (M4) — iptables DNAT"; return 1; }
```

tests/smoke.sh:

```bash
#!/usr/bin/env bash
# Smoke test: runs everywhere; runtime behavior only asserted on Linux+root.
set -u
cd "$(dirname "$0")/.."

pass=0; fail=0
ok()   { echo "ok   - $1"; pass=$((pass+1)); }
bad()  { echo "FAIL - $1"; fail=$((fail+1)); }

# 1. every shell file parses
for f in bin/minidocker lib/*.sh tests/*.sh; do
  bash -n "$f" && ok "syntax: $f" || bad "syntax: $f"
done

# 2. help works
if out="$(./bin/minidocker help 2>&1)"; then
  [[ "$out" == *"minidocker"* ]] && ok "help prints usage" || bad "help output unexpected"
else
  bad "help exits non-zero"
fi

# 3. unknown command fails
if ./bin/minidocker nope >/dev/null 2>&1; then
  bad "unknown command should fail"
else
  ok "unknown command rejected"
fi

# 4. runtime behavior: only on Linux with root
if [[ "$(uname -s)" == "Linux" && "$(id -u)" == "0" ]]; then
  echo "-- linux runtime checks (M1+) go here as milestones land --"
else
  echo "skip - runtime checks (need Linux + root); use: make test-linux"
fi

echo "smoke: $pass passed, $fail failed"
[[ $fail -eq 0 ]]
```

Careful: `./bin/minidocker nope` — main returns 1, and bin has `set -e`... `main "$@"` returning 1 → script exits 1. Good.

But wait: in bin/minidocker, `shift || true` when no args: `cmd="${1:-help}"`, if no args, cmd=help, then `shift` on empty → error, `|| true` handles. Good.

Also `main "$@"` with set -e: if main returns 1, script exits with 1. Good.

One issue: in dispatch, `run) container_run "$@" ;;` — container_run stub returns 1 → exits 1. Fine for smoke (we don't call run).

Also need `ensure_dirs` called somewhere — maybe in main before dispatch? For stubs it doesn't matter. Keep it minimal; call ensure_dirs in main? It creates state/ and images/ dirs on every invocation including help — slightly noisy but harmless (gitignored). Better: don't call it yet; each milestone will call what it needs. Actually keep skeleton minimal — leave ensure_dirs defined but unused for now. Hmm, unused function is fine in a learning skeleton. Or call it in run/pull paths later. Leave it.

Line count of bin/minidocker: let me count roughly — should be ~45 lines. Good, well under 100 with room to grow.

chmod +x bin/minidocker tests/smoke.sh.

Then run make lint, make test, wc -l.

Let me write all files in parallel, then chmod + verify.All green. bin/minidocker is 58 lines, leaving 42 lines of budget for future milestones within the 100-line target.

Update todos to completed. Then final summary — concise, lead with what was delivered, milestone plan summary, how to start M1. Avoid forbidden phrasings (no "不是...而是", no summary stamps, no conditional next-step menus).骨架已建好，`make lint && make test` 全绿（8 passed），核心脚本 `bin/minidocker` 目前 58 行，100 行预算内还留有 42 行余量。

**里程碑路线**（详见 `docs/milestones.md`，每个都含机制讲解、任务清单、验收标准和提示）：

| 里程碑 | 主题 | 内核机制 |
|---|---|---|
| M0 | 项目骨架（已完成） | — |
| M1 | rootfs + chroot | chroot(2)、busybox 静态二进制 |
| M2 | namespaces | unshare、pivot_root、独立 /proc 与 hostname |
| M3 | 资源限制 | cgroups v2（memory.max / pids.max） |
| M4 | 网络 | veth + bridge + iptables NAT + 端口发布 |
| M5 | 镜像与层 | Registry API v2 拉镜像、overlayfs 写时复制 |
| M6 | 生命周期 | -d / ps / exec(nsenter) / stop / rm / logs / 卷 |

**项目结构**：

```
bin/minidocker      CLI 入口 + 子命令分发（≤100 行预算）
lib/common.sh       日志、require_linux/root、new_id 等助手
lib/image.sh        M1/M5 桩函数（含 Registry API 提示）
lib/container.sh    M2/M3/M6 桩函数
lib/net.sh          M4 桩函数
tests/smoke.sh      冒烟测试（随里程碑扩充运行时断言）
docs/milestones.md  里程碑详细计划
Dockerfile.dev      Linux 测试环境
```

一个关键环境事实：namespaces/cgroups/overlayfs 只存在于 Linux，macOS 上可以开发和跑语法/CLI 冒烟测试，运行容器需 `make test-linux`（通过 Docker/OrbStack/colima 在特权 Linux 容器里执行，Dockerfile.dev 已备好）或任意 Linux VM/WSL2。

从 M1 开始动手：实现 `lib/image.sh` 里的 `image_prepare_rootfs`（下载 busybox 静态二进制搭最小 rootfs），然后在 Linux 环境里让 `minidocker run <rootfs> sh` 走通 chroot。