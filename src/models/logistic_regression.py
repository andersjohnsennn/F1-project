import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler


def prepare_data(X_train, X_test):

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

    scaler = StandardScaler()

    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    return (
        X_train_scaled,
        X_test_scaled,
        scaler
    )


def train_logistic_regression(
    X_train,
    y_train
):

    model = LogisticRegression(
        max_iter=1000,
        class_weight="balanced"
    )

    model.fit(X_train, y_train)

    return model