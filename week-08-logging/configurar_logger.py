import logging

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

if __name__ == "__main__":
    logger = configurar_logger("mi_logger", "app.log")
    logger.debug("Logger configurado correctamente")
    logger.info("Servidor iniciado")
    logger.error("No se pudo conectar a la base de datos")


