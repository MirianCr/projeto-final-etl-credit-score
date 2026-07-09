# Projeto Final - Engenharia de Dados- DATAGIRLS 2026 

## Objetivo
Construir um pipeline ETL automatizado para processamento de dados financeiros utilizando o dataset Credit Score Classification.

## Arquitetura
Kaggle
↓
CSV
↓
PySpark
↓
Parquet
↓
AWS S3

📋 Principais Características dos Dados
Fonte Oficial:https://www.kaggle.com/docs/api#getting-started-installation-&-authentication) Importei dos dados do CSV

## Tecnologias para transformação dos dados
- Python
- PySpark
- Apache Spark
- Kaggle API
- AWS S3
- Airflow
  
## Estrutura
Projeto_Final_ETL/
│
├── dags/
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
│
└── README.md

## Validações
- Remoção de duplicidades
- Verificação de idade válida
- Padronização de colunas
- Conversão de tipos de dados
  
## Resultado
Dados processados e armazenados em formato Parquet para consumo analítico.



## Opcional – Bônus
Integração com um Painel no Power BI
• Conectei o banco e arquivos tratados com uma visualização (exportar
dashboard);
• Criei um dashboard simples com métricas como:
o Total de clientes cadastrados;
o Distribuição dos clientes por classificação de Score de Crédito;
o Distribuição da renda mensal por categoria de score.

Página 1 – Visão Geral
Cards:
Total de Clientes
Renda Média
Dívida Média
Número de Empréstimos
Página 2 – Crédito
Gráficos:
Clientes por Credit Score
Credit Score por Occupation
Credit Score por faixa de renda
Página 3 – Financeiro
Gráficos:
Outstanding Debt
Monthly Balance
Credit Utilization Ratio


## Respostas das Perguntas Norteadoras

## 1. Como garantir que os dados estejam sempre atualizados?
A atualização dos dados deve ser garantida por meio da automatização do pipeline de ingestão e processamento. Para isso, o Apache Airflow pode ser utilizado para agendar e orquestrar a execução das tarefas em intervalos definidos, como diariamente. Além disso, é importante implementar mecanismos de reprocessamento para recuperar falhas eventuais e manter logs detalhados de execução, possibilitando monitoramento, rastreabilidade e auditoria do fluxo de dados.
Boas práticas:

Agendamento automático via Apache Airflow.
Execução periódica do pipeline (batch diário).
Monitoramento e alertas para falhas.
Reprocessamento automatizado em caso de erros.
Registro de logs para auditoria e observabilidade.


## 2. Quais validações devem ser realizadas antes do carregamento dos dados?
A etapa de validação é fundamental para garantir a qualidade e a confiabilidade das informações armazenadas. Devem ser aplicadas regras que identifiquem inconsistências, valores inválidos e problemas de integridade antes que os dados sejam disponibilizados para análises ou modelos preditivos.
Validações recomendadas:

Verificação de valores nulos em campos obrigatórios.
Identificação e remoção de registros duplicados.
Validação de faixas aceitáveis para idade dos clientes.
Garantia de que a renda mensal possua valores positivos.
Verificação da consistência das variáveis relacionadas ao score de crédito.
Conferência dos tipos de dados (inteiro, decimal, texto e data).
Validação de regras de negócio específicas do domínio financeiro.


## 3. Como evitar a duplicação de registros?
A prevenção de duplicidades deve ser implementada desde a etapa de ingestão dos dados. Para isso, é recomendável definir uma chave de negócio única, como o identificador do cliente (Customer_ID), permitindo identificar registros repetidos. Além disso, podem ser utilizadas estratégias de carga incremental ou sobrescrita controlada dos dados processados.
Estratégias adotadas:

Utilização do campo Customer_ID como chave de negócio.
Aplicação de processos de deduplicação durante a transformação.
Controle de carga incremental baseado em identificadores ou datas.
Uso de operações de upsert quando aplicável.
Escrita dos dados em modo overwrite ou merge, conforme o cenário.


## 4. Como organizar os dados no Data Lake?
A organização dos dados no Amazon S3 deve seguir uma arquitetura em camadas, permitindo melhor governança, rastreabilidade e manutenção. Os dados brutos são armazenados na camada Raw, enquanto os dados tratados e prontos para consumo ficam na camada Processed. Já os registros de execução e monitoramento são mantidos em uma área específica de Logs.
Estrutura proposta
s3://credit-score/

├── raw/
│   └── train.csv
│
├── processed/
│   └── credit_score.parquet
│
└── logs/

## Descrição das camadas


## Raw (Bronze):

Armazena os dados exatamente como recebidos da fonte.
Preserva o histórico original para auditoria e reprocessamentos.



## Processed (Silver):

Contém dados tratados, validados e padronizados.
Utilizados para análises, dashboards e modelos de Machine Learning.



## Logs:

Registra informações sobre execuções do pipeline.
Auxilia no monitoramento, troubleshooting e governança dos processos.

