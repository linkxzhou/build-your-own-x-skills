The user reports a bug: their consumer re-reads old messages every time it restarts. This is a classic offset management / commit issue. But I don't know their codebase. Let me look at the workspace to find the consumer code.

The workspace is "build-your-own-x-distributed-systems-2" — likely a project building a distributed system (maybe a message queue like Kafka). Let me explore.Your workspace is empty, so I can't inspect the code — here's the diagnosis path for the usual suspects, then tell me your stack (Kafka, RabbitMQ, custom queue?) and share the consumer config/code.

**Kafka — most likely causes, in order:**

1. **`group.id` changes on every restart** (e.g., generated with a random suffix or timestamp). A new group has no committed offset, so `auto.offset.reset=earliest` kicks in and you replay everything. Fix: use a stable group id.
2. **Offsets never committed.** `enable.auto.commit=true` commits on the poll loop, but if your consumer exits before the interval elapses (or you call `consumer.close()` without letting the loop run), nothing is persisted. Fix: commit manually after processing — `commitSync()` per batch, or `commitAsync()` with a final `commitSync()` on shutdown.
3. **Commit happens before processing completes.** If you commit on poll and crash mid-processing, you get the opposite problem (message loss) — but if you commit only after a full batch and your batches are huge, restarts replay a lot. Tune batch size / commit cadence.
4. **`auto.offset.reset=earliest`** — this only matters when no committed offset exists for the group/partition. If you're seeing replay, it's almost always #1 or #2 making that fallback trigger.

**Quick check:** run `kafka-consumer-groups.sh --describe --group <your-group>` before and after a restart. If the group doesn't exist after restart → cause #1. If it exists but the OFFSET column lags behind LOG-END-OFFSET by the whole history → cause #2.

**RabbitMQ:** messages are redelivered whenever the channel/queue isn't acked — check that `basicAck` fires after processing and that you're using a durable queue with persistent messages if you expect them to survive broker restarts.

**Custom queue (given the repo name):** if offsets live in consumer memory, restart = replay by definition. Persist the committed offset (fsync'd file or the broker itself) before or after each processed message, and load it on startup.

Paste the consumer setup (group id, commit config, poll loop) and I'll point at the exact line.