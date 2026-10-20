The user is describing a classic blockchain learning project bug: tampering with block 1's data doesn't invalidate the chain because they only compare each block's `prev_hash` to the previous block's stored `hash` field, without recomputing the hash from the block's contents.

This matches the build-your-own-x skill trigger: "my own git's hash differs from real git", "my ray tracer has shadow acne", "my CHIP-8 draws garbage", "my toy kernel triple-faults" — stuck/debugging midway through their own from-scratch implementation. A blockchain is in the build-your-own-x list ("blockchain"). So I should read the skill's SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it.The topic maps to `blockchain-cryptocurrency`. Reading the track skill now, as required.The track skill doesn't exist at that path. Let me check what skills exist.The glob output was truncated. Let me search specifically for the blockchain track skill.The track skill exists. Reading it.The file is truncated. Let me read the rest.Track skill read. The user is at milestone 2 (chain + validation), and their checkpoint "tampering with block 1 makes validation fail" is failing. Let me check if their project is in the workspace so I can point at the exact spot.Those are all skill files. Let me look for the user's actual project files outside `.agents`.**Where we are:** milestone 2/7 — chain + validation. Your checkpoint ("tampering with block 1 makes validation fail") is currently failing.

**The bug:** `prev_hash == previous.hash` only verifies the links between blocks. The `hash` field stored inside each block is itself just data — editing block 1's `data` leaves its stored `hash` untouched, so every link still matches and validation passes. The stored hash and the block's actual contents have drifted apart, and your validator never looks at the contents.

**The fix (minimal):** validation must recompute each block's hash from its own fields and compare it against the stored `hash`, in addition to the link check:

```python
def is_valid_chain(chain):
    for i, block in enumerate(chain):
        # 1. recompute from the block's contents
        if calculate_hash(block) != block.hash:
            return False
        # 2. link to the previous block
        if i > 0 and block.prev_hash != chain[i - 1].hash:
            return False
    return True
```

`calculate_hash` is the same function you used when creating blocks in milestone 1 — reuse it, and make sure it serializes the exact same fields in the same order (index, timestamp, data, prev_hash, nonce if you have one). A field-order mismatch makes every block look invalid. The genesis block gets check 1 too; optionally assert its `prev_hash` equals your `"0"` sentinel.

**Why this catches the tamper:** editing block 1's data changes what `calculate_hash(block)` returns, so check 1 fails at `i == 1` immediately. The stored `hash` field is attacker-visible data; recomputation is what binds it to the contents.

Worth knowing for the next milestone: a tamperer can also recompute the stored hash after editing. Milestone 3 (proof of work) closes that — re-mining every block becomes expensive.

**How to check it:** save this in your project as `scratch/tamper_test.py` (adjust the import to your module/class names) and run `python scratch/tamper_test.py`:

```python
from blockchain import Blockchain

bc = Blockchain()
bc.add_block("alice pays bob 5")
assert bc.is_valid_chain(bc.chain), "fresh chain must be valid"

bc.chain[1].data = "alice pays eve 500"  # tamper
assert not bc.is_valid_chain(bc.chain), "tampered chain must fail"
print("OK: tamper detected")
```

Expected output: `OK: tamper detected`. If the first assert fires instead, your validation-time `calculate_hash` disagrees with the one used at block creation — compare the field lists.