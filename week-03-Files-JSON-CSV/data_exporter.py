import json

def exportar_json(datos, filepath):
    with open(filepath, 'w') as f:
        json.dump(datos, f, indent=4)
datos = [
    {'service': 'nginx', 'level': 'INFO', 'status': 'activo'},
    {'service': 'mysql', 'level': 'ERROR', 'status': 'error'}
]

exportar_json(datos, "reporte.json")
print("Archivo JSON exportado.")

