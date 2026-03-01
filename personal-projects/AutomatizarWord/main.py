import argparse
import os
import sys
import logging
from automatizar_word.generator import generar_documentos
from automatizar_word.utils import cargar_csv


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generador automático de cartas de presentación en Word"
    )

    parser.add_argument(
        "--template",
        type=str,
        default="templates/mi-plantilla.docx",
        help="Ruta del archivo plantilla .docx",
    )

    parser.add_argument(
        "--csv",
        type=str,
        default="data/Datos-job.csv",
        help="Ruta del archivo CSV con datos",
    )

    parser.add_argument(
        "--output",
        type=str,
        default="output",
        help="Directorio donde se guardarán los documentos generados",
    )

    args = parser.parse_args()

    if not os.path.exists(args.template):
        logging.error(f"No se encontró la plantilla en '{args.template}'")
        sys.exit(1)

    if not os.path.exists(args.csv):
        logging.error(f"No se encontró el archivo CSV en '{args.csv}'")
        sys.exit(1)

    os.makedirs(args.output, exist_ok=True)

    try:
        datos = cargar_csv(args.csv)
        generar_documentos(args.template, datos, args.output)
        logging.info("Documentos generados correctamente.")
    except Exception as e:
        logging.error(f"Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
