# MCP Servers — Source

> Production deployment: [wildfirebill-ai/mcp-servers-prod](https://github.com/wildfirebill-ai/mcp-servers-prod)

100 local MCP (Model Context Protocol) servers for coding,
programming, and web development. Each runs on
`localhost:25000-25099` with SSE transport.

## Generation & Testing

| File | Purpose |
| --- | --- |
| `_generator.py` | Master generator |
| `_test_single.py` | Sequential test script |
| `_test_server.py` | Deprecated parallel test |

## Per-Server Structure

```text
server-name/
├── server.py          # MCP server (27 tools, memory, logging)
├── skills.md          # Unique skills for this server
├── Dockerfile         # python:3.12-alpine
├── docker-compose.yml # Port 25000-25099, bind mount ./data:/app/data
├── requirements.txt   # mcp, httpx, beautifulsoup4, etc.
├── start.bat          # Silent start — run hidden, no console window
├── stop.bat           # Kill by port
└── data/
    ├── memory.json    # Persistent key-value memory store
    └── server.log     # Rotating log (all tool calls logged)
```

## Root Files

| File | Purpose |
| --- | --- |
| `docker-compose.yml` | Single compose for all 100 |
| `start-all.bat` | Starts all 100 servers |
| `stop-all.bat` | Stops all 100 servers |
| `requirements.txt` | Shared dependencies |

## Running

```batch
start-all.bat          # Start all 100 servers
stop-all.bat           # Stop all 100 servers
```

Or individually per folder:

```batch
cd server-name && start.bat
cd server-name && stop.bat
```

## Security Warnings

- **`eval()` usage** — Some servers use `eval()` for dynamic code
  evaluation (e.g., `algorithm-master` evaluates expressions).
  This is intentional but presents a code injection risk.
  Do not expose to untrusted input. If content can be defined
  by external sources, a malicious actor could execute
  arbitrary code.
  See: <https://semgrep.dev/r?q=python.lang.security.audit.eval-detected.eval-detected>
- **`subprocess` with `shell=True`** — Several servers spawn shell
  commands using `subprocess` with `shell=True`. This propagates
  current shell settings and variables, making it easier for a
  malicious actor to execute commands. These servers are designed
  for ⚠️WARNING⚠️ **local development only** ⚠️WARNING⚠️.
  Do not expose to public networks. Use `shell=False` for any
  production-facing code.
  See: <https://semgrep.dev/r?q=python.lang.security.audit.subprocess-shell-true.subprocess-shell-true>

## Operational Warnings

- **Port range 25000-25099** — Ensure none are in use before
  starting. Run `stop-all.bat` first if previously started.
- **Race conditions** — Starting all 100 simultaneously can
  cause port conflicts. `start-all.bat` uses sequential startup.
- **Python 3.14+** — Requires Python 3.12+. The `mcp` package
  must be installed (`pip install mcp`).
- **Memory files** — Each server stores `data/memory.json`
  locally. Persistent across restarts. Delete to reset.
- **Log files** — `data/server.log` grows over time.
  Monitor disk usage if running long-term.
- **No authentication** — All tools exposed on localhost
  with no auth. Do not expose to public networks.
- **Deprecation warnings** — Some Python features may show
  deprecation warnings. Non-fatal. Use `-W ignore` to suppress.
- **The 27 tools include:** `ping`, `echo`, `server_info`,
  memory tools (`set_memory`, `get_memory`, `delete_memory`,
  `list_memory`, `clear_memory`, `memory_stats`), code tools,
  web tools, and domain-specific tools per server.
- **Docker** — Each server has a Dockerfile. Use
  `docker compose up -d` in any server folder.
  Root `docker-compose.yml` starts all 100.
- **Generator** — `_generator.py` can regenerate any server
  folder. Modify the template and re-run to update all.
- **Testing** — Use `python _test_single.py` to validate all
  100 servers sequentially. Confirms name, port, tools, ops.
