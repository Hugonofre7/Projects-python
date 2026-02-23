import argparse
from automatizar_word.generator import generar_documentos
from automatizar_word.utils import cargar_csv


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

    datos = cargar_csv(args.csv)
    generar_documentos(args.template, datos, args.output)


if __name__ == "__main__":
    main()

