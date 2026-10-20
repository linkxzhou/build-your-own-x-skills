The user wants to learn networking by writing their own TCP/IP stack in C. This matches the build-your-own-x skill — specifically "TCP/IP stack" which is a category in codecrafters-io/build-your-own-x. I should read the skill's SKILL.md first before doing anything else.The file was truncated mid-table. Let me read the rest to find the TCP/IP stack category slug.The category is `network-stack`. Reading the track skill now — it's mandatory before anything else.The track skill says:
1. Agree on scope: language, target, checks. Ask at most 2 questions, suggest a default.
2. Pick a guide. The learner already said C. The natural pick: "Let's code a TCP/IP stack" (saminiir) for the TUN/TAP user-space stack, plus Beej's Guide for milestone 1 (sockets).
3. Work milestone by milestone.

The learner said C already, so I don't need to ask about language. The skill says ask at most 2 questions and suggest a default. The main open question: OS environment (TUN/TAP needs Linux + root or a VM). That's worth one question. Also whether they want to start with sockets (milestone 1) or jump straight to the TAP stack.

Per the skill's output format for each turn:
- Where we are: milestone N/total
- The concept: short
- What to write next: skeleton or TODO list, not full answer
- How to check it: command + expected output
- Stuck? One hint at a time.

Also: "Never dump the whole project." Give skeleton, not full solution. Credit upstream tutorial with exact link. Don't install anything myself.

The user asked "Where do I start?" — so I should give the roadmap (milestones), pick the guide, and start milestone 1 with a skeleton and checkpoint. I should ask at most 2 short questions — the key one being their OS (Linux? macOS? Windows?) since TUN/TAP requires Linux. And maybe whether they've done socket programming before (to decide whether milestone 1 is needed or can be skimmed).

Let me check if there's a per-tutorial skill for saminiir's article: `ls skills | grep '^network-stack-'`. Let me check the manifest quickly.There's a per-tutorial skill for the saminiir article. Since that's the guide I'm about to recommend, let me read it.You're building a **user-space TCP/IP stack in C** — the classic route is: warm up with sockets, then implement Ethernet/ARP/IP/ICMP/TCP yourself on top of a TAP device. I'll coach this milestone by milestone; you write the code, I scaffold and we verify each step with a runnable check.

**Guide:** [_Let's code a TCP/IP stack_](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/) (saminiir, C), with [_Beej's Guide to Network Programming_](http://beej.us/guide/bgnet/) for the warm-up.

**The roadmap:**

| # | Milestone | Checkpoint |
|---|---|---|
| 1 | TCP echo server/client (sockets) | `nc localhost 9000` echoes lines |
| 2 | TAP device + Ethernet frame parsing | frames logged when host sends traffic to the TAP IP |
| 3 | ARP: request/reply + cache | `arping` gets a reply from your stack |
| 4 | IPv4 + ICMP echo reply | `ping 10.0.0.2` gets replies from your stack |
| 5 | TCP handshake (SYN/SYN-ACK/ACK, states) | `nc 10.0.0.2 80` connects; tcpdump shows a clean handshake |
| 6 | TCP data + close (windowing, retransmit, FIN) | 1 MB transfers intact |
| 7 | Stretch: VPN / tunnel frames over UDP | two TAP endpoints ping through your tunnel |

Two questions before we lock scope:

1. **What OS are you on?** Milestones 2+ need Linux with root (or a Linux VM) for `/dev/net/tun`. Milestone 1 works anywhere.
2. **Have you written socket code before?** If yes, milestone 1 is a one-sitting skim; if no, it's a real milestone and Beej ch. 1–6 is your reading.

Default if you don't care: Linux, new to sockets, start at milestone 1 now.

---

**Where we are:** milestone 1/7 — TCP echo server.

**The concept:** A TCP server does four syscalls in order: `socket()` creates an endpoint, `bind()` attaches it to an address/port, `listen()` marks it passive, `accept()` blocks until a client connects and returns a *new* fd for that connection. Then it's plain `read()`/`write()` on that fd. The kernel handles all of TCP for you — this milestone is about learning the interface your own stack will eventually replace.

**What to write** (`echo.c`):

- `main()`: create socket (`AF_INET`, `SOCK_STREAM`), set `SO_REUSEADDR`, bind to `0.0.0.0:9000`, `listen(fd, 10)`
- accept loop: on each connection, `read()` into a buffer, `write()` the same bytes back, close when `read()` returns 0
- compile: `gcc -Wall -Wextra -o echo echo.c`

**Check it:**

```
./echo            # terminal 1
nc localhost 9000 # terminal 2 — type a line, get it back
```

Expected: every line you type comes back verbatim; Ctrl-C on `nc` closes cleanly.

**Stuck?** First hint: if `bind` fails with "Address already in use", you forgot `SO_REUSEADDR` or an old `./echo` is still running.

Tell me your OS + socket experience, and paste your echo server (or its errors) when it compiles — then we move to the TAP device, where the real fun starts.