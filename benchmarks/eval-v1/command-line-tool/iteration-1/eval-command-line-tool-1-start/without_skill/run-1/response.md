The user wants to build a cowsay-like CLI tool in Rust. This is a "build your own X" style task — they want to be guided through building it, not just have me dump the whole thing. Let me think about what "带我开始" means: "start with me / guide me through it". So I should scaffold the project, explain the design, and build it incrementally with them.

Let me first check the workspace to see what's there.

The workspace is `/Users/linkxzhou/skev/byox-eval/v1/base/build-your-own-x-command-line-tool-1`. Let me look at what's in it.

Plan:
1. Check workspace contents (empty? existing files?)
2. Check Rust toolchain availability
3. Scaffold a new cargo project
4. Design the cowsay clone: 
   - CLI args: message text, maybe flags like -d (dead), -t (tongue), -e eyes, -w width, -f cowfile
   - Bubble drawing: word wrap to width, bubble with `_/` and `\` corners for single line, `|` for middle lines, `\` and `/` for bottom
   - The cow ASCII art
5. Implement step by step, test

Since this is a teaching/starting task, I should keep it interactive but also make real progress. Let me start by exploring the environment, then propose a plan, then implement a minimal v1 (bubble + cow), and suggest next steps (flags, tests).

Per instructions: for multi-step change, call explore once, then plan, then todo_write, then execute. Let me do that.

First, parallel: glob to see workspace contents, bash to check cargo/rustc versions.

Let me think about the actual cowsay algorithm so I get it right:

Cowsay bubble format:
```
 ________
< hello >
 --------
```
Single line: `< message >` with `_` top and `-` bottom.

Multi-line:
```
 ________
/ hello  \
| world  |
\ foo    /
 --------
```

The bubble width = max line length + 2 (for padding). Top border: `_` repeated width. Bottom: `-` repeated width.

Lines: first line starts with `/` (if multi-line) or `<` (if single), last ends with `\` (multi-line) or `>` (single). Middle lines use `|` on both sides. Lines are padded to max width.

Word wrapping: cowsay wraps at ~40 columns by default. It breaks words longer than the width. The classic cowsay uses a greedy wrap at 40 chars.

The cow:
```
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Default eyes `oo`, tongue `  ` (two spaces). Dead: `xx` eyes, `U ` tongue. 

Let me write the Rust code:

```rust
use std::env;

const COW: &str = r#"
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
"#;
```

Actually, better to build the cow with placeholders for eyes/tongue.

Main logic:
1. Parse args: collect message from positional args; flags: `-e eyes`, `-t tongue` (cowsay uses -T for tongue), `-w wrap`, `-d` dead, `-b` borg, etc. Keep v1 simple: message + `-e` + `-T` + `-w` + `-d`.
2. Wrap text.
3. Build bubble.
4. Print bubble + cow.

Let me write clean code:

```rust
fn wrap(text: &str, width: usize) -> Vec<String> {
    let mut lines = Vec::new();
    let mut current = String::new();
    for word in text.split_whitespace() {
        // hard-break words longer than width
        let mut word = word;
        loop {
            let space = if current.is_empty() { 0 } else { 1 };
            if current.chars().count() + space + word.chars().count() <= width {
                if space == 1 { current.push(' '); }
                current.push_str(word);
                break;
            } else if current.is_empty() {
                // word alone too long: hard split
                let take: usize = word.chars().take(width).count(); // hmm
                ...
            } else {
                lines.push(std::mem::take(&mut current));
            }
        }
    }
    if !current.is_empty() { lines.push(current); }
    if lines.is_empty() { lines.push(String::new()); }
    lines
}
```

Hard-splitting long words with chars is a bit fiddly; for v1 I can do a simpler version: if a word is longer than width, push it as its own line (overflow) — but classic cowsay does break. Let me do a proper char-based hard break, it's not that hard:

