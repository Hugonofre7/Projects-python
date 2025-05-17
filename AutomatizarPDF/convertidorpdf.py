import pdfkit
import jinja2
from datetime import datetime

my_name = "Hugo"
item1 = "TV"
item2 = "Refrigerator"
item3 = "Mueble"
today_date = datetime.today().strftime("%d-%b-%Y")

context = {'my_name': my_name, 'item1': item1, 'item2': item2, 'item3': item3,
           'today_date': today_date}

# Load the HTML template
template_loader = jinja2.FileSystemLoader(searchpath="./")
template_env = jinja2.Environment(loader=template_loader)

html_template = 'plantilla.html'
template = template_env.get_template(html_template)
template.render(context)

pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
