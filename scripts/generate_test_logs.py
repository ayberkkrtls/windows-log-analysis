#!/usr/bin/env python3
"""
generate_test_logs.py
======================

Synthetic Windows Security event log generator for the windows-log-analysis
repository. Produces JSON-Lines output that mimics the fields documented in
logs/*.md, so the Sigma rules in sigma-rules/ (or any custom detection logic)
can be smoke-tested without needing a real Windows host or EVTX file.

This is a learning/testing aid, not a forensics tool. Events are entirely
synthetic.

Usage
-----
    python3 generate_test_logs.py --scenario brute_force -o out.jsonl
    python3 generate_test_logs.py --scenario all -o out.jsonl
    python3 generate_test_logs.py --list

Scenarios
---------
    brute_force            4625 x N against one account, then a 4624 success
    account_enum           4625 with SubStatus 0xC0000064 (no such user)
    scheduled_task         4698 with a suspicious Command
    service_persistence    7045 with a suspicious ImagePath
    log_cleared             1102 anti-forensics event
    backdoor_account       4720 followed by 4732 (persistence via new admin)
    privilege_escalation   4672 for a non-admin account
    normal                 Benign 4624/4688 noise, for false-positive testing
    all                    Every scenario above, interleaved by timestamp
"""

import argparse
import json
import random
import uuid
from datetime import datetime, timedelta, timezone

SCENARIOS = [
    "brute_force",
    "account_enum",
    "scheduled_task",
    "service_persistence",
    "log_cleared",
    "backdoor_account",
    "privilege_escalation",
    "normal",
]

FAKE_IPS = ["203.0.113.{}".format(n) for n in range(2, 60)]
FAKE_HOSTS = ["WKSTN-{:03d}".format(n) for n in range(1, 30)]
FAKE_USERS = ["jsmith", "mkaya", "aozturk", "bwilson", "svc_backup", "svc_sql"]


def now_iso(offset_seconds=0):
    return (datetime.now(timezone.utc) + timedelta(seconds=offset_seconds)).isoformat()


def base_event(event_id, offset_seconds=0, **fields):
    evt = {
        "EventRecordID": str(uuid.uuid4()),
        "EventID": event_id,
        "TimeCreated": now_iso(offset_seconds),
    }
    evt.update(fields)
    return evt


def gen_brute_force(t0=0):
    events = []
    target = "Administrator"
    ip = random.choice(FAKE_IPS)
    for i in range(15):
        events.append(base_event(
            4625, t0 + i * 3,
            TargetUserName=target,
            IpAddress=ip,
            LogonType=3,
            Status="0xC000006D",
            SubStatus="0xC000006A",
        ))
    events.append(base_event(
        4624, t0 + 15 * 3 + 2,
        TargetUserName=target,
        IpAddress=ip,
        LogonType=3,
    ))
    return events


def gen_account_enum(t0=0):
    events = []
    ip = random.choice(FAKE_IPS)
    for i in range(8):
        events.append(base_event(
            4625, t0 + i * 5,
            TargetUserName="user{}".format(random.randint(1000, 9999)),
            IpAddress=ip,
            LogonType=3,
            Status="0xC000006D",
            SubStatus="0xC0000064",
        ))
    return events


def gen_scheduled_task(t0=0):
    return [base_event(
        4698, t0,
        TaskName="\\Microsoft\\Windows\\WindowsUpdate",
        Command="powershell.exe -enc SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQA",
        SubjectUserName=random.choice(FAKE_USERS),
        ClientProcessId=random.randint(1000, 9999),
    )]


def gen_service_persistence(t0=0):
    return [base_event(
        7045, t0,
        ServiceName="WinDefendSvc",
        ImagePath="C:\\Users\\Public\\shell.exe",
        ServiceType="Win32OwnProcess",
        StartType="Auto Start",
        AccountName="LocalSystem",
    )]


def gen_log_cleared(t0=0):
    return [base_event(
        1102, t0,
        SubjectUserName=random.choice(FAKE_USERS),
        SubjectDomainName="CORP",
    )]


def gen_backdoor_account(t0=0):
    target = "backup_svc"
    subject = random.choice(FAKE_USERS)
    return [
        base_event(4720, t0, TargetUserName=target, SubjectUserName=subject),
        base_event(4732, t0 + 45, TargetUserName=target, SubjectUserName=subject,
                    GroupName="Administrators"),
    ]


def gen_privilege_escalation(t0=0):
    return [base_event(
        4672, t0,
        SubjectUserName=random.choice(["jsmith", "mkaya", "aozturk"]),
        PrivilegeList="SeDebugPrivilege,SeTakeOwnershipPrivilege",
        LogonId="0x{:08x}".format(random.randint(1, 0xFFFFFFF)),
        WorkstationName=random.choice(FAKE_HOSTS),
    )]


def gen_normal(t0=0):
    events = []
    for i in range(5):
        events.append(base_event(
            4624, t0 + i * 60,
            TargetUserName=random.choice(FAKE_USERS),
            IpAddress="10.0.0.{}".format(random.randint(2, 250)),
            LogonType=2,
        ))
        events.append(base_event(
            4688, t0 + i * 60 + 5,
            NewProcessName="C:\\Windows\\System32\\notepad.exe",
            SubjectUserName=random.choice(FAKE_USERS),
        ))
    return events


GENERATORS = {
    "brute_force": gen_brute_force,
    "account_enum": gen_account_enum,
    "scheduled_task": gen_scheduled_task,
    "service_persistence": gen_service_persistence,
    "log_cleared": gen_log_cleared,
    "backdoor_account": gen_backdoor_account,
    "privilege_escalation": gen_privilege_escalation,
    "normal": gen_normal,
}


def build_events(scenario):
    if scenario == "all":
        events = []
        t = 0
        for name in SCENARIOS:
            events.extend(GENERATORS[name](t0=t))
            t += 300
        events.sort(key=lambda e: e["TimeCreated"])
        return events
    return GENERATORS[scenario]()


def main():
    parser = argparse.ArgumentParser(description="Generate synthetic Windows Security events for testing detection logic.")
    parser.add_argument("--scenario", "-s", choices=SCENARIOS + ["all"], default="all",
                         help="Which attack scenario to generate (default: all)")
    parser.add_argument("--output", "-o", default="test_logs.jsonl",
                         help="Output file path (JSON Lines format)")
    parser.add_argument("--list", action="store_true", help="List available scenarios and exit")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducible output")
    args = parser.parse_args()

    if args.list:
        print("Available scenarios:")
        for s in SCENARIOS:
            print("  -", s)
        print("  - all (default)")
        return

    if args.seed is not None:
        random.seed(args.seed)

    events = build_events(args.scenario)

    with open(args.output, "w", encoding="utf-8") as f:
        for evt in events:
            f.write(json.dumps(evt, ensure_ascii=False) + "\n")

    print(f"Wrote {len(events)} synthetic event(s) to {args.output} (scenario: {args.scenario})")


if __name__ == "__main__":
    main()
