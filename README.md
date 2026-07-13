# KittyOSINT

Graphical OSINT interface for [KittySploit](https://github.com/SIA-IOTechnology) — visualize and chain reconnaissance modules on an interactive graph.

KittyOSINT automatically loads auxiliary modules from the **OSINT** group (`auxiliary/osint/`), runs transforms against your target, and aggregates results as nodes and edges (vis.js).

## Features

- **Interactive graph** — map entities (domains, IPs, emails, secrets, exposures, etc.) with category grouping, pivots, and view modes
- **Module catalog** — list filtered by the entered target, with compatibility hints (domain, IP, URL, email, file, keyword)
- **REST API** — discover modules and run transforms from the UI or external integrations
- **CLI mode** — run all compatible modules sequentially on a target, without a web UI
- **KittySploit integration** — shared charter, encryption, and database with the framework

## Prerequisites

- [KittySploit](https://github.com/SIA-IOTechnology) **≥ 1.0.0** (≤ 3.0.0)
- OSINT modules installed under `modules/auxiliary/osint/`
- Python dependencies allowed by the extension: `flask`, `flask_cors`, `requests`

## Installation

From the KittySploit console:

```bash
kittysploit> market install kittyosint
```

Local install (development):

```bash
kittysploit> market install /path/to/KittyOsint
```

The extension type is **UI**; the entry point is `main.py` (defined in `extension.toml`).

## Usage

### Web UI (default)

After installation, launch the extension from the marketplace or directly:

```bash
python main.py
```

The UI is served at **http://127.0.0.1:8001** by default.

Available options:

| Option | Description | Default |
|--------|-------------|---------|
| `--host` / `--api-host` | Bind address | `127.0.0.1` |
| `--port` / `--api-port` | HTTP port | `8001` |

Examples:

```bash
python main.py --port 8003
python main.py --host 0.0.0.0 --port 8003
```

On first startup, KittySploit may prompt for charter acceptance and encryption setup (sensitive data in the database).

### CLI mode

Run all compatible OSINT modules on a target without opening a browser:

```bash
python main.py example.com
python main.py user@domain.tld
python main.py https://target.example/
```

### API

| Method | Route | Description |
|--------|-------|-------------|
| `GET` | `/` | Graphical interface |
| `GET` | `/api/modules?target=…` | Module list (optional compatibility for the given target) |
| `POST` | `/api/transform` | Run a module — JSON body: `{ "module": "<id>", "target": "<target>" }` |

Typical transform response: `raw`, `graph` (`nodes`, `edges`), `meta` (timestamp, supported target types, etc.).

## Target types

KittyOSINT auto-detects the target type and adjusts the module list:

| Type | Examples |
|------|----------|
| `domain` | `example.com` |
| `ip` | `203.0.113.10` |
| `url` | `https://example.com/page` |
| `email` | `contact@example.com` |
| `file` | path to an existing local file |
| `keyword` | other free-text input |

Incompatible modules are flagged in the UI and skipped in CLI mode (`skipped` + reason).

## Project structure

```
KittyOsint/
├── extension.toml          # KittySploit marketplace metadata
├── src/
│   ├── main.py             # Extension entry point (paths + delegation)
│   └── kittyosint/
│       ├── __init__.py     # Flask app, CLI, framework init
│       ├── core.py         # Module loading, compatibility, execution
│       ├── _paths.py       # Shared static paths
│       ├── templates/      # HTML UI
│       └── static/         # Graph logic (vis.js)
└── LICENSE
```

## Development

1. Clone the repo and install locally with `market install ./KittyOsint`
2. Ensure the KittySploit framework and `auxiliary/osint/` modules are available
3. Run `python main.py` and open the URL printed in the terminal

Network and database permissions are declared in `extension.toml` (`network_access`, `database_access`).

## License

MIT — see [LICENSE](LICENSE).

Copyright © 2026 [IOTechnology](https://github.com/SIA-IOTechnology).
