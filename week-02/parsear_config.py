
def parsear_config(filepath):
    lines = leer_config(filepath)
    config = {}
    for line in lines:
        clave, valor = line.split("=")
        config[clave] = valor
    return config

