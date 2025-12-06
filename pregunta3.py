import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import f1_score, precision_score
import numpy as np

df = pd.read_csv('aids_clinical-4.csv')

X = df.drop('str2', axis=1)
y = df['str2']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

modelo_rf = RandomForestClassifier(n_estimators=100, random_state=42)
modelo_rf.fit(X_train, y_train)

y_pred = modelo_rf.predict(X_test)

precision = precision_score(y_test, y_pred, average='weighted')
print(f"Precisión (Precision): {precision:.4f}")
print(f"Interpretación: De los casos predichos como positivos, el {precision*100:.2f}% son realmente correctos.")

f1 = f1_score(y_test, y_pred, average='weighted')
print(f"\nF1-Score: {f1:.4f}")
print(f"Interpretación: El F1-Score es el balance entre precisión y recall. Valor de {f1:.4f} indica buena relación entre ambas métricas.")
