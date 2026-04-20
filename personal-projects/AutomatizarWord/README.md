# Automatizacion de archivos Word

# 📝 AutomatizarWord - Cover Letters Automáticas con Python.

Herramienta en Python para generar automáticamente **cartas de presentación (cover letters)** en formato Word (.docx), utilizando plantillas dinámicas y datos desde archivos CSV.

Ideal para agilizar procesos de postulación a múltiples empleos de forma profesional y eficiente.
---

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **docxtpl** → Para crear documentos Word desde plantillas.
- **pandas** → Para leer y procesar archivos CSV.
- **datetime** → Para insertar fechas actuales en los documentos.

---
## 🚀 Características

- Generación masiva de documentos Word
- Uso de plantillas dinámicas con `docxtpl`
- Lectura de datos desde CSV con `pandas`
- CLI configurable (línea de comandos)
- Logging profesional
- Nombres de archivos dinámicos y seguros
- Eliminación de caracteres especiales
- Manejo de duplicados (evita sobreescritura)
- Limpieza automática del directorio de salida
---

## 📄 ¿Cómo funciona?
1. Se utiliza una plantilla de Word (`.docx`) con variables dinámicas como:
   {{ mi_nombre }}
   {{ nombre_empresa }}
   {{ puesto_de_trabajo }}


2. Se proporciona un archivo CSV con los datos:

| company        | job                 |
|----------------|---------------------|
| Google         | Software Engineer   |
| Amazon         | Data Analyst        |

---
3. El script genera automáticamente un documento por cada fila del CSV.

---

### 🔹 Activar entorno

```bash
source venv/bin/activate
1. El script toma cada fila del CSV, llena la plantilla y genera un documento Word personalizado para cada empresa.

---

🔹 Ejecutar
python main.py --name "HugoOnofre"
⚙️ Parámetros disponibles
--template   Ruta de plantilla Word
--csv        Archivo CSV con datos
--output     Carpeta de salida
--name       Nombre del usuario
--verbose    Modo debug
📁 Estructura del proyecto
AutomatizarWord/
│── automatizar_word/
│   ├── generator.py
│   ├── utils.py
│── data/
│── templates/
│── output/
│── main.py
│── requirements.txt
│── README.md
📌 Ejemplo de salida
HugoOnofre_Google_SoftwareEngineer.docx
HugoOnofre_Amazon_DataAnalyst.docx
📦 Instalación
git clone https://github.com/Hugonofre7/Projects-python.git
cd AutomatizarWord
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

👨‍💻 Autor

Hugo Onofre

---
