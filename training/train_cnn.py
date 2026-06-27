import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from models.cnn_model import build_cnn
from training.callbacks import get_callbacks
from training.trainer import prepare_data

X_train, X_test, y_train, y_test = prepare_data(
    "data/raw/exoplanet.csv"
)

model = build_cnn(
    input_shape=X_train.shape[1:]
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=get_callbacks("cnn_model"),
    verbose=1
)

loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print(f"Test Accuracy: {accuracy:.4f}")

from evaluation.evaluate import evaluate_model

evaluate_model(
    model,
    X_test,
    y_test
)