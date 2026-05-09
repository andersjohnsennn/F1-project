# Circuits DataFrame

## Non-needed columns
- `latitude`
- `longitude`
- `url`

## Missing values
No missing values were found in the circuits dataframe.

---

# Constructors DataFrame

## Non-needed columns
- `url`

## Missing values
No missing values were found in the constructors dataframe.

---

# Constructor Standings DataFrame

## Non-needed columns
- `constructor`

The constructor name can be retrieved from the constructors dataframe using `constructor_id`.

## Missing values
Missing values in `position` occur because constructors with 0 points are sometimes not assigned an official standing position.

---

# Drivers DataFrame

## Non-needed columns
- `code`
- `number`
- `url`

## Missing values
Missing values were found in:
- `number`
- `code`
- `dob`
- `nationality`
- `url`

These missing values are mainly caused by incomplete historical records for older drivers.

---

# Driver Standings DataFrame

## Non-needed columns
None.

## Missing values
Missing values in `position` occur because drivers with 0 points are sometimes not assigned an official standing position.

---

# Qualifying DataFrame

## Non-needed columns
None.

## Missing values

Missing values in:
- `q1` are typically caused by DNFs or cases where no valid qualifying lap was recorded.
- `q2` and `q3` occur because:
  - drivers may have been eliminated before later qualifying sessions,
  - the qualifying format evolved historically,
  - Q2 and Q3 were introduced in the mid-2000s.

These missing values are therefore not completely random and may contain performance-related information.

---

# Races DataFrame

## Non-needed columns
- `url`

## Missing values
Missing values in `time` occur because the race start time was not documented for some historical races.

---

# Results DataFrame

## Non-needed columns
- `race_name`
- `constructor`

`race_name` can be retrieved from the races dataframe using `season` and `round`.

`constructor` can be retrieved from the constructors dataframe using `constructor_id`.

## Missing values
Missing values occur in:
- `time`
- `fastest_lap`
- `fastest_lap_rank`

The `time` column is only recorded for drivers who finished within one lap of the race winner.

`fastest_lap` and `fastest_lap_rank` were not consistently recorded in early Formula 1 seasons.

Moving into the Data preprocessing:

* Identified the 14 drivers missing birthdays and nationality, should the age or nationality become significant later the values can be found and put in manually.

* removed all non needed columns and made new clean .csvs






