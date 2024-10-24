# Resumo

Encontrar os melhores modelos para predição da receita total e, por categoria, de uma grande varejista para o próximo mês e próximos 3 meses que possa ser aplicado repetidamente ao longo do ano, isto é, em um dado mês do ano obter as previsões de receita para os próximos meses fins de planejamento. Para isso são empregados modelos estatísticos de séries temporais (SARIMA) e modelos de aprendizado de máquina (XGBOOST). 

# Introdução

Importância do mercado de varejo no Brasil (referências)
Importância e o desafio de se fazer previsões (referências)
Descritivo da empresa e dos dados. Seguimento, produtos, categorias, receita total (pode ser anonimizada), número de clientes/mês etc.
Novamente o resumo mais detalhado.

Desse modo as contribuições desse trabalho são:
1. Fornecer uma base de dados real e pública sobre vendas no varejo que possa ser utilizada para outros trabalhos de estudo de previsões de venda no varejo.
2. Comparar modelos de previsão estatísticos e de aprendizado de máquina ao problema de previsões de vendas e receita no varejo. 
3. Fornecer ao final, um melhor modelo para previsão de receita no curto prazo (1-3 meses) e disponibilizá-lo de modo aberto.

# Referencial Teórico

Previsões de preços, demanda e receita vem sendo aplicados em diversos trabalhos.

A tabela 1, apresenta alguns dos trabalhos recentes na área.

| Referência | Resumo | Modelos Empregados | Resultados |
|----------------|-----------------|------------------------------------|------------------|
| Joao (2022) | Série de preços atacado (USA), 8000 instâncias | SARIMA  | MAPE = 0.21 |
| Maria, et al. (2023) | Série de vendas brinquedos (Taiwan), 20000 instâncias | SARIMA, RandomForest  | - |
| Daniel & Ana (2024) | Série demanda de lâmpadas (China), 1.5M instâncias | SARIMA, DeepLearning  | MAPE=0.22 |

> Comente 

A exemplo desses estudos, aqui, empregamos tanto modelos estatísticos (SARIMA) como de aprendizado de máquina (XGBoost).
(em cada seção alinhamos o conteúdo com o trabalho!)

# Modelos Estatísticos (um pouco menos de 1 página)

Dentre os diversos modelos estatísticos, os modelos SARIMA, encontram-se entre os modelos mais empregados. O modelo SARIMA é um modelo... \< definição, incluindo explicar o que é auto-regressivo e sazonalidade, pré-requisito desses modelos: estacionariedade \>. Incluir alguma figura que ilustre esses conceitos. Incluir umas 2-3 referências.

Os modelos SARIMA têm como parâmetros principais... \<explicar A(p, q, d) e S(p, q, d) \<

Neste estudo, além da análise exploratória, empregamos o pmdarima para obtenção dos melhores parâmetros. O pmdarima é um \<definir\>
(em cada seção alinhamos o conteúdo com o trabalho!)

# Modelos de Aprendizado de Máquina aplicados a Séries Temporais (um pouco menos de 1 página)

Modelos de Aprendizado de Máquina vem sendo aplicados com sucesso em uma série de problemas... (referências). Para séries temporais, em geral, aplicam-se modelos de aprendizado supervisionado... \<definir\>. Nesses modelos os dados das séries temporais são adaptados para fornecer um conjunto de dados de entrada X e y... \< explicar o procedimento das lags, preferencialmente incluindo uma figura \>. Incluir referência.

Neste estudo, empregamos ainda um aprendizado híbrido. O aprendizado híbrido consiste \< definir, explicar, aprendizado híbrido \>. Incluir referência.**NÃO VI ENTRETANTO, ISSO APLICADO NO SEU CÓDIGO**.

Dentre os diferentes modelos de aprendizado de máquina destacam os modelos *ensemble models*, que são \< definir, explicar, aprendizado híbrido \>. Esses modelos apresentam em geral um desempenho melhor que modelos mais simples. Neste estudo, optou-se pelo uso do modelo XGBOOST, por sua... (referências). 

# Metodologia

Descrevemos a seguir... 

## Pré-processamento dos Dados

Um único dataset de receitas:

| categoria 			| 1     | 2     | 3     | ... | 35   | 36   | 
|----------------------------------|------|------|------|------|------|------|	
| brinquedos 			| 200 | 100 | 50   | ... | 50   | 150 |
| escritório			| 200 | 100 | 50   | ... | 50   | 150 |
| ...  			| ...| ...| ...   | ... | ...   | ... |
| total   			| 200 | 100 | 50   | ... | 50   | 150 |

