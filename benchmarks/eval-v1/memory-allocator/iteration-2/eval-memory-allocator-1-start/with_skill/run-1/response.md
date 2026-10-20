The user wants to implement malloc/free in C from scratch. This matches the build-your-own-x skill. I should read the skill file first.The file was truncated. Let me read the rest of it.malloc 映射到 `memory-allocator` track。读取该 track skill。Skills 嵌套在 `build-your-own-x/skills/` 下。查找 memory-allocator track。C 语言对应上游教程 "Malloc is not magic"。读取该教程的 per-tutorial skill。Track 和教程 skill 已读完。检查工作区状态和工具链。环境就绪：macOS + Apple clang + make，工作区为空。按 track skill 记录探索与计划，然后搭好项目骨架。先验证这台 macOS 上 `sbrk` 的行为（弃用警告级别、是否可用），避免骨架踩坑。`sbrk` 在这台 macOS 上可用（仅弃用警告，行为正确）。搭好项目骨架。`rm` 被沙箱拦截，但其他命令可用。先跑构建验证，scratch 目录稍后手动清理。骨架就绪，checkpoint 如预期失败（`my_malloc` 返回 NULL）。现在轮到你写代码。

## 里程碑 1/7：bump allocator

**概念**：进程的堆是一段可增长的内存，`sbrk(increment)` 把“程序断点”（break）向前推，返回新内存的起点。最朴素的分配器只做一件事：每次调用 `sbrk` 要一块新内存，切一块给调用者，指针只进不退——这就是 bump allocator。`free` 此时无事可做（内存还不回收），但两个约束必须满足：返回的指针按 16 字节对齐（macOS ABI 要求），且块之间绝不重叠。

**你要写的**：`mymalloc/mymalloc.c` 里的 4 个 TODO，总共约 10 行：

1. `sbrk(0)` 拿当前 break（它返回 `void*`，可以直接当地址用）
2. 算 padding，让 `break + padding` 对齐到 16：`(x + 15) & ~15` 是向上取整到 16 的惯用法
3. 先 `sbrk(padding)` 再 `sbrk(size)`——两次调用，第一次的返回值就是你要交出去的指针；`sbrk` 失败返回 `(void*)-1`，要检查
4. 返回那个对齐好的指针

**检查**：

```
cd mymalloc && make test
```

预期输出：`PASS: 1000 allocations, all 16-byte aligned, data intact`

两个提示备用（卡住再说，一次一个）：测试里 `memset` 写满每个块、再抽查内容，就是在验证“块不重叠”；如果 `make test` 报对齐失败，先打印你算出的 padding 看看。

另外：`scratch/` 里是我探测 `sbrk` 用的临时文件，可以 `rm -rf scratch` 删掉（我的沙箱拦了 `rm`，你本地没问题）。教程原文在 [Malloc is not magic](https://medium.com/p/e0354e914402)，本里程碑对应它的开头部分。写完跑一下，把输出贴给我。