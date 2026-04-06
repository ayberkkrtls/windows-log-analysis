# Event ID 7045: A New Service Was Installed

### Description

This event is recorded in the **System** event log whenever a new service is installed on a Windows system. Attackers commonly abuse Windows services for persistence, privilege escalation, or to execute malicious payloads that survive reboots.

### Key Fields to Monitor

| Field | Description |
| :--- | :--- |
| **ServiceName** | The name of the newly installed service. Attackers often use names that mimic legitimate Windows services (e.g., `WindowsUpdate`, `svchost32`). |
| **ImagePath** | The full path to the executable or command the service runs. This is the most critical field to inspect. |
| **ServiceType** | The type of service (e.g., Kernel Driver, Win32 OwnProcess). Malicious services are often `Win32OwnProcess`. |
| **StartType** | Indicates when the service starts (e.g., Auto Start, On Demand). Auto Start is commonly used for persistence. |
| **AccountName** | The account under which the service runs. `LocalSystem` or `SYSTEM` grants the highest privileges. |

### Attack Scenario: Persistence via Malicious Service

An attacker with Administrator privileges installs a new service named `WinDefendSvc` that actually runs a reverse shell executable located in `C:\Users\Public\shell.exe`. The service is set to start automatically, ensuring persistence across reboots.

- **Evidence:** A 7045 event where the **ImagePath** points to a non-standard location (e.g., `C:\Temp\`, `C:\Users\Public\`, or `%APPDATA%\`), or uses PowerShell/cmd commands.

### Detection Logic

* **Alert on:** Any service installed with an **ImagePath** containing `powershell`, `cmd.exe`, `mshta`, `wscript`, `cscript`, `rundll32`, `certutil`, or `bitsadmin`.
* **Alert on:** Services installed from non-standard directories (outside `C:\Windows\` and `C:\Program Files\`).
* **Alert on:** Services with names resembling legitimate Windows services but with slight variations (e.g., extra characters, numbers appended).
* **Baseline:** Maintain an inventory of known legitimate services and alert on any deviation.

### MITRE ATT&CK Mapping

- **Technique ID**: T1543.003 (Create or Modify System Process: Windows Service)
- **Tactic**: Persistence, Privilege Escalation
