from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

# Crea un documento de Word a partir de una plantilla
doc = DocxTemplate("mi-plantilla.docx")

# Crea un diccionario con los datos que quieres insertar
mi_nombre = "Hugo Onofre"
mi_numero = "56-1383-0443"
mi_correo = "hugoant7@gmail.com"
mi_direccion = "Calle 123, Ciudad de México"
fecha_actual = datetime.now().strftime("%d %b, %Y")

# Crea un diccionario con los datos a insertar en la plantilla.
context = { 'mi_nombre': mi_nombre, 
            'mi_numero': mi_numero,
            'mi_correo': mi_correo,
            'mi_direccion': mi_direccion,
            'fecha_actual': fecha_actual
            }

# Crea un diccionario con los datos a insertar de cvs.
df = pd.read_csv("Datos-job.csv")

for index, fila in df.iterrows():
    # Crea un diccionario con los datos a insertar en la plantilla.
    my_context = {
        'nombre_persona_rrhh': fila['name'],
        'direccion' : fila['address'],
        'numero_telefono' : fila['phone_number'],
        'correo' : fila['email'],
        'puesto_de_trabajo' : fila['job'],
        'nombre_empresa' : fila['company'],
    }

    context.update(my_context) # Unifica los dos diccionarios
# Renderiza el documento con los datos
    doc.render(context) # Guarda el documento con un nombre único
    doc.save(f"mi-info_{index}.docx") # Guarda el documento con un nombre único

