# Primeros Pasos

Este tutorial rápido te mostrará cómo utilizar `apklis-downloader` para consultar información de una app y descargarla en unos pocos pasos utilizando asincronía.

## Consultar y descargar tu primer APK

Para interactuar con la API asíncrona, necesitas ejecutar el código dentro de un bucle de eventos (`asyncio`). Aquí tienes un ejemplo completo que muestra cómo obtener metadatos de toDus y descargar su APK mostrando la barra de progreso integrada:

```python
import asyncio
import sys
import apklis

# Configura la terminal para soportar caracteres unicode en Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    package = "cu.todus.android"
    
    print(f"Buscando información de {package}...")
    # 1. Obtener metadatos básicos
    icon, name, description, updated = await apklis.get_info(package)
    print(f"Nombre: {name}")
    print(f"Última actualización: {updated}")
    
    # 2. Obtener automáticamente el enlace de descarga (resuelve fallbacks si es Forbidden)
    print("\nResolviendo URL de descarga...")
    download_url = await apklis.get_apk_url(package)
    print(f"URL: {download_url}")
    
    # 3. Descargar el archivo APK
    print("\nIniciando descarga...")
    filename = await apklis.download_apk(download_url)
    print(f"\n¡Descargado con éxito! Guardado en: {filename}")

if __name__ == "__main__":
    asyncio.run(main())
```

## Ejecución

Guarda el archivo anterior como `descargar.py` y ejecútalo:

```bash
python descargar.py
```

El script consultará los servidores de Apklis, resolverá el enlace directo o alternativo (en caso de ser un paquete protegido), y comenzará la descarga mostrando una barra de progreso limpia en tu consola con el tamaño formateado (MB) y velocidad en tiempo real.

---

Para aprender a capturar el progreso y enviarlo a un chat de Telegram o usar callbacks personalizados, revisa la sección del **[Descargador](../api-reference/downloader.md)**.
