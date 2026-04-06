# 🪟 Windows Log Analysis Mastery

<p align="center">
  <img src="https://img.shields.io/badge/Focus-SOC%20Analysis-blue?style=for-the-badge&logo=windows" />
  <img src="https://img.shields.io/badge/Focus-Threat%20Hunting-red?style=for-the-badge&logo=target" />
  <img src="https://img.shields.io/badge/Focus-Incident%20Response-orange?style=for-the-badge&logo=firefoxbrowser" />
  <img src="https://img.shields.io/badge/MITRE-ATT%26CK%20Mapped-purple?style=for-the-badge" />
</p>

A hands-on study repository for mastering **Windows Event Logs** — the cornerstone of SOC Analysis, Incident Response, and Threat Hunting. Each entry documents real attacker footprints, detection logic, and MITRE ATT&CK mappings.

---

## 🎯 Objective

> Understand the **footprints (Event IDs)** left by attackers on a Windows system and develop effective detection logic to identify malicious activities before they cause damage.

---

## 📁 Repository Structure

```
windows-log-analysis/
├── logs/               # Event ID documentation (description, fields, detection logic)
└── scenarios/          # End-to-end attack scenarios with detection chains
```

---

## 🗺️ Roadmap

### ✅ Phase 1: Foundation (Completed)

| Event ID | Description | Documentation |
| :---: | :--- | :---: |
| **4624** | Successful Logon | [📄 View](logs/4624-successful-logon.md) |
| **4625** | Failed Logon | [📄 View](logs/4625-failed-logon.md) |
| **4688** | Process Creation | [📄 View](logs/4688-process-creation.md) |
| **4720** | User Account Creation | [📄 View](logs/4720-user-creation.md) |
| **4672** | Administrative Logon (Special Privileges) | [📄 View](logs/4672-special-privileges.md) |
| **—** | Logon Types Reference Guide | [📄 View](logs/logon-types-reference.md) |
| **Scenario** | Brute Force Detection Logic | [📄 View](scenarios/brute-force-detection.md) |

---

### ✅ Phase 2: Persistence & Evasion (Completed)

| Event ID | Description | Documentation |
| :---: | :--- | :---: |
| **4698** | A scheduled task was created (Persistence) | [📄 View](logs/4698-scheduled-task-created.md) |
| **7045** | A new service was installed (Persistence) | [📄 View](logs/7045-service-installed.md) |
| **1102** | The audit log was cleared (Anti-Forensics) | [📄 View](logs/1102-audit-log-cleared.md) |
| **Scenario** | Detecting Lateral Movement via RDP | [📄 View](scenarios/lateral-movement-rdp.md) |

---

### 🔲 Phase 3: Privilege Escalation & Credential Access (Planned)

| Event ID | Description |
| :---: | :--- |
| **4670** | Permissions on an object were changed |
| **4732** | A member was added to a security-enabled local group |
| **4768** | A Kerberos authentication ticket (TGT) was requested |
| **4769** | A Kerberos service ticket was requested |
| **4776** | The domain controller attempted to validate credentials (NTLM) |
| **Scenario** | Pass-the-Hash / Pass-the-Ticket Attack Detection |

---

## 🧠 Key Concepts

| Concept | Why It Matters |
| :--- | :--- |
| **LogonType** | Distinguishes interactive, network, and remote logon sessions |
| **MITRE ATT&CK** | Maps event IDs to real-world adversary techniques and tactics |
| **Detection Logic** | Translates log patterns into actionable SOC alerts |
| **False Positives** | Understanding benign triggers is essential for reducing alert fatigue |

---

## 📚 Resources

- [Microsoft Event ID Reference](https://docs.microsoft.com/en-us/windows/security/threat-protection/auditing/security-auditing-overview)
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [Sigma Rules](https://github.com/SigmaHQ/sigma)
