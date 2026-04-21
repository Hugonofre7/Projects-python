import sounddevice as sd


def listar_dispositivos() -> None:
    """
    Muestra los dispositivos de audio disponibles.
    """
    dispositivos = sd.query_devices()

    for i, dispositivo in enumerate(dispositivos):
        print(f"{i}: {dispositivo['name']}")