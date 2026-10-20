The user wants to write their own HTTP server from raw sockets in Python, and wants coaching. This matches the build-your-own-x skill — "a web server" is explicitly listed. I must read the SKILL.md first before doing anything else.The SKILL.md was truncated. Let me read the rest of it, and also find the track skill for web server. The topic is "web server" — I need to map to a category slug. Let me read the rest of the SKILL.md first and look at the skills directory.Topic mapped: `web-server`. Reading the mandatory track skill now.Truncated again. Let me read the rest of the track skill.Now the tutorials reference to pick the right guide and get its exact link.The learner's ask maps cleanly to Python + raw sockets. The closest upstream guide is Ruslan Spivak's "Let's Build A Web Server" (lsbaws part 1), which has a per-tutorial skill. Let me read it and check the workspace state in parallel.The per-tutorial skill points to a `references/tutorial-map.md`. Let me read it before scaffolding.I have everything I need. Now, per the track skill's coaching workflow:

1. **Agree on scope** — language is already settled (Python, raw sockets — the learner said so). Target: I should propose the milestone list and checks, and ask at most 2 questions. The skill says "Ask at most 2 questions, and suggest a default if the learner doesn't care."

2. **Pick a guide** — Ruslan Spivak's "Let's Build A Web Server" part 1: https://ruslanspivak.com/lsbaws-part1/ — exact link. Credit it.

3. **Work milestone by milestone** — start milestone 1 in the learner's workspace.

The coaching rules:
- Never dump the whole project. Give full code only for the current milestone, and only when asked or after the learner has tried.
- Teaching loop: explain concept in 3-6 sentences → show interface/skeleton → learner writes core → run check → debug → recap.
- Output for each turn: Where we are (milestone N/total), the concept (short), what to write next (skeleton/TODO, not full answer), how to check it (command + expected output — every reply ends with this), stuck? one hint at a time.
- Stay in workspace, never install anything. Python 3.14.7 is available — good, no installs needed.
- When a milestone passes, record in PROGRESS.md.

The workspace is empty (just .agents and AGENTS.md). So we start from an empty directory.

Scope agreement: The skill says ask at most 2 questions and suggest a default. The learner already said: Python, raw sockets, HTTP server. That's quite specific. I could just propose the default scope and start milestone 1, letting them redirect. The skill says "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care."

I think the best move: propose the target ("a Python HTTP server on raw sockets that serves static files, routes, and handles concurrency"), show the 7-milestone plan (from the track skill table), and start milestone 1 immediately with the concept + skeleton + check. That respects "start milestone 1 in the learner's workspace" from the router skill's workflow step 3: "Then start milestone 1 in the learner's workspace."

Should I ask questions first? The learner was specific: "my own HTTP server from raw sockets in Python". Language: Python. Target: HTTP server from raw sockets. The only open question is how far to go (through concurrency? middleware?). The track skill default: raw sockets in Python, then a small framework. I'll propose the full milestone list as the default and let them trim. Asking 2 questions and waiting would slow things down; the skill says suggest a default if the learner doesn't care — they clearly care about the core (raw sockets), so I'll present the plan and dive into milestone 1. That matches "start milestone 1 in the learner's workspace."

Now, milestone 1: TCP listener. Core concepts: sockets, accept loop. Checkpoint: `curl -v localhost:8080` connects and gets a hard-coded 200 response.

Teaching loop for milestone 1:
1. Explain the concept in 3-6 sentences: what a socket is, bind/listen/accept, the accept loop, and that HTTP is just text over TCP.
2. Show the interface or skeleton — NOT the full solution. The learner writes the core.
3. Let the learner write the core.

Per "Do not dump a full solution. Give complete code only for the current milestone, and only when asked, or after the learner has tried." — So for milestone 1, I give a skeleton with TODOs, and the learner fills in the core.

The output format for each turn:
- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton or TODO list, not the full answer
- How to check it: command + expected output (every reply ends with this)

