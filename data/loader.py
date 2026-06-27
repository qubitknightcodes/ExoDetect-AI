import numpy as np
import pandas as pd


def load_kepler_data(path):
    """
    Load Kepler/TESS light curve dataset.

    Assumes:
    Column 0 -> Label (0/1)
    Remaining columns -> Flux values
    """

    df = pd.read_csv(path)

    y = df.iloc[:, 0].values.astype(np.int32)
    X = df.iloc[:, 1:].values.astype(np.float32)

    return X, y


def normalize_light_curves(X):
    """
    Normalize each light curve independently.
    """

    mean = X.mean(axis=1, keepdims=True)
    std = X.std(axis=1, keepdims=True) + 1e-8

    return (X - mean) / std


def reshape_for_cnn(X):
    """
    CNN expects:
    (samples, timesteps, channels)
    """

    return X[..., np.newaxis]