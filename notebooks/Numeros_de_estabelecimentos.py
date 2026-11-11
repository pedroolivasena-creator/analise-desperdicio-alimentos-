import pandas as pd

df = pd.read_excel('dados_desperdicio_de_alimentos.xlsx')

print('DIMENSÕES DA TABELA:')
print(df.shape)

print('\nNOMES DAS COLUNAS:')
print(df.columns.tolist())

print('\nINFORMAÇÕES DOS DADOS:')
df.info()

print('\nVALORES AUSENTES:')
print(df.isnull().sum())

print('\nESTATÍSTICAS:')
print(df.describe())

#valores nulos
print('Total de valores nulos:', df.isnull().sum().sum())

# Contar duplicadas antes da remoção
print('Duplicadas antes:', df.duplicated().sum())

# Remover linhas duplicadas
df = df.drop_duplicates()

# Contar duplicadas depois da remoção
print('Duplicadas depois:', df.duplicated().sum())

# Mostrar tabela tratada
print(df.to_string())


# Agrupar os alimentos e somar a compra
top_50 = (
    df.groupby('Categoria')['Quantidade comprada (kg)']
    .sum()
    .sort_values(ascending=False)
    .head(7)
    .reset_index()
)

# Renomear as colunas
top_50.columns = ['Alimento', 'Total compra(kg)']

# Exibir resultado
print(top_50.to_string(index=False))

# Salvar em Excel
top_50.to_excel('top_50_alimentos_desperdicados.xlsx', index=False)
