from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML
from datetime import datetime
import os

# Configuración de rutas
current_dir = os.path.dirname(os.path.abspath(__file__))
output_dir = os.path.join(current_dir, 'ContratoGenerado')
template_dir = current_dir

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
    'cantidad_numeros': '150,000',
    'cantidad_letras': 'ciento cincuenta mil',
}

# Renderizar plantilla
template = env.get_template('plantilla.html')
html_content = template.render(datos_contrato)

# Guardar HTML para debug
debug_html_path = os.path.join(output_dir, 'debug.html')
with open(debug_html_path, 'w', encoding='utf-8') as f:
    f.write(html_content)

# Generar PDF con WeasyPrint
output_pdf = os.path.join(output_dir, f"contrato_{datos_contrato['nombre_comprador']}.pdf")
HTML(string=html_content).write_pdf(output_pdf)

print(f"✅ PDF generado en: {output_pdf}")
print(f"📄 HTML de debug en: {debug_html_path}")

