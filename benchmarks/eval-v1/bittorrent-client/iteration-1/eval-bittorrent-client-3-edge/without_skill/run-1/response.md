The user is building their own BitTorrent client and wants to know how to test it without downloading anything illegal. This is a question, not a code modification task. Let me check the workspace context — the cwd is `build-your-own-x-bittorrent-client-3`, which suggests they're working through a "build your own X" challenge. Let me look at what's in the workspace to give context-aware advice.

Actually, this is primarily an informational question. But since we're in a workspace, it might be useful to peek at what they have. Let me do a quick glob to see the project structure, then answer.

The answer should cover legal test options:
1. **Legal torrent content**:
   - Big Buck Bunny, Sintel, other Blender Foundation open movies (CC licensed)
   - Linux distribution ISOs (Ubuntu, Debian, Fedora) — official torrents
   - Internet Archive content (public domain)
   - Project Gutenberg audiobooks
2. **Create your own torrent** — make a file, create a .torrent with your client or `mktorrent`, seed it yourself
3. **Local tracker setup** — run opentracker or a simple tracker locally, or use a DHT bootstrap node
4. **Test harnesses**: 
   - Use existing clients as peers (transmission, qBittorrent, aria2) to test interop
   - `transmission-create` to make test torrents
5. **Protocol-level testing**: 
   - The official BitTorrent spec test suites
   - CodeCrafters "Build Your Own BitTorrent" challenge has a test harness (this cwd looks like exactly that challenge!)
6. **Seeding/leeching loop with yourself**: run two instances of your client, one seeding one leeching
7. **Mock peers**: write a fake peer that speaks the wire protocol to unit test handshake, piece requests, etc.

Also mention: avoid downloading copyrighted content; even "testing" with popular torrents is risky and often against tracker rules.

Since the cwd looks like the CodeCrafters challenge, they may already have a test harness. Let me check the workspace quickly with glob to see files. That's a cheap read-only call and makes the answer context-aware.

Let me glob for files in the workspace.Empty workspace, so here's the full testing playbook from scratch.

## Legal test content

- **Blender open movies** — Big Buck Bunny, Sintel, Tears of Steel (CC-licensed, well-seeded, classic interop test files)
- **Linux ISOs** — Ubuntu/Debian/Fedora official torrents; large enough to exercise multi-piece downloads
- **Internet Archive** — millions of public-domain items with torrent links
- **Your own files** — the most reliable option (see below)

## Self-contained test loop (best for development)

You control both sides, so you can test offline and deterministically:

1. **Create a torrent** from a local file: `mktorrent -o test.torrent bigfile.bin`, or `transmission-create bigfile.bin -o test.torrent -t http://localhost:8000/announce`
2. **Run a local tracker**: `opentracker` (single binary) or a minimal HTTP tracker you write yourself — building a tracker is a great companion project and teaches you the announce/scrape protocol
3. **Seed with your client**, then leech with a second instance of your client in another directory
4. **Verify integrity**: `sha256sum` the downloaded file against the original

This loop tests handshake → metadata → piece negotiation → verification end-to-end without any external network.

## Interop testing with real clients

Your client must speak the same protocol as everyone else, so test against established implementations:

- Seed with **Transmission** or **qBittorrent**, leech with yours, then swap roles
- Use `aria2c` as a scripted peer — it's headless and easy to automate
- Real clients will ruthlessly expose protocol bugs (wrong message framing, missing keep-alives, bad piece ordering) that a self-play loop hides

## Protocol-level unit tests

- Write a **mock peer**: a fake TCP server that speaks the wire protocol (handshake, bitfield, have, request, piece) so you can unit-test your state machine with scripted responses — including edge cases like choked requests and invalid piece data
- Test the **bencode codec** exhaustively: nested dicts, integers with leading zeros (should fail), non-UTF-8 keys
- Test **piece hashing** against known SHA-1 values from a hand-built `.torrent`

## If you're following the CodeCrafters challenge

The "Build Your Own BitTorrent" challenge ships its own test harness (`codecrafters test`) that runs staged tests — handshake, info dict parsing, piece download from their provided seeder. That's the fastest feedback loop and needs zero legal consideration since their seeder serves synthetic data.

One practical tip: keep a `testdata/` directory with a generated 1–4 MB file and its `.torrent` checked in, so your test suite is reproducible. Multi-MB sizes force multi-piece paths (pipelining, endgame mode) that a single-piece torrent never exercises.