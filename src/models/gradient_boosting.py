from sklearn.ensemble import GradientBoostingClassifier


def train_gradient_boosting(
    X_train,
    y_train):
    # Create model
    gb_model = GradientBoostingClassifier(
        n_estimators=200,
        learning_rate=0.05,
        max_depth=5,
        random_state=42
    )

    # Train model
    gb_model.fit(
        X_train,
        y_train
    )

    return gb_model