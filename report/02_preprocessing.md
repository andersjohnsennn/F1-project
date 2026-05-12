# 02_preprocessing.ipynb — Summary

This notebook performs preprocessing and cleaning of multiple Formula 1 datasets before analysis or modeling.

## Main Tasks

- Imports required Python libraries and helper functions
- Loads datasets related to:
  - drivers
  - races
  - circuits
  - constructors
  - standings
  - qualifying
  - results

## Preprocessing Performed

### General Cleaning
- Creates cleaned copies of datasets
- Removes unnecessary columns (mainly URLs and unused metadata)
- Checks for missing values
- Standardizes dataset structure

### Dataset-Specific Notes
- **Drivers:** investigates missing birth dates and nationality information. The notebook identifies 14 drivers with missing values; these can later be manually completed if age or nationality becomes important for analysis.
- **Circuits / Constructors / Races:** removes irrelevant columns and prepares data for analysis
- **Standings:** cleans and verifies ranking-related data
- **Qualifying:** keeps missing Q1/Q2/Q3 values because they are meaningful (e.g. driver eliminated early)
- **Results:** prepares race result data for downstream use
