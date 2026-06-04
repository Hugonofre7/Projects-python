def crear_servicio(nombre, estado, puerto, dependencias=[]):
    dict_servicio = {
        'nombre': nombre,
        'estado': estado,
        'puerto': puerto,
        'dependencias': dependencias
    }
    return dict_servicio
print(crear_servicio('postgres', 'error', '5432', ['mysql', 'redis']))

