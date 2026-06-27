import numpy as np
from scipy.stats import median_abs_deviation


def remove_nan(time, flux):
    mask = np.isfinite(time) & np.isfinite(flux)
    return time[mask], flux[mask]


def sigma_clip(flux, sigma=5):
    median = np.median(flux)
    mad = median_abs_deviation(flux)

    if mad == 0:
        return flux

    z = 0.6745 * (flux - median) / mad
    mask = np.abs(z) < sigma

    return flux[mask], mask


def normalize_flux(flux):
    median = np.median(flux)
    return flux / median


def smooth_signal(flux, window=7):
    kernel = np.ones(window) / window
    return np.convolve(flux, kernel, mode="same")


def estimate_noise(flux):
    return np.std(flux - np.median(flux))