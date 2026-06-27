import numpy as np

from features.phase_folding import PhaseFolder
from features.transit_analysis import TransitAnalyzer

time = np.linspace(0, 30, 3000)

flux = np.ones_like(time)

period = 5

for i in range(0, 30, period):
    mask = np.abs(time - i) < 0.15
    flux[mask] = 0.99

folder = PhaseFolder(period)

phase, folded_flux = folder.fold(time, flux)

analyzer = TransitAnalyzer()

results = analyzer.analyze(phase, folded_flux)

print("\nTransit Parameters")
print("------------------")
for key, value in results.items():
    print(f"{key}: {value}")