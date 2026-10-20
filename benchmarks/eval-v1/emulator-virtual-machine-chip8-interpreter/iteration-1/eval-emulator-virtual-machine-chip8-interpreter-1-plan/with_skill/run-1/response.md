The user wants to learn how to write a CHIP-8 interpreter/emulator from scratch in C++. They want me to:
1. Plan milestones
2. Create a minimal project skeleton

This matches the `build-your-own-x` skill. I should read that skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also look for the emulator track skill. The category map was truncated. Let me read more of the file and find the skills directory.The topic maps to the `emulator-virtual-machine` track. Reading that track skill now.There's a track skill `emulator-virtual-machine/SKILL.md` and a per-tutorial skill `emulator-virtual-machine-chip8-interpreter/SKILL.md`. The track skill is mandatory. Let me read both — the track skill first, then the chip8-interpreter one (which is likely the "How to write an emulator (CHIP-8 interpreter)" by Tania — that's the famous tutorial "chip8" by Tania (taniarascia/chip8)... Actually "How to write an emulator (CHIP-8 interpreter)" is the well-known tutorial by Tania Rascia. Let me read the track skill and the chip8-interpreter skill.Both skills loaded. The track skill references `references/tutorials.md` and the per-tutorial skill references `references/tutorial-map.md`. Let me read those plus the rest of the track skill.技能已加载。范围已确定：C++、CHIP-8、multigesture.net 教程。现在我来检查工作区状态和可用的工具链，以及该技能的最小示例 README。工作区是空的（仅包含 `.agents/` 和 `AGENTS.md`），且工具链已就绪（Apple clang 21, CMake 4.2, make）。让我检查一下 `AGENTS.md` 中的工作区规则，以及 SDL2 是否已存在（这与后续的显示里程碑相关）。技能与工具链都确认了：`emulator-virtual-machine` 轨道 + 上游教程《How to write an emulator (CHIP-8 interpreter)》（multigesture.net，C++），本机有 Apple clang 21、CMake 4.2、SDL2 2.32.10（M4 显示阶段直接可用）。先记录探索结论，再立计划。开始执行。先写 README 与构建配置（s1、s2 相互独立，并行写）。测试需要能读到内存才能验证装载位置——给头文件补一个只读访问器，并让测试真正校验 0x200 处的字节。测试目标缺 include 路径，补上：测试通过，但有一个编译警告，看一下并清掉：`stack_` 未使用是因为 `cycle()` 还是 TODO（栈要到里程碑 3 的 0x2NNN/0x00EE 才用上）。给它加一个只读访问器——里程碑 6 的调试器转储栈时正好要用：全绿：0 警告、测试通过、CLI 用法路径正确。写 PROGRESS.md 记录骨架完成：The reflection tool returned just an echo. Let me do the final verification myself: re-derive each required output from actual artifacts.

1. Milestone plan with runnable checks — in chip8/README.md (7 milestones table). ✓ (written, verified content when writing)
2. Minimal project skeleton — chip8/ with CMakeLists.txt, chip8.hpp, chip8.cpp, main.cpp, tests/test_chip8.cpp, .gitignore, README.md, PROGRESS.md. ✓
3. Build passes, ctest passes, 0 warnings, CLI usage path works. ✓ (verified via bash output)
4. Attribution to upstream tutorial — README.md has the link. ✓
5. cycle() left as TODO for learner — yes, chip8.cpp cycle() is a TODO with hints. ✓
6. PROGRESS.md records milestone 0. ✓

One thing to double check: the README says `./build/chip8 roms/xxx.ch8 --trace` prints first 16 bytes — main.cpp has a TODO for that (milestone 1 checkpoint). That's consistent with the plan (milestone 1 deliverable).

Also verify the final file listing to confirm everything is in place. Let me do a quick final listing to be thorough. Actually I've verified via build+test already. A quick ls for the final answer's directory tree would be good evidence.骨架就绪，构建与测试全绿。当前进度：里程碑 0/7 完成，下一步是里程碑 1（字体集 + `--trace`）。

**项目结构**（`chip8/`，零依赖，C++17 + CMake）：

```
chip8/
├── README.md        # 7 里程碑规划表（概念/交付物/检查命令）+ 教程署名
├── CMakeLists.txt   # chip8 主程序 + test_chip8 测试（CTest）
├── chip8.hpp        # 完整机器状态：4KB 内存、V0-VF、I、PC、栈、定时器、键、64×32 显示
├── chip8.cpp        # 构造 + load()（0x200 装载、大小校验）已实现；cycle() 留给你
├── main.cpp         # 入口 + 主循环节奏注释（每帧 N 条指令 + 60Hz 定时器）
├── tests/test_chip8.cpp  # 加载器断言（已通过）
└── PROGRESS.md      # 里程碑 0 已记录
```

**验证结果**：`ctest` 1/1 通过，0 编译警告，无 ROM 时打印用法并返回退出码 1。

**里程碑路线**（每步都有可运行检查，详见 `chip8/README.md`）：

1. 内存 + ROM 加载器 → 字体集写入 0x050、`--trace` 打印 ROM 头 16 字节
2. 取指–译码–执行 → 5 条指令（0x00E0/0x1NNN/0x3XNN/0x6XNN/0x7XNN）单元测试
3. 完整指令集 → corax89/chip8-test-suite 全 OK
4. 显示 → SDL2 渲染 IBM logo（本机 SDL2 2.32.10 已就绪）
5. 输入 + 定时器 → 游戏 ROM 可玩
6. 调试器 → `--step` 单步打印 PC/opcode/寄存器
7. 进阶（可选）→ Game Boy / NES

**里程碑 1 你要写的两处**（都标了 TODO）：

- `chip8.cpp:7` 构造函数：把 16 个字符 × 5 字节的字体集写入 `memory_[0x050..0x09F]`，`I_` 置 0x050。字体每行的位模式（如 `0xF0, 0x90, 0x90, 0x90, 0xF0` 是 "0"）在教程 "Fonts" 一节，建议自己推导 1-2 个再对照。
- `main.cpp:19`：打印 `chip8.mem(0x200)` 起的 16 字节，与 ROM 文件头用 `xxd` 比对。

检查命令：`ctest --test-dir build --output-on-failure`（给字体集加断言：`mem(0x050)==0xF0`、`mem(0x054)==0xF0`），以及 `./build/chip8 roms/xxx.ch8 --trace`。测试 ROM 可从 [tobiasvl/chip8-test-rom](https://github.com/tobiasvl/chip8-test-rom) 或 IBM logo ROM 获取（放入 `roms/`，已被 .gitignore 排除）。

教程原文：[How to write an emulator (CHIP-8 interpreter)](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/)。写完里程碑 1 后把代码贴给我，我帮你 review 并跑检查点。