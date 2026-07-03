# Utilidades

El módulo `apklis.utils` contiene funciones auxiliares y utilidades de formateo para la presentación de datos legibles por humanos (tamaño de archivo, velocidades de descarga, etc.).

---

## `sizeof_fmt`

```python
def sizeof_fmt(num: float, suffix: str = "B") -> str
```

Formatea un número flotante de bytes en una cadena de texto legible para humanos utilizando prefijos binarios estándar (K, M, G, T, P, etc.).

**Parámetros:**
- `num` *(float)*: La cantidad de bytes a formatear.
- `suffix` *(str, opcional)*: El sufijo de unidad que se agregará (por defecto `"B"`).

**Retorna:**
- `str`: Cadena formateada de forma compacta (ej. `"68.24MB"`, `"45.96KB"`).

**Ejemplo de uso:**
```python
from apklis import sizeof_fmt

print(sizeof_fmt(1024))          # Imprime "1.00 KB"
print(sizeof_fmt(1048576))       # Imprime "1.00 MB"
print(sizeof_fmt(45000, suffix="")) # Imprime "43.95 K"
```

---

## `format_size`

```python
def format_size(bytes_count: int) -> str
```

Alias directo de `sizeof_fmt` para mantener compatibilidad hacia atrás en integraciones previas.

---

## `format_speed`

```python
def format_speed(bytes_per_second: float) -> str
```

Formatea una tasa de transferencia de datos por segundo utilizando `sizeof_fmt`.

**Parámetros:**
- `bytes_per_second` *(float)*: Velocidad en bytes por segundo.

**Retorna:**
- `str`: Cadena formateada con la velocidad por segundo (ej. `"1.30 M/s"`, `"81.16 K/s"`).
