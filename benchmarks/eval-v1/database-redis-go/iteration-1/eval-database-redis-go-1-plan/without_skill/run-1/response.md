The user wants to learn and implement "Build Your Own Redis" from scratch in Go. They want me to:
1. Plan milestones
2. Create a minimal project skeleton

The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-database-redis-go-1` — this looks like a "build your own X" challenge workspace (codecrafters-style, "build-your-own-x-database-redis-go").

Let me first explore the current workspace to see what's there, then plan milestones and create a minimal skeleton.

Let me start by exploring the workspace structure.Empty workspace, Go 1.26.1 available. Now let me plan the milestones for building a Redis clone in Go, and create a minimal project skeleton.

Let me think about what a "Build Your Own Redis" course looks like (codecrafters "Build your own Redis" challenge):

Stages typically:
1. Bind to a port and respond to PING (handle `-PING` / `+PONG`)
2. RESP protocol basics — parse simple inline commands, handle echo
3. RESP arrays (bulk strings), SET/GET
4. Expiration (PX option)
5. RDB persistence (key-value, expiry)
6. Replication (master/replica, handshake, wait command)
7. Streams (XADD, XRANGE, XREAD)

For a learning project from scratch, I'll plan milestones:

M0: Project skeleton — go.mod, main.go, TCP server skeleton, graceful shutdown, logging, Makefile, README with milestones.
M1: TCP server + RESP protocol parser (RESP2: simple strings, errors, integers, bulk strings, arrays) — echo server, unit tests for parser.
M2: Command dispatch — PING, ECHO, SET, GET with in-memory store (concurrent-safe map).
M3: Key expiration (PX/TTL, lazy + active eviction).
M4: Persistence — RDB-like snapshot (or AOF append log).
M5: Replication — master/replica handshake, propagation, WAIT.
M6: Streams — XADD, XRANGE, XREAD (blocking).
M7: Hardening — tests, benchmarks, CI.

Now create the minimal skeleton:
- go.mod (module name, e.g. `github.com/linkxzhou/miniredis` or simpler `miniredis`)
- cmd/server/main.go — flag parsing (port), start server
- internal/server/server.go — TCP accept loop, per-connection goroutine
- internal/resp/resp.go — minimal RESP reader/writer stubs (maybe just types + TODO)
- internal/store/store.go — in-memory store stub
- Makefile
- README.md with milestone plan
- .gitignore

Keep it minimal but runnable: the skeleton should compile and run, accept connections, and maybe respond to PING already? "最小项目骨架" — minimal skeleton. I'd make it compile and run with a TCP accept loop and a placeholder handler that logs unknown commands. Maybe include PING as a smoke test since it's trivial and gives immediate feedback. But keep the RESP parser minimal — maybe just implement enough to read an inline command or a RESP array? To keep it "minimal skeleton", I'll implement:

- resp: a Reader that can parse a RESP array of bulk strings (the core of Redis protocol), with tests
- server: accept loop, connection handler dispatching to a command registry
- commands: PING implemented as the first command
- store: placeholder package with a Get/Set skeleton

Actually, let me be careful about scope. The user asked for: 规划里程碑 (plan milestones) + 创建最小项目骨架 (create minimal project skeleton). So the deliverable is:

1. A milestone plan (in README or a PLAN.md)
2. A minimal skeleton that compiles and runs

I should follow the explore → plan → execute → verify flow. The workspace is empty, so exploration is trivial. I'll call explore to record, then plan, then create files, then verify with `go build` and `go test`, and a quick smoke test with redis-cli or a raw nc/python test.

Let me check if redis-cli is available for smoke testing later. I can do a smoke test with a small Go test or nc.

Let me structure the skeleton:

```
go.mod                      module miniredis
Makefile                    build / test / run
README.md                   milestones + how to run
.gitignore
cmd/miniredis/main.go       flags: --port, start server, graceful shutdown on SIGINT/SIGTERM
internal/resp/resp.go       RESP2 reader: ReadArray (bulk strings), Writer: SimpleString/Error/Bulk/Integer/Array/Null
internal/resp/resp_test.go  parser tests
internal/server/server.go   Server: Listen, Serve loop, Conn handler; Handler interface
internal/server/server_test.go  integration smoke test over real TCP
internal/command/registry.go  command table: name -> func
internal/command/ping.go    PING
internal/store/store.go     Store with Get/Set/TTL stubs (mutex + map)
```

Hmm, is that too much? "最小" — minimal. But a good skeleton has the seams where future milestones plug in. I think this is reasonable: ~6 source files, each small. The key design decision: command registry + RESP codec + store separation, which is exactly how milestones 2-6 will extend.

Actually, let me reconsider: maybe keep it even leaner — cmd/miniredis/main.go, internal/server, internal/resp, internal/store, and put PING dispatch inside server with a simple map. I'll keep a tiny command package since it's the natural extension point. Let me not over-engineer: I'll put the command registry in internal/server or a small internal/command package. I'll go with internal/command — clean.

Wait — per instructions: "Don't create helpers / abstractions for one-time operations." The command registry is the core extension mechanism for the whole project, so it's justified. The store stub with Get/Set is justified as milestone 2's seam. OK.

RESP protocol details for the parser:
- RESP2 types: `+simple\r\n`, `-Error\r\n`, `:123\r\n`, `$5\r\nhello\r\n`, `*2\r\n...`
- Client → server: arrays of bulk strings.
- Reader should be buffered, read line by line, parse types. Support inline commands too (space-separated) — real Redis supports that; nice for nc testing. I'll include inline command support since it's cheap and helps debugging.

Writer: encode replies.

Let me write the code.

go.mod:
```
module github.com/linkxzhou/miniredis

go 1.26
```

Hmm, module path — user is linkxzhou. I'll use `github.com/linkxzhou/miniredis`. Or simpler: `miniredis`. For a learning project, a plain `miniredis` module name works fine and avoids implying a GitHub repo. But convention favors full path. I'll use `github.com/linkxzhou/miniredis`.

cmd/miniredis/main.go:
```go
package main

