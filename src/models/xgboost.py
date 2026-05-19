from xgboost import XGBClassifier
import joblib


def train_xgboost(
    X_train,
    y_train,
    name="xgboost_model"
):

    xgb_model = XGBClassifier(
        n_estimators=500,
        learning_rate=0.03,
        max_depth=4,
        reg_alpha=0.5,
        reg_lambda=1,
        min_child_weight=3,
        gamma=1,
        subsample=0.8,
        colsample_bytree=0.8,
        scale_pos_weight=5,
        eval_metric="logloss",
        random_state=42
    )

    xgb_model.fit(
        X_train,
        y_train
    )

    path = rf"C:\Users\Ander\Desktop\F1-project\trained_models\{name}.pkl"

    # Save trained model
    joblib.dump(
        xgb_model,
        path)

    print("Model saved.")

    return xgb_model