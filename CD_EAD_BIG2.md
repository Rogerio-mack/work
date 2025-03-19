# Resumos das Aulas do Ecossistema de Big Data II

Aqui estão os quatro resumos, combinados em um único texto em formato Markdown:


## Aula 1: Pipelines de Dados

* **Introdução a Pipelines de Dados:** Pipelines de dados são essenciais para transformar dados brutos em informações úteis para a tomada de decisão.  Eles extraem dados de várias fontes, limpam e transformam os dados e os entregam em um formato utilizável.  A comparação com o processo de refino do petróleo é utilizada para ilustrar a importância do processo.

* **O que são Pipelines de Dados?:**  Um pipeline de dados é um processo sequencial, similar a um encanamento, onde os dados brutos fluem de várias fontes (bancos de dados, APIs, arquivos).  Os dados são processados (filtrados, mascarados, agregados) e armazenados em um repositório (data lake ou data warehouse).

* **Tipos de Pipelines de Dados:** O texto descreve três tipos principais:
    * **Dados em Lote (ou Processamento em Lote):** Processa grandes volumes de dados em momentos específicos, geralmente durante horários de menor atividade. É eficiente para lidar com muitos dados que não precisam de análise imediata.
    * **Dados em Streaming (ou Dados em Fluxo):** Processa dados continuamente e em tempo real. Cada ação é um evento, agrupados em fluxos transmitidos por sistemas de mensagens (brokers).  Tem latência menor que o processamento em lote, mas maior risco de perda de mensagens.
    * **Dados Interativos:** Acessados e atualizados em tempo real, em resposta às ações do usuário.  Importantes em aplicativos que exigem respostas rápidas.

* **Complexidade de um Pipeline de Dados:** A complexidade varia de acordo com o tamanho dos dados, sua condição, estrutura e o objetivo da análise. Pipelines podem ser simples (extração de uma fonte para um destino) ou complexos (várias etapas interligadas, diferentes sistemas e linguagens de programação).

* **Orquestração de Pipeline de Dados:** Processo de automatizar e gerenciar tarefas em um fluxo de trabalho, cuidando das dependências entre as tarefas. Utiliza o Gráfico Acíclico Direcionado (DAG) para visualizar o fluxo de dados e dependências.

* **Implantação em Nuvem ou On-Premise:** A implantação em nuvem oferece escalabilidade, flexibilidade e potencialmente custos menores.  A solução *on-premise* proporciona maior controle e segurança, mas requer maior investimento inicial.


## Aula 2: Arquiteturas de Referência para Big Data

* **Introdução:** Apresenta duas arquiteturas principais para Big Data: a Arquitetura de Referência para Big Data e a Arquitetura NIST.  Ambas fornecem estruturas para organizar, processar e extrair valor de grandes volumes de dados.

* **Arquitetura de Referência para Big Data (Pakkala, 2015):** Organiza funcionalidades em áreas funcionais, focando no fluxo de dados e armazenamento. Abrange desde as fontes de dados até a visualização e especificação de trabalhos e modelos.

* **Arquitetura NIST:** Modelo conceitual e duas visões arquitetônicas focadas em Big Data.  Estruturada em cinco funções principais (Orquestrador, Provedor de Dados, Provedor de Aplicativos, Provedor de Estrutura e Consumidor de Dados), além de funções transversais (Gerenciamento e Segurança/Privacidade).

* **Funções-chave da Arquitetura NIST:** Detalhes das cinco funções-chave e suas responsabilidades.

* **Funções Transversais da Arquitetura NIST:**  Descrição das estruturas de gerenciamento e de segurança e privacidade.


## Aula 3: Estratégias Avançadas no Processamento de Big Data

* **Estratégias Avançadas no Processamento de Big Data:** As estruturas de processamento em Big Data são essenciais para lidar com os desafios de volume, velocidade, variedade e variabilidade dos dados.  Elas variam entre processamento em lote e *streaming*.

* **Planejamento da Coleta Batch e Streaming e Arquitetura Baseada em Silos:**  Empresas em crescimento podem desenvolver arquiteturas de dados baseadas em silos, causando problemas para a colaboração e o compartilhamento eficiente de dados.

* **Processamento em Lote vs. Processamento em Tempo Real:** Processamento em lote processa grandes volumes de dados em grupos, com defasagem temporal.  Processamento em tempo real processa dados no momento em que ocorrem, proporcionando insights imediatos.

* **Streaming de Dados em Tempo Real:** Coleta e processamento contínuo de dados de várias fontes. A escalabilidade é crucial em cada etapa (ingestão, processamento e análise).

* **Construções de Processamento de Fluxo:** Detalhes sobre *agregações*, *janelas de tempo*, e *causalidade e relacionamentos*.

* **Transformando Dados Transacionais em Fluxo Contínuo de Eventos:**  A captura de dados de alteração (CDC) integra dados de sistemas tradicionais com metodologias de processamento de fluxo contínuo.

* **Ferramentas de Apoio para Coleta de Dados:**  Apresentação do Apache Hadoop e MapReduce.

* **Processamento em Tempo Real:** Usado para processar dados e obter resultados quase que imediatamente (exemplo: Google Dremel).

* **Processamento em Stream:** Processa continuamente dados de *stream* ao vivo (exemplos: Apache Storm e Apache Flink).

* **Diferenças entre Processamento em Stream e em Tempo Real:**  Processamento em *stream* lida com fluxos contínuos, processando sequencialmente.  Processamento em tempo real foca na rapidez da resposta, podendo ou não ser baseado em *streaming*.


## Aula 4: DataOps, Pipelines as Code e Notebooks

* **Gerenciamento Abrangente de Data Pipelines:** Abrange armazenamento, metadados e governança.

* **Metadados:**  "Dados sobre dados", cruciais para a descoberta e governança de dados.  Categorias: autogerados e gerados por humanos;  de negócios, técnicos, de pipeline, operacionais e de referência.  Ferramentas de gerenciamento de metadados facilitam o processo.

* **DataOps:** Adoção de melhores práticas ágeis e DevOps no contexto de dados.  Busca inovação, qualidade, colaboração e medição clara.  MLOps é um conceito relacionado.

* **Pipelines as Code:** Declaração de tarefas e dependências em código (ex: Python), promovendo automatização, reprodutibilidade, rastreabilidade e flexibilidade.  Exemplo de pipeline simples em Airflow.

* **Aspectos das Ferramentas de DataOps:**  As ferramentas monitoram e melhoram aspectos críticos: saúde dos dados, latência, qualidade, segurança e gerenciamento de versões.

* **Servindo Dados em Notebooks:** Notebooks (ex: Jupyter) são ferramentas essenciais para cientistas de dados.  A conexão com fontes de dados é crucial.  Para grandes conjuntos de dados, sistemas distribuídos ou soluções em nuvem podem ser necessários.

* **Exemplo Prático:** Um cientista de dados usa um notebook para se conectar a um data warehouse e carregar dados para análise.

* **Arquitetura de Notebooks na Netflix:**  Notebooks são utilizados na produção, com suas vantagens e desafios.  Uma abordagem híbrida é sugerida.


Este documento consolidado proporciona uma visão geral completa do conteúdo das quatro aulas.  Para uma compreensão mais detalhada de cada tópico, recomenda-se a consulta dos documentos originais de cada aula.
