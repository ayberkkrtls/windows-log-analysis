# Scenario: Detecting Lateral Movement via RDP

### Description

This scenario covers the detection of lateral movement attacks where an adversary uses the Remote Desktop Protocol (RDP) to move through a network after gaining an initial foothold. RDP (port 3389) is a legitimate Windows feature that is frequently abused by attackers to pivot to high-value targets.

### Related Event IDs

- **4624**: Successful Logon (LogonType **10** = RemoteInteractive — the key indicator for RDP)
- **4625**: Failed Logon (LogonType 10 = failed RDP attempts)
- **4672**: Special Privileges Assigned (indicates the RDP session was opened with admin rights)
- **4688**: Process Creation (suspicious processes spawned within the RDP session)
- **7045**: New Service Installed (attacker may install tools during the RDP session)

### Detection Logic

An alert should be raised when the following chain of events is observed:

1. One or more **4625** events with **LogonType 10** from the same source IP against an internal machine (indicates failed RDP attempts).
2. Followed by a **4624** event with **LogonType 10** from the same source IP (successful RDP logon).
3. The **source IP** is another internal workstation — not a dedicated jump server or admin machine.
4. The **TargetUserName** is a high-privilege account (e.g., Administrator, Domain Admin).

### Important Fields for Analysis

| Field | Description |
| :--- | :--- |
| **LogonType** | Must be **10** (RemoteInteractive) to confirm RDP usage. |
| **IpAddress** | The source machine initiating the RDP connection. Cross-reference with your asset inventory. |
| **TargetUserName** | The account being used for the RDP session. High-privilege accounts are high risk. |
| **WorkstationName** | The hostname of the connecting machine. |
| **SubjectUserName** | The account that initiated the logon request. |

### Attack Scenario: Pivoting via Stolen Credentials

An attacker compromises `WORKSTATION-01` and discovers domain admin credentials in memory using a credential dumping tool. They then open an RDP session from `WORKSTATION-01` to `DC-01` (the Domain Controller) using those credentials.

- **Step 1:** Attacker runs credential dumper on `WORKSTATION-01` → Event **4688** (suspicious process like `mimikatz.exe` or `lsass` access)
- **Step 2:** RDP connection initiated from `WORKSTATION-01` to `DC-01` → Event **4624** (LogonType 10) on `DC-01`
- **Step 3:** Admin-level access granted → Event **4672** on `DC-01`
- **Step 4:** Attacker installs a backdoor service → Event **7045** on `DC-01`

### MITRE ATT&CK Mapping

| Technique | ID | Tactic |
| :--- | :--- | :--- |
| Remote Desktop Protocol | T1021.001 | Lateral Movement |
| Valid Accounts | T1078 | Defense Evasion, Persistence |
| OS Credential Dumping | T1003 | Credential Access |

### False Positive Considerations

- **IT administrators** legitimately use RDP for remote management. Baseline normal admin RDP sources (e.g., dedicated jump servers).
- **Help desk staff** may RDP into user machines for support. Whitelist known help desk source IPs.
- **Automated backup or monitoring tools** may authenticate via RDP-like sessions. Verify `WorkstationName` against known tool servers.
