# GeoPulse | Hyper-Local Retail Mobility Analytics

**Internship project · Data Associate L1 · Infotact Solutions**

GeoPulse is an analytics project intended to explore hyper-local retail and mobility patterns. The final business questions, metrics, dataset, tools, and deliverables must be confirmed against the official project brief and mentor instructions.

> **Project status:** Repository scaffold initialized. Dataset analysis and business findings have not yet been completed.

## Project goals

- Understand the approved dataset, its structure, and its limitations.
- Assess and document data quality.
- Explore retail and mobility patterns supported by available fields.
- Define transparent, reproducible KPIs with clear calculation logic.
- Build visualizations and a dashboard aligned with the project requirements.
- Communicate evidence-based findings and recommendations.

## Repository map

```text
GeoPulse-Professional-Repository/
├── data/
│   ├── raw/                 # Original approved data; ignored by Git
│   ├── processed/           # Derived data; ignored by Git by default
│   └── README.md
├── dashboard/               # Dashboard plan, assets and documentation
├── docs/                    # Brief, methodology, data dictionary, decisions
├── notebooks/               # Ordered analysis notebooks
├── reports/                 # Interim and final reports
├── src/                     # Reusable Python modules
├── tests/                   # Automated checks
├── visualizations/          # Approved, non-sensitive exports
├── .gitignore
├── CONTRIBUTING.md
├── LICENSE-DECISION.md
├── requirements.txt
└── README.md
```

## Quick start

### 1. Clone the repository

```bash
git clone https://github.com/Tusharwagadre/GeoPulse-Retail-Mobility-Analytics.git
cd GeoPulse-Retail-Mobility-Analytics
```

If you are starting from the downloaded ZIP instead, extract it and open the extracted folder in VS Code.

### 2. Create a Python environment

```bash
python -m venv .venv
```

Windows PowerShell:
```powershell
.venv\Scripts\Activate.ps1
```

macOS/Linux:
```bash
source .venv/bin/activate
```

### 3. Install dependencies and run checks

```bash
pip install -r requirements.txt
pytest
```

## Recommended project workflow

1. Confirm the official brief, business questions, scope, and deliverables.
2. Record dataset provenance, schema, grain, and coverage.
3. Profile data quality before modifying data.
4. Clean and transform data reproducibly; preserve original source data.
5. Conduct exploratory analysis guided by the confirmed questions.
6. Define and validate KPIs with explicit formulas.
7. Build visualizations and dashboard pages.
8. Validate results and document limitations.
9. Prepare the final report and presentation.

## Daily progress

Use [`docs/DAILY_PROGRESS_LOG.md`](docs/DAILY_PROGRESS_LOG.md) to record actual progress across the planned 20-day work period. Every commit should represent a genuine change: code, analysis, documentation, testing, or a verified project decision.

## Data and security policy

- Do not commit confidential company data, personal information, credentials, access tokens, or restricted files.
- Keep raw source files unchanged and out of Git unless explicit permission is given.
- Check company rules before making this repository public.
- Do not publish dashboard exports or screenshots containing restricted information.
- Use synthetic or anonymized samples only when permitted.

## Project documentation

- [Official project brief template](docs/PROJECT_BRIEF_TEMPLATE.md)
- [Dataset inventory and data dictionary](docs/DATA_DICTIONARY_TEMPLATE.md)
- [Methodology](docs/METHODOLOGY.md)
- [KPI definition template](docs/KPI_CATALOG_TEMPLATE.md)
- [Daily progress log](docs/DAILY_PROGRESS_LOG.md)
- [Dashboard plan](dashboard/DASHBOARD_PLAN.md)
- [Contributing and commit conventions](CONTRIBUTING.md)

## License

Review `LICENSE-DECISION.md` and obtain the required approval before adding an open-source license. A public GitHub repository does not automatically mean the project or its data may be reused.
