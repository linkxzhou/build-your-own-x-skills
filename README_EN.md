# Background

The goal of this project is to gradually convert projects from `https://github.com/codecrafters-io/build-your-own-x` into skills, enabling developers to learn engineering topics quickly with AI-assisted, project-based workflows.

## Current Status

- Original build-your-own-x entries: `351`
- Available generated skills kept: `351`
- Generated examples: `351`
- Categories: `27`
- Conversion plans: `plan/`
- Skill manifest: `skills/x-skills-manifest.json`
- Example manifest: `examples/examples-manifest.json`

> Note: earlier temporary skills with 8-character hash suffixes were removed because their names were not readable. Checked items below correspond to skills currently kept under `skills/`.

## Directory Structure

```
build-your-own-x-skills/
├── .claude/skills/          # Claude Code skills directory, symlinked to skills/
├── .codebuddy/skills/       # CodeBuddy skills directory, symlinked to skills/
├── .trae/skills/            # TRAE skills directory, symlinked to skills/
├── .gemini/skills/          # Gemini CLI skills directory, symlinked to skills/
├── skills/                  # Main skills directory; each subdirectory is a skill
├── plan/                    # Conversion plans from build-your-own-x entries to skills
├── examples/                # Skill usage examples grouped by category
├── tests/                   # Skill tests
├── README.md                # Chinese README
├── README_EN.md             # English README
├── README_PROMPT.md         # Prompt templates and test prompts
└── init.sh                  # Symlink initialization script
```

## Installation

1. Clone this repository.
2. Run `./init.sh` to symlink `skills/` into supported AI coding tools.
3. Use `[使用Skills: skill-name]` or rely on automatic skill triggering.

## Examples

Each available generated skill has a corresponding example grouped by category:

| Category | Examples |
|---|---:|
| [3d-renderer](./examples/3d-renderer/) | 11 |
| [augmented-reality](./examples/augmented-reality/) | 6 |
| [bittorrent-client](./examples/bittorrent-client/) | 5 |
| [blockchain-cryptocurrency](./examples/blockchain-cryptocurrency/) | 22 |
| [bot](./examples/bot/) | 15 |
| [command-line-tool](./examples/command-line-tool/) | 9 |
| [database](./examples/database/) | 13 |
| [docker](./examples/docker/) | 6 |
| [emulator-virtual-machine](./examples/emulator-virtual-machine/) | 13 |
| [frontend-framework-library](./examples/frontend-framework-library/) | 14 |
| [game](./examples/game/) | 34 |
| [git](./examples/git/) | 7 |
| [misc](./examples/misc/) | 62 |
| [network-stack](./examples/network-stack/) | 4 |
| [neural-network](./examples/neural-network/) | 14 |
| [operating-system](./examples/operating-system/) | 19 |
| [physics-engine](./examples/physics-engine/) | 7 |
| [programming-language](./examples/programming-language/) | 41 |
| [regex-engine](./examples/regex-engine/) | 9 |
| [search-engine](./examples/search-engine/) | 6 |
| [shell](./examples/shell/) | 7 |
| [template-engine](./examples/template-engine/) | 5 |
| [text-editor](./examples/text-editor/) | 6 |
| [visual-recognition-system](./examples/visual-recognition-system/) | 2 |
| [voxel-engine](./examples/voxel-engine/) | 1 |
| [web-browser](./examples/web-browser/) | 2 |
| [web-server](./examples/web-server/) | 11 |

Entry points:

- Root index: [`examples/README.md`](./examples/README.md)
- Database example: [`examples/database/database-redis/`](./examples/database/database-redis/)
- Programming language examples: [`examples/programming-language/`](./examples/programming-language/)

## Conversion Plans

- Index: [`plan/README.md`](./plan/README.md)
- One plan file per category, e.g. `plan/database.md`, `plan/programming-language.md`.
- Each project plan includes suggested skill name, trigger scenarios, `SKILL.md` plan, resource plan, and acceptance criteria.

## Progress

