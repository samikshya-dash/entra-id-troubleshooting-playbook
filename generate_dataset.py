"""Rebuild the synthetic sign-in failure sample (seeded, so the output is reproducible).

Nothing here is real tenant data. The AADSTS codes are real; users, apps and volumes are invented.
Run:  python tools/generate_dataset.py
"""
import csv, random
from datetime import datetime, timedelta
from pathlib import Path

random.seed(42)
ROOT = Path(__file__).resolve().parent.parent


def signin_failures():
    """30 days of failed sign-ins for the troubleshooting playbook (codes are real AADSTS codes; rows are invented)."""
    codes = [  # code, short name, playbook scenario, weight
        ("50126", "Invalid username or password", "1 Sign-in fails", 0.27),
        ("50053", "Account locked (smart lockout)", "5 Lockout loop", 0.09),
        ("50055", "Password expired", "1 Sign-in fails", 0.04),
        ("50057", "Account disabled", "1 Sign-in fails", 0.03),
        ("500121", "MFA challenge failed", "2 MFA problems", 0.12),
        ("50074", "MFA required, not completed", "2 MFA problems", 0.08),
        ("53003", "Blocked by Conditional Access", "3 Conditional Access", 0.11),
        ("53000", "Device not compliant", "15 Compliance and PRT", 0.06),
        ("50105", "User not assigned to app", "9 Assignment and consent", 0.05),
        ("70043", "Sign-in frequency expired", "6 Repeated prompts", 0.05),
        ("7000222", "Client secret expired", "7 App authentication", 0.03),
        ("50011", "Reply URL mismatch", "7 App authentication", 0.02),
        ("65001", "Consent not granted", "9 Assignment and consent", 0.02),
        ("90072", "Guest account not in tenant", "22 Guest access", 0.02),
        ("50158", "External MFA challenge not met", "2 MFA problems", 0.01),
    ]
    apps = ["Office 365 Exchange Online", "Microsoft Teams", "SharePoint Online", "HR Portal", "Service Desk", "VPN", "Azure Portal", "CRM", "Payroll"]
    rows, start = [], datetime(2026, 8, 1)
    for i in range(6000):
        c = random.choices(codes, [w for *_, w in codes])[0]
        t = start + timedelta(minutes=random.randint(0, 60 * 24 * 30))
        if c[0] == "7000222":  # a secret expired on the 18th: a burst from one app
            t = datetime(2026, 8, 18, 6) + timedelta(minutes=random.randint(0, 600))
        rows.append({"time": t.isoformat(timespec="minutes"), "user": f"u{random.randint(1000, 4999)}@contoso.example",
                     "app": "Payroll" if c[0] == "7000222" else random.choice(apps), "result_type": c[0], "result_description": c[1],
                     "playbook_scenario": c[2],
                     "client_app": random.choices(["Browser", "Mobile Apps and Desktop clients", "Exchange ActiveSync", "IMAP4"], [0.5, 0.42, 0.05, 0.03])[0],
                     "country": random.choices(["IN", "US", "GB", "DE", "SG"], [0.55, 0.2, 0.12, 0.08, 0.05])[0]})
    rows.sort(key=lambda r: r["time"])
    p = ROOT / "data/signin_failures_sample.csv"
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)



if __name__ == "__main__":
    signin_failures()
    print("Synthetic dataset written.")
