
import pandas as pd

def load_session_laptimes_file(
    registry,
    race,
    session,
):
    
    row = registry[
        (registry["race"] == race)
        &
        (registry["session"] == session)
        &
        (registry["type"] == "session_laptimes")
    ]

    session_laptimes = pd.read_parquet(
        row.iloc[0]["path"]
    )

    return session_laptimes

def get_telemetry_file(
    registry,
    race,
    session,
    driver,
):

    row = registry[
        (registry["race"] == race)
        &
        (registry["session"] == session)
        &
        (registry["type"] == "telemetry")
        &
        (registry["driver"] == driver)
    ]

    return row.iloc[0]["path"]

def get_laps_file(
    registry,
    race,
    session,
    driver,
):

    row = registry[
        (registry["race"] == race)
        &
        (registry["session"] == session)
        &
        (registry["type"] == "laps")
        &
        (registry["driver"] == driver)
    ]

    return row.iloc[0]["path"]

def load_driver_session(
    registry,
    race,
    session,
    driver,
):

    telemetry_path = get_telemetry_file(
        registry,
        race,
        session,
        driver,
    )

    laps_path = get_laps_file(
        registry,
        race,
        session,
        driver,
    )

    telemetry = pd.read_parquet(
        telemetry_path
    )

    laps = pd.read_parquet(
        laps_path
    )

    return telemetry, laps