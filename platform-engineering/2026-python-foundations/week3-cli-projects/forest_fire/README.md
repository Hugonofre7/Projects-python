## Error encontrado en Forest Fire original (#29)

**Error:** `KeyError: (x, y)` al intentar acceder al diccionario forest.

**Causa:** El diccionario solo contiene coordenadas donde hay árboles, no todas las celdas.

### Solución Propuesta

Inicializar el diccionario con **todas las coordenadas** antes de poblarlo con árboles:

```python
# Inicializar todas las celdas como vacías
forest = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        forest[(x, y)] = EMPTY

# Luego agregar árboles en posiciones aleatorias