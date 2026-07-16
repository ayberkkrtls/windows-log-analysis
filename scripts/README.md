# Scripts

## `generate_test_logs.py`

A dependency-free (stdlib-only) Python 3 script that generates synthetic
Windows Security event logs in JSON Lines format, mirroring the fields
used throughout `/logs`. Use it to sanity-check the Sigma rules in
`/sigma-rules` — or your own detections — without needing a real Windows
host, EVTX file, or lab environment.

### Usage

```bash
# List available attack scenarios
python3 generate_test_logs.py --list

# Generate a single scenario
python3 generate_test_logs.py --scenario brute_force -o brute_force.jsonl

# Generate every scenario, interleaved by timestamp
python3 generate_test_logs.py --scenario all -o all_events.jsonl

# Reproducible output (fixed seed)
python3 generate_test_logs.py --scenario all --seed 42 -o all_events.jsonl
```

### Scenarios

| Scenario | Simulates | Corresponding doc |
| :--- | :--- | :--- |
| `brute_force` | 15x failed logons + 1 success, same IP | [4625](../logs/4625-failed-logon.md) |
| `account_enum` | Failed logons against non-existent accounts | [4625](../logs/4625-failed-logon.md) |
| `scheduled_task` | Scheduled task with encoded PowerShell command | [4698](../logs/4698-scheduled-task-created.md) |
| `service_persistence` | Service installed from `C:\Users\Public\` | [7045](../logs/7045-service-installed.md) |
| `log_cleared` | Security log cleared | [1102](../logs/1102-audit-log-cleared.md) |
| `backdoor_account` | New user immediately added to Administrators | [4720](../logs/4720-user-creation.md) |
| `privilege_escalation` | Non-admin account gets special privileges | [4672](../logs/4672-special-privileges.md) |
| `normal` | Benign logons/process creation (false-positive baseline) | — |
| `all` | All of the above, interleaved | — |

### Output format

One JSON object per line, e.g.:

```json
{"EventRecordID": "…", "EventID": 4625, "TimeCreated": "2026-07-16T12:00:00+00:00", "TargetUserName": "Administrator", "IpAddress": "203.0.113.14", "LogonType": 3, "Status": "0xC000006D", "SubStatus": "0xC000006A"}
```

Field names intentionally match the "Key Fields to Monitor" tables in each
`/logs/*.md` page, so the output can be fed into a SIEM ingest pipeline,
a Sigma backend test harness, or just eyeballed directly.

All events and IP addresses are synthetic (`203.0.113.0/24` — TEST-NET-3,
reserved for documentation). This is a training/testing aid only; it does
not simulate real EVTX binary structure.
