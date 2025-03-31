# %%

# 03.01 - Quantas linhas há no arquivo clientes.csv ?
# 03.02 - Quantas colunas do tipo int há no arquivo transacoes.csv ?
# 03.03 - Quantas colunas do tipo object há no arquivo produtos.csv ?
# 03.04 - Qual o id do cliente no índice 4 no arquivo clientes.csv ?
# 03.05 - Qual o saldo de pontos do cliente na 10a posição (sem ordenar) do arquivo clientes.csv ?

import pandas as pd

# %%

df_clientes = pd.read_csv("../data/clientes.csv")
df_clientes

print(f"Linhas no clientes.csv: {df_clientes.shape[0]}") 
# Linhas no clientes.csv: 2436

# %%

df_transacoes = pd.read_csv("../data/transacoes.csv")
colunas_int = df_transacoes.select_dtypes(include=["int64"]).columns
# Index(['qtdePontos'], dtype='object')

print(f"Colunas int no transacoes.csv: {len(colunas_int)}") 

# %%

df_produtos = pd.read_csv("../data/produtos.csv")
colunas_object = df_produtos.select_dtypes(include="object").columns
# Index(['descProduto'], dtype='object')

print(f"Colunas object no produtos.csv: {len(colunas_object)}") 

# %%

indice_4 = df_clientes["idCliente"].loc[4]
print(f"Id do cliente no indice 4: {indice_4}")
# 00684343-40b5-4ce7-b2e8-71a5340973bf

# %%

saldo_pontos = df_clientes["qtdePontos"].iloc[9]
print(f"O saldo de pontos do cliente na posição 10 é: {saldo_pontos}")
# 119