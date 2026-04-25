def convertir_a_segundos(tiempo: str) -> int:
    horas, minutos, segundos = tiempo.split(":")

    return int(horas) * 3600 + int(minutos) * 60 + int(segundos)