The user wants to write a BitTorrent client in Go and asks "Step 1?". This matches the build-your-own-x skill — "build your own BitTorrent client" is a category in codecrafters-io/build-your-own-x. The skill instructions say: when the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it.

Let me read the skill first.The file was truncated. I need to see the category map to find the slug for BitTorrent. Let me read more of the file.The slug is `bittorrent-client`. Reading the track skill now — it's mandatory before coaching.Reading the rest of the track skill and the tutorials reference in parallel.The Go guide is jse.li's article. Checking for a per-tutorial skill and what's already in the workspace.There's a per-tutorial skill for the Go article. Reading it, since the learner picked Go.The track is set: Go, upstream guide https://blog.jse.li/posts/torrent/ (jse.li — the clearest Go walkthrough). Checking the toolchain in your workspace before we start.Track confirmed: Go, upstream guide [jse.li's "Building a BitTorrent client from the ground up in Go"](https://blog.jse.li/posts/torrent/), 7 milestones. Go 1.26.1 is available and the workspace is empty, so I'll scaffold the project and set up milestone 1 (bencode) with its checkpoint tests.Two compile errors in the skeleton — fixing them so the scaffold builds and the tests fail red cleanly.The `_ = x` landed outside the switch scope. Restructuring `Encode` so each case uses its variable.The scaffold is verified:
- `go build ./...` passes
- `go vet ./...` passes
- `go test ./bencode/` fails red, and every failure is `bencode: not implemented` — exactly the expected starting state.

Mark s4 complete and hand off to the learner with the milestone-1 coaching format:
- Where we are: milestone 1/7
- The concept: bencode in 3-6 sentences
- What to write next: TODO list / skeleton pointers
- How to check it: commands + expected output
- Stuck? one hint at a time

Keep it tight. Credit upstream tutorial link. Don't dump the solution.**Where we are:** Milestone 1/7 — Bencode. Scaffold is in place and verified: `go build ./...` and `go vet ./...` pass, and `go test ./bencode/` fails red with only `bencode: not implemented` errors. That red test run is your starting line.

**The concept:** Bencode is the wire format for everything in BitTorrent — .torrent files, tracker responses, peer messages. It has exactly four types: `i42e` (integers), `4:spam` (byte strings: length, colon, bytes), `l...e` (lists), and `d...e` (dicts whose keys are always byte strings, sorted when encoding). It's self-delimiting, which is why `Decode` returns how many bytes it consumed — nested values need to know where the parent's next field starts. The whole parser is one dispatch on the first byte, recursing for lists and dicts.

**What to write next** — all TODOs live in `bencode/bencode.go`:

1. `decodeInt` — find the `e`, `strconv.Atoi` the digits; reject empty, leading zeros, `i-0e`
2. `decodeString` — digits up to `:`, then slice that many bytes; reject truncated payloads
3. `decodeList` / `decodeDict` — loop `decodeAny` (or key/value pairs) until `e`
4. `decodeAny` + `Decode` — dispatch on first byte: `i`, digit, `l`, `d`; `Decode` rejects trailing garbage
5. `Encode` — same four cases; sort dict keys with `sort.Strings` (BEP 3 requires byte order)

**How to check it:**

```
go test ./bencode/        # all green, including round-trip and error cases
go run . ubuntu.torrent   # prints announce, name, length once main.go's TODO is done
```

The fixture test `TestDecodeTorrentFixture` mirrors what a real .torrent looks like, so milestone 1 is done when tests are green and `go run .` prints a real torrent's name and length. Grab a small legal torrent to try (e.g. a Debian netinst ISO's .torrent).

Guide we're following: [Building a BitTorrent client from the ground up in Go](https://blog.jse.li/posts/torrent/) — its bencode section maps 1:1 to this milestone.

Stuck? Ask and you get one hint at a time. When tests pass, I'll record it in `PROGRESS.md` and we move to milestone 2: the info hash.