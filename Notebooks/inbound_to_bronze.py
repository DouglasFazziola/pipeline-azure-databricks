# Databricks notebook source
from pyspark.sql.functions import col

# COMMAND ----------

dbutils.fs.ls("/mnt/dados/inbound")

# COMMAND ----------

path = 'dbfs:/mnt/dados/inbound/dados_brutos_imoveis.json'


# COMMAND ----------

dados = spark.read.json(path)

# COMMAND ----------

display(dados)

# COMMAND ----------

dados = dados.drop("imagens","usuario")

# COMMAND ----------

dados = dados.withColumn("id",col("anuncio.id"))
display(dados)

# COMMAND ----------

path = "dbfs:/mnt/dados/bronze/dataset_imoveis"
dados.write.format("delta").mode("overwrite").save(path)
