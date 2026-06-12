# linkforge

A multi-agent system that helps a single user ideate, write, and refine LinkedIn posts through a natural-language Telegram chat. Messages hit a FastAPI webhook, get routed by an super agent to specialist subagents (ideation, writing, refining), and drafts are persisted in SQLite. Quick `.commands` handle actions outside the chat memory of the agents.

## Project structure

```text
linkforge/
├── pyproject.toml              # Dependencies & tooling (uv, ruff)
├── uv.lock
├── README.md
├── DECISIONS.md                # Architecture decisions & rationale
├── data/
│   └── linkforge.db            # SQLite DB (state + approved drafts + agent sessions)
└── src/
    ├── main.py                 # FastAPI app, lifespan, /telegram/webhook endpoint
    ├── config.py               # Env/secrets loading
    ├── telegram/
    │   ├── client.py           # TelegramClient: sends messages via Bot API
    │   ├── webhook.py          # Webhook handling + .command routing
    │   └── auth.py             # Verify webhook secret & authorized user
    ├── database/
    │   ├── client.py           # SQLite connection helpers (low level functions)
    │   ├── schema.py           # Table creation (init_tables)
    │   └── operations.py       # Draft CRUD (save/get/approve)
    ├── agent_workforce/
    │   ├── prompt.py           # load_prompt() helper
    │   ├── tools.py            # Tools for the agents
    │   ├── super_agent/        # Orchestrator: routes to subagents
    │   │   ├── agent.py
    │   │   └── prompt.md
    │   ├── ideation_agent/     # Brainstorms angles & content
    │   │   ├── agent.py
    │   │   └── prompt.md
    │   ├── writing_agent/      # Writes the main body of the LinkedIn post
    │   │   ├── agent.py
    │   │   └── prompt.md
    │   └── refining_agent/     # Critiques & rewrites a draft
    │       ├── agent.py
    │       └── prompt.md
    └── utils/
        └── logger.py
```

## Architecture

![Architecture diagram](docs/linkforge_architecture.png)

## How it works

1. **Telegram → webhook**: User messages reach `POST /telegram/webhook`, validated by a shared secret header and an allowlisted user id (`telegram/auth.py`).
2. **Routing**: `.commands` (e.g. `.draft`, `.approve`) are handled directly for administrative actions; all other text is sent to the `SuperAgent`.
3. **Orchestration**: The `SuperAgent` routes requests to the right specialist subagent (ideation / writing / refining) exposed as tools, and persists full drafts via the `save_draft` tool.
4. **Persistence**: Drafts and approved posts live in SQLite; agent conversation memory uses `SQLiteSession` in the same DB.
5. **Models**: All agents run through LiteLLM, making model swaps configurable.
