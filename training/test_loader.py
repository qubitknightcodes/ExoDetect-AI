from data.loader import (
    load_kepler_data,
    normalize_light_curves,
    reshape_for_cnn,
)

X, y = load_kepler_data("data/raw/exoplanet.csv")

X = normalize_light_curves(X)
X = reshape_for_cnn(X)

print("Shape:", X.shape)
print("Labels:", y.shape)