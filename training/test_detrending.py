import numpy as np
import matplotlib.pyplot as plt

from features.detrending import Detrender

time = np.linspace(0, 20, 1000)

trend = 1 + 0.02 * np.sin(time)

transit = np.ones_like(time)
transit[450:470] = 0.99

flux = trend * transit

detrender = Detrender()

trend_est, flat = detrender.detrend(time, flux)

print("Median:", np.median(flat))
print("Minimum:", flat.min())

plt.figure(figsize=(10,4))
plt.plot(time, flux, label="Original")
plt.plot(time, trend_est, label="Estimated Trend")
plt.legend()
plt.show()

plt.figure(figsize=(10,4))
plt.plot(time, flat)
plt.title("Detrended Light Curve")
plt.show()