import sounddevice as sd
from scipy.io.wavfile import write
import logging


def grabar_audio(duracion: int, archivo_salida: str, samplerate: int, device: int) -> None:
    """
    Graba audio desde el micrófono y lo guarda en un archivo WAV.
    """

    try:
        logging.info("Iniciando grabación...")

        recording = sd.rec(
            int(duracion * samplerate),
            samplerate=samplerate,
            channels=1,
            device=device,
            dtype='int16'
        )

        sd.wait()

        write(archivo_salida, samplerate, recording)

        logging.info(f"Grabación guardada en: {archivo_salida}")

    except Exception as e:
        logging.error(f"Error durante la grabación: {e}")
        raise