import time
from datetime import datetime


def monitor_servicios(servicios, intervalo=5):
    try:
        
        while True:
            for servicio in servicios:
                ts = timestamp_actual()
                print(f"[{ts}] {servicio}")
            esperar(intervalo, "Esperando próximo ciclo...")
    except KeyboardInterrupt:
        print("Monitor detenido por el usuario.")

def esperar(segundos, mensaje="Esperando..."):
    time_left = segundos
    
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left -= 1
        
    print(mensaje)

def timestamp_actual():
    
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == "__main__":

    servicios = [
        "nginx",
        "mysql",
        "redis"
    ]

    monitor_servicios(servicios, intervalo=5)
