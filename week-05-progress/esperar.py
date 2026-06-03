import time

def esperar(segundos, mensaje="Esperando..."):
    time_left = segundos
    while time_left > 0:
        print(time_left)
        time.sleep(1)
        time_left -= 1
    print(mensaje)

if __name__ == "__main__":
    esperar(5, "Health check completado!")
    