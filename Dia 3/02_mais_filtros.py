# %%
import pandas as pd

# %%

df = pd.read_csv("../data/transacao_produto.csv")
df.head()
df.head(1)

# %%

filtro = (df["idProduto"] == 5) | (df["idProduto"] == 11)
df[filtro]

# %%

df[df["idProduto"].isin([5, 11])]

# %%

clientes = pd.read_csv("../data/clientes.csv")	

clientes[~clientes["dtCriacao"].isna()]