Also per the router skill: "Agree on scope... Then start milestone 1 in the learner's workspace." I can create the project directory and a skeleton file with TODOs. Should I write the skeleton file to the workspace? The skill says "Give an interface or skeleton" and "Stay in the learner's workspace. Keep scratch files inside the project". Writing a skeleton file with TODOs into the workspace seems right — the learner fills in the core. Let me create `http-server/` directory with `server.py` skeleton containing TODOs, and maybe PROGRESS.md to track milestones.

Actually, let me be careful: "Never dump the whole project" — a skeleton with TODOs is fine. The learner writes the core (the socket calls).

Let me design the milestone 1 skeleton:

```python
"""Milestone 1: a TCP listener that answers one hard-coded HTTP response."""
import socket

HOST, PORT = "127.0.0.1", 8080

def run(host: str = HOST, port: int = PORT) -> None:
    # 1. Create a TCP socket (AF_INET + SOCK_STREAM)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 2. Allow quick restarts: set SO_REUSEADDR
    # TODO
    # 3. Bind to (host, port), then listen()
    # TODO
    print(f"Serving on http://{host}:{port}")
    while True:
        # 4. Block until a client connects: conn, addr = server.accept()
        # TODO
        # 5. Read up to 1024 bytes from conn (the raw HTTP request)
        # TODO
        # 6. Send a hard-coded HTTP/1.1 200 response, then close conn
        # TODO
        pass

if __name__ == "__main__":
    run()
```

Hmm, but should I give even the socket.socket line? The concept explanation covers it. I think a skeleton with numbered TODOs and the first line done is good scaffolding — the learner writes the core (bind/listen/accept/recv/send/close).

Also the hard-coded response — I should explain what a minimal valid HTTP response looks like:

```
HTTP/1.1 200 OK
Content-Type: text/plain
Content-Length: 13

Hello, world!
```

Note: the blank line separates headers from body, and Content-Length must match the body byte count. That's a key learning point. I'll explain it but let them write it.

Checkpoint command: `curl -v localhost:8080` → expect `HTTP/1.1 200 OK` and `Hello, world!`. Also `python3 server.py` runs without error.

Also mention: needs a free local port only (OS limits note from skill — "Name any OS limits up front (needs a free local port only)"). Port 8080 on localhost, no admin rights needed since >1024.

Also credit the upstream tutorial with exact link: https://ruslanspivak.com/lsbaws-part1/ — "Let's Build A Web Server" by Ruslan Spivak. I'll mention we'll loosely follow it (his part 1 does exactly this: accept loop, hard-coded response, then serving files). Also mention aosabook 500L "A Simple Web Server" as a secondary reference? The skill says pick ONE guide. I'll pick Spivak's and mention it. Maybe mention that later milestones (static files) draw from joaoventura's post... no — keep it to one guide per the skill. Spivak part 1 covers the accept loop and hard-coded response; part 2 covers serving files via WSGI-ish. Our milestone list extends beyond, which is fine — the track skill owns milestones.

Scope questions: The skill says ask at most 2 questions. I'll fold scope into a single confirmable default: "Default plan below — say 'go' or trim it." Actually I shouldn't create a conditional next-step menu ("if you want, I can..."). I'll state the plan as the default and start milestone 1; the learner can redirect. That's taking the action directly.

Now — should I use plan/todo tools? The developer instructions say: for any multi-step change, call `plan` with 3-7 steps and seed_todos=true. This is a multi-milestone coaching engagement. The plan tool is for "BEFORE editing code". I'm about to write a skeleton file. The milestones are already defined by the track skill. Creating a plan.json with the 7 milestones would be reasonable and seed todos. But the skill's own workflow (milestone table + PROGRESS.md) already tracks this. Hmm. The developer instruction is fairly strong: "For any multi-step change (>1 file, >1 logical action, or touching config/tests), call plan". I'm writing 2 files (server.py skeleton, PROGRESS.md). I'll call plan with the milestone steps, seed_todos=true. That also gives the learner a visible roadmap. It's cheap and aligns.

