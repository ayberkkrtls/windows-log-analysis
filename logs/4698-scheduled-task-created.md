# Event ID 4698: A scheduled task was created

### Description
This event is triggered whenever a new task is scheduled using the Windows Task Scheduler. Attackers frequently use this for persistence to ensure their malicious code runs automatically.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| **Task Name** | The name given to the scheduled task. |
| **Command** | The full path of the executable or script that the task runs. |
| **SubjectUserName** | The account that created the task. |
| **Client Process ID** | Can be used to identify which program (e.g., cmd.exe, powershell.exe) created the task. |

### Attack Scenario: Persistence via Task Scheduler
An attacker uses a compromised account to schedule a task named "WindowsUpdate" that actually executes a reverse shell script every day at 12:00 PM.
- **Evidence:** A 4698 event where the **Command** points to a suspicious location (e.g., `C:\Users\Public\`) or uses encoded PowerShell commands.

### Detection Logic
* **Alert on:** Any scheduled task created by a non-administrative user.
* **Alert on:** Tasks where the command line contains suspicious keywords like `powershell -enc`, `temp`, `bitsadmin`, or `certutil`.
* **Baseline:** Compare new tasks against a list of known legitimate system tasks.
