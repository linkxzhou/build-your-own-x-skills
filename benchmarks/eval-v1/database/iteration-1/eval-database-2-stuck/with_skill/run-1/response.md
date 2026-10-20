The user has a toy Redis in Go. They accept connections in a loop and call handle(conn) directly (synchronously). The first client blocks the accept loop, so the second client connects (TCP backlog accepts the connection at kernel level) but never gets served — it hangs.

This is a conceptual question, not a code change request. The fix: run handle in a goroutine: `go handle(conn)`. Also mention closing conn in handler, and maybe mention that Redis itself is single-threaded but multiplexes via event loop; in Go the idiomatic way is goroutine per connection.

Should I use tools? The user didn't provide code files. Maybe check workspace for their project? The instructions say explore before modifying code, but this is a question — no code modification. I could quickly glob for Go files to see if their project is in the workspace. That could be helpful but might be unnecessary. The question is answerable directly. Let me check if there's a workspace with their code — a quick glob is cheap and lets me reference their actual code if present.

Let me do a quick glob for **/*.go. If found, read the main file. If not, answer directly.

Actually the tone guidance: lead with the answer. Keep it tight. Let me glob first.`handle(conn)` runs synchronously inside the accept loop, so the loop is stuck inside the first client's handler until that client disconnects. The second `redis-cli` completes its TCP handshake (the kernel does that via the listen backlog, before your program accepts anything), so the client believes it's connected — then it blocks forever on read, because your server never calls `Accept` again to get its connection.

Fix: serve each connection in its own goroutine.

```go
for {
    conn, err := ln.Accept()
    if err != nil {
        log.Println("accept:", err)
        continue
    }
    go handle(conn)
}
```

and inside `handle`:

```go
func handle(conn net.Conn) {
    defer conn.Close()
    // read/parse/reply loop
}
```

Two things to keep in mind as you grow it:

- Goroutines are cheap; this is the idiomatic Go equivalent of Redis's event loop — one flow of execution per client, blocking I/O per connection.
- Once handlers run concurrently, any shared state (your key/value map) needs synchronization. A single `sync.Mutex` around map access is the right toy-level answer, and it preserves Redis's serial-per-command semantics.