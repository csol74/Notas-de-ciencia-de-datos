import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
# leer CSV con separador y decimal correcto
df = pd.read_csv("numero8.csv", sep=";", decimal=",")
# quitar primera fila
image = df.iloc[1:]
print(image)
plt.imshow(image, cmap='gray', vmin=0, vmax=1)
plt.axis('off')
plt.show()
