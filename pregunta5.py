import pandas as pd

df = pd.read_csv('data-2.csv')

print("1. Tipos de datos de todas las variables:")
print(df.dtypes)

print("\n2. Columnas CIC y EGFR:")
print(df[['CIC', 'EGFR']])

print("\n3. Suma total de EGFR:")
suma_egfr = df['EGFR'].sum()
print(f"Suma EGFR: {suma_egfr}")

print("\n4. Suma total de SMARCA4:")
suma_smarca4 = df['SMARCA4'].sum()
print(f"Suma SMARCA4: {suma_smarca4}")
