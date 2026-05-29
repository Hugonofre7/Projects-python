import argparse

def crear_parser():
    parser = argparse.ArgumentParser(description='Herramienta de línea de comandos para gestionar configuraciones.')
    parser.add_argument('--action', choices=['read', 'save'], required=True, help='Acción a realizar')
    parser.add_argument('--file', required=True, help='Ruta al archivo de configuración')
    return parser