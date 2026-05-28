
import leer_config

def parsear_config(filepath):
    lines = leer_config(filepath)
    config = {}
    for line in lines:
        try:
            clave, valor = line.split("=")
            config[clave] = valor
        except ValueError:
            print(f"Linea inválida: {line}. Se esperaba el formato clave=valor.")
    
    return config
print(parsear_config("config.txt"))

