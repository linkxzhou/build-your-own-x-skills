The user wants to implement "Write yourself a Git!" (wyag - the tutorial from "Build your own X") in Python from scratch. They want me to plan milestones and only complete the first phase.

Let me first check the workspace to see what's there. The workspace is named "build-your-own-x-git-git-wyag-thb-lt-1" which suggests it's related to the wyag tutorial (wyag.thb.lt).

Let me explore the workspace first, then plan milestones, and complete only phase 1.

The wyag tutorial (https://wyag.thb.lt/) covers:
1. Introduction
2. Creating a new repository (init)
3. Parsing commit objects
4. Reconstructing commit history (log)
5. Content-addressable storage: object model (hash-object, cat-file)
6. Finding files (ls-files, index)
7. Staging files (add)
8. Committing (commit)
9. Trees (ls-tree, checkout)
10. References (branch, tag, checkout)
11. Resolving HEAD (rev-parse)
12. The branch command
13. The tag command
14. Diff (diff)
15. Syncing (fetch, push)
16. Cloning (clone)

So a reasonable milestone plan:
- Phase 1 (M1): Foundation — repo model, `init`, object storage (blob/tree/commit), `hash-object`, `cat-file`
- Phase 2 (M2): History — commit parsing, `log`
- Phase 3 (M3): Index & staging — `ls-files`, `add`, `rm`
- Phase 4 (M4): Commit & trees — `commit`, `ls-tree`, `checkout`
- Phase 5 (M5): References — `branch`, `tag`, `rev-parse`, HEAD resolution
- Phase 6 (M6): Diff & sync — `diff`, `fetch`, `push`, `clone`

Phase 1 should include: project skeleton, `wyag init`, object model (blob, tree, commit), `hash-object`, `cat-file`. Actually in the tutorial, the order is: init → parsing commits → log → object storage (cat-file, hash-object). But logically, object storage comes before commit parsing. The tutorial's actual order is a bit pedagogical. For a clean implementation, Phase 1 = repo + init + object model + hash-object + cat-file.

Let me check the workspace first to see if there's anything there.

I should:
1. Explore workspace (glob to see what's there)
2. Maybe fetch the wyag tutorial to align with it
3. Create plan with milestones
4. Implement Phase 1
5. Verify with tests

Let me start. The user speaks Chinese, so I should respond in Chinese.

Let me check the workspace contents first.空目录，Python 3.14.7。先拉取 wyag 教程原文对齐命令清单，再定里程碑。The tutorial structure is confirmed. Now let me plan milestones and implement Phase 1.

Milestones (aligned with wyag tutorial):
- M1 (Phase 1): 仓库地基 — GitRepository 模型、`init`、`repo_find`、对象模型（blob/tree/commit 读取）、`object read/write`、`cat-file`、`hash-object`
- M2: 提交历史 — commit 解析、`log`、Merkle DAG 理论
- M3: 树与检出 — tree 解析/写入、`ls-tree`、`checkout`
- M4: 引用系统 — refs、`show-ref`、tag（轻量+附注）、`branch`、`object_find`、`rev-parse`
- M5: 暂存区与索引 — index 读写、`ls-files`、`check-ignore`、`status`、`rm`、`add`、`commit`
- M6: 同步 — `fetch`、`push`、`clone`（教程里其实有 diff 吗？看目录没有 diff 章节。目录里没有 diff。教程最终实现 init, add, rm, status, commit, log, ls-tree, cat-file, checkout, clone, fetch, push, show-ref, tag, ls-files, check-ignore, hash-object, branch, rev-parse）

Wait, the TOC doesn't show fetch/push/clone sections... Let me check: sections are 1-10: intro, getting started, init, objects (hash-object, cat-file), log, checkout (ls-tree, checkout), refs/tags/branches (show-ref, tag, branch, rev-parse), staging area (index, ls-files, check-ignore, status), committing (index_write, rm, add, commit), final words. Hmm, the intro says "init, add, rm, status, commit, log…". The TOC I got doesn't show fetch/push/clone/diff. Actually the real wyag tutorial does have fetch/push/clone sections (sections 10-12 in the original). But this fetched version (updated July 2026) shows only up to section 10 "Final words". Interesting — maybe the newer version dropped them, or the TOC was truncated. The TOC clearly lists up to "10. Final words". So the current version of the tutorial covers: init, hash-object, cat-file, log, ls-tree, checkout, show-ref, tag, branch, rev-parse, ls-files, check-ignore, status, rm, add, commit.

Hmm wait, actually the original wyag has sections: 10. diff? No. Original wyag TOC: 1 intro, 2 getting started, 3 init, 4 objects, 5 log, 6 checkout, 7 refs/tags/branches, 8 staging area/index, 9 committing, 10 final words. Yes! The original wyag doesn't have fetch/push/clone either — I was confusing it with "build your own git" other tutorials. Actually no — wyag does mention clone in the intro ("and even a clone command"?). Let me not worry; the fetched TOC is authoritative: no fetch/push/clone sections. But the intro text says "implement all the fundamental features of git: init, add, rm, status, commit, log…". 

Hmm, actually I recall wyag does have a clone section... Let me check the truncated part. The fetch was truncated at 30057 chars with 27266 truncated. The TOC is complete though (it lists 10 sections ending with Final words). So the tutorial as it stands covers those commands. Fine.

So my milestone plan:

- M1（本次交付）: 地基 — 项目骨架 + `init` + 对象存储（blob/tree/commit/tag 的读写）+ `cat-file` + `hash-object` + `repo_find`
- M2: 历史与树 — commit 解析、`log`、tree 解析/写入、`ls-tree`、`checkout`
- M3: 引用 — refs、`show-ref`、tag 对象、`tag`、`branch`、`object_find`、`rev-parse`
- M4: 索引与暂存 — index 读写、`ls-files`、`check-ignore`、`status`
- M5: 提交闭环 — `rm`、`add`、`commit`，端到端验证（init→add→commit→log 全链路）

Phase 1 scope (from tutorial sections 3-4):
- GitRepository class (worktree, gitdir, conf, repo_find)
- init command (repo_create): .git structure — objects, refs, refs/heads, refs/tags, HEAD, config, description
- Object model: GitObject base, GitBlob, GitCommit, GitTree (read side for commit/tree minimal), object_read, object_write
- cat-file (type + pretty print)
- hash-object (write blob)

Per the tutorial, in section 4 the object classes are: GitObject (base with serialize/deserialize), GitBlob. GitCommit and GitTree come later (sections 5 and 6). For Phase 1, I'll implement GitObject base + GitBlob fully, and object_read that dispatches on type — for commit/tree/tag I can raise "not implemented yet" or implement raw passthrough. Actually cat-file -p on a commit would need commit parsing (M2). To keep phase boundaries clean: Phase 1 implements blob fully; object_read handles blob; for other types, store a raw placeholder that cat-file can dump raw bytes (cat-file -p dumps raw for unknown types in tutorial? In tutorial, cat-file pretty-prints via serialize; for blob it's raw. For commit it would fail until M2).

Hmm, but to make cat-file useful for verification against real git, I could implement a generic raw object for commit/tree/tag that just dumps bytes. The tutorial's GitObject.deserialize raises for unknown; GitBlob handles blob. For phase 1, I'll add a minimal raw passthrough for commit/tree/tag so cat-file -p works (dump raw), and M2/M3 will replace with real parsers. Actually — simpler and truer to the tutorial: implement GitBlob only, and object_read raises Exception for other types with a clear message. But then verifying against real git repos (cat-file a commit) fails. 

The tutorial itself: object_read dispatches k to class map {b'commit': GitCommit, b'tree': GitTree, b'tag': GitTag, b'blob': GitBlob} — but at that point in the tutorial only GitBlob and GitObject exist; the others are defined later. The tutorial code at section 4 references classes defined in later sections (the final code has them all). Since we're building the final program incrementally, I'll define GitCommit/GitTree/GitTag as raw passthrough stubs in M1 (deserialize stores raw bytes, serialize returns them), then upgrade in M2/M3. That keeps cat-file functional for all types from day one, which is genuinely useful.

Actually, let me reconsider: keep it minimal and honest. Phase 1 = sections 3+4 of tutorial:
- wyag.py CLI skeleton with subcommand dispatch
- repo_create, repo_find, GitRepository
- object_read, object_write, GitObject, GitBlob, plus raw stubs for commit/tree/tag (documented as upgraded in M2/M3)
- cmd_cat_file, cmd_hash_object

Also config file: init writes a minimal config (repositoryformatversion=0, filemode=true, bare=false). repo_find walks up parents.

Testing: verify against real git — create repo with wyag init, then `git status` should recognize it; hash-object output must match `git hash-object`; cat-file on a real git repo's objects must match `git cat-file`. That's a strong verification. Also `git cat-file -p` on our written objects.

Note: git may complain about ownership ("detected dubious ownership") — can set GIT_CONFIG_GLOBAL or use -C with safe.directory. We'll see in the sandbox. Also newer git might require `git config --global --add safe.directory`. I'll handle if it appears.

Project layout: single file `wyag.py` like the tutorial? Or a package? The tutorial uses a single wyag.py. For a from-scratch learning project, single file is faithful and simple. I'll do single `wyag.py` + `README.md` (milestones) + `tests/test_phase1.sh` or a pytest? Keep it light: a shell-based smoke test script `tests/phase1_test.sh` that verifies against real git. Actually a Python test file using subprocess might be cleaner cross-platform, but shell is fine on macOS. I'll write `tests/test_phase1.py` with pytest? pytest may not be installed. Use plain python script with asserts, runnable via `python3 tests/test_phase1.py`. That avoids dependencies.

Let me now write the plan, then implement.

Plan steps:
1. s1: 写 README.md 里程碑规划（M1-M5）
2. s2: 实现 wyag.py 骨架 + repo 模型 + init
3. s3: 实现对象存储 + cat-file + hash-object
4. s4: 写 tests/test_phase1.py（对照真实 git 验证）
5. s5: 运行验证，修复问题

Let me write the code. Faithful to wyag but my own implementation.

Key details from the tutorial:

repo_create:
```
os.makedirs(worktree/.git)
os.makedirs(.git/objects)
os.makedirs(.git/refs/heads)
os.makedirs(.git/refs/tags)
HEAD: "ref: refs/heads/master\n"
config: [core]\n\trepositoryformatversion = 0\n\tfilemode = false\n\tbare = false\n
description: unnamed repository; edit this file 'description' to name the repository.\n
```

GitRepository: worktree, gitdir; conf parsed by configparser; repo_dir(*path), repo_file(*path, mkdir)

repo_find(path=".", required=True): walk up looking for .git dir (or path itself if .git).

object_read(repo, sha): read .git/objects/sha[:2]/sha[2:], zlib decompress, parse "type size\x00content", dispatch to class.

object_write(obj, repo, actually_write): serialize, header "fmt sp size \x00", sha1, path, zlib compress, write if actually_write and not exists.

GitObject: fmt attribute; deserialize(data) classmethod; serialize(self).

GitBlob: fmt=b'blob', raw passthrough.

cat-file: wyag cat-file TYPE OBJECT — verify type matches, print serialize() to stdout (binary safe: sys.stdout.buffer.write).

hash-object: wyag hash-object [-t TYPE] [-w] PATH — compute sha, optionally write, print sha.

argparse setup with subparsers, set_defaults(func=...).

Also `wyag init [path]` with --bare? Tutorial has --bare option. I'll include bare support minimal (gitdir = path, worktree None). Keep it: tutorial includes it, it's cheap.

Edge: Python 3.14 — argparse fine, zlib fine, hashlib fine.

For the raw stubs of commit/tree/tag: I'll name them GitCommit/GitTree/GitTag with fmt and raw passthrough deserialize/serialize, with docstring "M2/M3 will add real parsing". This makes cat-file -p work on any object type immediately.

CLI name: `wyag.py`. Entry: `if __name__ == "__main__": main()`.

Test plan (tests/test_phase1.py):
1. init in temp dir → check .git layout (objects, refs/heads, refs/tags, HEAD content, config parse)
2. real git recognizes repo: `git -C tmp status` succeeds (need safe.directory? same user, fine)
3. hash-object matches `git hash-object` for a few files (empty, text, binary with all byte values)
4. hash-object -w then `git cat-file -p <sha>` matches content; object file exists at right path
5. cat-file -p on blob created by real git (`git hash-object -w`) matches content
6. cat-file -t matches
7. cat-file on commit object from a real git repo (git init + git commit via real git) — raw dump equals `git cat-file commit <sha>`? Hmm, `git cat-file -p` for commit prints raw commit content. Our raw passthrough prints the content bytes, which equals what git cat-file -p prints. Good.
8. repo_find: run from subdirectory, finds root repo.
9. cat-file with wrong type errors with exit code non-zero.

Also verify zlib object file format: `git cat-file -p` works on our written object (already covered by 4).

Let me also make sure hash-object -t tree/commit works (write arbitrary type) — tutorial supports -t with any of blob/commit/tag/tree.

Now write files. Single wyag.py, README.md, tests/test_phase1.py.

Let me write the code carefully.

```python
#!/usr/bin/env python3
"""wyag — Write Yourself A Git. 阶段一：仓库地基与对象存储。"""

import argparse
import configparser
import hashlib
import os
import sys
import zlib

# ---------- Repository ----------

class GitRepository:
    """一个 git 仓库：工作树 + .git 目录。"""

    def __init__(self, worktree, gitdir, force=False):
        self.worktree = worktree
        self.gitdir = gitdir

        conf = configparser.ConfigParser()
        corepath = os.path.join(gitdir, "config")
        if os.path.exists(corepath):
            conf.read(corepath)
        elif not force:
            raise Exception(f"配置文件缺失: {corepath}")

        if not force:
            vers = int(conf.get("Core", "repositoryformatversion", fallback="0"))
            if vers != 0:
                raise Exception(f"不支持的 repositoryformatversion {vers}")

        self.conf = conf

    def repo_path(self, *path):
        return os.path.join(self.gitdir, *path)

    def repo_dir(self, *path, mkdir=False):
        path = self.repo_path(*path)
        if os.path.exists(path):
            if os.path.isdir(path):
                return path
            raise Exception(f"目录被文件占用: {path}")
        if mkdir:
            os.makedirs(path)
            return path

    def repo_file(self, *path, mkdir=False):
        if self.repo_dir(*path[:-1], mkdir=mkdir):
            return self.repo_path(*path)
```

Wait, tutorial's repo_file: `if repo_dir(*path[:-1], mkdir=mkdir): return repo_path(*path)`. If dir exists already, repo_dir returns path (truthy). OK.

repo_create:

```python
def repo_create(path):
    repo = GitRepository(path, os.path.join(path, ".git"))

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} 不是目录")
        if os.listdir(repo.worktree):
            raise Exception(f"{path} 非空")   # hmm, tutorial doesn't check non-empty
```

Tutorial doesn't refuse non-empty (git init works in non-empty dirs). Skip that check — trust tutorial behavior. Actually git init in non-empty dir is fine and common. Don't add checks beyond tutorial.

```python
def repo_create(path):
    repo = GitRepository(path, os.path.join(path, ".git"), force=True)
    os.makedirs(repo.gitdir)  # fails if exists? tutorial: os.makedirs(repo.worktree, exist_ok=True)? 
```

Tutorial:
```python
def repo_create(path):
    """Create a new repository at path."""
    repo = GitRepository(path, os.path.join(path, ".git"), force=True)
    # First, we make sure the path either doesn't exist or is an empty dir.
    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception ("%s is not a directory!" % path)
        if os.listdir(repo.worktree):
            raise Exception("%s is not empty!" % path)
    else:
        os.makedirs(repo.worktree)
```

Hmm wait, actually the tutorial does check non-empty? Let me recall... The actual wyag code:

```python
def repo_create(path):
  """Create a new repository at path."""

  repo = GitRepository(path, os.path.join(path, ".git"), force=True)

  # First, we make sure the path either doesn't exist or is an
  # empty dir.

  if os.path.exists(repo.worktree):
    if not os.path.isdir(repo.worktree):
      raise Exception ("%s is not a directory!" % path)
    if os.listdir(repo.worktree):
      raise Exception("%s is not empty!" % path)
  else:
    os.makedirs(repo.worktree)
```

Yes, wyag does refuse non-empty dirs. Hmm, that's actually what wyag does (it's stricter than git). I'll follow wyag. Actually wait — is that right? git init in a non-empty directory works. wyag refuses. Since we're following wyag, and it's phase 1, I'll follow wyag's behavior but... hmm, for usability `wyag init .` in a dir with files would fail. The tutorial chose strictness. I'll keep wyag behavior — it's the reference. Actually, let me reconsider: the user said "从零实现「给自己写一个 Git！」" — following the wyag tutorial. Faithfulness to the tutorial is the spec here. Keep wyag behavior.

