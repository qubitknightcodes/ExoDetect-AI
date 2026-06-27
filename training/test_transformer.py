import numpy as np

from models.transformer_model import build_transformer

model = build_transformer((3197, 1))

model.summary()

dummy = np.random.rand(4, 3197, 1)

pred = model.predict(dummy)

print(pred)