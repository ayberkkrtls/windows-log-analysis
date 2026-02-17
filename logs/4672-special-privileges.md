# Event ID 4672: Special privileges assigned to new logon

### Description
This event is generated when a user logs on with administrative or "special" privileges. It allows security analysts to see whenever a powerful account (like an Administrator) accesses the system.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| SubjectUserName | The account that logged on with special privileges. |
| PrivilegeList | The specific list of administrative rights assigned to the session (e.g., SeDebugPrivilege, SeTakeOwnershipPrivilege). |
| Logon ID | The ID used to link this event to the corresponding 4624 (Successful Logon) event. |

### Attack Scenario: Privilege Escalation
A standard user account is compromised, and the attacker uses an exploit to gain administrative rights.
* Evidence: A 4672 event triggered by a user account that normally does not have administrative duties, especially if it occurs immediately after suspicious process executions (4688).

### Detection Logic
* Alert on: Any 4672 event associated with a non-admin service account or a standard employee account.
* Alert on: Frequent 4672 events from a single workstation within a short period, which may indicate automated credential testing.
* Correlation: Always link this event with Event ID 4624 using the Logon ID to identify the source IP and logon type.
