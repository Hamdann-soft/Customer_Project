from src.ingestion.load_data import load_raw_data
from src.transformations.clean_data import transform_data
from src.database.connection import get_database_connection
from src.database.load_to_sql import load_clean_data_to_sql
df = load_raw_data()
clean=transform_data(df)

df.info()
print(df.isna().sum())
print(df.duplicated().sum())
print(df["city"].value_counts(dropna=False))
print(df["customer_segment"].value_counts(dropna=False))
print(df["payment_method"].value_counts(dropna=False))
print(df["order_status"].value_counts(dropna=False))
print(df["city"])

clean = transform_data(df)
print(clean.info())
print(clean.isna().sum())
print(clean.duplicated().sum())
print(clean["city"].value_counts(dropna=False))
print(clean["payment_method"].value_counts(dropna=False))
print(clean["order_status"].value_counts(dropna=False))
print(clean[["quantity", "unit_price_pkr", "total_amount_pkr"]].describe())


from src.validation.validate_data import validate_data

valid = validate_data(clean)
print(len(clean), len(valid))



connection = get_database_connection()
print(connection)



load_clean_data_to_sql(valid, connection)