import (
    "flag"
    "log"
    "os"
    "os/signal"
    "syscall"

    "github.com/linkxzhou/miniredis/internal/server"
)

func main() {
    port := flag.Int("port", 6379, "port to listen on")
    flag.Parse()

    srv := server.New(server.Options{Addr: fmt.Sprintf("127.0.0.1:%d", *port)})
    ...
}
```

Graceful shutdown: listen on signal, srv.Close().

internal/resp/resp.go — the codec:

```go
// Package resp implements the RESP2 protocol used by Redis clients.
package resp

import (
    "bufio"
    "errors"
    "fmt"
    "io"
    "strconv"
    "strings"
)

// Value is a decoded RESP value.
type Value struct {
    Type  Type
    Str   string   // SimpleString, Error, Bulk
    Int   int64    // Integer
    Array []Value  // Array
    Null  bool
}
```

Hmm, a struct-based Value or an interface? For learning, a tagged struct is simpler to pattern-match. Alternatively use Go idiomatic: `type Value interface{}` with concrete types string, int64, []Value, nil. Many mini-redis implementations use a struct with kind. I'll go with a small struct.

Actually simpler and idiomatic: 

```go
type Value struct {
    typ   byte // '+', '-', ':', '$', '*'
    str   string
    num   int64
    array []Value
    null  bool
}
```

with constructors SimpleString(s), Error(s), Integer(n), Bulk(s), Null(), Array(vs) and accessors. Keep it exported minimal: I'll make fields exported for simplicity in a learning project? Encapsulation adds boilerplate. Let me use exported fields with constructors:

```go
type Value struct {
    Kind  Kind
    Str   string
    Int   int64
    Array []Value
}
```

with Kind enum: KindSimpleString, KindError, KindInteger, KindBulk, KindArray, KindNull. For Bulk null vs empty: KindNull covers both `$-1` and `*-1`.

Reader:

```go
type Reader struct {
    r *bufio.Reader
}

func NewReader(r io.Reader) *Reader

// ReadValue reads one RESP value from the wire.
func (r *Reader) ReadValue() (Value, error)
```

Parse:
- read a line (until \r\n)
- switch on first byte:
  - '+': SimpleString
  - '-': Error
  - ':': Integer
  - '$': bulk: read length n; if -1 → Null; read n bytes + CRLF
  - '*': array: count n; if -1 → Null; recurse
- first byte not a known type → treat as inline command: split the line on whitespace → Array of Bulk strings. (Redis inline commands.)

Writer:

```go
type Writer struct {
    w *bufio.Writer
}

func (w *Writer) WriteValue(v Value) error
func (w *Writer) Flush() error
```

Encode per kind.

internal/command/registry.go:

```go
package command

// Handler executes a command and returns the reply.
type Handler func(ctx context.Context, s *store.Store, args []string) (resp.Value, error)

var registry = map[string]Handler{}

func Register(name string, h Handler)
func Lookup(name string) (Handler, bool)
```

Hmm, do I need ctx? For future blocking commands (BLPOP, XREAD block), ctx helps cancellation on connection close. But minimal skeleton — skip ctx, keep `func(s *store.Store, args []string) resp.Value`. Simpler. When milestone for blocking commands arrives, they can extend. Actually returning error vs Value: errors map to RESP `-ERR ...`. I'll have Handler return (resp.Value, error) where error → Error value. That's a clean seam. Keep it.

ping.go:

```go
func init() { Register("PING", ping) }

func ping(s *store.Store, args []string) (resp.Value, error) {
    if len(args) > 0 { return resp.Bulk(args[0]), nil }
    return resp.SimpleString("PONG"), nil
}
```

Wait — real Redis PING with message returns bulk string. Yes.

internal/store/store.go:

```go
package store

import (
    "sync"
    "time"
)

type entry struct {
    val      string
    expiresAt time.Time // zero means no expiry
}

type Store struct {
    mu sync.RWMutex
    m  map[string]entry
}

func New() *Store
func (s *Store) Get(key string) (string, bool)
func (s *Store) Set(key, val string)
func (s *Store) SetEx(key, val string, ttl time.Duration)  // maybe leave for milestone
func (s *Store) Delete(key string) bool
```

Minimal: Get/Set/Delete. TTL in milestone 3. But adding expiresAt field now with SetEx is fine... keep minimal: Get/Set/Delete only. Milestone 3 adds expiry.

internal/server/server.go:

```go
package server

type Options struct {
    Addr string
}

type Server struct {
    ln   net.Listener
    store *store.Store
}

