import tensorflow as tf
from tensorflow.keras import layers, models

def build_cnn(input_shape):
    model = models.Sequential()

    model.add(layers.Conv1D(32, 5, activation='relu', input_shape=input_shape))
    model.add(layers.MaxPooling1D(2))

    model.add(layers.Conv1D(64, 5, activation='relu'))
    model.add(layers.MaxPooling1D(2))

    model.add(layers.Conv1D(128, 3, activation='relu'))
    model.add(layers.GlobalAveragePooling1D())

    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dropout(0.3))

    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(
        optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
    )

    return model