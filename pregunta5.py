from pyspark.sql import SparkSession
import warnings
warnings.filterwarnings('ignore')

spark = SparkSession.builder.appName("Pregunta5").getOrCreate()

df = spark.read.csv('data-2.csv', header=True, inferSchema=True)

print("1. Tipos de datos de todas las variables:")
df.printSchema()

print("\n2. Columnas CIC y EGFR:")
df.select('CIC', 'EGFR').show()

print("\n3. Suma total de EGFR:")
suma_egfr = df.agg({'EGFR': 'sum'}).collect()[0][0]
print(f"Suma EGFR: {suma_egfr}")

print("\n4. Suma total de SMARCA4:")
suma_smarca4 = df.agg({'SMARCA4': 'sum'}).collect()[0][0]
print(f"Suma SMARCA4: {suma_smarca4}")

spark.stop()
