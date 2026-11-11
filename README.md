# Customer Churn Prediction – Data Engineering Team Project

## Summary

Subscription businesses lose revenue every time a customer cancels (churns), and it is usually cheaper to keep a customer than to win a new one. This project builds an ETL pipeline that extracts the supplied data files and SQLite database, cleans and joins them, runs data quality checks, and loads one tidy Parquet dataset with one row per customer. From that dataset we will train classification models that predict each customer's probability of churning, so the business can target at-risk customers with retention offers.

## Team

| Name | Role | GitHub username |
| --- | --- | --- |
| Kavindu Pabasara | TBC | kavinduUHgit |
| TBC | TBC | TBC |
| TBC | TBC | TBC |
| TBC | TBC | TBC |
| TBC | TBC | TBC |

## Folder structure

```text
Data-Engineering-Team-Project/
├── data/
│   └── raw/          # the lecturer's original files – never edited
├── notebooks/        # numbered Jupyter notebooks for exploration and results
├── src/              # the real pipeline code as plain Python functions
│   ├── etl/          # extract, transform, validate and load steps
│   └── utils/        # shared helpers such as logging
├── tests/            # pytest checks that the code works
├── docs/             # documentation, diagrams, meeting notes, screenshots
├── output/           # everything the code produces
│   ├── cleaned/      # the final Parquet dataset
│   ├── html/         # notebooks exported to HTML
│   ├── plots/        # saved charts
│   └── models/       # saved models (later phases)
└── logs/             # pipeline run logs (not saved to Git)
```

## Getting started

You need Git and Python 3.11 or newer.

**1. Clone the repo**

```bash
git clone https://github.com/kavinduUHgit/Data-Engineering-Team-Project.git
cd Data-Engineering-Team-Project
```

**2. Create and activate a virtual environment**

Windows (PowerShell):

```powershell
python -m venv venv
venv\Scripts\activate
```

Mac / Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install the packages and check everything works**

```bash
pip install -r requirements.txt
pytest
```

You should see `1 passed`.

## How to run

Coming soon.

## Documentation

These files are added as the project progresses:

- [Project brief notes](docs/project_brief_notes.md) – deliverables, deadlines, open questions (Practical C1)
- [Meeting notes](docs/meetings/) – one file per meeting
- [Decisions log](docs/decisions.md) – team decisions and why we made them
- [Data investigation](docs/data_investigation.md) – what the supplied data contains (Practical C3)
- [Data dictionary](docs/data_dictionary.md) – every column explained (Practical C3)
- [ER diagram](docs/er_diagram.png) – how the database tables relate (Practical C3)
- [Learning plan](docs/learning_plan.md) – skills audit, roles and learning plans (Practical C4)
- [ETL design](docs/etl_design.md) – the planned pipeline (Practical C5)
- [Data folder notes](data/README.md) – where the data came from

## AI use

We use an AI coding assistant to help write code and documentation; all team members review and understand the code.
