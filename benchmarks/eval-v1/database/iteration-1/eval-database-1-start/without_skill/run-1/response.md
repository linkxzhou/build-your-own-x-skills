The user wants to build a mini Redis in Python from scratch with GET/SET support. Let me check the workspace first to see what's there, then plan the work.

The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-database-1` — looks like a "build your own x" style project. Let me look at what exists.

I should:
1. Explore the workspace
2. Plan the implementation
3. Build it step by step

A mini Redis with GET/SET needs:
- TCP server (socket) speaking RESP protocol (Redis Serialization Protocol)
- RESP parsing: inline commands and arrays of bulk strings
- Command dispatch: PING, GET, SET (maybe DEL, EXPIRE as extras — but user asked GET/SET, keep minimal; PING is useful for testing with redis-cli)
- Key-value store with optional TTL on SET (EX/PX options are part of SET spec, but keep minimal — maybe just SET key value, and maybe SET with EX as a stretch)
- Concurrency: threading per connection
- Tests: a simple test script using raw sockets, and compatibility with redis-cli

Let me start by exploring the workspace.Empty workspace, Python 3.14.7. Let me record an exploration note and plan, then build.

Plan:
1. `mini_redis/server.py` — TCP server, thread per connection, RESP protocol
2. `mini_redis/resp.py` — RESP encoder/decoder (or keep in one file? A small project — maybe two files: protocol and server, plus store)
3. `mini_redis/store.py` — in-memory dict with TTL support
4. `mini_redis/commands.py` — command dispatch (PING, GET, SET, DEL, maybe EXPIRE/TTL)
5. `tests/test_mini_redis.py` — integration test with raw sockets
6. README with usage

Keep it minimal but correct. The user said "从零写一个迷你 Redis（GET/SET）" — from scratch, GET/SET. I'll include PING (needed for redis-cli handshake... actually redis-cli sends COMMAND/HELLO etc. but works without), DEL and TTL/EXPIRE are nice-to-have but the spec says GET/SET. I'll keep the core GET/SET/PING, and add SET with EX/PX + TTL/DEL as small extras since they're cheap and make it feel real. Actually, let me be careful about scope: "Don't add features beyond what was asked." GET/SET is the ask. PING is practically required for testing. I'll do GET/SET/PING and mention DEL/EXPIRE as possible next steps. Hmm, but SET with EX is a natural part of SET. I'll keep SET simple: SET key value [EX seconds] — actually minimal: SET key value only. Let me just do GET/SET/PING, plus graceful handling of unknown commands and wrong arity. That's the cleanest scope.

Actually, let me reconsider — a "mini Redis" tutorial-style build usually includes: RESP parsing, command loop, and the store. I'll structure:

- `mini_redis/__init__.py`
- `mini_redis/resp.py` — RESP encoding + a streaming decoder that handles partial reads
- `mini_redis/store.py` — KV store (dict) with optional TTL hooks (keep simple: just dict for now)
- `mini_redis/server.py` — socket server, thread per client, dispatch table
- `tests/test_server.py` — raw socket integration tests
- `README.md` — how to run

RESP details:
- Client → server: arrays of bulk strings: `*2\r\n$3\r\nGET\r\n$3\r\nfoo\r\n`
- Server → client:
  - Simple string: `+OK\r\n`
  - Error: `-ERR ...\r\n`
  - Integer: `:1\r\n`
  - Bulk string: `$3\r\nbar\r\n` or `$-1\r\n` for nil
  - Array: `*N\r\n...` or `*-1\r\n`
  - Null array for unknown command errors etc.

Decoder: read from socket until we have a complete command. Implement a buffered parser: feed bytes, return list of commands. Simplest robust approach: read chunks into a buffer, try to parse one message; if incomplete, read more.

Inline commands: redis supports `GET foo\r\n` inline. redis-cli uses RESP arrays, so inline is optional. I'll support inline too since it's easy and helps manual telnet testing. Hmm, keep it — it's ~10 lines.

Concurrency: thread per connection, store protected by a lock (dict ops are atomic-ish under GIL but compound ops like check-then-act need lock; with just GET/SET a plain dict is fine, but I'll add a lock for correctness discipline).

Also handle: empty request (`*0\r\n` → ignore?), unknown command → error reply, wrong number of arguments → error reply matching Redis's message format: "ERR wrong number of arguments for 'get' command".

Key/value must be bytes; decode for logging.

Server: SO_REUSEADDR, bind 127.0.0.1:6379 by default (allow --port). Graceful shutdown on KeyboardInterrupt.

Testing: run server on a free port in a subprocess, connect with socket, send RESP, assert replies. Also test with redis-cli if available? Just mention it in README.

Let me write the plan and todos, then implement. Since this is a multi-file change, I should call `explore` (record) and `plan`. The workspace is empty so exploration is trivial — I already did ls. I'll call explore briefly and plan with seed_todos.

Let me now write the code.

resp.py:

```python
"""RESP (REdis Serialization Protocol) encoding and decoding."""

CRLF = b"\r\n"


class RespError(Exception):
    """Protocol-level error (malformed client input)."""


class RespProtocolError(RespError):
    pass


def encode_simple(value: bytes) -> bytes:
    return b"+" + value + CRLF


def encode_error(message: bytes) -> bytes:
    return b"-" + message + CRLF


def encode_int(value: int) -> bytes:
    return b":" + str(value).encode() + CRLF


def encode_bulk(value: bytes | None) -> bytes:
    if value is None:
        return b"$-1\r\n"
    return b"$" + str(len(value)).encode() + CRLF + value + CRLF


