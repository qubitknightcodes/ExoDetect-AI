import numpy as np
from scipy.signal import find_peaks


def transit_depth(signal):
    """
    Maximum transit depth.
    """
    return np.min(signal)


def flux_variance(signal):
    """
    Variability of stellar flux.
    """
    return np.var(signal)


def count_transit_candidates(signal):
    """
    Count significant dips in the light curve.
    """
    peaks, _ = find_peaks(-signal, distance=20)
    return len(peaks)


def flux_asymmetry(signal):
    """
    Average change between consecutive observations.
    """
    return np.mean(np.diff(signal))


def signal_entropy(signal, bins=50):
    """
    Shannon entropy of the light curve.
    """
    hist, _ = np.histogram(signal, bins=bins, density=True)
    hist = hist + 1e-8

    return -np.sum(hist * np.log(hist))


def extract_physics_features(signal):
    """
    Extract all engineered physics features.
    """

    return np.array([
        transit_depth(signal),
        flux_variance(signal),
        count_transit_candidates(signal),
        flux_asymmetry(signal),
        signal_entropy(signal)
    ])