Also `explore` — "Before modifying code, call explore once to record the files you have read". I've read the skill files; the workspace is empty. The explore tool says to record files read and findings. I've effectively done the exploration (workspace empty, Python 3.14.7 present). Calling explore once to consolidate is per instructions. It's a bit ceremonial here, but the instructions say to do it before modifying code. I'll do a quick explore call, then plan, then write the skeleton + PROGRESS.md, then reply with the coaching turn.

Wait — order: explore (consolidate findings) → plan (blueprint, seed todos) → write files → reply. The reply itself must follow the track skill's output format and end with the check command.

Let me also think about what the skeleton should contain vs. what the learner writes. Milestone 1 core concepts: sockets, accept loop. The learner should write: SO_REUSEADDR, bind, listen, accept loop, recv, send, close. I'll leave those as TODOs. I'll provide the response template as a comment? Hmm — the hard-coded response is part of the learning (HTTP is text). I'll leave a TODO for building the response too, but explain the shape in prose (status line, headers, blank line, body; Content-Length must match). Actually, to keep milestone 1 truly small, I can give them the exact response bytes in the explanation prose and let them wire it in. The skill says "Show the interface or skeleton. Let the learner write the core." The core of milestone 1 is the socket lifecycle. The response text I can show in prose as "what a minimal HTTP response looks like" — that's concept explanation, fine.

One more consideration: Python 3.14 — nothing exotic needed; plain socket module works.

Also: should the server handle one connection at a time? Yes for milestone 1 — sequential accept loop. Concurrency is milestone 5. Good.

Edge: curl sends the request and waits; if we recv once and respond, fine. curl -v will show the response. Also note: after sending, close. If they forget Content-Length, curl may hang waiting for body end or close-delimited body — actually with Connection: close semantics, curl handles EOF-terminated bodies. But teaching Content-Length early is good hygiene. I'll mention the blank line + Content-Length point in the concept.

Now the files:

`http-server/server.py`:

```python
"""Build-your-own HTTP server — milestone 1: TCP listener.

Goal: accept one connection at a time and reply with a hard-coded
HTTP 200 response. No parsing yet — that's milestone 2.
"""
import socket

HOST = "127.0.0.1"
PORT = 8080

# A minimal, valid HTTP/1.1 response. Note the blank line between
# headers and body, and that Content-Length must equal the body size.
RESPONSE = b""  # TODO(milestone 1): build the raw response bytes


def run(host: str = HOST, port: int = PORT) -> None:
    # AF_INET = IPv4, SOCK_STREAM = TCP
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO 1: set SO_REUSEADDR so restarting the server doesn't hit
    #         "Address already in use" while the old socket lingers.
    # TODO 2: bind the socket to (host, port)...
    # TODO 3: ...and mark it passive with listen().
    print(f"Serving on http://{host}:{port}")

    while True:
        # TODO 4: block until a client connects -> (conn, addr)
        # TODO 5: read the client's request bytes (one recv is fine here)
        # TODO 6: send RESPONSE on conn, then close conn
        break  # remove once the loop body is real

    server.close()


if __name__ == "__main__":
    run()
```

Hmm, the `break` placeholder is a bit awkward but keeps the file runnable-ish (it exits immediately). Actually if they run it before filling TODOs, it prints "Serving on..." and exits — confusing? It's fine; the TODOs are clear. Alternatively leave `pass` in the loop → infinite busy loop, bad. `break` is safer. Or I could make the loop body raise NotImplementedError. Hmm, `raise NotImplementedError("milestone 1 TODOs")` inside the loop is clearer: run it → crash with a clear message. But then the accept hasn't happened. Simplest: keep `break` with the comment. Actually let me use NotImplementedError — it's the standard skeleton idiom and fails loudly:

```python
    while True:
        # TODO 4..6
        raise NotImplementedError("fill in TODOs 4-6")
```

Wait, but then TODO 1-3 also unimplemented → bind never happens, prints "Serving on" then raises. Fine and loud.

Hmm, actually — maybe cleaner: put the raise before the print? No. Keep it simple.

`http-server/PROGRESS.md`:

```markdown
# Progress

| # | Milestone | Check | Status |
|---|-----------|-------|--------|
| 1 | TCP listener | `curl -v localhost:8080` → hard-coded 200 | in progress |
| 2 | HTTP parsing | parser unit tests on fixtures; malformed → 400 | pending |
| 3 | Static files | serves /index.html; /../etc/passwd → 403/404 | pending |
| 4 | Routing + handlers | GET /users/42 → {"id": 42}; wrong method → 405 | pending |
| 5 | Concurrency + keep-alive | load script completes with no errors | pending |
| 6 | Middleware / mini-framework | logging + JSON middleware compose | pending |
| 7 | Stretch: WebSockets | browser echo works | pending |
```

Guide credit: Ruslan Spivak, "Let's Build A Web Server. Part 1." https://ruslanspivak.com/lsbaws-part1/

Now the reply structure per the track skill "Output for each turn":
- Where we are: milestone 1/7
- The concept: short (3-6 sentences on sockets/accept loop/HTTP-as-text)
- What to write next: the TODOs (skeleton already written to workspace)
- How to check it: command + expected output — must end the reply
- Stuck? one hint at a time (only when stuck)

Also scope agreement: state the target in one line: "A single-file Python HTTP server on raw sockets: parses requests, serves static files safely, routes, survives concurrent load; stretch: WebSockets." And note the guide. Keep it tight.

Tone rules: no filler, no "Let's dive in", no summary stamps, no conditional menus. End with the check command. Also "Every reply ends with this" — the check command and expected output.

Concept explanation (3-6 sentences): A TCP socket is one endpoint of a byte pipe. A server creates a listening socket with socket(AF_INET, SOCK_STREAM), binds it to an address, and listen() marks it passive. accept() blocks until a client connects and returns a new connected socket dedicated to that client — the listening socket keeps accepting. HTTP is plain text on top of that pipe: a request like `GET / HTTP/1.1\r\nHost: ...\r\n\r\n`, and a response with a status line, headers, a blank line, then the body. For milestone 1 we ignore the request entirely and always send the same bytes.

That's the right depth. The `\r\n` detail matters — curl is lenient but real HTTP uses CRLF; worth one sentence since it's a classic gotcha (b"\r\n" not "\n").

Skeleton: I show the file path and say TODOs 1-6 are yours. Don't paste the whole skeleton in the reply (it's in the workspace; the reply should stay high-signal). Actually showing the TODO list in the reply is useful — the skill says "What to write next: a skeleton or a TODO list". I'll list the 6 TODOs compactly.

Check command:
```
python3 http-server/server.py        # terminal 1
curl -v localhost:8080               # terminal 2
```
Expected: `HTTP/1.1 200 OK` in the curl output, body `Hello, world!`, and the server keeps running (loop returns to accept).

Also OS limits note: needs only a free local port (8080); no admin rights. One line.

Now the tool sequence: explore → plan (seed_todos) → write 2 files → final reply. explore and plan are independent? plan doesn't depend on explore's output technically, but instructions say explore before modifying code, plan before editing code. I can call explore and plan in parallel in one block, then write files. Actually plan should reflect exploration findings... I already have the findings (workspace empty, python 3.14.7). Fine to parallelize: both are metadata writes. I'll do them in one block, then the two writes in the next block (independent of each other, same block).

Wait — one thing about the plan tool: steps should be 3-7 high-level. I'll use the 7 milestones compressed: s1 skeleton+TCP listener, s2 parsing, s3 static files, s4 routing, s5 concurrency, s6 middleware, s7 stretch. That's 7. Good.

Assumptions: learner knows basic Python; port 8080 free; single file project `http-server/`; guide = Spivak lsbaws part 1; Python 3.14 stdlib only (socket module), no installs.

Risks: learner may want async instead of threads at milestone 5 (defer choice); CRLF gotchas; SO_REUSEADDR needed for fast restarts; port conflicts.

Rollback: coaching engagement — rollback = delete http-server/ directory; no system state changed.

Now write the final reply. Keep it tight:

**Where we are:** milestone 1/7 — TCP listener.

Scope + guide (2 lines). Concept (short paragraph). Skeleton written to http-server/server.py with TODOs 1-6 (list them). PROGRESS.md created. Check commands + expected output at the end.