def encode_array(values) -> bytes:
    ...
```

Decoder class:

```python
class RespDecoder:
    """Incremental RESP decoder: feed() bytes, pop() complete messages."""

    def __init__(self):
        self._buffer = b""

    def feed(self, data: bytes):
        self._buffer += data

    def next_message(self):
        """Return the next complete message (list[bytes]) or None if incomplete."""
        ...
```

Parsing: message can be an array of bulk strings, or an inline command.

Array parse:
- buffer must start with `*`
- find first CRLF; if none → incomplete
- header = buffer[1:idx]; n = int(header); if n == -1 → null array (treat as empty/ignore)
- then parse n bulk strings: each `$len\r\n<bytes>\r\n`
- if len == -1 → None element

Inline: if buffer doesn't start with `*` (or `$`), read until CRLF, split on whitespace.

Edge: if buffer starts with something else like `$` — clients don't send that as a command; treat as inline too? Redis treats any non-`*` line as inline. I'll do: if first byte is `*` → RESP array, else inline line.

Malformed → raise RespError, server replies `-ERR Protocol error` and closes connection (like real Redis).

server.py:

```python
import argparse
import socket
import threading

from .resp import RespDecoder, RespError, encode_bulk, encode_error, encode_simple
from .store import Store


class MiniRedis:
    def __init__(self, store=None):
        self.store = store or Store()
        self.commands = {
            "PING": self.cmd_ping,
            "GET": self.cmd_get,
            "SET": self.cmd_set,
        }

    # command handlers take decoded args (list[bytes]) and return bytes to send
    def cmd_ping(self, args):
        if not args:
            return encode_simple(b"PONG")
        if len(args) == 1:
            return encode_bulk(args[0])
        return encode_error(b"ERR wrong number of arguments for 'ping' command")

    def cmd_get(self, args):
        if len(args) != 1:
            return encode_error(b"ERR wrong number of arguments for 'get' command")
        value = self.store.get(args[0])
        return encode_bulk(value)

    def cmd_set(self, args):
        if len(args) != 2:
            return encode_error(b"ERR wrong number of arguments for 'set' command")
        self.store.set(args[0], args[1])
        return encode_simple(b"OK")

    def handle_command(self, command: bytes, args: list[bytes]) -> bytes:
        handler = self.commands.get(command.upper())
        if handler is None:
            return encode_error(b"ERR unknown command '" + command + b"'")
        return handler(args)
```

Connection handling:

```python
def handle_connection(conn, addr, redis):
    decoder = RespDecoder()
    with conn:
        while True:
            data = conn.recv(4096)
            if not data:
                break
            decoder.feed(data)
            while True:
                try:
                    message = decoder.next_message()
                except RespError as exc:
                    conn.sendall(encode_error(...)); return
                if message is None:
                    break
                if not message:
                    continue  # empty array / blank line
                reply = redis.handle_command(message[0], message[1:])
                conn.sendall(reply)
```

Wait — one subtlety: if protocol error occurs, we should send error and close. Also sendall may raise BrokenPipeError if client disconnected — catch and close.

Server main:

```python
def serve(host="127.0.0.1", port=6379):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen()
    print(f"mini-redis listening on {host}:{port}")
    while True:
        conn, addr = server.accept()
        t = threading.Thread(target=handle_connection, args=(conn, addr, redis), daemon=True)
        t.start()
```

store.py:

```python
import threading


class Store:
    """Thread-safe in-memory key/value store."""

    def __init__(self):
        self._data = {}
        self._lock = threading.Lock()

    def get(self, key: bytes) -> bytes | None:
        with self._lock:
            return self._data.get(key)

    def set(self, key: bytes, value: bytes) -> None:
        with self._lock:
            self._data[key] = value
```

tests: use subprocess to launch server on a random free port, wait for it to accept, then run tests:

- SET → +OK
- GET existing → bulk
- GET missing → $-1
- PING → +PONG
- PING hello → bulk hello
- unknown command → -ERR
- wrong arity → -ERR
- pipelining: send two commands in one packet → two replies
- partial send: send header, then rest → still works
- inline command: "SET a b\r\n" works
- binary value with CRLF inside: SET key with value containing \r\n → roundtrip works (bulk strings handle binary safely)
- unicode key

Test harness: pick free port by binding socket to port 0, close, then pass to server (small race but fine for tests). Or run server in a thread in-process instead of subprocess — simpler and faster: start serve() in a thread with port 0? serve() binds internally... I can make serve accept a pre-bound socket or return the bound port. Simplest: in tests, create the server socket, get port, run accept loop in thread. Let me structure server.py so `make_server(host, port)` returns (socket, port) and `serve_forever(sock, redis)` runs the loop. Then tests use in-process threads. And `__main__` uses serve().

Actually simpler for tests: subprocess with `python -m mini_redis.server --port 0`? Port 0 then we don't know the port. Could print the port. In-process threading is cleaner. I'll do:

```python
def create_server(host="127.0.0.1", port=6379):
    sock = socket.socket(...)
    sock.setsockopt(...)
    sock.bind((host, port))
    sock.listen()
    return sock

def serve_forever(sock, redis=None):
    ...
```

main: `sock = create_server(args.host, args.port); serve_forever(sock)`.

Tests with in-process: sock = create_server("127.0.0.1", 0); port = sock.getsockname()[1]; thread = Thread(target=serve_forever, args=(sock,), daemon=True).

Client helper in tests:

```python
class Client:
    def __init__(self, port):
        self.sock = socket.create_connection(("127.0.0.1", port))
        self.buf = b""
    def send_raw(self, data): self.sock.sendall(data)
    def command(self, *args):
        self.send_raw(encode_command(*args))
        return self.read_reply()
    def read_reply(self): parse one reply from buffer, reading more as needed
