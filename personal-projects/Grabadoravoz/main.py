import argparse
import os
import sys
import logging
from voice_recorder.recorder import grabar_audio


def configurar_logging(verbose: bool) -> None:
    nivel = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=nivel,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Grabador de voz desde línea de comandos"
    )

    parser.add_argument(
        "--duration",
        type=int,
        default=5,
        help="Duración de la grabación en segundos",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="output/audio.wav",
        help="Ruta del archivo de salida",
    )

    parser.add_argument(
        "--samplerate",
        type=int,
        default=44100,
        help="Frecuencia de muestreo",
    )

    parser.add_argument(
        "--device",
        type=int,
        default=0,
        help="ID del dispositivo de audio",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Modo debug",
    )

    args = parser.parse_args()

    configurar_logging(args.verbose)

    # Crear carpeta output si no existe
    os.makedirs(os.path.dirname(args.output), exist_ok=True)

    try:
        grabar_audio(
            duracion=args.duration,
            archivo_salida=args.output,
            samplerate=args.samplerate,
            device=args.device,
        )
        logging.info("Grabación completada correctamente.")

    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()