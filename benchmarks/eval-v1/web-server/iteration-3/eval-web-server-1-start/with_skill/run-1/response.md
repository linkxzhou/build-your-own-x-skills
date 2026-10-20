The user wants to write their own HTTP server from raw sockets in Python, and wants coaching. This matches the build-your-own-x skill — "a web server" is explicitly listed. I must read the SKILL.md first before doing anything else.The file was truncated. Let me read the rest of it.Topic maps to `web-server`. Reading the track skill now — it's mandatory before coaching.I need to see the truncated milestone rows 4-6. Let me read lines 40-46.The track skill is loaded. The learner's request (Python, raw sockets) matches the default path and the Ruslan Spivak tutorial. Let me check the per-tutorial skill for article-specific details before coaching.I have everything I need. Now let me check the workspace state — is there an existing project? Let me look at what's in the workspace root.

Then I'll coach per the skill:
1. Agree on scope (language is given: Python; target: raw-socket HTTP server). Ask at most 2 questions, suggest defaults.
2. Pick a guide: Ruslan Spivak's "Let's Build A Web Server" part 1 (Python, raw sockets) — exact link: https://ruslanspivak.com/lsbaws-part1/
3. Milestone list from the track skill (7 milestones, can shrink).
4. Start milestone 1: TCP listener. Explain concept in 3-6 sentences, give skeleton/interface, let learner write the core, end with checkpoint command + expected output.
5. Every reply ends with the checkpoint. Keep replies short (~60 lines).
6. Record progress in PROGRESS.md when a milestone passes.

The skill says: "Agree on scope: language, target and checks. Ask at most 2 questions, and suggest a default if the learner doesn't care." The learner already said Python + raw sockets. So scope is mostly settled. I could ask 1-2 questions (e.g., do you want to follow Spivak's article closely, and what's your end goal — serve static files, or a mini-framework?). But the skill also says to start milestone 1 in the learner's workspace. I think the best move: state the plan, ask the 2 questions inline with defaults, and give milestone 1 skeleton so they can start immediately. Actually the skill says "Ask at most 2 short questions... Then start milestone 1 in the learner's workspace" (from the router skill: "Agree on scope. Settle the language, the target..., the milestone list and how each milestone is checked. Then start milestone 1 in the learner's workspace.")

Since language is settled (Python), I'll propose the target and milestone list, ask one question about depth (follow the article vs. just coach), and give milestone 1 with a skeleton. The learner writes the core — I should NOT dump the full solution. Give the interface/skeleton with TODOs.

Let me check the workspace first to see if there's an existing project.Empty workspace — starting from scratch. Scope is settled: Python, stdlib only, raw sockets. Guide: Ruslan Spivak's [Let's Build A Web Server, Part 1](https://ruslanspivak.com/lsbaws-part1/). I've scaffolded the project and PROGRESS.md.**Where we are:** Milestone 1/6 — TCP listener. Project scaffolded in `httpserver/` (`server.py` with TODOs, `PROGRESS.md` tracking all milestones).

**The concept:** A web server is a program that sits in an accept loop on a TCP socket. `bind` claims an address, `listen` opens the queue, `accept` blocks until a client connects and hands you a fresh `conn` socket for that conversation. HTTP rides on top of TCP as plain text: request bytes in, response bytes out, and the response is just a status line, headers, a blank `\r\n\r\n` line, then the body. Milestone 1 ignores what the client says and always answers the same hard-coded 200 — the point is to see the raw request bytes curl sends.

**What to write next:** Fill in the three TODOs in `httpserver/server.py` — socket + `SO_REUSEADDR`, `bind`/`listen`, then the accept loop with `recv`, `sendall`, `close`. Run it in one terminal, curl from another.

One scope question (default applies if you don't care): after milestone 4 I'd steer us toward a tiny WSGI-compatible layer rather than WebSockets — say so if you'd rather do the WebSocket stretch.

Guide we're following: [Let's Build A Web Server — Part 1](https://ruslanspivak.com/lsbaws-part1/) (Ruslan Spivak).

**Checkpoint** — run the server, then:

```
curl -v localhost:8080
```

Expected: `HTTP/1.1 200 OK` in the response headers, `Hello, world!` as the body, and your server's stdout printing the raw request (`GET / HTTP/1.1`, `Host: localhost:8080`, ...). Paste your server code and that output here when it works — or paste the error if it doesn't.