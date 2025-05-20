from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import datetime
import os

# Configuración de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'AutomatizarPDF') 
output_dir = os.path.join(current_dir, 'ContratoGenerado')

# Crear directorios si no existen
os.makedirs(template_dir, exist_ok=True)
os.makedirs(output_dir, exist_ok=True)

# Configuración de Jinja2
env = Environment(loader=FileSystemLoader(template_dir))

# Datos de ejemplo para el contrato
datos_contrato = {
    'fecha_actual': datetime.now().strftime('%d %b %Y'),
    'localidad': 'Madrid',
    'nombre_vendedor': 'Ana López',
    'nif_vendedor': '12345678A',
    'localidad_vendedor': 'Barcelona',
    'calle_vendedor': 'Gran Vía',
    'numero_vendedor': '123',
    'cp_vendedor': '08001',
    'nombre_comprador': 'Hugo Onofre',
    'nif_comprador': '87654321B',
    'localidad_comprador': 'Valencia',
    'calle_comprador': 'Avenida del Puerto',
    'numero_comprador': '456',
    'cp_comprador': '46001',
    'descripcion_bien': 'un vehículo modelo Toyota Corolla del año 2015',
    'cantidad_numeros': '10,000',
    'cantidad_letras': 'diez mil',
}

# Nombre del archivo de plantilla
template_name = 'plantilla.html'
template_path = os.path.join(template_dir, template_name)

# Verificar si la plantilla existe
if not os.path.exists(template_path):
    raise FileNotFoundError(f"La plantilla {template_name} no existe en {template_dir}")

# Renderizar la plantilla
template = env.get_template(template_name)
html_content = template.render(datos_contrato)

# Configurar pdfkit (asegúrate de tener wkhtmltopdf instalado)
options = {
    'encoding': 'UTF-8',
    'no-outline': None
}

# Generar PDF
output_pdf = os.path.join(output_dir, f"contrato_{datos_contrato['nombre_cliente']}.pdf")
pdfkit.from_string(html_content, output_pdf, options=options)

print(f"Contrato generado en: {output_pdf}")
