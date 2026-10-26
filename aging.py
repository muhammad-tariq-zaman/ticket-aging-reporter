import csv, sys
from datetime import datetime
FMT = "%Y-%m-%d"
def bucket(age_days):
    if age_days <= 1: return "0-1 days"
    if age_days <= 7: return "2-7 days"
    if age_days <= 30: return "8-30 days"
    return "30+ days"
def report(rows, today):
    counts = {"0-1 days": 0, "2-7 days": 0, "8-30 days": 0, "30+ days": 0}
    for r in rows:
        age = (today - datetime.strptime(r["created_at"], FMT).date()).days
        counts[bucket(age)] += 1
    return counts
def report_csv(path, today_str):
    today = datetime.strptime(today_str, FMT).date()
    with open(path, newline="", encoding="utf-8") as f: return report(list(csv.DictReader(f)), today)
if __name__ == "__main__":
    print(report_csv(sys.argv[1], sys.argv[2]))
