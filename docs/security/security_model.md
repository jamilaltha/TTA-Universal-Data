# D10Z Security Model

## Risks
- Supply chain vulnerabilities in dependencies.
- Data leakage from misconfigured notebooks.
- Credential exposure in automation pipelines.

## Attack Surface
- Python package dependencies.
- Notebook execution environments.
- CI/CD workflows.

## Controls
- Scheduled vulnerability scans (trivy, bandit, pip-audit).
- Dependency reporting and review.
- Manual review of notebook outputs prior to publication.