func New(opts Options) *Server
func (s *Server) Listen() error   // bind
func (s *Server) Serve() error    // accept loop
func (s *Server) Close() error
```

Connection handling:

```go
func (s *Server) handleConn(conn net.Conn) {
    defer conn.Close()
    r := resp.NewReader(conn)
    w := resp.NewWriter(conn)
    for {
        v, err := r.ReadValue()
        if err != nil { return } // EOF or bad protocol
        args := flatten(v) // expect array of bulk strings
        if len(args) == 0 { continue }
        name := strings.ToUpper(args[0])
        h, ok := command.Lookup(name)
        if !ok { w.WriteValue(resp.Error(fmt.Sprintf("ERR unknown command '%s'", name))); w.Flush(); continue }
        reply, err := h(s.store, args[1:])
        if err != nil { w.WriteValue(resp.Error(err.Error())) } else { w.WriteValue(reply) }
        w.Flush()
    }
}
```

flatten: convert Value (array of bulk) to []string; handle inline too since reader already returns Array for inline.

server_test.go: spin up server on 127.0.0.1:0, dial with net.Dial, write RESP-encoded PING, expect +PONG. Also test SET/GET? SET/GET are milestone 2 — but if store stub has Get/Set, wiring SET/GET commands is trivial... Should the skeleton include SET/GET? The user said minimal skeleton. PING only proves the pipeline works. I'll include PING + ECHO (both trivial, prove arg passing) and leave SET/GET for milestone 2. Hmm, but store stub with Get/Set unused would be dead code. Options: (a) include SET/GET commands now (they're 10 lines and make the store non-dead), (b) leave store empty with just New() and a TODO.

I think including SET/GET makes the skeleton more satisfying and the store seam real. But it eats into milestone 2's learning. The user wants to learn by implementing. The skeleton should provide structure, with the learning milestones left as TODOs. I'll keep PING + ECHO in the skeleton (protocol-level, no state), and leave the store with a TODO comment for milestone 2. Actually a completely empty store package is weird. Let me just have store.Store with the map and New(), and a doc comment saying M2 adds Get/Set with TTL. Hmm.

Alternative: skip the store package entirely in the skeleton; server holds a `*store.Store`... no. Let me include store with Get/Set/Delete implemented (it's 20 lines, mutex+map) and commands SET/GET/DEL wired. That makes the skeleton a working mini-Redis for the basics, and milestones 3+ (TTL, persistence, replication, streams) remain the learning work. The user asked to "学习并实现" — they want to implement it themselves. Over-implementing the skeleton defeats the purpose.

Decision: skeleton = TCP server + RESP codec (with tests) + command registry + PING/ECHO + store stub (map + New, TODO for M2). This gives them a running base and clear seams. Milestone 2 (SET/GET/DEL + store) is their first real exercise. I'll note in README that PING/ECHO are provided as reference implementations to study.

Hmm wait, actually let me reconsider once more. "创建最小项目骨架" — create minimal project skeleton. The essence: directory layout, go.mod, runnable server, one reference command, tests, README with milestones. My decision above fits. Good.

README.md content:
- Project intro
- Quick start: make run / go run ./cmd/miniredis, test with redis-cli -p 6379 PING or nc
- Milestones M0-M7 with acceptance criteria each
- Layout

Milestones (with acceptance criteria):

M0 骨架 (done): TCP server, RESP codec, PING/ECHO, tests.
M1 RESP 协议完善: full RESP2 encode/decode, inline commands, error cases, fuzz-ish tests. Acceptance: redis-cli connects, protocol round-trip tests pass.

Hmm wait, if the codec is already in the skeleton, M1 is partially done. Let me restructure milestones so the skeleton covers M0 only, and the codec in skeleton is "good enough for PING/ECHO" while M1 hardens it. Actually simpler: skeleton implements the codec fully (it's ~150 lines) and M1 becomes "命令分发与内存存储: SET/GET/DEL/EXISTS/KEYS + 并发安全". Let me lay out:

- M0 ✅ 骨架: go.mod, TCP accept loop, RESP2 codec, 命令注册表, PING/ECHO, 单测+集成测试
- M1 数据命令与存储: SET/GET/DEL/EXISTS/KEYS, store 并发安全, 过期 PX/EX + 惰性删除 (maybe split)
- M2 过期机制: EX/PX/EXPIRE/TTL, 惰性 + 定期删除
- M3 持久化: AOF (append + rewrite) 或 RDB 快照, 启动恢复
- M4 复制: replicaof, 主从握手, 命令传播, WAIT
- M5 流 Streams: XADD/XRANGE/XLEN/XREAD (含阻塞)
- M6 收尾: 基准测试, 并发压测, 与真实 redis-cli 兼容性验证, CI

That's 7 milestones, good granularity for learning. Each with 验收标准.

Makefile:
```make
build:
	go build -o bin/miniredis ./cmd/miniredis
run:
	go run ./cmd/miniredis -port 6379
test:
	go test ./...
vet:
	go vet ./...
```

.gitignore: bin/, *.test

Now the RESP codec code. Let me write it carefully.

```go
// Package resp implements the RESP2 wire protocol spoken by Redis clients.
package resp

import (
	"bufio"
	"errors"
	"fmt"
	"io"
	"strconv"
	"strings"
)

// Kind identifies which RESP2 type a Value holds.
type Kind byte

const (
	KindSimpleString Kind = '+' // +OK\r\n
	KindError        Kind = '-' // -ERR msg\r\n
	KindInteger      Kind = ':' // :42\r\n
	KindBulk         Kind = '$' // $5\r\nhello\r\n
	KindArray        Kind = '*' // *1\r\n$4\r\nPING\r\n
	KindNull         Kind = 0   // $-1 / *-1
)

// Value is one decoded RESP2 value.
type Value struct {
	Kind  Kind
	Str   string  // KindSimpleString, KindError, KindBulk
	Int   int64   // KindInteger
	Array []Value // KindArray
}

func SimpleString(s string) Value { return Value{Kind: KindSimpleString, Str: s} }
func Error(s string) Value        { return Value{Kind: KindError, Str: s} }
func Integer(n int64) Value       { return Value{Kind: KindInteger, Int: n} }
func Bulk(s string) Value         { return Value{Kind: KindBulk, Str: s} }
func Array(vs ...Value) Value     { return Value{Kind: KindArray, Array: vs} }
func Null() Value                 { return Value{Kind: KindNull} }
```

Reader:

```go
// Reader decodes RESP2 values from an io.Reader.
type Reader struct {
	br *bufio.Reader
}

func NewReader(r io.Reader) *Reader {
	return &Reader{br: bufio.NewReader(r)}
}

