import logging
import time
import requests


def configurar_logger(nombre, archivo_log):
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.DEBUG)
    
    consola = logging.StreamHandler()
    archivo = logging.FileHandler(archivo_log)
    
    formato = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    consola.setFormatter(formato)
    archivo.setFormatter(formato)
    
    logger.addHandler(consola)
    logger.addHandler(archivo)
    
    return logger

def verificar_url(url):
    try:
        response = requests.get(url)
        return {
            'url': url,
            'status_code': response.status_code,
            'disponible': response.status_code == 200
        }
    except requests.exceptions.ConnectionError:
        return {
            'url': url,
            'status_code': None,
            'disponible': False
        }
        
def verificar_servicios(urls):
    resultados = []
    for url in urls:
        resultado = verificar_url(url)
        resultados.append(resultado)
    return resultados


def monitor_servicios(urls, archivo_log, intervalo=60):
    try:
        logger = configurar_logger("monitor_logger", archivo_log)
        while True:
            resultados = verificar_servicios(urls)
            for resultado in resultados:
                if resultado["disponible"]:
                    logger.info(f"{resultado['url']} está disponible (status: {resultado['status_code']})")
                else:
                    logger.error(f"{resultado['url']} NO está disponible (disponible: {resultado['disponible']})")
            time.sleep(intervalo)
    except KeyboardInterrupt:
        logger.info("Monitor detenido por el usuario")

if __name__ == "__main__":
    monitor_servicios(
        ["https://www.google.com", "https://url-que-no-existe-123456.com"],
        "servicios.log",
        intervalo=10
    )