Then:
```python
    assert repo.repo_dir("branches", mkdir=True)
    assert repo.repo_dir("objects", mkdir=True)
    assert repo.repo_dir("refs", "tags", mkdir=True)
    assert repo.repo_dir("refs", "heads", mkdir=True)

    # .git/description
    with open(repo.repo_path("description"), "w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

    with open(repo.repo_path("config"), "w") as f:
        f.write("[core]\n" +
                "\trepositoryformatversion = 0\n" +
                "\tfilemode = false\n" +
                "\tbare = false\n")

    with open(repo.repo_path("HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    return repo
```

Hmm, wyag also creates .git/branches? Yes: `assert repo.repo_dir("branches", mkdir=True)`. OK.

repo_find:

```python
def repo_find(path=".", required=True):
    path = os.path.realpath(path)
    if os.path.isdir(os.path.join(path, ".git")):
        return GitRepository(path, os.path.join(path, ".git"))
    parent = os.path.realpath(os.path.dirname(path))
    if parent == path:
        if required:
            raise Exception("未找到 git 目录")
        return None
    return repo_find(parent, required)
```

Objects:

```python
class GitObject:
    repo = None

    def serialize(self, repo):
        raise Exception("子类未实现 serialize")

    def deserialize(self, data):
        raise Exception("子类未实现 deserialize")

    @classmethod
    def read(cls, repo, sha): ...
```

