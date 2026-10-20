The user is working on a malloc implementation (build-your-own-x context — "my own malloc" style debugging). The skill says: use the build-your-own-x skill whenever someone is stuck/debugging midway through their own from-scratch implementation (e.g. "my malloc..."). The trigger mentions "my own malloc" explicitly. So I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of the SKILL.md, and also look for the malloc track skill. The topic is malloc — category slug likely "malloc" or "allocator". Let me check the skills directory.The topic maps to the `memory-allocator` track. Reading the track skill now — it's mandatory before coaching.Truncated again. Let me read the rest of the file.The track skill is loaded. This is a debugging turn — the symptom (heap grows despite frees) points at milestone 3 territory (reuse/coalescing). Let me check the workspace for the learner's code.**Where we are:** milestone 3/7 territory (reuse + coalescing). "Works for small tests, heap grows under churn" is the classic signature of freed blocks never being reused.

The three usual causes, ranked:

1. **malloc never searches the free list** — every call falls through to `sbrk`. `free` marks the block, `malloc` ignores it.
2. **No coalescing** — adjacent free blocks stay separate, so any request larger than a single hole forces heap growth. Small tests pass because each request fits one hole; churn kills it.
3. **No splitting** — a freed 1 KB block can't serve a 100 B request, so small allocations always extend the heap.

This 20-line test tells them apart — drop it next to your allocator:

```c
#include <stdio.h>
#include <stddef.h>
extern void *my_malloc(size_t n);
extern void my_free(void *p);

int main(void) {
    for (int i = 0; i < 5; i++) {           /* Test A: same-size churn */
        void *p = my_malloc(100);
        printf("A%d %p\n", i, p);
        my_free(p);
    }
    void *b[10];                             /* Test B: fragmentation */
    for (int i = 0; i < 10; i++) b[i] = my_malloc(100);
    for (int i = 0; i < 10; i += 2) my_free(b[i]);
    printf("big %p\n", my_malloc(500));      /* 5 holes of 100B exist */
    return 0;
}
```

Reading the output:

- **A0–A4 all the same address** → reuse works; your growth comes from coalescing or splitting (causes 2–3).
- **A0–A4 strictly increasing** → cause 1: check that `free()` actually inserts the block into your free list, and that `malloc()`'s search runs *before* the `sbrk` fallback.
- **`big` lands above every earlier address** while 500 B of holes exist → coalescing is missing; you need to merge with the next block when it's also free (usually done while walking the list in `free`, or by address-ordered insertion + a merge pass).

If the output doesn't settle it, paste your `malloc` and `free` — the bug is almost always in one of three places: the free-list insert in `free()`, the search loop in `malloc()`, or the split/merge step.

**Checkpoint:**

```
gcc -o heap_test heap_test.c my_malloc.c && ./heap_test
```

Pass looks like: `A0`–`A4` print the identical address, and `big` prints an address inside the range of the earlier allocations.