import statistics
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html

df = pd.read_excel(
    'dados_desperdicio_de_alimentos.xlsx',
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

df = pd.read_excel('dados_desperdicio_de_alimentos.xlsx')

# Agrupar os alimentos e somar o desperdício
top_50 = (
    df.groupby('Produto')['Quantidade desperdiçada (kg)']
    .sum()
    .sort_values(ascending=False)
    .head(50)
    .reset_index()
)

# Renomear as colunas
top_50.columns = ['Alimento', 'Total desperdiçado (kg)']

# Exibir resultado
print(top_50.to_string(index=False))

# Salvar em Excel
top_50.to_excel('top_50_alimentos_desperdicados.xlsx', index=False)

# Grafico de pizza
desperdicio = (
    df.groupby("Produto")["Quantidade desperdiçada (kg)"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_pie = px.pie(
    desperdicio,
    values="Quantidade desperdiçada (kg)",
    names="Produto",
    title="Top 10 alimentos mais desperdiçados",
    hole=0.3
)

fig_pie.show()

#media desperdiçada
media = statistics.mean(df['Quantidade desperdiçada (kg)'])

print(f'Média desperdiçada: {media:.2f} kg')