One hint budget: not stuck yet, so no hint needed.

Let me draft the response text:

---

**Where we are:** milestone 1/7 — TCP listener.

**Scope (default, trim if you like):** one file, stdlib only, Python 3.14. Target: an HTTP server on raw sockets that parses requests, serves static files safely, routes with params, and survives concurrent load. We loosely follow Ruslan Spivak's *Let's Build A Web Server* (https://ruslanspivak.com/lsbaws-part1/), extended with routing/concurrency milestones. Milestones: 1 TCP listener → 2 request parsing → 3 static files → 4 routing → 5 concurrency + keep-alive → 6 middleware → 7 stretch WebSockets. Each ends with a runnable check recorded in `http-server/PROGRESS.md`.

**The concept.** A TCP socket is one end of a reliable byte pipe. A server creates one with `socket.socket(AF_INET, SOCK_STREAM)`, `bind()`s it to an address, and `listen()` marks it passive. `accept()` blocks until a client connects and returns a *new* socket dedicated to that client, while the listening socket keeps accepting. HTTP is plain text over that pipe: the client sends `GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n` and expects a status line, headers, a blank line (`\r\n\r\n`), then a body whose length matches `Content-Length`. Milestone 1 ignores the request bytes entirely and always answers with the same hard-coded response.

**What to write next.** I scaffolded `http-server/server.py` — the six TODOs are yours:

1. `SO_REUSEADDR` (so restarts don't die on "Address already in use")
2. `bind((host, port))`
3. `listen()`
4. `accept()` in the `while True` loop
5. one `recv(1024)` — just print it for now, we parse in milestone 2
6. `sendall(RESPONSE)` + `conn.close()`

Build `RESPONSE` yourself: status line, `Content-Type`, `Content-Length` matching the body, blank line, `Hello, world!`. Remember every line ends `\r\n`.

OS limits: none — it only needs free local port 8080, no admin rights.

**How to check it:**
```
python3 http-server/server.py   # terminal 1
curl -v localhost:8080          # terminal 2
```
Expected: curl prints `HTTP/1.1 200 OK`, then `Hello, world!`; the server stays up and accepts the next connection. Paste your server.py (or the error) when it passes or gets stuck — one hint at a time from there.

---

Hmm, "trim if you like" — is that a conditional menu? It's scope agreement, which the skill mandates ("Agree on scope"). It's fine — it's an invitation to adjust the plan, part of the coaching contract, and the skill explicitly says to agree on scope. But the tone rules say no conditional next-step menus like "If you want, I can also...". "trim if you like" is borderline. I'll phrase as: "Default scope below — redirect me if you want it smaller." Hmm, that's still conditional-ish. The skill requires agreeing on scope though; stating the default and proceeding is the action. I'll say "Default scope; say the word to shrink it." Actually simpler: just state the scope as decided and note they can redirect. Keep one short clause.

Also "Paste your server.py (or the error) when it passes or gets stuck" — good, direct next action, not a menu.

Check the "no negation-based contrastive phrasing" rule: "ignores the request bytes entirely and always answers" — that's a positive claim about behavior, fine. "No parsing yet" — fine, plain statement. Avoid "not X but Y" constructions. I think my draft is clean. "while the listening socket keeps accepting" — positive. Good.

Also the skeleton file: let me finalize it. One concern — `RESPONSE = b""` with TODO. Good. And the loop with `raise NotImplementedError`. Let me write it cleanly:

```python
"""Build-your-own HTTP server - milestone 1: TCP listener.

Accepts one connection at a time and answers every request with the
same hard-coded HTTP 200 response. Request parsing arrives in
milestone 2; for now we just print the raw bytes we receive.
"""
import socket

HOST = "127.0.0.1"
PORT = 8080

# TODO: build a minimal, valid HTTP/1.1 response:
#   status line, Content-Type, Content-Length, blank line, body.
# Every line ends with \r\n, and Content-Length must equal the
# body's byte length. Body: "Hello, world!"
RESPONSE = b""


def run(host: str = HOST, port: int = PORT) -> None:
    # AF_INET = IPv4 addresses, SOCK_STREAM = TCP (a reliable byte pipe).
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # TODO 1: setsockopt SO_REUSEADDR - lets you restart the server
    #         without waiting for the OS to release the port.
    # TODO 2: bind the socket to the (host, port) address.
    # TODO 3: mark the socket passive with listen().
    print(f"Serving on http://{host}:{port}")

    while True:
        # TODO 4: block until a client connects; accept() returns a
        #         NEW socket (conn) for this client + its address.
        # TODO 5: recv up to 1024 bytes from conn and print them -
        #         that's the raw HTTP request. One recv is fine here.
        # TODO 6: sendall(RESPONSE) on conn, then conn.close().
        raise NotImplementedError("fill in TODOs 1-6")


if __name__ == "__main__":
    run()
```

Wait — TODOs 1-3 are before the print, and the raise is inside the loop, so running it prints "Serving on..." then crashes with NotImplementedError. Clear enough.

Hmm, one subtlety: if they run before filling TODO 1-3, the raise happens before bind — fine.

PROGRESS.md as designed above.

Now the explore call — consolidate: goal, reads (skill files), findings (empty workspace, Python 3.14.7, track milestones, chosen guide), unknowns (learner's Python comfort level, port 8080 availability — minor).

Plan call: goal, assumptions, 7 steps, risks, rollback, seed_todos=true.

Then writes. Then final reply.

Let me make sure the final reply ends with the check command per the skill ("Every reply ends with this"). My draft ends with the check + a one-line "paste your code when done or stuck". The skill says the reply ends with the check command/expected output — I'll put the "paste when stuck" line before the check block, or keep it after as part of the check section. The skill: "How to check it: the command and its expected output. Every reply ends with this, including debugging answers". I'll end with the check block, and fold the "report back" line into the "What to write next" section. Cleaner compliance.

Also: should I mention the per-tutorial skill handoff? The router says hand off to per-tutorial skill if the learner wants to follow that article closely. I'm using it as the guide; I already read its skill. No need to narrate that.

One more check on the response template in the concept: `GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n` — accurate for curl. Good.

Length check: the reply is moderately long but this is a coaching kickoff with mandated sections; it's high-signal. Trim where possible. I'll compress the scope line.

Final reply draft (tightened):

---
**Where we are:** milestone 1/7 — TCP listener.

**Scope.** One file, stdlib only (`socket`), Python 3.14 — already on your machine, zero installs. Target: an HTTP server on raw sockets that parses requests, serves static files safely, routes with params, and survives concurrent load; stretch goal WebSockets. Guide: Ruslan Spivak, [*Let's Build A Web Server*](https://ruslanspivak.com/lsbaws-part1/) — we follow its part-1 arc, extended with routing/concurrency milestones. Path: 1 TCP listener → 2 request parsing → 3 static files → 4 routing → 5 concurrency + keep-alive → 6 middleware → 7 stretch. Each milestone ends with a runnable check, recorded in `http-server/PROGRESS.md` (created).

**The concept.** A TCP socket is one end of a reliable byte pipe. The server creates one with `socket.socket(AF_INET, SOCK_STREAM)`, `bind()`s it to an address, and `listen()` marks it passive. `accept()` blocks until a client connects, then returns a *new* socket dedicated to that client while the listening socket keeps accepting. HTTP is plain text over that pipe: the client sends `GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n` and expects a status line, headers, a blank line, then a body whose byte length matches `Content-Length`. Milestone 1 ignores the request and answers every connection with the same hard-coded bytes.

**What to write next.** Skeleton is at `http-server/server.py`; the TODOs are yours:

1. `SO_REUSEADDR` via `setsockopt` — restarts won't die on "Address already in use"
2. `bind((host, port))`
3. `listen()`
4. `accept()` inside the `while True` loop
5. one `recv(1024)` — print the raw request bytes; parsing is milestone 2
6. `sendall(RESPONSE)` then `conn.close()`

Also build `RESPONSE` yourself: status line, `Content-Type: text/plain`, `Content-Length` matching the body, blank line, `Hello, world!` — every line ends `\r\n`, and that detail is the classic first bug. OS limits: none, it needs only free local port 8080. When curl shows the 200 (or you hit an error), paste your `server.py` and we move to milestone 2 or debug from the real output.

**How to check it:**
```bash
python3 http-server/server.py    # terminal 1
curl -v localhost:8080           # terminal 2
```
Expected: curl prints `HTTP/1.1 200 OK` and `Hello, world!`; the server stays up and accepts the next connection.
---

Hmm "the classic first bug" — fine. "ignores the request" — positive statement, ok.

Wait, tone rule: "Don't narrate tool calls". I say "Skeleton is at http-server/server.py" — that's stating an artifact location, fine.

Also "created" for PROGRESS.md — fine.

Check forbidden constructions once more:
- "restarts won't die on..." — negation but it's a plain factual statement about behavior, and the rule targets negation-based *contrastive* phrasing (不是X而是Y / "not about X, it's about Y"). "won't die on Address already in use" is a direct positive-purpose claim... it uses "won't". The rule says "Do not use negation-based contrastive phrasing" — contrastive. "won't die" is a simple negative statement of fact, and honestly the natural way to state it. The BAD examples are all contrastive ("It's not about intelligence, it's about taste"). A plain "so restarts don't hit 'Address already in use'" is standard engineering prose. I'll keep it minimal: "so restarts skip the 'Address already in use' wait". Hmm, that's awkward. "prevents 'Address already in use' on quick restarts" — positive framing. Use that.
- "Milestone 1 ignores the request and answers every connection with the same hard-coded bytes." — positive. Good.
- "zero installs" — fine.

Also avoid "Let's" anywhere. Check. No emojis. Check.

One thing: the skill says "Ask at most 2 questions" for scope. I'm asking zero and proposing a default — allowed ("suggest a default if the learner doesn't care"). The learner was specific enough. Good.

Now execute: explore + plan in one block, then two writes in one block, then reply.**Where we are:** milestone 1/7 — TCP listener.

**Scope.** One file, stdlib only (`socket`), Python 3.14 — already on your machine, zero installs. Target: an HTTP server on raw sockets that parses requests, serves static files safely, routes with params, and survives concurrent load; WebSockets as the stretch. Guide: Ruslan Spivak, [*Let's Build A Web Server*](https://ruslanspivak.com/lsbaws-part1/) — we follow its part-1 arc, extended with routing and concurrency milestones. Each milestone ends in a runnable check, tracked in `http-server/PROGRESS.md`.

**The concept.** A TCP socket is one end of a reliable byte pipe. The server creates one with `socket.socket(AF_INET, SOCK_STREAM)`, `bind()`s it to an address, and `listen()` marks it passive. `accept()` blocks until a client connects, then returns a *new* socket dedicated to that client while the listening socket keeps accepting. HTTP is plain text over that pipe: the client sends `GET / HTTP/1.1\r\nHost: localhost:8080\r\n\r\n` and expects a status line, headers, a blank line, then a body whose byte length matches `Content-Length`. Milestone 1 ignores the request and answers every connection with the same hard-coded bytes.

**What to write next.** Skeleton is at `http-server/server.py`; the TODOs are yours:

1. `SO_REUSEADDR` via `setsockopt` — prevents "Address already in use" on quick restarts
2. `bind((host, port))`
3. `listen()`
4. `accept()` inside the `while True` loop
5. one `recv(1024)` — print the raw request bytes; parsing is milestone 2
6. `sendall(RESPONSE)` then `conn.close()`

Also build `RESPONSE` yourself: status line, `Content-Type: text/plain`, `Content-Length` matching the body, blank line, `Hello, world!`. Every line ends `\r\n` — that detail is the classic first bug. OS limits: none, it needs only free local port 8080. When curl shows the 200 (or you hit an error), paste your `server.py` and we move to milestone 2 or debug from the real output.

**How to check it:**
```bash
python3 http-server/server.py    # terminal 1
curl -v localhost:8080           # terminal 2
```
Expected: curl prints `HTTP/1.1 200 OK` and `Hello, world!`; the server stays up and accepts the next connection.