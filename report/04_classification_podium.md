# 04 Classification — Podium Prediction

## Objective

The objective of this task is to build a supervised machine learning model capable of predicting whether a Formula 1 driver will finish on the podium.

The target variable is:

- `podium`
    - `1` = podium finish
    - `0` = non-podium finish

---

# Feature Engineering

Several new features were engineered to improve predictive performance while avoiding data leakage. All features were constructed using only information available before the race being predicted.

## Engineered Features

### Current Season Driver Points

The cumulative number of points scored by a driver earlier in the same season before the current race.

Feature:
- `current_season_points`

---

### Average Points Per Season

The average number of points scored across previous seasons.

Feature:
- `avg_points_per_season`

---

### Constructor Current Season Points

The cumulative constructor points before the current race.

Feature:
- `constructor_points_current_season`

Special care was taken to correctly aggregate teammate points per round before calculating cumulative constructor totals.

---

### Points in Previous Five Races

The total number of points scored by a driver across the previous five races.

Feature:
- `points_last_5_races`

This feature captures recent driver form and momentum.

---

# Statistical Analysis of Features

A statistical analysis was performed to evaluate the discriminative ability of candidate features.

---

## Distribution Analysis

Before selecting statistical tests, feature distributions were visually inspected using:

- histograms
- Q-Q plots

---

## Numerical Variables

### Non-Normal Variables

Variables showing skewness or non-normal distributions were evaluated using the Mann–Whitney U test.

Examples:
- `grid`
- `current_season_points`
- `avg_points_per_season`
- `driver_age`

These variables showed strong or light right-skewed distributions and therefore violated strict normality assumptions.

---

## Categorical Variables

Categorical variables were evaluated using the Chi-square test of independence.

Examples:
- `constructor_name`
- `front_row`
- `driver_nationality`

The analysis showed that several categorical variables had statistically significant associations with podium outcomes.

---

# Correlation Analysis

Correlation analysis was performed on numerical features to detect multicollinearity and redundant predictors.

Pearson correlation coefficients were calculated and visualized using a heatmap.

One feature pair exceeded the predefined multicollinearity threshold of:

- `|correlation| > 0.90`

A strong correlation (`0.95`) was observed between:

- `constructor_points_current_season`
- `current_season_points`

Since both variables capture similar competitive performance information, `constructor_points_current_season` was removed to reduce redundancy.

---

# Categorical Association Analysis

Associations between categorical variables were evaluated using Cramér’s V.

No categorical variables showed excessive redundancy requiring removal.

---

# Selected Features for Modeling

The final feature set contains a combination of:

- qualifying performance
- driver experience
- recent form
- historical performance
- constructor strength

Selected features include:

- `grid`
- `driver_age`
- `constructor_name`
- `current_season_points`
- `avg_points_per_season`
- `points_last_5_races`

These features will be used in the supervised learning stage for podium classification.