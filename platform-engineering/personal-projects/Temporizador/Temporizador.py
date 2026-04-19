import time


def temporizador(segundos: int) -> None:
    """
    Ejecuta un temporizador regresivo desde la cantidad de segundos indicada.

    Args:
        segundos (int): Tiempo en segundos para el conteo regresivo.
    """
    while segundos > 0:
        mins, secs = divmod(segundos, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        segundos -= 1

    print("\n⏰ Tiempo finalizado.")


def obtener_tiempo_usuario() -> int:
    """
    Solicita al usuario un tiempo válido en segundos.
    
    Returns:
        int: Tiempo válido en segundos.
    """
    while True:
        try:
            tiempo = int(input("Introduce el tiempo en segundos: "))
            if tiempo < 0:
                print(" El tiempo no puede ser negativo.")
                continue
            return tiempo
        except ValueError:
            print(" Por favor, introduce un número válido.")


if __name__ == "__main__":
    tiempo_usuario = obtener_tiempo_usuario()
    temporizador(tiempo_usuario)