> Os dados estão muito, muito, desorganizados. Não faz sentido ter tantos arquivos quando, o que você precisa é uma tabela como essa.
> Crie uma tabela no mesmo formato para os produtos x preços e outra para produtos x receita. Essa acima, é a consolidação das duas mais a tabela de categoria dos produtos.

> Comente e justifique: exclusões, tratamento de dados nulos ou ‘zerados’, desafio. NÃO PARECE FAZER SENTIDO, TRATANDO-SE DE RECEITA AGREGADA, EXCLUIR PRODUTOS E SÓ FICAR COM OS 10 MAIS VENDIDOS.

## Análise Exploratória dos Dados

Gráfico de receita total ao longo do tempo
Gráfico de algumas categorias 
> Comente: sazonalidade, variações, maiores e menores, padrões de comportamento mensal, desafio de fazer as previsões etc.

Para cada série aplique a o teste adfuller sobre estacionariedade

| categoria 			| estacionariedade   | p-value | 
|----------------------------------|---------------------------|-----------|	
| brinquedos 			| estacionária | 0.01 |
| escritório			| estacionária | 0.04 |
| ...   			| ... | ... |
| total   			| estacionária | 0.05 |

> Comente

### ACF (Função de Autocorrelação) 
É utilizada para identificar a presença de sazonalidade em uma série temporal.
Gráfico das 15 categorias+total, 

| categoria 			| sazonalidade  |   
|----------------------------------|---------------------------| 	
| brinquedos 			| 12  |  
| escritório			| 12 |  
| limpeza			|  0  |  
| ...   			| ... | 
| total   			| 12 |  

0 = produtos de ano inteiro

> Comente
 
### PACF (Função de Autocorrelação Parcial) 
É empregada para identificar a ordem do componente autoregressivo (p) em um modelo ARIMA.
Gráfico das 15 categorias+total

| categoria 			| sazonalidade  |   
|----------------------------------|---------------------------| 	
| brinquedos 			| 1  |  
| escritório			| 2 |  
| limpeza			| 1 |  
| ... | ... |
| total   			| 3 |  

> Comente

### Métricas 

A seleção dos modelos estatísticos emprega a métrica AIC (referência), tradicional para seleção do melhor ajuste de modelos estatísticos e implementada pode padrão no pmdarima. Para avaliação dos resultados são empregadas as métricas de erro RMSE ( ), MAE ( ), MAPE ( ) e MedAE (Median Absolute error). O RMSE é empregado para comparar os modelos. As demais métricas são empregadas ao final para o entendimento do erro das previsões.

### Rolling Window

Utiliza-se aqui uma janela deslizante (rolling window) para dividir seus dados em conjuntos de treinamento e teste. Emprega-se a receita total para estimar o uso de previsões com base em 30 ou 36 meses. Busca-se empregar a maior quantidade de dados (36 meses), mas essa, pela limitação dos dados disponíveis, não permite a previsão de 12 meses.

Execuções pmdarima sobre receita total
```
  pmdarima 30 -> 1 (x 12 execuções) -> média AIC, média RMSE 
  pmdarima 36 -> 1 (x 6 execuções) -> média AIC, média RMSE
```

Mostrar a diferença, mas apesar do erro, vamos empregar 30 -> 1

### Pmdarima, SARIMA

O pmdarima otimiza somente os parâmetros A(p, q, d). Para os parâmetros S(p, q, d) emprega-se os valores obtidos de... (veja a analise que fez antes do ACF, espera-se empregar 0, aí é sazonal False, ou 12, com sazonal True).      Os valores A(p, q, d) são otimizados então entre... (ver os valores que emprega... padrão?, o PACF pode dar uma dica melhor e você pode empregar menos valores)

Pode justificar isso?
error_action='ignore',  # Ignora erros em combinações inválidas
suppress_warnings=True  # Suprime avisos

Execuções pmdarima sobre receita total e categorias
```
  Para cada categoria (inclui a total):
  	pmdarima 30 -> 1 (x 12 execuções) -> melhor modelo A(p,q,d) S(p,q,d)
```

Modelo escolhido, isso é mostrado nos resultados.  
Empregar A(p,q,d) S(p,q,d) 

| categoria 			| modelo  |   freq. |
|----------------------------------|---------------------------|------| 	
| brinquedos 			| A(1,1,0) S(0,12,0)  |  12 |
| escritório			| A(1,2,1) S(0,12,0) |  7 |
| limpeza			| A(1,2,1) S(0,0,0) |  9 |
| ...| ... |...|
| total   			| A(1,2,0) S(0,0,0) |  8 | 

