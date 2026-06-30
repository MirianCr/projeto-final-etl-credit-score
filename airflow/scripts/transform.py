import pandas as pd
import os

# Ler arquivo
df = pd.read_csv("/opt/airflow/data/raw/train.csv")

# Remover duplicados
df = df.drop_duplicates()

# Substituir valores inválidos comuns no dataset
df.replace("_______", pd.NA, inplace=True)
df.replace("__10000__", pd.NA, inplace=True)

# Colunas numéricas
colunas_numericas = [
    "Age",
    "Annual_Income",
    "Monthly_Inhand_Salary",
    "Num_Bank_Accounts",
    "Num_Credit_Card",
    "Interest_Rate",
    "Num_of_Loan",
    "Delay_from_due_date",
    "Num_of_Delayed_Payment",
    "Outstanding_Debt",
    "Credit_Utilization_Ratio",
    "Monthly_Balance"
]

for coluna in colunas_numericas:
    if coluna in df.columns:
        df[coluna] = pd.to_numeric(
            df[coluna],
            errors="coerce"
        )

# Criar pasta processada
os.makedirs("/opt/airflow/data/processed", exist_ok=True)

# Salvar parquet
df.to_parquet(
    "/opt/airflow/data/processed/credit_score.parquet",
    engine="pyarrow",
    index=False
)

print("Parquet salvo com sucesso!")
