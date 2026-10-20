The user has a Go CLI that prints colored output fine in the terminal, but when piped to a file, the file contains ANSI escape codes. This is a classic problem: the program should detect whether stdout is a TTY and disable colors when it's not. The user hasn't shared code, so I should check the workspace for their Go project first. Let me look at what's in the workspace.

Let me explore the workspace to find the Go files.The cause: your program emits ANSI escapes unconditionally. A terminal interprets them; a file or pipe just stores the raw bytes. The fix is to detect whether stdout is a TTY and gate color output on that.

Standard check without dependencies:

```go
func useColor() bool {
	if os.Getenv("NO_COLOR") != "" {
		return false
	}
	fi, err := os.Stdout.Stat()
	if err != nil {
		return false
	}
	return fi.Mode()&os.ModeCharDevice != 0
}
```

Or with `golang.org/x/term`, which is more precise:

```go
import "golang.org/x/term"

useColor := term.IsTerminal(int(os.Stdout.Fd()))
```

Then wrap your color helpers:

```go
func green(s string) string {
	if !useColor {
		return s
	}
	return "\033[32m" + s + "\033[0m"
}
```

Notes depending on how you color today:

- **fatih/color** and **charmbracelet/lipgloss** already auto-disable when stdout isn't a TTY. If you're seeing escapes in a file with these, you likely forced color on (`color.NoColor = false`, `lipgloss.SetColorProfile(...)`, or a `--color always` default). Remove the force, or make it opt-in.
- **Raw escape strings** (the snippet above) need the TTY check yourself — this is the most common case.
- Check **stdout**, not stderr. If you print diagnostics to stderr, that stream has its own TTY state.
- Common convention worth supporting: `NO_COLOR` disables, `CLICOLOR_FORCE=1` or `--color always` forces (useful for `tee`, `less -R`, CI logs). A `--color auto|always|never` flag with `auto` as default covers everything.

Quick sanity test after the fix: `./mycli | cat` should print plain text, `./mycli` in the terminal should still be colored, and `./mycli --color always | less -R` should show color through the pipe.