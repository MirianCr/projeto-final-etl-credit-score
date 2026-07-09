# Projeto Final - Engenharia de Dados
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
## Tecnologias
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
