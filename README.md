# 背景
本项目的目标是将 `https://github.com/codecrafters-io/build-your-own-x` 中的所有项目，逐步转换为 skills，让每个开发者都能通过 AI 技术，快速学习到各种技能。

## 目录结构
```
build-your-own-x-skills/
├── .claude/skills/          # Claude Code 技能目录，软链到 skills/，提供给 Claude Code 使用
├── .codebuddy/skills/       # CodeBuddy 技能目录，软链到 skills/，提供给 Codebuddy IDE 使用
├── .trae/skills/            # TRAE 技能目录，软链到 skills/，提供给 TRAE IDE 使用
├── .gemini/skills/          # gemini 技能目录，软链到 skills/，提供给 Gemini-Cli 使用
|── skills/                  # 技能目录，提供给 Codex-Cli 使用，可以在当前目录修改或者添加
├── examples/                # 示例项目
└── tests/                   # 技能测试
├── README.md                # 项目 README  
├── init.sh                  # 初始化技能脚本，用于各个平台的 skills 的目录软链，如果存在则不操作
└── REDME_PROMPT.md          # 每个 skills 的测试提示词
```

## 安装
1. 克隆项目到本地
2. 运行 `init.sh` 脚本，将技能目录软链到 `./skills` 目录
3. 开始使用技能

