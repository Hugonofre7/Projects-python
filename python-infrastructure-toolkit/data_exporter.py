import json
import csv

def exportar_json(datos, filepath):
    with open(filepath, 'w') as f:
        json.dump(datos, f, indent=4)

def importar_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def exportar_csv(datos, filepath):
    with open(filepath, 'w', newline='') as file:
        columnas = datos[0].keys()
        writer = csv.DictWriter(file, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(datos)

if __name__ == "__main__":
    datos = [
        {'service': 'nginx', 'level': 'INFO', 'status': 'activo'},
        {'service': 'mysql', 'level': 'ERROR', 'status': 'error'}
]

    exportar_json(datos, "reporte.json")
    print("Archivo JSON exportado.")

    datos_importados = importar_json("reporte.json")
    print(datos_importados)

    exportar_csv(datos, "reporte.csv")
    print("Archivo CSV exportado.")