// ReadValue decodes the next value. Inline commands (plain text lines) are
// returned as an array of bulk strings, like real Redis does.
func (r *Reader) ReadValue() (Value, error) {
	line, err := r.readLine()
	if err != nil {
		return Value{}, err
	}
	switch line[0] {
	case '+':
		return SimpleString(line[1:]), nil
	case '-':
		return Error(line[1:]), nil
	case ':':
		n, err := strconv.ParseInt(line[1:], 10, 64)
		if err != nil {
			return Value{}, fmt.Errorf("resp: bad integer %q", line[1:])
		}
		return Integer(n), nil
	case '$':
		return r.readBulk(line[1:])
	case '*':
		return r.readArray(line[1:])
	default:
		// Inline command: "PING\r\n" -> ["PING"].
		return Array(bulkStrings(strings.Fields(line))...), nil
	}
}
```

readLine: read until \n, strip trailing \r\n. Use bufio.Reader ReadBytes('\n')? ReadBytes returns err==io.EOF with partial data if no trailing newline. Handle: if err != nil && err != io.EOF → return err; if len(line)==0 && err==io.EOF → return io.EOF. Strip \r\n suffix.

```go
func (r *Reader) readLine() (string, error) {
	line, err := r.br.ReadString('\n')
	if err != nil {
		if err == io.EOF && line != "" {
			return "", errors.New("resp: unexpected EOF mid-line")
		}
		return "", err // io.EOF or real error
	}
	line = strings.TrimSuffix(line, "\n")
	line = strings.TrimSuffix(line, "\r")
	return line, nil
}
```

Hmm, ReadString('\n') on EOF with partial data returns (partial, io.EOF). If line non-empty at EOF → protocol error (truncated). If empty → clean EOF. Good.

readBulk:

```go
func (r *Reader) readBulk(lenStr string) (Value, error) {
	n, err := strconv.Atoi(lenStr)
	if err != nil || n < -1 {
		return Value{}, fmt.Errorf("resp: bad bulk length %q", lenStr)
	}
	if n == -1 {
		return Null(), nil
	}
	buf := make([]byte, n+2) // payload + CRLF
	if _, err := io.ReadFull(r.br, buf); err != nil {
		return Value{}, fmt.Errorf("resp: short bulk: %w", err)
	}
	return Bulk(string(buf[:n])), nil
}
```

readArray:

```go
func (r *Reader) readArray(countStr string) (Value, error) {
	n, err := strconv.Atoi(countStr)
	if err != nil || n < -1 {
		return Value{}, fmt.Errorf("resp: bad array length %q", countStr)
	}
	if n == -1 {
		return Null(), nil
	}
	vs := make([]Value, 0, n)
	for i := 0; i < n; i++ {
		v, err := r.ReadValue()
		if err != nil {
			return Value{}, err
		}
		vs = append(vs, v)
	}
	return Value{Kind: KindArray, Array: vs}, nil
}
```

Writer:

```go
// Writer encodes RESP2 values to an io.Writer.
type Writer struct {
	bw *bufio.Writer
}

func NewWriter(w io.Writer) *Writer { return &Writer{bw: bufio.NewWriter(w)} }

func (w *Writer) WriteValue(v Value) error {
	var err error
	switch v.Kind {
	case KindSimpleString:
		_, err = fmt.Fprintf(w.bw, "+%s\r\n", v.Str)
	case KindError:
		_, err = fmt.Fprintf(w.bw, "-%s\r\n", v.Str)
	case KindInteger:
		_, err = fmt.Fprintf(w.bw, ":%d\r\n", v.Int)
	case KindBulk:
		_, err = fmt.Fprintf(w.bw, "$%d\r\n%s\r\n", len(v.Str), v.Str)
	case KindArray:
		if _, err = fmt.Fprintf(w.bw, "*%d\r\n", len(v.Array)); err != nil {
			break
		}
		for _, e := range v.Array {
			if err = w.WriteValue(e); err != nil {
				return err
			}
		}
		return nil
	case KindNull:
		_, err = w.bw.WriteString("$-1\r\n")
	}
	return err
}

func (w *Writer) Flush() error { return w.bw.Flush() }
```

Careful with the switch/break in Go — `break` inside switch breaks the switch. In the KindArray case I wrote early returns, fine. Let me restructure to avoid confusion:

```go
func (w *Writer) WriteValue(v Value) error {
	switch v.Kind {
	case KindSimpleString:
		_, err := fmt.Fprintf(w.bw, "+%s\r\n", v.Str)
		return err
	...
	case KindArray:
		if _, err := fmt.Fprintf(w.bw, "*%d\r\n", len(v.Array)); err != nil {
			return err
		}
		for _, e := range v.Array {
			if err := w.WriteValue(e); err != nil {
				return err
			}
		}
		return nil
	default:
		return fmt.Errorf("resp: cannot encode kind %d", v.Kind)
	}
}
```

Cleaner.

Note: len(v.Str) is byte length — correct for RESP bulk length. Good.

resp_test.go: table-driven round-trip tests:
- decode `*1\r\n$4\r\nPING\r\n` → array [PING]
- inline `PING\r\n` → [PING], `SET k v\r\n` → [SET k v]
- decode bulk with spaces `$3\r\na b\r\n`
- null bulk `$-1\r\n`
- integer `:42\r\n`
- error `-ERR x\r\n`
- encode each kind and compare bytes
- round-trip: encode array then decode

Also a test for partial reads? bufio handles that; skip for minimal.

command package:

registry.go:
```go
// Package command holds the command registry: name -> handler.
package command

import (
	"fmt"

	"github.com/linkxzhou/miniredis/internal/resp"
	"github.com/linkxzhou/miniredis/internal/store"
)

// Handler executes one command. args excludes the command name.
// A returned error is sent to the client as a RESP error reply.
type Handler func(s *store.Store, args []string) (resp.Value, error)

var registry = map[string]Handler{}

// Register adds a handler; panics on duplicate names (programming error).
func Register(name string, h Handler) {
	if _, dup := registry[name]; dup {
		panic(fmt.Sprintf("command %q registered twice", name))
	}
	registry[name] = h
}

// Lookup finds a handler by (upper-cased) name.
func Lookup(name string) (Handler, bool) {
	h, ok := registry[strings.ToUpper(name)]
	return h, ok
}
```

ping.go:
```go
package command

import "github.com/linkxzhou/miniredis/internal/resp"

