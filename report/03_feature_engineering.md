# 03_feature_engineering.ipynb — Summary

This notebook focuses on feature engineering and creation of the final master dataset used for analysis and modeling.

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

- Determined that `grid` and `qualifying_position` are not redundant and should both be retained
- Missing values for `qualifying_position` were filled using the corresponding `grid` position, as both variables were determined to contain complementary information rather than redundancy
- Corrected and standardized data types across variables
- Drivers with missing demographic information that never participated in races were naturally excluded during dataset merging
- Prepared the dataset for downstream analysis and machine learning workflows

## Output

- Saved the final processed master dataframe as a `.csv` file