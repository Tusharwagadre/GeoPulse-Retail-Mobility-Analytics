# GeoPulse: Hyper-Local Retail Mobility Analytics

> Data Associate L1 Internship Project | Infotact Solutions

## Project overview
GeoPulse is an analytics project focused on understanding how people move around local retail areas and how mobility patterns may relate to retail activity. The exact analysis, metrics, and deliverables must be aligned with the official project brief and the fields available in the approved dataset.

## Objectives
- Understand the supplied dataset and its structure.
- Assess data quality and document cleaning decisions.
- Explore relevant mobility and retail patterns.
- Develop meaningful KPIs and visualizations.
- Communicate evidence-based findings and recommendations.

## Project status
**Scaffold created.** No source dataset, analysis results, or business conclusions have been added yet.

## Repository structure
```text
GeoPulse-Retail-Mobility-Analytics/
├── data/
│   ├── raw/                 # Original data; do not commit confidential data
│   ├── processed/           # Cleaned/derived data; review before committing
│   └── README.md
├── dashboard/               # Dashboard files and documentation
├── docs/                    # Project brief, methodology, data dictionary
├── notebooks/               # Exploratory analysis notebooks
├── reports/                 # Findings and final report
├── src/                     # Reusable Python code
│   └── data_quality.py
├── tests/                   # Basic automated tests
├── visualizations/          # Exported charts and maps
├── .gitignore
├── requirements.txt
└── README.md
```

## Getting started
1. Read `docs/PROJECT_BRIEF_TEMPLATE.md` and replace placeholders using the official brief.
2. Place approved, non-sensitive source data in `data/raw/` locally.
3. Create an environment and install dependencies:
   ```bash
   python -m venv .venv
   # Windows PowerShell:
   .venv\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```
4. Start with `notebooks/01_data_understanding.ipynb`.
5. Record decisions and evidence in `docs/` and `reports/`.

## Data handling
- Never commit passwords, API keys, personal data, confidential company files, or restricted datasets.
- Keep raw data unchanged.
- Confirm company rules before publishing any dataset or dashboard.
- Use anonymized/synthetic samples when sharing examples publicly.

## Suggested workflow
Brief and scope → data inventory → data quality → cleaning → exploratory analysis → KPI definition → visualization/dashboard → validation → reporting.

## Commit convention
Use clear, meaningful commits, for example:
- `docs: add project objectives`
- `data: document dataset structure`
- `analysis: add initial profiling`
- `feat: add data quality checks`
- `viz: add exploratory charts`

Commit genuine progress only; do not create empty commits to inflate contribution counts.

## Disclaimer
This repository is an initial working scaffold, not a completed project. Update it only with verified project requirements, approved data, and reproducible findings.
