import numpy as np


class EnsemblePredictor:

    def __init__(self, cnn_model, transformer_model, xgb_model):
        self.cnn = cnn_model
        self.transformer = transformer_model
        self.xgb = xgb_model

    def predict(self, signal, physics_features):

        cnn_prob = float(
            self.cnn.predict(signal, verbose=0)[0][0]
        )

        transformer_prob = float(
            self.transformer.predict(signal, verbose=0)[0][0]
        )

        xgb_prob = float(
            self.xgb.predict_proba(
                physics_features.reshape(1, -1)
            )[0][1]
        )

        probabilities = np.array([
            cnn_prob,
            transformer_prob,
            xgb_prob
        ])

        probability = probabilities.mean()

        confidence = 1.0 - probabilities.std()

        return {
            "cnn": cnn_prob,
            "transformer": transformer_prob,
            "xgboost": xgb_prob,
            "probability": probability,
            "confidence": confidence
        }