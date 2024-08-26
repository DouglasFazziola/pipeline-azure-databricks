# Projeto de Ingestão de Dados no Azure Data Lake

Este projeto realiza a ingestão, transformação e armazenamento de dados utilizando o Azure Data Lake, Databricks e Azure Data Factory. O fluxo de dados segue o padrão de camadas (Unbound, Bronze, Silver) e envolve a transformação dos dados brutos em um formato mais refinado e organizado, pronto para análise.

## Estrutura do Projeto

### 1. Organização do Data Lake
O Data Lake foi organizado em três camadas principais:
- **Unbound:** Armazena os arquivos de dados brutos em formato JSON.
- **Bronze:** Armazena os dados transformados em formato Delta, após a primeira etapa do ETL.
- **Silver:** Contém os dados refinados em formato Delta, após a segunda etapa do ETL.

### 2. Notebooks Databricks

#### 2.1. inbound_to_bronze.py
Este notebook realiza a primeira etapa do processo ETL, onde os dados brutos em formato JSON são carregados, transformados e salvos na camada Bronze.

**Etapas do Notebook:**
1. Carregamento do arquivo JSON da pasta Unbound.
2. Remoção de colunas irrelevantes (`imagens`, `usuario`).
3. Adição de uma coluna de ID (`id`).
4. Salvamento dos dados transformados na camada Bronze em formato Delta.

#### 2.2. bronze_to_silver.py
Este notebook realiza a segunda etapa do processo ETL, onde os dados da camada Bronze são refinados e salvos na camada Silver.

**Etapas do Notebook:**
1. Carregamento dos dados da camada Bronze em formato Delta.
2. Seleção das colunas relevantes e refinamento dos dados.
3. Remoção de colunas desnecessárias (`caracteristicas`, `endereco`).
4. Salvamento dos dados refinados na camada Silver em formato Delta.

### 3. Pipeline no Azure Data Factory

O pipeline no Azure Data Factory orquestra a execução dos notebooks Databricks, garantindo que as etapas de transformação de dados sejam executadas na sequência correta.

**Pipeline:** `datalake-ingestion`
- **Atividade 1:** `ingestao-camada-bronze` - Executa o notebook `inbound_to_bronze.py`.
- **Atividade 2:** `ingestao-camada-silver` - Executa o notebook `bronze_to_silver.py` após a conclusão da atividade 1.

### 4. Gatilho de Execução

Um gatilho de execução foi configurado no Azure Data Factory para acionar o pipeline `datalake-ingestion` a cada hora.

**Gatilho:** `pipeline_trigger`
- **Tipo:** `ScheduleTrigger`
- **Frequência:** A cada 1 hora.
- **Hora de início:** 15 de agosto de 2024, 12:42 (Horário Padrão da América do Sul Oriental).

## Requisitos

- **Azure Data Lake Storage**
- **Azure Databricks**
- **Azure Data Factory**

## Como Executar

1. Configure as credenciais e permissões necessárias para acessar o Azure Data Lake, Databricks e Data Factory.
2. Carregue o arquivo JSON de dados brutos na pasta Unbound do Data Lake.
3. Execute o pipeline no Azure Data Factory para iniciar o processo de transformação e armazenamento dos dados.
4. Monitore a execução através dos logs gerados no Azure Data Factory e Databricks.

## Conclusão

Este projeto demonstra um fluxo de trabalho completo para ingestão e transformação de dados em um ambiente de Big Data, utilizando ferramentas da Azure. A organização das camadas e o uso de notebooks Databricks permitem uma gestão eficiente dos dados e a criação de um pipeline escalável e automatizado.
