import unittest
import sys
from pathlib import Path

# Add backend directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent))

from database import init_db, get_db_connection
from engine import calculate_readiness_score, generate_verifiable_credential
import uuid

class TestWageProofCore(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        init_db()

    def test_database_and_seed_data(self):
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT * FROM workers WHERE id = 'worker_sana_01'")
        row = c.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row["name"], "Sana Khan")

        c.execute("SELECT COUNT(*) as cnt FROM evidence_documents WHERE worker_id = 'worker_sana_01'")
        self.assertGreaterEqual(c.fetchone()["cnt"], 2)
        conn.close()

    def test_readiness_scoring_engine(self):
        worker = {
            "name": "Dev Sharma",
            "monthly_income_est": 38000.0,
            "primary_platform": "Uber",
            "secondary_platforms": "Zomato, Swiggy"
        }
        evidence = [
            {"platform": "Uber", "confidence_score": 0.98},
            {"platform": "Zomato", "confidence_score": 0.95},
            {"platform": "Swiggy", "confidence_score": 0.92}
        ]

        result = calculate_readiness_score(worker, evidence)
        self.assertIn("score", result)
        self.assertGreaterEqual(result["score"], 50)
        self.assertLessEqual(result["score"], 100)
        self.assertIn("₹", result["income_band"])
        self.assertGreater(result["recommended_loan_limit"], 50000)

    def test_verifiable_credential_cryptography(self):
        cred = generate_verifiable_credential("worker_test_99", score=82, income_band="₹40,000 - ₹50,000/mo")
        self.assertTrue(cred["id"].startswith("cred_wp_"))
        self.assertEqual(len(cred["credential_hash"]), 64) # SHA-256 length
        self.assertIn("https://wageproof.io/verify", cred["qr_data"])
        self.assertEqual(cred["readiness_score"], 82)

    def test_db_insert_and_audit(self):
        conn = get_db_connection()
        c = conn.cursor()
        test_id = f"test_{uuid.uuid4().hex[:6]}"
        c.execute("""
            INSERT INTO lender_audit_logs (id, credential_id, lender_name, verification_status, readiness_score, income_band, queried_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (test_id, "cred_wp_8892", "TestBank", "VERIFIED_VALID", 71, "₹35,000 - ₹42,000/mo", "2026-09-11T00:00:00Z"))
        conn.commit()

        c.execute("SELECT * FROM lender_audit_logs WHERE id = ?", (test_id,))
        row = c.fetchone()
        self.assertIsNotNone(row)
        self.assertEqual(row["lender_name"], "TestBank")
        conn.close()

if __name__ == "__main__":
    unittest.main()