```rust
fn wrap(text: &str, width: usize) -> Vec<String> {
    let mut lines: Vec<String> = Vec::new();
    let mut cur = String::new();
    let mut cur_len = 0usize;
    for word in text.split_whitespace() {
        let mut w = word;
        loop {
            let wlen = w.chars().count();
            let sep = if cur.is_empty() { 0 } else { 1 };
            if cur_len + sep + wlen <= width {
                if sep == 1 { cur.push(' '); cur_len += 1; }
                cur.push_str(w);
                cur_len += wlen;
                break;
            }
            if cur_len > 0 {
                lines.push(std::mem::take(&mut cur));
                cur_len = 0;
                continue;
            }
            // word alone exceeds width: hard break
            let mut take = String::new();
            let mut taken = 0;
            let mut rest = String::new();
            for (i, c) in w.chars().enumerate() {
                if i < width { take.push(c); taken += 1; } else { rest.push(c); }
            }
            lines.push(take);
            if taken >= wlen { break; } // w fully consumed
            w = rest.as_str(); // borrow issue: rest is local...
        }
    }
    ...
}
```

Borrow issue: `w = rest.as_str()` where rest is local to loop iteration. Need to restructure with owned String. Let me use:

```rust
let mut rest_owned: Option<String> = None;
...
```

Simpler: process word as Vec<char> chunks:

```rust
fn wrap(text: &str, width: usize) -> Vec<String> {
    let mut lines = Vec::new();
    let mut cur = String::new();
    let mut cur_len = 0usize;

    for word in text.split_whitespace() {
        let mut chars: Vec<char> = word.chars().collect();
        loop {
            let sep = usize::from(!cur.is_empty());
            if cur_len + sep + chars.len() <= width {
                if sep == 1 { cur.push(' '); cur_len += 1; }
                cur.extend(&chars);
                cur_len += chars.len();
                break;
            }
            if !cur.is_empty() {
                lines.push(std::mem::take(&mut cur));
                cur_len = 0;
                continue;
            }
            // hard break
            let head: String = chars[..width].iter().collect();
            lines.push(head);
            chars = chars[width..].to_vec();
        }
    }
    if !cur.is_empty() { lines.push(cur); }
    if lines.is_empty() { lines.push(String::new()); }
    lines
}
```

Wait, edge: if width is 0 this infinite-loops. Guard width >= 1 (or clamp to at least 1). Also if chars.len() > width but cur empty, we push head of exactly width. Fine.

Hmm, one more edge: `chars[..width]` panics if chars.len() < width — but we only get here when cur_len + sep + chars.len() > width and cur is empty, so chars.len() > width... actually chars.len() > width - 0 - 0 = width? cur_len=0, sep=0, so condition failing means chars.len() > width. So chars.len() >= width+1, safe. Good.

Bubble:

```rust
fn bubble(lines: &[String]) -> String {
    let width = lines.iter().map(|l| l.chars().count()).max().unwrap_or(0);
    let mut out = String::new();
    out.push(' ');
    out.push_str(&"_".repeat(width + 2));
    out.push('\n');
    let n = lines.len();
    for (i, line) in lines.iter().enumerate() {
        let pad = width - line.chars().count();
        let (l, r) = match (n, i) {
            (1, _) => ('<', '>'),
            (_, 0) => ('/', '\\'),
            (_, j) if j == n - 1 => ('\\', '/'),
            _ => ('|', '|'),
        };
        out.push_str(&format!("{l} {line}{} {r}\n", " ".repeat(pad)));
    }
    out.push(' ');
    out.push_str(&"-".repeat(width + 2));
    out.push('\n');
    out
}
```

Cow with eyes/tongue substitution:

```rust
fn cow(eyes: &str, tongue: &str) -> String {
    format!(
        r#"        \   ^__^
         \  ({eyes})\_______
            (__)\       )\/\
                ||----{t} |
                ||     ||
"#,
        eyes = eyes,
        t = tongue
    )
}
```

Wait, tongue in cowsay: `||----w |` — the `w` is the tongue tip? Actually the tongue appears as `U` in dead mode: `||----U |`? Let me recall. Dead cow:

```
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\
             U  ||----w |
                ||     ||
```

Hmm no. Dead cowsay:
```
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\
             U ||----w |
                ||     ||
```

Actually the tongue in cowsay replaces... Let me recall the cow file:

```
$thoughts   ^__^
 $thoughts  ($eyes)\_______
            (__)\       )\/\
 $tongue ||----w |
            ||     ||
```

Hmm, the standard cow.pf:

```
        $thoughts   ^__^
         $thoughts  ($eyes)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

And tongue: in cow files, `$tongue` appears like:

```
       \   ^__^
        \  ($eyes)\_______
           (__)\       )\/\
