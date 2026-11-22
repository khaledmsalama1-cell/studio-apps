# studio-apps

The app registry for [Brand Content Studio](https://github.com/khaledmsalama1-cell/brand-content-studio): {{COUNT}} tools, services, skills and MCP connectors for making brand content with Claude.

The Studio scans this repo (**Apps → Sources → Refresh**) and lists everything here on its Apps page, where each app can be connected in one click.

## How it works

- One file per app in [`apps/`](apps), validated by [`scripts/build-index.mjs`](scripts/build-index.mjs) into [`index.json`](index.json), which is what the Studio reads.
- Each app declares one **integration** the Studio applies *without running any code*:

| Integration | What the Studio does |
|---|---|
| `mcp` | Adds an MCP connector to the project's `.mcp.json` (remote URL, or an `npx`/`uvx` package), with keys kept in `.env` |
| `skills-repo` | Copies every folder with a `SKILL.md` from a GitHub repo into `.claude/skills` |
| `keys` | Asks for API keys and stores them in `.env` |
| `folder` | Connects the app's export folder to the Library, so its files can be used in projects |
| `link` | Information and links only |

Commands that install software are **never** accepted from this registry; only the Studio's own local catalogue can define them.

## Add an app

1. Create `apps/<id>.json` (copy any existing file; fields are described in [`schema.json`](schema.json)).
2. Run `node scripts/build-index.mjs`. It fails on anything invalid.
3. Commit `apps/<id>.json`, `index.json` and `README.md`.

Facts change fast: check links, licenses and pricing on the vendor's site before relying on them.
