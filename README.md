# Pongogo Test Project

**Purpose**: Sample project for Pongogo E2E testing.

## Important

> **This repository is PULL-ONLY**
>
> - No direct pushes allowed
> - No force pushes allowed
> - Branch protection enforced on main
> - Deploy keys are read-only

## What This Repo Is For

This repository provides a minimal project structure that Pongogo's test harness can:

1. Clone (read-only)
2. Run `pongogo init` against
3. Test MCP server functionality
4. Validate routing, database operations, etc.

## Structure

```
pongogo-test-project/
├── README.md           # This file
├── pyproject.toml      # Python project config
├── src/
│   └── main.py         # Sample Python module
└── .gitignore
```

## Usage in Tests

```bash
# Clone (read-only)
git clone --depth 1 git@github.com:pongogo/pongogo-test-project.git project
cd project

# Initialize Pongogo
pongogo init

# Run tests against .pongogo/ directory
python -m tests.mcp_client --test-all --container pongogo-test-server
```

## Maintainers

This repo is maintained by the Pongogo team for CI/CD and development testing only.
