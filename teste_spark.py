from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master("local[*]") \
    .appName("Teste") \
    .getOrCreate()

print("Spark funcionando!")

spark.stop()