## ⚠️ Nota sobre el Proyecto #57 (Progress Bar)

El código original del libro **omite la inicialización del corchete izquierdo** `'['` en la función `getProgressBar`.

### Error en el código original:
```python
def getProgressBar(progress, total, barWidth=40):
    # ... cálculos ...
    progressBar += BAR * numberOfBars  # ❌ Error: progressBar no está definida
def getProgressBar(progress, total, barWidth=40):
    # ... cálculos ...
    progressBar = '['  # ✅ Inicializar con el corchete izquierdo
    progressBar += BAR * numberOfBars
    progressBar += ' ' * (barWidth - numberOfBars)
    progressBar += ']'
    # ... resto del código ...