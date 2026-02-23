from docxtpl import DocxTemplate
from datetime import datetime


def generar_documentos(template_path: str, csv_data: list[dict], output_dir: str) -> None:
    """
    Genera documentos Word personalizados a partir de una plantilla
    y una lista de diccionarios con datos.
    """
    for index, fila in enumerate(csv_data):
        doc = DocxTemplate(template_path)

        fecha_actual = datetime.now().strftime("%d %b, %Y")

        context = {
            "mi_nombre": fila.get("mi_nombre"),
            "mi_numero": fila.get("mi_numero"),
            "mi_correo": fila.get("mi_correo"),
            "mi_direccion": fila.get("mi_direccion"),
            "fecha_actual": fecha_actual,
            "nombre_persona_rrhh": fila.get("name"),
            "direccion": fila.get("address"),
            "numero_telefono": fila.get("phone_number"),
            "correo": fila.get("email"),
            "puesto_de_trabajo": fila.get("job"),
            "nombre_empresa": fila.get("company"),
        }

        doc.render(context)
        doc.save(f"{output_dir}/mi-info_{index}.docx")

