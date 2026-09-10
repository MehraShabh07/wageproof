# 🎨 WageProof — Figma Design System & UI Architecture

This document provides the complete UI/UX specification, design tokens, frame blueprints, and prototyping instructions for the **WageProof** Financial Readiness Passport platform.

---

## 📑 Table of Contents
1. [Project Overview](#project-overview)
2. [Figma File Architecture](#figma-file-architecture)
3. [Design Tokens](#design-tokens)
   - [Color Palette](#color-palette)
   - [Typography](#typography)
   - [Elevation & Shadows](#elevation--shadows)
   - [Border Radius & Spacing](#border-radius--spacing)
4. [Master Artboards (6 Screens)](#master-artboards-6-screens)
   - [Screen 1: Landing Page](#screen-1-landing-page)
   - [Screen 2: Worker Onboarding Wizard](#screen-2-worker-onboarding-wizard)
   - [Screen 3: Evidence Vault](#screen-3-evidence-vault)
   - [Screen 4: Readiness Profile & Scoring](#screen-4-readiness-profile--scoring)
   - [Screen 5: QR Credential Badge](#screen-5-qr-credential-badge)
   - [Screen 6: Lender Audit & Decision Portal](#screen-6-lender-audit--decision-portal)
5. [Interactive Prototyping Wireflow](#interactive-prototyping-wireflow)
6. [Importing Tokens into Figma](#importing-tokens-into-figma)

---

## 1. Project Overview
- **Product**: WageProof — Privacy-First Financial Readiness Passport for Informal & Gig Workers
- **Target Users**: 450M+ Indian informal gig workers (delivery partners, drivers, artisans) & Institutional Lenders (NBFCs, Banks)
- **Primary Artboard Resolution**: Desktop Web `1440 × 900 px` (Auto-Layout responsive to Mobile `390 × 844 px`)
- **Visual Style**: Sleek Dark Glassmorphic Fintech (`#0F172A` Navy base, `#00D4AA` Mint Teal accents)

---

## 2. Figma File Architecture

In your Figma project, structure your pages as follows:

```
📁 WageProof Master Project
 ├── 📄 00 · Cover & Changelog
 ├── 📄 01 · Global Design Tokens (Styles & Variables)
 ├── 📄 02 · Atomic Components & Variants (Badges, Buttons, Inputs)
 ├── 📄 03 · Complex Components (Vault Cards, Score Gauges, QR Cards)
 ├── 📄 04 · User Flow 1: Worker Journey (Landing ➔ Onboarding ➔ Profile)
 ├── 📄 05 · User Flow 2: Lender Journey (Search ➔ Claims ➔ Underwriting Decision)
 └── 📄 06 · Master Interactive Prototype (All Connected Frames)
```

---

## 3. Design Tokens

### Color Palette

| Token Name | Hex Code | RGB | Role / Usage |
|---|---|---|---|
| `color-bg-primary` | `#0F172A` | `rgb(15, 23, 42)` | Root Canvas Background (Deep Navy) |
| `color-bg-surface` | `#1E293B` | `rgb(30, 41, 59)` | Cards, Modals, Secondary Surfaces |
| `color-bg-elevated` | `#162032` | `rgb(22, 32, 50)` | Inner Wells, Nested Cards, Code Blocks |
| `color-accent-teal` | `#00D4AA` | `rgb(0, 212, 170)` | Primary Actions, Verified Status, High Scores |
| `color-accent-blue` | `#38BDF8` | `rgb(56, 189, 248)` | Identity Badges, W3C Tags, Micro-Indicators |
| `color-warning-amber`| `#F59E0B` | `rgb(245, 158, 11)` | In-Review Documents, Caution Banners |
| `color-success-green`| `#10B981` | `rgb(16, 185, 129)` | Verified Badges, Approved Applications |
| `color-danger-red` | `#F87171` | `rgb(248, 113, 113)` | Revoke Actions, Decline Status, Alerts |
| `color-text-primary`| `#FFFFFF` | `rgb(255, 255, 255)` | Main Headings, Strong Data Labels |
| `color-text-muted` | `#94A3B8` | `rgb(148, 163, 184)` | Secondary Labels, Metadata, Subtitles |
| `color-border-subtle`| `rgba(255, 255, 255, 0.08)` | — | Card Dividers & Borders |

### Typography

Font Family: **`Inter`** (Available free on Google Fonts / native to Figma)

| Figma Text Style | Font Size | Line Height | Weight | Letter Spacing |
|---|---|---|---|---|
| `Display / Hero Title` | `56px` | `64px` | 900 (Black) | `-0.02em` |
| `Heading / H1` | `36px` | `44px` | 800 (ExtraBold) | `-0.01em` |
| `Heading / H2` | `24px` | `32px` | 700 (Bold) | `0em` |
| `Heading / H3` | `18px` | `26px` | 600 (SemiBold) | `0em` |
| `Body / Regular` | `14px` | `22px` | 400 (Regular) | `0em` |
| `Body / Medium` | `14px` | `22px` | 500 (Medium) | `0em` |
| `Label / Bold` | `12px` | `16px` | 700 (Bold) | `0.05em` (Uppercase) |
| `Code / Mono` | `13px` | `20px` | 500 (JetBrains Mono) | `0em` |

### Elevation & Shadows
- **Card Shadow**: `0 4px 24px rgba(0, 0, 0, 0.35)`
- **Hover Glow (Teal)**: `0 8px 32px rgba(0, 212, 170, 0.25)`
- **Identity Glow (Blue)**: `0 8px 32px rgba(56, 189, 248, 0.25)`

### Border Radius & Spacing
- **Base Grid**: `8px`
- **Border Radius**:
  - `4px`: Chips & micro-badges
  - `8px`: Buttons, form inputs, nested badges
  - `14px`: Cards, panels, modals
  - `24px`: Hero stat containers

---

## 4. Master Artboards (6 Screens)

### Screen 1: Landing Page (`1440 × 900 px`)
- **Header**: Sticky Navbar (`#0F172A`, height `64px`, border-bottom `1px solid rgba(255,255,255,0.08)`).
- **Hero Section**:
  - Track Badge: `OPEN INNOVATION TRACK` (Teal pill, `12px`).
  - Heading: `"Informal Work, Formal Credibility."`
  - Subheading: 450M+ gig workers financial passport narrative.
  - CTAs: Primary `"🚀 Build My Proof"` & Outline `"For Lenders →"`.
  - Floating Stat Badges: 450M+ unbanked, 98% verification speed, 0 documents exposed.
- **6-Step "How It Works" Flow**:
  - Horizontal interactive stepper with connectors:
    1. Consent Gate ➔ 2. Upload Evidence ➔ 3. Verify & Analyse ➔ 4. Readiness Profile ➔ 5. QR Credential ➔ 6. Financial Access.

### Screen 2: Worker Onboarding Wizard (`1440 × 900 px`)
- **Stepper Header**: 4-Step progress bar (Step 1: Consent, Step 2: Track, Step 3: Evidence, Step 4: Submit).
- **Step 1 — Consent Gate**:
  - Digital Personal Data Protection (DPDP) compliance toggle cards.
- **Step 2 — Occupation Selector**:
  - 3 Grid Cards: Ride-Hailing (Uber/Ola), Food Delivery (Zomato/Swiggy), Quick Commerce / Artisan.
- **Step 3 — Evidence Ingestion**:
  - Drag-and-drop zone with OCR sample chips (UPI PhonePe statements, Meesho settlements).
- **Step 4 — Algorithmic Processing Indicator**:
  - Simulated progress animation filling to 100%.

### Screen 3: Evidence Vault (`1440 × 900 px`)
- **Vault Metrics Bar**: 7 Documents Uploaded | 5 Verified | 2 Under Review | 27 Months Continuity.
- **Evidence Card Grid (Auto-Layout 3 Columns)**:
  - Document icon, Title, Provider, Confidence Bar (88%–98% OCR match).
  - Instant **Revoke Permission** button (`#F87171`).
- **Privacy Assurance Footer**: Lock banner explaining zero document exposure to lenders.

### Screen 4: Readiness Profile & Scoring (`1440 × 900 px`)
- **Score Dashboard**:
  - Radial Gauge: **`71 / 100`** (Financial Readiness Tier: Strong).
  - Verified Income Band: **`₹35,000 – ₹42,000 / month`**.
  - Recommended Pre-Approved Credit: **`₹75,000`**.
- **Four Dimensional Score Breakdown**:
  1. Income Regularity: `78 / 100`
  2. Platform Diversity: `70 / 100`
  3. Expense Coverage Ratio: `74 / 100`
  4. Work Continuity: `82 / 100`

### Screen 5: QR Credential Badge (`1440 × 900 px`)
- **Digital Passport Card**:
  - High-contrast SVG QR Code bound to `cred_wp_8892`.
  - Cryptographic Verification Hash (`sha256: 4f88e9...`).
  - W3C Verifiable Credential standard seal.
  - Expiration Countdown Badge: `⏱ Valid for next 71h 58m`.
- **Worker Direct Actions**:
  - Copy Credential ID | Share to WhatsApp | Download PDF Badge.

### Screen 6: Lender Audit & Decision Portal (`1440 × 900 px`)
- **Credential Lookup Bar**: Search input with instant lookup for `cred_wp_8892`.
- **Zero-Knowledge Claims Table**:
  - Verified Monthly Cashflow: `₹38,400 (Confidence 96%)`
  - Inferred Continuity: `27 Consecutive Months`
  - Fraud / Tamper Flags: `0 Detected (Cryptographically Signed)`
- **Underwriter Decision Triggers (Live Backend Audited)**:
  - `✅ Flag for Manual Review` (Creates compliance audit trail).
  - `📋 Download Official Verification Certificate` (Signed PDF report).
  - `📧 Request More Evidence` (Dispatches SMS/WhatsApp link to worker).
  - `❌ Decline Application` (Logged with underwriting reason).

---

## 5. Interactive Prototyping Wireflow

When connecting frames in Figma's **Prototype Mode**:

| Starting Element | Interaction Trigger | Destination Frame | Animation Type |
|---|---|---|---|
| **Landing CTA ("Build My Proof")** | `On Click` | Frame #02 (Onboarding) | Smart Animate (300ms Ease) |
| **Landing Nav ("For Lenders")** | `On Click` | Frame #06 (Lender Portal) | Instant / Push Left |
| **Onboarding Step 4 Submit** | `On Click` | Frame #04 (Profile) | Smart Animate (400ms Ease-Out) |
| **Profile Nav ("View Vault")** | `On Click` | Frame #03 (Vault) | Instant |
| **Profile CTA ("Issue Credential")** | `On Click` | Frame #05 (QR Badge) | Smart Animate (350ms) |
| **QR Badge CTA ("Open in Lender")** | `On Click` | Frame #06 (Lender Portal) | Push Left (300ms) |

---

## 6. Importing Tokens into Figma

You can import all tokens into your Figma document in 3 simple steps:

1. Install the **Tokens Studio for Figma** plugin (or use Figma Native Variables).
2. Open the plugin ➔ Click **Settings** ➔ **Add New Set**.
3. Select **Load from JSON** and upload [`figma-tokens.json`](./figma-tokens.json) located in this directory.
4. Click **Apply to Selection** to instantly skin your artboards!
