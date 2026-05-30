import csv

def exportar_csv(datos, filepath):
    with open(filepath, 'w', newline='') as file:
        columnas = datos[0].keys()
        writer = csv.DictWriter(file, fieldnames=columnas)
        writer.writeheader()
        writer.writerows(datos)
        
datos = [
    {'service': 'nginx', 'level': 'INFO', 'status': 'activo'},
    {'service': 'mysql', 'level': 'ERROR', 'status': 'error'}
]



exportar_csv(datos, "reporte.csv")
print("Archivo CSV exportado.")