import numpy as np
import matplotlib.pyplot as plt

from features.bls_search import BLSSearch

time = np.linspace(0, 30, 3000)

period = 5

flux = np.ones_like(time)

for i in np.arange(0, 30, period):
    mask = np.abs(time - i) < 0.12
    flux[mask] = 0.99

search = BLSSearch()

best_period, power = search.find_period(
    time,
    flux,
)

print(f"Detected Period : {best_period:.3f} days")
print(f"BLS Power       : {power:.3f}")

plt.plot(time, flux)
plt.title("Synthetic Transit")
plt.show()