# Sigma Rules

Machine-readable [Sigma](https://github.com/SigmaHQ/sigma) detection rules that
implement the "Detection Logic" sections documented in [`/logs`](../logs). Each
file maps 1:1 (or 1:many, for multi-rule detections) to a Windows Event Log
page in this repository.

| File | Event ID(s) | Doc |
| :--- | :--- | :--- |
| `4625_brute_force.yml` | 4625 | [4625-failed-logon.md](../logs/4625-failed-logon.md) |
| `4698_scheduled_task_persistence.yml` | 4698 | [4698-scheduled-task-created.md](../logs/4698-scheduled-task-created.md) |
| `7045_malicious_service_install.yml` | 7045 | [7045-service-installed.md](../logs/7045-service-installed.md) |
| `1102_audit_log_cleared.yml` | 1102 | [1102-audit-log-cleared.md](../logs/1102-audit-log-cleared.md) |
| `4720_suspicious_user_creation.yml` | 4720, 4732 | [4720-user-creation.md](../logs/4720-user-creation.md) |
| `4672_privilege_anomaly.yml` | 4672 | [4672-special-privileges.md](../logs/4672-special-privileges.md) |

## Usage

Convert to your SIEM's query language with [`sigma-cli`](https://github.com/SigmaHQ/sigma-cli)
(the modern `pysigma`-based converter):

\`\`\`bash
pip install sigma-cli
sigma convert -t splunk sigma-rules/4625_brute_force.yml
sigma convert -t elasticsearch-lucene sigma-rules/1102_audit_log_cleared.yml
\`\`\`

Rules that use `count() by ... > N` or `correlate(...)` require a backend/target
that supports Sigma's aggregation and correlation syntax (e.g. recent
`sigma-cli` + a correlation-capable backend, or manual translation into your
SIEM's own aggregation rules).

## Testing against synthetic data

Use `scripts/generate_test_logs.py` to produce matching sample events, then
validate your converted queries against that output before deploying to
production.

## Notes

- `4672_privilege_anomaly.yml` ships with a placeholder `admin_watchlist` —
  populate it with your environment's real privileged/service accounts before
  use, otherwise it will alert on every legitimate admin logon.
- All rules are `status: experimental` unless noted, meaning: tune thresholds
  and filters to your environment before enabling in production.
# Sigma Rules

Machine-readable [Sigma](https://github.com/SigmaHQ/sigma) detection rules that
implement the "Detection Logic" sections documented in [`/logs`](../logs). Each
file maps 1:1 (or 1:many, for multi-rule detections) to a Windows Event Log
page in this repository.

| File | Event ID(s) | Doc |
| :--- | :--- | :--- |
| `4625_brute_force.yml` | 4625 | [4625-failed-logon.md](../logs/4625-failed-logon.md) |
| `4698_scheduled_task_persistence.yml` | 4698 | [4698-scheduled-task-created.md](../logs/4698-scheduled-task-created.md) |
| `7045_malicious_service_install.yml` | 7045 | [7045-service-installed.md](../logs/7045-service-installed.md) |
| `1102_audit_log_cleared.yml` | 1102 | [1102-audit-log-cleared.md](../logs/1102-audit-log-cleared.md) |
| `4720_suspicious_user_creation.yml` | 4720, 4732 | [4720-user-creation.md](../logs/4720-user-creation.md) |
| `4672_privilege_anomaly.yml` | 4672 | [4672-special-privileges.md](../logs/4672-special-privileges.md) |

## Usage

Convert to your SIEM's query language with [`sigma-cli`](https://github.com/SigmaHQ/sigma-cli)
(the modern `pysigma`-based converter):

```bash
pip install sigma-cli
sigma convert -t splunk sigma-rules/4625_brute_force.yml
sigma convert -t elasticsearch-lucene sigma-rules/1102_audit_log_cleared.yml
```

Rules that use `count() by ... > N` or `correlate(...)` require a backend/target
that supports Sigma's aggregation and correlation syntax (e.g. recent
`sigma-cli` + a correlation-capable backend, or manual translation into your
SIEM's own aggregation rules).

## Testing against synthetic data

Use `scripts/generate_test_logs.py` to produce matching sample events, then
validate your converted queries against that output before deploying to
production.

## Notes

- `4672_privilege_anomaly.yml` ships with a placeholder `admin_watchlist` —
  populate it with your environment's real privileged/service accounts before
  use, otherwise it will alert on every legitimate admin logon.
- All rules are `status: experimental` unless noted, meaning: tune thresholds
  and filters to your environment before enabling in production.
