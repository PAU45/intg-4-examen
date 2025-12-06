import pandas as pd
from xgboost import XGBRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder
import numpy as np
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('breast_wisconsin-4.csv')

for col in df.columns:
    if df[col].dtype == 'object':
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])

X = df.drop('fractal_dimension3', axis=1)
y = df['fractal_dimension3']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

modelo_xgb = XGBRegressor(n_estimators=100, random_state=42, verbosity=0)
modelo_xgb.fit(X_train, y_train)

y_pred = modelo_xgb.predict(X_test)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE (Raíz del Error Cuadrático Medio): {rmse:.6f}")
print(f"Interpretación: En promedio, las predicciones se desvían {rmse:.6f} unidades del valor real.")

r2 = r2_score(y_test, y_pred)
print(f"\nR² (Coeficiente de Determinación): {r2:.4f}")
print(f"Interpretación: El modelo explica el {r2*100:.2f}% de la varianza en fractal_dimension3.")
