def clasificar_servicio(nombre, estado):
    if estado == "activo":
        return nombre + " está activo ✓"
    elif estado == "inactivo":
        return nombre + " está inactivo —"
    elif estado == "error":
        return nombre + " tiene un error ✗"
    else:
        return nombre + " estado desconocido"


def reporte_servicios(servicios):
    for nombre, estado in servicios:
        resultado = clasificar_servicio(nombre, estado)
        print(resultado)


servicios = [
    ("nginx", "activo"),
    ("mysql", "error"),
    ("redis", "inactivo"),
    ("postgres", "activo")
]

reporte_servicios(servicios)

print("Reporte de servicios generado.")