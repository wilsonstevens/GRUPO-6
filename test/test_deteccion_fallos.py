import requests
import statistics
import csv
import time

# Parámetros del experimento
NUM_CORRIDAS = 60                   # cuántas corridas hacer
PETICIONES_POR_CORRIDA = 100        # cuántas peticiones en cada corrida
URL_ENDPOINT = "http://localhost:8080/api/api/inventory"  # cambia a tu endpoint real
TIMEOUT = 5                         # segundos de espera máximo por petición

resultados = []

for corrida in range(1, NUM_CORRIDAS + 1):
    fallos_detectados = 0
    exitos = 0

    for i in range(PETICIONES_POR_CORRIDA):
        try:
            r = requests.get(URL_ENDPOINT, timeout=TIMEOUT)
            # Consideramos fallo cualquier status >=400
            if r.status_code >= 400:
                fallos_detectados += 1
            else:
                exitos += 1
        except requests.RequestException:
            # Error de conexión o timeout
            fallos_detectados += 1

    total = PETICIONES_POR_CORRIDA
    porcentaje_exito = (exitos/total)*100
    porcentaje_fallo = (fallos_detectados/total)*100

    resultados.append({
        "corrida": corrida,
        "total_peticiones": total,
        "exitos": exitos,
        "fallos": fallos_detectados,
        "porcentaje_exito": porcentaje_exito,
        "porcentaje_fallo": porcentaje_fallo
    })

    print(f"Corrida {corrida}: {exitos} OK / {fallos_detectados} Fallos "
          f"({porcentaje_exito:.2f}% disponibilidad)")
    time.sleep(1)  # pequeña pausa entre corridas

# Guardar resultados a CSV
with open("resultados_disponibilidad.csv","w",newline="") as f:
    w = csv.DictWriter(f, fieldnames=resultados[0].keys())
    w.writeheader()
    w.writerows(resultados)

# Calcular estadísticas globales
porcentajes_exito = [r["porcentaje_exito"] for r in resultados]
media = statistics.mean(porcentajes_exito)
desviacion = statistics.stdev(porcentajes_exito) if len(porcentajes_exito) > 1 else 0

print("\n=== Estadísticas globales ===")
print(f"Corridas: {NUM_CORRIDAS}")
print(f"Media % disponibilidad: {media:.2f}%")
print(f"Desviación estándar: {desviacion:.2f}%")