```

Need a reply parser in tests — that duplicates resp decoding. Alternative: reuse RespDecoder? It parses client messages (arrays/inline). Server replies can be simple strings, errors, ints, bulk, arrays. My decoder only handles arrays+inline. For tests, write a small reply reader that handles +, -, :, $. That's fine — tests are allowed a mini parser. Or make the decoder generic enough to parse any RESP type. Generic parser is nicer: `parse_message` handles +, -, :, $, *. I'll make RespDecoder handle all five types and return tagged results. Hmm, but then server command handling expects list of bytes. I can have decoder return (type, value) tuples... Let me keep it pragmatic:

- `resp.py` has encoders for all types, and `RespDecoder` that parses any RESP message into Python values: simple string → bytes, error → RespServerError(bytes), int → int, bulk → bytes|None, array → list. Inline → list[bytes].

Server: `message = decoder.next_message()`; if it's a list → command; else ignore (clients shouldn't send other types; if they do, just ignore or error). For tests: same decoder to read replies. 

Error representation: define `class RedisError(Exception)` in resp.py wrapping server error replies so tests can assert on message. Simple.

Let me also handle the `*0\r\n` empty array → return empty list, server ignores. And null array `*-1\r\n` → None, ignore.

Inline parsing details: Redis splits inline on spaces/tabs, handles quotes — I'll do simple split() without quote handling, and empty line → empty list (ignored).

One more edge in decoder: `next_message` must not consume buffer unless a full message is available. Implementation:

```python
def next_message(self):
    msg, size = self._parse(self._buffer, 0)
    if msg is _INCOMPLETE: return None
    self._buffer = self._buffer[size:]
    return msg
```

Write `_parse(buf, pos)` returning (value, new_pos) or raising _Incomplete. Use an internal exception for incomplete to keep code clean.

Let me write it:

```python
class _Incomplete(Exception):
    pass


class RespDecoder:
    def __init__(self):
        self._buffer = b""

    def feed(self, data: bytes) -> None:
        self._buffer += data

    def next_message(self):
        try:
            value, pos = self._parse(self._buffer, 0)
        except _Incomplete:
            return None
        self._buffer = self._buffer[pos:]
        return value

    def _parse(self, buf, pos):
        if pos >= len(buf):
            raise _Incomplete
        marker = buf[pos:pos+1]
        if marker == b"*":
            return self._parse_array(buf, pos)
        if marker in (b"+", b"-", b":", b"$"):
            return self._parse_simple(buf, pos)
        return self._parse_inline(buf, pos)
```

_parse_simple: find CRLF from pos; if not found → incomplete. payload = buf[pos+1:eol]. 
- `+` → payload
- `-` → RedisError(payload)
- `:` → int(payload)
- `$` → n = int(payload); if n == -1 → None; end = eol+2+n; if len(buf) < end → incomplete; data = buf[eol+2:end]; check buf[end:end+2] == CRLF else protocol error; return data.

_parse_array: find CRLF; n = int; if n == -1 → None; pos = eol+2; items = []; for i in range(n): item, pos = self._parse(buf, pos) — but nested elements in commands are bulk strings; generic recursion works. Note: elements of an array could be any type per protocol; recursion handles it.

_parse_inline: find CRLF; if not found → incomplete; line = buf[pos:eol]; return line.split() as list of bytes. b"GET foo".split() → [b"GET", b"foo"]. Empty line → [].

Protocol errors: e.g. `$abc\r\n` → int() raises ValueError → let it propagate as ValueError? Better wrap into RespError. I'll catch ValueError in int parsing and raise RespError("Protocol error: invalid integer"). Server catches RespError → sends `-ERR Protocol error` and closes.

Also guard against absurdly long lines? Real Redis has 512MB limits etc. Skip — keep minimal, but maybe cap buffer to avoid memory blowup from a malicious client... skip, it's a learning project. Actually a tiny guard is cheap: if len(buffer) > 512MB raise. Skip it; keep code minimal per instructions.

Now the server dispatch. Redis error messages:
- unknown command: `ERR unknown command 'FOO'` (modern redis includes args count etc.) — I'll use `ERR unknown command '<CMD>'`.
- wrong arity: `ERR wrong number of arguments for 'get' command`.

GET on missing key → `$-1\r\n` (RESP2 null bulk string). Good for redis-cli.

Now tests file `tests/test_server.py` using unittest (stdlib, no deps):

```python
import socket
import threading
import unittest

from mini_redis.resp import RespDecoder, encode_array, RedisError
from mini_redis.server import create_server, serve_forever


class ServerTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sock = create_server("127.0.0.1", 0)
        cls.port = cls.sock.getsockname()[1]
        cls.thread = threading.Thread(target=serve_forever, args=(cls.sock,), daemon=True)
        cls.thread.start()

    def setUp(self):
        self.client = Client(self.port)
    def tearDown(self):
        self.client.close()
```

Client class in test file:

```python
class Client:
    def __init__(self, port):
        self.sock = socket.create_connection(("127.0.0.1", port), timeout=5)
        self.decoder = RespDecoder()

    def close(self): self.sock.close()

    def send_raw(self, data: bytes): self.sock.sendall(data)

    def command(self, *parts: bytes):
        self.send_raw(encode_array(list(parts)))
        return self.read_reply()

    def read_reply(self):
        while True:
            reply = self.decoder.next_message()
            if reply is not None:
                return reply
            data = self.sock.recv(4096)
            if not data:
                raise ConnectionError("server closed connection")
            self.decoder.feed(data)
