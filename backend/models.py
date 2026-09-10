from pydantic import BaseModel, Field
from typing import List, Optional

# --- Worker Models ---
class WorkerCreate(BaseModel):
    name: str = Field(..., example="Sana Khan")
    phone: str = Field(..., example="+91 98765 43210")
    primary_platform: str = Field(..., example="Uber")
    secondary_platforms: Optional[str] = Field(default="", example="Zomato, Swiggy")
    monthly_income_est: Optional[float] = Field(default=35000.0, example=38500.0)

class WorkerResponse(BaseModel):
    id: str
    name: str
    phone: str
    primary_platform: str
    secondary_platforms: str
    monthly_income_est: float
    consent_timestamp: str
    status: str

# --- Evidence Models ---
class EvidenceUploadRequest(BaseModel):
    worker_id: str
    doc_type: str = Field(..., example="Payout Slip")
    platform: str = Field(..., example="Uber")
    file_name: str = Field(..., example="uber_statement_aug.pdf")
    income_amount: Optional[float] = Field(default=24000.0)

class EvidenceResponse(BaseModel):
    id: str
    worker_id: str
    doc_type: str
    platform: str
    file_name: str
    extracted_income: float
    confidence_score: float
    verification_status: str
    uploaded_at: str

# --- Readiness Score Models ---
class ReadinessCalculationResponse(BaseModel):
    id: str
    worker_id: str
    score: int
    income_stability_subscore: int
    tenure_subscore: int
    diversity_subscore: int
    income_band: str
    recommended_loan_limit: int
    calculated_at: str

# --- Verifiable Credential Models ---
class CredentialIssueRequest(BaseModel):
    worker_id: str
    validity_days: Optional[int] = 30

class CredentialResponse(BaseModel):
    id: str
    worker_id: str
    credential_hash: str
    readiness_score: int
    income_band: str
    issued_at: str
    expires_at: str
    qr_data: str
    is_revoked: bool

# --- Lender Verification Models ---
class LenderVerifyRequest(BaseModel):
    credential_id: str = Field(..., example="cred_wp_8892")
    lender_name: str = Field(..., example="FinSecure Capital")

class LenderVerifyResponse(BaseModel):
    verified: bool
    status: str
    credential_id: str
    readiness_score: Optional[int] = None
    income_band: Optional[str] = None
    expires_at: Optional[str] = None
    tamper_check_passed: bool
    audit_id: str
    message: str
