# 03_feature_engineering.ipynb — Summary

This notebook focuses on feature engineering and creation of the final master dataset used for analysis or modeling.

## Main Tasks

- Merged multiple cleaned datasets into a single master dataframe:
  - results
  - circuits
  - constructor standings
  - driver standings
  - qualifying
  - races

## Feature Engineering

Created several new variables to improve analysis and predictive capability, including:

- `pole`
- `driver_age`
- `win`
- `front_row`
- and other race/performance-related features

## Additional Processing

- Determined that `grid` and `qualifying_position` are not redundant and should both be retained, with missing values for `qualifying_position` was filled with values from `grid`
- Corrected and standardized data types across variables
- Prepared the dataset for downstream analysis and machine learning workflows

## Output

- Saved the final processed master dataframe as a `.csv` file