# 🔹 Mini-Projeto 1: Análise de gastos por cargo

import pandas as pd

viagens_df = pd.read_csv('arquivos/2025_Viagem.csv', encoding='Windows-1252', sep=';', decimal=',', engine='python', on_bad_lines='skip')
pd.set_option('display.float_format', '{:.2f}'.format)

valores_inicias = viagens_df.head()
print(valores_inicias)

viagens_df['Despesas'] = (viagens_df['Valor diárias'] + viagens_df['Valor outros gastos'] + viagens_df['Valor passagens']) - viagens_df['Valor devolução']
despesas_por_cargo = viagens_df.groupby('Cargo')['Despesas'].sum().reset_index()
print(despesas_por_cargo)

cargos_gastos_50mil = despesas_por_cargo[despesas_por_cargo['Despesas'] > 50_000]
print(cargos_gastos_50mil)

despesas_por_cargo_decrescente = viagens_df.groupby('Cargo')['Despesas'].sum().reset_index().sort_values(by='Despesas', ascending=False)
print(despesas_por_cargo_decrescente)

mais_gastos = despesas_por_cargo_decrescente.head()
print(mais_gastos)