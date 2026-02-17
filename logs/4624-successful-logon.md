# Event ID 4624: An account was successfully logged on

### Description
This event is generated when a logon session is created. It is recorded on the target computer that was accessed.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| Logon Type | Specifies how the user logged on (Local, Network, RDP). |
| TargetUserName | The name of the user who logged on. |
| IpAddress | The source IP address of the logon attempt. |
| Logon ID | A unique ID used to correlate this logon with other events. |

### Common Logon Types
* Type 2 (Interactive): Physical logon (keyboard/monitor).
* Type 3 (Network): Accessing a shared folder or printer.
* Type 10 (RemoteInteractive): Remote Desktop Protocol (RDP).

### Attack Scenario: Lateral Movement
An attacker steals credentials and uses them to move from a compromised workstation to a server via RDP.
* Evidence: A Logon Type 10 event with a suspicious source IpAddress and an administrative TargetUserName.

### Detection Logic
* Alert on: Any Logon Type 10 (RDP) attempts outside of business hours.
* Alert on: Multiple successful logons from the same IP address using different usernames within a short timeframe.
