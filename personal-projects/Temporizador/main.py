import argparse
import sys
import logging
from timer.timer import iniciar_temporizador
from timer.utils import convertir_a_segundos


def configurar_logging(verbose: bool) -> None:
    nivel = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=nivel,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Temporizador desde línea de comandos"
    )

    parser.add_argument(
        "--time",
        type=str,
        required=True,
        help="Tiempo en formato HH:MM:SS (ej: 00:01:30)",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Modo debug",
    )

    args = parser.parse_args()

    configurar_logging(args.verbose)

    try:
        segundos = convertir_a_segundos(args.time)
        iniciar_temporizador(segundos)

    except ValueError as e:
        logging.error(e)
        sys.exit(1)

    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()