# Databricks notebook source
dbutils.fs.ls("/mnt/dados/bronze")

# COMMAND ----------

path='dbfs:/mnt/dados/bronze/dataset_imoveis/'
df = spark.read.format("delta").load(path)

# COMMAND ----------

display(df)

# COMMAND ----------

dados = df.select("anuncio.*", "anuncio.endereco.*")

# COMMAND ----------

display(dados)

# COMMAND ----------

dados = dados.drop("caracteristicas","endereco")
display(dados)

# COMMAND ----------

path = "dbfs:/mnt/dados/silver/dataset_imoveis"
dados.write.format("delta").mode("overwrite").save(path)
