from utils.fits_loader import FITSLoader

from features.signal_processing import (
    remove_nan,
    sigma_clip,
    normalize_flux,
    smooth_signal,
    estimate_noise,
)

from features.detrending import Detrender
from features.bls_search import BLSSearch
from features.phase_folding import PhaseFolder
from features.transit_analysis import TransitAnalyzer
from features.significance import SignalSignificance

class Detector:

    def __init__(self):

        self.loader = FITSLoader()

        self.detrender = Detrender()

        self.bls = BLSSearch()

        self.analyzer = TransitAnalyzer()

        self.significance = SignalSignificance()

    def detect(self, fits_path):

        time, flux = self.loader.load(fits_path)

        time, flux = remove_nan(time, flux)

        flux, mask = sigma_clip(flux)

        time = time[mask]

        flux = normalize_flux(flux)

        noise = estimate_noise(flux)

        flux = smooth_signal(flux)

        trend, flux = self.detrender.detrend(
            time,
            flux,
        )

        period, power = self.bls.find_period(
            time,
            flux,
        )

        folder = PhaseFolder(period)

        phase, folded_flux = folder.fold(
            time,
            flux,
        )

        physics = self.analyzer.analyze(
            phase,
            folded_flux,
        )

        stats = self.significance.compute(
            physics["transit_depth"],
            noise,
        )

        return {
            "period": period,
            "bls_power": power,
            "noise": float(noise),
            **physics,
            **stats,
        }