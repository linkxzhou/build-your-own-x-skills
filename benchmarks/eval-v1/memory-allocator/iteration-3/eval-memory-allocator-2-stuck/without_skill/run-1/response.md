The user has a memory allocator issue: heap keeps growing after many malloc/free calls. This is a "build-your-own-x memory allocator" project based on the workspace path. I should explore the workspace to find the allocator code and diagnose why free'd memory isn't being reused.

Let me start by looking at the files in the workspace.The workspace is empty. Let me check with bash to see hidden files.The workspace is empty — I can't see your allocator source. Drop the `.c`/`.h` files here (or paste them) and I'll pinpoint the bug. Meanwhile, "works small, grows under churn" almost always means freed blocks are never reused. Check these in order:

1. **malloc never searches the free list** — it bumps `sbrk` unconditionally. Verify `malloc` walks the free list (or implicit heap) for a fit *before* extending the heap.

2. **No coalescing** — adjacent free blocks are never merged. Symptom: total free bytes exceed the request, but no single block is big enough, so the heap grows anyway (external fragmentation). This is the classic cause under many alloc/free cycles with varying sizes. Merge on `free` with the next block (and previous, if you have footers/boundary tags).

3. **Split remainder is lost** — when a free block is reused and split, the leftover tail must be pushed back on the free list with a correct header. If it's dropped, free space silently evaporates.

4. **Size accounting bug** — header/footer size confusion: a block of payload `N` gets recorded as `N - header_size`, so a later request of `N` never fits and the heap grows. Check that the size stored in the header is the *block* size (header included) consistently in `malloc`, `free`, and split/coalesce logic.

5. **Free list corruption** — double free, or a payload write stomping the next block's header, silently removes blocks from the free list.

Quick diagnostic: instrument `malloc`/`free` to log heap size (`sbrk` total), free-list byte total, and largest free block. If free bytes ≥ request but `sbrk` is still called → coalescing/fit bug. If the free list is empty right after frees → `free` isn't inserting blocks or `malloc` isn't searching it.