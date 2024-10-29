import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# Leitura do arquivo CSV
file_path = "test.csv"  # Substitua pelo caminho do seu arquivo
df = pd.read_csv(file_path)

# Mostrar as primeiras 5 linhas (head) e as últimas 5 linhas (tail)
st.write("Head do dataset:")
st.dataframe(df.head())  # Exibir como um DataFrame interativo

st.write("\nTail do dataset:")
st.dataframe(df.tail())  # Exibir como um DataFrame interativo

# Exibir o tamanho do dataset (número de linhas e colunas)
st.write("\nTamanho do dataset (linhas, colunas):")
st.write(df.shape)

# Estatísticas descritivas
st.write("\nEstatísticas descritivas:")
st.write(df.describe())

# Contar NaN em cada coluna
nan_counts = df.isna().sum()

# Contar nulos em cada coluna
null_counts = df.isnull().sum()

# Contar valores não nulos em cada coluna
not_null_counts = df.notna().sum()

# Calcular a porcentagem de nulos
percentage_null = (null_counts / len(df)) * 100

# Calcular correlações
correlations = {}
for i in range(0, 62):  # Alterado para ir de x0 a x61
    if f'x{i}' in df.columns:  # Verifique se a coluna existe
        correlations[f'x{i}'] = df[f'x{i}'].corr(df['y'])  # Substitua 'y' pelo nome real da sua coluna

# Ordenar as correlações em ordem decrescente
sorted_correlations = dict(sorted(correlations.items(), key=lambda item: item[1], reverse=True))

# Criar um DataFrame para mostrar os resultados de NaN e null
missing_data = pd.DataFrame({
    'NaN Counts': nan_counts,
    'Null Counts': null_counts,
    'Not Null Counts': not_null_counts,
    'Percentage Nulls (%)': percentage_null,
    'Correlation with y': [correlations.get(f'x{i}', None) for i in range(0, 62)]  # Usa get para evitar erro se não existir
})

# Título da seção de dados ausentes
st.write("Quantidade de NaN, nulos e não nulos em cada coluna:")
st.dataframe(missing_data)

# Resumo das melhores correlações
st.write("\nResumo das Melhores Correlações:")
best_correlations = sorted_correlations.items()

# Top 10 correlações positivas (maiores)
top_positive = [(k, v) for k, v in best_correlations if v > 0][:10]

# Top 10 correlações negativas (menores)
top_negative = sorted(((k, v) for k, v in correlations.items() if v < 0), key=lambda item: item[1])[:10]

# Exibir correlações positivas
st.write("Top 10 Correlações Positivas:")
st.write(pd.DataFrame(top_positive, columns=['Variável', 'Correlação']))

# Exibir correlações negativas
st.write("Top 10 Correlações Negativas:")
st.write(pd.DataFrame(top_negative, columns=['Variável', 'Correlação']))

# Criar gráfico interativo de barras
fig = go.Figure()

# Adicionando barras ao gráfico
fig.add_trace(go.Bar(
    x=list(sorted_correlations.keys()),
    y=list(sorted_correlations.values()),
    marker_color='indigo'  # Você pode mudar a cor como desejar
))

# Configurar layout do gráfico
fig.update_layout(
    title='Correlação entre Variáveis X e Y (do maior para o menor)',
    xaxis_title='Variáveis X',
    yaxis_title='Correlação',
    showlegend=False
)

# Exibir gráfico
st.plotly_chart(fig)

# Criar a matriz de correlação
correlation_matrix = df.corr()

# Exibir a matriz de correlação
st.write("Matriz de Correlação:")
fig_matrix = px.imshow(correlation_matrix, 
                        labels=dict(x="Variáveis", y="Variáveis", color="Correlação"),
                        color_continuous_scale='Viridis', 
                        title='Matriz de Correlação')
st.plotly_chart(fig_matrix)
