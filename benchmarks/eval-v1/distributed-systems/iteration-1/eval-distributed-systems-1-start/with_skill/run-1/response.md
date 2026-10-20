The user is asking in Chinese: "I want to implement a Kafka-like distributed log myself, in Go, what's the first step?"

This matches the build-your-own-x skill — "build your own Kafka / distributed log" is a category in codecrafters-io/build-your-own-x. The skill description says: use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project... Chinese triggers include 从零实现、自己动手写一个 X、造轮子学原理.

So I must read the skill's SKILL.md first before doing anything else.The file was truncated. I need to read more of it, particularly the category map to find the right slug for a Kafka-like distributed log. Let me read the rest of the file.Kafka/distributed log 映射到 `distributed-systems` track。现在正在读取 track skill（根据 skill workflow，这是必需的）。The file was truncated. Let me read the rest of the file (lines 47+).现在让我检查一下教程参考，为 Go 找到合适的上游指南。只有一个上游教程，而且是 Java 的。我来检查一下每个教程的 skills 和 catalog，看看有没有 Go 相关的选项。上游指南是 Java 的；track skill 明确允许将 Go 作为替代方案，并沿用相同的里程碑。让我快速检查一下 per-tutorial skill 以了解里程碑细节，并查看 workspace 环境（Go toolchain，现有代码）。Environment: Go 1.26.1 on macOS arm64, empty workspace (only .agents and AGENTS.md). The learner wants Go, Kafka-like distributed log.

