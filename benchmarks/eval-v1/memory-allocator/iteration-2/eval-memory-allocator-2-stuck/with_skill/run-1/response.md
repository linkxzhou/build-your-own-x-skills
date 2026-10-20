The user is working on a malloc implementation (build-your-own-x territory — "my own malloc" debugging). The skill instructions say: when someone is stuck/debugging midway through their own from-scratch implementation (e.g. malloc), I should read the build-your-own-x SKILL.md first BEFORE doing anything else.

Let me read the skill file first.The file was truncated. Let me read the rest of the SKILL.md, and also look for the malloc track skill. The topic is malloc — likely under a "malloc" or "memory allocators" slug. Let me check the skills directory.The track skill is `memory-allocator`. Reading it now.Truncated again. Let me read the rest of the file.The track skill is loaded. This is a debugging turn — let me check the workspace for the allocator code first.No code in the workspace, so I'll coach from the symptom. Let me grab the upstream tutorial links for reference.**Where we are:** milestone 3/7 (splitting + coalescing). "Small tests pass, heap grows under churn" is the exact signature of the milestone-3 checkpoint failing.

**The concept:** `free()` only flips a flag. Two adjacent free blocks stay separate until free() merges them. Under churn the heap fills with holes smaller than any incoming request, so malloc calls `sbrk` again even though total free space is enough — no single hole fits. The upstream tutorial covers this in its coalescing section: [Malloc is not magic](https://medium.com/p/e0354e914402).

**Confirm which bug you have (2-minute differential).** Add a counter to your sbrk wrapper, then run two loops:

```c
/* A: same-size churn — heap must stay flat */
for (int i = 0; i < 1000; i++) { free(my_malloc(64)); }

/* B: merge test — c must land at a's address */
void *a = my_malloc(100), *b = my_malloc(100);
free(a); free(b);
void *c = my_malloc(200);
```

- A grows → malloc never finds freed blocks. Check free(): it must leave the block in the free list (set the flag, keep the links) and malloc's fit test must accept `size <= hole->size`.
- A flat, B calls sbrk → coalescing is missing. This is the likely one.

**The minimal fix (in `free()`):** after marking the block free, look at the next physical block and absorb it:

```c
header *next = (header *)((char *)blk + sizeof(header) + blk->size);
if ((char *)next < heap_top && next->free) {
    blk->size += sizeof(header) + next->size;
    /* unlink next from the free list */
}
```

Merging the previous neighbour needs a walk from the heap start (fine at this stage) or a prev pointer in the header — do the next-merge first; it alone fixes pattern B. One more spot to check: if malloc() splits blocks, the remainder must be written back as a well-formed free block in the list; a bad split produces the same symptom.

**How to check it:**

```
cc -o churn churn.c mymalloc.c && ./churn
```

Expected output:

```
A: sbrk calls = 1, heap top constant
B: c == a, sbrk calls = 1
```

Then rerun your original workload — the sbrk counter should plateau once the working set stabilizes. Drop `mymalloc.c` into the workspace and I'll point at the exact line.