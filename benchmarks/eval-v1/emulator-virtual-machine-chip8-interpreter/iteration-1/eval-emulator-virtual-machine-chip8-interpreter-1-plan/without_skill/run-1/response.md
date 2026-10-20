The user wants to learn how to write a CHIP-8 interpreter emulator from scratch in C++. They want me to:
1. Plan milestones
2. Create a minimal project skeleton

Let me first check the current workspace to see what's there. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-emulator-virtual-machine-chip8-interpreter-1` — this looks like a clone of the "build-your-own-x" repo guide for CHIP-8 interpreter.

Let me explore the workspace first, then plan milestones and create the skeleton.

I should:
1. Look at what's in the workspace (maybe there's a guide/README)
2. Create a plan with milestones
3. Create minimal project skeleton (CMakeLists.txt, main.cpp, chip8.h/cpp, etc.)

Let me start by exploring the directory.工作区是空的，我先记录探索结果并确认构建环境，然后规划里程碑、创建骨架。工具链齐全（cmake 4.2.3 + clang++ 22）。检查一下 SDL2 是否可用，这决定图形里程碑的选型。SDL2 已就绪。下面是里程碑规划，然后创建骨架。构建成功但有 4 个警告，查看并修复。警告来自 M1 才会使用的私有字段。用 `[[maybe_unused]]` 标注，M1 实现后可移除：骨架已就绪，构建零警告，冒烟测试通过（正常 ROM 打印就绪、坏 ROM 报错退出）。

## 里程碑路线图

| 里程碑 | 内容 | 验收标准 |
|---|---|---|
| **M0 骨架**（已完成） | CMake + `Chip8` 类数据布局 + `loadROM` | 编译运行通过 |
| **M1 核心解释器** | 字体集、35 个 opcode、定时器 | 单元测试驱动 `cycle()` 通过 |
| **M2 图形与输入** | SDL2 渲染 64×32、16 键映射 | IBM logo ROM 显示正确 |
| **M3 声音与节奏** | 音频回调、CPU 节流 ~600 op/s | 声音正常、节奏稳定 |
| **M4 兼容性** | Timendus 测试套件、VF/移位行为差异 | 测试套件全过 |
| **M5 打磨**（可选） | 反汇编器、调试单步 | — |

## 项目结构

```
├── CMakeLists.txt      # C++17，-Wall -Wextra
├── README.md           # 路线图 + 构建说明 + 参考资料
├── src/
│   ├── chip8.h         # 4KB 内存、V0–VF、栈、定时器、64×32 显示、键盘
│   ├── chip8.cpp       # loadROM 已实现；cycle() 留了译码惯例注释
│   └── main.cpp        # 入口，M1/M2 的接入点已用 TODO 标出
└── tests/              # M1 起添加
```

关键设计决定：`cycle()` 里已写好译码惯例（`X/Y/N/NN/NNN` 的位提取），M1 直接照着 Cowgod's Reference 逐个填 opcode 即可；`display`/`keypad`/`drawFlag` 设为 public，方便 M2 的 SDL2 层访问。

下一步是 M1：先把字体集（80 字节）写进 `0x050`，然后从最简单的 opcode 开始实现（`00E0` 清屏、`1NNN` 跳转、`6XNN` 置寄存器），每实现一批就配一个单元测试。