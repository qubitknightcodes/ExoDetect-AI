import joblib
import numpy as np
from xgboost import XGBClassifier

from data.loader import load_kepler_data
from features.physics_features import extract_physics_features

# Load data
X, y = load_kepler_data("data/raw/exoplanet.csv")

# Extract engineered features
physics_X = np.array([
    extract_physics_features(signal)
    for signal in X
])

# Train model
model = XGBClassifier(
    n_estimators=200,
    max_depth=6,
    learning_rate=0.05,
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    eval_metric="logloss"
)

model.fit(physics_X, y)

# Save model
joblib.dump(model, "models/xgboost_model.pkl")

print("XGBoost model saved!")