```

Hmm — `next_message` returning None means incomplete; but a null bulk reply is also None! Ambiguity: GET missing → server sends `$-1\r\n` → decoder returns None → test thinks incomplete and blocks. Bad. Fix: decoder should distinguish. Options: `next_message()` returns a sentinel `_INCOMPLETE` or raise. I'll make `next_message()` return `None` only for incomplete and... no. Better: have `next_message()` raise nothing and return a distinct object? Cleaner: give decoder a method `try_parse()` that returns `(True, value)` or `(False, None)`. Or: represent null bulk as None but have next_message return a wrapper... 

Simplest: `next_message()` returns `_MISSING` sentinel when incomplete. Public API: `next_message()` → value or `_MISSING`? Ugly for server code. Alternative: decoder exposes `messages()` generator... 

Let me restructure: `RespDecoder.next_message()` returns `NotParsed` sentinel (module-level singleton) when incomplete. Server: `msg = decoder.next_message(); if msg is NotParsed: break`. Tests: `if reply is NotParsed: read more`. That's explicit and unambiguous. I'll name it `INCOMPLETE`. Fine.

Actually cleaner alternative: null bulk → None, and next_message returns tuple? No — sentinel is fine and explicit.

Now server loop with the sentinel:

```python
while True:
    msg = decoder.next_message()
    if msg is INCOMPLETE:
        break
    if isinstance(msg, RedisError):  # client sent "-..."? weird; ignore
        continue
    if not isinstance(msg, list):
        # clients normally only send arrays/inline; ignore anything else
        continue
    if not msg:
        continue
    reply = redis.handle_command(msg[0], msg[1:])
    conn.sendall(reply)
```

Hmm wait, inline empty line → [] → continue. Good.

Protocol error handling: RespError raised by decoder → send `-ERR Protocol error: ...` and close connection. RedisError is for server error replies (from `-` parsing) — in server context clients don't send `-`, but if they do, ignore.

Wait, there's a subtlety: RespError vs RedisError naming. Let me define:
- `RespError(Exception)` — malformed input (protocol error).
- `RedisError(Exception)` — an error reply from a Redis server (`-ERR ...`), used when parsing replies; tests assert `err.args[0].startswith(b"ERR")`.

In decoder `_parse_simple` for `-`: raise RedisError(payload). For invalid ints: raise RespError.

Server catches RespError around parsing → reply `-ERR Protocol error` + close.

Now `handle_command`:

```python
def handle_command(self, command: bytes, args):
    handler = self.commands.get(command.upper())
    if handler is None:
        return encode_error(b"ERR unknown command '" + command + b"'")
    return handler(args)
```

Note: command.upper() on bytes works in Python (bytes.upper() ASCII-only — perfect).

SET with wrong arity: `SET key` → error. GET with 2 args → error.

PING with 0 args → +PONG; 1 arg → bulk echo.

Now serve_forever:

```python
def serve_forever(sock, redis=None):
    redis = redis or MiniRedis()
    while True:
        try:
            conn, addr = sock.accept()
        except OSError:
            break  # socket closed
        thread = threading.Thread(target=_handle_connection, args=(conn, redis), daemon=True)
        thread.start()
```

_handle_connection:

```python
def _handle_connection(conn, redis):
    decoder = RespDecoder()
    try:
        with conn:
            while True:
                msg = decoder.next_message()
                if msg is INCOMPLETE:
                    data = conn.recv(4096)
                    if not data:
                        return
                    decoder.feed(data)
                    continue
                if isinstance(msg, list) and msg:
                    conn.sendall(redis.handle_command(msg[0], msg[1:]))
                # non-command messages (stray simple strings etc.) are ignored
    except (RespError, ConnectionError, OSError):
        # RespError: malformed input -> tell the client, then drop the connection
        try:
            if isinstance(...)... 
```

Hmm, cleaner: catch RespError separately to send protocol error reply:

```python
def _handle_connection(conn, redis):
    decoder = RespDecoder()
    try:
        with conn:
            while True:
                try:
                    msg = decoder.next_message()
                except RespError as exc:
                    conn.sendall(encode_error(b"ERR Protocol error: " + str(exc).encode()))
                    return
                if msg is INCOMPLETE:
                    data = conn.recv(4096)
                    if not data:
                        return
                    decoder.feed(data)
                    continue
                if isinstance(msg, list) and msg:
                    conn.sendall(redis.handle_command(msg[0], msg[1:]))
    except OSError:
        return  # client went away mid-conversation
```

Wait — order: `except RespError` inner, `except OSError` outer. conn.sendall raising BrokenPipeError (OSError subclass) → outer catch → return. Good. But careful: `conn.sendall` inside inner try for RespError — if sendall raises OSError it propagates to outer. Fine.

One issue: after RespError we return without draining buffer — correct, connection closes like real Redis.

Also: `with conn:` then `return` inside — fine, closes.

Edge: `msg is INCOMPLETE` check must come before isinstance checks. And note `msg` could be `None` (null array `*-1`) or `b"..."` (stray simple string) or int — all ignored by the `isinstance(msg, list) and msg` guard. Good.

main entry:

```python
def main(argv=None):
    parser = argparse.ArgumentParser(description="mini Redis server (GET/SET/PING)")
    parser.add_argument("--host", default="127.0.0.1")
    parser.add_argument("--port", type=int, default=6379)
    args = parser.parse_args(argv)
    sock = create_server(args.host, args.port)
    print(f"mini-redis listening on {args.host}:{args.port}")
    try:
        serve_forever(sock)
    except KeyboardInterrupt:
        pass
    finally:
        sock.close()