Tutorial has object_read as module function. I'll follow tutorial style: module functions object_read(repo, sha), object_write(obj, repo, actually_write=True), and classes GitObject/GitBlob/GitCommit/GitTree/GitTag.

```python
def object_read(repo, sha):
    path = repo.repo_file("objects", sha[0:2], sha[2:])
    if not os.path.isfile(path):
        raise Exception(f"对象不存在: {sha}")
    with open(path, "rb") as f:
        raw = zlib.decompress(f.read())
    space = raw.find(b" ")
    fmt = raw[0:space]
    nul = raw.find(b"\x00", space)
    size = int(raw[space:nul].decode("ascii"))
    if size != len(raw) - nul - 1:
        raise Exception(f"对象大小校验失败: {sha}")
    klass = OBJECT_CLASSES.get(fmt)
    if klass is None:
        raise Exception(f"未知对象类型: {fmt.decode('ascii')}")
    return klass(repo, raw[nul + 1:])
```

Tutorial: klass = {b'commit': GitCommit, b'tree': GitTree, b'tag': GitTag, b'blob': GitBlob}[fmt]; return klass(repo, data). And each class's __init__ calls deserialize. I'll do:

```python
class GitObject:
    fmt = None

    def __init__(self, repo=None, data=None):
        self.repo = repo
        if data is not None:
            self.deserialize(data)
```

