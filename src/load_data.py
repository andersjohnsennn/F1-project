import pandas as pd

def load_all_data():

    dfs = {
        "circuits": pd.read_csv("../data/raw/f1_circuits.csv"),
        "constructors": pd.read_csv("../data/raw/f1_constructors.csv"),
        "constructor_standings": pd.read_csv("../data/raw/f1_constructor_standings.csv"),
        "drivers": pd.read_csv("../data/raw/f1_drivers.csv"),
        "driver_standings": pd.read_csv("../data/raw/f1_driver_standings.csv"),
        "qualifying": pd.read_csv("../data/raw/f1_qualifying.csv"),
        "races": pd.read_csv("../data/raw/f1_races.csv"),
        "results": pd.read_csv("../data/raw/f1_results.csv")
    }

    return dfs