import json

def importar_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

datos_importados = importar_json("reporte.json")

print(datos_importados)
