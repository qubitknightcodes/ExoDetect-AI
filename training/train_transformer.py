from models.transformer_model import build_transformer
from training.callbacks import get_callbacks
from training.trainer import prepare_data

X_train, X_test, y_train, y_test = prepare_data(
    "data/raw/exoplanet.csv"
)

model = build_transformer(
    input_shape=X_train.shape[1:]
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=50,
    batch_size=32,
    callbacks=get_callbacks("transformer_model"),
    verbose=1
)

loss, accuracy = model.evaluate(
    X_test,
    y_test
)

print(f"Test Accuracy: {accuracy:.4f}")