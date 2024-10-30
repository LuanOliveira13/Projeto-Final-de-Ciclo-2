# Árvore de Decisão vs. Regressão Logística
Este projeto explora a eficácia de dois algoritmos de classificação, **Árvore de Decisão e Regressão Logística**, aplicados a um conjunto de dados financeiros. O objetivo é comparar o desempenho dos modelos em classificar os dados e selecionar o modelo que apresenta a melhor performance.

## Arquivos do Projeto 
1. **Modelos:**

- ```final_ciclo_2_decision_tree_teste_final.ipynb```: Notebook que constrói, otimiza e avalia um modelo de Árvore de Decisão com uma busca aleatória de hiperparâmetros.
- ```regressao_logistica_lending.ipynb```: Notebook que constrói e avalia um modelo de Regressão Logística.
  
2. **Relatórios de Análise Exploratória:**

- ```comparative_report.html```: Relatório gerado pelo Sweetviz, comparando características de diferentes conjuntos de dados.
- ```sweetviz_lending_report.html```: Análise detalhada do conjunto de dados de empréstimos.
- ```sweetviz_test_report.html```: Relatório Sweetviz sobre o conjunto de dados de teste.
- ```sweetviz_train_report.html```: Relatório Sweetviz sobre o conjunto de dados de treino.

3. **Visualização com Streamlit:**

- ```Dados_Streamlit.py```: Exibe estatísticas descritivas, análise de dados ausentes e correlações, e visualiza a matriz de correlação com gráficos interativos.
  
## Pré-requisitos
Certifique-se de ter as seguintes bibliotecas instaladas para executar os notebooks:

```pip install pandas numpy scikit-learn matplotlib sweetviz streamlit plotly ```

## Execução
1. **Exploração de Dados:**

Abra os arquivos HTML de relatórios do Sweetviz para entender melhor os dados antes de construir os modelos.

2. **Treinamento e Avaliação dos Modelos:**

Abra e execute os notebooks ```final_ciclo_2_decision_tree_teste_final.ipynb``` e ```regressao_logistica_lending.ipynb``` para treinar e avaliar os modelos de Árvore de Decisão e Regressão Logística, respectivamente.

3. **Visualização Interativa com Streamlit:**

- Para rodar o script Streamlit, execute:

```streamlit run Dados_Streamlit.py```

- O script exibe as estatísticas e visualizações do dataset, incluindo correlações e uma matriz de correlação interativa.

## Conclusão
Este projeto oferece uma abordagem prática para comparar algoritmos de aprendizado de máquina, desde a análise exploratória até a avaliação de performance. A escolha do melhor modelo dependerá das métricas de avaliação e do contexto dos dados.
