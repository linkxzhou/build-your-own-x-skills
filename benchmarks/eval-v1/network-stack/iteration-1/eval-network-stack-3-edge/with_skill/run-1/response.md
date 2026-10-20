The user wants to write their own TCP/IP stack using a TAP device, but they're on macOS. They ask: "Can I do the TAP part?"

This matches the build-your-own-x skill — "build your own TCP/IP stack" is a classic build-your-own-x project. The skill description says: use it whenever someone wants to understand how a tool works by building their own, names a category from build-your-own-x (network stack). So I should read the SKILL.md first before doing anything else.

Let me read the skill file.The file was truncated. Let me read the rest of it, and also look for the relevant track skill. The topic is "TCP/IP stack" — likely maps to a category like "network-stack" or similar. Let me read the rest of the SKILL.md and check the skills directory.The topic maps to the `network-stack` track. Reading that track skill now (mandatory per the workflow).The file is truncated. Let me read the rest of it.Now let me check the tutorials reference and any per-tutorial skills for the network-stack track.The track skill flags the OS limit up front ("TUN/TAP needs Linux + root or a VM"). Since the user is asking specifically about the TAP milestone, let me check the per-tutorial skill for the saminiir article and verify the current state of TAP support on macOS.The search returned nothing. Let me try again with different terms.Search seems flaky. Let me try once more and also read the tutorial map reference.Search is unresponsive; let me verify the key facts directly from primary sources.SourceForge is behind a JS challenge and GitHub's HTML is mostly chrome. Let me fetch the raw files instead.wireguard-go confirms the key fact: on macOS it uses `com.apple.net.utun_control` (utun, L3-only), on Linux `/dev/net/tun` (TUN/TAP). One more check on QEMU's macOS backend, then I'll summarize.tuntaposx's last release was 2009 (news feed ends 2012) — that confirms it's dead. One last detail to verify: the utun packet framing quirk in wireguard-go.Short answer: native TAP on macOS is a dead end, but the TAP milestone is still doable — you just pick one of three routes.

**Why plain TAP fails on macOS**

- macOS ships only `utun`, which is L3-only: it speaks IP packets with a 4-byte address-family header, and has no Ethernet layer. You can verify this in the wild: wireguard-go implements `tun_linux.go` via `/dev/net/tun` (TUN+TAP) but `tun_darwin.go` via `com.apple.net.utun_control`, L3 only.
- The classic third-party TAP driver, tuntaposx, last released in 2009 and its news feed went quiet in 2012. It's a kext, and modern macOS (especially Apple Silicon) requires kexts to be signed and explicitly approved — in practice it's unusable.

**Your three routes**

1. **utun, skip Ethernet/ARP (pure macOS, least friction).** Open a `utun` control socket, and start your stack at IPv4. Two adjustments to the saminiir tutorial:
   - Every read/write gets a 4-byte header: `00 00 00 02` for IPv4 (protocol family in the last byte).
   - Milestone 2 becomes "utun + IPv4 parsing" and milestone 3 (ARP) is dropped — there's no link layer to resolve. Milestones 4–7 (ICMP, TCP handshake, data/close) are unchanged, and `ping <your utun IP>` still works as the checkpoint.
2. **Linux VM (closest to the tutorial).** UTM, Lima, or OrbStack give you a real `/dev/net/tun`. You run the stack inside the VM, and the saminiir milestones — Ethernet frames, ARP, everything — work verbatim. Best if you want the full L2 experience including ARP.
3. **tuntaposx on an Intel Mac** — technically possible, but you'd be debugging a 2009 kext on a modern OS. I'd skip it.

**Recommendation:** route 1 if your goal is understanding TCP itself (the interesting 80% of the project), route 2 if you specifically want the Ethernet/ARP layers.

Either way, milestone 1 — a TCP echo server/client with Beej's Guide (http://beej.us/guide/bgnet/) — is plain sockets and runs identically on macOS. Tell me which route you want and we'll set up the project skeleton and the utun (or VM) open/read/write loop as milestone 2.