import boto3

ACCESS_KEY = "SUA_ACCESS_KEY"
SECRET_KEY = "SUA_SECRET_KEY"

s3 = boto3.client(
    "s3",
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

arquivo = "data/processed/credit_score"

print("Upload concluído!")