import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from ucimlrepo import fetch_ucirepo
import warnings
warnings.filterwarnings('ignore')

wine = fetch_ucirepo(id=109)
X = wine.data.features
y = wine.data.targets

X_selected = X[['Alcohol', 'Alcalinity_of_ash', 'Nonflavanoid_phenols']]

X_train, X_test, y_train, y_test = train_test_split(
    X_selected, y, test_size=0.2, random_state=42
)

modelo_svm = SVC(kernel='rbf', random_state=42)
modelo_svm.fit(X_train, y_train)

y_pred = modelo_svm.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Exactitud (Accuracy): {accuracy:.4f}")
print(f"Interpretación: El modelo clasifica correctamente el {accuracy*100:.2f}% de los vinos en el conjunto de prueba.")

print("\nReporte de Clasificación:")
print(classification_report(y_test, y_pred, zero_division=0))
