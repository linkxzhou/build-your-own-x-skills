The user is writing a toy blockchain in Python and asks: "Can we connect it to Bitcoin mainnet and send real coins?"

This is a question about connecting a toy blockchain to Bitcoin mainnet and sending real coins. Let me think about what's actually being asked and what the right answer is.

Key facts:
1. A toy blockchain (custom Python implementation) is a completely separate ledger from Bitcoin. Blockchains don't "connect" to each other in the sense of sharing state — Bitcoin mainnet is its own network with its own consensus rules, its own UTXO set, its own peer-to-peer protocol.
2. To send real coins on Bitcoin mainnet, you need to construct and sign transactions that are valid under Bitcoin's consensus rules, using real private keys that control real UTXOs. Your toy blockchain cannot do this unless you implement Bitcoin's transaction format, script, signing (ECDSA/secp256k1), etc.
3. Ways to interact with Bitcoin mainnet:
   - Run a full node (Bitcoin Core) and use its JSON-RPC API. Your Python code can call `sendrawtransaction`, `createrawtransaction`, etc. But this means Bitcoin Core does the heavy lifting; your toy chain is just a client.
   - Use a lightweight library like `python-bitcoinlib`, `bit`, or `btcd`... to construct/sign transactions and broadcast via a node or a third-party API (blockstream.info Esplora API, mempool.space).
   - Talk the P2P protocol directly (your toy could implement the Bitcoin wire protocol to listen to blocks/transactions — that's a great learning exercise — but you still can't "send coins" without valid signed transactions).