$tongue       ||----w |
            ||     ||
```

The default tongue is "  " (two spaces) and dead tongue is "U ". In default.cow:

```
$the_cow = <<EOC;
$thoughts   ^__^
 $thoughts  ($eyes)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
EOC
```

Hmm, that one has no tongue. three-eyes... Actually default cow has tongue position: looking at real cowsay output for -d:

```
 __________
< moo dead >
 ----------
        \   ^__^
         \  (xx)\_______
            (__)\       )\/\
             U  ||----w |
                ||     ||
```

Yes! The `U` appears before `||----w |`. So the line is `$tongue ||----w |` where tongue default is "  " (2 spaces) making it `                ||----w |` (16 spaces + ...). Wait let me count: default line `                ||----w |` — 16 spaces. With tongue "U ": `             U  ||----w |` — 13 spaces + "U " + ... hmm that gives 13+2=15 chars before `||`. That doesn't match 16.

Let me just check: default.cow actual content:

```
$the_cow = <<EOC;
        $thoughts   ^__^
         $thoughts  ($eyes)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
EOC
```

And there's a variant with tongue... The real default.cow is:

```
$the_cow = <<EOC;
        $thoughts   ^__^
         $thoughts  ($eyes)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
EOC
```

Hmm, but then how does -d show the tongue? cowsay's default.cow actually is:

```
$the_cow = <<EOC;
        $thoughts   ^__^
         $thoughts  ($eyes)\_______
            (__)\       )\/\
$tongue        ||----w |
                ||     ||
EOC
```

With $tongue = "  " (two spaces) by default: `  ` + `        ||----w |` = 10 spaces? That gives `          ||----w |` — 10 spaces. But real output shows 16 spaces. Hmm.

Let me count real cowsay output:
```
 ______
< moo  >
 ------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Line `                ||----w |`: count spaces before `||`: "                " = 16 spaces. And dead:
```
             U  ||----w |
```
"             U  " = 13 spaces + "U" + 2 spaces = 16. So tongue "U " replaces... 13 + 3 = 16, and default 16 = 14 spaces + tongue(2 spaces)? 14 + 2 = 16. Yes! So the template line is `              $tongue||----w |` where $tongue is 2 spaces default → 14+2=16. Dead tongue "U " → 14+2=16 with U at position 15. But observed dead shows U at position 14 (13 spaces then U). Hmm, 13 spaces + U = position 14. 

I'm overanalyzing pixel-perfect fidelity. For our clone, I'll do the common rendering:

Default:
```
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
```

Dead: eyes `xx`, tongue line becomes `             U  ||----w |`. I'll implement tongue as a 2-char string placed before `||----w |` with the rest spaces: template `              $tongue||----w |`? That gives default 14+2=16 spaces ✓. Dead "U " → `              U ||----w |` = 14 spaces + "U " → U at col 15. Real cowsay has U at col 14. Close enough — honestly for a from-scratch clone, exact tongue column is a cosmetic detail. I'll go with template where tongue replaces the last 2 of the 16 leading spaces: i.e. line = `" " * 14 + tongue + "||----w |"`. Default tongue "  " → 16 spaces ✓. Dead "U " → 14 spaces + "U " → U at col 15. Real cowsay has U at col 14. 

Actually, let me just verify with real cowsay if available on the system. I can run `cowsay -d moo` if installed. If not, fine — cosmetic.

Actually simpler and cleaner for the tutorial: keep the cow as a const with `{eyes}` and `{tongue}` placeholders via format!. I'll write:

```rust
fn cow(eyes: &str, tongue: &str) -> String {
    let t = format!("{tongue:>2}"); // right-align tongue in 2 cols
    format!(
"        \\   ^__^
         \\  ({eyes})\\_______
            (__)\\       )\\/\\
            {t}||----w |
                ||     ||
")
}
```

Hmm wait: `            {t}||----w |` = 12 spaces + 2-char tongue + `||----w |`. Default tongue "  " → 14 spaces before `||`. But we want 16. So use 14 spaces: `              {t}||----w |`. Default → 16 ✓. Dead "U " → 14 spaces + "U " → U at col 15. Real cowsay has U at col 14. 

