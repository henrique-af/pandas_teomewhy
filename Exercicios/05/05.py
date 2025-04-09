# %% 
import pandas as pd
import numpy as np
#%%

df_clientes = pd.read_csv("../../data/clientes.csv")
df_clientes.head()

#%%

# 05.01 - Crie uma coluna nova “twitch_points” que e resultado da multiplicação do saldo de pontos e a marcação da twitch
df_clientes["twitch_points"] = df_clientes["qtdePontos"] * df_clientes["flTwitch"]
df_clientes.head()
# %%

#05.02 - Aplique o log na coluna de saldo de pontos, criando uma coluna nova
df_clientes["log_pontos"] = np.log(df_clientes["qtdePontos"] + 1)
df_clientes.head()

#%%

#05.03 - Crie uma coluna que sinalize se a pessoa tem vínculo com alguma (qualquer uma) plataforma de rede social.
df_clientes["fl_social"] = df_clientes[["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]].sum(axis=1)
df_clientes.head()

# %%

#05.04 - Qual é o id de cliente que tem maior saldo de pontos? E o menor?
df_clientes.loc[df_clientes["qtdePontos"].idxmax(), "idCliente"], df_clientes.loc[df_clientes["qtdePontos"].idxmin(), "idCliente"]

#%%

#05.05 - Selecione a primeira transação diária de cada cliente.

transacoes = pd.read_csv("../../data/transacoes.csv")
transacoes.head()

transacoes["data"] = pd.to_datetime(transacoes["dtCriacao"]).dt.date
transacoes = transacoes.sort_values("dtCriacao")

# %%

first = transacoes.drop_duplicates(keep="first", subset=["idCliente", "data"])
last = transacoes.drop_duplicates(keep="last", subset=["idCliente", "data"])

pd.concat([last, first])
# %%