![Progress](https://img.shields.io/badge/Progress-100%25-yellow?style=flat-square)

▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 100%

## build-your-own-x Projects
#### Build your own `3D Renderer`

- [X] [**C++**: _Introduction to Ray Tracing: a Simple Method for Creating 3D Images_](https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/how-does-it-work)
- [X] [**C++**: _How OpenGL works: software rendering in 500 lines of code_](https://github.com/ssloy/tinyrenderer/wiki)
- [X] [**C++**: _Raycasting engine of Wolfenstein 3D_](http://lodev.org/cgtutor/raycasting.html)
- [X] [**C++**: _Physically Based Rendering:From Theory To Implementation_](http://www.pbr-book.org/)
- [X] [**C++**: _Ray Tracing in One Weekend_](https://raytracing.github.io/books/RayTracingInOneWeekend.html)
- [X] [**C++**: _Rasterization: a Practical Implementation_](https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation/overview-rasterization-algorithm)
- [X] [**C# / TypeScript / JavaScript**: _Learning how to write a 3D soft engine from scratch in C#, TypeScript or JavaScript_](https://www.davrous.com/2013/06/13/tutorial-series-learning-how-to-write-a-3d-soft-engine-from-scratch-in-c-typescript-or-javascript/)
- [X] [**Java / JavaScript**: _Build your own 3D renderer_](https://avik-das.github.io/build-your-own-raytracer/)
- [X] [**Java**: _How to create your own simple 3D render engine in pure Java_](http://blog.rogach.org/2015/08/how-to-create-your-own-simple-3d-render.html)
- [X] [**JavaScript / Pseudocode**: _Computer Graphics from scratch_](http://www.gabrielgambetta.com/computer-graphics-from-scratch/introduction.html)
- [X] [**Python**: _A 3D Modeller_](http://aosabook.org/en/500L/a-3d-modeller.html)

#### Build your own `Augmented Reality`

- [X] [**C#**: _How To: Augmented Reality App Tutorial for Beginners with Vuforia and Unity 3D_](https://www.youtube.com/watch?v=uXNjNcqW4kY) [video]
- [X] [**C#**: _How To Unity ARCore_](https://www.youtube.com/playlist?list=PLKIKuXdn4ZMjuUAtdQfK1vwTZPQn_rgSv) [video]
- [X] [**C#**: _AR Portal Tutorial with Unity_](https://www.youtube.com/playlist?list=PLPCqNOwwN794Gz5fzUSi1p4OqLU0HTmvn) [video]
- [X] [**C#**: _How to create a Dragon in Augmented Reality in Unity ARCore_](https://www.youtube.com/watch?v=qTSDPkPyPqs) [video]
- [X] [**C#**: _How to Augmented Reality AR Tutorial: ARKit Portal to the Upside Down_](https://www.youtube.com/watch?v=Z5AmqMuNi08) [video]
- [X] [**Python**: _Augmented Reality with Python and OpenCV_](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)

#### Build your own `BitTorrent Client`

- [X] [**C#**: _Building a BitTorrent client from scratch in C#_](https://www.seanjoflynn.com/research/bittorrent.html)
- [X] [**Go**: _Building a BitTorrent client from the ground up in Go_](https://blog.jse.li/posts/torrent/)
- [X] [**Nim**: _Writing a Bencode Parser_](https://xmonader.github.io/nimdays/day02_bencode.html)
- [X] [**Node.js**: _Write your own bittorrent client_](https://allenkim67.github.io/programming/2016/05/04/how-to-make-your-own-bittorrent-client.html)
- [X] [**Python**: _A BitTorrent client in Python 3.5_](http://markuseliasson.se/article/bittorrent-in-python/)

#### Build your own `Blockchain / Cryptocurrency`

- [X] [**ATS**: _Functional Blockchain_](https://beta.observablehq.com/@galletti94/functional-blockchain)
- [X] [**C#**: _Programming The Blockchain in C#_](https://programmingblockchain.gitbooks.io/programmingblockchain/)
- [X] [**Crystal**: _Write your own blockchain and PoW algorithm using Crystal_](https://medium.com/@bradford_hamilton/write-your-own-blockchain-and-pow-algorithm-using-crystal-d53d5d9d0c52)
- [X] [**Go**: _Building Blockchain in Go_](https://jeiwan.net/posts/building-blockchain-in-go-part-1/)
- [X] [**Go**: _Code your own blockchain in less than 200 lines of Go_](https://medium.com/@mycoralhealth/code-your-own-blockchain-in-less-than-200-lines-of-go-e296282bcffc)
- [X] [**Java**: _Creating Your First Blockchain with Java_](https://medium.com/programmers-blockchain/create-simple-blockchain-java-tutorial-from-scratch-6eeed3cb03fa)
- [X] [**JavaScript**: _A cryptocurrency implementation in less than 1500 lines of code_](https://github.com/conradoqg/naivecoin)
- [X] [**JavaScript**: _Build your own Blockchain in JavaScript_](https://github.com/nambrot/blockchain-in-js)
- [X] [**JavaScript**: _Learn & Build a JavaScript Blockchain_](https://medium.com/digital-alchemy-holdings/learn-build-a-javascript-blockchain-part-1-ca61c285821e)
- [X] [**JavaScript**: _Creating a blockchain with JavaScript_](https://github.com/SavjeeTutorials/SavjeeCoin)
- [X] [**JavaScript**: _How To Launch Your Own Production-Ready Cryptocurrency_](https://hackernoon.com/how-to-launch-your-own-production-ready-cryptocurrency-ab97cb773371)
- [X] [**JavaScript**: _Writing a Blockchain in Node.js_](https://www.smashingmagazine.com/2020/02/cryptocurrency-blockchain-node-js/)
- [X] [**Kotlin**: _Let's implement a cryptocurrency in Kotlin_](https://medium.com/@vasilyf/lets-implement-a-cryptocurrency-in-kotlin-part-1-blockchain-8704069f8580)
- [X] [**Python**: _Learn Blockchains by Building One_](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
- [X] [**Python**: _Build your own blockchain: a Python tutorial_](http://ecomunsing.com/build-your-own-blockchain)
- [X] [**Python**: _A Practical Introduction to Blockchain with Python_](http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/)
- [X] [**Python**: _Let's Build the Tiniest Blockchain_](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)
- [X] [**Ruby**: _Programming Blockchains Step-by-Step (Manuscripts Book Edition)_](https://github.com/yukimotopress/programming-blockchains-step-by-step)
- [X] [**Scala**: _How to build a simple actor-based blockchain_](https://medium.freecodecamp.org/how-to-build-a-simple-actor-based-blockchain-aac1e996c177)
- [X] [**TypeScript**: _Naivecoin: a tutorial for building a cryptocurrency_](https://lhartikk.github.io/)
- [X] [**TypeScript**: _NaivecoinStake: a tutorial for building a cryptocurrency with the Proof of Stake consensus_](https://naivecoinstake.learn.uno/)
- [X] [**Rust**: _Building A Blockchain in Rust & Substrate_](https://hackernoon.com/building-a-blockchain-in-rust-and-substrate-a-step-by-step-guide-for-developers-kc223ybp)


#### Build your own `Bot`

- [X] [**Haskell**: _Roll your own IRC bot_](https://wiki.haskell.org/Roll_your_own_IRC_bot)
- [X] [**Node.js**: _Creating a Simple Facebook Messenger AI Bot with API.ai in Node.js_](https://tutorials.botsfloor.com/creating-a-simple-facebook-messenger-ai-bot-with-api-ai-in-node-js-50ae2fa5c80d)
- [X] [**Node.js**: _How to make a responsive telegram bot_](https://www.sohamkamani.com/blog/2016/09/21/making-a-telegram-bot/)
- [X] [**Node.js**: _Create a Discord bot_](https://discordjs.guide/)
- [X] [**Node.js**: _gifbot - Building a GitHub App_](https://blog.scottlogic.com/2017/05/22/gifbot-github-integration.html)
- [X] [**Node.js**: _Building A Simple AI Chatbot With Web Speech API And Node.js_](https://www.smashingmagazine.com/2017/08/ai-chatbot-web-speech-api-node-js/)
- [X] [**Python**: _How to Build Your First Slack Bot with Python_](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
- [X] [**Python**: _How to build a Slack Bot with Python using Slack Events API & Django under 20 minute_](https://medium.com/freehunch/how-to-build-a-slack-bot-with-python-using-slack-events-api-django-under-20-minute-code-included-269c3a9bf64e)
- [X] [**Python**: _Build a Reddit Bot_](http://pythonforengineers.com/build-a-reddit-bot-part-1/)
- [X] [**Python**: _How To Make A Reddit Bot_](https://www.youtube.com/watch?v=krTUf7BpTc0) [video]
- [X] [**Python**: _How To Create a Telegram Bot Using Python_](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
- [X] [**Python**: _Create a Twitter Bot in Python Using Tweepy_](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607)
- [X] [**Python**: _Creating Reddit Bot with Python & PRAW_](https://www.youtube.com/playlist?list=PLIFBTFgFpoJ9vmYYlfxRFV6U_XhG-4fpP) [video]
- [X] [**R**: _Build A Cryptocurrency Trading Bot with R_](https://towardsdatascience.com/build-a-cryptocurrency-trading-bot-with-r-1445c429e1b1)
- [X] [**Rust**: _A bot for Starcraft in Rust, C or any other language_](https://habr.com/en/post/436254/)

#### Build your own `Command-Line Tool`

- [X] [**Go**: _Visualize your local git contributions with Go_](https://flaviocopes.com/go-git-contributions/)
- [X] [**Go**: _Build a command line app with Go: lolcat_](https://flaviocopes.com/go-tutorial-lolcat/)
- [X] [**Go**: _Building a cli command with Go: cowsay_](https://flaviocopes.com/go-tutorial-cowsay/)
- [X] [**Go**: _Go CLI tutorial: fortune clone_](https://flaviocopes.com/go-tutorial-fortune/)
- [X] [**Nim**: _Writing a stow alternative to manage dotfiles_](https://xmonader.github.io/nimdays/day06_nistow.html)
- [X] [**Node.js**: _Create a CLI tool in Javascript_](https://citw.dev/tutorial/create-your-own-cli-tool)
- [X] [**Rust**: _Command line apps in Rust_](https://rust-cli.github.io/book/index.html)
- [X] [**Rust**: _Writing a Command Line Tool in Rust_](https://mattgathu.dev/2017/08/29/writing-cli-app-rust.html)
- [X] [**Zig**: _Build Your Own CLI App in Zig from Scratch_](https://rebuild-x.github.io/docs/#/./zig/terminal/cli)


#### Build your own `Database`

- [X] [**C**: _Let's Build a Simple Database_](https://cstack.github.io/db_tutorial/)
- [X] [**C++**: _Build Your Own Redis from Scratch_](https://build-your-own.org/redis)
- [X] [**C#**: _Build Your Own Database_](https://www.codeproject.com/Articles/1029838/Build-Your-Own-Database)
- [X] [**Clojure**: _An Archaeology-Inspired Database_](http://aosabook.org/en/500L/an-archaeology-inspired-database.html)
- [X] [**Crystal**: _Why you should build your own NoSQL Database_](https://medium.com/@marceloboeira/why-you-should-build-your-own-nosql-database-9bbba42039f5)
- [X] [**Go**: _Build Your Own Database from Scratch: From B+Tree To SQL in 3000 Lines_](https://build-your-own.org/database/)
- [X] [**Go**: _Code a database in 45 steps: a series of test-driven small coding puzzles_](https://trialofcode.org/database/)
- [X] [**Go**: _Build Your Own Redis from Scratch_](https://www.build-redis-from-scratch.dev/)
- [X] [**JavaScript**: _Dagoba: an in-memory graph database_](http://aosabook.org/en/500L/dagoba-an-in-memory-graph-database.html)
- [X] [**Python**: _DBDB: Dog Bed Database_](http://aosabook.org/en/500L/dbdb-dog-bed-database.html)
- [X] [**Python**: _Write your own miniature Redis with Python_](http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)
- [X] [**Ruby**: _Build your own fast, persistent KV store in Ruby_](https://dineshgowda.com/posts/build-your-own-persistent-kv-store/)
- [X] [**Rust**: _Build your own Redis client and server_](https://tokio.rs/tokio/tutorial/setup)

#### Build your own `Docker`

- [X] [**C**: _Linux containers in 500 lines of code_](https://blog.lizzie.io/linux-containers-in-500-loc.html)
- [X] [**Go**: _Build Your Own Container Using Less than 100 Lines of Go_](https://www.infoq.com/articles/build-a-container-golang)
- [X] [**Go**: _Building a container from scratch in Go_](https://www.youtube.com/watch?v=8fi7uSYlOdc) [video]
- [X] [**Python**: _A workshop on Linux containers: Rebuild Docker from Scratch_](https://github.com/Fewbytes/rubber-docker)
- [X] [**Python**: _A proof-of-concept imitation of Docker, written in 100% Python_](https://github.com/tonybaloney/mocker)
- [X] [**Shell**: _Docker implemented in around 100 lines of bash_](https://github.com/p8952/bocker)

#### Build your own `Emulator / Virtual Machine`

- [X] [**C**: _Home-grown bytecode interpreters_](https://medium.com/bumble-tech/home-grown-bytecode-interpreters-51e12d59b25c)
- [X] [**C**: _Virtual machine in C_](http://web.archive.org/web/20200121100942/https://blog.felixangell.com/virtual-machine-in-c/)
- [X] [**C**: _Write your Own Virtual Machine_](https://justinmeiners.github.io/lc3-vm/)
- [X] [**C**: _Writing a Game Boy emulator, Cinoop_](https://cturt.github.io/cinoop.html)
- [X] [**C++**: _How to write an emulator (CHIP-8 interpreter)_](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/)
- [X] [**C++**: _Emulation tutorial (CHIP-8 interpreter)_](http://www.codeslinger.co.uk/pages/projects/chip8.html)
- [X] [**C++**: _Emulation tutorial (GameBoy emulator)_](http://www.codeslinger.co.uk/pages/projects/gameboy.html)
- [X] [**C++**: _Emulation tutorial (Master System emulator)_](http://www.codeslinger.co.uk/pages/projects/mastersystem/memory.html)
- [X] [**C++**: _NES Emulator From Scratch_](https://www.youtube.com/playlist?list=PLrOv9FMX8xJHqMvSGB_9G9nZZ_4IgteYf) [video]
- [X] [**Common Lisp**: _CHIP-8 in Common Lisp_](http://stevelosh.com/blog/2016/12/chip8-cpu/)
- [X] [**JavaScript**: _GameBoy Emulation in JavaScript_](http://imrannazar.com/GameBoy-Emulation-in-JavaScript)
- [X] [**Python**: _Emulation Basics: Write your own Chip 8 Emulator/Interpreter_](http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8.html)
- [X] [**Rust**: _0dmg: Learning Rust by building a partial Game Boy emulator_](https://jeremybanks.github.io/0dmg/)

#### Build your own `Front-end Framework / Library`

- [X] [**JavaScript**: _WTF is JSX (Let's Build a JSX Renderer)_](https://jasonformat.com/wtf-is-jsx/)
- [X] [**JavaScript**: _A DIY guide to build your own React_](https://github.com/hexacta/didact)
- [X] [**JavaScript**: _Building React From Scratch_](https://www.youtube.com/watch?v=_MAD4Oly9yg) [video]
- [X] [**JavaScript**: _Gooact: React in 160 lines of JavaScript_](https://medium.com/@sweetpalma/gooact-react-in-160-lines-of-javascript-44e0742ad60f)
- [X] [**JavaScript**: _Learn how React Reconciler package works by building your own lightweight React DOM_](https://hackernoon.com/learn-you-some-custom-react-renderers-aed7164a4199)
- [X] [**JavaScript**: _Build Yourself a Redux_](https://zapier.com/engineering/how-to-build-redux/)
- [X] [**JavaScript**: _Let's Write Redux!_](https://www.jamasoftware.com/blog/lets-write-redux/)
- [X] [**JavaScript**: _Redux: Implementing Store from Scratch_](https://egghead.io/lessons/react-redux-implementing-store-from-scratch) [video]
- [X] [**JavaScript**: _Build Your own Simplified AngularJS in 200 Lines of JavaScript_](https://blog.mgechev.com/2015/03/09/build-learn-your-own-light-lightweight-angularjs/)
- [X] [**JavaScript**: _Make Your Own AngularJS_](http://teropa.info/blog/2013/11/03/make-your-own-angular-part-1-scopes-and-digest.html)
- [X] [**JavaScript**: _How to write your own Virtual DOM_](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)
- [X] [**JavaScript**: _Building a frontend framework, from scratch, with components (templating, state, VDOM)_](https://mfrachet.github.io/create-frontend-framework/)
- [X] [**JavaScript**: _Build your own React_](https://pomb.us/build-your-own-react/)
- [X] [**JavaScript**: _Building a Custom React Renderer_](https://youtu.be/CGpMlWVcHok) [video]

#### Build your own `Game`

- [X] [**C**: _Handmade Hero_](https://handmadehero.org/)
- [X] [**C**: _How to Program an NES game in C_](https://nesdoug.com/)
- [X] [**C**: _Chess Engine In C_](https://www.youtube.com/playlist?list=PLZ1QII7yudbc-Ky058TEaOstZHVbT-2hg) [video]
- [X] [**C**: _Let's Make: Dangerous Dave_](https://www.youtube.com/playlist?list=PLSkJey49cOgTSj465v2KbLZ7LMn10bCF9) [video]
- [X] [**C**: _Learn Video Game Programming in C_](https://www.youtube.com/playlist?list=PLT6WFYYZE6uLMcPGS3qfpYm7T_gViYMMt) [video]
- [X] [**C**: _Coding A Sudoku Solver in C_](https://www.youtube.com/playlist?list=PLkTXsX7igf8edTYU92nU-f5Ntzuf-RKvW) [video]
- [X] [**C**: _Coding a Rogue/Nethack RPG in C_](https://www.youtube.com/playlist?list=PLkTXsX7igf8erbWGYT4iSAhpnJLJ0Nk5G) [video]
- [X] [**C**: _On Tetris and Reimplementation_](https://brennan.io/2015/06/12/tetris-reimplementation/)
- [X] [**C++**: _Breakout_](https://learnopengl.com/In-Practice/2D-Game/Breakout)
- [X] [**C++**: _Beginning Game Programming v2.0_](http://lazyfoo.net/tutorials/SDL/)
- [X] [**C++**: _Tetris tutorial in C++ platform independent focused in game logic for beginners_](http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/)
- [X] [**C++**: _Remaking Cavestory in C++_](https://www.youtube.com/watch?v=ETvApbD5xRo&list=PLNOBk_id22bw6LXhrGfhVwqQIa-M2MsLa) [video]
- [X] [**C++**: _Reconstructing Cave Story_](https://www.youtube.com/playlist?list=PL006xsVEsbKjSKBmLu1clo85yLrwjY67X) [video]
- [X] [**C++**: _Space Invaders from Scratch_](http://nicktasios.nl/posts/space-invaders-from-scratch-part-1.html)
- [X] [**C#**: _Learn C# by Building a Simple RPG_](http://scottlilly.com/learn-c-by-building-a-simple-rpg-index/)
- [X] [**C#**: _Creating a Roguelike Game in C#_](https://roguesharp.wordpress.com/)
- [X] [**C#**: _Build a C#/WPF RPG_](https://scottlilly.com/build-a-cwpf-rpg/)
- [X] [**Go**: _Games With Go_](https://www.youtube.com/playlist?list=PLDZujg-VgQlZUy1iCqBbe5faZLMkA3g2x) [video]
- [X] [**Java**: _Code a 2D Game Engine using Java - Full Course for Beginners_](https://www.youtube.com/watch?v=025QFeZfeyM) [video]
- [X] [**Java**: _3D Game Development with LWJGL 3_](https://lwjglgamedev.gitbooks.io/3d-game-development-with-lwjgl/content/)
- [X] [**JavaScript**: _2D breakout game using Phaser_](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_breakout_game_Phaser)
- [X] [**JavaScript**: _How to Make Flappy Bird in HTML5 With Phaser_](http://www.lessmilk.com/tutorial/flappy-bird-phaser-1)
- [X] [**JavaScript**: _Developing Games with React, Redux, and SVG_](https://auth0.com/blog/developing-games-with-react-redux-and-svg-part-1/)
- [X] [**JavaScript**: _Build your own 8-Ball Pool game from scratch_](https://www.youtube.com/watch?v=aXwCrtAo4Wc) [video]
- [X] [**JavaScript**: _How to Make Your First Roguelike_](https://gamedevelopment.tutsplus.com/tutorials/how-to-make-your-first-roguelike--gamedev-13677)
- [X] [**JavaScript**: _Think like a programmer: How to build Snake using only JavaScript, HTML & CSS_](https://medium.freecodecamp.org/think-like-a-programmer-how-to-build-snake-using-only-javascript-html-and-css-7b1479c3339e)
- [X] [**Lua**: _BYTEPATH_](https://github.com/SSYGEN/blog/issues/30)
- [X] [**Python**: _Developing Games With PyGame_](https://pythonprogramming.net/pygame-python-3-part-1-intro/)
- [X] [**Python**: _Making Games with Python & Pygame_](https://inventwithpython.com/makinggames.pdf) [pdf]
- [X] [**Python**: _Roguelike Tutorial Revised_](http://rogueliketutorials.com/)
- [X] [**Ruby**: _Developing Games With Ruby_](https://leanpub.com/developing-games-with-ruby/read)
- [X] [**Ruby**: _Ruby Snake_](https://www.diatomenterprises.com/gamedev-on-ruby-why-not/)
- [X] [**Rust**: _Adventures in Rust: A Basic 2D Game_](https://a5huynh.github.io/posts/2018/adventures-in-rust/)
- [X] [**Rust**: _Roguelike Tutorial in Rust + tcod_](https://tomassedovic.github.io/roguelike-tutorial/)

#### Build your own `Git`

- [X] [**Haskell**: _Reimplementing "git clone" in Haskell from the bottom up_](http://stefan.saasen.me/articles/git-clone-in-haskell-from-the-bottom-up/)
- [X] [**JavaScript**: _Gitlet_](http://gitlet.maryrosecook.com/docs/gitlet.html)
- [X] [**JavaScript**: _Build GIT - Learn GIT_](https://kushagra.dev/blog/build-git-learn-git/)
- [X] [**Python**: _Just enough of a Git client to create a repo, commit, and push itself to GitHub_](https://benhoyt.com/writings/pygit/)
- [X] [**Python**: _Write yourself a Git!_](https://wyag.thb.lt/)
- [X] [**Python**: _ugit: Learn Git Internals by Building Git Yourself_](https://www.leshenko.net/p/ugit/)
- [X] [**Ruby**: _Rebuilding Git in Ruby_](https://robots.thoughtbot.com/rebuilding-git-in-ruby)

#### Build your own `Network Stack`

- [X] [**C**: _Beej's Guide to Network Programming_](http://beej.us/guide/bgnet/)
- [X] [**C**: _Let's code a TCP/IP stack_](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/)
- [X] [**C / Python**: _Build your own VPN/Virtual Switch_](https://github.com/peiyuanix/build-your-own-zerotier)
- [X] [**Ruby**: _How to build a network stack in Ruby_](https://medium.com/geckoboard-under-the-hood/how-to-build-a-network-stack-in-ruby-f73aeb1b661b)

#### Build your own `Neural Network`

- [X] [**C#**: _Neural Network OCR_](https://www.codeproject.com/Articles/11285/Neural-Network-OCR)
- [X] [**F#**: _Building Neural Networks in F#_](https://towardsdatascience.com/building-neural-networks-in-f-part-1-a2832ae972e6)
- [X] [**Go**: _Build a multilayer perceptron with Golang_](https://made2591.github.io/posts/neuralnetwork)
- [X] [**Go**: _How to build a simple artificial neural network with Go_](https://sausheong.github.io/posts/how-to-build-a-simple-artificial-neural-network-with-go/)
- [X] [**Go**: _Building a Neural Net from Scratch in Go_](https://datadan.io/blog/neural-net-with-go)
- [X] [**JavaScript / Java**: _Neural Networks - The Nature of Code_](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6aCibgK1PTWWu9by6XFdCfh) [video]
- [X] [**JavaScript**: _Neural networks from scratch for JavaScript linguists (Part1 — The Perceptron)_](https://hackernoon.com/neural-networks-from-scratch-for-javascript-linguists-part1-the-perceptron-632a4d1fbad2)
- [X] [**Python**: _A Neural Network in 11 lines of Python_](https://iamtrask.github.io/2015/07/12/basic-python-network/)
- [X] [**Python**: _Implement a Neural Network from Scratch_](https://victorzhou.com/blog/intro-to-neural-networks/)
- [X] [**Python**: _Optical Character Recognition (OCR)_](http://aosabook.org/en/500L/optical-character-recognition-ocr.html)
- [X] [**Python**: _Traffic signs classification with a convolutional network_](https://navoshta.com/traffic-signs-classification/)
- [X] [**Python**: _Generate Music using LSTM Neural Network in Keras_](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5)
- [X] [**Python**: _An Introduction to Convolutional Neural Networks_](https://victorzhou.com/blog/intro-to-cnns-part-1/)
- [X] [**Python**: _Neural Networks: Zero to Hero_](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

#### Build your own `Operating System`

- [X] [**Assembly**: _Writing a Tiny x86 Bootloader_](http://joebergeron.io/posts/post_two.html)
- [X] [**Assembly**: _Baking Pi – Operating Systems Development_](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/index.html)
- [X] [**C**: _Building a software and hardware stack for a simple computer from scratch_](https://www.youtube.com/watch?v=ZjwvMcP3Nf0&list=PLU94OURih-CiP4WxKSMt3UcwMSDM3aTtX) [video]
- [X] [**C**: _Operating Systems: From 0 to 1_](https://tuhdo.github.io/os01/)
- [X] [**C**: _The little book about OS development_](https://littleosbook.github.io/)
- [X] [**C**: _Roll your own toy UNIX-clone OS_](http://jamesmolloy.co.uk/tutorial_html/)
- [X] [**C**: _Kernel 101 – Let's write a Kernel_](https://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)
- [X] [**C**: _Kernel 201 – Let's write a Kernel with keyboard and screen support_](https://arjunsreedharan.org/post/99370248137/kernel-201-lets-write-a-kernel-with-keyboard)
- [X] [**C**: _Build a minimal multi-tasking kernel for ARM from scratch_](https://github.com/jserv/mini-arm-os)
- [X] [**C**: _How to create an OS from scratch_](https://github.com/cfenollosa/os-tutorial)
- [X] [**C**: _Malloc tutorial_](https://danluu.com/malloc-tutorial/)
- [X] [**C**: _Hack the virtual memory_](https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/)
- [X] [**C**: _Learning operating system development using Linux kernel and Raspberry Pi_](https://github.com/s-matyukevich/raspberry-pi-os)
- [X] [**C**: _Operating systems development for Dummies_](https://medium.com/@lduck11007/operating-systems-development-for-dummies-3d4d786e8ac)
- [X] [**C++**: _Write your own Operating System_](https://www.youtube.com/playlist?list=PLHh55M_Kq4OApWScZyPl5HhgsTJS9MZ6M) [video]
- [X] [**C++**: _Writing a Bootloader_](http://3zanders.co.uk/2017/10/13/writing-a-bootloader/)
- [X] [**Rust**: _Writing an OS in Rust_](https://os.phil-opp.com/)
- [X] [**Rust**: _Add RISC-V Rust Operating System Tutorial_](https://osblog.stephenmarz.com/)
- [X] [**(any)**: _Linux from scratch_](https://linuxfromscratch.org/lfs)

#### Build your own `Physics Engine`

- [X] [**C**: _Video Game Physics Tutorial_](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics)
- [X] [**C++**: _Game physics series by Allen Chou_](http://allenchou.net/game-physics-series/)
- [X] [**C++**: _How to Create a Custom Physics Engine_](https://gamedevelopment.tutsplus.com/series/how-to-create-a-custom-physics-engine--gamedev-12715)
- [X] [**C++**: _3D Physics Engine Tutorial_](https://www.youtube.com/playlist?list=PLEETnX-uPtBXm1KEr_2zQ6K_0hoGH6JJ0) [video]
- [X] [**JavaScript**: _How Physics Engines Work_](http://buildnewgames.com/gamephysics/)
- [X] [**JavaScript**: _Broad Phase Collision Detection Using Spatial Partitioning_](http://buildnewgames.com/broad-phase-collision-detection/)
- [X] [**JavaScript**: _Build a simple 2D physics engine for JavaScript games_](https://developer.ibm.com/tutorials/wa-build2dphysicsengine/?mhsrc=ibmsearch_a&mhq=2dphysic)

#### Build your own `Programming Language`

- [X] [**(any)**: _mal - Make a Lisp_](https://github.com/kanaka/mal#mal---make-a-lisp)
- [X] [**Assembly**: _Jonesforth_](https://github.com/nornagon/jonesforth/blob/master/jonesforth.S)
- [X] [**C**: _Baby's First Garbage Collector_](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)
- [X] [**C**: _Build Your Own Lisp: Learn C and build your own programming language in 1000 lines of code_](http://www.buildyourownlisp.com/)
- [X] [**C**: _Writing a Simple Garbage Collector in C_](http://maplant.com/gc.html)
- [X] [**C**: _C interpreter that interprets itself._](https://github.com/lotabout/write-a-C-interpreter)
- [X] [**C**: _A C & x86 version of the "Let's Build a Compiler" by Jack Crenshaw_](https://github.com/lotabout/Let-s-build-a-compiler)
- [X] [**C**: _A journey explaining how to build a compiler from scratch_](https://github.com/DoctorWkt/acwj)
- [X] [**C++**: _Writing Your Own Toy Compiler Using Flex_](https://gnuu.org/2009/09/18/writing-your-own-toy-compiler/)
- [X] [**C++**: _How to Create a Compiler_](https://www.youtube.com/watch?v=eF9qWbuQLuw) [video]
- [X] [**C++**: _Kaleidoscope: Implementing a Language with LLVM_](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html)
- [X] [**F#**: _Understanding Parser Combinators_](https://fsharpforfunandprofit.com/posts/understanding-parser-combinators/)
- [X] [**Elixir**: _Demystifying compilers by writing your own_](https://www.youtube.com/watch?v=zMJYoYwOCd4) [video]
- [X] [**Go**: _The Super Tiny Compiler_](https://github.com/hazbo/the-super-tiny-compiler)
- [X] [**Go**: _Lexical Scanning in Go_](https://www.youtube.com/watch?v=HxaD_trXwRE) [video]
- [X] [**Haskell**: _Let's Build a Compiler_](https://g-ford.github.io/cradle/)
- [X] [**Haskell**: _Write You a Haskell_](http://dev.stephendiehl.com/fun/)
- [X] [**Haskell**: _Write Yourself a Scheme in 48 Hours_](https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours)
- [X] [**Haskell**: _Write You A Scheme_](https://www.wespiser.com/writings/wyas/home.html)
- [X] [**Java**: _Crafting interpreters: A handbook for making programming languages_](http://www.craftinginterpreters.com/)
- [X] [**Java**: _Creating JVM Language_](http://jakubdziworski.github.io/categories.html#Enkel-ref)
- [X] [**JavaScript**: _The Super Tiny Compiler_](https://github.com/jamiebuilds/the-super-tiny-compiler)
- [X] [**JavaScript**: _The Super Tiny Interpreter_](https://github.com/keyanzhang/the-super-tiny-interpreter)
- [X] [**JavaScript**: _Little Lisp interpreter_](https://maryrosecook.com/blog/post/little-lisp-interpreter)
- [X] [**JavaScript**: _How to implement a programming language in JavaScript_](http://lisperator.net/pltut/)
- [X] [**JavaScript**: _Let's go write a Lisp_](https://idiocy.org/lets-go-write-a-lisp/part-1.html)
- [X] [**OCaml**: _Writing a C Compiler_](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
- [X] [**OCaml**: _Writing a Lisp, the series_](https://bernsteinbear.com/blog/lisp/)
- [X] [**Pascal**: _Let's Build a Compiler_](https://compilers.iecc.com/crenshaw/)
- [X] [**Python**: _A Python Interpreter Written in Python_](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
- [X] [**Python**: _lisp.py: Make your own Lisp interpreter_](http://khamidou.com/compilers/lisp.py/)
- [X] [**Python**: _How to Write a Lisp Interpreter in Python_](http://norvig.com/lispy.html)
- [X] [**Python**: _Let's Build A Simple Interpreter_](https://ruslanspivak.com/lsbasi-part1/)
- [X] [**Python**: _Make Your Own Simple Interpreted Programming Language_](https://www.youtube.com/watch?v=dj9CBS3ikGA&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD&index=1) [video]
- [X] [**Python**: _From Source Code To Machine Code: Build Your Own Compiler From Scratch_](https://build-your-own.org/compiler/)
- [X] [**Racket**: _Beautiful Racket: How to make your own programming languages with Racket_](https://beautifulracket.com/)
- [X] [**Ruby**: _A Compiler From Scratch_](https://www.destroyallsoftware.com/screencasts/catalog/a-compiler-from-scratch)
- [X] [**Ruby**: _Markdown compiler from scratch in Ruby_](https://blog.beezwax.net/2017/07/07/writing-a-markdown-compiler/)
- [X] [**Rust**: _Learning Parser Combinators With Rust_](https://bodil.lol/parser-combinators/)
- [X] [**Swift**: _Building a LISP from scratch with Swift_](https://www.uraimo.com/2017/02/05/building-a-lisp-from-scratch-with-swift/)
- [X] [**TypeScript**: _Build your own WebAssembly Compiler_](https://blog.scottlogic.com/2019/05/17/webassembly-compiler.html)

#### Build your own `Regex Engine`

- [X] [**C**: _A Regular Expression Matcher_](https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html)
- [X] [**C**: _Regular Expression Matching Can Be Simple And Fast_](https://swtch.com/~rsc/regexp/regexp1.html)
- [X] [**Go**: _How to build a regex engine from scratch_](https://rhaeguard.github.io/posts/regex)
- [X] [**JavaScript**: _Build a Regex Engine in Less than 40 Lines of Code_](https://nickdrane.com/build-your-own-regex/)
- [X] [**JavaScript**: _How to implement regular expressions in functional javascript using derivatives_](http://dpk.io/dregs/toydregs)
- [X] [**JavaScript**: _Implementing a Regular Expression Engine_](https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/) 
- [X] [**Perl**: _How Regexes Work_](https://perl.plover.com/Regex/article.html)
- [X] [**Python**: _Build Your Own Regular Expression Engines: Backtracking, NFA, DFA_](https://build-your-own.org/b2a/r0_intro)
- [X] [**Scala**: _No Magic: Regular Expressions_](https://rcoh.svbtle.com/no-magic-regular-expressions)

#### Build your own `Search Engine`

- [X] [**CSS**: _A search engine in CSS_](https://stories.algolia.com/a-search-engine-in-css-b5ec4e902e97)
- [X] [**Python**: _Building a search engine using Redis and redis-py_](http://www.dr-josiah.com/2010/07/building-search-engine-using-redis-and.html)
- [X] [**Python**: _Building a Vector Space Indexing Engine in Python_](https://boyter.org/2010/08/build-vector-space-search-engine-python/)
- [X] [**Python**: _Building A Python-Based Search Engine_](https://www.youtube.com/watch?v=cY7pE7vX6MU) [video]
- [X] [**Python**: _Making text search learn from feedback_](https://medium.com/filament-ai/making-text-search-learn-from-feedback-4fe210fd87b0)
- [X] [**Python**: _Finding Important Words in Text Using TF-IDF_](https://stevenloria.com/tf-idf/)

#### Build your own `Shell`

- [X] [**C**: _Tutorial - Write a Shell in C_](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- [X] [**C**: _Let's build a shell!_](https://github.com/kamalmarhubi/shell-workshop)
- [X] [**C**: _Writing a UNIX Shell_](https://indradhanush.github.io/blog/writing-a-unix-shell-part-1/)
- [X] [**C**: _Build Your Own Shell_](https://github.com/tokenrove/build-your-own-shell)
- [X] [**C**: Write a shell in C](https://danishpraka.sh/posts/write-a-shell/)
- [X] [**Go**: _Writing a simple shell in Go_](https://sj14.gitlab.io/post/2018-07-01-go-unix-shell/)
- [X] [**Rust**: _Build Your Own Shell using Rust_](https://www.joshmcguigan.com/blog/build-your-own-shell-rust/)

#### Build your own `Template Engine`

- [X] [**JavaScript**: _JavaScript template engine in just 20 lines_](http://krasimirtsonev.com/blog/article/Javascript-template-engine-in-just-20-line)
- [X] [**JavaScript**: _Understanding JavaScript Micro-Templating_](https://medium.com/wdstack/understanding-javascript-micro-templating-f37a37b3b40e)
- [X] [**Python**: _Approach: Building a toy template engine in Python_](http://alexmic.net/building-a-template-engine/)
- [X] [**Python**: _A Template Engine_](http://aosabook.org/en/500L/a-template-engine.html)
- [X] [**Ruby**: _How to write a template engine in less than 30 lines of code_](http://bits.citrusbyte.com/how-to-write-a-template-library/)

#### Build your own `Text Editor`

- [X] [**C**: _Build Your Own Text Editor_](https://viewsourcecode.org/snaptoken/kilo/)
- [X] [**C++**: _Designing a Simple Text Editor_](http://www.fltk.org/doc-1.1/editor.html)
- [X] [**Python**: _Python Tutorial: Make Your Own Text Editor_](https://www.youtube.com/watch?v=xqDonHEYPgA) [video]
- [X] [**Python**: _Create a Simple Python Text Editor!_](http://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/)
- [X] [**Ruby**: _Build a Collaborative Text Editor Using Rails_](https://blog.aha.io/text-editor/)
- [X] [**Rust**: _Hecto: Build your own text editor in Rust_ ](https://www.flenker.blog/hecto/)

#### Build your own `Visual Recognition System`

- [X] [**Python**: _Developing a License Plate Recognition System with Machine Learning in Python_](https://medium.com/devcenter/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)
- [X] [**Python**: _Building a Facial Recognition Pipeline with Deep Learning in Tensorflow_](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)

#### Build your own `Voxel Engine`

- [X] [**C++**: _Let's Make a Voxel Engine_](https://sites.google.com/site/letsmakeavoxelengine/home)

#### Build your own `Web Browser`

- [X] [**Rust**: _Let's build a browser engine_](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
- [X] [**Python**: _Browser Engineering_](https://browser.engineering)

#### Build your own `Web Server`

- [X] [**C#**: _Writing a Web Server from Scratch_](https://www.codeproject.com/Articles/859108/Writing-a-Web-Server-from-Scratch)
- [X] [**Node.js**: _Build Your Own Web Server From Scratch In JavaScript_](https://build-your-own.org/webserver/)
- [X] [**Node.js**: _Let's code a web server from scratch with NodeJS Streams_](https://www.codementor.io/@ziad-saab/let-s-code-a-web-server-from-scratch-with-nodejs-streams-h4uc9utji)
- [X] [**Node.js**: _lets-build-express_](https://github.com/antoaravinth/lets-build-express)
- [X] [**PHP**: _Writing a webserver in pure PHP_](http://station.clancats.com/writing-a-webserver-in-pure-php/)
- [X] [**Python**: _A Simple Web Server_](http://aosabook.org/en/500L/a-simple-web-server.html)
- [X] [**Python**: _Let's Build A Web Server._](https://ruslanspivak.com/lsbaws-part1/)
- [X] [**Python**: _Web application from scratch_](https://defn.io/2018/02/25/web-app-from-scratch-01/)
- [X] [**Python**: _Building a basic HTTP Server from scratch in Python_](http://joaoventura.net/blog/2017/python-webserver/)
- [X] [**Python**: _Implementing a RESTful Web API with Python & Flask_](http://blog.luisrei.com/articles/flaskrest.html)
- [X] [**Ruby**: _Building a simple websockets server from scratch in Ruby_](http://blog.honeybadger.io/building-a-simple-websockets-server-from-scratch-in-ruby/)

#### Uncategorized

- [X] [**(any)**: _From NAND to Tetris: Building a Modern Computer From First Principles_](http://nand2tetris.org/)
- [X] [**(any)**:  build-your-own-x-vibe-coding: BYOX-style tutorials adapted for vibe coding](https://github.com/inFaaa/build-your-own-x-vibe-coding)
- [X] [**Alloy**: _The Same-Origin Policy_](http://aosabook.org/en/500L/the-same-origin-policy.html)
- [X] [**C**: _How to Write a Video Player in Less Than 1000 Lines_](http://dranger.com/ffmpeg/ffmpeg.html)
- [X] [**C**: _Learn how to write a hash table in C_](https://github.com/jamesroutley/write-a-hash-table)
- [X] [**C**: _The very basics of a terminal emulator_](https://www.uninformativ.de/blog/postings/2018-02-24/0/POSTING-en.html)
- [X] [**C**: _Write a System Call_](https://brennan.io/2016/11/14/kernel-dev-ep3/)
- [X] [**C**: _Sol - An MQTT broker from scratch_](https://codepr.github.io/posts/sol-mqtt-broker)
- [X] [**C++**: _Build your own VR headset for $200_](https://github.com/relativty/Relativ)
- [X] [**C++**: _How X Window Managers work and how to write one_](https://seasonofcode.com/posts/how-x-window-managers-work-and-how-to-write-one-part-i.html)
- [X] [**C++**: _Writing a Linux Debugger_](https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/)
- [X] [**C++**: _How a 64k intro is made_](http://www.lofibucket.com/articles/64k_intro.html)
- [X] [**C++**: _Make your own Game Engine_](https://www.youtube.com/playlist?list=PLlrATfBNZ98dC-V-N3m0Go4deliWHPFwT)
- [X] [**C#**: _C# Networking: Create a TCP chater server, TCP games, UDP Pong and more_](https://16bpp.net/tutorials/csharp-networking)
- [X] [**C#**: _Loading and rendering 3D skeletal animations from scratch in C# and GLSL_](https://www.seanjoflynn.com/research/skeletal-animation.html)
- [X] [**Clojure**: _Building a spell-checker_](https://bernhardwenzel.com/articles/clojure-spellchecker/)
- [X] [**Go**: _Build A Simple Terminal Emulator In 100 Lines of Golang_](https://ishuah.com/2021/03/10/build-a-terminal-emulator-in-100-lines-of-go/)
- [X] [**Go**: _Let's Create a Simple Load Balancer_](https://kasvith.me/posts/lets-create-a-simple-lb-go/)
- [X] [**Go**: _Video Encoding from Scratch_](https://github.com/kevmo314/codec-from-scratch)
- [X] [**Java**: _How to Build an Android Reddit App_](https://www.youtube.com/playlist?list=PLgCYzUzKIBE9HUJU-upNvl3TRVAo9W47y) [video]
- [X] [**JavaScript**: _Build Your Own Module Bundler - Minipack_](https://github.com/ronami/minipack)
- [X] [**JavaScript**: _Learn JavaScript Promises by Building a Promise from Scratch_](https://levelup.gitconnected.com/understand-javascript-promises-by-building-a-promise-from-scratch-84c0fd855720)
- [X] [**JavaScript**: _Implementing promises from scratch (TDD way)_](https://www.mauriciopoppe.com/notes/computer-science/computation/promises/)
- [X] [**JavaScript**: _Implement your own — call(), apply() and bind() method in JavaScript_](https://blog.usejournal.com/implement-your-own-call-apply-and-bind-method-in-javascript-42cc85dba1b)
- [X] [**JavaScript**: _JavaScript Algorithms and Data Structures_](https://github.com/trekhleb/javascript-algorithms)
- [X] [**JavaScript**: _Build a ride hailing app with React Native_](https://pusher.com/tutorials/ride-hailing-react-native)
- [X] [**JavaScript**: _Build Your Own AdBlocker in (Literally) 10 Minutes_](https://levelup.gitconnected.com/building-your-own-adblocker-in-literally-10-minutes-1eec093b04cd)
- [X] [**Kotlin**: _Build Your Own Cache_](https://github.com/kezhenxu94/cache-lite)
- [X] [**Lua**: _Building a CDN from Scratch to Learn about CDN_](https://github.com/leandromoreira/cdn-up-and-running)
- [X] [**Nim**: _Writing a Redis Protocol Parser_](https://xmonader.github.io/nimdays/day12_resp.html)
- [X] [**Nim**: _Writing a Build system_](https://xmonader.github.io/nimdays/day11_buildsystem.html)
- [X] [**Nim**: _Writing a MiniTest Framework_](https://xmonader.github.io/nimdays/day08_minitest.html)
- [X] [**Nim**: _Writing a DMIDecode Parser_](https://xmonader.github.io/nimdays/day01_dmidecode.html)
- [X] [**Nim**: _Writing a INI Parser_](https://xmonader.github.io/nimdays/day05_iniparser.html)
- [X] [**Nim**: _Writing a Link Checker_](https://xmonader.github.io/nimdays/day04_asynclinkschecker.html)
- [X] [**Nim**: _Writing a URL Shortening Service_](https://xmonader.github.io/nimdays/day07_shorturl.html)
- [X] [**Node.js**: _Build a static site generator in 40 lines with Node.js_](https://www.webdevdrops.com/en/build-static-site-generator-nodejs-8969ebe34b22/)
- [X] [**Node.js**: _Building A Simple Single Sign On(SSO) Server And Solution From Scratch In Node.js._](https://codeburst.io/building-a-simple-single-sign-on-sso-server-and-solution-from-scratch-in-node-js-ea6ee5fdf340)
- [X] [**Node.js**: _How to create a real-world Node CLI app with Node_](https://medium.freecodecamp.org/how-to-create-a-real-world-node-cli-app-with-node-391b727bbed3)
- [X] [**Node.js**: _Build a DNS Server in Node.js_](https://engineerhead.github.io/dns-server/)
- [X] [**PHP**: _Write your own MVC from scratch in PHP_ ](https://chaitya62.github.io/2018/04/29/Writing-your-own-MVC-from-Scratch-in-PHP.html)
- [X] [**PHP**: _Make your own blog_](https://ilovephp.jondh.me.uk/en/tutorial/make-your-own-blog)
- [X] [**PHP**: _Modern PHP Without a Framework_](https://kevinsmith.io/modern-php-without-a-framework)
- [X] [**PHP**: _Code a Web Search Engine in PHP_](https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/)
- [X] [**Python**: _Build a Deep Learning Library_](https://www.youtube.com/watch?v=o64FV-ez6Gw) [video]
- [X] [**Python**: _How to Build a Kick-Ass Mobile Document Scanner in Just 5 Minutes_](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [X] [**Python**: _Continuous Integration System_](http://aosabook.org/en/500L/a-continuous-integration-system.html)
- [X] [**Python**: _Recommender Systems in Python: Beginner Tutorial_](https://www.datacamp.com/community/tutorials/recommender-systems-python)
- [X] [**Python**: _Write SMS-spam detector with Scikit-learn_](https://medium.com/@kopilov.vlad/detect-sms-spam-in-kaggle-with-scikit-learn-5f6afa7a3ca2)
- [X] [**Python**: _A Simple Content-Based Recommendation Engine in Python_](http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html)
- [X] [**Python**: _Stock Market Predictions with LSTM in Python_](https://www.datacamp.com/community/tutorials/lstm-python-stock-market)
- [X] [**Python**: _Building a simple Generative Adversarial Network (GAN) using Tensorflow_](https://blog.paperspace.com/implementing-gans-in-tensorflow/)
- [X] [**Python**: _Learn ML Algorithms by coding: Decision Trees_](https://lethalbrains.com/learn-ml-algorithms-by-coding-decision-trees-439ac503c9a4)
- [X] [**Python**: _JSON Decoding Algorithm_](https://github.com/cheery/json-algorithm)
- [X] [**Python**: _Build your own Git plugin with python_](https://joshburns-xyz.vercel.app/posts/build-your-own-git-plugin)
- [X] [**Ruby**: _A Pedometer in the Real World_](http://aosabook.org/en/500L/a-pedometer-in-the-real-world.html)
- [X] [**Ruby**: _Creating a Linux Desktop application with Ruby_](https://iridakos.com/tutorials/2018/01/25/creating-a-gtk-todo-application-with-ruby)
- [X] [**Rust**: _Building a DNS server in Rust_](https://github.com/EmilHernvall/dnsguide/blob/master/README.md)
- [X] [**Rust**: _Writing Scalable Chat Service from Scratch_](https://nbaksalyar.github.io/2015/07/10/writing-chat-in-rust.html)
- [X] [**Rust**: _WebGL + Rust: Basic Water Tutorial_](https://www.chinedufn.com/3d-webgl-basic-water-tutorial/)
- [X] [**TypeScript**: _Tiny Package Manager: Learns how npm or Yarn works_](https://github.com/g-plane/tiny-package-manager)
- [X] [Generate Manim videos](https://github.com/ManimCommunity/Manim)
    - skills: ./skills/manim-composer
