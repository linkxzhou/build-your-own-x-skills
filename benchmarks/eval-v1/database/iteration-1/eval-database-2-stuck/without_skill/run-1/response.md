The user has a classic bug: single-threaded accept loop calling handle(conn) synchronously, so the second connection blocks until the first client disconnects. This is a conceptual question — no files to read necessarily. Let me check if there's actual code in the workspace to reference. The cwd is "build-your-own-x-database-2" — maybe there's a Redis implementation there. Let me quickly glob for Go files to see if I can point at their actual code.

Actually, the question is "Why?" — a conceptual answer. But if their code is in the workspace, I should look at it and give a concrete fix. Let me check quickly.`handle(conn)` runs inline in the accept loop, so the loop stays inside `handle` until the first client disconnects. Only then does control return to `Accept()`. The second client's TCP connection is accepted by the kernel (it sits in the listen backlog), but your code never reads from it — redis-cli sends its command and blocks forever waiting for a reply.

Fix: handle each connection in its own goroutine.

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

Two things to watch once you do this:

- Any state shared between connections (your key-value map, counters) now needs synchronization — a `sync.RWMutex` around the map, or you'll get data races. Run with `go run -race .` to catch them.
- If you later add persistence (AOF-style appends), serialize writes to the file with a mutex too, since multiple goroutines will write concurrently.