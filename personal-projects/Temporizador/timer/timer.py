import time
import logging


def iniciar_temporizador(segundos: int) -> None:
    """
    Ejecuta un temporizador regresivo.
    """
    try:
        while segundos >= 0:
            mins, secs = divmod(segundos, 60)
            timer = f"{mins:02d}:{secs:02d}"
    
            print(timer)  # ← cambio clave (sin \r)

            time.sleep(1)
            segundos -= 1

        print("\n⏰ Tiempo finalizado.")
        logging.info("Temporizador finalizado.")

    except KeyboardInterrupt:
        logging.warning("Temporizador interrumpido por el usuario.")