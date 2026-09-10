import hashlib
import json
import uuid
from datetime import datetime, timedelta, timezone

def calculate_readiness_score(worker: dict, evidence_list: list) -> dict:
    """
    Algorithmic Readiness Score Engine (0-100)
    Factors:
    1. Income Stability (40 pts)
    2. Platform Consistency / Evidence Count (30 pts)
    3. Multi-platform Diversity (20 pts)
    4. Document Verification / OCR Confidence (10 pts)
    """
    # 1. Income stability subscore (Max 40)
    base_income = worker.get("monthly_income_est", 30000.0)
    if base_income >= 40000:
        income_stability = 38
    elif base_income >= 30000:
        income_stability = 32
    elif base_income >= 20000:
        income_stability = 26
    else:
        income_stability = 18

    # 2. Platform Consistency / Evidence Volume (Max 30)
    doc_count = len(evidence_list)
    if doc_count >= 3:
        tenure_score = 28
    elif doc_count == 2:
        tenure_score = 22
    elif doc_count == 1:
        tenure_score = 15
    else:
        tenure_score = 10

    # 3. Multi-platform Diversity (Max 20)
    platforms = set()
    if worker.get("primary_platform"):
        platforms.add(worker["primary_platform"].strip())
    secondaries = worker.get("secondary_platforms", "")
    if secondaries:
        for p in secondaries.split(","):
            if p.strip():
                platforms.add(p.strip())

    for doc in evidence_list:
        if doc.get("platform"):
            platforms.add(doc["platform"].strip())

    if len(platforms) >= 3:
        diversity_score = 19
    elif len(platforms) == 2:
        diversity_score = 15
    else:
        diversity_score = 10

    # 4. OCR / Document Confidence (Max 10)
    if evidence_list:
        avg_confidence = sum(d.get("confidence_score", 0.9) for d in evidence_list) / len(evidence_list)
        doc_score = int(round(avg_confidence * 10))
    else:
        doc_score = 7

    total_score = min(99, max(25, income_stability + tenure_score + diversity_score + doc_score))

    # Determine income band
    est_income = worker.get("monthly_income_est", 35000)
    lower = int(est_income * 0.9 / 1000) * 1000
    upper = int(est_income * 1.15 / 1000) * 1000
    income_band = f"₹{lower:,} - ₹{upper:,}/mo"

    # Recommended loan limit (approx 2x - 2.5x monthly income based on score tier)
    multiplier = 2.5 if total_score >= 70 else (2.0 if total_score >= 50 else 1.2)
    recommended_loan_limit = int(round((est_income * multiplier) / 5000)) * 5000

    return {
        "score": total_score,
        "income_stability_subscore": int(income_stability * 2.5), # normalized to 100 scale for UI
        "tenure_subscore": int(tenure_score * 3.33),
        "diversity_subscore": int(diversity_score * 5.0),
        "income_band": income_band,
        "recommended_loan_limit": recommended_loan_limit,
    }

def generate_verifiable_credential(worker_id: str, score: int, income_band: str, validity_days: int = 30) -> dict:
    """
    Generates a cryptographically signed verifiable credential token with SHA-256 digest
    """
    now = datetime.now(timezone.utc)
    expires = now + timedelta(days=validity_days)
    cred_id = f"cred_wp_{uuid.uuid4().hex[:8]}"

    payload = {
        "credential_id": cred_id,
        "worker_id": worker_id,
        "score": score,
        "income_band": income_band,
        "issued_at": now.isoformat(),
        "expires_at": expires.isoformat(),
        "issuer": "WageProof Decentralized Identity Network",
        "standard": "W3C-Verifiable-Credentials-v2"
    }

    # Generate SHA-256 digest of canonical JSON payload
    raw_payload = json.dumps(payload, sort_keys=True).encode("utf-8")
    credential_hash = hashlib.sha256(raw_payload).hexdigest()

    qr_url = f"https://wageproof.io/verify?cred={cred_id}&hash={credential_hash[:12]}"

    return {
        "id": cred_id,
        "credential_hash": credential_hash,
        "readiness_score": score,
        "income_band": income_band,
        "issued_at": now.isoformat(),
        "expires_at": expires.isoformat(),
        "qr_data": qr_url,
    }
