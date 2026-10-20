The user wants to build their own DNS server to learn the protocol. This matches the build-your-own-x skill. I should read the SKILL.md first before doing anything else.The file is truncated. Let me read the rest of it, and also look for the DNS-related track skill. DNS would likely fall under "database" or "networking" or maybe there's a specific DNS category. Let me read the rest of the SKILL.md and check the skills directory.DNS maps to the `misc` track. Let me read that track skill and check for a DNS-specific tutorial skill.Two DNS-specific tutorial skills exist: `misc-nodejs-dns` and `misc-rust-dns`. Let me read the rest of the track skill and the tutorials reference.Both per-tutorial skills point to milestone maps. Let me check the Rust one (the canonical DNS protocol tutorial) and see which toolchains exist in this workspace.Good news: this workspace already has Rust 1.95, Node 25, Python 3.14 and Go, and the skill library has a dedicated track for this. DNS falls under the `misc` build-your-own-x track, and the canonical upstream tutorial is **[Building a DNS server in Rust](https://github.com/EmilHernvall/dnsguide/blob/master/README.md)** (Emil Hernvall) — it's the best protocol-teaching resource of the bunch because you hand-roll every byte of the wire format.

**The target I propose:** a DNS server that listens on UDP `127.0.0.1:5353`, parses raw query packets, and answers A records for a local zone — then learns recursive resolution against real root servers. Defined done as: `dig @127.0.0.1 -p 5353 example.test A` returns a valid answer.

**Milestones** (each ends with a runnable check):

| # | Milestone | You learn | Checkpoint |
|---|---|---|---|
| 1 | Skeleton + packet capture | UDP sockets, what a DNS packet looks like on the wire | `dig` query arrives, server prints the raw bytes |
| 2 | Header + question parser | Byte layout: ID, flags, counts; name compression pointers | Unit tests parse a fixture packet correctly |
| 3 | Response builder | RCODEs, answer sections, encoding names back to bytes | `dig` gets a valid NXDOMAIN response |
| 4 | Local zone answers | Record types (A, AAAA, CNAME), TTLs | `dig @127.0.0.1 -p 5353 example.test` returns your IP |
| 5 | Recursive resolver | The real hierarchy: root → TLD → authoritative | `dig @127.0.0.1 -p 5353 google.com` resolves for real |
| 6 | Hardening | Truncation, timeouts, malformed packet handling | 3 failure-mode tests pass |

One question before we start: **Rust, Node, Python, or Go?** My default is Rust — the tutorial maps 1:1 to the milestones above and the borrow checker forces you to actually understand the buffer parsing. If you'd rather move faster with less ceremony, Python is the low-friction option.

Tell me the language and I'll scaffold milestone 1.