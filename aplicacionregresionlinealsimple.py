import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# PASO 1: CREAR DATOS (Simulación)
# Ejemplo: academia de idiomas
# X = horas de estudio semanales
# y = nota del examen
# Relación base: Nota = 4 * Horas + 40

np.random.seed(42)  # Para que siempre se generen los mismos datos

# Generamos 200 valores de horas de estudio entre 1 y 15 horas por semana
X = np.random.uniform(1, 16, size=(200, 1))

# Generamos las notas con la fórmula base + un poco de ruido
# El ruido sirve para simular variaciones reales entre alumnos
y = (4 * X).squeeze() + 40 + np.random.randn(200) * 5

print("Primeras 10 muestras de datos:")
print("Horas de estudio:", X[:10].flatten())
print("Notas del examen:", y[:10])

# PASO 2: DIVIDIR LOS DATOS
# 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print(f"\nDatos de entrenamiento: {len(X_train)}")
print(f"Datos de prueba: {len(X_test)}")

# PASO 3: CREAR Y ENTRENAR EL MODELO
modelo = LinearRegression()
modelo.fit(X_train, y_train)

print("\nModelo entrenado correctamente")
print(f"Pendiente aprendida: {modelo.coef_[0]:.2f}")
print(f"Intercepto aprendido: {modelo.intercept_:.2f}")

# PASO 4: HACER PREDICCIONES
y_pred = modelo.predict(X_test)

print("\nComparación entre valor real y predicho:")
for i in range(10):
    print(f"Alumno {i+1}: Real={y_test[i]:.2f} | Predicho={y_pred[i]:.2f}")

# PASO 5: EVALUAR EL MODELO
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMétricas del modelo:")
print(f"Error Cuadrático Medio (MSE): {mse:.2f}")
print(f"R^2: {r2:.2f}")

# PASO 6: GRAFICAR LOS RESULTADOS
plt.figure(figsize=(10, 6))

# Datos de entrenamiento
plt.scatter(X_train, y_train, alpha=0.5, label="Datos de entrenamiento")

# Datos de prueba
plt.scatter(X_test, y_test, edgecolors="black", label="Datos de prueba")

# Línea de regresión
X_linea = np.linspace(X.min(), X.max(), 200).reshape(-1, 1)
y_linea = modelo.predict(X_linea)
plt.plot(X_linea, y_linea, linewidth=2, label="Línea de regresión")

plt.title("Regresión lineal simple: Horas de estudio vs Nota")
plt.xlabel("Horas de estudio semanales")
plt.ylabel("Nota del examen")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# PASO 7: PREDICCIÓN FINAL
horas_nuevas = np.array([[8]])
nota_estimada = modelo.predict(horas_nuevas)

print(f"\nSi un alumno estudia 8 horas por semana,")
print(f"el modelo predice una nota aproximada de: {nota_estimada[0]:.2f}")