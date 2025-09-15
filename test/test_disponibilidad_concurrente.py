import requests, time, csv
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://localhost:8080/api/api/inventory"   # endpoint 
TOTAL_REQUESTS = 200            # total de solicitudes
CONCURRENCY = 20                # cuántas a la vez

def make_request(i):
    """Envía una petición y devuelve (i, status, success, response_time)"""
    start_time = time.time()
    try:
        r = requests.get(URL, timeout=2)
        status = r.status_code
        response_time = (time.time() - start_time) * 1000  # en milisegundos
    except Exception:
        status = 599
        response_time = (time.time() - start_time) * 1000  # tiempo hasta el error
    ok = 1 if 200 <= status < 300 else 0
    return (i, status, ok, response_time)

start = time.time()
results = []
response_times = []

with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    futures = [executor.submit(make_request, i+1) for i in range(TOTAL_REQUESTS)]
    for future in as_completed(futures):
        i, status, ok, response_time = future.result()
        results.append((i, status, ok, response_time))
        if ok:  # solo tiempos exitosos para el promedio
            response_times.append(response_time)
        print(f"Req {i}: status {status}, tiempo: {response_time:.2f}ms")

elapsed = time.time() - start

# Calcular tiempo promedio
avg_time = sum(response_times) / len(response_times) if response_times else 0

# Guardar resultados
with open("resultados_concurrente.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["request","status","success","response_time_ms"])
    for row in results:
        w.writerow(row)

# Calcular disponibilidad
success_count = sum(r[2] for r in results)
print(f"\nDisponibilidad: {success_count}/{TOTAL_REQUESTS} = {success_count/TOTAL_REQUESTS*100:.2f}%")
print(f"Tiempo total: {elapsed:.2f} s")
print(f"Tiempo promedio de respuesta: {avg_time:.2f}ms")