object_write:

```python
def object_write(obj, actually_write=True):
    data = obj.serialize()
    result = obj.fmt + b" " + str(len(data)).encode() + b"\x00" + data
    sha = hashlib.sha1(result).hexdigest()
    if actually_write:
        path = obj.repo.repo_file("objects", sha[0:2], sha[2:], mkdir=True)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(zlib.compress(result))
    return sha
```

GitBlob:
```python
class GitBlob(GitObject):
    fmt = b"blob"
    def serialize(self):
        return self.blobdata
    def deserialize(self, data):
        self.blobdata = data
```

Stubs for commit/tree/tag (raw passthrough, upgraded in later phases):
```python
class GitCommitRaw(GitObject):  # hmm naming
```

Actually simpler: name them GitCommit, GitTree, GitTag with raw passthrough and docstrings noting real parsing lands in M2/M3. When M2 arrives, GitCommit gains kvlm parsing. Fine.

cat-file:

```python
def cmd_cat_file(args):
    repo = repo_find()
    obj = object_read(repo, args.object)  # tutorial: cat-file only accepts full sha in phase 4
    if obj.fmt.decode() != args.type:
        raise Exception(f"类型不匹配: 请求 {args.type}, 实际 {obj.fmt.decode()}")
    sys.stdout.buffer.write(obj.serialize())
```

Wait tutorial cat-file: `cat_file(repo, obj, args.type)` checks `if cat_file... fmt != args.type: raise`. And object_find is introduced later (section 7); at section 4, cat-file takes full sha. Keep full-sha only in M1 (rev-parse/object_find comes in M3). Good — document that.

hash-object:

```python
def cmd_hash_object(args):
    if args.write:
        repo = repo_find()
    else:
        repo = None
    with open(args.path, "rb") as f:
        data = f.read()
    obj = OBJECT_TYPE_MAP[args.type](repo, data)  # hmm
```

Tutorial:
```python
def cmd_hash_object(args):
  if args.write:
    repo = GitRepository.find()
  else:
    repo = None

  with open(args.path, "rb") as fd:
    sha = object_hash(fd.read(), args.type.encode(), repo)
    print(sha)

def object_hash(data, fmt, repo=None):
  """Hash object, possibly writing it to repo."""
  obj = object_class(fmt)()
  if obj is None:
    raise Exception(f"Unknown type {fmt}!")
  obj.deserialize(data)
  return object_write(obj, repo, actually_write=repo is not None)
```

I'll do similar: object_hash(data, fmt, repo=None).

object_class(fmt) helper returns class or None.

CLI:

```python
argparser = argparse.ArgumentParser(prog="wyag", description="Write Yourself A Git — 教学版 Git")

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    if hasattr(args, "func"):
        args.func(args)
    else:
        argparser.print_help()
```

Subcommands:
- init: p = sub.add_parser("init"); p.add_argument("directory", nargs="?", default="."); p.add_argument("--bare", action="store_true"); p.set_defaults(func=cmd_init)

cmd_init:
```python
def cmd_init(args):
    repo = repo_create(args.directory, args.bare)  # hmm bare handling
    print(f"已初始化空 Git 仓库: {repo.gitdir}")
```

