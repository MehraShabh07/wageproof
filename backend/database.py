import sqlite3
import os
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "wageproof.db"

def get_db_connection():
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Workers table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS workers (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        primary_platform TEXT NOT NULL,
        secondary_platforms TEXT DEFAULT '',
        monthly_income_est REAL DEFAULT 0,
        consent_timestamp TEXT NOT NULL,
        status TEXT DEFAULT 'active'
    )
    """)

    # 2. Evidence Documents table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS evidence_documents (
        id TEXT PRIMARY KEY,
        worker_id TEXT NOT NULL,
        doc_type TEXT NOT NULL,
        platform TEXT NOT NULL,
        file_name TEXT NOT NULL,
        extracted_income REAL DEFAULT 0,
        confidence_score REAL DEFAULT 0.95,
        verification_status TEXT DEFAULT 'verified',
        uploaded_at TEXT NOT NULL,
        FOREIGN KEY (worker_id) REFERENCES workers (id)
    )
    """)

    # 3. Readiness Scores table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS readiness_scores (
        id TEXT PRIMARY KEY,
        worker_id TEXT NOT NULL,
        score INTEGER NOT NULL,
        income_stability_subscore INTEGER NOT NULL,
        tenure_subscore INTEGER NOT NULL,
        diversity_subscore INTEGER NOT NULL,
        income_band TEXT NOT NULL,
        recommended_loan_limit INTEGER NOT NULL,
        calculated_at TEXT NOT NULL,
        FOREIGN KEY (worker_id) REFERENCES workers (id)
    )
    """)

    # 4. Verifiable Credentials table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS verifiable_credentials (
        id TEXT PRIMARY KEY,
        worker_id TEXT NOT NULL,
        credential_hash TEXT NOT NULL,
        readiness_score INTEGER NOT NULL,
        income_band TEXT NOT NULL,
        issued_at TEXT NOT NULL,
        expires_at TEXT NOT NULL,
        qr_data TEXT NOT NULL,
        is_revoked INTEGER DEFAULT 0,
        FOREIGN KEY (worker_id) REFERENCES workers (id)
    )
    """)

    # 5. Lender Audit Trail table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS lender_audit_logs (
        id TEXT PRIMARY KEY,
        credential_id TEXT NOT NULL,
        lender_name TEXT NOT NULL,
        verification_status TEXT NOT NULL,
        readiness_score INTEGER,
        income_band TEXT,
        queried_at TEXT NOT NULL
    )
    """)

    # Check if seed worker already exists
    cursor.execute("SELECT id FROM workers WHERE id = 'worker_sana_01'")
    if not cursor.fetchone():
        cursor.execute("""
        INSERT INTO workers (id, name, phone, primary_platform, secondary_platforms, monthly_income_est, consent_timestamp, status)
        VALUES ('worker_sana_01', 'Sana Khan', '+91 98765 43210', 'Uber', 'Zomato, Swiggy', 38500.0, '2026-09-10T14:30:00Z', 'active')
        """)

        cursor.execute("""
        INSERT INTO evidence_documents (id, worker_id, doc_type, platform, file_name, extracted_income, confidence_score, verification_status, uploaded_at)
        VALUES 
        ('doc_01', 'worker_sana_01', 'Payout Slip', 'Uber Driver', 'uber_payout_aug2026.pdf', 24200.0, 0.98, 'verified', '2026-09-10T14:35:00Z'),
        ('doc_02', 'worker_sana_01', 'Gig Settlement', 'Zomato Delivery', 'zomato_settlement_aug2026.pdf', 14300.0, 0.95, 'verified', '2026-09-10T14:36:00Z')
        """)

        cursor.execute("""
        INSERT INTO readiness_scores (id, worker_id, score, income_stability_subscore, tenure_subscore, diversity_subscore, income_band, recommended_loan_limit, calculated_at)
        VALUES ('score_01', 'worker_sana_01', 71, 75, 68, 70, '₹35,000 - ₹42,000/mo', 75000, '2026-09-10T14:40:00Z')
        """)

        cursor.execute("""
        INSERT INTO verifiable_credentials (id, worker_id, credential_hash, readiness_score, income_band, issued_at, expires_at, qr_data, is_revoked)
        VALUES ('cred_wp_8892', 'worker_sana_01', 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855', 71, '₹35,000 - ₹42,000/mo', '2026-09-10T14:42:00Z', '2026-10-10T14:42:00Z', 'https://wageproof.io/verify?cred=cred_wp_8892', 0)
        """)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully at:", DB_PATH)
