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

lines = leer_config("config.txt")
for line in lines:
    print(line)