Tutorial init with bare: gitdir = os.path.abspath(path) if bare else os.path.join(path, ".git"). And message: `print(f"Initialized empty wyag repository in {repo.gitdir}")`. I'll support --bare similarly.

Wait, with bare, GitRepository(path, gitdir) where worktree=path? Tutorial: `GitRepository(os.path.abspath(path), os.path.abspath(path), force=True)` for bare — worktree == gitdir. OK, follow that.

- cat-file: p.add_argument("type", choices=["blob","commit","tag","tree"]); p.add_argument("object")
- hash-object: p.add_argument("-t", dest="type", default="blob", choices=[...]); p.add_argument("-w", dest="write", action="store_true"); p.add_argument("path")

Also add repo_find to GitRepository as classmethod? Tutorial: GitRepository.find(path=".", required=True) classmethod calling module repo_find. I'll just use module function repo_find.

Now the test file. tests/test_phase1.py, plain python, no deps:

```python
#!/usr/bin/env python3
"""阶段一验收：wyag init / hash-object / cat-file 对照真实 git。"""
import os, subprocess, sys, tempfile, shutil, hashlib

WYAG = os.path.join(os.path.dirname(__file__), "..", "wyag.py")

def run(cmd, cwd=None, check=True, input=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, input=input)
    if check and r.returncode != 0:
        raise AssertionError(f"命令失败: {cmd}\nstdout={r.stdout!r}\nstderr={r.stderr!r}")
    return r

def wyag(*args, cwd=None, check=True):
    return run([sys.executable, WYAG, *args], cwd=cwd, check=check)

def git(*args, cwd=None, check=True):
    return run(["git", *args], cwd=cwd, check=check)
```

Tests:
1. test_init_layout: temp dir, wyag init → assert .git/objects, .git/refs/heads, .git/refs/tags, .git/branches exist; HEAD == "ref: refs/heads/master\n"; config contains repositoryformatversion = 0; description exists.
2. test_git_recognizes: git -C tmp rev-parse --is-inside-work-tree → "true"; git status succeeds.
3. test_hash_object_matches_git: files: empty, b"hello wyag\n", bytes(range(256)), random binary; for each: wyag hash-object f == git hash-object f.
4. test_hash_object_write: wyag hash-object -w f → sha; object file exists at .git/objects/sha[:2]/sha[2:]; git cat-file -p sha == content; git cat-file -t sha == blob.
5. test_cat_file_read_git_object: in a wyag-inited repo, use real git to write objects: git hash-object -w --stdin (needs git env ok in wyag repo — fine), then wyag cat-file -p sha == git cat-file -p sha; also -t.
6. test_cat_file_commit_raw: create real commit with git (config user.email etc.), get sha via git rev-parse HEAD, wyag cat-file -p sha == git cat-file -p sha (raw passthrough). Also wyag cat-file -t sha == commit.
7. test_repo_find_from_subdir: mkdir -p a/b/c, run wyag hash-object -w from a/b/c → object lands in root .git.
8. test_cat_file_wrong_type_fails: wyag cat-file tree <blob-sha> → nonzero exit.
9. test_hash_object_other_types: wyag hash-object -t commit -w file → git cat-file -t == commit (loose object of type commit). Hmm, git cat-file -t on a loose "commit" object written that way returns commit. Yes.
10. test_init_refuses_nonempty? wyag init in non-empty dir should fail (wyag behavior). Assert nonzero exit. Hmm — but is that behavior we want to lock in? It's wyag's behavior; fine to test.

Also test bare init? wyag init --bare → HEAD exists at path directly. git recognizes bare repo: git -C barepath rev-parse --is-bare-repository → true. Nice check.

Note: git may complain about dubious ownership if temp dirs are owned differently — same user, should be fine. Also git commit needs user.name/email: set with -c user.name=t -c user.email=t@t or env GIT_AUTHOR_NAME etc. Use `git -c user.name=wyag -c user.email=wyag@test commit --allow-empty -m init`. Also need `git init` first (real git init in separate dir, or reuse wyag repo — better: reuse wyag-created repo to double-check compatibility: git -C wyagrepo add/commit works). For test 6, do: wyag init tmp; then git -C tmp -c ... commit --allow-empty -m "x" — real git writes commit+tree objects into our .git; then wyag cat-file reads them. That's a great cross-check both directions.

Edge: git version on macOS — fine.

Also `git status` in wyag repo: git might warn about default branch name? No, status is fine.

One more: HEAD ref refs/heads/master doesn't exist yet; git rev-parse HEAD fails but rev-parse --is-inside-work-tree works. Use the latter.

Now README.md with milestone plan:

# wyag — 给自己写一个 Git
里程碑:
- M1 阶段一（本次）: 仓库地基 — init / repo_find / 对象读写 / cat-file / hash-object
- M2: 历史与树 — commit 解析(kvlm) / log / tree 解析与写入 / ls-tree / checkout
- M3: 引用系统 — show-ref / tag(轻量+附注) / branch / object_find / rev-parse
- M4: 索引与状态 — index 读写 / ls-files / check-ignore / status
- M5: 提交闭环 — rm / add / commit + 端到端验收（init→add→commit→log→checkout）

Each milestone: scope, commands, acceptance criteria.

Also usage section: python3 wyag.py init etc.

Let me also think about whether to make wyag executable with shebang — yes, chmod +x.

Now, about `explore` tool requirement: "Before modifying code, call `explore` once to record the files you have read (or intend to read)". The workspace is empty; I've read the tutorial TOC. I'll call explore once to record, then plan, then implement. The instructions say to use explore before modifying code — I'll comply briefly.

Then plan with seed_todos=true, then write files, then run tests.

Let me write everything now. I'll be careful with the code details.

