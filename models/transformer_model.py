import tensorflow as tf
from tensorflow.keras import layers


def transformer_block(x, head_size=64, num_heads=4, ff_dim=128):
    attention = layers.MultiHeadAttention(
        num_heads=num_heads,
        key_dim=head_size
    )(x, x)

    x = layers.Add()([x, attention])
    x = layers.LayerNormalization()(x)

    ff = layers.Dense(ff_dim, activation="relu")(x)
    ff = layers.Dense(x.shape[-1])(ff)

    x = layers.Add()([x, ff])
    x = layers.LayerNormalization()(x)

    return x


def build_transformer(input_shape):

    inputs = tf.keras.Input(shape=input_shape)

    x = layers.Dense(64)(inputs)

    x = transformer_block(x)
    x = transformer_block(x)

    x = layers.GlobalAveragePooling1D()(x)

    x = layers.Dense(64, activation="relu")(x)
    x = layers.Dropout(0.3)(x)

    outputs = layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.Model(inputs, outputs)

    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )

    return model