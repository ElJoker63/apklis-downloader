# Cliente de API

El módulo `apklis.api` proporciona las funciones asíncronas para interactuar con las APIs web oficiales de Apklis.cu.

---

## `get_categories`

```python
async def get_categories() -> list
```

Obtiene el listado completo de categorías disponibles para aplicaciones y juegos en Apklis.

**Retorna:**
- `list`: Lista de diccionarios con la información de las categorías (ej. `[{'name': 'Utilidades', 'icon': 'utils', ...}]`).

---

## `get_apps`

```python
async def get_apps() -> dict
```

**Función de compatibilidad original.** Obtiene la estructura JSON completa de las categorías de aplicaciones agrupadas por Apklis.

**Retorna:**
- `dict`: JSON con la paginación y la lista de categorías (ej. `{"count": 10, "results": [...]}`).

---

## `get_applications`

```python
async def get_applications(limit=30, offset=0, ordering=None, category=None, free=None, paid=None) -> list
```

**Función de consulta flexible de aplicaciones.** Obtiene un listado de aplicaciones aplicando paginación, ordenamiento y filtros por precio o categorías.

**Parámetros:**
- `limit` *(int, opcional)*: Cantidad máxima de aplicaciones a retornar (por defecto `30`).
- `offset` *(int, opcional)*: Desplazamiento de paginación (por defecto `0`).
- `ordering` *(str, opcional)*: Campo por el cual ordenar los resultados. Ejemplos comunes:
  - `-download_count` (Más descargadas)
  - `-sale_count` (Más vendidas)
  - `-rating` (Mejor valoradas)
  - `-updated` (Actualizaciones recientes)
- `category` *(str, opcional)*: Filtrar por código de categoría (ej. `"utils"`, `"games"`).
- `free` *(bool, opcional)*: Si es `True`, filtra únicamente aplicaciones gratuitas.
- `paid` *(bool, opcional)*: Si es `True`, filtra únicamente aplicaciones de pago.

**Retorna:**
- `list`: Lista de diccionarios con la metadata de las aplicaciones que cumplen con los criterios.

---

## `search`

```python
async def search(text: str, limit=30, offset=0) -> list
```

Busca aplicaciones que coincidan con la cadena de texto de búsqueda proporcionada.

**Parámetros:**
- `text` *(str)*: El término de búsqueda (ej. `"todus"`).
- `limit` *(int, opcional)*: Límite de resultados (por defecto `30`).
- `offset` *(int, opcional)*: Desplazamiento de paginación (por defecto `0`).

**Retorna:**
- `list`: Una lista de diccionarios con la metadata de las aplicaciones coincidentes.

---

## `get_app_details`

```python
async def get_app_details(package: str) -> dict
```

Obtiene el **diccionario completo de metadatos** de una aplicación sin filtros, tal como lo sirve el servidor oficial de Apklis. Útil para capturar toda la información disponible (desarrollador, screenshots de releases, tamaño, puntuación, etc.).

**Parámetros:**
- `package` *(str)*: Nombre del paquete de la aplicación (ej. `"cu.todus.android"`).

**Retorna:**
- `dict`: Diccionario completo con toda la información de la aplicación.

---

## `get_releases`

```python
async def get_releases(package: str, limit=10, offset=0) -> list
```

Obtiene el historial de lanzamientos (releases) de una aplicación específica. Incluye detalles de changelogs, capturas de pantalla, permisos requeridos, tamaño del archivo y arquitecturas soportadas.

**Parámetros:**
- `package` *(str)*: Nombre del paquete de la aplicación.
- `limit` *(int, opcional)*: Cantidad de lanzamientos a retornar (por defecto `10`).
- `offset` *(int, opcional)*: Desplazamiento de paginación.

**Retorna:**
- `list`: Lista de diccionarios, donde cada uno describe un lanzamiento con sus capturas, permisos y changelog.

---

## `get_release`

```python
async def get_release(package: str) -> dict
```

Obtiene los detalles del **último lanzamiento** (lanzamiento más reciente) disponible para una aplicación.

**Parámetros:**
- `package` *(str)*: Nombre del paquete de la aplicación.

**Retorna:**
- `dict`: Diccionario con las propiedades detalladas del último lanzamiento.

---

## `get_apk_url`

```python
async def get_apk_url(package_name: str) -> str
```

**Función de alto nivel para descargas.** Resuelve el enlace de descarga física del APK para cualquier paquete. Maneja de forma transparente las restricciones de aplicaciones de pago (`Forbidden`) inyectando un token público temporal (`gid`).

**Parámetros:**
- `package_name` *(str)*: Nombre del paquete de la aplicación.

**Retorna:**
- `str`: Enlace de descarga directo completamente funcional.

---

## Funciones heredadas (Compatibilidad)

### `get_info`
```python
async def get_info(package: str) -> tuple
```
Retorna la tupla simplificada de compatibilidad: `(icon_url, name, description, updated_date)`.

### `pays_app`
```python
async def pays_app(offset: str = "0") -> list
```
Retorna las aplicaciones de pago (equivalente a `get_apps(paid=True)`).

### `get_apps_by_category`
```python
async def get_apps_by_category(category: str, offset: str = "0") -> list
```
Retorna aplicaciones de una categoría (equivalente a `get_apps(category=category)`).