One detail: in object_read, tutorial checks `if size != len(raw)-nul-1: raise`. Keep.

In repo_file with mkdir: repo_file("objects", sha[:2], sha[2:], mkdir=True) — repo_dir(*path[:-1], mkdir=mkdir) creates objects/xx dir. Good.

cat-file output: use sys.stdout.buffer.write(obj.serialize()) — binary safe.

For hash-object printing: print(sha).

Error handling in main: catch Exception, print to stderr, exit 1? Tutorial doesn't catch (traceback). For a teaching tool, traceback is actually informative. But tests for failure cases just need nonzero exit — uncaught exception gives exit 1. Hmm, but ugly. I'll catch in main and print f"fatal: {e}" to stderr, exit 1. Cleaner CLI. Keep it.

Wait — but then debugging is harder for later phases. Compromise: catch Exception, print fatal message; that's what git does. Fine.

argparse: subparsers = argparser.add_subparsers(title="命令", dest="command"); each with required? If no args, print help. main: if not hasattr(args, "func"): argparser.print_help(); sys.exit(1)? Or return 2. Fine.

Python 3.14: configparser fine. Note: conf.get("Core", ...) — configparser section names case-sensitive; we write "[core]" lowercase; tutorial uses conf.get("Core", ...) with fallback... Actually tutorial writes "[core]" and reads with `conf.get("Core", "repositoryformatversion")`? Let me recall:

```python
    if not force:
      vers = int(conf.get("Core", "repositoryformatversion"))
```

Hmm, configparser by default lowercases option names but section names are case-sensitive. wyag writes "[core]" and reads "Core"?? That would fail... Actually no — wyag's repo_create writes:

```python
    with open(repo.repo_path("config"), "w") as f:
      f.write("[core]\n" + ...)
```

and GitRepository reads:

```python
      vers = int(conf.get("Core", "repositoryformatversion"))
```

Hmm, that would raise NoSectionError. I think wyag actually reads "Core"... Let me not rely on memory: I'll write "[core]" and read conf.get("core", ...) — consistent, correct. My own implementation, my own consistency.

Also when reading real git repos' config, section is [core] lowercase. Good.

Now GitRepository.__init__ signature: (worktree, gitdir, force=False). For bare, worktree=gitdir=path.

Let me also handle `repo_find` when path itself is a gitdir? Tutorial only checks .git subdir. Keep.

Alright, also the `wyag init` message: print(f"Initialized empty Git repository in {repo.gitdir}") — mirror git's message. Chinese or English? Code comments/messages: user speaks Chinese; I'll use Chinese comments and messages. Hmm, CLI messages in Chinese are fine for a personal teaching project. I'll use Chinese for comments, English-ish for CLI messages? Mixed is ugly. Decide: comments in Chinese (user's language), CLI output messages in Chinese too. Tests assert on behavior, not messages. OK.

Actually for git-compat feel, keep CLI messages like git: "已初始化空 Git 仓库：/path/.git". Fine.

Let me write the files now.

wyag.py full code:

```python
#!/usr/bin/env python3
"""wyag —— Write Yourself A Git（教学版）。

阶段一（M1）：仓库地基与内容寻址对象存储。
  - wyag init [--bare] [目录]
  - wyag cat-file TYPE 对象
  - wyag hash-object [-t TYPE] [-w] 文件

后续里程碑见 README.md。
"""

import argparse
import configparser
import hashlib
import os
import sys
import zlib


# ---------------------------------------------------------------------------
# 仓库模型
# ---------------------------------------------------------------------------

class GitRepository:
    """一个 Git 仓库 = 工作树（worktree）+ .git 目录（gitdir）。"""

    def __init__(self, worktree, gitdir, force=False):
        self.worktree = worktree
        self.gitdir = gitdir

        conf = configparser.ConfigParser()
        core = os.path.join(gitdir, "config")
        if os.path.isfile(core):
            conf.read(core)
        elif not force:
            raise Exception(f"配置文件缺失：{core}")

        if not force:
            vers = int(conf.get("core", "repositoryformatversion", fallback="0"))
            if vers != 0:
                raise Exception(f"不支持的 repositoryformatversion：{vers}")

        self.conf = conf

    # 路径助手 ------------------------------------------------------------

    def repo_path(self, *path):
        """gitdir 下的路径。"""
        return os.path.join(self.gitdir, *path)

    def repo_dir(self, *path, mkdir=False):
        """gitdir 下的目录；mkdir=True 时按需创建。"""
        p = self.repo_path(*path)
        if os.path.exists(p):
            if os.path.isdir(p):
                return p
            raise Exception(f"应为目录，实际是文件：{p}")
        if mkdir:
            os.makedirs(p)
        return p

    def repo_file(self, *path, mkdir=False):
        """gitdir 下的文件；mkdir=True 时先创建父目录。"""
        if self.repo_dir(*path[:-1], mkdir=mkdir):
            return self.repo_path(*path)

    @staticmethod
    def find(path=".", required=True):
        """从 path 逐级向上查找包含 .git 的目录。"""
        return repo_find(path, required)
```

Hmm wait, repo_file returns None if dir creation not requested and missing... tutorial same. Fine.

repo_create:

