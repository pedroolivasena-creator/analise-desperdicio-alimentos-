import pandas as pd

df = pd.read_excel(
    'LSPA - Produção, por período da safra e produto (toneladas).xlsx',
    header=1
)

print(df.head(10))
print(df.info())
df = df.dropna(how='all')
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