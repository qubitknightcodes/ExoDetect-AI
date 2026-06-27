import numpy as np


def remove_nan(signal):
    signal = np.nan_to_num(signal)
    return signal


def smooth_signal(signal, window=5):
    kernel = np.ones(window) / window
    return np.convolve(signal, kernel, mode="same")


def normalize_flux(signal):
    signal = np.asarray(signal)

    return (
        signal - np.median(signal)
    ) / (np.std(signal) + 1e-8)