```python
def repo_create(path, bare=False):
    """在 path 创建新仓库；bare=True 时创建裸仓库。"""
    if bare:
        wt = gd = os.path.abspath(path)
    else:
        wt = os.path.abspath(path)
        gd = os.path.join(wt, ".git")
    repo = GitRepository(wt, gd, force=True)

    if os.path.exists(repo.worktree):
        if not os.path.isdir(repo.worktree):
            raise Exception(f"{path} 不是目录！")
        if os.listdir(repo.worktree):
            raise Exception(f"{path} 不是空目录！")
    else:
        os.makedirs(repo.worktree)

    assert repo.repo_dir("branches", mkdir=True)
    assert repo.repo_dir("objects", mkdir=True)
    assert repo.repo_dir("refs", "tags", mkdir=True)
    assert repo.repo_dir("refs", "heads", mkdir=True)

    with open(repo.repo_path("description"), "w") as f:
        f.write("Unnamed repository; edit this file 'description' to name the repository.\n")

    with open(repo.repo_path("config"), "w") as f:
        f.write("[core]\n"
                "\trepositoryformatversion = 0\n"
                "\tfilemode = false\n"
                "\tbare = false\n")

    with open(repo.repo_path("HEAD"), "w") as f:
        f.write("ref: refs/heads/master\n")

    return repo
```

