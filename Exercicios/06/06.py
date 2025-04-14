# %%
import pandas as pd
#%%
df = pd.read_csv("../data/clientes.csv")
#%%
# 06.01 - Qual a quantidade média de redes sociais dos usuários? E a Variância? E o máximo?

df["qtRedesSociais"] = (df["flEmail"] + df["flTwitch"] + df["flYouTube"] + df["flBlueSky"] + df["flInstagram"])
media_redes_sociais = df["qtRedesSociais"].mean()
variancia_redes_sociais = df["qtRedesSociais"].var()
valor_maximo_redes_socais = df["qtRedesSociais"].max()

print(f"A média de redes sociais é de: {media_redes_sociais}")
print(f"A variância é: {variancia_redes_sociais}")
print(f"O valor máximo de redes sociais é: {valor_maximo_redes_socais}")

# %%
# 06.02 - Quais são os usuários que mais fizeram transações? Considere os 10 primeiros.

df_transacoes = pd.read_csv("../data/transacoes.csv")

top_clientes = (df_transacoes.groupby(by=["idCliente"])["idTransacao"]
   .count()
   .sort_values(ascending=False)
   .head(10))

lista_clientes = top_clientes.index.tolist()

print(f"Os usuários que mais fizeram transações é o: {lista_clientes}")

#%%
# 06.03 - Qual usuário teve maior quantidade de pontos debitados?

quantidadePontos = (df_transacoes[df_transacoes["qtdePontos"] < 0]
                        .groupby(by=["idCliente"])["qtdePontos"]
                        .sum()
                        .sort_values(ascending=True)
                        .head(1))

cliente_top_debito = quantidadePontos.index[0]
pontos_debitados = quantidadePontos.iloc[0]

print(f"O usuário que teve a maior quantidade de pontos debitados foi o cliente: {cliente_top_debito} com {pontos_debitados} pontos.")

#%%
# 06.04 - Quem teve mais transações de Streak?

df_transacoes_produto = pd.read_csv("../data/transacao_produto.csv")
df_transacoes_produto.head()

df_produtos = pd.read_csv("../data/produtos.csv")
df_produtos.head()

cliente_df_transacoes_produto = df_transacoes.merge(
    df_transacoes_produto,
    on="idTransacao",
    how="left",
)[['idTransacao', "idCliente", "idProduto"]]

df_full = cliente_df_transacoes_produto.merge(
    df_produtos,
    on=['idProduto'],
    how='left',
)

df_full = df_full[df_full["descProduto"]=="Presença Streak"]

(df_full.groupby(by=["idCliente"])["idTransacao"]
        .count()
        .sort_values(ascending=False)
        .head(1)
)

df_produtos = df_produtos[df_produtos["descProduto"]=="Presença Streak"]

(df_transacoes.merge(df_transacoes_produto, on=["idTransacao"], how="left")
           .merge(df_produtos, on=["idProduto"], how="inner")
           .groupby(by="idCliente")["idTransacao"]
           .count()
           .sort_values(ascending=False)
           .head(1)
)

# %%
# 06.05 - Qual a média de transações / dia?

df_transacoes['dtCriacao'] = pd.to_datetime(df_transacoes['dtCriacao'])

transacoes_dia = (
    df_transacoes.groupby(df_transacoes['dtCriacao'].dt.date)["idTransacao"]
    .count()
)

media_transacoes_por_dia = transacoes_dia.mean()

print(f"A média de transações por dia foi de {media_transacoes_por_dia:.2f}.")

# %%

# 06.06 - Como podemos calcular as estatísticas descritivas dos pontos das transações de cada usuário?

(df_transacoes.groupby(by=['idCliente'], as_index=False)['qtdePontos']
           .describe())