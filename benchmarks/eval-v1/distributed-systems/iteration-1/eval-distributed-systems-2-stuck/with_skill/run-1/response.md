The user says: "My consumer re-reads old messages every time it restarts." This is a debugging question about message queue consumers (Kafka, RabbitMQ, etc.). There's no workspace context given. Let me check if there's a workspace with code to look at.

The user hasn't specified which technology. I should check the workspace for context first — maybe there's a project with consumer code. Let me glob/grep for consumer-related files.

Let me look at the workspace first.Your broker has no committed position for your consumer, so every restart looks like a brand-new consumer and it falls back to the "start from" default (earliest / queue head). The fix depends on which system you're using — the usual culprits:

**Kafka**
- `enable.auto.commit=false` but you never call `commitSync()`/`commitAsync()` after processing.
- `group.id` changes on every restart (generated randomly, or set per-instance) — a new group has no committed offset, so `auto.offset.reset` (often `earliest`) applies.
- Commits fail silently during rebalances; check the `CommitFailedException` path.

Confirm with `kafka-consumer-groups.sh --describe --group <gid>`: if `CURRENT-OFFSET` is `-` or far behind `LOG-END-OFFSET`, commits aren't landing.

**RabbitMQ**
- Manual ack mode (`autoAck=false`) but `basicAck()` is never reached — messages stay unacked and get requeued when the channel closes.
- `prefetch` unset/unbounded combined with acks only at the end of a batch.

Check the queue in the management UI: a large *Unacked* count that drops back to *Ready* when your consumer stops is the signature.

**Redis Streams**
- Reading with `XREAD` from `0` instead of using a consumer group (`XGROUP CREATE` + `XREADGROUP` + `XACK`), so there's no persistent read position.

**SQS**
- Visibility timeout shorter than processing time — the message becomes visible again after restart/timeout; delete after processing or extend the visibility timeout.

**RocketMQ**
- `CONSUME_FROM_FIRST_OFFSET` combined with a changing consumer group, or consumption throwing before offsets are persisted.

The two cross-cutting checks: is the offset/ack actually being persisted after successful processing, and is your consumer identity (group id / queue name) stable across restarts? Tell me which broker and I'll point at the exact config lines.