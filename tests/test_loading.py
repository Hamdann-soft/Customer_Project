"""Tests for raw-data ingestion."""
import pytest
from src.ingestion.load_data import load_raw_data

def test_successful_loading() -> None:
  df = load_raw_data()

def test_missing_or_invalid_input() -> None:
   with pytest.raises(FileNotFoundError):
       load_raw_data("does_not_exist.csv")