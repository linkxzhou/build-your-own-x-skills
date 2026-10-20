The user wants to build a Telegram bot in Python to learn how bots work. This matches the build-your-own-x skill — "hands-on project to learn systems skills" and "推荐一个练手项目". The skill description says: use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems skills... Telegram bot building is a learning-by-building project. The skill is an entry point for learning by rebuilding real software from scratch. A Telegram bot is arguably in that category ("a web server", "build your own X"). The trigger list includes things like Git, Redis, shell, Docker, interpreter, OS, emulator, web server, browser, regex engine, ray tracer, game, neural network, blockchain, LLM, malloc, CPU. A Telegram bot isn't explicitly listed, but the skill says "OR asks for a hands-on project to learn systems skills". The user says "I want to build a Telegram bot in Python to learn how bots work. Get me going." This is a hands-on learning project. I should read the skill first per instructions.

Let me read the SKILL.md.The file was truncated. Let me read the rest of the SKILL.md.The topic maps to the `bot` track. Reading the track skill now — it's mandatory before anything else.Now the tutorials list to pick a Python/Telegram guide.The Python + Telegram tutorial is: "How To Create a Telegram Bot Using Using Python" — https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/

Let me check if there's a per-tutorial skill for it: `ls skills | grep '^bot-'`.There's a per-tutorial skill for the Python/Telegram article. Reading it.The track and per-tutorial skills are loaded. Two things to check before scaffolding: what's already in the workspace, and which library the upstream guide uses.Workspace is empty apart from skill files — starting from scratch. Quick environment check, the project notes, and confirmation of the tutorial's stack, in parallel:Search came up empty; fetching the article with a larger budget to confirm which library it teaches:Environment confirmed: Python 3.14.7 (Homebrew, so PEP 668 externally-managed — venv needed), git available, empty workspace. Tutorial confirmed: freeCodeCamp's guide uses `pyTelegramBotAPI` with long polling and a horoscope-bot target. Recording exploration and the plan:Scaffolding milestone 1 now:Scaffold is in place and compiles. Here's your setup.

**Where we are:** milestone 1/6 — skeleton + config.

**The concept.** A Telegram bot is a program that talks to Telegram's servers over HTTPS. Your token identifies the bot; every API call is just an HTTP request like `https://api.telegram.org/bot<TOKEN>/getMe`. `pyTelegramBotAPI` wraps those requests in a `TeleBot` object. With **long polling**, your process repeatedly asks "any new messages?" and Telegram holds the request open until one arrives — that's why the bot looks instant without a public URL (webhooks are the alternative; milestone 7 territory).

**Your project lives in `telegram-bot/`:**
- `bot.py` — skeleton with 3 TODOs, compiles clean
- `.gitignore` — already covers `.env`, `.venv/`, `bot.db`
- `PROGRESS.md` — milestone table we update as checkpoints pass

**What to write next** (fill the TODOs in `bot.py`):
1. `BOT_TOKEN = os.environ.get("BOT_TOKEN")` — plus a guard that exits with a clear message if it's `None`.
2. `bot = telebot.TeleBot(BOT_TOKEN)`
3. Before `infinity_polling()`: `me = bot.get_me()` then `print(f"Logged in as @{me.username}")`.

**Your commands** (run these yourself, in order):

```bash
# 1. Get a token: open Telegram, message @BotFather, send /newbot, follow prompts.
#    Keep the token out of chat — it goes straight into .env.

# 2. Environment. Homebrew Python is externally managed, so a venv is required:
cd telegram-bot
python3 -m venv .venv
source .venv/bin/activate
pip install pyTelegramBotAPI

# 3. Token file (never commit it):
echo 'export BOT_TOKEN=123456:ABC-your-real-token' > .env

# 4. Version control:
git init && git add .gitignore PROGRESS.md bot.py && git commit -m "Milestone 1: skeleton"

# 5. Run it:
source .env && python3 bot.py
```

**How to check it:**
```bash
source .env && python3 bot.py
# expected: "Logged in as @yourbotname", then it sits there polling — Ctrl+C to stop
git check-ignore .env
# expected output: .env  (proves the token can't be committed)
```

When `Logged in as @...` prints, message your bot `/start` in Telegram — the welcome reply should already work since the handler is in the skeleton. Tell me the result (or paste any traceback, minus the token) and we move to milestone 2: the echo command.