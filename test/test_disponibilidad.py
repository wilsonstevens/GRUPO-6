import requests, time, csv

URL = "http://localhost:8080"  # endpoint 
REQUESTS = 100  # número de solicitudes

results = []
success = 0

for i in range(REQUESTS):
    try:
        r = requests.get(URL, timeout=2)
        status = r.status_code
    except Exception:
        status = 599  # error de conexión

    ok = 1 if 200 <= status < 300 else 0
    if ok: success += 1
    results.append([i+1, status, ok])
    print(f"Req {i+1}: status {status}")

# Guardar resultados
with open("resultados.csv","w",newline="") as f:
    w = csv.writer(f)
    w.writerow(["request","status","success"])
    w.writerows(results)

print(f"\nDisponibilidad: {success}/{REQUESTS} = {success/REQUESTS*100:.2f}%")
