# test-api-service

Platform API backend (FastAPI, PostgreSQL, JWT auth). Owner: Alice.

## Jurati — Team Knowledge

This project uses **Jurati** for shared team intelligence. The jurati MCP server is configured in `.mcp.json`.

**Before starting any task**, call `context()` to get:
- Team decisions and principles relevant to your work
- Cross-repo coordination signals (open PRs with the `jurati` label)
- Active context from other developers/agents

Key tools:
- `context()` — what the team knows about your current area of work, plus coordination signals
- `query(topic="...")` — search for specific knowledge entries
- `record()` — share active context (design decisions, blockers, status) with other agents
- `search(query="...")` — full-text search across all knowledge entries
- `sync()` — pull latest changes from the knowledge repo

This repo is part of a multi-repo system:
- `ostinato-forge/test-api-service` — this repo (backend API)
- `ostinato-forge/test-web-frontend` — React frontend (depends on this API)
- `ostinato-forge/test-shared-libs` — shared error types and utilities
