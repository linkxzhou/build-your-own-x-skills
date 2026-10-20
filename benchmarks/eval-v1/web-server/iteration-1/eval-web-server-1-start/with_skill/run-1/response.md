The user wants to write their own HTTP server from raw sockets in Python, and wants coaching. This matches the build-your-own-x skill — "a web server" is explicitly named. I must read the SKILL.md first before doing anything else.The file was truncated. I need to read the rest of it, and find the category slug for "web server". Let me read more of the SKILL.md and also look at the skills directory.The slug is `web-server`. Reading the track skill now — it's mandatory before anything else.The track skill was truncated. Let me read the rest of it (lines 47+). Also there's a per-tutorial skill `web-server-web-ruslanspivak-lsbaws-part1` which is Python raw sockets — that matches perfectly. Let me read the rest of the track skill and check the tutorials reference.Track skill read. The learner's request (Python, raw sockets) maps directly to Ruslan Spivak's "Let's Build A Web Server" — there's a per-tutorial skill for it. Reading it, and checking the workspace state in parallel.The per-tutorial skill references a `references/tutorial-map.md`. Let me read it.Track skill and per-tutorial skill are read. Scope is already settled by your request: Python, raw sockets, stdlib only. I'll set up the coaching plan, scaffold the workspace, then hand you milestone 1.Where we are: **Milestone 1/7 — TCP listener.** Scaffold is ready in `httpserver/`: `server.py` with TODOs, `PROGRESS.md` to log checkpoints. Guide: Ruslan Spivak, [Let's Build A Web Server. Part 1](https://ruslanspivak.com/lsbaws-part1/) — worth skimming after each milestone.

**The concept.** An HTTP server is a loop over TCP connections. `socket()` creates an endpoint, `bind()` claims an address, `listen()` turns it into a queue of pending connections, and `accept()` blocks until a client connects, handing you a new socket for that conversation. HTTP rides on top: the client sends a request as bytes, you send back a response as bytes. The wire format is plain text with `\r\n` line endings and a blank line separating headers from body — that's the whole magic.

**What to write next** — two functions in `httpserver/server.py`:

1. `main()`: create the socket (`AF_INET` + `SOCK_STREAM`), set `SO_REUSEADDR`, bind to `(HOST, PORT)`, `listen()`, then `while True:` accept and call `handle_connection(conn, addr)`.
2. `handle_connection()`: one `conn.recv(1024)` to drain the request (parsing comes in M2), then `conn.sendall()` the exact response bytes from the TODO comment, then `conn.close()`.

The response must be byte-exact: status line, one `Content-Length` header matching the body, blank line, body. Getting `Content-Length` right by hand once is the point — it's what lets `curl` know where the response ends.

**How to check it:**

```
python3 httpserver/server.py        # terminal 1
curl -v http://127.0.0.1:8080/      # terminal 2
```

Expected: `HTTP/1.1 200 OK`, `Content-Length: 13`, and `Hello, world!` in the body. Use `127.0.0.1`, since `localhost` can resolve to `::1` and miss your IPv4 socket.

Write it, run the check, and paste whatever `curl -v` prints — including the request bytes curl shows you sending. That output is the raw material for Milestone 2. If it hangs or errors, paste that instead and we debug from the real output.