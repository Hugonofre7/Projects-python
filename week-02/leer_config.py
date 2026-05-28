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

lines = leer_config("no_existe.txt")
print(lines)