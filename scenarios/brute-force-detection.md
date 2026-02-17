# Scenario: Windows Brute Force Attack

### Description
This scenario covers the detection of brute-force attacks, where an actor attempts to gain access to a system by repeatedly guessing passwords for one or more user accounts.

### Related Event IDs
- **4625**: Failed logon (Multiple occurrences)
- **4624**: Successful logon (Indicating the attack succeeded)

### Detection Logic
An alert should be raised if:
- 5 or more failed logon attempts (4625) occur within a 5-minute window for the same user.
- **AND** a successful logon (4624) follows from the same Source IP and for the same Target User.

### Important Fields for Analysis
- **TargetUserName**: To identify the targeted account.
- **IpAddress**: To identify the source of the attack.
- **LogonType**: To distinguish between local and remote (network) attempts.
- **FailureReason**: To understand if the account is disabled or if the password was simply wrong.

### MITRE ATT&CK Mapping
- **ID**: T1110 (Brute Force)
- **Tactic**: Credential Access

### False Positive Considerations
- **Service accounts**: Automated accounts with expired passwords can trigger high volumes of 4625 events.
- **Password expiration**: Users who have not updated their saved credentials on multiple devices after a password change.
