# Windows Log Analysis Mastery

This repository is dedicated to mastering Windows Event Logs, which are crucial for SOC Analysis, Incident Response, and Threat Hunting.

## Objective
To understand the footprints (Event IDs) left by attackers on a system and develop effective detection logic to identify malicious activities.

## Roadmap
### Phase 1: Foundation (Completed)
- [x] **4624**: Successful Logon
- [x] **4625**: Failed Logon
- [x] **4688**: Process Creation
- [x] **4720**: User Account Creation
- [x] **4672**: Administrative Logon
- [x] **Logon Types** Reference Guide
- [x] **Scenario**: Brute Force Detection Logic

### Phase 2: Persistence & Evasion (In Progress)
- [ ] **4698**: A scheduled task was created (Persistence)
- [ ] **7045**: A new service was installed in the system (Persistence)
- [ ] **1102**: The audit log was cleared (Anti-Forensics/Evasion)
- [ ] **Scenario**: Detecting Lateral Movement via RDP
