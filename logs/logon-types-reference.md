# Windows Logon Types Reference

### Description
Logon type numbers in Event ID 4624 and 4625 indicate how the user attempted to log on. Understanding these codes is essential for identifying the source of an access attempt.

### Logon Type Codes
| Type | Name | Description |
| :--- | :--- | :--- |
| 2 | Interactive | Logon at the local keyboard and monitor of the computer. |
| 3 | Network | Connection to a shared resource (folder, printer) from another computer. |
| 4 | Batch | Used by scheduled tasks or batch servers. |
| 5 | Service | Service started by the Service Control Manager. |
| 7 | Unlock | User unlocked the computer (e.g., after a screen saver). |
| 8 | NetworkCleartext | Logon using cleartext password (often over IIS). |
| 9 | NewCredentials | Used when a program runs with different credentials (e.g., RunAs). |
| 10 | RemoteInteractive | Remote Desktop Protocol (RDP) connection. |
| 11 | CachedInteractive | Logon with cached credentials (no connection to Domain Controller). |

### Security Implications
- **Type 3 vs Type 10:** Attackers moving laterally through a network often use Type 3 for SMB/PowerShell or Type 10 for RDP.
- **Type 8:** Highly suspicious as it indicates passwords being sent in plain text across the network.
