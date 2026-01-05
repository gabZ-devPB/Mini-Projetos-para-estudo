# 🔹 Mini-Projeto 2: Viagens mais caras

import pandas as pd

# Lê o arquivo CSV com os dados de viagens
# encoding e separador ajustados ao padrão dos dados do Portal da Transparência
viagens_df = pd.read_csv(
    'arquivos/2025_Viagem.csv',
    encoding='Windows-1252',
    sep=';',
    decimal=','
)

# Configurações de exibição do pandas
# Mostra no máximo 3 colunas na impressão
pd.set_option('display.max_columns', 3)

# Formata números decimais com duas casas
pd.set_option('display.float_format', '{:.2f}'.format)

# Cria a coluna "Despesas" somando todos os gastos
# e subtraindo possíveis devoluções
viagens_df['Despesas'] = (viagens_df['Valor diárias'] + viagens_df['Valor outros gastos'] + viagens_df['Valor passagens']) - viagens_df['Valor devolução']

# Seleciona apenas as colunas relevantes
# Ordena pelas despesas em ordem decrescente
# Retorna as 10 viagens mais caras
# Substitui valores nulos por "Sem Informações"
viagens_mais_caras = (
    viagens_df[['Cargo', 'Destinos', 'Despesas']]
    .sort_values(by='Despesas', ascending=False)
    .head(10)
    .fillna('Sem Informacoes')
)

# Exibe as 10 viagens mais caras
print(viagens_mais_caras)

# Calcula o valor médio das despesas das 10 viagens mais caras
valor_medio_viagens = viagens_mais_caras['Despesas'].mean()

# Exibe o valor médio
print(valor_medio_viagens)

# Filtra apenas as viagens cujo valor está acima da média
valor_acima_da_media = viagens_mais_caras[
    viagens_mais_caras['Despesas'] > valor_medio_viagens
]

# Exibe as viagens acima da média de gastos
print(valor_acima_da_media)


