import pandas as pd


def load_master_data():

    df = pd.read_csv(
        "../data/processed/master_ml_dataset.csv",
        low_memory=False
    )

    # Datetimes
    df["dob"] = pd.to_datetime(df["dob"])
    df["race_date"] = pd.to_datetime(df["race_date"])

    # Categories
    categorical_columns = [
        "driver_id",
        "driver_name",
        "constructor_id",
        "status",
        # "driver_nationality",
        "constructor_name",
        "constructor_nationality",
        "race_name",
        "circuit_id",
        "circuit_name",
        "circuit_locality",
        "circuit_country"
    ]

    for col in categorical_columns:
        df[col] = df[col].astype("category")

    return df
    