import numpy as np
import pandas as pd

def time_to_seconds(time_str):

    if pd.isna(time_str):
        return np.nan

    try:
        minutes, seconds = time_str.split(":")
        return (
            int(minutes) * 60
            + float(seconds)
        )

    except:
        return np.nan