4. Safety: real money, irreversible transactions, testnets exist (testnet3/testnet4, signet, regtest), faucets give free testnet coins. Strongly recommend regtest/testnet first.
5. The user's mental model may be confused: "connect my blockchain to Bitcoin mainnet" — I should clarify what's possible: (a) read-only observation of mainnet (easy, safe), (b) broadcasting real transactions (requires real keys and real Bitcoin's rules; your toy chain is irrelevant to validity), (c) merging your chain with Bitcoin (impossible without a fork / hashrate).

Also there's a skill: "build-your-own-x" — the description says use it whenever someone wants to understand how a tool works by building their own, or names a category from build-your-own-x (blockchain is in there). The user says "I'm writing my own toy blockchain in Python" — this matches the skill trigger: "从零实现、自己动手写一个 X... blockchain". The skill says to read SKILL.md BEFORE doing anything else when the task matches. The user's task is a question about their in-progress project — it's arguably a match ("writing my own toy blockchain" = building their own blockchain). I should read the skill first.

Let me read the skill file first, then answer.

The instruction: "When the user's task matches a skill's description, read that skill's SKILL.md with the read tool BEFORE doing anything else, then follow it (including reading the reference files it points to when relevant)."

So I should read .agents/skills/build-your-own-x/SKILL.md first.

Then answer the question. The answer should be direct: 

- Direct answer: You can connect to mainnet as a read-only listener/client, but your toy chain can't move real coins — moving coins requires valid, signed Bitcoin transactions from keys controlling real UTXOs, and Bitcoin miners/nodes only accept those. Your chain is a separate ledger; there's no bridge.
- What "connecting" can realistically mean:
  1. Read-only: implement Bitcoin P2P protocol (handshake, headers sync) or use an Esplora/mempool.space REST API to watch blocks/txs. Safe, great learning.
  2. Write (spend): use Bitcoin Core RPC (regtest/testnet first) or a Python lib (python-bitcoinlib, `bit`) to build+sign txs and broadcast. Real coins only if you have real UTXOs; fees matter; irreversible.
  3. What's impossible: making mainnet accept your chain's blocks or merging ledgers. That would require a fork with hashrate.
- Recommendation: do regtest (Bitcoin Core in a box, free coins via `generatetoaddress`), then testnet4 with faucet coins, then mainnet with dust amounts if desired. Your toy chain can still learn from mainnet by parsing blocks.

Also safety notes: never paste real private keys/seed phrases into toy code; test on regtest; mainnet txs are irreversible; fee estimation.

Tone: senior engineer, direct, no filler. Lead with the answer. Use structure but keep it tight. No negation-contrastive phrasing per constraints ("not X but Y" banned). Careful: "Your toy chain can't move real coins" — that's a plain negative statement, which is fine; the ban is on negation-based contrastive phrasing (不是X而是Y / "It's not about X, it's about Y"). Plain factual negatives like "you can't" should be okay — the constraint targets contrastive constructions. I'll keep plain negatives minimal but they're allowed; the ban is specifically on the contrastive pattern. Let me re-read: "Prefer direct positive claims. Do not use negation-based contrastive phrasing... State only the positive. If a real distinction needs both sides, name them as parallel positive clauses." So I should phrase distinctions as parallel positive clauses: "Reading mainnet is easy and safe; moving coins requires valid signed transactions under Bitcoin's rules." That's positive phrasing. Good.

Also no conditional next-step menus ("If you want, I can also..."). I can name a concrete next action directly, e.g., "Start with regtest: ..." and offer to scaffold? "Offer to scaffold" would be a next-step menu... The rule says don't stage menus where user must say a magic phrase. I can end with a direct recommendation. Maybe end with the concrete first command to run. That's an action, fine.

Should I use tools? The skill read is mandated. Do I need web search? Not really; this is knowledge I have. Maybe verify current testnet status (testnet3 vs testnet4, faucets)? Could be useful but not essential. The core answer is stable knowledge. I might quickly check the skill file and then answer. Keep tool use minimal: read SKILL.md.

Let me read the skill first.

After reading, follow it: the skill likely says to pick topic/language/tutorial and coach step by step. The user already has a project in progress and asked a specific question. The skill probably has sub-skills for blockchain. Let me read it and any relevant reference.

Then produce the answer. Keep it high-signal.

Plan for the answer content:

1. Direct answer up front: Two different things — observing mainnet (yes, safe) and moving real coins (your chain has no authority there; coins move only via valid signed Bitcoin transactions). A blockchain is a ledger plus consensus; mainnet accepts only txs signed by keys controlling real UTXOs, so "connecting" your toy chain gives it zero spending power.

2. Three realistic integration levels:
   - Read-only observer: implement Bitcoin P2P handshake + headers/blocks sync in your Python code, or hit mempool.space / blockstream Esplora REST API. Your toy chain can mirror/parse mainnet blocks — great for learning serialization, Merkle trees, difficulty.
   - Spend via Bitcoin's own stack: run Bitcoin Core; use RPC (`createrawtransaction`/`signrawtransactionwithwallet`/`sendrawtransaction`) or Python libs (`python-bitcoinlib`, `bit`). Your code becomes a wallet/client on Bitcoin; the toy chain stays a separate ledger.
   - Fork/merge: would require convincing miners to adopt your rules — a full-blown fork project, out of scope for a toy.

3. Safety ladder: regtest (Core in-process, free coins, `generatetoaddress`) → testnet4/signet (faucet coins) → mainnet (real sats, irreversible, fee market). Never put real keys in toy code; generate throwaway keys, keep amounts to dust you can afford to lose.

4. Concrete first step: install Bitcoin Core, run regtest, and point your Python code at RPC port 18443. Maybe give 3-4 commands.

Also mention: if the goal is to learn how Bitcoin works, implementing the P2P protocol listener in the toy chain is the sweet spot.

Length: moderate. Use a few bullets. Avoid banned phrasings. No "In summary". End with concrete recommendation/first command.

Let me read the skill now.The skill file is truncated. I need to see the category map for blockchain slug. Let me grep for blockchain in the skills directory.The track skill lives at `skills/blockchain-cryptocurrency/SKILL.md`. Reading it now.Let me see the truncated remainder of the track skill (last ~600 chars) and the tutorials reference. Let me read the rest of the file and tutorials.md.Short answer, split in two:

- **Connect as a client:** yes. Your Python code can talk to Bitcoin's network or its public APIs and read real blocks.
- **Send real coins from your chain:** there is no bridge for that. Coins move only through transactions signed by keys controlling real UTXOs, and every mainnet node validates them against Bitcoin's consensus rules. Your chain's internal state is invisible to Bitcoin — a transaction it produces is just invalid bytes to the network. To move real coins you'd build and sign Bitcoin transactions with Bitcoin's own stack (Bitcoin Core RPC, or `python-bitcoinlib`/`bit`), at which point your toy chain is a separate ledger sitting next to a wallet.

Three realistic levels of "connecting":

1. **Read-only observer (safe, recommended).** Implement the Bitcoin P2P handshake and `headers`/`block` sync in your Python code, or call a public REST API (mempool.space, blockstream.info Esplora). Parsing real blocks with your own validator is excellent practice for serialization, Merkle trees, and difficulty adjustment. Zero risk.
2. **Spending via Bitcoin's own stack.** Your code becomes a wallet client on Bitcoin: build, sign, broadcast through Core's JSON-RPC. Real coins demand real UTXOs, correct fees, and every mistake is irreversible.
3. **Merging your chain into mainnet.** That's a consensus fork needing miners to adopt your rules — a multi-year project, out of scope for a toy.

House rule for this coaching track: all funds work happens on regtest or testnet; mainnet funds stay out of the project. One wrong fee or address on mainnet and the coins are gone with no undo.

The ladder:

- **regtest** — private Bitcoin Core, unlimited free coins, instant blocks. Ideal for milestone 4 (ECDSA-signed transfers) and milestone 7 (double-spend rejection).
- **testnet4 / signet** — public network, faucet coins, real block times and fee estimation.
- **mainnet** — read-only observation only.

Concrete first step on regtest (you run the install from bitcoincore.org; I stay out of your shell for installs):

```
bitcoind -regtest -daemon
bitcoin-cli -regtest createwallet toy
bitcoin-cli -regtest generatetoaddress 101 $(bitcoin-cli -regtest getnewaddress)
```

Then point your Python code at the regtest RPC port (18443) with `requests` + basic auth, and you have free, resettable coins to practice building, signing, and broadcasting transactions against a real node.

Where does your chain sit in the milestone table — do you have signed transactions yet (milestone 4)? That decides whether the fun next step is a regtest wallet or a mainnet block observer. If you want a Python reference to follow alongside, the track's canonical one is [_Learn Blockchains by Building One_](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46).