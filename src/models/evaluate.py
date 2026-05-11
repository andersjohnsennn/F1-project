from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix
)


def evaluate_model(
    y_test,
    y_pred
):

    print(
        "Accuracy:",
        accuracy_score(y_test, y_pred)
    )

    print(
        classification_report(
            y_test,
            y_pred
        )
    )

    print(
        confusion_matrix(
            y_test,
            y_pred
        )
    )