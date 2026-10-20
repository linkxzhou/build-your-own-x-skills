The user wants to learn and implement "Malloc is not magic -- Implementing your own memory allocator" from scratch in C. They want me to first plan milestones and create a minimal project skeleton.

This matches the build-your-own-x skill. I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file is truncated. Let me read more of it, and also find the malloc track skill.The topic maps to the `memory-allocator` track, and there's a per-tutorial skill for the exact article. Let me read the track skill first (mandatory), plus check what exists.Let me read the rest of the malloc-c skill, the track skill (memory-allocator/SKILL.md), and the tutorial-map.md.Let me read the rest of the track skill, the concepts reference, the minimal example README, and check the current workspace state.工作区是空的，工具链是 macOS 上的 Apple clang —— 这会影响后面的技术选型（sbrk 在 macOS 上已废弃、LD_PRELOAD 受 SIP 限制），我会把这些约束记下来。先记录探索结论，再看一眼上游教程清单。技能与上下文都齐了：工作区为空、Apple clang 21 / macOS（这决定了用 `mmap` 替代已废弃的 `sbrk`，M5 的 `LD_PRELOAD` 检查点也要适配）。先落计划，再建骨架。计划已定。现在批量创建骨架文件（文档、API 契约、桩实现、测试、Makefile），同时取系统日期用于进度记录。所有文件已写入。现在验证基线：`make test` 应编译通过、测试为红（桩返回 NULL）。基线符合预期：编译零警告通过（`-Werror` + ASan/UBSan），测试为红。核对失败数：1256 = 1000（对齐测试的 NULL 检查）+ 256（堆增长测试的 NULL 检查），与桩实现完全一致。写入进度记录并收尾。骨架就绪，基线已验证：编译零警告（`-Wall -Wextra -Werror` + ASan/UBSan），`make test` 为红（1256/1256 失败 = 1000 + 256 个 NULL 检查，与桩实现完全吻合）。

```
README.md             里程碑表 + macOS 注意事项 + 上游署名
PROGRESS.md           进度记录（M0 骨架已过）
Makefile              make test / make clean
src/myalloc.h         公共 API 契约（4 个函数 + 3 个诊断接口）
src/myalloc.c         桩实现，TODO 注释标出每步要写什么
tests/test_myalloc.c  极简测试框架 + M1 检查点
```

里程碑路线（每个都有可运行检查点，过关才前进）：

| # | 里程碑 | 检查点 |
|---|---|---|
| M1 | Bump allocator | 1000 次分配全部 16 字节对齐且可写；累计 1 MiB 成功 |
| M2 | 块头 + free | malloc/free/malloc 复用刚释放的块（同地址） |
| M3 | 拆分 + 合并 | 碎片测试：free 序列后大分配成功且堆不增长 |
| M4 | calloc / realloc | 含 `realloc(NULL, n)`、`realloc(p, 0)` 的单元测试 |
| M5 | 线程安全 + 接管 | `DYLD_INSERT_LIBRARIES=./libmymalloc.dylib /bin/ls -l` |
| M6 | 度量 | 随机负载下 vs 系统 malloc 的吞吐/碎片表 |
| M7 | size classes / arenas | 多线程 benchmark 有提升 |

两个平台适配已定：堆增长用 `mmap`（macOS 的 `sbrk` 已废弃），M5 用 `DYLD_INSERT_LIBRARIES`（`LD_PRELOAD` 受 SIP 限制）。

**当前：M1 / 7。** 概念一句话：分配器先向内核要一大块内存，然后只把指针往前推（bump），对齐就是向上取整到 16 的倍数。你接下来在 `src/myalloc.c` 的 `my_malloc` 里写：

1. 一个静态指针记录堆当前位置，首次调用时用 `mmap` 申请一块（比如 1 MiB）；
2. 把 `size` 向上对齐到 16；
3. 若剩余空间够，返回当前指针并把指针前移；不够就再 `mmap` 一块。

检查命令：`make test`，预期输出 `OK: 1256 checks passed`。卡住时说一声，我一次给一条提示。