import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# ===============================
# PARTE 1: Estadísticas del % de alcohol
# ===============================
datos = [4.8, 5.1, 5.0, 4.7, 5.2, 5.0, 4.9, 5.3, 4.7, 5.0,
         5.0, 5.1, 4.6, 5.2, 5.1, 4.9, 5.3, 4.7, 5.0, 5.0]

media = round(np.mean(datos), 2)
mediana = round(np.median(datos), 2)
moda = max(set(datos), key=datos.count)
rango = round(max(datos) - min(datos), 2)
desv = round(np.std(datos, ddof=1), 2)

# Mostrar tabla
df = pd.DataFrame({
    'Medida': ['Media', 'Mediana', 'Moda', 'Rango', 'Desviación estándar'],
    'Valor': [media, mediana, moda, rango, desv]
})
print(" Medidas de tendencia central y dispersión:")
print(df.to_string(index=False))

# Gráfico de barras de los valores
plt.figure(figsize=(8, 5))
plt.bar(df['Medida'], df['Valor'], color="#4DB6AC")
plt.title(" Gráfico de Estadísticas del % de Alcohol")
plt.ylabel("Valor")
plt.grid(True, linestyle="--", alpha=0.3)
plt.tight_layout()
plt.show()

# ===============================
# PARTE 2: Diagrama de Causa - Efecto (Ishikawa)
# ===============================
print("\n Diagrama de Causa Y Efecto (Resumen en tabla):")

ishikawa = pd.DataFrame({
    'Categoría': ['Máquina', 'Método', 'Mano de Obra', 'Material'],
    'Causas': [
        'Equipos sin mantenimiento, temperatura inestable',
        'Falta de estándares, sin control en tiempo real',
        'Falta de capacitación, errores manuales',
        'Materia prima variable, mala conservación'
    ]
})
print(ishikawa.to_string(index=False))

# ===============================
# PARTE 3: Propuesta de Mejora Continua
# ===============================
print("\n✅ Propuesta práctica de mejora continua:")

mejora = pd.DataFrame({
    "¿Qué hacer?": [
        "Implementar CEP (gráficas de control)",
        "Capacitar al personal",
        "Aplicar la norma ISO 9000",
        "Usar diagrama de Pareto y causa-efecto",
        "Hacer auditorías internas mensuales",
        "Definir indicadores clave (KPIs)",
        "Fomentar cultura de mejora continua"
    ],
    "¿Para qué sirve?": [
        "Reducir la variabilidad del proceso",
        "Mejorar la calidad del trabajo",
        "Estandarizar procesos y reducir reprocesos",
        "Identificar las causas principales de problemas",
        "Revisar y corregir a tiempo",
        "Medir avances y resultados",
        "Mejorar continuamente la empresa"
    ]
})
print(mejora.to_string(index=False))

# BONUS: Diagrama tipo lista visual
plt.figure(figsize=(10, 6))
for i, txt in enumerate(mejora["¿Qué hacer?"]):
    plt.text(0.1, 0.9 - i * 0.12, f"✓ {txt}", fontsize=11,
             bbox=dict(boxstyle='round', facecolor='#E1F5FE', edgecolor='gray'))
plt.axis('off')
plt.title(" Propuesta de Mejora Continua – Caso PERUVIAM", fontsize=14)
plt.tight_layout()
plt.show()
