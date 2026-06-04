

def crear_servicio(nombre, estado, puerto, dependencias=[]):
    dict_servicio = {
        'nombre': nombre,
        'estado': estado,
        'puerto': puerto,
        'dependencias': dependencias
    }
    return dict_servicio

if __name__ == "__main__":
    
    print(crear_servicio('nginx', 'activo', '80', ['mysql', 'redis']))
