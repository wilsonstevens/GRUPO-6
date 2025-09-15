import requests, time, csv

URL = "http://localhost:8080/api/api/inventory"  # endpoint 
REQUESTS = 100  # número de solicitudes

results = []
success = 0
response_times = []

for i in range(REQUESTS):
    start_time = time.time()
    try:
        r = requests.get(URL, timeout=2)
        status = r.status_code
        response_time = (time.time() - start_time) * 1000  # en milisegundos
    except Exception:
        status = 599  # error de conexión
        response_time = (time.time() - start_time) * 1000  # tiempo hasta el error

    ok = 1 if 200 <= status < 300 else 0
    if ok: 
        success += 1
        response_times.append(response_time)  # solo tiempos exitosos para el promedio
    
    results.append([i+1, status, ok, f"{response_time:.2f}"])
    print(f"Req {i+1}: status {status}, tiempo: {response_time:.2f}ms")

# Calcular tiempo promedio
avg_time = sum(response_times) / len(response_times) if response_times else 0

# Guardar resultados
with open("resultados.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["request","status","success","response_time_ms"])
    w.writerows(results)

print(f"\nDisponibilidad: {success}/{REQUESTS} = {success/REQUESTS*100:.2f}%")
print(f"Tiempo promedio de respuesta: {avg_time:.2f}ms")