import numpy as np


class SignalSignificance:

    def compute(self, depth, noise):

        # Reject physically unrealistic transit depths
        if depth > 0.05:
            return {
                "snr": 0.0,
                "confidence": 0.0
            }

        snr = depth / (noise + 1e-10)

        confidence = 1 - np.exp(-snr / 10)

        confidence = np.clip(confidence, 0, 1)

        return {
            "snr": float(snr),
            "confidence": float(confidence),
        }