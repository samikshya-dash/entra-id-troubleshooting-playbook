"""Turn a sign-in log export into a triage list: which failures are biggest, and which playbook page fixes them.

Works on the synthetic sample by default, or on your own export of the Entra sign-in logs
(CSV with at least: time, result_type, app).

    python triage.py                     # synthetic data, redraws docs/*.svg
    python triage.py my_signin_export.csv
"""
import csv, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import svgchart as sc  # noqa: E402

# AADSTS code -> (plain-English meaning, playbook page, scenario number)
PLAYBOOK = {
    "50126": ("Invalid username or password", "01-sign-in.md", 1), "50034": ("User not found in this tenant", "01-sign-in.md", 1),
    "50055": ("Password expired", "01-sign-in.md", 1), "50057": ("Account disabled", "01-sign-in.md", 1),
    "50074": ("MFA required, not completed", "01-sign-in.md", 2), "50076": ("MFA required by policy change", "01-sign-in.md", 2),
    "500121": ("MFA challenge failed", "01-sign-in.md", 2), "50158": ("External MFA challenge not met", "01-sign-in.md", 2),
    "53003": ("Blocked by Conditional Access", "01-sign-in.md", 3), "530032": ("Blocked by security policy", "01-sign-in.md", 3),
    "50053": ("Account locked (smart lockout)", "01-sign-in.md", 5),
    "70043": ("Sign-in frequency expired", "01-sign-in.md", 6), "50133": ("Session revoked by password change", "01-sign-in.md", 6),
    "50173": ("Grant revoked", "01-sign-in.md", 6), "700082": ("Refresh token expired (inactivity)", "01-sign-in.md", 6),
    "700016": ("Application not found in tenant", "02-applications.md", 7), "7000215": ("Invalid client secret", "02-applications.md", 7),
    "7000222": ("Client secret expired", "02-applications.md", 7), "50011": ("Reply URL mismatch", "02-applications.md", 7),
    "75011": ("SAML authentication method mismatch", "02-applications.md", 8), "50008": ("SAML assertion missing or invalid", "02-applications.md", 8),
    "50105": ("User not assigned to app", "02-applications.md", 9), "65001": ("Consent not granted", "02-applications.md", 9),
    "90094": ("Admin consent required", "02-applications.md", 9),
    "53000": ("Device not compliant", "04-devices.md", 15), "53001": ("Device not domain joined", "04-devices.md", 15),
    "90072": ("Guest account not in tenant", "06-risk-guests-platform.md", 22), "500213": ("Blocked by cross-tenant access policy", "06-risk-guests-platform.md", 22),
}
SPIKE_FACTOR = 3  # an app whose failures on one day are 3x its daily average gets flagged


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else HERE / "data/signin_failures_sample.csv"
    rows = list(csv.DictReader(path.open()))
    by_code = Counter(r["result_type"] for r in rows).most_common()
    print(f"{len(rows):,} failed sign-ins in {path.name}\n")
    print(f"{'Code':>8}  {'Count':>6}  {'Share':>6}  Meaning -> playbook")
    for code, n in by_code:
        meaning, page, num = PLAYBOOK.get(code, ("Not in playbook yet", "error-codes.md", "-"))
        print(f"{code:>8}  {n:>6,}  {n/len(rows):>6.1%}  {meaning} -> scenarios/{page} (scenario {num})")

    # spike detection: one app suddenly failing with one code usually means a config change or an expired secret
    per_day = defaultdict(Counter)
    for r in rows:
        per_day[(r["app"], r["result_type"])][r["time"][:10]] += 1
    days = sorted({r["time"][:10] for r in rows})
    print("\nSpikes worth a look:")
    for (app, code), c in per_day.items():
        avg = sum(c.values()) / len(days)
        day, peak = c.most_common(1)[0]
        if peak >= 20 and peak > SPIKE_FACTOR * avg:
            print(f"  {day}  {app}: {peak} x AADSTS{code} ({PLAYBOOK.get(code, ('?',))[0]}), daily average {avg:.0f}")

    top = by_code[:10]
    sc.hbars(str(HERE / "docs/top_failure_codes.svg"), "Top sign-in failure codes",
             f"{len(rows):,} failed sign-ins over {len(days)} days (synthetic sample). Each code maps to a playbook scenario",
             [f"{c} · {PLAYBOOK.get(c, ('?',))[0]}" for c, _ in top], [n for _, n in top], w=900, label_w=300)
    daily = Counter(r["time"][:10] for r in rows)
    vals = [daily[d] for d in days]
    med = sorted(vals)[len(vals) // 2]
    sc.bars(str(HERE / "docs/failures_per_day.svg"), "Failed sign-ins per day",
            "Synthetic sample. The orange day is a client secret that expired on one app: scenario 7",
            [d[8:] if i % 2 == 0 else "" for i, d in enumerate(days)], vals,
            [sc.ORANGE if v > 1.25 * med else sc.BLUE for v in vals], annotate=False, w=900, h=320)


if __name__ == "__main__":
    main()
