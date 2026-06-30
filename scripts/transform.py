from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Teste") \
    .getOrCreate()

print("Lendo CSV...")

df = spark.read.csv(
    "data/raw/train.csv",
    header=True,
    inferSchema=True
)

print("Quantidade de linhas:")
print(df.count())

print("Salvando parquet...")

df.write.mode("overwrite").parquet(
    "data/processed/credit_score"
)

print("Parquet salvo com sucesso!")

spark.stop()