```

`__init__.py`: export MiniRedis, create_server, serve_forever, RespDecoder, encoders. Keep light.

README.md: what it is, RESP quick intro, run instructions, redis-cli / telnet examples, test instructions, project layout, next steps (DEL/EXPIRE/TTL, persistence, event loop).

Tests to write (unittest):
1. test_set_then_get — SET foo bar → b"OK"; GET foo → b"bar"
2. test_get_missing → None
3. test_overwrite — SET foo bar; SET foo baz; GET foo → b"baz"
4. test_ping — PING → b"PONG"; PING hello → b"hello"
5. test_unknown_command → RedisError with b"ERR unknown command"
6. test_wrong_arity — GET with no args → error "wrong number of arguments"
7. test_binary_value_with_crlf — value b"a\r\nb" roundtrip
8. test_empty_value — SET k "" → GET → b""
9. test_pipelining — send two encoded commands in one sendall, read two replies
10. test_partial_writes — send `*3\r\n$3\r\nSE`, then rest → works
11. test_inline_command — send b"SET a b\r\n" → OK; b"GET a\r\n" → b"b"
12. test_protocol_error — send b"$abc\r\n" → server replies -ERR Protocol error and closes connection
13. test_multiple_clients — two clients, value set by one visible to other
14. test_keys_are_binary — key with spaces? Keys via RESP arrays can contain spaces: SET "a b" c → GET "a b" → c. Nice.

Also unicode: value "héllo".encode() roundtrip — covered by binary test basically. Keep list tight but meaningful.

For test 12 (protocol error): after sending garbage, read reply → RedisError containing b"Protocol error", then subsequent recv → b"" (connection closed). 

For reading error replies: decoder raises RedisError when parsing `-...`. So read_reply in Client must catch RedisError and return it? If decoder raises RedisError during next_message, the buffer position... careful: my next_message parses then commits buffer only on success. If parse raises RedisError, buffer isn't consumed — but for tests we just want the error; I'll catch RedisError in read_reply and return the exception itself? Better: return the exception's payload. Let me have read_reply catch RedisError and return it as the result (test asserts isinstance). Hmm, but the buffer wasn't consumed — doesn't matter since connection closes after protocol error.

Wait, actually there's a design question: should next_message consume the buffer when it parses a `-ERR` reply? For a client reading replies, after getting the error the next reply follows. If buffer isn't consumed, subsequent next_message re-parses the same error forever → infinite loop in read_reply! That's a real bug for pipelined error replies. Fix: in next_message, catch RedisError, commit buffer, re-raise. Let me implement:

```python
def next_message(self):
    try:
        value, pos = self._parse(self._buffer, 0)
    except _Incomplete:
        return INCOMPLETE
    except RedisError:
        self._buffer = b""  # hmm, or consume up to end of that message
        raise
    self._buffer = self._buffer[pos:]
    return value
```

For RedisError, the message ends at the CRLF we found — _parse_simple knows eol. Simplest: consume entire buffer? No — pipelined replies after an error would be lost. Proper: _parse_simple for `-` returns (RedisError(payload), eol+2) as a *value*, and next_message returns the exception object as the parsed value! Then no exception semantics in parsing; callers check isinstance. Hmm, that makes decoder return exception objects — a bit odd but pragmatic and unambiguous. 

Alternative: raise RedisError but with buffer consumed correctly by having _parse raise a composite... Overcomplicating. Decision: `_parse` returns RedisError instances as values for `-` replies. Callers: server ignores non-list messages (an error object isn't a list → ignored). Tests: read_reply returns whatever; if it's RedisError, test asserts on it. Clean, no buffer-commit bugs. 

But wait — is it confusing that parsing a server error reply yields an exception instance rather than raising? For a test client it's actually convenient. I'll document it in resp.py docstring: "error replies are returned as RedisError instances (they are data, not parse failures)".

Hmm, one more consideration: should RedisError subclass Exception with `.args[0]` = payload bytes. Tests: `err = client.command(...); self.assertIsInstance(err, RedisError); self.assertTrue(err.args[0].startswith(b"ERR"))`. Fine.

Now, `INCOMPLETE` sentinel: module-level `INCOMPLETE = object()` with a nicer repr? Make a tiny class:

```python
class _IncompleteType:
    __slots__ = ()
    def __repr__(self):
        return "INCOMPLETE"

INCOMPLETE = _IncompleteType()
```

Slightly nicer for debugging. OK.

Let me also double check `_parse_array` recursion for inline elements: elements inside `*` arrays must be parsed with `_parse` which for non-`*` markers falls to `_parse_inline` — but inside an array, an element like `+OK\r\n` would parse as inline line "+OK" → ["+OK"]. Per RESP spec, array elements are actually any RESP type, so `+` should parse as simple string. My dispatch: `+`, `-`, `:`, `$` → typed parse; `*` → array; else inline. Inside arrays, inline fallback only triggers for garbage. Good enough and spec-compliant for the types we emit.

Edge: inline parse when buffer starts with `\r\n` (empty line) → returns []. Server ignores. Good.

Edge: client sends `*1\r\n$-1\r\n` (array with null) → items [None] → msg = [None] → truthy list, msg[0] is None → handle_command(None, ...) → command.upper() crashes! Guard: in server, `if isinstance(msg, list) and msg and isinstance(msg[0], bytes)`. Or in handle_command, treat non-bytes command as unknown. I'll add the isinstance check in the server loop. Actually simpler: `if isinstance(msg, list) and msg:` then `command = msg[0]; if not isinstance(command, bytes): continue`. Hmm, just fold into one condition: `if isinstance(msg, list) and msg and isinstance(msg[0], (bytes, bytearray))`. bytes only is fine.

Now — threading: each connection has its own decoder (local), store shared with lock. 

Store: keep get/set with lock. Fine.

File layout:

```
mini_redis/
  __init__.py
  resp.py
  store.py
  server.py
