"""Functions for loading raw source data."""

from pathlib import Path

import pandas as pd
from src.config import RAW_DATA_PATH

def load_raw_data(file_path: Path | str | None = None) -> pd.DataFrame:
    """Load the raw customer CSV and return it as a DataFrame."""
    if file_path is None:
         file_path = RAW_DATA_PATH

    df = pd.read_csv(file_path, encoding="utf-8-sig", na_values=["N/A", "unknown", ""])
    return df

