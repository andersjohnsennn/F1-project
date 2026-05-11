import pandas as pd

from sklearn.ensemble import RandomForestClassifier


def prepare_data(
    X_train,
    X_test
):
    """
    Encode categorical variables
    and align train/test columns.
    """

    X_train = pd.get_dummies(
        X_train,
        drop_first=True
    )

    X_test = pd.get_dummies(
        X_test,
        drop_first=True
    )

    X_train, X_test = X_train.align(
        X_test,
        join="left",
        axis=1,
        fill_value=0
    )

    return X_train, X_test


def train_random_forest(
    X_train,
    y_train
):
    """
    Train Random Forest classifier.
    """

    model = RandomForestClassifier(
        n_estimators=200,
        max_depth=10,
        random_state=42,
        class_weight="balanced"
    )

    model.fit(
        X_train,
        y_train
    )

    return model
    