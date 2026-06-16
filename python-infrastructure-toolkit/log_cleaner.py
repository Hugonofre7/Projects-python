import re

def parse_log_line(line):
    pattern = r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (ERROR|WARN|INFO|DEBUG) \[(.+?)\] (.+)'
    
    match = re.match(pattern, line)
    
    if match:
        return {
            'timestamp': match.group(1),
            'level':     match.group(2),
            'service':   match.group(3),
            'message':   match.group(4)
        }
    
    return None


def clasificar_servicio(nombre, estado):
    if estado == "INFO":
        return f"{nombre} está activo ✓"
    elif estado == "WARN":
        return f"{nombre} está inactivo —"
    elif estado == "ERROR":
        return f"{nombre} tiene un error ✗"
    else:
        return f"{nombre} estado desconocido"

def reporte_servicios(servicios):
    for nombre, estado in servicios:
        resultado = clasificar_servicio(nombre, estado)
        print(resultado)

if __name__ == "__main__":
    
    servicios = [
        ("nginx", "INFO"),
        ("mysql", "ERROR"),
        ("redis", "WARN"),
        ("postgres", "INFO")
    ]

    reporte_servicios(servicios)

    line_ok  = "2024-01-15 14:32:01 ERROR [auth-service] Login failed for user: admin"
    line_bad = "--- system startup ---"

    print("Reporte de servicios generado.")
    print(parse_log_line(line_ok))
    print(parse_log_line(line_bad))
