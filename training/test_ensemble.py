import numpy as np

probs = np.array([0.91, 0.87, 0.89])

print("Mean:", probs.mean())
print("Confidence:", 1 - probs.std())