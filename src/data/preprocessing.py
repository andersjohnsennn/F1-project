import pandas as pd

from sklearn.preprocessing import StandardScaler


def prepare_chronological_data(
    df,
    features,
    target="podium",
    split_season=2013,
    scale=False
):
    """
    Prepare chronological train/test split.
    """

    # Split

    train_df = df[
        df["season"] <= split_season
    ]

    test_df = df[
        df["season"] > split_season
    ]

    # Features and target

    X_train = train_df[features]
    y_train = train_df[target]

    X_test = test_df[features]
    y_test = test_df[target]

    # Fill missing values

    X_train = X_train.fillna(0)
    X_test = X_test.fillna(0)

    # One-hot encoding

    X_train = pd.get_dummies(
        X_train,
        drop_first=True
    )

    X_test = pd.get_dummies(
        X_test,
        drop_first=True
    )

    # Align columns

    X_train, X_test = X_train.align(
        X_test,
        join="left",
        axis=1,
        fill_value=0
    )

    # Optional scaling

    scaler = None

    if scale:

        scaler = StandardScaler()

        X_train = scaler.fit_transform(
            X_train
        )

        X_test = scaler.transform(
            X_test
        )

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        scaler
    )