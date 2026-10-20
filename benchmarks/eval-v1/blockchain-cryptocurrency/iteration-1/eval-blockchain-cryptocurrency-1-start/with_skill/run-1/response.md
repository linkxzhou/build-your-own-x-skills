The user wants to build a simple blockchain in Python, step by step. This matches the build-your-own-x skill — "从零实现" / "build your own" / blockchain category. I must read the skill's SKILL.md first before doing anything else.The file was truncated. Let me read the rest of it, and also find the blockchain track skill.主题映射到 `blockchain-cryptocurrency`。现在正在读取轨道技能（强制），并检查哪些教程技能与 Python 匹配。有一个 Python 特定的教程技能。让我阅读轨道技能的其余部分以及 Python 教程技能。已读取轨道技能和 Python 教程技能。上游教程是 HackerNoon 的 "Learn Blockchains by Building One"。现在正在检查工作区状态、Python 可用性以及里程碑映射。工作区是空的，Python 3.14 可用，教程已选定。先记录探索结论并制定计划，然后搭里程碑 1 的脚手架。现在写里程碑 1 的骨架和检查脚本。The red baseline is confirmed: 0/3, exit 1. Now update todos (s1, s2 done, s3 in_progress) and give the coaching output per the track skill format:

- Where we are: milestone 1/7
- The concept: short
- What to write next: skeleton/TODO list (already in file)
- How to check: command + expected output
- Stuck: one hint at a time

Credit the upstream tutorial with exact link. Keep it tight.**里程碑 1/7：区块 + 哈希 + 创世区块**

**概念（30 秒版）**：区块链就是一个链表，每个节点是「区块」。区块 = 一批数据 + 前一个区块的哈希 + 自己内容的 SHA-256 指纹。因为哈希由内容决定，改一个字母哈希就全变，而下一个区块又引用这个哈希——篡改历史会像多米诺一样被识破。这就是整条链防篡改的全部根基。

**你的任务**：打开 `blockchain.py`，填 4 个 TODO（每处都有注释提示）：

1. `compute_hash()` 里构造 dict：`index / timestamp / data / previous_hash` 四个字段——千万别把 `self.hash` 放进去，那是自己算自己
2. `json.dumps(..., sort_keys=True)` 序列化成字符串
3. `hashlib.sha256(字符串.encode()).hexdigest()` 返回
4. `create_genesis_block()` 返回创世区块，`timestamp` 写死 `0`（用 `time.time()` 每次运行哈希都不同，检查 1 会挂）

**检查**：

```
python3 check_m1.py
```

当前是红基线（0/3，我刚跑过）。填完后应输出：

```
PASS  1. 创世区块哈希跨运行稳定
PASS  2. 哈希是 64 位十六进制（SHA-256）
PASS  3. 改动数据会改变哈希

3/3 通过
```

**卡住了就喊一声**，一次给一个提示。写完把 `check_m1.py` 的输出贴给我，或者直接说「过了」，我们进里程碑 2：把区块串成链 + 防篡改校验。

参考教程（可对照，非必读）：[Learn Blockchains by Building One — HackerNoon](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)