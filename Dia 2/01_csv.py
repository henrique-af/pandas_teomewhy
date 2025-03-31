#%%
import pandas as pd
#%%

df = pd.read_csv('./data/clientes.csv')
df

#%%

df.to_excel('./data/clientes.xlsx', index=False)	

# %%

df2 = pd.read_excel('./data/clientes.xlsx')
df2

#%%