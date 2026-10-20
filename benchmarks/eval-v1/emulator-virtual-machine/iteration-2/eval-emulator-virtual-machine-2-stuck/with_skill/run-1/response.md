The user is speaking Chinese. They have a CHIP-8 emulator, and when running the IBM logo ROM, they get garbled pixels. They mention the DXYN draw instruction uses direct pixel assignment (直接赋值像素) instead of XOR.

This matches the build-your-own-x skill trigger: "my CHIP-8 draws garbage" — explicitly listed in the skill description. I must read the SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of the SKILL.md.CHIP-8 映射到 `emulator-virtual-machine` track。按流程先读 track skill。The track skill file doesn't exist at that path. Let me check what's in the skills directory.The skills directory only contains `build-your-own-x`. There's no `emulator-virtual-machine` track skill. Let me check the references/catalog.md mentioned in the SKILL.md, and the x-skills-manifest.json.Track skills 在 `.agents/skills/build-your-own-x/skills/` 下。查找 emulator track skill。The file is truncated. Let me read the rest.Track skill 已读。这是调试回合（Milestone 4: Display）。先看工作区里有没有你的模拟器代码，好给出精确的最小修复。工作区里没有你的代码，所以按你自己的诊断来：DXYN 用直接赋值，这正是 IBM logo 花屏的原因。

**进度：** Milestone 4/7（Display）调试。

**概念（为什么恰好是 IBM logo 坏掉）：** CHIP-8 的 sprite 是 XOR 绘制：sprite 位为 1 时翻转屏幕像素，为 0 时保持不变。IBM logo ROM 的画法是先画实心块，再用 XOR 重画同一区域把横向条纹“擦”出来。直接赋值（`display[y][x] = 1`）只会把像素点亮，永远擦不掉，于是条纹全部糊死，看起来就是乱码色块。

**最小修复（只改 DXYN 的内层循环）：**

```c
// DXYN: VF 清零后
for (int row = 0; row < n; row++) {
    uint8_t bits = memory[I + row];
    for (int col = 0; col < 8; col++) {
        if (bits & (0x80 >> col)) {
            int x = (vx + col) % 64;
            int y = (vy + row) % 32;
            if (display[y][x]) vf = 1;   // 撞检：1 被翻成 0
            display[y][x] ^= 1;          // 关键：XOR，不是赋值
        }
    }
}
```

注意 `^= 1` 要在撞检判断之后做，顺序反了 VF 会永远为 0。

**验证：** 重新跑 IBM logo ROM：

```
./your_emulator roms/ibm-logo.ch8
```

预期输出：清晰的 "IBM" 三个字母，每个字母中间有横向空隙（条纹）。如果修完 XOR 后字母边缘仍有毛刺，再回来，下一个怀疑点是坐标越界时该裁剪还是回绕。