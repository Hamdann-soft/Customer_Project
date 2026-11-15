"""Functions for validating transformed customer data."""

import pandas as pd


def validate_data(transformed_data: pd.DataFrame) -> pd.DataFrame:
   df=transformed_data.copy()
   rule_customer_id = df["customer_id"].notna()
   rule_date = df["order_date"].notna()
   rule_price = df["unit_price_pkr"].between(1, 500000)
   rule_order_id = df["order_id"].notna()
   rule_quantity = df["quantity"].between(1, 20)
   rule_status = df["order_status"].isin(["Completed", "Pending", "Cancelled", "Returned"])

   valid = rule_order_id & rule_quantity & rule_status & rule_customer_id & rule_date & rule_price   # add your other rules with &
   accepted = df[valid]
   rejected = df[~valid]
   print(len(rejected), "rejected")   # optional, to see the count
   print("bad order_id:", (~rule_order_id).sum())
   print("bad quantity:", (~rule_quantity).sum())
   print("bad status:", (~rule_status).sum())
   print("bad customer_id:", (~rule_customer_id).sum())
   print("bad date:", (~rule_date).sum())
   print("bad price:", (~rule_price).sum())
   return accepted