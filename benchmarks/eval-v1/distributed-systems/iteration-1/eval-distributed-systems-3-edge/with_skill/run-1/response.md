The user is building their own Raft-replicated key-value store and asks whether they can test replication and leader failover on one laptop. This matches the build-your-own-x skill — specifically "build your own Redis/databases" or distributed systems. The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it.

Let me read the skill first.The SKILL.md was truncated. Let me read the rest of it, and also find the relevant track skill. The topic is "Raft-replicated key-value store" — this maps to a category. Let me see the category map. The truncated part likely contains the table. Let me read more of the file and also list the skills directory.Raft-replicated KV store maps to the `distributed-systems` track. Reading the track skill now — it's mandatory per the router.The track skill is about Kafka-like distributed systems, but the user is building a Raft-replicated KV store. The track skill mentions milestone 7 stretch: consensus — Raft. The user's question is specific: "Can I test replication and leader failover on one laptop?" This is a practical question about testing methodology.

Let me read the rest of the track skill (truncated part) and check the tutorials reference. Also check if there's a per-tutorial skill for Raft specifically.No dedicated Raft per-tutorial skill exists, so the `distributed-systems` track governs. Let me check the upstream tutorial list for Raft-specific guides to credit.The track's upstream list only covers the Kafka guide; for Raft itself the canonical reference is the Raft paper. Before answering, let me check whether there's existing project code in the workspace so the advice matches what's actually there.Yes — one laptop is exactly how consensus systems get tested. etcd, hashicorp/raft, and TigerBeetle all run their Raft tests as multiple nodes on one machine in CI. A 3-node cluster is 3 processes on `127.0.0.1:7001-7003`, each with its own data dir. This maps to milestones 5–6 of the distributed-systems track (replication, then failure testing).

**Basic failover test (no special tooling):**

1. Write keys through the leader, note every acked response.
2. `kill -9` the leader — SIGKILL, deliberately. SIGTERM lets your graceful-shutdown path run and masks real crash bugs.
3. Wait for the election, confirm a new leader exists.
4. Verify: every acked write is readable from the new leader, and the restarted old leader truncates any uncommitted tail entries from its log.

**The one thing localhost makes awkward: partitions** (node alive but cut off — the case that exercises Raft's term/leader-completeness rules hardest). Three options, best first:

- **In-process fault hooks.** Put a `Network` interface in front of your RPC layer; in test mode it drops, delays, or duplicates messages between chosen node pairs. No root access, fully scriptable, works in any language. This is the right default for automated tests.
- **TCP proxy per link** (Toxiproxy, or ~50 lines of your own). Nodes talk through proxies you can pause mid-test. Good for exercising your real socket code as a black box.
- **OS firewall** (`iptables`/`pfctl` per port). Most realistic, needs root, painful to automate. Skip it.

**The upgrade worth building later: deterministic simulation.** Run all 3 nodes as goroutines/threads inside one process with a mocked clock, the mocked network from above, and a seeded RNG — then loop thousands of random kill/restart/partition schedules per second, checking after each that the state machine history is identical on all nodes. FoundationDB and TigerBeetle credit this technique with finding nearly all of their consensus bugs; manual kill tests miss the weird interleavings. Build your basic failover test first, this second.

Two practical notes: shrink election timeouts in tests (e.g. 50–150 ms) so failover scenarios finish in about a second, and know the limits — a laptop can't reproduce real clock skew or cross-machine latency, but the logic bugs you're hunting (split votes, lost acks, stale leaders serving reads) all reproduce locally.

Reference for the test design: Jepsen's etcd analysis (jepsen.io) is the model — kill the leader mid-replication, then check that no acknowledged write was lost. Canonical spec: the Raft paper at raft.github.io.

Which language is the store in? That decides whether the fault hooks live in your RPC client, a middleware trait, or a proxy process.