## 完成进度
![Progress](https://img.shields.io/badge/进度-1%25-red?style=flat-square)

▓░░░░░░░░░░░░░░░░░░░ 1%

## build-your-own-x 项目列表

#### 构建你自己的 `3D 渲染器`

- [ ] [**C++**: _光线追踪导论：一种创建 3D 图像的简单方法_](https://www.scratchapixel.com/lessons/3d-basic-rendering/introduction-to-ray-tracing/how-does-it-work)
- [ ] [**C++**: _OpenGL 如何工作：500 行代码实现软件渲染_](https://github.com/ssloy/tinyrenderer/wiki)
- [ ] [**C++**: _《德军总部 3D》射线投射引擎_](http://lodev.org/cgtutor/raycasting.html)
- [ ] [**C++**: _基于物理的渲染：从理论到实现_](http://www.pbr-book.org/)
- [ ] [**C++**: _周末搞定光线追踪（Ray Tracing in One Weekend）_](https://raytracing.github.io/books/RayTracingInOneWeekend.html)
- [ ] [**C++**: _光栅化：一次实用实现_](https://www.scratchapixel.com/lessons/3d-basic-rendering/rasterization-practical-implementation/overview-rasterization-algorithm)
- [ ] [**C# / TypeScript / JavaScript**: _从零学习用 C#、TypeScript 或 JavaScript 编写 3D 软渲染引擎_](https://www.davrous.com/2013/06/13/tutorial-series-learning-how-to-write-a-3d-soft-engine-from-scratch-in-c-typescript-or-javascript/)
- [ ] [**Java / JavaScript**: _构建你自己的 3D 渲染器_](https://avik-das.github.io/build-your-own-raytracer/)
- [ ] [**Java**: _如何用纯 Java 创建一个简单的 3D 渲染引擎_](http://blog.rogach.org/2015/08/how-to-create-your-own-simple-3d-render.html)
- [ ] [**JavaScript / Pseudocode**: _从零开始的计算机图形学_](http://www.gabrielgambetta.com/computer-graphics-from-scratch/introduction.html)
- [ ] [**Python**: _一个 3D 建模器_](http://aosabook.org/en/500L/a-3d-modeller.html)

#### 构建你自己的 `增强现实（AR）`

- [ ] [**C#**: _入门教程：使用 Vuforia 与 Unity 3D 的增强现实应用_](https://www.youtube.com/watch?v=uXNjNcqW4kY) [video]
- [ ] [**C#**: _Unity ARCore 教程_](https://www.youtube.com/playlist?list=PLKIKuXdn4ZMjuUAtdQfK1vwTZPQn_rgSv) [video]
- [ ] [**C#**: _Unity AR 传送门（Portal）教程_](https://www.youtube.com/playlist?list=PLPCqNOwwN794Gz5fzUSi1p4OqLU0HTmvn) [video]
- [ ] [**C#**: _如何在 Unity ARCore 中创建一条 AR 龙_](https://www.youtube.com/watch?v=qTSDPkPyPqs) [video]
- [ ] [**C#**: _AR 教程：ARKit 传送门通往“颠倒世界”_](https://www.youtube.com/watch?v=Z5AmqMuNi08) [video]
- [ ] [**Python**: _用 Python 与 OpenCV 实现增强现实_](https://bitesofcode.wordpress.com/2017/09/12/augmented-reality-with-python-and-opencv-part-1/)

#### 构建你自己的 `BitTorrent 客户端`

- [ ] [**C#**: _用 C# 从零构建 BitTorrent 客户端_](https://www.seanjoflynn.com/research/bittorrent.html)
- [ ] [**Go**: _用 Go 从底层开始构建 BitTorrent 客户端_](https://blog.jse.li/posts/torrent/)
- [ ] [**Nim**: _编写一个 Bencode 解析器_](https://xmonader.github.io/nimdays/day02_bencode.html)
- [ ] [**Node.js**: _自己写一个 BitTorrent 客户端_](https://allenkim67.github.io/programming/2016/05/04/how-to-make-your-own-bittorrent-client.html)
- [ ] [**Python**: _Python 3.5 的 BitTorrent 客户端_](http://markuseliasson.se/article/bittorrent-in-python/)

#### 构建你自己的 `区块链 / 加密货币`

- [ ] [**ATS**: _函数式区块链_](https://beta.observablehq.com/@galletti94/functional-blockchain)
- [ ] [**C#**: _用 C# 编程实现区块链_](https://programmingblockchain.gitbooks.io/programmingblockchain/)
- [ ] [**Crystal**: _用 Crystal 实现你自己的区块链与 PoW 算法_](https://medium.com/@bradford_hamilton/write-your-own-blockchain-and-pow-algorithm-using-crystal-d53d5d9d0c52)
- [ ] [**Go**: _用 Go 构建区块链_](https://jeiwan.net/posts/building-blockchain-in-go-part-1/)
- [ ] [**Go**: _用不到 200 行 Go 写出你自己的区块链_](https://medium.com/@mycoralhealth/code-your-own-blockchain-in-less-than-200-lines-of-go-e296282bcffc)
- [ ] [**Java**: _用 Java 创建你的第一条区块链_](https://medium.com/programmers-blockchain/create-simple-blockchain-java-tutorial-from-scratch-6eeed3cb03fa)
- [ ] [**JavaScript**: _少于 1500 行代码的加密货币实现_](https://github.com/conradoqg/naivecoin)
- [ ] [**JavaScript**: _用 JavaScript 构建你自己的区块链_](https://github.com/nambrot/blockchain-in-js)
- [ ] [**JavaScript**: _学习并构建一个 JavaScript 区块链_](https://medium.com/digital-alchemy-holdings/learn-build-a-javascript-blockchain-part-1-ca61c285821e)
- [ ] [**JavaScript**: _用 JavaScript 创建区块链_](https://github.com/SavjeeTutorials/SavjeeCoin)
- [ ] [**JavaScript**: _如何发布一个可用于生产的加密货币_](https://hackernoon.com/how-to-launch-your-own-production-ready-cryptocurrency-ab97cb773371)
- [ ] [**JavaScript**: _在 Node.js 中编写区块链_](https://www.smashingmagazine.com/2020/02/cryptocurrency-blockchain-node-js/)
- [ ] [**Kotlin**: _用 Kotlin 实现加密货币_](https://medium.com/@vasilyf/lets-implement-a-cryptocurrency-in-kotlin-part-1-blockchain-8704069f8580)
- [ ] [**Python**: _通过构建来学习区块链_](https://hackernoon.com/learn-blockchains-by-building-one-117428612f46)
- [ ] [**Python**: _自己动手构建区块链：Python 教程_](http://ecomunsing.com/build-your-own-blockchain)
- [ ] [**Python**: _Python 区块链实用入门_](http://adilmoujahid.com/posts/2018/03/intro-blockchain-bitcoin-python/)
- [ ] [**Python**: _来构建最小的区块链_](https://medium.com/crypto-currently/lets-build-the-tiniest-blockchain-e70965a248b)
- [ ] [**Ruby**: _一步步编程实现区块链（手稿/书籍版）_](https://github.com/yukimotopress/programming-blockchains-step-by-step)
- [ ] [**Scala**: _如何构建一个基于 actor 的简单区块链_](https://medium.freecodecamp.org/how-to-build-a-simple-actor-based-blockchain-aac1e996c177)
- [ ] [**TypeScript**: _Naivecoin：构建加密货币的教程_](https://lhartikk.github.io/)
- [ ] [**TypeScript**: _NaivecoinStake：基于 PoS 共识构建加密货币的教程_](https://naivecoinstake.learn.uno/)
- [ ] [**Rust**: _用 Rust 与 Substrate 构建区块链（分步指南）_](https://hackernoon.com/building-a-blockchain-in-rust-and-substrate-a-step-by-step-guide-for-developers-kc223ybp)


#### 构建你自己的 `机器人（Bot）`

- [ ] [**Haskell**: _自己做一个 IRC 机器人_](https://wiki.haskell.org/Roll_your_own_IRC_bot)
- [ ] [**Node.js**: _用 Node.js 与 API.ai 创建一个简单的 Facebook Messenger AI 机器人_](https://tutorials.botsfloor.com/creating-a-simple-facebook-messenger-ai-bot-with-api-ai-in-node-js-50ae2fa5c80d)
- [ ] [**Node.js**: _如何制作一个响应式的 Telegram 机器人_](https://www.sohamkamani.com/blog/2016/09/21/making-a-telegram-bot/)
- [ ] [**Node.js**: _创建一个 Discord 机器人_](https://discordjs.guide/)
- [ ] [**Node.js**: _gifbot：构建一个 GitHub App_](https://blog.scottlogic.com/2017/05/22/gifbot-github-integration.html)
- [ ] [**Node.js**: _用 Web Speech API 与 Node.js 构建一个简单的 AI 聊天机器人_](https://www.smashingmagazine.com/2017/08/ai-chatbot-web-speech-api-node-js/)
- [ ] [**Python**: _如何用 Python 构建你的第一个 Slack 机器人_](https://www.fullstackpython.com/blog/build-first-slack-bot-python.html)
- [ ] [**Python**: _用 Python + Slack Events API + Django 在 20 分钟内构建 Slack 机器人_](https://medium.com/freehunch/how-to-build-a-slack-bot-with-python-using-slack-events-api-django-under-20-minute-code-included-269c3a9bf64e)
- [ ] [**Python**: _构建一个 Reddit 机器人_](http://pythonforengineers.com/build-a-reddit-bot-part-1/)
- [ ] [**Python**: _如何制作 Reddit 机器人_](https://www.youtube.com/watch?v=krTUf7BpTc0) [video]
- [ ] [**Python**: _如何用 Python 创建 Telegram 机器人_](https://www.freecodecamp.org/news/how-to-create-a-telegram-bot-using-python/)
- [ ] [**Python**: _使用 Tweepy 用 Python 创建 Twitter 机器人_](https://medium.freecodecamp.org/creating-a-twitter-bot-in-python-with-tweepy-ac524157a607)
- [ ] [**Python**: _用 Python 与 PRAW 创建 Reddit 机器人_](https://www.youtube.com/playlist?list=PLIFBTFgFpoJ9vmYYlfxRFV6U_XhG-4fpP) [video]
- [ ] [**R**: _用 R 构建一个加密货币交易机器人_](https://towardsdatascience.com/build-a-cryptocurrency-trading-bot-with-r-1445c429e1b1)
- [ ] [**Rust**: _用 Rust（或 C 等）为《星际争霸》写一个机器人_](https://habr.com/en/post/436254/)

#### 构建你自己的 `命令行工具`

- [ ] [**Go**: _用 Go 可视化本地 Git 贡献_](https://flaviocopes.com/go-git-contributions/)
- [ ] [**Go**: _用 Go 构建命令行应用：lolcat_](https://flaviocopes.com/go-tutorial-lolcat/)
- [ ] [**Go**: _用 Go 构建 CLI 命令：cowsay_](https://flaviocopes.com/go-tutorial-cowsay/)
- [ ] [**Go**: _Go CLI 教程：fortune 克隆_](https://flaviocopes.com/go-tutorial-fortune/)
- [ ] [**Nim**: _编写 stow 的替代方案来管理 dotfiles_](https://xmonader.github.io/nimdays/day06_nistow.html)
- [ ] [**Node.js**: _用 JavaScript 创建一个 CLI 工具_](https://citw.dev/tutorial/create-your-own-cli-tool)
- [ ] [**Rust**: _Rust 中的命令行应用_](https://rust-cli.github.io/book/index.html)
- [ ] [**Rust**: _用 Rust 编写命令行工具_](https://mattgathu.dev/2017/08/29/writing-cli-app-rust.html)
- [ ] [**Zig**: _从零用 Zig 构建你的 CLI 应用_](https://rebuild-x.github.io/docs/#/./zig/terminal/cli)


#### 构建你自己的 `数据库`

- [ ] [**C**: _来构建一个简单数据库_](https://cstack.github.io/db_tutorial/)
- [ ] [**C++**: _从零构建你自己的 Redis_](https://build-your-own.org/redis)
- [ ] [**C#**: _构建你自己的数据库_](https://www.codeproject.com/Articles/1029838/Build-Your-Own-Database)
- [ ] [**Clojure**: _考古学启发的数据库_](http://aosabook.org/en/500L/an-archaeology-inspired-database.html)
- [ ] [**Crystal**: _为什么你应该构建自己的 NoSQL 数据库_](https://medium.com/@marceloboeira/why-you-should-build-your-own-nosql-database-9bbba42039f5)
- [ ] [**Go**: _从零构建数据库：从 B+Tree 到 SQL，3000 行实现_](https://build-your-own.org/database/)
- [ ] [**Go**: _45 步写数据库：一系列以 TDD 为主的小型编码谜题_](https://trialofcode.org/database/)
- [ ] [**Go**: _从零构建你自己的 Redis_](https://www.build-redis-from-scratch.dev/)
- [ ] [**JavaScript**: _Dagoba：内存图数据库_](http://aosabook.org/en/500L/dagoba-an-in-memory-graph-database.html)
- [ ] [**Python**: _DBDB：狗窝数据库_](http://aosabook.org/en/500L/dbdb-dog-bed-database.html)
- [ ] [**Python**: _用 Python 写一个迷你 Redis_](http://charlesleifer.com/blog/building-a-simple-redis-server-with-python/)
- [ ] [**Ruby**: _用 Ruby 构建快速、持久化的 KV 存储_](https://dineshgowda.com/posts/build-your-own-persistent-kv-store/)
- [ ] [**Rust**: _构建你自己的 Redis 客户端与服务端_](https://tokio.rs/tokio/tutorial/setup)

#### 构建你自己的 `Docker`

- [ ] [**C**: _500 行代码实现 Linux 容器_](https://blog.lizzie.io/linux-containers-in-500-loc.html)
- [ ] [**Go**: _用不到 100 行 Go 构建自己的容器_](https://www.infoq.com/articles/build-a-container-golang)
- [ ] [**Go**: _用 Go 从零构建容器_](https://www.youtube.com/watch?v=8fi7uSYlOdc) [video]
- [ ] [**Python**: _Linux 容器工作坊：从零重建 Docker_](https://github.com/Fewbytes/rubber-docker)
- [ ] [**Python**: _一个 Docker 的概念验证替代品（100% Python）_](https://github.com/tonybaloney/mocker)
- [ ] [**Shell**: _用大约 100 行 bash 实现 Docker_](https://github.com/p8952/bocker)

#### 构建你自己的 `模拟器 / 虚拟机`

- [ ] [**C**: _自制字节码解释器_](https://medium.com/bumble-tech/home-grown-bytecode-interpreters-51e12d59b25c)
- [ ] [**C**: _用 C 写虚拟机_](http://web.archive.org/web/20200121100942/https://blog.felixangell.com/virtual-machine-in-c/)
- [ ] [**C**: _编写你自己的虚拟机_](https://justinmeiners.github.io/lc3-vm/)
- [ ] [**C**: _用 Cinoop 编写 Game Boy 模拟器_](https://cturt.github.io/cinoop.html)
- [ ] [**C++**: _如何写一个模拟器（CHIP-8 解释器）_](http://www.multigesture.net/articles/how-to-write-an-emulator-chip-8-interpreter/)
- [ ] [**C++**: _模拟器教程（CHIP-8 解释器）_](http://www.codeslinger.co.uk/pages/projects/chip8.html)
- [ ] [**C++**: _模拟器教程（GameBoy 模拟器）_](http://www.codeslinger.co.uk/pages/projects/gameboy.html)
- [ ] [**C++**: _模拟器教程（Master System 模拟器）_](http://www.codeslinger.co.uk/pages/projects/mastersystem/memory.html)
- [ ] [**C++**: _从零构建 NES 模拟器_](https://www.youtube.com/playlist?list=PLrOv9FMX8xJHqMvSGB_9G9nZZ_4IgteYf) [video]
- [ ] [**Common Lisp**: _用 Common Lisp 实现 CHIP-8_](http://stevelosh.com/blog/2016/12/chip8-cpu/)
- [ ] [**JavaScript**: _用 JavaScript 做 GameBoy 模拟_](http://imrannazar.com/GameBoy-Emulation-in-JavaScript)
- [ ] [**Python**: _模拟器基础：编写你自己的 Chip-8 模拟器/解释器_](http://omokute.blogspot.com.br/2012/06/emulation-basics-write-your-own-chip-8.html)
- [ ] [**Rust**: _0dmg：通过构建部分 Game Boy 模拟器学习 Rust_](https://jeremybanks.github.io/0dmg/)

#### 构建你自己的 `前端框架 / 库`

- [ ] [**JavaScript**: _JSX 到底是什么（让我们构建一个 JSX 渲染器）_](https://jasonformat.com/wtf-is-jsx/)
- [ ] [**JavaScript**: _从零构建你自己的 React（DIY 指南）_](https://github.com/hexacta/didact)
- [ ] [**JavaScript**: _从零构建 React_](https://www.youtube.com/watch?v=_MAD4Oly9yg) [video]
- [ ] [**JavaScript**: _Gooact：160 行 JavaScript 的 React_](https://medium.com/@sweetpalma/gooact-react-in-160-lines-of-javascript-44e0742ad60f)
- [ ] [**JavaScript**: _通过构建轻量 React DOM 来理解 React Reconciler 如何工作_](https://hackernoon.com/learn-you-some-custom-react-renderers-aed7164a4199)
- [ ] [**JavaScript**: _自己写一个 Redux_](https://zapier.com/engineering/how-to-build-redux/)
- [ ] [**JavaScript**: _让我们写 Redux！_](https://www.jamasoftware.com/blog/lets-write-redux/)
- [ ] [**JavaScript**: _Redux：从零实现 Store_](https://egghead.io/lessons/react-redux-implementing-store-from-scratch) [video]
- [ ] [**JavaScript**: _200 行 JavaScript 实现一个简化版 AngularJS_](https://blog.mgechev.com/2015/03/09/build-learn-your-own-light-lightweight-angularjs/)
- [ ] [**JavaScript**: _自己做一个 AngularJS_](http://teropa.info/blog/2013/11/03/make-your-own-angular-part-1-scopes-and-digest.html)
- [ ] [**JavaScript**: _如何实现你自己的 Virtual DOM_](https://medium.com/@deathmood/how-to-write-your-own-virtual-dom-ee74acc13060)
- [ ] [**JavaScript**: _从零构建前端框架（组件、模板、状态、VDOM）_](https://mfrachet.github.io/create-frontend-framework/)
- [ ] [**JavaScript**: _构建你自己的 React_](https://pomb.us/build-your-own-react/)
- [ ] [**JavaScript**: _构建一个自定义 React Renderer_](https://youtu.be/CGpMlWVcHok) [video]

#### 构建你自己的 `游戏`

- [ ] [**C**: _Handmade Hero_](https://handmadehero.org/)
- [ ] [**C**: _用 C 编写 NES 游戏_](https://nesdoug.com/)
- [ ] [**C**: _用 C 写国际象棋引擎_](https://www.youtube.com/playlist?list=PLZ1QII7yudbc-Ky058TEaOstZHVbT-2hg) [video]
- [ ] [**C**: _Let's Make: Dangerous Dave_](https://www.youtube.com/playlist?list=PLSkJey49cOgTSj465v2KbLZ7LMn10bCF9) [video]
- [ ] [**C**: _用 C 学习游戏编程_](https://www.youtube.com/playlist?list=PLT6WFYYZE6uLMcPGS3qfpYm7T_gViYMMt) [video]
- [ ] [**C**: _用 C 编写数独求解器_](https://www.youtube.com/playlist?list=PLkTXsX7igf8edTYU92nU-f5Ntzuf-RKvW) [video]
- [ ] [**C**: _用 C 编写 Rogue/Nethack RPG_](https://www.youtube.com/playlist?list=PLkTXsX7igf8erbWGYT4iSAhpnJLJ0Nk5G) [video]
- [ ] [**C**: _关于俄罗斯方块与重实现_](https://brennan.io/2015/06/12/tetris-reimplementation/)
- [ ] [**C++**: _Breakout_](https://learnopengl.com/In-Practice/2D-Game/Breakout)
- [ ] [**C++**: _入门游戏编程 v2.0_](http://lazyfoo.net/tutorials/SDL/)
- [ ] [**C++**: _面向初学者、平台无关、专注逻辑的 C++ 俄罗斯方块教程_](http://javilop.com/gamedev/tetris-tutorial-in-c-platform-independent-focused-in-game-logic-for-beginners/)
- [ ] [**C++**: _用 C++ 重制 Cavestory_](https://www.youtube.com/watch?v=ETvApbD5xRo&list=PLNOBk_id22bw6LXhrGfhVwqQIa-M2MsLa) [video]
- [ ] [**C++**: _重构 Cave Story_](https://www.youtube.com/playlist?list=PL006xsVEsbKjSKBmLu1clo85yLrwjY67X) [video]
- [ ] [**C++**: _从零做 Space Invaders_](http://nicktasios.nl/posts/space-invaders-from-scratch-part-1.html)
- [ ] [**C#**: _通过构建一个简单 RPG 学习 C#_](http://scottlilly.com/learn-c-by-building-a-simple-rpg-index/)
- [ ] [**C#**: _用 C# 创建 Roguelike 游戏_](https://roguesharp.wordpress.com/)
- [ ] [**C#**: _构建一个 C#/WPF RPG_](https://scottlilly.com/build-a-cwpf-rpg/)
- [ ] [**Go**: _用 Go 做游戏_](https://www.youtube.com/playlist?list=PLDZujg-VgQlZUy1iCqBbe5faZLMkA3g2x) [video]
- [ ] [**Java**: _用 Java 写 2D 游戏引擎（完整入门课）_](https://www.youtube.com/watch?v=025QFeZfeyM) [video]
- [ ] [**Java**: _LWJGL 3 的 3D 游戏开发_](https://lwjglgamedev.gitbooks.io/3d-game-development-with-lwjgl/content/)
- [ ] [**JavaScript**: _用 Phaser 制作 2D 打砖块_](https://developer.mozilla.org/en-US/docs/Games/Tutorials/2D_breakout_game_Phaser)
- [ ] [**JavaScript**: _用 Phaser 在 HTML5 中做 Flappy Bird_](http://www.lessmilk.com/tutorial/flappy-bird-phaser-1)
- [ ] [**JavaScript**: _用 React、Redux 与 SVG 开发游戏_](https://auth0.com/blog/developing-games-with-react-redux-and-svg-part-1/)
- [ ] [**JavaScript**: _从零构建你自己的 8 号球台球游戏_](https://www.youtube.com/watch?v=aXwCrtAo4Wc) [video]
- [ ] [**JavaScript**: _如何制作你的第一个 Roguelike_](https://gamedevelopment.tutsplus.com/tutorials/how-to-make-your-first-roguelike--gamedev-13677)
- [ ] [**JavaScript**: _像程序员一样思考：只用 JS/HTML/CSS 做贪吃蛇_](https://medium.freecodecamp.org/think-like-a-programmer-how-to-build-snake-using-only-javascript-html-and-css-7b1479c3339e)
- [ ] [**Lua**: _BYTEPATH_](https://github.com/SSYGEN/blog/issues/30)
- [ ] [**Python**: _用 PyGame 开发游戏_](https://pythonprogramming.net/pygame-python-3-part-1-intro/)
- [ ] [**Python**: _用 Python 与 Pygame 制作游戏_](https://inventwithpython.com/makinggames.pdf) [pdf]
- [ ] [**Python**: _Roguelike 教程（修订版）_](http://rogueliketutorials.com/)
- [ ] [**Ruby**: _用 Ruby 开发游戏_](https://leanpub.com/developing-games-with-ruby/read)
- [ ] [**Ruby**: _Ruby 贪吃蛇_](https://www.diatomenterprises.com/gamedev-on-ruby-why-not/)
- [ ] [**Rust**: _Rust 冒险：一个基础 2D 游戏_](https://a5huynh.github.io/posts/2018/adventures-in-rust/)
- [ ] [**Rust**: _Rust + tcod 的 Roguelike 教程_](https://tomassedovic.github.io/roguelike-tutorial/)

#### 构建你自己的 `Git`

- [ ] [**Haskell**: _用 Haskell 从底层重实现 “git clone”_](http://stefan.saasen.me/articles/git-clone-in-haskell-from-the-bottom-up/)
- [ ] [**JavaScript**: _Gitlet_](http://gitlet.maryrosecook.com/docs/gitlet.html)
- [ ] [**JavaScript**: _Build GIT - Learn GIT_](https://kushagra.dev/blog/build-git-learn-git/)
- [ ] [**Python**: _刚好够用的 Git 客户端：能创建仓库、提交并把自己推到 GitHub_](https://benhoyt.com/writings/pygit/)
- [ ] [**Python**: _给自己写一个 Git！_](https://wyag.thb.lt/)
- [ ] [**Python**: _ugit：通过自己构建 Git 来学习 Git 内部原理_](https://www.leshenko.net/p/ugit/)
- [ ] [**Ruby**: _用 Ruby 重建 Git_](https://robots.thoughtbot.com/rebuilding-git-in-ruby)

#### 构建你自己的 `网络协议栈`

- [ ] [**C**: _Beej 的网络编程指南_](http://beej.us/guide/bgnet/)
- [ ] [**C**: _让我们写一个 TCP/IP 协议栈_](http://www.saminiir.com/lets-code-tcp-ip-stack-1-ethernet-arp/)
- [ ] [**C / Python**: _构建你自己的 VPN/虚拟交换机_](https://github.com/peiyuanix/build-your-own-zerotier)
- [ ] [**Ruby**: _如何用 Ruby 构建网络协议栈_](https://medium.com/geckoboard-under-the-hood/how-to-build-a-network-stack-in-ruby-f73aeb1b661b)

#### 构建你自己的 `神经网络`

- [ ] [**C#**: _神经网络 OCR_](https://www.codeproject.com/Articles/11285/Neural-Network-OCR)
- [ ] [**F#**: _用 F# 构建神经网络_](https://towardsdatascience.com/building-neural-networks-in-f-part-1-a2832ae972e6)
- [ ] [**Go**: _用 Go 构建多层感知机_](https://made2591.github.io/posts/neuralnetwork)
- [ ] [**Go**: _如何用 Go 构建一个简单的人工神经网络_](https://sausheong.github.io/posts/how-to-build-a-simple-artificial-neural-network-with-go/)
- [ ] [**Go**: _用 Go 从零构建神经网络_](https://datadan.io/blog/neural-net-with-go)
- [ ] [**JavaScript / Java**: _神经网络：《代码本色》_](https://www.youtube.com/playlist?list=PLRqwX-V7Uu6aCibgK1PTWWu9by6XFdCfh) [video]
- [ ] [**JavaScript**: _面向 JavaScript 语言学家的神经网络从零开始（第 1 部分：感知机）_](https://hackernoon.com/neural-networks-from-scratch-for-javascript-linguists-part1-the-perceptron-632a4d1fbad2)
- [ ] [**Python**: _11 行 Python 的神经网络_](https://iamtrask.github.io/2015/07/12/basic-python-network/)
- [ ] [**Python**: _从零实现神经网络_](https://victorzhou.com/blog/intro-to-neural-networks/)
- [ ] [**Python**: _光学字符识别（OCR）_](http://aosabook.org/en/500L/optical-character-recognition-ocr.html)
- [ ] [**Python**: _用卷积网络进行交通标志分类_](https://navoshta.com/traffic-signs-classification/)
- [ ] [**Python**: _用 Keras 的 LSTM 生成音乐_](https://towardsdatascience.com/how-to-generate-music-using-a-lstm-neural-network-in-keras-68786834d4c5)
- [ ] [**Python**: _卷积神经网络（CNN）入门_](https://victorzhou.com/blog/intro-to-cnns-part-1/)
- [ ] [**Python**: _神经网络：从零到英雄（Zero to Hero）_](https://www.youtube.com/playlist?list=PLAqhIrjkxbuWI23v9cThsA9GvCAUhRvKZ)

#### 构建你自己的 `操作系统`

- [ ] [**Assembly**: _编写一个微型 x86 引导程序（Bootloader）_](http://joebergeron.io/posts/post_two.html)
- [ ] [**Assembly**: _Baking Pi：操作系统开发_](http://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/os/index.html)
- [ ] [**C**: _从零构建简单计算机的软件/硬件栈_](https://www.youtube.com/watch?v=ZjwvMcP3Nf0&list=PLU94OURih-CiP4WxKSMt3UcwMSDM3aTtX) [video]
- [ ] [**C**: _操作系统：从 0 到 1_](https://tuhdo.github.io/os01/)
- [ ] [**C**: _操作系统开发小书_](https://littleosbook.github.io/)
- [ ] [**C**: _自己做一个玩具 UNIX 克隆操作系统_](http://jamesmolloy.co.uk/tutorial_html/)
- [ ] [**C**: _Kernel 101：让我们写一个内核_](https://arjunsreedharan.org/post/82710718100/kernel-101-lets-write-a-kernel)
- [ ] [**C**: _Kernel 201：写一个带键盘与屏幕支持的内核_](https://arjunsreedharan.org/post/99370248137/kernel-201-lets-write-a-kernel-with-keyboard)
- [ ] [**C**: _从零为 ARM 构建一个最小多任务内核_](https://github.com/jserv/mini-arm-os)
- [ ] [**C**: _如何从零创建一个 OS_](https://github.com/cfenollosa/os-tutorial)
- [ ] [**C**: _malloc 教程_](https://danluu.com/malloc-tutorial/)
- [ ] [**C**: _黑进虚拟内存_](https://blog.holbertonschool.com/hack-the-virtual-memory-c-strings-proc/)
- [ ] [**C**: _用 Linux 内核与树莓派学习 OS 开发_](https://github.com/s-matyukevich/raspberry-pi-os)
- [ ] [**C**: _给小白的操作系统开发_](https://medium.com/@lduck11007/operating-systems-development-for-dummies-3d4d786e8ac)
- [ ] [**C++**: _写你自己的操作系统_](https://www.youtube.com/playlist?list=PLHh55M_Kq4OApWScZyPl5HhgsTJS9MZ6M) [video]
- [ ] [**C++**: _编写 Bootloader_](http://3zanders.co.uk/2017/10/13/writing-a-bootloader/)
- [ ] [**Rust**: _用 Rust 写操作系统_](https://os.phil-opp.com/)
- [ ] [**Rust**: _RISC-V 的 Rust 操作系统教程_](https://osblog.stephenmarz.com/)
- [ ] [**(any)**: _Linux From Scratch_](https://linuxfromscratch.org/lfs)

#### 构建你自己的 `物理引擎`

- [ ] [**C**: _视频游戏物理教程_](https://www.toptal.com/game/video-game-physics-part-i-an-introduction-to-rigid-body-dynamics)
- [ ] [**C++**: _Allen Chou 的游戏物理系列_](http://allenchou.net/game-physics-series/)
- [ ] [**C++**: _如何创建自定义物理引擎_](https://gamedevelopment.tutsplus.com/series/how-to-create-a-custom-physics-engine--gamedev-12715)
- [ ] [**C++**: _3D 物理引擎教程_](https://www.youtube.com/playlist?list=PLEETnX-uPtBXm1KEr_2zQ6K_0hoGH6JJ0) [video]
- [ ] [**JavaScript**: _物理引擎如何工作_](http://buildnewgames.com/gamephysics/)
- [ ] [**JavaScript**: _使用空间划分的广义阶段碰撞检测_](http://buildnewgames.com/broad-phase-collision-detection/)
- [ ] [**JavaScript**: _为 JavaScript 游戏构建一个简单 2D 物理引擎_](https://developer.ibm.com/tutorials/wa-build2dphysicsengine/?mhsrc=ibmsearch_a&mhq=2dphysic)

#### 构建你自己的 `编程语言`

- [ ] [**(any)**: _mal - Make a Lisp_](https://github.com/kanaka/mal#mal---make-a-lisp)
- [ ] [**Assembly**: _Jonesforth_](https://github.com/nornagon/jonesforth/blob/master/jonesforth.S)
- [ ] [**C**: _宝宝的第一个垃圾回收器_](http://journal.stuffwithstuff.com/2013/12/08/babys-first-garbage-collector/)
- [ ] [**C**: _构建你自己的 Lisp：用 1000 行代码学习 C 并写出语言_](http://www.buildyourownlisp.com/)
- [ ] [**C**: _用 C 编写一个简单垃圾回收器_](http://maplant.com/gc.html)
- [ ] [**C**: _能解释自身的 C 解释器_](https://github.com/lotabout/write-a-C-interpreter)
- [ ] [**C**: _Jack Crenshaw《Let’s Build a Compiler》的 C/x86 版本_](https://github.com/lotabout/Let-s-build-a-compiler)
- [ ] [**C**: _一段从零构建编译器的旅程_](https://github.com/DoctorWkt/acwj)
- [ ] [**C++**: _用 Flex 编写你自己的玩具编译器_](https://gnuu.org/2009/09/18/writing-your-own-toy-compiler/)
- [ ] [**C++**: _如何创建一个编译器_](https://www.youtube.com/watch?v=eF9qWbuQLuw) [video]
- [ ] [**C++**: _Kaleidoscope：用 LLVM 实现一门语言_](https://llvm.org/docs/tutorial/MyFirstLanguageFrontend/index.html)
- [ ] [**F#**: _理解解析器组合子_](https://fsharpforfunandprofit.com/posts/understanding-parser-combinators/)
- [ ] [**Elixir**: _通过自己写一个编译器来破除迷思_](https://www.youtube.com/watch?v=zMJYoYwOCd4) [video]
- [ ] [**Go**: _超小编译器（The Super Tiny Compiler）_](https://github.com/hazbo/the-super-tiny-compiler)
- [ ] [**Go**: _Go 词法扫描_](https://www.youtube.com/watch?v=HxaD_trXwRE) [video]
- [ ] [**Haskell**: _让我们构建一个编译器_](https://g-ford.github.io/cradle/)
- [ ] [**Haskell**: _Write You a Haskell_](http://dev.stephendiehl.com/fun/)
- [ ] [**Haskell**: _48 小时写一个 Scheme_](https://en.wikibooks.org/wiki/Write_Yourself_a_Scheme_in_48_Hours)
- [ ] [**Haskell**: _Write You A Scheme_](https://www.wespiser.com/writings/wyas/home.html)
- [ ] [**Java**: _《Crafting Interpreters》：制作编程语言的手册_](http://www.craftinginterpreters.com/)
- [ ] [**Java**: _创建 JVM 语言_](http://jakubdziworski.github.io/categories.html#Enkel-ref)
- [ ] [**JavaScript**: _超小编译器（The Super Tiny Compiler）_](https://github.com/jamiebuilds/the-super-tiny-compiler)
- [ ] [**JavaScript**: _超小解释器（The Super Tiny Interpreter）_](https://github.com/keyanzhang/the-super-tiny-interpreter)
- [ ] [**JavaScript**: _小型 Lisp 解释器_](https://maryrosecook.com/blog/post/little-lisp-interpreter)
- [ ] [**JavaScript**: _如何用 JavaScript 实现一门编程语言_](http://lisperator.net/pltut/)
- [ ] [**JavaScript**: _让我们写一个 Lisp_](https://idiocy.org/lets-go-write-a-lisp/part-1.html)
- [ ] [**OCaml**: _编写一个 C 编译器_](https://norasandler.com/2017/11/29/Write-a-Compiler.html)
- [ ] [**OCaml**: _写 Lisp 系列_](https://bernsteinbear.com/blog/lisp/)
- [ ] [**Pascal**: _让我们构建一个编译器_](https://compilers.iecc.com/crenshaw/)
- [ ] [**Python**: _用 Python 写的 Python 解释器_](http://aosabook.org/en/500L/a-python-interpreter-written-in-python.html)
- [ ] [**Python**: _lisp.py：做你自己的 Lisp 解释器_](http://khamidou.com/compilers/lisp.py/)
- [ ] [**Python**: _如何用 Python 写 Lisp 解释器_](http://norvig.com/lispy.html)
- [ ] [**Python**: _让我们构建一个简单解释器_](https://ruslanspivak.com/lsbasi-part1/)
- [ ] [**Python**: _制作你自己的简单解释型编程语言_](https://www.youtube.com/watch?v=dj9CBS3ikGA&list=PLZQftyCk7_SdoVexSmwy_tBgs7P0b97yD&index=1) [video]
- [ ] [**Python**: _从源代码到机器码：从零构建你自己的编译器_](https://build-your-own.org/compiler/)
- [ ] [**Racket**: _Beautiful Racket：如何用 Racket 制作自己的编程语言_](https://beautifulracket.com/)
- [ ] [**Ruby**: _从零构建编译器_](https://www.destroyallsoftware.com/screencasts/catalog/a-compiler-from-scratch)
- [ ] [**Ruby**: _用 Ruby 从零写 Markdown 编译器_](https://blog.beezwax.net/2017/07/07/writing-a-markdown-compiler/)
- [ ] [**Rust**: _用 Rust 学习解析器组合子_](https://bodil.lol/parser-combinators/)
- [ ] [**Swift**: _用 Swift 从零构建 Lisp_](https://www.uraimo.com/2017/02/05/building-a-lisp-from-scratch-with-swift/)
- [ ] [**TypeScript**: _构建你自己的 WebAssembly 编译器_](https://blog.scottlogic.com/2019/05/17/webassembly-compiler.html)

#### 构建你自己的 `正则表达式引擎`

- [ ] [**C**: _正则表达式匹配器_](https://www.cs.princeton.edu/courses/archive/spr09/cos333/beautiful.html)
- [ ] [**C**: _正则匹配可以既简单又快速_](https://swtch.com/~rsc/regexp/regexp1.html)
- [ ] [**Go**: _如何从零构建正则引擎_](https://rhaeguard.github.io/posts/regex)
- [ ] [**JavaScript**: _用不到 40 行代码构建正则引擎_](https://nickdrane.com/build-your-own-regex/)
- [ ] [**JavaScript**: _用函数式 JavaScript 通过导数法实现正则_](http://dpk.io/dregs/toydregs)
- [ ] [**JavaScript**: _实现一个正则表达式引擎_](https://deniskyashif.com/2019/02/17/implementing-a-regular-expression-engine/) 
- [ ] [**Perl**: _正则是如何工作的_](https://perl.plover.com/Regex/article.html)
- [ ] [**Python**: _构建你自己的正则引擎：回溯、NFA、DFA_](https://build-your-own.org/b2a/r0_intro)
- [ ] [**Scala**: _没有魔法：正则表达式_](https://rcoh.svbtle.com/no-magic-regular-expressions)

#### 构建你自己的 `搜索引擎`

- [ ] [**CSS**: _用 CSS 做一个搜索引擎_](https://stories.algolia.com/a-search-engine-in-css-b5ec4e902e97)
- [ ] [**Python**: _用 Redis 与 redis-py 构建搜索引擎_](http://www.dr-josiah.com/2010/07/building-search-engine-using-redis-and.html)
- [ ] [**Python**: _用 Python 构建向量空间索引搜索引擎_](https://boyter.org/2010/08/build-vector-space-search-engine-python/)
- [ ] [**Python**: _构建基于 Python 的搜索引擎_](https://www.youtube.com/watch?v=cY7pE7vX6MU) [video]
- [ ] [**Python**: _让文本搜索从反馈中学习_](https://medium.com/filament-ai/making-text-search-learn-from-feedback-4fe210fd87b0)
- [ ] [**Python**: _使用 TF-IDF 从文本中找出重要词_](https://stevenloria.com/tf-idf/)

#### 构建你自己的 `Shell`

- [ ] [**C**: _教程：用 C 写一个 Shell_](https://brennan.io/2015/01/16/write-a-shell-in-c/)
- [ ] [**C**: _让我们构建一个 Shell！_](https://github.com/kamalmarhubi/shell-workshop)
- [ ] [**C**: _编写 UNIX Shell_](https://indradhanush.github.io/blog/writing-a-unix-shell-part-1/)
- [ ] [**C**: _构建你自己的 Shell_](https://github.com/tokenrove/build-your-own-shell)
- [ ] [**C**: _用 C 写一个 Shell_](https://danishpraka.sh/posts/write-a-shell/)
- [ ] [**Go**: _用 Go 写一个简单 Shell_](https://sj14.gitlab.io/post/2018-07-01-go-unix-shell/)
- [ ] [**Rust**: _使用 Rust 构建你自己的 Shell_](https://www.joshmcguigan.com/blog/build-your-own-shell-rust/)

#### 构建你自己的 `模板引擎`

- [ ] [**JavaScript**: _20 行实现 JavaScript 模板引擎_](http://krasimirtsonev.com/blog/article/Javascript-template-engine-in-just-20-line)
- [ ] [**JavaScript**: _理解 JavaScript 微模板（Micro-Templating）_](https://medium.com/wdstack/understanding-javascript-micro-templating-f37a37b3b40e)
- [ ] [**Python**: _方法：用 Python 构建玩具模板引擎_](http://alexmic.net/building-a-template-engine/)
- [ ] [**Python**: _一个模板引擎_](http://aosabook.org/en/500L/a-template-engine.html)
- [ ] [**Ruby**: _如何在不到 30 行代码里写一个模板引擎_](http://bits.citrusbyte.com/how-to-write-a-template-library/)

#### 构建你自己的 `文本编辑器`

- [ ] [**C**: _构建你自己的文本编辑器_](https://viewsourcecode.org/snaptoken/kilo/)
- [ ] [**C++**: _设计一个简单文本编辑器_](http://www.fltk.org/doc-1.1/editor.html)
- [ ] [**Python**: _Python 教程：制作你自己的文本编辑器_](https://www.youtube.com/watch?v=xqDonHEYPgA) [video]
- [ ] [**Python**: _创建一个简单的 Python 文本编辑器！_](http://www.instructables.com/id/Create-a-Simple-Python-Text-Editor/)
- [ ] [**Ruby**: _用 Rails 构建协作式文本编辑器_](https://blog.aha.io/text-editor/)
- [ ] [**Rust**: _Hecto：用 Rust 构建你自己的文本编辑器_ ](https://www.flenker.blog/hecto/)

#### 构建你自己的 `视觉识别系统`

- [ ] [**Python**: _用 Python 机器学习开发车牌识别系统_](https://medium.com/devcenter/developing-a-license-plate-recognition-system-with-machine-learning-in-python-787833569ccd)
- [ ] [**Python**: _用 Tensorflow 深度学习构建人脸识别流水线_](https://hackernoon.com/building-a-facial-recognition-pipeline-with-deep-learning-in-tensorflow-66e7645015b8)

#### 构建你自己的 `体素引擎（Voxel Engine）`

- [ ] [**C++**: _让我们做一个体素引擎_](https://sites.google.com/site/letsmakeavoxelengine/home)

#### 构建你自己的 `网页浏览器`

- [ ] [**Rust**: _让我们构建一个浏览器引擎_](https://limpet.net/mbrubeck/2014/08/08/toy-layout-engine-1.html)
- [ ] [**Python**: _Browser Engineering_](https://browser.engineering)

#### 构建你自己的 `Web 服务器`

- [ ] [**C#**: _从零编写 Web 服务器_](https://www.codeproject.com/Articles/859108/Writing-a-Web-Server-from-Scratch)
- [ ] [**Node.js**: _用 JavaScript 从零构建你自己的 Web 服务器_](https://build-your-own.org/webserver/)
- [ ] [**Node.js**: _用 NodeJS Streams 从零写 Web 服务器_](https://www.codementor.io/@ziad-saab/let-s-code-a-web-server-from-scratch-with-nodejs-streams-h4uc9utji)
- [ ] [**Node.js**: _lets-build-express_](https://github.com/antoaravinth/lets-build-express)
- [ ] [**PHP**: _用纯 PHP 编写 Web 服务器_](http://station.clancats.com/writing-a-webserver-in-pure-php/)
- [ ] [**Python**: _一个简单的 Web 服务器_](http://aosabook.org/en/500L/a-simple-web-server.html)
- [ ] [**Python**: _让我们构建一个 Web 服务器_](https://ruslanspivak.com/lsbaws-part1/)
- [ ] [**Python**: _从零构建 Web 应用_](https://defn.io/2018/02/25/web-app-from-scratch-01/)
- [ ] [**Python**: _用 Python 从零构建基础 HTTP Server_](http://joaoventura.net/blog/2017/python-webserver/)
- [ ] [**Python**: _用 Python + Flask 实现 RESTful Web API_](http://blog.luisrei.com/articles/flaskrest.html)
- [ ] [**Ruby**: _用 Ruby 从零构建简单 websockets 服务器_](http://blog.honeybadger.io/building-a-simple-websockets-server-from-scratch-in-ruby/)

#### 未分类

- [ ] [**(any)**: _从 NAND 到俄罗斯方块：从第一性原理构建现代计算机_](http://nand2tetris.org/)
- [ ] [**(any)**:  _build-your-own-x-vibe-coding：面向“vibe coding”改编的 BYOX 风格教程_](https://github.com/inFaaa/build-your-own-x-vibe-coding)
- [ ] [**Alloy**: _同源策略_](http://aosabook.org/en/500L/the-same-origin-policy.html)
- [ ] [**C**: _如何用不到 1000 行代码写一个视频播放器_](http://dranger.com/ffmpeg/ffmpeg.html)
- [ ] [**C**: _学习如何用 C 写哈希表_](https://github.com/jamesroutley/write-a-hash-table)
- [ ] [**C**: _终端模拟器的基础知识_](https://www.uninformativ.de/blog/postings/2018-02-24/0/POSTING-en.html)
- [ ] [**C**: _编写一个系统调用_](https://brennan.io/2016/11/14/kernel-dev-ep3/)
- [ ] [**C**: _Sol：从零实现 MQTT Broker_](https://codepr.github.io/posts/sol-mqtt-broker)
- [ ] [**C++**: _用 200 美元构建你自己的 VR 头显_](https://github.com/relativty/Relativ)
- [ ] [**C++**: _X Window Manager 如何工作，以及如何编写一个_](https://seasonofcode.com/posts/how-x-window-managers-work-and-how-to-write-one-part-i.html)
- [ ] [**C++**: _编写 Linux 调试器_](https://blog.tartanllama.xyz/writing-a-linux-debugger-setup/)
- [ ] [**C++**: _一个 64k intro 是如何制作的_](http://www.lofibucket.com/articles/64k_intro.html)
- [ ] [**C++**: _自己做一个游戏引擎_](https://www.youtube.com/playlist?list=PLlrATfBNZ98dC-V-N3m0Go4deliWHPFwT)
- [ ] [**C#**: _C# 网络编程：TCP 聊天服务端、TCP 游戏、UDP Pong 等_](https://16bpp.net/tutorials/csharp-networking)
- [ ] [**C#**: _在 C# 与 GLSL 中从零加载并渲染 3D 骨骼动画_](https://www.seanjoflynn.com/research/skeletal-animation.html)
- [ ] [**Clojure**: _构建一个拼写检查器_](https://bernhardwenzel.com/articles/clojure-spellchecker/)
- [ ] [**Go**: _100 行 Go 构建简单终端模拟器_](https://ishuah.com/2021/03/10/build-a-terminal-emulator-in-100-lines-of-go/)
- [ ] [**Go**: _让我们创建一个简单负载均衡器_](https://kasvith.me/posts/lets-create-a-simple-lb-go/)
- [ ] [**Go**: _从零进行视频编码_](https://github.com/kevmo314/codec-from-scratch)
- [ ] [**Java**: _如何构建一个 Android Reddit 应用_](https://www.youtube.com/playlist?list=PLgCYzUzKIBE9HUJU-upNvl3TRVAo9W47y) [video]
- [ ] [**JavaScript**: _构建你自己的模块打包器：Minipack_](https://github.com/ronami/minipack)
- [ ] [**JavaScript**: _通过自己实现 Promise 来理解 JavaScript Promise_](https://levelup.gitconnected.com/understand-javascript-promises-by-building-a-promise-from-scratch-84c0fd855720)
- [ ] [**JavaScript**: _从零实现 Promise（TDD 风格）_](https://www.mauriciopoppe.com/notes/computer-science/computation/promises/)
- [ ] [**JavaScript**: _自己实现 JavaScript 的 call() / apply() / bind()_](https://blog.usejournal.com/implement-your-own-call-apply-and-bind-method-in-javascript-42cc85dba1b)
- [ ] [**JavaScript**: _JavaScript 算法与数据结构_](https://github.com/trekhleb/javascript-algorithms)
- [ ] [**JavaScript**: _用 React Native 构建网约车应用_](https://pusher.com/tutorials/ride-hailing-react-native)
- [ ] [**JavaScript**: _（真的）10 分钟写出你自己的 AdBlocker_](https://levelup.gitconnected.com/building-your-own-adblocker-in-literally-10-minutes-1eec093b04cd)
- [ ] [**Kotlin**: _构建你自己的缓存_](https://github.com/kezhenxu94/cache-lite)
- [ ] [**Lua**: _从零构建 CDN 来学习 CDN_](https://github.com/leandromoreira/cdn-up-and-running)
- [ ] [**Nim**: _编写 Redis 协议解析器_](https://xmonader.github.io/nimdays/day12_resp.html)
- [ ] [**Nim**: _编写构建系统_](https://xmonader.github.io/nimdays/day11_buildsystem.html)
- [ ] [**Nim**: _编写 MiniTest 测试框架_](https://xmonader.github.io/nimdays/day08_minitest.html)
- [ ] [**Nim**: _编写 DMIDecode 解析器_](https://xmonader.github.io/nimdays/day01_dmidecode.html)
- [ ] [**Nim**: _编写 INI 解析器_](https://xmonader.github.io/nimdays/day05_iniparser.html)
- [ ] [**Nim**: _编写链接检查器_](https://xmonader.github.io/nimdays/day04_asynclinkschecker.html)
- [ ] [**Nim**: _编写 URL 短链接服务_](https://xmonader.github.io/nimdays/day07_shorturl.html)
- [ ] [**Node.js**: _用 Node.js 用 40 行写静态站点生成器_](https://www.webdevdrops.com/en/build-static-site-generator-nodejs-8969ebe34b22/)
- [ ] [**Node.js**: _用 Node.js 从零构建一个简单 SSO 服务与方案_](https://codeburst.io/building-a-simple-single-sign-on-sso-server-and-solution-from-scratch-in-node-js-ea6ee5fdf340)
- [ ] [**Node.js**: _如何用 Node 创建一个真实世界的 Node CLI 应用_](https://medium.freecodecamp.org/how-to-create-a-real-world-node-cli-app-with-node-391b727bbed3)
- [ ] [**Node.js**: _用 Node.js 构建 DNS 服务器_](https://engineerhead.github.io/dns-server/)
- [ ] [**PHP**: _用 PHP 从零编写 MVC_ ](https://chaitya62.github.io/2018/04/29/Writing-your-own-MVC-from-Scratch-in-PHP.html)
- [ ] [**PHP**: _自己做一个博客_](https://ilovephp.jondh.me.uk/en/tutorial/make-your-own-blog)
- [ ] [**PHP**: _没有框架的现代 PHP_](https://kevinsmith.io/modern-php-without-a-framework)
- [ ] [**PHP**: _用 PHP 编写 Web 搜索引擎_](https://boyter.org/2013/01/code-for-a-search-engine-in-php-part-1/)
- [ ] [**Python**: _构建深度学习库_](https://www.youtube.com/watch?v=o64FV-ez6Gw) [video]
- [ ] [**Python**: _5 分钟构建一个超棒的移动文档扫描器_](https://www.pyimagesearch.com/2014/09/01/build-kick-ass-mobile-document-scanner-just-5-minutes/)
- [ ] [**Python**: _持续集成系统_](http://aosabook.org/en/500L/a-continuous-integration-system.html)
- [ ] [**Python**: _Python 推荐系统：入门教程_](https://www.datacamp.com/community/tutorials/recommender-systems-python)
- [ ] [**Python**: _用 Scikit-learn 写短信垃圾检测器_](https://medium.com/@kopilov.vlad/detect-sms-spam-in-kaggle-with-scikit-learn-5f6afa7a3ca2)
- [ ] [**Python**: _一个简单的基于内容的推荐引擎_](http://blog.untrod.com/2016/06/simple-similar-products-recommendation-engine-in-python.html)
- [ ] [**Python**: _用 LSTM 预测股市_](https://www.datacamp.com/community/tutorials/lstm-python-stock-market)
- [ ] [**Python**: _用 Tensorflow 构建一个简单 GAN_](https://blog.paperspace.com/implementing-gans-in-tensorflow/)
- [ ] [**Python**: _通过编码学习机器学习算法：决策树_](https://lethalbrains.com/learn-ml-algorithms-by-coding-decision-trees-439ac503c9a4)
- [ ] [**Python**: _JSON 解码算法_](https://github.com/cheery/json-algorithm)
- [ ] [**Python**: _用 Python 构建你自己的 Git 插件_](https://joshburns-xyz.vercel.app/posts/build-your-own-git-plugin)
- [ ] [**Ruby**: _现实世界里的计步器_](http://aosabook.org/en/500L/a-pedometer-in-the-real-world.html)
- [ ] [**Ruby**: _用 Ruby 创建 Linux 桌面应用_](https://iridakos.com/tutorials/2018/01/25/creating-a-gtk-todo-application-with-ruby)
- [ ] [**Rust**: _用 Rust 构建 DNS 服务器_](https://github.com/EmilHernvall/dnsguide/blob/master/README.md)
- [ ] [**Rust**: _从零编写可扩展聊天服务_](https://nbaksalyar.github.io/2015/07/10/writing-chat-in-rust.html)
- [ ] [**Rust**: _WebGL + Rust：基础水面教程_](https://www.chinedufn.com/3d-webgl-basic-water-tutorial/)
- [ ] [**TypeScript**: _Tiny Package Manager：学习 npm / Yarn 的工作方式_](https://github.com/g-plane/tiny-package-manager)
- [X] [生成 manim 视频](https://github.com/ManimCommunity/Manim)
    - skills：./skills/manim-composer