import pandas as pd

def load_all_clean_data():

    dfs = {
        "circuits": pd.read_csv("../data/processed/circuits_clean.csv"),
        "constructors": pd.read_csv("../data/processed/constructors_clean.csv"),
        "constructor_standings": pd.read_csv("../data/processed/constructor_standings_clean.csv"),
        "drivers": pd.read_csv("../data/processed/drivers_clean.csv"),
        "driver_standings": pd.read_csv("../data/processed/driver_standings_clean.csv"),
        "qualifying": pd.read_csv("../data/processed/qualifying_clean.csv"),
        "races": pd.read_csv("../data/processed/races_clean.csv"),
        "results": pd.read_csv("../data/processed/results_clean.csv")
    }

    return dfs