# test-api-service

Platform API backend (FastAPI, PostgreSQL, JWT auth). Owner: Alice.

## Jurati — Team Knowledge

This project uses [Jurati](https://github.com/ostinato-forge/jurati) for cross-agent coordination.

**You MUST call `context()` before starting any task.** This surfaces active work, team decisions, and cross-repo dependencies that affect your work. Summarize what you learn in 2-3 sentences for the developer.

### Tool quick-reference

| Tool | When to use |
|------|-------------|
| `context()` | First thing, every task. Pass `repo` and `goal` for better results. |
| `query(topic=...)` | Deep-dive on a specific topic after context(). |
| `record(type, title, content)` | Capture active context others should know about (e.g., breaking changes, in-progress work). |
| `propose(type, title, content)` | Record a team decision or workflow that needs review. |
| `sync()` | Call silently before context() to get fresh data. |

### Rules

- **Never expose Jurati internals to the developer.** No entry IDs, ref paths, branch names, expiry dates, or lifecycle instructions. These are implementation details.
- **Never ask the developer to manage the knowledge repo.** Don't say "merge PR #X" or "run sync." Jurati handles its own lifecycle.
- **Confirm actions in one sentence.** After recording or proposing, say something like "Recorded your auth refactor context" — not a multi-paragraph explanation of L0/L1/L2 escalation.
- **State coordination plainly.** If someone's PR blocks this work, say so directly: "Wait for Alice's auth PR to merge before changing the token format."

### Sibling repos

- `ostinato-forge/test-api-service` — this repo (backend API)
- `ostinato-forge/test-web-frontend` — React frontend (depends on this API)
- `ostinato-forge/test-shared-libs` — shared error types and utilities