I'll stop chasing the exact column; I'll note it as a fidelity detail. Actually — let me just test against real cowsay if it's installed on this Mac (often not). I'll check during execution and adjust if available.

CLI parsing: v1 without clap (zero deps, more instructive), or with clap (idiomatic)? For a "build your own X" learning exercise, hand-rolled arg parsing is more instructive and keeps it dependency-free. But clap is the real-world choice. I'll hand-roll a small parser supporting:

- positional args → message (joined with spaces)
- `-e EYES` / `--eyes EYES`
- `-T TONGUE` / `--tongue TONGUE`
- `-w N` / `--wrap N`
- `-d` / `--dead` → eyes xx, tongue U
- `-h` / `--help`
- stdin if no message given (cowsay reads stdin when no args)

Reading stdin when no positional args: `cowsay` reads from stdin always if no message args. I'll do: if positional args empty, read stdin fully.

Eyes must be 2 chars (cowsay truncates/pads to 2). I'll enforce: take first 2 chars, pad with space.

Project name: something fun — "moo"? "rustysay"? Let me call it `moosay`. Or keep generic `cowsay-rs`. I'll go with `moosay`.

Structure: single `src/main.rs` for v1, then suggest splitting into modules + tests as next steps. Actually for teaching, maybe start with main.rs containing functions + a few unit tests. Good balance.

Now the process: explore (check workspace + toolchain), plan, todo, execute, verify (cargo run + cargo test).

Let me start. First parallel calls: glob workspace, bash check rustc/cargo.

Actually the instructions say call `explore` once before modifying code, recording files read/intended. The workspace is likely empty. Let me glob and check toolchain in parallel, then explore+plan.

For the response style: user speaks Chinese, so respond in Chinese. Keep it concise, lead with action.

Let me also think about what "带我开始" implies — they want to be guided. I'll do the scaffold + v1 implementation, explain the design decisions briefly (bubble geometry, wrapping), run it, show output, and lay out next steps (flags, cowfile, tests, publish). That's a good "start together" experience: I build the skeleton, explain, and they can extend.

One consideration: should I ask them questions first (name? features?) instead of building? "带我开始" = "get me started". Best: make concrete progress with sensible defaults, explain choices, invite direction. Don't stall with questions.

Let me execute:

1. glob `**/*` in workspace + `cargo --version; rustc --version` in parallel.
2. explore note.
3. plan with steps.
4. todo_write.
5. cargo init, write main.rs, build, run, test.
6. Show output, explain, next steps.

Let me write the final main.rs carefully.

```rust
use std::io::Read;

const DEFAULT_WIDTH: usize = 40;

fn main() {
    let args = parse_args(std::env::args().skip(1));
    let message = if args.text.is_empty() {
        let mut buf = String::new();
        std::io::stdin().read_to_string(&mut buf).expect("read stdin");
        buf
    } else {
        args.text.join(" ")
    };
    let lines = wrap(&message, args.width);
    print!("{}", bubble(&lines));
    print!("{}", cow(&args.eyes, &args.tongue));
}
```

Args struct:

```rust
struct Args {
    text: Vec<String>,
    eyes: String,
    tongue: String,
    width: usize,
}
```

Parser:

```rust
fn parse_args<I: Iterator<Item = String>>(mut it: I) -> Args {
    let mut a = Args { text: vec![], eyes: "oo".into(), tongue: "  ".into(), width: DEFAULT_WIDTH };
    while let Some(arg) = it.next() {
        match arg.as_str() {
            "-h" | "--help" => { print_usage(); std::process::exit(0); }
            "-e" | "--eyes" => a.eyes = it.next().unwrap_or_else(|| die("--eyes 需要一个参数")),
            "-T" | "--tongue" => a.tongue = it.next().unwrap_or_else(...),
            "-w" | "--wrap" => { let v = it.next()...; a.width = v.parse().unwrap_or_else(...); }
            "-d" | "--dead" => { a.eyes = "xx".into(); a.tongue = "U ".into(); }
            _ => a.text.push(arg),
        }
    }
    a
}
```

Hmm, `-w 0` → clamp to 1 to avoid infinite loop in wrap. Or treat 0 as "no wrap". cowsay: -w 0 means infinity actually (no wrapping). I'll treat 0 as no-wrap: in wrap, if width == 0, return whole text as one line. Nice touch.