tests/
  test_server.py
README.md
```

Run: `python -m mini_redis.server` (needs `if __name__ == "__main__": main()` in server.py).

Let me also verify Python 3.14 compat — all stdlib, fine. Type hints `bytes | None` fine.

Now write everything. Steps:
1. explore note (already have workspace info) — call explore to record.
2. plan with seed_todos.
3. Write files.
4. Run tests.
5. Quick manual smoke test with a real client (start server, use a small python snippet or redis-cli if installed) — tests already cover; maybe run server and use `redis-cli` if available, else skip. I'll do a quick bash smoke: start server in background, send RESP via python one-liner, kill server. Actually tests cover this in-process. A separate smoke test with the actual `python -m mini_redis.server` entry point verifies main() wiring — worth it.

Let me write the code now. I'll write resp.py carefully.

```python
"""RESP (REdis Serialization Protocol) encoding and decoding.

Client -> server requests are arrays of bulk strings, e.g.:

    *2\r\n$3\r\nGET\r\n$3\r\nfoo\r\n

Server -> client replies use five top-level types:

    +OK\r\n            simple string
    -ERR ...\r\n       error
    :1\r\n             integer
    $3\r\nbar\r\n      bulk string ($-1\r\n for nil)
    *1\r\n$3\r\nbar\r\n  array (*-1\r\n for nil)
"""

CRLF = b"\r\n"


class RespError(Exception):
    """Malformed protocol input (the connection must be dropped)."""


class RedisError(Exception):
    """An error reply received from a Redis server (parsed as data)."""


class _IncompleteType:
    """Singleton returned by RespDecoder.next_message() when more bytes are needed."""

    __slots__ = ()

    def __repr__(self) -> str:
        return "INCOMPLETE"


INCOMPLETE = _IncompleteType()


# --- encoding -----------------------------------------------------------

def encode_simple(value: bytes) -> bytes:
    return b"+" + value + CRLF


def encode_error(message: bytes) -> bytes:
    return b"-" + message + CRLF


def encode_int(value: int) -> bytes:
    return b":" + str(value).encode("ascii") + CRLF


def encode_bulk(value: bytes | None) -> bytes:
    if value is None:
        return b"$-1" + CRLF
    return b"$%d%s%s%s" % (len(value), CRLF, value, CRLF)


def encode_array(values) -> bytes:
    if values is None:
        return b"*-1" + CRLF
    out = [b"*%d%s" % (len(values), CRLF)]
    for value in values:
        if isinstance(value, bytes):
            out.append(encode_bulk(value))
        elif isinstance(value, int):
            out.append(encode_int(value))
        elif value is None:
            out.append(b"$-1" + CRLF)
        else:
            raise TypeError(f"cannot encode {type(value).__name__} as a RESP array element")
    return b"".join(out)


def encode_command(*parts: bytes) -> bytes:
    """Encode a client request (array of bulk strings)."""
    return encode_array([bytes(p) for p in parts])
```

Decoder:

```python
class RespDecoder:
    """Incremental RESP parser.

    feed() raw bytes, then call next_message() repeatedly; it returns
    INCOMPLETE when a full message has not arrived yet. Parsed values:

      +simple  -> bytes
      -error   -> RedisError (data, not a parse failure)
      :int     -> int
      $bulk    -> bytes or None
      *array   -> list of parsed values
      inline   -> list[bytes] (whitespace-split, e.g. "GET foo\r\n")
    """

    def __init__(self) -> None:
        self._buffer = b""

    def feed(self, data: bytes) -> None:
        self._buffer += data

    def next_message(self):
        try:
            value, end = self._parse(self._buffer, 0)
        except _Incomplete:
            return INCOMPLETE
        self._buffer = self._buffer[end:]
        return value

    # -- internals --

    def _parse(self, buf: bytes, pos: int):
        if pos >= len(buf):
            raise _Incomplete()
        marker = buf[pos : pos + 1]
        if marker == b"*":
            return self._parse_array(buf, pos)
        if marker in (b"+", b"-", b":", b"$"):
            return self._parse_prefixed(buf, pos)
        return self._parse_inline(buf, pos)

    def _find_crlf(self, buf: bytes, pos: int) -> int:
        eol = buf.find(CRLF, pos)
        if eol == -1:
            raise _Incomplete()
        return eol

    def _parse_int(self, payload: bytes) -> int:
        try:
            return int(payload)
        except ValueError:
            raise RespError(f"invalid integer '{payload.decode("ascii", "replace")}'") from None