> Comente
Salve em um dicionário ou em um dataframe, parm_SARIMA[‘categoria’] -> A(1,2,0) S(0,0,0)

> Comente
Salve em um dicionário ou em um dataframe, parm_SARIMA[‘categoria’] -> A(1,2,0) S(0,0,0)

Execuções SARIMA (não é o pmdarima, ou se é o modelo é fixo) sobre receita total e categorias
Para cada categoria (inclui a total):
	SARIMA ou pdmaria com parm_SARIMA[‘categoria’]: 30 -> 1 (x 12 execuções) -> RMSE

Resultados, isso é mostrado nos resultados.  

SARIMA

| categoria 			| 1  | 2 | ... | 12 | Média 12m | Média 3m |
|-----------------|-----|----|-----|-----|-----------|----------|
| brinquedos 			|rmse|rmse| ... |  rmse | rmse | rmse |
| escritório			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| limpeza			| rmse  | rmse  | ... |  rmse | rmse | rmse |
|||| ... ||||
| total   			| rmse  | rmse  | ... |  rmse | rmse | rmse |

### XGBOOST

Para a construção das lags (os valores defasados), empregam-se 12 valores passados com base na sazonalidade da maior parte dos produtos (recomendo avaliar com 6 também). Os mesmos procedimentos e previsões empregados nos modelos SARIMA são então aplicados. Outros parâmetros do XGBOOST? Verifique se não tem melhores resultados com 200, 500 ou 1000 estimadores.

Execuções XGBOOST sobre receita total e categorias
Para cada categoria (inclui a total):
	XGBOOST: 30 -> 1 (x 12 execuções) -> RMSE

Resultados, isso é mostrado nos resultados.  

XGBOOST
| categoria 			| 1  | 2 | ... | 12 | Média 12m | Média 3m |
|-----------------|-----|----|-----|-----|-----------|----------|
| brinquedos 			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| escritório			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| limpeza			| rmse  | rmse  | ... |  rmse | rmse | rmse |
|||| ... ||||
| total   			| rmse  | rmse  | ... |  rmse | rmse | rmse |

### Escolha dos melhores modelos

Os dados do RMSE dos modelos são então empregados para seleção dos melhores modelos para previsões de 1 ou 3 meses. 

### Diagrama

Para concluir, crie um diagrama com todo o fluxo e fases dessa metodologia.

# Resultados

Bla bla bla..

**SARIMA**
| categoria 			| 1  | 2 | ... | 12 | Média 12m | Média 3m |
|-----------------|-----|----|-----|-----|-----------|----------|
| brinquedos 			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| escritório			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| limpeza			| rmse  | rmse  | ... |  rmse | rmse | rmse |
|||| ... ||||
| total   			| rmse  | rmse  | ... |  rmse | rmse | rmse |

> Comente 

**XGBOOST**
| categoria 			| 1  | 2 | ... | 12 | Média 12m | Média 3m |
|-----------------|-----|----|-----|-----|-----------|----------|
| brinquedos 			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| escritório			| rmse  | rmse  | ... |  rmse | rmse | rmse |
| limpeza			| rmse  | rmse  | ... |  rmse | rmse | rmse |
|||| ... ||||
| total   			| rmse  | rmse  | ... |  rmse | rmse | rmse |

> Comente 

## Melhores Modelos 

|                         |   SARIMA   | SARIMA |  XGBOOST |  XGBOOST |   |
|-|-|-| - |-|-|
| categoria 			| **1m**  |  *3m** | **1m**  |  **3m** |  Melhor |
|-|-|-| - |-|-|
| brinquedos 			| **rmse**  | **rmse**  |  rmse | rmse | **SARIMA** |
| escritório			| **rmse**  | **rmse**  |  rmse | rmse | **SARIMA** |
| limpeza		|  rmse | rmse |   **rmse**  | **rmse** | **XGBOOST** |
|-|-|-| - |-|-|
| total   			| **rmse**  | **rmse**  |  rmse | rmse | **SARIMA** |

## Visualização dos Resultados

Somente para os melhores modelos 3 meses de forecast, incluir nos gráficos as outras métricas.

> Comentar,
Que categorias apresentam bons modelos  
Que categorias apresentam maus modelos, por que?
Discuta as métricas dos resultados, MAPE, MAE, MedAE (qual a implicação prática, é o % de erro ou erro médio).

# Conclusão 
Aplicabilidade, importância
Trabalhos futuros: análises complementares como a análise de erros dos modelos, aplicação de outros modelos de ML como modelos de redes neurais e transformers.
