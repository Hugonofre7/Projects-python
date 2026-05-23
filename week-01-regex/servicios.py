def clasificar_servicio(nombre, estado):
    if estado == "activo":
        return f"{nombre} está activo ✓"
    elif estado == "inactivo":
        return f"{nombre} está inactivo —"
    elif estado == "error":
        return f"{nombre} tiene un error ✗"
    else:
        return f"{nombre} estado desconocido"

print (f'Tu estado de servicio es: {clasificar_servicio("nginx", "activo")}.')
print (f'Tu estado de servicio es: {clasificar_servicio("mysql", "inactivo")}.')
print (f'Tu estado de servicio es: {clasificar_servicio("redis", "error")}.')
print (f'Tu estado de servicio es: {clasificar_servicio("postgres", "desconocido")}.')

