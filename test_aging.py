import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import unittest
from datetime import date
from aging import bucket, report
class T(unittest.TestCase):
    def test_buckets(self):
        self.assertEqual(bucket(0), "0-1 days"); self.assertEqual(bucket(5), "2-7 days")
        self.assertEqual(bucket(20), "8-30 days"); self.assertEqual(bucket(99), "30+ days")
    def test_report(self):
        rows = [{"created_at": "2026-10-25"}, {"created_at": "2026-10-20"}, {"created_at": "2026-09-01"}]
        r = report(rows, date(2026, 10, 25))
        self.assertEqual(r, {"0-1 days": 1, "2-7 days": 1, "8-30 days": 0, "30+ days": 1})
if __name__ == "__main__": unittest.main()
