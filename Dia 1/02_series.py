# %%

import pandas as pd

# %%

idades = [
          32, 38, 30, 30, 31, 35, 25,
          29, 31, 37, 27, 23, 36, 33, 32
        ]

# %%

diffs = 0
media = sum(idades) / len(idades)
for i in idades:
    diffs += (i - media) ** 2
variancia = diffs / (len(idades) - 1)

print(f'Variância: {variancia}')

# %%

series_idades = pd.Series(idades)
series_idades

# %%

media_idades = series_idades.mean()
var_idades = series_idades.var()
summary_idades = series_idades.describe()
summary_idades