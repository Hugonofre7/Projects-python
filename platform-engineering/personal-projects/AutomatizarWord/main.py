import argparse
import os
import sys
import logging
from automatizar_word.generator import generar_documentos
from automatizar_word.utils import cargar_csv


def configurar_logging(verbose: bool) -> None:
    """
    Configura el sistema de logging.
    """
    nivel = logging.DEBUG if verbose else logging.INFO

    logging.basicConfig(
        level=nivel,
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
    help="Ruta del archivo de plantilla Word (.docx)",
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

    parser.add_argument(
    "--verbose",
    action="store_true",
    help="Activa modo detallado (DEBUG)",
)

    args = parser.parse_args()
    configurar_logging(args.verbose)
    
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
