# Automatizacion de archivos Word

# 📝 AutomatizarWord - Cover Letters Automáticas con Python.

Este proyecto automatiza la generación de **cartas de presentación (cover letters)** personalizadas para diferentes empresas y vacantes, utilizando plantillas en Word (.docx) y datos en CSV.

Ideal para agilizar procesos de postulación a múltiples empleos de forma profesional y eficiente.
---

## 🛠️ Tecnologías utilizadas
- **Python 3.x**
- **docxtpl** → Para crear documentos Word desde plantillas.
- **pandas** → Para leer y procesar archivos CSV.
- **datetime** → Para insertar fechas actuales en los documentos.

---

## 📄 ¿Cómo funciona?
1. Tienes una plantilla de Word con **variables** (placeholders) como:

2. Usas un archivo CSV con los datos de las vacantes y empresas:
| nombre_empresa | puesto           | nombre_candidato |
|----------------|------------------|------------------|
| Google         | Software Engineer| Hugo García      |
| Amazon         | Data Analyst     | Hugo García      |

3. El script toma cada fila del CSV, llena la plantilla y genera un documento Word personalizado para cada empresa.

---

## ▶️ Ejecución del proyecto

### 1. Instalar dependencias
```bash
pip3 install docxtpl pandas
