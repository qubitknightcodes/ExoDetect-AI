import tensorflow as tf


def get_callbacks(model_name):
    return [
        tf.keras.callbacks.EarlyStopping(
            monitor="val_loss",
            patience=10,
            restore_best_weights=True
        ),

        tf.keras.callbacks.ModelCheckpoint(
            filepath=f"models/{model_name}.keras",
            save_best_only=True,
            monitor="val_loss"
        ),

        tf.keras.callbacks.ReduceLROnPlateau(
            monitor="val_loss",
            factor=0.5,
            patience=5,
            min_lr=1e-6
        )
    ]