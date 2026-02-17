# Event ID 4688: A new process has been created

### Description
This event documents every time a process starts. This is one of the most important events for detecting malicious activity, as it reveals which programs or commands were executed on the system.

### Key Fields to Monitor
| Field | Description |
| :--- | :--- |
| **New Process Name** | The full path of the executable that was started (e.g., C:\Windows\System32\whoami.exe). |
| **Process Command Line** | The exact command and arguments used (e.g., net user /add). *Requires extra configuration to enable.* |
| **Creator Process Name** | The program that started the new process (e.g., cmd.exe starting powershell.exe). |
| **TargetUserName** | The account context under which the process is running. |

### Attack Scenario: Discovery & Persistence
An attacker gains access and wants to see who they are and what privileges they have.
- **Evidence:** Multiple 4688 events in seconds showing commands like `whoami.exe`, `net user`, `hostname.exe`, or `ipconfig.exe` being executed by a non-admin user.

### Detection Logic
* **Alert on:** Execution of known "living off the land" binaries (Lolbins) like `certutil.exe` downloading files or `powershell.exe` with encoded commands.
* **Alert on:** Suspicious parent-child relationships, such as `outlook.exe` starting `cmd.exe` or `wscript.exe`.
* **Alert on:** Any process execution from temporary folders (e.g., `C:\Users\...\AppData\Local\Temp\`).