func init() {
	Register("PING", ping)
	Register("ECHO", echo)
}

// PING [message] -> +PONG or bulk(message)
func ping(_ *store.Store, args []string) (resp.Value, error) {
	if len(args) > 1 {
		return resp.Value{}, fmt.Errorf("ERR wrong number of arguments for 'ping' command")
	}
	if len(args) == 1 {
		return resp.Bulk(args[0]), nil
	}
	return resp.SimpleString("PONG"), nil
}

func echo(_ *store.Store, args []string) (resp.Value, error) {
	if len(args) != 1 {
		return resp.Value{}, errors.New("ERR wrong number of arguments for 'echo' command")
	}
	return resp.Bulk(args[0]), nil
}
```

store.go:
```go
// Package store holds the in-memory key/value data.
package store

import "sync"

// Store is a concurrency-safe in-memory key/value store.
// Milestone M1 adds typed values and TTL support on top of this.
type Store struct {
	mu sync.RWMutex
	m  map[string]string
}

func New() *Store {
	return &Store{m: make(map[string]string)}
}

func (s *Store) Get(key string) (string, bool) {
	s.mu.RLock()
	defer s.mu.RUnlock()
	v, ok := s.m[key]
	return v, ok
}

func (s *Store) Set(key, val string) {
	s.mu.Lock()
	defer s.mu.Unlock()
	s.m[key] = val
}

func (s *Store) Delete(key string) bool {
	s.mu.Lock()
	defer s.mu.Unlock()
	_, ok := s.m[key]
	delete(s.m, key)
	return ok
}
```

Wait — I decided to leave SET/GET for M1 as the user's first exercise. But then store.Get/Set/Delete would be unused code in the skeleton. Unused exported methods in a library-ish package are fine (no compile error). But "don't add features beyond what was asked"... The skeleton needs a store seam for the server to hold. I'll include the store with Get/Set/Delete (it's the natural minimal seam) and wire SET/GET/DEL commands too — actually no. Let me decide firmly:

Option A: skeleton includes PING/ECHO only; store package exists with map+Get/Set/Delete but no commands use it yet. Server still holds *store.Store and passes it to handlers. This is fine — the seam exists, commands come in M1.

Option B: include SET/GET/DEL too.

The user wants to learn by doing. M1 (SET/GET/DEL) is the perfect first exercise — 30 lines using the existing seams. I'll go with Option A and say so in the README ("M1 是你的第一个练习"). The store methods being pre-written slightly reduces the exercise... I could leave store as just `New()` + map + a TODO. But then the server can't compile handlers referencing store... handlers receive *store.Store and ignore it. Fine.

Hmm, actually for the skeleton to be useful as a *reference*, having store.Get/Set implemented shows the locking pattern. But it's trivial. I'll include Get/Set/Delete in store (small, shows the mutex pattern) and leave command wiring to the user. Compromise is fine.

server.go:

```go
// Package server accepts TCP connections and speaks RESP.
package server

import (
	"fmt"
	"io"
	"log"
	"net"
	"strings"

	"github.com/linkxzhou/miniredis/internal/command"
	"github.com/linkxzhou/miniredis/internal/resp"
	"github.com/linkxzhou/miniredis/internal/store"
)

type Options struct {
	// Addr to listen on, e.g. "127.0.0.1:6379". Empty means ":6379".
	Addr string
}

type Server struct {
	ln    net.Listener
	store *store.Store
}

// New creates a server; call Listen then Serve.
func New(opts Options) *Server {
	return &Server{store: store.New()}
}

// Listen binds the listening socket.
func (s *Server) Listen(addr string) error {
	ln, err := net.Listen("tcp", addr)
	if err != nil {
		return fmt.Errorf("listen %s: %w", addr, err)
	}
	s.ln = ln
	return nil
}

// Serve accepts connections until Close. Each connection gets its own
// goroutine; commands on one connection are processed sequentially.
func (s *Server) Serve() error {
	for {
		conn, err := s.ln.Accept()
		if err != nil {
			return err // TODO: tolerate temporary errors with net.Error handling
		}
		go s.handleConn(conn)
	}
}

// Close stops the listener.
func (s *Server) Close() error {
	if s.ln != nil {
		return s.ln.Close()
	}
	return nil
}

// Addr returns the bound address (useful in tests with port 0).
func (s *Server) Addr() string {
	if s.ln == nil {
		return ""
	}
	return s.ln.Addr().String()
}

func (s *Server) handleConn(conn net.Conn) {
	defer conn.Close()
	r := resp.NewReader(conn)
	w := resp.NewWriter(conn)
	for {
		v, err := r.ReadValue()
		if err != nil {
			if err != io.EOF {
				log.Printf("conn %s: read: %v", conn.RemoteAddr(), err)
			}
			return
		}
		reply := s.dispatch(v)
		if err := w.WriteValue(reply); err != nil {
			return
		}
		if err := w.Flush(); err != nil {
			return
		}
	}
}

// dispatch turns one decoded request into one reply.
func (s *Server) dispatch(v resp.Value) resp.Value {
	args := flatten(v)
	if len(args) == 0 {
		return resp.Error("ERR empty command")
	}
	h, ok := command.Lookup(args[0])
	if !ok {
		return resp.Error(fmt.Sprintf("ERR unknown command '%s'", strings.ToUpper(args[0])))
	}
	reply, err := h(s.store, args[1:])
	if err != nil {
		return resp.Error(err.Error())
	}
	return reply
}

// flatten converts a decoded request (array of bulk strings, or an inline
// command already decoded as an array) into a []string.
func flatten(v resp.Value) []string {
	if v.Kind != resp.KindArray {
		return nil
	}
	args := make([]string, 0, len(v.Array))
	for _, e := range v.Array {
		if e.Kind != resp.KindBulk {
			return nil
		}
		args = append(args, e.Str)
	}
	return args
}
```

main.go:

```go
package main

