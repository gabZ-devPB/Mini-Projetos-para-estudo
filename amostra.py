import pandas as pd

df_viagens = pd.read_csv('arquivos/2025_Viagem.csv', encoding='Windows-1252', sep=';', decimal=',')
amostra = df_viagens.sample(5000, random_state=42)
amostra.to_csv("viagens_amostra.csv", index=False)
