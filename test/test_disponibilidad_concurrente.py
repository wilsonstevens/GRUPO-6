import requests, time, csv
from concurrent.futures import ThreadPoolExecutor, as_completed

URL = "http://localhost:8080"   # endpoint 
TOTAL_REQUESTS = 200            # total de solicitudes
CONCURRENCY = 20                # cuántas a la vez

def make_request(i):
    """Envía una petición y devuelve (i, status, success)"""
    try:
        r = requests.get(URL, timeout=2)
        status = r.status_code
    except Exception:
        status = 599
    ok = 1 if 200 <= status < 300 else 0
    return (i, status, ok)

start = time.time()
results = []

with ThreadPoolExecutor(max_workers=CONCURRENCY) as executor:
    futures = [executor.submit(make_request, i+1) for i in range(TOTAL_REQUESTS)]
    for future in as_completed(futures):
        i, status, ok = future.result()
        results.append((i, status, ok))
        print(f"Req {i}: status {status}")

elapsed = time.time() - start

# Guardar resultados
with open("resultados_concurrente.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["request","status","success"])
    for row in results:
        w.writerow(row)

# Calcular disponibilidad
success_count = sum(r[2] for r in results)
print(f"\nDisponibilidad: {success_count}/{TOTAL_REQUESTS} = {success_count/TOTAL_REQUESTS*100:.2f}%")
print(f"Tiempo total: {elapsed:.2f} s")
