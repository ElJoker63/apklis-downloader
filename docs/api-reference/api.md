# Cliente de API

El módulo `apklis.api` proporciona las funciones asíncronas para interactuar con las APIs web oficiales de Apklis.cu.

---

## `get_info`

```python
async def get_info(package: str) -> tuple
```

Obtiene metadatos informativos básicos de una aplicación específica por su identificador de paquete (package name).

**Parámetros:**
- `package` *(str)*: Nombre del paquete de la aplicación (ej. `"cu.todus.android"`).

**Retorna:**
- `tuple`: Una tupla conteniendo `(icon_url, name, description, updated_date)`.

---

## `get_release`

```python
async def get_release(package: str) -> dict
```

Obtiene la información detallada del último lanzamiento (release) disponible para una aplicación.

**Parámetros:**
- `package` *(str)*: Nombre del paquete de la aplicación.

**Retorna:**
- `dict`: Diccionario con las propiedades del release (ej. `sha256`, `version_name`, `version_code`, `public`, etc.).

---

## `get_download_url`

```python
async def get_download_url(release_sha256: str) -> dict
```

Envía una solicitud POST a Apklis para obtener el enlace de descarga del release correspondiente al SHA256 proporcionado.

**Parámetros:**
- `release_sha256` *(str)*: El hash SHA256 del lanzamiento de la aplicación.

**Retorna:**
- `dict`: Diccionario con la URL de descarga o detalles del error (como `{"detail": "Forbidden"}` para apps de pago).

---

## `get_apk_url`

```python
async def get_apk_url(package_name: str) -> str
```

**Función de alto nivel.** Obtiene automáticamente la URL de descarga lista para descargar para cualquier aplicación. Si la descarga directa devuelve un error `Forbidden` (debido a restricciones de compra/pago de la app), resuelve automáticamente el bypass a través de un token público (`gid`).

**Parámetros:**
- `package_name` *(str)*: Nombre del paquete de la aplicación.

**Retorna:**
- `str`: Enlace de descarga directo o alternativo completamente funcional.

---

## `search`

```python
async def search(text: str) -> list
```

Busca aplicaciones en la plataforma Apklis que coincidan con el texto de búsqueda proporcionado.

**Parámetros:**
- `text` *(str)*: El término de búsqueda (ej. `"minecraft"`).

**Retorna:**
- `list`: Una lista de diccionarios, donde cada diccionario contiene información del paquete de la aplicación coincidente.

---

## `pays_app`

```python
async def pays_app(offset: str = "0") -> list
```

Obtiene el listado de aplicaciones de pago (con precio mayor a cero) disponibles en la plataforma.

**Parámetros:**
- `offset` *(str, opcional)*: El desplazamiento para la paginación (por defecto `"0"`).

**Retorna:**
- `list`: Una lista de diccionarios con la información de las aplicaciones de pago encontradas.

---

## `get_apps_by_category`

```python
async def get_apps_by_category(category: str, offset: str = "0") -> list
```

Recupera las aplicaciones asociadas a una categoría específica.

**Parámetros:**
- `category` *(str)*: El identificador o nombre de la categoría (ej. `"utils"`).
- `offset` *(str, opcional)*: El desplazamiento para la paginación.

**Retorna:**
- `list`: Una lista de diccionarios de las aplicaciones pertenecientes a la categoría.