```

Hmm wait, f-string with nested same quotes — Python 3.12+ allows nested same quotes in f-strings (PEP 701). Python 3.14 fine. But to be safe/readable use different quotes.

```python
    def _parse_prefixed(self, buf: bytes, pos: int):
        eol = self._find_crlf(buf, pos)
        payload = buf[pos + 1 : eol]
        marker = buf[pos : pos + 1]
        after = eol + 2
        if marker == b"+":
            return payload, after
        if marker == b"-":
            return RedisError(payload.decode("utf-8", "replace")), after
        if marker == b":":
            return self._parse_int(payload), after
        # bulk string
        length = self._parse_int(payload)
        if length < -1:
            raise RespError("invalid bulk string length")
        if length == -1:
            return None, after
        end = after + length + 2
        if len(buf) < end:
            raise _Incomplete()
        data = buf[after : after + length]
        if buf[after + length : end] != CRLF:
            raise RespError("bulk string is missing trailing CRLF")
        return data, end
```

Wait — RedisError payload: keep bytes or str? For tests, comparing with b"ERR..." is natural. I'll keep bytes: `RedisError(payload)`. args[0] is bytes. Fine.

```python
    def _parse_array(self, buf: bytes, pos: int):
        eol = self._find_crlf(buf, pos)
        count = self._parse_int(buf[pos + 1 : eol])
        if count < -1:
            raise RespError("invalid array length")
        if count == -1:
            return None, eol + 2
        pos = eol + 2
        items = []
        for _ in range(count):
            item, pos = self._parse(buf, pos)
            items.append(item)
        return items, pos

    def _parse_inline(self, buf: bytes, pos: int):
        eol = self._find_crlf(buf, pos)
        line = buf[pos:eol]
        return line.split(), eol + 2
```

Note `_Incomplete` internal exception class — define before use.

One catch: `_parse_int` raising RespError for inline garbage like `+hello` — no wait, `+` is handled. Inline `GET foo` → split. A line like `SET` alone → ["SET"] → server: wrong number of arguments error. Good.

Another catch: inline commands with `\n` only (no `\r`)? Redis accepts `\n` for inline. My find(CRLF) would treat `GET foo\nGET bar\n` — find CRLF fails → incomplete forever. Real Redis inline accepts plain \n. Minor; telnet sends \r\n. I could search for both. Keep CRLF-only, document. Actually let me handle bare `\n` in inline mode for robustness: find first occurrence of `\n`, strip trailing `\r`. Cheap:

```python
    def _parse_inline(self, buf, pos):
        nl = buf.find(b"\n", pos)
        if nl == -1:
            raise _Incomplete()
        line = buf[pos:nl]
        if line.endswith(b"\r"):
            line = line[:-1]
        return line.split(), nl + 1
```

But then a RESP array containing... no, arrays never hit inline path. But careful: `_parse` dispatch — if buffer starts with `*` we parse array; inline only for non-RESP first byte. With bare-\n support, `GET foo\n` works. Good, include it.

Hmm wait, one more: what if the first byte is `$` from a client? `_parse_prefixed` handles it — a client sending a bare bulk string gets it parsed as data and ignored by server. Fine.

store.py:

```python
"""Thread-safe in-memory key/value storage."""

import threading


class Store:
    def __init__(self) -> None:
        self._data: dict[bytes, bytes] = {}
        self._lock = threading.Lock()

    def get(self, key: bytes) -> bytes | None:
        with self._lock:
            return self._data.get(key)

    def set(self, key: bytes, value: bytes) -> None:
        with self._lock:
            self._data[key] = value

    def __len__(self) -> int:
        with self._lock:
            return len(self._data)
```

server.py:

```python
"""mini-redis: a tiny Redis-compatible TCP server (GET / SET / PING)."""

import argparse
import socket
import threading

from .resp import (
    INCOMPLETE,
    RespError,
    encode_bulk,
    encode_error,
    encode_simple,
)
from .store import Store


class MiniRedis:
    """Command dispatch + shared store. One instance serves all connections."""

    def __init__(self, store: Store | None = None) -> None:
        self.store = store if store is not None else Store()
        self._commands = {
            b"PING": self._cmd_ping,
            b"GET": self._cmd_get,
            b"SET": self._cmd_set,
        }

    def handle_command(self, command: bytes, args: list[bytes]) -> bytes:
        handler = self._commands.get(command.upper())
        if handler is None:
            return encode_error(b"ERR unknown command '" + command + b"'")
        return handler(args)

    def _cmd_ping(self, args):
        if len(args) > 1:
            return encode_error(b"ERR wrong number of arguments for 'ping' command")
        if not args:
            return encode_simple(b"PONG")
        return encode_bulk(args[0])

    def _cmd_get(self, args):
        if len(args) != 1:
            return encode_error(b"ERR wrong number of arguments for 'get' command")
        return encode_bulk(self.store.get(args[0]))

    def _cmd_set(self, args):
        if len(args) != 2:
            return encode_error(b"ERR wrong number of arguments for 'set' command")
        self.store.set(args[0], args[1])
        return encode_simple(b"OK")


def create_server(host: str = "127.0.0.1", port: int = 6379) -> socket.socket:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(128)
    return sock


def serve_forever(sock: socket.socket, redis: MiniRedis | None = None) -> None:
    redis = redis if redis is not None else MiniRedis()
    while True:
        try:
            conn, _addr = sock.accept()
        except OSError:
            return  # server socket closed
        threading.Thread(target=_handle_connection, args=(conn, redis), daemon=True).start()


def _handle_connection(conn: socket.socket, redis: MiniRedis) -> None:
    decoder = RespDecoder()
    try:
        with conn:
            while True:
                try:
                    message = decoder.next_message()
                except RespError as exc:
                    conn.sendall(encode_error(b"ERR Protocol error: " + str(exc).encode()))
                    return
                if message is INCOMPLETE:
                    data = conn.recv(4096)
                    if not data:
                        return
                    decoder.feed(data)
                    continue
                if isinstance(message, list) and message and isinstance(message[0], bytes):
                    conn.sendall(redis.handle_command(message[0], message[1:]))
                # anything else (stray non-command data) is ignored
    except OSError:
        return  # client disconnected mid-conversation