import (
	"flag"
	"log"
	"os"
	"os/signal"
	"syscall"

	"github.com/linkxzhou/miniredis/internal/server"
)

func main() {
	port := flag.Int("port", 6379, "TCP port to listen on")
	flag.Parse()

	srv := server.New(server.Options{})
	if err := srv.Listen(fmt.Sprintf("127.0.0.1:%d", *port)); err != nil {
		log.Fatalf("listen: %v", err)
	}
	log.Printf("miniredis listening on %s", srv.Addr())

	go func() {
		sig := make(chan os.Signal, 1)
		signal.Notify(sig, os.Interrupt, syscall.SIGTERM)
		<-sig
		srv.Close()
	}()

	if err := srv.Serve(); err != nil {
		log.Printf("server stopped: %v", err)
	}
}
```

Bind to 127.0.0.1 or 0.0.0.0? For a learning server, 127.0.0.1 is safer. CodeCrafters binds 0.0.0.0. I'll default 127.0.0.1 and note it. Actually make it a flag: -addr? Keep -port and bind 127.0.0.1. Fine.

server_test.go — integration test:

```go
func TestServerPingEcho(t *testing.T) {
	srv := server.New(server.Options{})
	if err := srv.Listen("127.0.0.1:0"); err != nil { t.Fatal(err) }
	go srv.Serve()
	defer srv.Close()

	conn, err := net.Dial("tcp", srv.Addr())
	...
	w := resp.NewWriter(conn)
	r := resp.NewReader(conn)

	// PING
	w.WriteValue(resp.Array(resp.Bulk("PING")))
	w.Flush()
	v, err := r.ReadValue()
	// expect +PONG

	// ECHO hello
	...
	// unknown command
	...
}
```

Also command-level unit tests for ping/echo (wrong arg count).

Also a test using inline protocol: send "PING\r\n" raw → +PONG.

Now README.md — milestones in Chinese (user speaks Chinese). Include:

```
# miniredis — 从零实现 Redis（Go）

学习项目：用 Go 从零实现一个支持 RESP 协议、过期、持久化、复制与 Streams 的迷你 Redis。

## 快速开始
make run            # 或 go run ./cmd/miniredis -port 6379
redis-cli -p 6379 PING
# 没有 redis-cli 时：
printf 'PING\r\n' | nc 127.0.0.1 6379

make test

## 目录结构
cmd/miniredis/     入口：flag 解析、信号处理
internal/resp/     RESP2 编解码（协议层）
internal/command/  命令注册表与实现
internal/store/    内存存储（数据层）
internal/server/   TCP accept 循环与连接处理

## 里程碑
### M0 ✅ 项目骨架（本次完成）
- TCP 服务器 + 每连接一个 goroutine
- RESP2 编解码（数组/批量字符串/简单串/错误/整数/NULL，支持 inline 命令）
- 命令注册表 + PING/ECHO 参考实现
- 单元测试 + TCP 集成测试
验收：make test 通过；redis-cli PING 返回 PONG

### M1 数据命令与并发存储（你的第一个练习）
- 实现 SET / GET / DEL / EXISTS / KEYS（在 internal/command 下新建文件，Register 注册即可）
- 思考点：锁粒度、GET 不存在时返回 $-1（resp.Null()）
验收：redis-cli 读写一致；-race 下 go test ./... 通过

### M2 过期机制
- SET key val EX/PX、EXPIRE / PEXPIRE / TTL / PTTL
- 惰性删除（读时检查）+ 定期抽样删除（后台 goroutine）
验收：TTL 递减、过期后 GET 返回 nil

### M3 持久化
- AOF：每条写命令追加日志，启动重放；可选 BGREWRITEAOF
- 或 RDB：定时快照（二进制编码 + CRC64）
验收：kill -9 后重启数据仍在

### M4 复制
- REPLICAOF host port；主从握手（PING/REPLCONF/PSYNC）
- 主机命令传播 + 复制积压缓冲区；WAIT
验收：从库能读到主库写入；断线重连部分重同步

### M5 Streams
- XADD / XLEN / XRANGE / XREAD（含 BLOCK 阻塞读）
- 思考点：entry ID 生成（seq 自动递增）、阻塞唤醒（channel 通知）
验收：XREAD BLOCK 在新消息到达时立即返回

### M6 收尾打磨
- go test -race 全绿；基准测试（go test -bench）
- 用真实 redis-cli / redis-benchmark 做兼容性冒烟
- README 记录设计取舍

## 学习建议
每个里程碑：先写测试（协议/行为预期）→ 实现 → make test → 用 redis-cli 手工验证。
```

That's a solid README. Keep it reasonably concise.

Makefile:
```make
.PHONY: build run test vet

build:
	go build -o bin/miniredis ./cmd/miniredis

run:
	go run ./cmd/miniredis -port 6379

test:
	go test ./...

vet:
	go vet ./...
