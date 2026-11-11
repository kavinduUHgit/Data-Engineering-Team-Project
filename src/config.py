"""All file paths and settings for the project, kept in one place.

Every other file imports its paths from here instead of typing them out.
That way, if a folder moves, we only change it in this one file.
pathlib is used so the same paths work on Windows, Mac and Linux.
"""

from pathlib import Path

# The repo root folder. This file lives in <root>/src/config.py, so we go up
# two levels from this file's location. Working it out from the file (rather
# than the folder you run Python from) means it is correct on every laptop.
PROJECT_ROOT: Path = Path(__file__).resolve().parent.parent

# The lecturer's original data files and SQLite database. Never edited.
DATA_RAW_DIR: Path = PROJECT_ROOT / "data" / "raw"

# Top-level folder for everything the code produces.
OUTPUT_DIR: Path = PROJECT_ROOT / "output"

# Where the final cleaned dataset is saved.
CLEANED_DIR: Path = OUTPUT_DIR / "cleaned"

# Notebooks exported to HTML for the lecturer.
HTML_DIR: Path = OUTPUT_DIR / "html"

# Saved charts and figures.
PLOTS_DIR: Path = OUTPUT_DIR / "plots"

# Saved machine learning models (used in later phases).
MODELS_DIR: Path = OUTPUT_DIR / "models"

# Pipeline run logs. Ignored by Git.
LOGS_DIR: Path = PROJECT_ROOT / "logs"

# The single file the ETL pipeline produces: one row per customer.
FINAL_DATASET_PATH: Path = CLEANED_DIR / "churn_dataset.parquet"
