The user says: "In my single-cycle RISC-V core, after writing to x0 register, reading it back doesn't give 0."

This is a debugging task for a hardware design (likely Verilog/SystemVerilog). I should look at their workspace to find the register file implementation. Let me explore the workspace first.

The user's task matches... hmm, the skill "build-your-own-x" — it's about learning by rebuilding real software. The user already has a single-cycle RISC-V core and is debugging it. This is a debugging task, not a "help me pick a project" task. The skill says "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills..." — the user is already building one and hit a bug. I think the skill is more for picking/starting projects and coaching. This is a concrete bug fix. I'll skip the skill since it doesn't match — actually, let me reconsider. The skill description says it "hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution." The user is mid-project with a bug. The trigger includes "从零实现、自己动手写一个 X..." — they're building a RISC-V core. But the request is a specific bug: x0 reads non-zero. I think debugging help is fine without loading the skill; the skill is for choosing/starting projects. I'll proceed with debugging directly.

Per the developer instructions: before modifying code, call `explore` once to record files read. First I need to find the register file. Let me glob for verilog files and grep for x0 handling.

Let me start by looking at the workspace.工作区里没有找到你的代码（没有 `.v`/`.sv` 文件），所以我先按最常见的原因给结论，你可以对照检查；如果对不上，把寄存器堆模块贴出来我帮你看。

这个症状几乎总是同一个问题：寄存器堆没有把 x0 硬连到 0。写回时 `regs[0]` 被真实写入了数据，读出时又直接索引 `regs[rs]`，于是 x0 的值就是上次写进去的垃圾值。典型写法：

```verilog
// 有 bug 的写法
always @(posedge clk) begin
    if (we)
        regs[rd] <= wdata;   // rd==0 时也会写
end
assign rdata = regs[rs];     // rs==0 时读出的是被污染的 regs[0]
```

标准修法是两道保险都加上：

```verilog
// 1. 写端口屏蔽 x0
always @(posedge clk) begin
    if (we && rd != 5'd0)
        regs[rd] <= wdata;
end

// 2. 读端口硬连 0
assign rdata_a = (rs_a == 5'd0) ? 32'b0 : regs[rs_a];
assign rdata_b = (rs_b == 5'd0) ? 32'b0 : regs[rs_b];
```

只做第 1 条通常也能过功能测试，但两条都做更稳：读端 mux 保证无论谁污染了 `regs[0]`（包括你以后加的调试逻辑、复位遗漏），架构上 x0 永远读 0；写端屏蔽则避免综合出无用的存储单元。

如果检查后你的寄存器堆已经有这两处，那问题在别处，按这个顺序排查：

1. **写回数据源**：确认 `rd` 信号本身没错——比如 JAL/JALR 译码时 rd 字段取错位，把本该写 x1 的写到了 x0。
2. **读出的位置**：确认你观察的是寄存器堆输出，而不是 forwarding/写回级之后的信号（单周期一般没有，但如果你加了旁路就要查）。
3. **复位**：`regs` 没初始化时 `regs[0]` 是 X，仿真里会显示成非 0 值——加上面的读端 mux 后这个也会消失。

把你的 regfile 和写回那段代码贴上来，我可以直接指出具体行。