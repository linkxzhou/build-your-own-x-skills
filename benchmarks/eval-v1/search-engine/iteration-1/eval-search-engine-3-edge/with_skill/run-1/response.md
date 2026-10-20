The user says "I don't have a dataset. What should I index?" This is a question without much context. There's no prior conversation. The question seems to be about indexing — possibly for a search engine, RAG, vector database, or some project. Without context, I should figure out what they're working on. But there's no context at all in this thread.

Let me check the workspace to see if there's any project context — maybe there's a project in the workspace that gives hints about what they're building.

Let me look at the workspace files first.The workspace only contains the build-your-own-x skill files. There's no user project here. The question "I don't have a dataset. What should I index?" is ambiguous — it could relate to:

1. Building a search engine / full-text search (inverted index)
2. Building a vector database / RAG (embeddings index)
3. Building a database (B-tree index)
4. Some ML project

Given the workspace has the build-your-own-x skill, the user might be in the context of a learning project — e.g., "build your own search engine" or "build your own database". The question "What should I index?" strongly suggests they're building something that needs an index (search engine, vector DB, RAG) and they lack a dataset to index.

The skill instructions say: when the user's task matches a skill's description, read the SKILL.md first. Does this match? The user is asking what to index — this could be part of a build-your-own-x project (e.g., building a search engine and needing data). The skill covers "which build-your-own project to start with" and hands off to sub-skills. The question is ambiguous but plausibly matches — they may be starting a project like a search engine and need a dataset.

Actually, let me think. The user's question is short and contextless. The best response: ask what they're building OR give concrete dataset suggestions for common indexing projects. Given the environment (build-your-own-x skill present), it's likely they're doing a hands-on project like building a search engine, vector DB, or database and need data to index.

I should read the SKILL.md to see if it has guidance on datasets for such projects. The skill says to read it before doing anything else when the task matches. The question "I don't have a dataset. What should I index?" — if they're building a search engine or similar, this matches the skill's coaching scope. Let me read the main SKILL.md.

Let me also check the manifest to see what categories exist, which might help me give targeted advice.You don't need a special dataset — pick a corpus that matches what you're building. Good starting points by project type:

**Full-text search engine (inverted index)**
- Classic IR collections: CACM (3,204 abstracts) or Cranfield (1,400 docs) — small, plain text, and they ship with queries + relevance judgments so you can actually measure precision/recall instead of eyeballing results.
- 100–500 Project Gutenberg books — free plain text, zero parsing pain.
- One Stack Exchange dump (e.g., english.stackexchange.com) — real-world messy text, and upvotes give you a free relevance signal.

**Vector search / RAG (embeddings index)**
- arXiv abstracts (Kaggle, ~2M rows — sample 50k to start) or a Wikipedia subset.
- Your own notes, bookmarks, or PDFs — the most motivating option, because you can judge retrieval quality yourself.

**Database (B-tree / LSM tree)**
- No dataset needed. Generate synthetic keys (`uuid4` or sequential ints) and random values. What matters is workload shape — key distribution, value size, write/read ratio — which you control in the benchmark harness.

For any learning project, keep it small enough to fit in memory: 10k–100k documents is the sweet spot. You want index-build times in seconds so the edit-run-debug loop stays fast.

What are you building, and in which language? That decides which track I'd coach you through.