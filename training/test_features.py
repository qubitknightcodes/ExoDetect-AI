import numpy as np

from features.physics_features import extract_physics_features

signal = np.random.normal(size=3197)

features = extract_physics_features(signal)

print(features)
print(features.shape)