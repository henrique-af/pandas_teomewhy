# %%

import pandas as pd

idades = [
          32, 38, 30, 30, 31, 35, 25,
          29, 31, 37, 27, 23, 36, 33, 32
        ]

series_idades = pd.Series(idades)
series_idades


# %%
series_idades = series_idades.sort_values()

series_idades

series_idades.iloc[-1]

series_idades.iloc[:3]

# %%

idades = [
    32, 38, 30, 30, 31,
    35, 25, 29, 31, 37,
    27, 23, 36, 33, 39,
]

nomes = [
    "Téo", "Maria", "Jose", "Luis", "Ana",
    "Nah", "Dani", "Mah", "Fer", "Nanda",
    "Naty", "Nih", "Pedro", "Kozato", "Kozato",
]


series_idades = pd.Series(idades, index=nomes)
series_idades
# %%

series_idades.loc["Téo"]