Per the track skill workflow:
1. Agree on scope: language (Go — given), target, milestone list, checks. Ask at most 2 questions, suggest defaults.
2. Pick a guide: the only upstream one is Java (https://github.com/buildthingsuseful/build-your-own-kafka). Track skill says Go is a good alternative; milestones table is language-agnostic. I should credit the upstream tutorial with its exact link.
3. Start milestone 1 in the learner's workspace.

The user asked "第一步做什么?" (what's the first step?). Per the coaching rules:
- Don't dump a full solution. Give skeleton/interface for milestone 1, let the learner write the core.
- Output format per turn: Where we are (milestone N/total), the concept (short), what to write next (skeleton/TODO, not full answer), how to check it (command + expected output), stuck? one hint at a time.

The skill says "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care." The language is already given (Go). I could ask about scope (e.g., TCP vs HTTP for milestone 2, whether they want to follow the Java tutorial's structure), but the user asked a direct question: what's the first step. I should answer with milestone 1 and its concrete first step, maybe with one scope question at most. Actually the skill says ask at most 2 questions and suggest defaults. I can propose the default scope and start milestone 1, asking one question only if needed. Better: state the default scope (Go, single-node log first, TCP binary protocol later, local processes on ports), give milestone 1 concept + skeleton + checkpoint, and let them write the core.

Should I create files in the workspace? The skill says "start milestone 1 in the learner's workspace" and "Stay in the workspace". The teaching loop: explain concept, show interface/skeleton, let learner write core. I can scaffold: create the project skeleton (go.mod, a log.go with TODOs, a test file for the checkpoint). That's scaffolding, which the skill encourages ("you scaffold, review and test it"). But "Do not dump a full solution. Give complete code only for the current milestone, and only when asked, or after the learner has tried." A skeleton with TODOs is fine.

The user asked "第一步做什么" — a question. The best response: answer directly with the first step (milestone 1: append-only log), explain the concept briefly, give the skeleton, define the checkpoint. I can scaffold the workspace with a skeleton + test so they can start immediately. That matches "start milestone 1 in the learner's workspace."

Let me think about what milestone 1 involves:
- Append-only log: segments, offsets, index file.
- Checkpoint: append 10k messages, then read offset 5000 and get the right payload.

Design for Go:
- `Log` struct: dir, segments list, active segment.
- `Segment`: baseOffset, data file (.log), index file (.index) mapping offset → file position.
- Append(msg []byte) (offset uint64, err error): append to active segment, roll when size exceeds threshold.
- Read(offset uint64) ([]byte, error): use index to find position, scan to the record.
- Record format: length + payload (maybe CRC later). Keep it simple: 8-byte offset? Actually offset can be derived from base offset + position; simplest: each record = 4-byte length + payload; offset = baseOffset + recordIndex. Or store offset explicitly (8 bytes) — simpler to reason about, and matches Kafka's on-disk format loosely. For a first milestone, simplest robust choice: record = [4-byte length][payload], offsets implicit by counting within segment; index maps logical offset → physical position.

Keep the skeleton minimal: define the interface and TODOs, let the learner implement Append/Read. Provide a test file `log_test.go` that appends 10k messages and reads offset 5000.

Per the skill, I should give the skeleton (interface/skeleton), not the full implementation. I'll create:
- `go.mod` (module name, e.g., `minilog`)
- `log.go` with type definitions and TODO comments
- `log_test.go` with the checkpoint test

Wait — should I write the test file? Yes, scaffolding includes the runnable check. The learner writes the core (log.go implementation).

Also per skill: record progress in PROGRESS.md when a milestone passes — that comes later.

Scope agreement: The skill says agree on scope, ask at most 2 questions with defaults. I'll state the default scope and one question max. Actually, I can just propose the scope and start; the user can redirect. The user's question is "what's the first step" — answer it concretely. I'll note the upstream tutorial is Java and we're porting the roadmap to Go, crediting the link.

Should I use plan/todo tools? The developer instructions say for multi-step changes call plan. But this is a coaching conversation, and the skill defines its own workflow. Creating skeleton files is a small change (3 files). The skill's workflow takes precedence for coaching style. I think a lightweight approach: create the scaffold files, present milestone 1. I could use todo_write to track milestones across the session — that seems genuinely useful for a multi-milestone project. Let me create a todo list with the milestones (7 items, milestone 1 in progress). That aligns with "Use todo_write to track progress while executing the plan."

Hmm, but the todo list is session-scoped. Milestones span sessions. Still, it helps. I'll keep it simple: seed todos with the 7 milestones.

Actually, let me not over-engineer. The core deliverable this turn: answer "第一步做什么" with milestone 1, scaffold the workspace, give the checkpoint. I'll use todo_write with the milestone list since this is a multi-step project.

Let me design the skeleton carefully.

go.mod:
```
module minilog

go 1.26
```

log.go — skeleton with TODOs:

```go
// Package minilog is an append-only, segmented, offset-addressed log —
// the storage core of a Kafka-like broker.
package minilog

import (
	"encoding/binary"
	"errors"
	"fmt"
	"hash/crc32"
	"os"
	"path/filepath"
	"sort"
	"strings"
	"sync"
)

// Segment = one .log file + one .index file.
// Record layout in the .log file (little-endian):
//   [4B length][4B crc32][payload]
// Offsets are implicit: the first record in a segment with baseOffset B is B,
// the next B+1, and so on.
// .index file layout: repeated [8B offset][8B physical position in .log].
type Segment struct {
	baseOffset uint64
	logFile    *os.File
	indexFile  *os.File
	position   int64 // write position in .log
}

// Log = an ordered list of segments plus the active one.
type Log struct {
	dir          string
	maxSegBytes  int64
	segments     []*Segment // closed, read-only segments, oldest first
	active       *Segment
}

// NewLog opens (or creates) a log directory.
func NewLog(dir string, maxSegBytes int64) (*Log, error) { ... }

// Append stores payload and returns the offset it was assigned.
func (l *Log) Append(payload []byte) (uint64, error) { ... }

// Read returns the payload stored at offset.
func (l *Log) Read(offset uint64) ([]byte, error) { ... }

// Close flushes and closes all files.
func (l *Log) Close() error { ... }
```

Hmm, how much skeleton? The skill says "Show the interface or skeleton" then "Let the learner write the core". I'll give the types + function signatures + doc comments explaining the on-disk format, with bodies as TODO panics. The learner implements.

The test (checkpoint):

```go
func TestAppendThenRead(t *testing.T) {
	dir, _ := os.MkdirTemp("", "minilog")
	defer os.RemoveAll(dir)

	log, err := NewLog(dir, 1<<20) // roll segment every 1 MiB
	...
	const n = 10000
	for i := 0; i < n; i++ {
		off, err := log.Append([]byte(fmt.Sprintf("msg-%d", i)))
		if err != nil { t.Fatal(err) }
		if off != uint64(i) { t.Fatalf(...) }
	}
	got, err := log.Read(5000)
	want := "msg-5000"
	if string(got) != want { t.Fatalf("Read(5000) = %q, want %q", got, want) }
}
```

Maybe also a reopen test (persistence) — but keep the checkpoint minimal per the milestone table: "append 10k messages, then read offset 5000 and get the right payload". I can add a second test for reopen as part of the same milestone since persistence is the point of an on-disk log. The milestone says segments, offsets, index file — reopen is a natural part. I'll include a reopen test too; it forces real file I/O rather than memory. Keep it small.

Now the response format per the skill's "Output for each turn":
- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton/TODO list
- How to check: command + expected output
- Stuck? one hint at a time

Also credit upstream: https://github.com/buildthingsuseful/build-your-own-kafka (Java; we port the roadmap to Go).

Language: respond in Chinese (user wrote in Chinese).

Tone rules: no filler, lead with the answer, no "不是X而是Y" constructions, no summary stamps, no conditional next-step menus. End with the concrete next action for the learner (write the core of log.go), which is a direct instruction, fine.

Now, about scope questions: the skill says ask at most 2 questions with defaults. I'll state defaults inline (Go, single binary, TCP binary protocol in milestone 2, local processes/ports) and let them object. That avoids blocking.

Let me also decide the record format precisely so the learner has an unambiguous spec:

Record (little-endian):
- 4 bytes: payload length (uint32)
- 4 bytes: crc32 of payload
- payload bytes

Offset: implicit within segment (baseOffset + record ordinal). Index entry: 8-byte offset + 8-byte position (int64). Index is sparse in real Kafka; for milestone 1, dense (one entry per record) is fine and simpler — mention that Kafka uses sparse indexing as a later optimization. Actually dense index of 8+8=16 bytes per record doubles write volume; but simplicity wins for milestone 1. Mention sparse as stretch.

Segment roll: when active segment's .log size ≥ maxSegBytes, seal it (flush, add to segments, start new segment with baseOffset = nextOffset).

Read(offset): find segment with largest baseOffset ≤ offset (binary search over segments), then use index to find position, read length+crc, verify crc, return payload. With dense index, direct lookup: read entry at (offset - baseOffset) * 16.

Edge cases the learner will hit (good hints to have ready, but only give one at a time per skill):
- offset beyond end → ErrOffsetOutOfRange
- empty log Read(0) → error
- crash mid-write (partial record) → length read fails or crc mismatch; milestone 6 territory, but crc check belongs in milestone 1.

I'll write the scaffold files now. Keep log.go as a skeleton with TODOs — the learner writes bodies. But should NewLog be fully implemented by me? No — leave TODOs for all core functions; the learner writes the core. I'll include the type definitions, constants, errors, and function signatures with doc comments, plus TODO markers describing each step. That's the "skeleton" the skill prescribes.

One consideration: `log` as a variable name shadows the stdlib `log` package — fine in the test since we don't import log. Use `lg` or `l`? In the test I'll name it `lg` to avoid confusion. Actually `log` is fine as a local var; Go allows shadowing. But style-wise I'll use `lg`.

Module name: `minilog`. Directory: workspace root (empty except .agents, AGENTS.md). Create files at root: go.mod, log.go, log_test.go. Or a subdir like `minilog/`? Root is fine and simplest for `go test ./...`.

Let me write the files.

go.mod:
```
module minilog

go 1.26
```

log.go skeleton:

```go
// Package minilog 实现一个 Kafka 风格的追加式日志：
// 消息按到达顺序编号（offset），落盘为多个段（segment），
// 每个段由一个 .log 数据文件和一个 .index 稀疏/稠密索引文件组成。
package minilog

import (
	"errors"
	"os"
	"path/filepath"
)

// 磁盘格式（小端）：
//
//	.log   : 若干条记录依次排列
//	         记录 = [4B payload 长度][4B crc32(payload)][payload]
//	         offset 是隐式的：baseOffset 为 B 的段里第 i 条记录的 offset = B+i
//	.index : 若干条索引项依次排列
//	         索引项 = [8B offset][8B 该记录在 .log 中的物理位置]
//	         milestone 1 用稠密索引（每条记录一项）；Kafka 实际用稀疏索引，留作优化
//
// 目录布局示例（baseOffset=0, 5, 10 …）：
//
//	00000000000.log  00000000000.index
//	00000000005.log  00000000005.index

var (
	ErrOffsetOutOfRange = errors.New("minilog: offset out of range")
	ErrCorrupt          = errors.New("minilog: crc mismatch")
)

// Segment 是一个已封口（只读）或活跃（可追加）的段。
type Segment struct {
	baseOffset uint64
	logFile    *os.File
	indexFile  *os.File
	position   int64 // .log 的当前写位置
}

// Log 是按 baseOffset 有序的段列表 + 一个活跃段。
type Log struct {
	dir         string
	maxSegBytes int64
	segments    []*Segment // 已封口的旧段，最旧在前，按 baseOffset 升序
	active      *Segment
	nextOffset  uint64 // 下一条消息将获得的 offset
}

// NewLog 打开（或初始化）一个日志目录，恢复已有段并从断点继续编号。
func NewLog(dir string, maxSegBytes int64) (*Log, error) {
	// TODO:
	//  1. os.MkdirAll(dir, 0o755)
	//  2. 扫描目录里的 *.log，按文件名（=baseOffset，20 位十进制）排序
	//  3. 每个旧段：打开 .log/.index，恢复 position（.log 文件大小）
	//  4. 最后一个段作为 active；没有段则新建 baseOffset=0 的段
	//  5. nextOffset = 最后一个段的 baseOffset + 它包含的记录条数
	//     （提示：记录条数可以从 .index 大小 / 16 得到）
	return nil, errors.New("not implemented")
}

// Append 追加一条消息，返回分配给它的 offset。
func (l *Log) Append(payload []byte) (uint64, error) {
	// TODO:
	//  1. off := l.nextOffset
	//  2. 编码记录 [len][crc][payload]，追加写 active.logFile，
	//     同时往 active.indexFile 写一条 [off][position]
	//  3. 更新 active.position 和 l.nextOffset
	//  4. 若 active.position >= l.maxSegBytes，封口当前段并开新段
	//     （新段 baseOffset = off + 1）
	return 0, errors.New("not implemented")
}

// Read 返回 offset 处的消息。
func (l *Log) Read(offset uint64) ([]byte, error) {
	// TODO:
	//  1. 二分（或线性）找到 baseOffset <= offset 的最后一个段
	//  2. offset - baseOffset 得到索引项序号，从 .index 读出物理位置
	//  3. 从 .log 该位置读 [len][crc][payload]，校验 crc
	//  4. offset 越界（超出所有段）返回 ErrOffsetOutOfRange
	return nil, errors.New("not implemented")
}

// Close 刷盘并关闭所有文件。
func (l *Log) Close() error { return errors.New("not implemented") }
```

Hmm wait — should I include the TODO comments with this much detail? The skill says "Give an interface or skeleton" and "a skeleton or a TODO list, not the full answer". Detailed TODOs are the scaffold; the learner still writes all the real code (encoding, file I/O, binary search, crc). I think this level is right — it's a spec, not a solution. The learner writes ~150 lines themselves.

log_test.go:

```go
package minilog

import (
	"fmt"
	"os"
	"path/filepath"
	"testing"
)

// checkpoint 1：追加 10k 条，读 offset 5000，内容必须正确。
func TestAppend10kThenRead5000(t *testing.T) {
	dir := t.TempDir()
	lg, err := NewLog(dir, 1<<20) // 每段 1 MiB，10k 条会滚出多个段
	if err != nil {
		t.Fatalf("NewLog: %v", err)
	}
	defer lg.Close()

	const n = 10000
	for i := 0; i < n; i++ {
		off, err := lg.Append([]byte(fmt.Sprintf("msg-%d", i)))
		if err != nil {
			t.Fatalf("Append(%d): %v", i, err)
		}
		if off != uint64(i) {
			t.Fatalf("Append returned offset %d, want %d", off, i)
		}
	}

	got, err := lg.Read(5000)
	if err != nil {
		t.Fatalf("Read(5000): %v", err)
	}
	if want := "msg-5000"; string(got) != want {
		t.Fatalf("Read(5000) = %q, want %q", got, want)
	}
}

// checkpoint 1b：关掉再重开，日志必须还在，编号必须接上。
func TestReopenContinuesNumbering(t *testing.T) {
	dir := t.TempDir()

	lg, err := NewLog(dir, 1<<20)
	if err != nil {
		t.Fatal(err)
	}
	for i := 0; i < 100; i++ {
		if _, err := lg.Append([]byte(fmt.Sprintf("msg-%d", i))); err != nil {
			t.Fatal(err)
		}
	}
	if err := lg.Close(); err != nil {
		t.Fatal(err)
	}

	lg2, err := NewLog(dir, 1<<20)
	if err != nil {
		t.Fatal(err)
	}
	defer lg2.Close()

	off, err := lg2.Append([]byte("after-restart"))
	if err != nil {
		t.Fatal(err)
	}
	if off != 100 {
		t.Fatalf("first offset after reopen = %d, want 100", off)
	}
	got, err := lg2.Read(42)
	if err != nil {
		t.Fatal(err)
	}
	if want := "msg-42"; string(got) != want {
		t.Fatalf("Read(42) = %q, want %q", got, want)
	}
}
```

Wait — TestReopenContinuesNumbering uses filepath? No, I removed that import need. Check imports: fmt, os?, testing. t.TempDir() handles dir. I don't use os or filepath in the test. Let me fix imports: fmt, testing only.

Also in log.go skeleton, imports: errors, os. I reference filepath in TODO text only (comments don't need imports). But unused imports cause compile errors — the skeleton must compile. errors and os are used (os.File in struct, errors.New in bodies). Good.

Actually, will the skeleton compile with `go vet`/test? Struct fields unused are fine. Functions return errors.New("not implemented") — compiles. Test will fail (that's the point — red first).

One more thing: the test file name `log_test.go`, package minilog (internal test). Fine.

Also should I create PROGRESS.md? The skill says record in PROGRESS.md when a milestone passes. Not yet — milestone 1 hasn't passed. I'll create it when it passes. Actually I could create it now with milestone 1 pending... The skill says "When a milestone passes, record it". So wait.

Todo list: seed with milestones. Let me do:
1. M1 追加式日志（segments/offset/index）— in_progress
2. M2 Broker API（TCP produce/fetch）
3. M3 Topics + partitions
4. M4 Consumer groups
5. M5 Replication
6. M6 故障注入测试
7. M7 stretch: Raft

Now the response text (Chinese), following the skill's output format:

- Where we are: 里程碑 1/7
- Concept: 3-6 sentences on append-only log, segments, offsets, index
- What to write next: the skeleton is scaffolded at log.go; implement the 4 TODOs
- How to check: `go test ./...` expected output
- Credit upstream tutorial link
- Scope defaults stated briefly

Also mention: the only upstream tutorial is Java (link), we port its roadmap to Go per the track skill.

Order of response: lead with the answer (第一步 = milestone 1: append-only log). Then concept, then what I scaffolded, then what they write, then check command.

Keep it tight. Let me write the files first, then respond.

One design decision to flag: dense vs sparse index — I chose dense for M1, noted Kafka uses sparse. Also record format includes crc32 — gives them a corruption check and prepares for M6. Offsets implicit (derived), matching Kafka where offset = base + ordinal within segment... actually in Kafka, offsets are assigned by the broker sequentially and stored implicitly too (Kafka computes offset from position since records are fixed... no, Kafka records have variable length but offsets are implicit by counting from baseOffset — yes, in Kafka the log file's records are sequential and offset = baseOffset + index within segment; the index maps offset→position sparsely). Fine.

maxSegBytes default in test: 1<<20 = 1 MiB. 10k messages × ~12 bytes ≈ 120 KB — that would fit in ONE 1MiB segment! msg-9999 is 8 bytes payload + 8 bytes header = 16 bytes; 10k × 16 = 160 KB < 1 MiB. So no segment roll would happen with 1 MiB. I need a smaller maxSegBytes to force multiple segments, e.g., 4096 bytes → 10k×16B = 160KB / 4KB ≈ 40 segments. Good: use 4096 in the test. That exercises the roll logic, which is the point of "segments". Let me set maxSegBytes = 4096 in both tests. In test 2, 100 messages × ~16B = 1.6KB < 4KB — single segment, fine (reopen logic still exercised). Maybe make test 2 also roll: 500 messages ≈ 8KB → 2 segments. Let me use 500 messages in test 2, expect first offset after reopen = 500, read offset 42 → "msg-42". Good.

Also the checkpoint from the skill table: "append 10k messages, then read offset 5000 and get the right payload" — covered by test 1.

Edge: with maxSegBytes=4096 and record ~16B, roll happens mid-append; the new segment's baseOffset = off+1. Read(5000) must find the right segment among ~40. Good exercise.

Now write files. After writing, run `go test ./...` to confirm it compiles and fails with "not implemented" (red state). That verifies the scaffold compiles — important. Then present.

Actually wait: should I run the test? It will fail (not implemented). Running it confirms the scaffold compiles and the failure is the expected one. Yes, run it, show expected output in my reply ("not implemented" failures = 正确的起点).

Let me also double check go.mod go version: go1.26.1 installed; `go 1.26` directive fine.

File creation: write tool. Then bash go test.

Response structure (Chinese, concise):

**第一步：里程碑 1/7 —— 追加式日志（append-only log）**

上游教程只有 Java 版（buildthingsuseful/build-your-own-kafka），路线图语言无关，我们用 Go 移植。默认范围：单机先跑通，M2 用 TCP 二进制协议，多节点用本地进程 + 不同端口。

概念（3-6 句）：Kafka 的存储核心就是一个只能追加的日志。消息按到达顺序拿到单调递增的 offset；磁盘上切成多个 segment（.log 数据文件 + .index 索引文件），写满一个就滚到下一个；读的时候先按 baseOffset 定位段，再用索引把 offset 换算成文件里的物理位置。这一步做完，你就有了后面所有功能（分区、复制、消费组）都要踩的那块地板。

已搭好骨架：
- go.mod
- log.go — 类型 + 磁盘格式注释 + 4 个 TODO（NewLog / Append / Read / Close）
- log_test.go — 两个 checkpoint 测试

你来写核心：实现 log.go 里的 4 个 TODO。建议顺序：Append（先只写单段）→ Read → NewLog 的恢复逻辑 → 段滚动。

检查：
```
go test ./...
```
当前是红的（not implemented）；两个测试都 PASS 即里程碑 1 完成，我会记进 PROGRESS.md。

卡住的话一次给一个提示。

Hmm, "卡住的话一次给一个提示" — that's from the skill's output format ("Stuck? One hint at a time."). I can phrase as: 卡住了直接贴报错，我一次给一个提示。

Also mention the disk format is specified in log.go comments so they have an unambiguous spec.

Length: keep tight. Let me finalize files.

One more check on log.go skeleton compile: struct Segment has fields baseOffset, logFile, indexFile, position — unused fields OK. Log struct similar. Functions return errors.New — need errors import. os used in *os.File. Good.

In test file: imports fmt, testing. t.TempDir() returns string. lg.Close() in defer — Close returns error, defer lg.Close() is fine (errcheck not enforced by go test).

Wait, in test 1 I have `defer lg.Close()` — fine.

Let me also think: does `go test ./...` with module `minilog` at root work? Yes, package in root dir.

Write the files now.Verify the scaffold compiles and fails with the expected "not implemented" errors.The scaffold compiles and fails with the expected "not implemented" errors. Now set up the todo list with the milestones and respond per the skill's output format.**当前位置：里程碑 1/7 —— 追加式日志（append-only log）。** 这是整个系统的地基：分区、复制、消费组全都踩在这块地板上。

上游教程只有 Java 版（[buildthingsuseful/build-your-own-kafka](https://github.com/buildthingsuseful/build-your-own-kafka)），路线图本身语言无关，我们用 Go 移植。默认范围：M2 用 TCP 二进制协议，多节点用本地进程 + 不同端口，全程零外部依赖。

**概念（3 句）：** Kafka 的存储核心是一个只能追加的日志。每条消息按到达顺序拿到单调递增的 offset；磁盘上切成多个 segment，每个段 = 一个 `.log` 数据文件 + 一个 `.index` 索引文件，写满就滚动到下一个段。读的时候先按 baseOffset 定位段，再用索引把 offset 换算成文件内的物理位置——顺序写、按 offset 随机读，这就是 Kafka 吞吐量的来源。

**已搭好的骨架**（工作区根目录，`go vet` 通过，测试当前是红的）：

- `log.go` — 类型定义 + 磁盘格式规格（写在注释里）+ 4 个 TODO：`NewLog` / `Append` / `Read` / `Close`
- `log_test.go` — 两个 checkpoint 测试
- `go.mod`

**你来写核心：** 实现 `log.go` 里的 4 个 TODO。建议顺序：`Append`（先只写单段）→ `Read` → `NewLog` 的恢复逻辑 → 段滚动。磁盘格式已定死在 `log.go:10` 的注释里：记录 = `[4B 长度][4B crc32][payload]`，索引项 = `[8B offset][8B 物理位置]`，offset 在段内隐式（baseOffset + 第几条）。

**检查方式：**

```
go test ./...
```

两个测试都 PASS 即里程碑 1 完成：`TestAppend10kThenRead5000` 追加 1 万条（`maxSegBytes=4096` 会强制滚出几十个段）后读 offset 5000 必须拿到 `msg-5000`；`TestReopenContinuesNumbering` 关掉重开后编号必须从断点继续。通过后我记入 `PROGRESS.md`，进 M2。

卡住了直接贴报错，我一次给一个提示。