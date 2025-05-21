from jinja2 import Environment, FileSystemLoader
import pdfkit
from datetime import datetime
import os

# Configuración de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = current_dir 
output_dir = os.path.join(current_dir, 'ContratoGenerado')

# Crear directorios si no existen
os.makedirs(output_dir, exist_ok=True)

# Configuración de Jinja2
env = Environment(loader=FileSystemLoader(template_dir))

# Datos de ejemplo para el contrato
datos_contrato = {
    'fecha_actual': datetime.now().strftime('%d %b %Y'),
    'localidad': 'Ciudad de México',
    'nombre_vendedor': 'Ana López',
    'nif_vendedor': '12345678A',
    'localidad_vendedor': 'ciudad de México',
    'calle_vendedor': 'Independencia',
    'numero_vendedor': '089',
    'cp_vendedor': '01800',
    'nombre_comprador': 'Hugo Onofre',
    'nif_comprador': '87654321B',
    'localidad_comprador': 'Valencia',
    'calle_comprador': 'Avenida del Puerto',
    'numero_comprador': '456',
    'cp_comprador': '01800',
    'descripcion_bien': 'un vehículo modelo Toyota Corolla del año 2015',
    'cantidad_numeros': '10,000',
    'cantidad_letras': 'diez mil',
}

# Renderizar plantilla
template = env.get_template('plantilla.html')
html_content = template.render(datos_contrato)

# Guardar HTML para debug (opcional)
with open(os.path.join(output_dir, 'debug.html'), 'w') as f:
    f.write(html_content)

# Configurar pdfkit (macOS)
config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf'))
options = {
    'encoding': 'UTF-8',
    'enable-local-file-access': None  # Necesario para cargar CSS/local files
}

# Generar PDF
try:
    output_pdf = os.path.join(output_dir, f"contrato_{datos_contrato['nombre_comprador']}.pdf")
    pdfkit.from_string(
        html_content, 
        output_pdf, 
        options=options, 
        configuration=config,
        verbose=True  # Mostrar logs detallados
    )
    print(f"✅ PDF generado con éxito en: {output_pdf}")
except Exception as e:
    print(f"❌ Error: {e}")