The user has a blockchain project where tampering with block 1's data doesn't invalidate the chain. They only check `prev_hash == previous_block.hash`. The classic bug: they never recompute the hash from the block's contents, so editing data doesn't change the stored `hash` field, and validation passes. The fix: recompute each block's hash from its actual contents (data + prev_hash + timestamp + nonce etc.) and compare against the stored hash, plus verify prev_hash linkage and proof-of-work if applicable.

Let me look at the workspace to find the actual code. The cwd is `build-your-own-x-blockchain-cryptocurrency-2`. Let me explore.Empty workspace? Let me check with bash ls.The workspace is empty, so I'll explain the bug directly — it's a classic one.

## Why tampering passes validation

Your stored `hash` field is just data written once at block creation. Editing block 1's data changes the data but leaves the stored `hash` untouched, so block 2's `prev_hash` still matches it. Your check verifies the *links* between stored hashes, never that each hash actually corresponds to its block's contents.

## Fix: recompute, then compare

Validation must re-derive each block's hash from its actual contents and compare against the stored value:

```python
def is_chain_valid(chain):
    for i, block in enumerate(chain):
        # 1. Recompute hash from the block's real contents
        block_data = f"{block.index}{block.timestamp}{block.data}{block.prev_hash}{block.nonce}"
        if block.hash != sha256(block_data.encode()).hexdigest():
            return False  # contents were tampered with

        # 2. Check linkage
        if i > 0 and block.prev_hash != chain[i - 1].hash:
            return False

        # 3. If you have proof-of-work, verify it too
        if not block.hash.startswith("0" * DIFFICULTY):
            return False
    return True
```

Now editing block 1's data makes the recomputed hash differ from the stored one → invalid. And because block 2's `prev_hash` references block 1's hash, you'd also need to re-mine every subsequent block to forge the chain — that's the tamper-evidence property.

Two things to check in your code:

1. **Hash computation must be identical in mining and validation** — same field order, same serialization. A mismatch there causes false "invalid" results, the opposite bug.
2. **The genesis block** — validate it with the same recompute check (it just has no `prev_hash` linkage check).

If you drop your actual block/validation code in here, I'll point at the exact lines to change.