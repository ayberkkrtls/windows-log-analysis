# Event ID 4625: An account failed to log on

### Description
This event is generated when a logon request fails. It is recorded on the computer where the logon attempt was made. It is the primary indicator of brute-force or password-guessing attacks.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| Failure Reason | A text explanation of why the logon failed. |
| Status / Sub-Status | Hexadecimal codes providing the exact reason (e.g., 0xC000006A for wrong password). |
| Logon Type | The method used for the attempt (e.g., Type 3 for Network, Type 10 for RDP). |
| TargetUserName | The account name that the attacker tried to access. |
| IpAddress | The source IP address of the failed attempt. |

### Critical Status Codes
- 0xC000006A: User name is correct but the password is wrong.
- 0xC0000064: User name does not exist. (Indicates account discovery)
- 0xC0000234: The user account is currently locked out.

### Attack Scenario: Brute Force
An attacker uses an automated script to try thousands of passwords against the "Administrator" account.
- Evidence: Hundreds of 4625 events from the same source IP within a very short timeframe.

### Detection Logic
* Alert on: More than 10 failed logon attempts for a single account within 60 seconds.
* Alert on: Failed logon attempts using a non-existent or disabled account name.
* Correlation: Monitor for multiple 4625 events followed by a single 4624 (Success) from the same IP.
