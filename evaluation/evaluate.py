"""
Model evaluation for ExoDetect-AI
"""

import os

import matplotlib.pyplot as plt
import numpy as np

from sklearn.metrics import (
    ConfusionMatrixDisplay,
    PrecisionRecallDisplay,
    RocCurveDisplay,
    accuracy_score,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
    roc_auc_score,
)


OUTPUT_DIR = "evaluation/results"
os.makedirs(OUTPUT_DIR, exist_ok=True)


def evaluate_model(model, X_test, y_test):

    print("=" * 50)
    print("Running Evaluation")
    print("=" * 50)

    y_prob = model.predict(X_test)

    if len(y_prob.shape) > 1:
        y_prob = y_prob[:, 0]

    y_pred = (y_prob >= 0.5).astype(int)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    try:
        roc = roc_auc_score(y_test, y_prob)
    except:
        roc = 0.0

    print(f"Accuracy : {accuracy:.4f}")
    print(f"Precision: {precision:.4f}")
    print(f"Recall   : {recall:.4f}")
    print(f"F1 Score : {f1:.4f}")
    print(f"ROC AUC  : {roc:.4f}")

    RocCurveDisplay.from_predictions(
        y_test,
        y_prob
    )

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            "roc_curve.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    PrecisionRecallDisplay.from_predictions(
        y_test,
        y_prob
    )

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            "pr_curve.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    cm = confusion_matrix(
        y_test,
        y_pred
    )

    ConfusionMatrixDisplay(cm).plot()

    plt.savefig(
        os.path.join(
            OUTPUT_DIR,
            "confusion_matrix.png"
        ),
        dpi=300,
        bbox_inches="tight"
    )

    plt.close()

    with open(
        os.path.join(
            OUTPUT_DIR,
            "metrics.txt"
        ),
        "w"
    ) as f:

        f.write(f"Accuracy : {accuracy:.4f}\n")
        f.write(f"Precision: {precision:.4f}\n")
        f.write(f"Recall   : {recall:.4f}\n")
        f.write(f"F1 Score : {f1:.4f}\n")
        f.write(f"ROC AUC  : {roc:.4f}\n")

    print("\nEvaluation completed.")
    print(f"Saved results in {OUTPUT_DIR}")