"""Functions for cleaning and transforming customer data."""

import pandas as pd
from src.ingestion.load_data import load_raw_data

def transform_data(raw_data: pd.DataFrame) -> pd.DataFrame:
  df = raw_data.copy()
  df["city"] = df["city"].str.strip().str.title()
  df["customer_segment"] = df["customer_segment"].str.strip().str.title()
  df["payment_method"] = df["payment_method"].str.strip().str.title()
  df["order_status"] = df["order_status"].str.strip().str.title()
  
  df["Full Name"]=df["first_name"].str.strip() + " " + df["last_name"].str.strip()
  df=df.drop(columns=["first_name", "last_name"])
  df["quantity"]=df["quantity"].replace({"five": "5"})
  df["quantity"]=pd.to_numeric(df["quantity"], errors="coerce")

  bad_price = df["unit_price_pkr"] < 0
  df.loc[bad_price, "unit_price_pkr"] = pd.NA

  df["order_date"] = pd.to_datetime(df["order_date"], format="mixed", dayfirst=True, errors="coerce")
  df["city"] = df["city"].fillna("Unknown")
  df = df.drop_duplicates()

  return df