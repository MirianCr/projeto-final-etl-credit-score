import os

arquivo = "/opt/airflow/data/raw/train.csv"

if os.path.exists(arquivo):
    print("Arquivo encontrado.")
else:
    raise FileNotFoundError("train.csv não encontrado.")