def guardar_config(filepath, config):
    with open(filepath, 'w') as file:
        for clave, valor in config.items():
            file.write(f"{clave}={valor}\n")
config = {'host': '192.168.1.1', 'port': '8080'}
guardar_config("config.txt", config)

print("Archivo guardado exitosamente.")
