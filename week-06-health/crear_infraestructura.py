from crear_servicio import crear_servicio

def crear_infraestructura():

    infraestructura = [
        crear_servicio('nginx', 'activo', '80', ['mysql', 'redis']),
        crear_servicio('mysql', 'activo', '3306', []),
        crear_servicio('redis', 'activo', '6379', []),
        crear_servicio('api', 'activo', '8080', ['nginx', 'mysql']) 
]
    return infraestructura

if __name__ == "__main__":
    infraestructura = crear_infraestructura()
    print(infraestructura)