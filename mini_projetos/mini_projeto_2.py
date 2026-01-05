# 🔹 Mini-Projeto 2: Viagens mais caras

import pandas as pd

viagens_df = pd.read_csv('arquivos/2025_Viagem.csv', encoding='Windows-1252', sep=';', decimal=',')
pd.set_option('display.max_columns', 3)
pd.set_option('display.float_format', '{:.2f}'.format)
viagens_df['Despesas'] = (viagens_df['Valor diárias'] + viagens_df['Valor outros gastos'] + viagens_df['Valor passagens']) - viagens_df['Valor devolução']

viagens_mais_caras = viagens_df[['Cargo', 'Destinos', 'Despesas']].sort_values(by='Despesas', ascending=False).head(10).fillna('Sem Informacoes')
print(viagens_mais_caras)

valor_medio_viagens = viagens_mais_caras['Despesas'].mean()
print(valor_medio_viagens)

valor_acima_da_media = viagens_mais_caras[viagens_mais_caras['Despesas'] > valor_medio_viagens]
print(valor_acima_da_media)

