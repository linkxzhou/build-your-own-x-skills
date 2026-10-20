The user has a CHIP-8 emulator issue: when running the IBM logo ROM, they get garbled pixels instead of the expected IBM logo. They mention they use direct assignment for pixels in the DXYN draw instruction.

This is a classic CHIP-8 bug: DXYN should XOR sprites onto the display, not assign them. Direct assignment (OR or SET) breaks sprite drawing — the IBM logo test ROM specifically relies on XOR behavior and collision detection (VF flag).

Let me look at the workspace to see if there's actual code to inspect. The cwd is /Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-emulator-virtual-machine-2 — this looks like a clone of the "build your own x" list repo, but maybe the user's emulator code is in there. Let me check.

I should explore the workspace first to find their emulator code. Let me glob for source files.工作区里没有你的模拟器源码，直接说结论：DXYN 必须用 XOR（异或）写像素，直接赋值会破坏精灵绘制，这正是 IBM logo 花屏的典型原因。

## 为什么赋值会花屏

IBM logo ROM 依赖 XOR 的"二次绘制即擦除"特性：它先画出 logo，再在偏移 1 像素的位置重画同一精灵，把重叠部分翻转掉，形成镂空效果。用赋值（`= 1` 或 `|= 1`）时，重叠区域只会被再次置 1，永远擦不掉，最终糊成一团乱码。

## 正确的 DXYN 语义

```
0xDXYN: 从 I 指向的地址读 N 字节，画在 (VX, VY)，宽固定 8 像素
```

C 风格参考实现：

```c
void op_DXYN(Chip8 *c) {
    uint8_t x = c->V[(c->opcode & 0x0F00) >> 8] % 64;   // 起点坐标回绕
    uint8_t y = c->V[(c->opcode & 0x00F0) >> 4] % 32;
    uint8_t n = c->opcode & 0x000F;

    c->V[0xF] = 0;                                       // 先清零，整个精灵期间只置一次
    for (int row = 0; row < n; row++) {
        uint8_t sprite = c->memory[c->I + row];          // 每行 1 字节，MSB 在左
        for (int col = 0; col < 8; col++) {
            if ((sprite & (0x80 >> col)) == 0) continue; // 为 0 的位不碰屏幕
            int px = (x + col) % 64;
            int py = (y + row) % 32;
            if (c->display[py][px]) c->V[0xF] = 1;       // 撞击检测：原像素为 1
            c->display[py][px] ^= 1;                     // 关键：异或
        }
    }
}
```

容易一起踩的坑，逐条核对：

1. **VF 初始化**：进入指令时置 0，绘制中任一像素发生翻转 1→0 才置 1。别在每个像素里重置 VF，也别用赋值逻辑推 VF。
2. **坐标回绕**：起点 `(VX % 64, VY % 32)`，绘制中越界也回绕（COSMAC VIP 行为）。另一种流派是越界裁剪直接跳过该像素，两种都能跑 IBM logo，但回绕更接近原机。
3. **位序**：`0x80 >> col`，最高位对应最左像素。位序反了同样花屏。
4. **sprite 位为 0 时跳过**：只对 1 的位做 XOR，0 的位必须保持屏幕原样。
5. **VX 不自增**：现代解释器（TIA/CHIP-8 文档惯例）绘制后 VX 保持不变。

改完 XOR 后 IBM logo 应该显示为清晰的镂空 "IBM" 字样。如果还有问题，下一步检查取指解码（`n = opcode & 0xF`）和 I 寄存器是否指向了正确的精灵数据。