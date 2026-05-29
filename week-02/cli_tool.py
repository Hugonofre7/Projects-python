import argparse
from config_manager import parsear_config, guardar_config

def crear_parser():
    parser = argparse.ArgumentParser(description='Herramienta de línea de comandos para gestionar configuraciones.')
    parser.add_argument('--action', choices=['read', 'save'], required=True, help='Acción a realizar')
    parser.add_argument('--file', required=True, help='Ruta al archivo de configuración')
    return parser

def main():
    parser = crear_parser()
    args = parser.parse_args()

    if args.action == 'read':
        config = parsear_config(args.file)
        print(f"Configuración leída desde {args.file}: {config}")
    elif args.action == 'save':
        config = {'host': '192.168.1.1', 'port': '8080'}
        guardar_config(args.file, config)
        print(f"Configuración guardada en {args.file}.")
if __name__ == "__main__":
    main()

