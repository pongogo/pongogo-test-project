# Pongogo Test Project

**Purpose**: Isolated repository for Pongogo E2E testing infrastructure.

## ⚠️ IMPORTANT: Pull-Only Repository

This repository is **READ-ONLY** for automated systems:

- **No direct pushes** to `main` branch (branch protection enabled)
- **No force pushes** allowed
- **All changes** require PR with approval
- **CI/VM systems** have read-only access only

## Access Methods

### For CI/CD (GitHub Actions)
Uses `GITHUB_TOKEN` with default read permissions - no additional setup needed.

### For Azure VM (dev.pongogo.com)
Requires authentication credential stored in Azure Key Vault:

```bash
# Retrieve from Key Vault (VM must have Managed Identity with access)
az keyvault secret show --vault-name pongogo-kv --name "github-pat-test-repo" --query value -o tsv
```

**Key Vault**: `pongogo-kv` (pongogo-rg resource group)

**Required Secrets**:
| Secret Name | Purpose | Scope |
|-------------|---------|-------|
| `github-pat-test-repo` | Clone test repo | `repo:read` on `pongogo/pongogo-test-project` only |

### Creating the PAT (Admin Task)

1. Go to GitHub Settings → Developer Settings → Fine-grained tokens
2. Create token with:
   - **Name**: `pongogo-test-repo-readonly`
   - **Expiration**: 90 days (or as per policy)
   - **Repository access**: Only `pongogo/pongogo-test-project`
   - **Permissions**: Contents: Read-only
3. Store in Key Vault:
   ```bash
   az keyvault secret set --vault-name pongogo-kv --name "github-pat-test-repo" --value "github_pat_xxx"
   ```

## Project Structure

```
pongogo-test-project/
├── README.md           # This file
├── pyproject.toml      # Python project config
├── .gitignore          # Standard ignores
└── src/
    ├── __init__.py
    └── main.py         # Sample application
```

## Usage in E2E Tests

```bash
# Clone (read-only)
git clone https://github.com/pongogo/pongogo-test-project.git

# Run pongogo init
pongogo init

# Verify .pongogo/ created
ls -la .pongogo/
```

## Related Documentation

- **Parity Todo**: See `tmp/2026_01_19-parity_creation-todo.md` in main pongogo repo
- **PI-110**: Pull-only enforcement rationale
- **Key Vault**: `pongogo-kv` in Azure `pongogo-rg`