```

Wait — `RespDecoder` import missing in that snippet; add to imports.

Also `str(exc).encode()` — RespError messages are ASCII. Fine.

main:

```python
def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="mini-redis: GET/SET/PING over RESP")
    parser.add_argument("--host", default="127.0.0.1", help="bind address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=6379, help="bind port (default: 6379)")
    args = parser.parse_args(argv)
    sock = create_server(args.host, args.port)
    print(f"mini-redis listening on {args.host}:{args.port}")
    try:
        serve_forever(sock)
    except KeyboardInterrupt:
        print("\nbye")
    finally:
        sock.close()


if __name__ == "__main__":
    main()
```

__init__.py:

```python
"""mini-redis: a tiny Redis-compatible server (GET/SET/PING) written from scratch."""

from .resp import (
    INCOMPLETE,
    RedisError,
    RespDecoder,
    RespError,
    encode_array,
    encode_bulk,
    encode_command,
    encode_error,
    encode_int,
    encode_simple,
)
from .server import MiniRedis, create_server, main, serve_forever
from .store import Store

__all__ = [...]
```

Hmm, exporting `main` maybe unnecessary; keep create_server, serve_forever, MiniRedis, Store, resp stuff. Fine.

tests/test_server.py — as sketched. Client.read_reply:

```python
def read_reply(self):
    while True:
        reply = self.decoder.next_message()
        if reply is not INCOMPLETE:
            return reply
        data = self.sock.recv(4096)
        if not data:
            raise ConnectionError("server closed the connection")
        self.decoder.feed(data)
```

Note: reply could legitimately be None (null bulk) — `is not INCOMPLETE` handles that correctly. 

Test protocol error:

```python
def test_protocol_error_closes_connection(self):
    self.client.send_raw(b"$abc\r\n")
    reply = self.client.read_reply()
    self.assertIsInstanceI was cut off mid-way through writing the test file content. I need to continue: finish the plan, write the files, run tests, smoke test. Let me continue from where I left off — I had just finished sketching the code in my head. I should now actually create the files. Let me continue with the test file and then write everything to disk.

Let me continue: finish test_protocol_error test, then write all files, run tests, smoke test with the real entry point.I introduced a bug in the test client's `read_reply` (a nonsense condition and a mid-file import). Fixing it now.Both failures are bugs in my test bytes, and the server actually behaved correctly: `PING` with zero args is valid (`+PONG`), and my hand-written partial chunk declared `$3` but delivered a 1-byte value — the server rightly rejected it. Fixing the tests:16/16 pass. Smoke test the real entry point, and check for `redis-cli`:Works end to end. The `RuntimeWarning` comes from `__init__.py` importing `.server` while `python -m mini_redis.server` re-executes it as `__main__` — I'll make `__init__.py` docstring-only to keep the entry point clean:The background server held the shell open. Retrying with output redirected and an explicit kill:The PING smoke test passed (`+PONG`), but a stale server from the earlier timed-out command still holds port 6398. Cleaning it up:Everything works:
- 16/16 tests pass
- Entry point smoke test: clean startup, correct `+PONG` reply, clean shutdown, no warnings

Let me do a final verification of the file tree and then summarize.迷你 Redis 已经从零搭好并通过全部测试。

## 项目结构

```
mini_redis/
├── resp.py     # RESP 协议：编码器 + 增量解码器
├── store.py    # 线程安全的内存 KV 存储（dict + lock）
└── server.py   # TCP 服务器 + 命令分发（PING / GET / SET）
tests/
└── test_server.py  # 16 个集成测试（真实 TCP 连接）
README.md
```

## 运行

```bash
python3 -m mini_redis.server --port 6379
# 另一个终端
redis-cli -p 6379 set greeting "hello world"
redis-cli -p 6379 get greeting
```

## 核心设计（三个值得理解的部分）

1. **RESP 协议**（`mini_redis/resp.py`）：客户端发来的是 bulk string 数组，如 `*3\r\n$3\r\nSET\r\n...`。解码器是**增量式**的——`feed()` 收字节，`next_message()` 在消息不完整时返回 `INCOMPLETE` 哨兵，所以天然支持两种真实场景：一条命令拆在多个 TCP 包里、以及 pipelining（一个包里塞多条命令）。bulk string 按长度前缀读取，值里含 `\r\n`、`\x00` 都安全。

2. **连接处理**（`mini_redis/server.py:60`）：每连接一个线程，各自持有独立 decoder，共享同一个 store。协议错误（如 `$abc`）回复 `-ERR Protocol error` 后断开连接，和真实 Redis 行为一致；未知命令、参数个数错误返回 Redis 风格的错误消息。

3. **存储**（`mini_redis/store.py`）：加锁的 dict，键值都是 bytes。

## 测试覆盖

SET/GET 往返、覆盖写、缺失键返回 `$-1`、二进制值（含 `\r\n` 和 `\x00`）、pipelining、分包写入、inline 命令（`telnet` 风格）、协议错误断连、多客户端共享数据、小写命令名。

下一步可以加 `DEL`/`EXPIRE`/`TTL`（在 `server.py` 的 `_commands` 表里加一个 handler 即可），或者用 `selectors` 把 thread-per-connection 换成单线程事件循环——那才是真实 Redis 的模型。