Hmm wait: for bare repo, worktree == gitdir == path; the non-empty check would refuse existing non-empty dir — same as wyag. But config writes "bare = false" even for bare... wyag does that too (it always writes bare=false; it's a known simplification). Hmm, for bare let me write bare = true. Small improvement, harmless. Actually wyag writes bare=false always. But then git rev-parse --is-bare-repository on our bare repo: git determines bare-ness from... core.bare config! If we write bare=false in a bare layout, git may treat it as non-bare with worktree=parent? That could break test "git recognizes bare". Let me write bare = true when bare. Deviation from wyag but correct. I'll do it.

Also for bare, worktree check: os.listdir on existing dir — if user does `wyag init --bare newdir` and newdir doesn't exist, makedirs. OK.

repo_find:

```python
def repo_find(path=".", required=True):
    """自 path 向上查找仓库根；找不到时按 required 决定报错或返回 None。"""
    path = os.path.realpath(path)

    if os.path.isdir(os.path.join(path, ".git")):
        return GitRepository(path, os.path.join(path, ".git"))

    parent = os.path.realpath(os.path.dirname(path))
    if parent == path:
        if required:
            raise Exception("没有找到 .git 目录，不在 Git 仓库中")
        return None
    return repo_find(parent, required)
```

Objects:

```python
# ---------------------------------------------------------------------------
# 内容寻址对象
# ---------------------------------------------------------------------------

class GitObject:
    """所有 git 对象的基类：fmt 是对象类型字节串。"""

    fmt = None

    def __init__(self, repo=None, data=None):
        self.repo = repo
        if data is not None:
            self.deserialize(data)

    def serialize(self):
        """对象内容 -> 字节串，由子类实现。"""
        raise Exception("子类必须实现 serialize()")

    def deserialize(self, data):
        """字节串 -> 对象内容，由子类实现。"""
        raise Exception("子类必须实现 deserialize()")


class GitBlob(GitObject):
    """blob：原始文件内容，原样存取。"""

    fmt = b"blob"

    def serialize(self):
        return self.data

    def deserialize(self, data):
        self.data = data


class GitCommit(GitObject):
    """commit：M1 先按原始字节透传，M2 实现 kvlm 解析。"""

    fmt = b"commit"

    def serialize(self):
        return self.data

    def deserialize(self, data):
        self.data = data


class GitTree(GitObject):
    """tree：M1 先按原始字节透传，M3 实现解析与写入。"""

    fmt = b"tree"

    def serialize(self):
        return self.data

    def deserialize(self, data):
        self.data = data


class GitTag(GitObject):
    """tag（附注标签）：M1 先按原始字节透传，M3 实现 kvlm 解析。"""

    fmt = b"tag"

    def serialize(self):
        return self.data

    def deserialize(self, data):
        self.data = data


OBJECT_CLASSES = {
    GitBlob.fmt: GitBlob,
    GitCommit.fmt: GitCommit,
    GitTree.fmt: GitTree,
    GitTag.fmt: GitTag,
}


def object_class(fmt):
    return OBJECT_CLASSES.get(fmt)


def object_read(repo, sha):
    """从 .git/objects 读取并解压对象，返回对应的 GitObject。"""
    path = repo.repo_file("objects", sha[0:2], sha[2:])

    if not os.path.isfile(path):
        raise Exception(f"对象不存在：{sha}")

    with open(path, "rb") as f:
        raw = zlib.decompress(f.read())

    # 头部格式："<type> <size>\x00<content>"
    space = raw.find(b" ")
    fmt = raw[0:space]
    nul = raw.find(b"\x00", space)
    size = int(raw[space:nul].decode("ascii"))
    if size != len(raw) - nul - 1:
        raise Exception(f"对象长度校验失败：{sha}")

    klass = object_class(fmt)
    if klass is None:
        raise Exception(f"未知对象类型：{fmt.decode('ascii')}")

    return klass(repo, raw[nul + 1:])


def object_write(obj, actually_write=True):
    """序列化对象，计算 SHA-1；actually_write 时写入 .git/objects。"""
    data = obj.serialize()
    result = obj.fmt + b" " + str(len(data)).encode("ascii") + b"\x00" + data
    sha = hashlib.sha1(result).hexdigest()

    if actually_write:
        path = obj.repo.repo_file("objects", sha[0:2], sha[2:], mkdir=True)
        if not os.path.exists(path):
            with open(path, "wb") as f:
                f.write(zlib.compress(result))

    return sha


def object_hash(data, fmt, repo=None, actually_write=True):
    """对 data 按类型 fmt 建对象；repo 为 None 时只算哈希不落盘。"""
    klass = object_class(fmt)
    if klass is None:
        raise Exception(f"未知对象类型：{fmt!r}")
    obj = klass(repo=repo, data=data)
    return object_write(obj, actually_write=actually_write and repo is not None)
```

Hmm, object_hash signature: tutorial object_hash(data, fmt, repo=None) writes iff repo is not None. I'll keep that: actually_write = repo is not None. Simplify:

```python
def object_hash(data, fmt, repo=None):
    klass = object_class(fmt)
    if klass is None:
        raise Exception(f"未知对象类型：{fmt!r}")
    obj = klass(repo=repo, data=data)
    return object_write(obj, actually_write=repo is not None)
```

Commands:

```python
# ---------------------------------------------------------------------------
# 命令
# ---------------------------------------------------------------------------

def cmd_init(args):
    repo = repo_create(args.directory, args.bare)
    print(f"已初始化空 Git 仓库：{repo.gitdir}")


def cmd_cat_file(args):
    repo = repo_find()
    obj = object_read(repo, args.object)
    if obj.fmt.decode("ascii") != args.type:
        raise Exception(f"类型不匹配：请求 {args.type}，实际 {obj.fmt.decode('ascii')}")
    sys.stdout.buffer.write(obj.serialize())


def cmd_hash_object(args):
    repo = repo_find(required=False) if args.write else None
    # hmm: tutorial uses GitRepository.find() when -w; if not in repo it errors. Keep required=True when write.
```

Wait: hash-object -w outside a repo should error (git does too). So repo = repo_find() if args.write else None. repo_find default required=True. Good.

```python
def cmd_hash_object(args):
    repo = repo_find() if args.write else None
    with open(args.path, "rb") as f:
        data = f.read()
    print(object_hash(data, args.type.encode("ascii"), repo))
```

CLI wiring:

```python
# ---------------------------------------------------------------------------
# 命令行入口
# ---------------------------------------------------------------------------

argparser = argparse.ArgumentParser(
    prog="wyag",
    description="Write Yourself A Git —— 教学版 Git（阶段一：init / hash-object / cat-file）")
subparsers = argparser.add_subparsers(title="命令", dest="command")

# init
p_init = subparsers.add_parser("init", help="初始化新仓库")
p_init.add_argument("directory", nargs="?", default=".", help="仓库位置（默认当前目录）")
p_init.add_argument("--bare", action="store_true", help="创建裸仓库")
p_init.set_defaults(func=cmd_init)

# cat-file
p_cat = subparsers.add_parser("cat-file", help="输出对象内容")
p_cat.add_argument("type", choices=["blob", "commit", "tag", "tree"], help="对象类型")
p_cat.add_argument("object", help="完整的 40 位 SHA-1")
p_cat.set_defaults(func=cmd_cat_file)

# hash-object
p_hash = subparsers.add_parser("hash-object", help="计算对象哈希（可选写入）")
p_hash.add_argument("-t", dest="type", default="blob",
                    choices=["blob", "commit", "tag", "tree"], help="对象类型（默认 blob）")
p_hash.add_argument("-w", dest="write", action="store_true", help="写入对象库")
p_hash.add_argument("path", help="要哈希的文件")
p_hash.set_defaults(func=cmd_hash_object)


def main(argv=None):
    args = argparser.parse_args(argv)
    if not hasattr(args, "func"):
        argparser.print_help()
        return 1
    try:
        args.func(args)
I was cut off mid-way through writing wyag.py. I need to continue: finish the main() function, then write the file, write README.md, write tests, run them. Let me continue from where I left off — the main() function was cut at `args.func(args)`. I should now actually write the files using the write tool.Now write README.md with the milestone plan, and the test file. These are independent — I can write both in parallel.测试框架存在两个问题：测试按字母顺序运行（`repo1` 尚未创建），以及 `git()` 没有传递 `input` 参数。我将使每个测试都独立，并修复 `git()`。现在我来更新所有测试，使其使用 `make_repo` 而不是共享的 `repo1`：测试使用了 git 风格的 `-t`/`-p` 标志，但 wyag 的 cat-file 采用的是教程中的位置参数接口 `cat-file TYPE OBJECT`。我来修复测试以匹配该接口：12/12 通过。最后做一次手工冒烟演示，确认 CLI 端到端可用：第一阶段完成。交付内容：

**里程碑规划**（README.md，对齐 wyag 教程 §3–§9）

| 里程碑 | 主题 | 命令 | 状态 |
|--------|------|------|------|
| M1 | 仓库地基与对象存储 | `init` / `hash-object` / `cat-file` | ✅ 本次 |
| M2 | 提交历史 | kvlm 解析、`log` | ⬜ |
| M3 | 树与引用 | `ls-tree` / `checkout` / `tag` / `branch` / `rev-parse` | ⬜ |
| M4 | 索引与状态 | index 读写、`ls-files` / `check-ignore` / `status` | ⬜ |
| M5 | 提交闭环 | `rm` / `add` / `commit` + 端到端验收 | ⬜ |

**M1 实现**（wyag.py，单文件零依赖）
- `GitRepository` + `repo_create()`：生成完整 `.git` 布局（objects、refs/heads、refs/tags、branches、HEAD、config、description），支持 `--bare`
- `repo_find()`：自当前目录逐级向上定位仓库根
- 对象模型：`"<type> <size>\x00<content>"` + zlib + SHA-1 内容寻址；blob 完整实现，commit/tree/tag 为原始透传（M2/M3 换成真实解析器），保证 `cat-file` 对任意类型立即可用
- `hash-object [-t] [-w]`、`cat-file TYPE SHA`

**验证**（tests/test_phase1.py，12/12 通过，全部与真实 git 交叉验证）
- 哈希逐字节一致：空文件、文本、全 256 字节、二进制
- 双向兼容：git 能读 wyag 写的对象、能识别 wyag 建的仓库（含裸仓库）；wyag 能读 git 写的 blob 和 commit
- 边界：非空目录拒绝 init、子目录执行写入仓库根、类型不匹配/对象缺失报错

下一步是 M2：给 `GitCommit` 换上 kvlm 解析器并实现 `log`。