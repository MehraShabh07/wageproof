# 💳 WageProof — Financial Readiness Passport for Informal & Gig Workers

[![FastAPI](https://img.shields.io/badge/Backend-FastAPI_0.115+-009688.svg?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB.svg?logo=python&logoColor=white)](https://python.org)
[![Figma](https://img.shields.io/badge/Design_System-Figma_2.4-F24E1E.svg?logo=figma&logoColor=white)](./FIGMA.md)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

> **"Informal Work, Formal Credibility."**  
> WageProof converts messy, fragmented UPI transactions, invoices, and gig payouts into a cryptographically verified, privacy-preserving **Financial Readiness Passport** for India's 450M+ informal workers — without ever exposing raw documents to lenders.

---

## 🎨 Figma Design System & UI Specifications

All Figma design specifications, layout frames, and design tokens are included directly in this repository for easy import and design handoff:

- 📘 **[FIGMA.md](./FIGMA.md)**: Full Figma design specification, including:
  - **6 Master Artboards** (`1440 × 900 px` Auto-Layout, mobile-responsive):
    1. Landing Page (Hero, Value Prop, 6-Step Interactive Flow)
    2. Worker Onboarding Wizard (4 Steps, DPDP Consent Gate, Evidence Upload)
    3. Evidence Vault (OCR Verification Confidence, Instant Revocation)
    4. Readiness Profile & Scoring (Explainable Score Dial `71/100`, ₹35k–₹42k/mo Income Band)
    5. Verifiable QR Credential Badge (W3C standard, 72h Expiry protection)
    6. Lender Audit Portal (Zero-Knowledge Verifier, Manual Review & Decline Decisions)
  - Color Tokens, Typography Scale (`Inter`), Shadows, and Spacing Grids.
  - Interactive Prototyping Wireflow triggers and transitions.
- 📦 **[`figma-tokens.json`](./figma-tokens.json)**: W3C Design Tokens JSON file ready to import into Figma via the **Tokens Studio for Figma** plugin or Figma Native Variables.

---

## 🚀 Live Demo & Endpoints

| Resource | Public URL | Local URL |
|---|---|---|
| **Interactive Web Prototype** | [Live Public Prototype](https://elfya-103-211-14-48.run.pinggy-free.link) | [http://localhost:8000](http://localhost:8000) |
| **Interactive API Documentation** | [Swagger UI](https://elfya-103-211-14-48.run.pinggy-free.link/docs) | [http://localhost:8000/docs](http://localhost:8000/docs) |
| **System Health Check** | [Health Check](https://elfya-103-211-14-48.run.pinggy-free.link/health) | [http://localhost:8000/health](http://localhost:8000/health) |
| **Platform Stats & Metrics** | [API Stats](https://elfya-103-211-14-48.run.pinggy-free.link/api/stats) | [http://localhost:8000/api/stats](http://localhost:8000/api/stats) |

---

## ✨ Key Features

1. **Consent-First Worker Ingestion**:
   - 4-step wizard with DPDP Act compliance.
   - Support for food delivery (Zomato/Swiggy), ride-hailing (Uber/Ola), quick commerce, and artisans.
2. **Deterministic Multi-Signal Scoring Engine**:
   - Scores 4 dimensions: Income Regularity (30%), Platform Diversity (25%), Expense Coverage (25%), and Work Continuity (20%).
3. **Cryptographic Verifiable Credential**:
   - W3C standard QR badge with a 72-hour expiration window preventing stale exposure.
4. **Institutional Lender Audit & Underwriting Portal**:
   - Zero-Knowledge claims verifier (lenders verify claims without seeing raw bank statements).
   - Real-time underwriting triggers: **Flag for Manual Review**, **Decline**, and **Download Official Certificate**.
5. **Multilingual (i18n) Engine**:
   - Instant language switching across 6 Indian languages: English, हिन्दी (Hindi), বাংলা (Bengali), தமிழ் (Tamil), తెలుగు (Telugu), and मराठी (Marathi).

---

## 🏗️ Quickstart (Running Locally)

### Prerequisites
- Python 3.9+
- pip

### 1. Install Dependencies
```bash
pip install fastapi uvicorn pydantic python-multipart
```

### 2. Start the Backend & Prototype Server
```bash
python3 -m uvicorn main:app --host 0.0.0.0 --port 8000 --app-dir backend --reload
```

### 3. Open in Browser
Visit **[http://localhost:8000](http://localhost:8000)** to interact with the prototype.

---

## 📁 Repository Structure

```
.
├── FIGMA.md                     # Complete Figma UI architecture & screen blueprints
├── figma-tokens.json            # W3C Standard Figma Design Tokens for Tokens Studio
├── README.md                    # Project documentation & quickstart
├── index.html                   # Primary Web Prototype frontend
├── wageproof_prototype.html     # Prototype master template
├── WageProof_Pitch_Deck.pptx    # Complete 12-slide Pitch Deck
└── backend/
    ├── database.py              # SQLite3 persistence layer & schema migrations
    ├── models.py                # Pydantic v2 schemas for requests & responses
    ├── engine.py                # 4-dimensional readiness scoring & credential generation
    ├── main.py                  # FastAPI REST routes & static file hosting
    └── tests.py                 # Automated backend test suite
```

---

## 📜 License
This project is open-source under the MIT License.
