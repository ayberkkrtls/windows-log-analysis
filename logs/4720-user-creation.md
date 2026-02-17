# Event ID 4720: A user account was created

### Description
This event is triggered every time a new local or domain user account is created. In a secure environment, account creation should be a scheduled and authorized administrative action.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| **TargetUserName** | The name of the newly created account. |
| **SubjectUserName** | The account that performed the creation (Who created the user?). |
| **Privileges** | Any specific administrative rights assigned during creation. |

### Attack Scenario: Persistence
An attacker compromises a server and creates a new user named "backup_svc" to blend in with legitimate service accounts. They then add this user to the "Administrators" group to maintain permanent access.
- **Evidence:** An unexpected 4720 event followed by a 4732 (A member was added to a security-enabled local group).

### Detection Logic
* **Alert on:** Any user creation performed by a non-standard administrative account.
* **Alert on:** User creation occurring at unusual times (e.g., 2:00 AM) or on sensitive systems like Domain Controllers.
* **Baseline:** Compare the `SubjectUserName` against a list of authorized IT personnel.
