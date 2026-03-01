import argparse
import os
import sys
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

    # Validar existencia del template
    if not os.path.exists(args.template):
        print(f"❌ Error: No se encontró la plantilla en '{args.template}'")
        sys.exit(1)

    # Validar existencia del CSV
    if not os.path.exists(args.csv):
        print(f"❌ Error: No se encontró el archivo CSV en '{args.csv}'")
        sys.exit(1)

    # Crear carpeta output si no existe
    os.makedirs(args.output, exist_ok=True)

    try:
        datos = cargar_csv(args.csv)
        generar_documentos(args.template, datos, args.output)
        print("✅ Documentos generados correctamente.")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
