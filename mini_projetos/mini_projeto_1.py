# 🔹 Mini-Projeto 1: Análise de gastos por cargo

import pandas as pd

# Leitura do arquivo CSV
# - encoding ajustado para evitar erros de caracteres
# - separador ';' padrão do Portal da Transparência
viagens_df = pd.read_csv(
    'arquivos/2025_Viagem.csv',
    encoding='Windows-1252',
    sep=';',
    decimal=',',
)

# Formatação dos números decimais para melhor visualização
pd.set_option('display.float_format', '{:.2f}'.format)

# Visualização inicial dos dados (análise exploratória)
valores_iniciais = viagens_df.head()
print(valores_iniciais)

# Criação da coluna "Despesas"
# Soma todos os gastos da viagem e subtrai possíveis devoluções
viagens_df['Despesas'] = (viagens_df['Valor diárias'] + viagens_df['Valor outros gastos'] + viagens_df['Valor passagens']) - viagens_df['Valor devolução']

# Agrupa os dados por cargo e calcula o total de despesas
despesas_por_cargo = (
    viagens_df
    .groupby('Cargo')['Despesas']
    .sum()
    .reset_index()
)

print(despesas_por_cargo)

# Filtra os cargos que gastaram mais de 50 mil reais
cargos_gastos_50mil = despesas_por_cargo[
    despesas_por_cargo['Despesas'] > 50_000
]

print(cargos_gastos_50mil)

# Ordena os cargos do maior para o menor gasto
despesas_por_cargo_decrescente = (
    despesas_por_cargo
    .sort_values(by='Despesas', ascending=False)
)

print(despesas_por_cargo_decrescente)

# Seleciona os cargos com maiores gastos
mais_gastos = despesas_por_cargo_decrescente.head()

print(mais_gastos)
