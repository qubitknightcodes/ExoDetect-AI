import numpy as np
import matplotlib.pyplot as plt

from features.phase_folding import PhaseFolder

time = np.linspace(0, 30, 3000)

period = 5

flux = np.ones_like(time)

for i in range(0, 30, period):
    mask = np.abs(time - i) < 0.15
    flux[mask] = 0.99

folder = PhaseFolder(period=period)

phase, folded_flux = folder.fold(time, flux)

plt.figure(figsize=(8,4))
plt.scatter(phase, folded_flux, s=5)
plt.xlabel("Phase")
plt.ylabel("Flux")
plt.title("Phase Folded Light Curve")
plt.show()