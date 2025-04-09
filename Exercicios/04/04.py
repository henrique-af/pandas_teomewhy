# %% 

import pandas as pd

# %%

df_clientes = pd.read_csv("../../data/clientes.csv")


# %%

# 04.01 - Quantos clientes tem vínculo com a Twitch?
count = df_clientes[df_clientes["flTwitch"] == 1].shape[0]
print(count)
# 820


# %%

# 04.02 - Quantos clientes tem um saldo de pontos maior que 1000?
count = df_clientes[df_clientes["qtdePontos"] > 1000].shape[0]
print(count)
# 271

# %%

# 04.03 - Quantas transações ocorreram no dia 2025-02-01?

df_transacoes = pd.read_csv("../../data/transacoes.csv")
df_transacoes['dtCriacao'] = pd.to_datetime(df_transacoes['dtCriacao'])

count = df_transacoes[
    (df_transacoes['dtCriacao'] >= '2025-02-01') &
    (df_transacoes['dtCriacao'] < '2025-02-02')
].shape[0]

print(f"No dia 2025-02-01 tivemos {count} transações")

# 6