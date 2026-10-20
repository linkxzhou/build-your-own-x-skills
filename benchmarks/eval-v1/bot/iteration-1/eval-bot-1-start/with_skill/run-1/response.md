The user wants to build a Telegram bot in Python to learn how bots work. This matches the build-your-own-x skill — "build your own... bot" — actually let me check: the skill description mentions "Git, Redis/databases, a shell, Docker/containers, an interpreter/compiler/programming language, an OS, an emulator, a web server, a browser, a regex or template engine, a game, a neural network, blockchain, an LLM, malloc, a CPU, and more." A Telegram bot is a hands-on project to learn engineering skills. The trigger says "Use it whenever someone wants to understand how a tool works by building their own, asks for a hands-on project to learn systems or engineering skills..." A Telegram bot is a hands-on project. The skill is an entry point for learning by rebuilding real software. A Telegram bot isn't exactly "rebuilding real software" but it's a hands-on project to learn. The skill says it "picks the topic, language and tutorial, then hands off to the matching sub-skill under skills/ and coaches step by step instead of dumping a finished solution."

I should read the SKILL.md first before doing anything else, per the instructions. Let me do that.The file is truncated. Let me read the rest of it to see the full category map and any other instructions.The topic maps to the `bot` track. Reading the track skill now — it's mandatory before anything else.There's a per-tutorial skill matching exactly: `bot-telegram-bot-python`. Reading it plus its tutorial map.The track and per-tutorial skills are loaded. Before scaffolding, let me check the workspace state.Workspace is empty apart from skill files. Checking AGENTS.md for workspace rules before I scaffold anything.Workspace is clean. Let me check the upstream tutorial so the milestones align with it.The tutorial page returned mostly page chrome, but I have what I need: the exact upstream link, the track's milestone table, and a clean workspace with Python 3.14. Recording the exploration and the plan, then scaffolding milestone 1.Scaffolding milestone 1 now — skeleton with TODOs, config files, and progress tracking.**Where we are:** milestone 1/7 — skeleton + config. Scaffold is in place: `bot.py` (with 3 TODOs), `.env.example`, `.gitignore`, `requirements.txt`, `README.md`, `PROGRESS.md`.

**The concept:** a Telegram bot is an HTTP client that polls `api.telegram.org` for new messages. Your token is the bot's password — it lives in `.env`, which is gitignored, and should never be pasted into chat or committed. Long polling means you need no public IP or webhook; your process just asks Telegram "anything new?" in a loop.

**Your moves (run these yourself):**

```bash
git init
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

Then get a token: message [@BotFather](https://t.me/BotFather) in Telegram → `/newbot` → follow prompts → paste the token into `.env`.

**What to write next** — fill the three TODOs in `bot.py`:

1. Read `BOT_TOKEN` from `os.environ`; if missing, log an error and `sys.exit(1)`.
2. Build the app: `Application.builder().token(token).build()`.
3. In `post_init`, call `await application.bot.get_me()` and log `Logged in as @<username>`; then start polling with `app.run_polling(post_init=post_init)`.

**Checkpoint:** `python bot.py` prints `Logged in as @<yourbotname>`, and `git check-ignore .env` outputs `.env`. When both pass, tell me and we'll log it in `PROGRESS.md` and move to the echo command.

Stuck? Ask and you get one hint at a time. Reference: [freeCodeCamp — How to Create a Telegram Bot using Python](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/).