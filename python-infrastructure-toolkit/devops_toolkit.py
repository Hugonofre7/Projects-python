import argparse
import logging
import requests
import time

from alert_system import configurar_logger, verificar_servicios
from log_cleaner import parse_log_line
from data_exporter import exportar_json, exportar_csv
from servicio import Servicio

def crear_parser():
    parser = argparse.ArgumentParser(description='DevOps Toolkit')
    parser.add_argument('--action', choices=['monitor', 'parse', 'falla'], required=True)
    parser.add_argument('--urls', nargs='+', help='URLs a monitorear')
    parser.add_argument('--log', help='Archivo de log para guardar resultados')
    parser.add_argument('--file', help='Archivo de log a parsear')
    parser.add_argument('--output', help='Archivo de salida JSON')
    parser.add_argument('--servicio', help='Nombre del servicio a simular falla')
    return parser

def main():
    parser = crear_parser()
    args = parser.parse_args()

    if args.action == 'monitor':
        configurar_logger(args.log)
        while True:
            resultados = verificar_servicios(args.urls)
            for url, status in resultados.items():
                logging.info(f"{url} - {status}")
            time.sleep(60)  # Monitorea cada minuto

    elif args.action == 'parse':
        if not args.file or not args.output:
            print("Para parsear logs, se requieren los argumentos --file y --output")
            return
        lineas = []
        with open(args.file, 'r') as f:
            for linea in f:
                resultado = parse_log_line(linea)
                if resultado is not None:
                    lineas.append(resultado)
        exportar_json(lineas, args.output)
        exportar_csv(lineas, args.output.replace('.json', '.csv'))
        print(f"Logs parseados y exportados a {args.output} y {args.output.replace('.json', '.csv')}")

    elif args.action == 'falla':
        if not args.servicio:
            print("Para simular una falla, se requiere el argumento --servicio")
            return
        servicio = Servicio(args.servicio)
        servicio.simular_falla(servicio)
        print(f"Falla simulada para el servicio {args.servicio}")

if __name__ == "__main__":
    main()
    