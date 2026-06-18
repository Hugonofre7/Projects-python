import leer_config

def leer_config(filepath):
    valid_lines = []
    try:
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line == "":
                    continue
                if line.startswith("#"):
                    continue
                valid_lines.append(line)
    except FileNotFoundError:
        print(f"Sorry, the file {filepath} does not exist.")
    return valid_lines

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

def guardar_config(filepath, config):
    with open(filepath, 'w') as file:
        for clave, valor in config.items():
            file.write(f"{clave}={valor}\n")
config = {'host': '192.168.1.1', 'port': '8080'}
guardar_config("config.txt", config)

if __name__ == "__main__":
    print("Archivo guardado exitosamente.")
    print(parsear_config("config.txt"))

    config = parsear_config("config.txt")
    print("Config leída:", config)

    config['host'] = '10.0.0.1'
    guardar_config("config.txt", config)
    print("Config guardada.")

    config_nueva = parsear_config("config.txt")
    print("Config actualizada:", config_nueva)

# Prueba de la linea inválida
'''print(parsear_config("config.txt")) 

# prueba de linea invalida
with open("config.txt", 'w') as f:
    f.write("host=10.0.0.1\nesta_linea_esta_mal\nport=8080\n")

print(parsear_config("config.txt"))''' 