```

.gitignore:
```
bin/
*.test
```

Now — process. The instructions say: explore before modifying code, plan for multi-step changes. Workspace is empty; exploration is trivial but I should still record it. Then plan with seed_todos, then execute, then verify (go build, go vet, go test, smoke test with printf | nc).

Let me also verify Go version compatibility: go 1.26.1, go.mod `go 1.26` — fine. Actually use `go 1.25` or `1.26`? go.mod directive should be ≤ installed. `go 1.26` works with go1.26.1. Hmm, but toolchain directive... plain `go 1.26` is fine.

Module path: `github.com/linkxzhou/miniredis`. 

One more consideration: should tests use the resp package for building requests (circular-ish but fine — tests import internal/resp, no cycle). Yes fine.

Smoke test after build: run server in background, `printf 'PING\r\n' | nc 127.0.0.1 6379` expect `+PONG`, and a RESP array PING via printf '*1\r\n$4\r\nPING\r\n' | nc. Also test with redis-cli if installed (check `which redis-cli`). Then kill server.

Also `go vet ./...`.

Edge: In dispatch, unknown command error message — real Redis: "ERR unknown command 'FOO', with args beginning with: ...". Keep simple version.

ECHO wrong args error: real Redis returns wrong number of arguments error. Fine.

One subtlety in ReadValue for inline: `strings.Fields` splits on any whitespace. Real Redis inline commands split on spaces/tabs. Fine.

Another subtlety: readLine for '+' simple strings etc. — line could contain \r stripped. Good.

For bulk read: `io.ReadFull(r.br, buf)` where buf is n+2 bytes; then verify buf[n] == '\r' && buf[n+1] == '\n'? Real protocol requires CRLF. For robustness, check and error if mismatch. Cheap, include it.

Also cap bulk size to avoid memory bombs? Real Redis has proto-max-bulk-len (512MB). Add a check: if n > 512<<20 → error. One line, worth it for safety. Include.

Now, about parallel tool calls: first explore (record), then plan. Actually explore tool "consolidates" findings — I've already listed the dir (empty) and checked go version. I can call explore and plan in sequence. The instructions: explore once before modifying; plan for multi-step. Let me do explore + plan in one message? They're independent (plan doesn't depend on explore output). But conceptually plan should follow exploration. I can call both in parallel since I already know the workspace is empty. To be safe and efficient: call explore and plan together, then todo_write, then create files in parallel batches, then verify.

Actually todo_write with seed_todos=true in plan already seeds todos. So: explore + plan (parallel) → write files (parallel batches) → verify (build/vet/test) → smoke test → final summary.

Let me also think: does the user want ME to implement everything, or scaffold for THEIR learning? "请先帮我规划里程碑并创建最小项目骨架" — plan milestones and create minimal skeleton. So skeleton now; they implement milestones. My README should make each milestone actionable with pointers to files. Good.

File list to create:
1. go.mod
2. Makefile
3. .gitignore
4. README.md
5. cmd/miniredis/main.go
6. internal/resp/resp.go
7. internal/resp/resp_test.go
8. internal/command/command.go (registry + ping + echo in one file? or registry.go + ping.go) — keep two files: registry.go, builtin.go. Actually minimal: one file `command.go` with registry + PING/ECHO. Hmm, separation aids learning: registry.go (mechanism) vs commands.go (examples). I'll do registry.go and commands.go.
9. internal/store/store.go
10. internal/server/server.go
11. internal/server/server_test.go

11 files. Reasonable for a skeleton.

Let me now write all the code carefully, double-checking compile-ability mentally.

resp.go — imports: bufio, errors, fmt, io, strconv, strings. All used? errors: used in readLine (errors.New). fmt: yes. io: ReadFull, EOF. strconv: yes. strings: TrimSuffix, Fields, ToUpper? ToUpper used in command package. OK.

In readLine, careful: `if err != nil { if errors.Is(err, io.EOF) && line != "" { return "", errors.New(...) } return "", err }`. ReadString returns io.EOF exactly. Fine.

Wait, one more: in ReadValue, `line[0]` — line could be empty? readLine returns "" only when...? If client sends just "\r\n" → line = "" after trim. Then line[0] panics! Guard: if line == "" → treat as empty inline command → return Array() (empty array) or skip? Real Redis: empty inline command returns... it just ignores? For safety: if line == "" { return Array(), nil } — dispatch handles empty args with "ERR empty command"... Hmm, real Redis returns nothing for empty inline? Actually it responds with error? Let me not overthink: return an empty array; server replies ERR empty command. Hmm, that would make `printf '\r\n' | nc` return an error — acceptable. Alternatively skip empty lines silently (continue loop). Redis actually ignores empty inline commands (no reply). To mimic: in handleConn, if len(args)==0 → continue without reply. That's closer to real Redis. I'll do that: dispatch only when args non-empty, else continue. And ReadValue returns Array{} for empty line. 

But careful: infinite loop risk? No — each iteration reads a new line; empty lines just consume input.

So handleConn:
```go
args := flatten(v)
if len(args) == 0 {
    continue
}
```

And remove "ERR empty command".

resp_test.go tests:

```go
func TestDecode(t *testing.T) {
	tests := []struct{
		name string
		in   string
		want Value
	}{
		{"array of bulk", "*2\r\n$4\r\nECHO\r\n$5\r\nhello\r\n", Array(Bulk("ECHO"), Bulk("hello"))},
		{"inline command", "PING\r\n", Array(Bulk("PING"))},
		{"inline with args", "SET key value\r\n", Array(Bulk("SET"), Bulk("key"), Bulk("value"))},
		{"simple string", "+OK\r\n", SimpleString("OK")},
		{"error", "-ERR bad\r\n", Error("ERR bad")},
		{"integer", ":42\r\n", Integer(42)},
		{"bulk with space", "$3\r\na b\r\n", Bulk("a b")},
		{"null bulk", "$-1\r\n", Null()},
		{"null array", "*-1\r\n", Null()},
		{"empty line", "\r\n", Array()},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got, err := NewReader(strings.NewReader(tt.in)).ReadValue()
			if err != nil { t.Fatalf("decode: %v", err) }
			if !reflect.DeepEqual(got, tt.want) { t.Fatalf("got %+v, want %+v", got, tt.want) }
		})
	}
}
```

Wait "empty line" case: readLine returns "" → ReadValue returns Array() (empty). DeepEqual(Array(), Value{Kind: KindArray, Array: nil})? Array() returns Value{Kind: KindArray, Array: nil} since variadic with no args → nil slice. And readArray with n=0 returns make([]Value,0,0) which is non-nil empty slice — DeepEqual(nil slice, empty slice) is false! Careful. For "empty line" I return `Value{Kind: KindArray}` directly (Array field nil). Let me make ReadValue's empty-line branch return `Value{Kind: KindArray}`. And in test want: `Value{Kind: KindArray}`. OK. Or avoid that test case. I'll include it with explicit Value{Kind: KindArray}.

Also errors test: truncated bulk `$5\r\nhi` → error. Bad length `$x\r\n` → error. Add a decode-error table.

I was in the middle of executing the task. The previous response was truncated — it seems I had written out my thinking about the plan and code, but the actual tool calls and file creation may not have completed. Let me check the current state of the workspace to see what was actually created, then continue from there.

The last visible content was my internal reasoning about resp_test.go. I need to check what files actually exist now, then continue creating the remaining files and verify.Workspace is still empty — the truncation happened before any files were written. Starting execution now: recording exploration + plan, then creating the skeleton.Now create the files. I'll batch independent writes in parallel. First batch: go.mod, Makefile, .gitignore, README.md. Second batch: source files. Actually all writes are independent — but to keep message sizes manageable, I'll do 2-3 batches.

Batch 1: go.mod, Makefile, .gitignore, cmd/miniredis/main.go, internal/store/store.go.Batch 2: RESP codec, its tests, and the command package.Batch 3: server, server test, README.The server.go write got corrupted (stray labels, dead code, missing import). Rewriting it cleanly.接下来是包含里程碑计划的 README，然后进行验证。`Value` 包含一个 slice 字段，因此无法使用 `==` 进行比较。我正在修复测试以使用 `reflect.DeepEqual`。The empty-line edge case I planned a guard for never made it into the code — `line[0]` panics on `""`. Fixing:全部通过。现在进行一次实时冒烟测试：启动服务器，通过 `nc` 发送 inline 和 RESP-array PING，以及一个未知命令，然后关闭它。`nc` 在 stdin EOF 后会挂起（服务器保持连接开启）。我先清理掉所有残留的服务器进程，并使用一个确定性的 Python socket client 代替。二进制文件运行正常——之前超时运行产生的服务器仍然占用了 16379 端口。我来终止它并使用一个新的端口。"permission denied" — odd. The previous command with pkill + background + heredoc worked partially before (the first one timed out, second gave bind error). Now "permission denied" with no output. Maybe pkill killed something it shouldn't, or the sandbox denies pkill? Actually the second command ran `pkill -f 'bin/miniredis' 2>/dev/null; sleep 0.3` and then worked (gave bind: address already in use — meaning pkill didn't kill it? or it did and the old one was still there...). Actually the second command's output showed the server DID start and log the bind error — so pkill may have failed silently.

Now "permission denied" — possibly pkill returning non-zero and the shell... no, that wouldn't produce "permission denied" as the whole result. Maybe the sandbox blocks pkill (killing processes outside session). Let me avoid pkill; find the PID via lsof and kill only that, or just use another port and leave the stale server (it'll die eventually — better to clean up though).

Let me try: use port 16381, and separately try to kill the stale one with lsof+kill.Smoke test passes:
- inline PING → +PONG
- RESP array ECHO → $5\r\nhello\r\n
- unknown → -ERR unknown command 'NOSUCH'
- empty line followed by PING → +PONG (empty line ignored, then PING answered)

All verification done: build, vet, test -race, live smoke. Mark todo s6 complete and summarize.

Let me also double check the final file tree for the summary. Files:
- go.mod, Makefile, .gitignore, README.md
- cmd/miniredis/main.go
- internal/resp/resp.go, resp_test.go
- internal/command/registry.go, commands.go
- internal/store/store.go
- internal/server/server.go, server_test.go

One more check: the earlier corrupted server.go write was overwritten cleanly — verified by build passing. Good.

Final summary: concise, lead with what was delivered, milestones table, how to run, next step (M1 as first exercise).骨架已建好并全部验证通过：`go build` / `go vet` / `go test -race` 全绿，真实 TCP 冒烟测试确认 inline PING → `+PONG`、RESP 数组 ECHO → `$5\r\nhello\r\n`、未知命令 → `-ERR unknown command`。

## 里程碑（详见 README.md）

| 里程碑 | 内容 | 验收标准 |
|---|---|---|
| M0 ✅ | TCP 服务器 + RESP2 编解码 + 命令注册表 + PING/ECHO | `make test` 全绿，redis-cli PING 通 |
| M1 | SET/GET/DEL/EXISTS/KEYS（你的第一个练习） | redis-cli 行为一致，`-race` 通过 |
| M2 | 过期：EX/PX、EXPIRE/TTL、惰性+定期删除 | TTL 递减，过期后 GET 返回 nil |
| M3 | 持久化：AOF 追加重放（或 RDB 快照） | `kill -9` 后重启数据仍在 |
| M4 | 复制：REPLICAOF、握手、命令传播、WAIT | 从库读到主库全部数据 |
| M5 | Streams：XADD/XRANGE/XREAD（含阻塞） | BLOCK 读在新消息到达时立即返回 |
| M6 | 打磨：基准测试、redis-benchmark 兼容冒烟 | 全绿 + 设计取舍记录 |

## 项目结构

```
cmd/miniredis/      入口：flag、信号处理、优雅关闭
internal/resp/      RESP2 编解码（含 inline 命令、截断/超长防护）
internal/command/   Register(name, handler) 注册表 + PING/ECHO 参考实现
internal/store/     RWMutex 保护的内存 map（M2/M3 的扩展点）
internal/server/    accept 循环、每连接 goroutine、命令分发
```

核心扩展点在 `internal/command/registry.go:24`：新增命令 = 写一个 `Handler` 函数 + 一行 `Register`，照着 `internal/command/commands.go` 里的 PING/ECHO 抄即可。

## 运行

```sh
make run        # 监听 127.0.0.1:6379
make test       # 单元 + TCP 集成测试
```

M1 是留给你的第一个练习：新建 `internal/command/kv.go`，实现 SET/GET/DEL 并注册，GET 不存在的 key 记得返回 `resp.Null()`（`$-1`）。README 里每个里程碑都附了思考点（锁粒度、TTL 语义、AOF 格式等），建议按「先写测试 → 实现 → redis-cli 手工验证 → 与真 Redis 对比字节输出」的节奏推进。