Eyes normalization: take first 2 chars, pad to 2:

```rust
fn norm2(s: &str) -> String {
    let mut c: Vec<char> = s.chars().take(2).collect();
    while c.len() < 2 { c.push(' '); }
    c.into_iter().collect()
}
```

Tongue same (2 chars).

Usage text in Chinese or English? CLI tools usually English; but user is Chinese. I'll do bilingual-ish minimal English usage (standard practice) — actually keep it simple English, it's a CLI convention. Hmm, or Chinese since it's their tool. I'll do English usage (portable), fine either way. Let me do concise English.

Tests: unit tests for wrap (basic, long word, empty), bubble (single line, multi-line), cow contains eyes. 

Now bubble edge: empty message → one empty line → `<  >` with width 0: 
```
 __
<  >
 --
```
Wait width = 0, top = "_" * 2 = "__", line `<  >` (space + empty + pad 0 + space). Bottom "--". That matches cowsay behavior for empty input? cowsay with empty input prints `<  >`? Actually cowsay prints an empty bubble. Fine.

Trailing newline in message from stdin: wrap uses split_whitespace so trailing newline is handled.

Multi-line bubble check with "hello world foo bar baz" width 12:
wrap → ["hello world", "foo bar baz"]? "hello world" = 11 ≤ 12 ✓; adding "foo" → 15 > 12 → push; "foo bar baz" = 11 ✓. Bubble:
```
 ____________
/ hello world \
| foo bar baz |
\_____________/
```
Wait no — bottom border is dashes, and last line uses `\ ... /`:
```
 ____________
/ hello world \
| foo bar baz |
 --------------
```
Hmm the last line right char: for multi-line, first `/`, last `\`. So:
```
/ hello world \
| foo bar baz |
```
Wait which corner? cowsay: first line `/`, last line `\`. So:
```
/ hello world \
| foo bar baz |
```
No wait — first line starts `/` ends `\`; last line starts `\` ends `/`. Yes my match does that: (n,0) → ('/','\\'); last → ('\\','/'). ✓.

In my bubble function the format string: `{l} {line}{pad} {r}` — cowsay format is `<space>text<pad><space>` between the corner chars: `/ hello world \`. So l + " " + text + padding + " " + r. ✓.

Cow art — need to double check backslashes in Rust string. Using raw string r#"..."# avoids escaping:

```rust
fn cow(eyes: &str, tongue: &str) -> String {
    format!(
        r#"        \   ^__^
         \  ({eyes})\_______
            (__)\       )\/\
              {tongue}||----w |
                ||     ||
"#,
        eyes = eyes,
        tongue = tongue,
    )
}
```

Wait tongue line: I decided 14 spaces + tongue(2) + `||----w |`. `              ` is 14 spaces. Default tongue "  " → 16 spaces total ✓.

Hmm, but raw string with format! and `{eyes}` — fine. The `\` in raw string is literal ✓. `)\/\` literal ✓.

Also the thought bubble variant (`-n`? no, cowsay has cowthink with `o` instead of `\`). Skip for v1, mention as next step.

Now — check if real cowsay exists on system to compare. `which cowsay`. If present, diff outputs. Nice verification.

Also `cargo new moosay` — or since workspace might be the project root already (dir name "build-your-own-x-command-line-tool-1"), maybe create project inside as subdirectory `moosay`. Let me check workspace contents first.

Alright, execute. First round of parallel calls: glob + bash (rustc/cargo versions + which cowsay).

Then explore, plan, todo, then implement.

For the final response: concise Chinese explanation of what was built, the geometry rules, how to run, and 3-4 next steps. Keep it tight.空工作区，Rust 1.95 就绪。我来规划一下这个项目。Wait, my bubble_multi_line_corners test is convoluted with that replace hack — that's ugly and error-prone. Let me fix it to a plain assertion. Expected bubble for ["hello world", "foo"]:
- width = 11, top = "_" * 13 = " ____________\n"
- line 0: "/ hello world \\\n" → `/ hello world \`
- line 1: pad = 11-3 = 8 → `\ foo          /` → `\ foo` + 8 spaces + ` /` → "\ foo          /\n" (foo + 8 spaces = "foo        " then " /")
- bottom: " -------------\n" (13 dashes)

Let me write it cleanly. Also `\\ foo         /` in my test — I wrote a weird replace. Let me just rewrite that test properly.Wait — for a 2-line bubble, line 0 is first (`/ ... \`) and line 1 is last (`\ ... /`). There is no middle line. My expected string: `/ hello world \` then `\ foo          /`. Let me verify pad: width=11, "foo" is 3 chars, pad = 8 spaces. Format: `{l} {line}{pad} {r}` → `\ foo` + 8 spaces + ` /` = `\ foo          /`. Count: "foo" + 8 spaces = "foo        " (11 chars), then " /". So the line is `\ foo          /` — between "foo" and "/" there are 8+1=9 spaces. In my expected string `\ foo          /`: after "foo" I have... let me count: `\ foo` then spaces then `/`. I wrote "foo" followed by 10 spaces then "/"? Let me count carefully in the string: `\ foo          /` — f-o-o then "          " — that's 10 spaces, then `/`. Hmm: `\ foo` = backslash, space, f, o, o. Then the spaces: I typed 10 spaces, then ` /`? No — the string is `\ foo          /` — after "foo" there are 10 spaces then "/". But format produces "foo" + 8 pad + 1 space + "/" = 9 spaces between "foo" and "/". So my expected has one extra space. Let me recount what I typed: `\ foo          /` — between "foo" and "/": "          " — I need to count the characters. In the edit I wrote: `" ____________\n/ hello world \\\n\\ foo          /\n -------------\n"`. The segment `\\ foo          /` → after unescaping: `\ foo          /`. Spaces between foo and /: I typed 10. Should be 9.

Hmm, rather than eyeball-counting spaces in a string literal (error-prone), the test will tell me. Let me just run cargo test and fix based on the actual diff. Actually better: make the test construct expected programmatically? No — a literal is clearer for teaching. Just run the test and correct.

Also line 1 for a 2-line bubble: my match gives i==0 → ('/','\\'), i==n-1 → ('\\','/'). For n=2, line 1 is both last → ('\\','/'). ✓.

Run cargo test.代码是正确的 —— 我的测试字面量在空格数量上出了错，而且 pads 测试使用了 2 行（其中没有 `|` 中间行）。正在修复这些测试：10 个测试全绿。跑一下真实输出验证：All outputs look correct:
1. Single line: `< Hello, Rust! >` ✓
2. Multi-line with corners `/ \ | \ /` ✓
3. Dead with custom eyes ^^ and tongue U ✓
4. Hard-break of long word ✓

One cosmetic note: real cowsay puts the tongue `U` one column to the left (at col 14 vs my 15). Minor. Also real cowsay's dead tongue is "U " placed differently. It's fine.

Let me also run clippy quickly and mark todos done. Then write the final summary in Chinese: what was built, structure, how to run, next steps.v1 完成，项目在 `moosay/`，零依赖，10 个测试全绿，clippy 干净。

**核心就三个函数**（`moosay/src/main.rs`）：

- `wrap(text, width)` — 贪心换行，超长单词硬切，`-w 0` 表示不换行（main.rs:80）
- `bubble(lines)` — 气泡几何：单行用 `< >`，多行首行 `/ \`、末行 `\ /`、中间 `| |`，边框宽度 = 最长行 + 2（main.rs:113）
- `cow(eyes, tongue)` — 牛的 ASCII 画，眼睛和舌头是占位符（main.rs:141）

参数解析是手写的（学习目的，没用 clap）：`-e` 眼睛、`-T` 舌头、`-w` 宽度、`-d` 死牛、`--help`；不带参数时从 stdin 读，所以支持管道：

```bash
cd moosay
cargo run -- "Hello, Rust!"
echo "hello world" | cargo run -q -- -w 20
cargo run -- -d -e ^^ "dead"
cargo test
```

**接下来可以一起加的**，按难度排：

1. **cowthink 模式**（`-c`）：气泡角换成 `o` 和 `(` `)`，改动极小，练手最合适
2. **`-f cowfile`**：把牛画抽到外部文件，用 `$eyes`/`$tongue` 占位符替换——这是 cowsay 的核心设计
3. **Unicode 宽度**：现在按 char 数计宽，中文（全角）会撑破气泡，需要按显示宽度计算
4. **迁移到 clap**：体会手写解析和声明式解析的取舍

想从哪个开始，或者你有别的方向？