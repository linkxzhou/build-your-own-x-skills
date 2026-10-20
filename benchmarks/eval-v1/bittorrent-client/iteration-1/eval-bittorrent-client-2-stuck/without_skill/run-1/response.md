The user is working on a BitTorrent client and their computed info hash doesn't match what other clients show. They're serializing the parsed info dict to JSON and then SHA1-ing it. This is a classic bencode round-trip issue.

The problem: info_hash must be the SHA1 of the exact original bencoded bytes of the `info` dictionary from the torrent file, not a re-serialization. JSON serialization changes key order, encoding, integer formatting, etc. Even re-bencoding a parsed dict can differ (key ordering, integer representation, string vs bytes handling).

The correct approach: when parsing the torrent file, record the byte range of the `info` dictionary in the original file (start offset of `4:info` value to its end), then slice those raw bytes and SHA1 them.

Let me look at the workspace to see their code. The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-bittorrent-client-2`. Let me explore the files first.

I should check what code exists, find where they compute the info hash, and fix it to use raw bencoded bytes.No files found? Let me check the directory contents with bash.工作区是空的，所以直接说结论：info_hash 必须对 torrent 文件里 `info` 字典的**原始 bencode 字节**做 SHA1，任何“解析后再重新序列化”的做法都会得到不同的哈希。

JSON 序列化必然失败，因为它和 bencode 是两种完全不同的编码：

- bencode 的 key 按字典序排列且带长度前缀（`4:infod...e`），JSON 是 `{"key": ...}` 带引号和冒号
- bencode 整数是 `i42e`，JSON 是 `42`
- bencode 的字符串就是原始字节，JSON 会做转义、且默认按文本处理，非 UTF-8 字节（很常见，比如 piece 哈希、非 UTF-8 文件名）直接就坏了

甚至把解析结果重新 bencode 一遍也可能出错：如果你的实现没严格按字典序排 key、或者把 bytes/str 混用，字节序列就和原文件不一致。

正确做法是解析时记录字节偏移。bencode 解析器在遇到 `4:info` 时记下 value 的起始偏移，解析完这个字典后记下结束偏移，然后：

```python
raw = open("sample.torrent", "rb").read()
info_bytes = raw[info_start:info_end]   # info 字典的原始字节，含首尾的 d...e
info_hash = hashlib.sha1(info_bytes).digest()
```

一个最小实现思路（在 decode 函数里加个可选的偏移记录）：

```python
def decode(data, i):
    if data[i:i+1] == b'd':
        i += 1
        start = i - 1  # 字典起始（含 'd'）
        result = {}
        while data[i:i+1] != b'e':
            key, i = decode(data, i)
            result[key], i = decode(data, i)
        return result, i + 1
    # ... 其他类型
```

顶层解析时判断 key 是否为 `b'info'`，记下它的起止即可。或者更省事：用现成库，比如 Python 的 `bencodepy`（`bencodepy.decode(f.read())` 配合 `bencodepy.encode` 不行，要用它的 `decode` 返回的有序结构配合原始切片），最稳的还是自己解析时记偏移。

验证方法：拿一个知名种子，对比 `transmission-show` 或 WebTorrent 网页显示的 info hash；或者用 `mktorrent` 自己造一个种子，它的哈希就是基准。