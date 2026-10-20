The user wants to build a Telegram bot in Python to learn how bots work. Let me look at the workspace first to see what's there, then set up a minimal but educational bot scaffold.

Let me check the current directory contents first.Empty workspace, Python 3.14. I'll build a minimal, dependency-light bot that teaches the core mechanics: long polling, update handling, command dispatch, and replies.Now write the bot. Keep it educational: comments explaining each concept, but not bloated. Core pieces:

1. Token from env
2. `api()` helper wrapping requests to Telegram Bot API
3. Long polling loop with offset tracking
4. Command dispatch: /start, /help, /roll, /count (per-chat state demo)
5. Echo fallback for non-command messages
6. KeyboardInterrupt handling

Keep it ~100 lines with good comments. Then requirements.txt and README.Compile OK, and the no-token path exits with a clear message. All three todos done. Update the todo list and give the user a concise wrap-up.Scaffold is ready — three files:

- `bot.py` — the whole bot in ~120 lines, built on the raw Bot API with only `requests`, so every moving part is visible: `api()` wraps the HTTPS calls, the main loop long-polls `getUpdates` with offset tracking, and a dict routes `/commands` to handler functions. Includes `/roll`, `/count` (per-chat state demo), `/echo`, and an echo fallback.
- `README.md` — BotFather setup, run instructions, and the four core concepts (HTTPS API, long polling, offsets, command dispatch) plus next exercises.
- `requirements.txt` — just `requests`.

To go live:

```sh
pip install -r requirements.txt
BOT_TOKEN=123456789:AAE... python3 bot.py
```

Get the token from [@BotFather](https://t.me/BotFather) via `/newbot`. The bot prints its identity on startup (`getMe` sanity check), then blocks waiting for messages — open it in Telegram and send `/start`.

One design choice worth knowing: I used long polling rather than webhooks because it needs no public IP or TLS cert, which keeps the first run friction-free. The README's exercises (inline keyboards, SQLite state, webhook mode) are the natural next steps once the basics click.