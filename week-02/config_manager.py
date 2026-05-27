def leer_config(filepath):
    valid_lines = []
    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                continue
            if line.startswith("#"):
                continue
            valid_lines.append(line)
        return valid_lines

def parsear_config(filepath):
    lines = leer_config(filepath)
    config = {}
    for line in lines:
        clave, valor = line.split("=")
        config[clave] = valor
    return config

print(parsear_config("config.txt"))

