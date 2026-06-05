
from health_check_sim import crear_servicio

def simular_falla(infraestructura, nombre_servicio):
    for servicio in infraestructura:
        if servicio['nombre'] == nombre_servicio:
            servicio['estado'] = 'error'
        elif nombre_servicio in servicio['dependencias']:
            servicio['estado'] = 'afectado'
    return infraestructura


def crear_infraestructura():

    infraestructura = [
        crear_servicio('nginx', 'activo', '80', ['mysql', 'redis']),
        crear_servicio('mysql', 'activo', '3306', []),
        crear_servicio('redis', 'activo', '6379', []),
        crear_servicio('api', 'activo', '8080', ['nginx', 'mysql'])
    ]
    return infraestructura

print(simular_falla(crear_infraestructura(), 'mysql'))