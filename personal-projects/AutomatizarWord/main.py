from automatizar_word.generator import generar_documentos
from automatizar_word.utils import cargar_csv


def main() -> None:
    template_path = "templates/mi-plantilla.docx"
    csv_path = "data/Datos-job.csv"
    output_dir = "output"

    datos = cargar_csv(csv_path)
    generar_documentos(template_path, datos, output_dir)


if __name__ == "__main__":
    main()

