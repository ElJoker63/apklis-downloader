<h1 align="center">📥 apklis-downloader</h1>

<p align="center">
  <a href="https://pypi.org/project/apklis-downloader/"><img src="https://img.shields.io/pypi/v/apklis-downloader" alt="PyPI"></a>
  <a href="https://pypi.org/project/apklis-downloader/"><img src="https://img.shields.io/pypi/pyversions/apklis-downloader" alt="Python"></a>
  <a href="https://github.com/ElJoker63/apklis-downloader/actions/workflows/ci.yml"><img src="https://github.com/ElJoker63/apklis-downloader/actions/workflows/ci.yml/badge.svg?branch=main" alt="Tests"></a>
  <a href="https://github.com/ElJoker63/apklis-downloader/actions/workflows/pypi-publish.yml"><img src="https://github.com/ElJoker63/apklis-downloader/actions/workflows/pypi-publish.yml/badge.svg?branch=main" alt="Publish"></a>
  <a href="https://eljoker63.github.io/apklis-downloader"><img src="https://img.shields.io/badge/docs-MkDocs-blueviolet" alt="Docs"></a>
  <a href="https://github.com/ElJoker63/apklis-downloader/blob/main/LICENSE"><img src="https://img.shields.io/badge/license-MIT-blue" alt="License"></a>
</p>

<p align="center"><strong>Cliente Python Asíncrono para Apklis.cu</strong> — descarga APKs y consulta la información completa de la plataforma.</p>

<p align="center">
  <a href="https://eljoker63.github.io/apklis-downloader"><b>📖 LEER LA DOCUMENTACIÓN COMPLETA AQUÍ 📖</b></a>
</p>

---

## ⚡ ¿Qué es apklis-downloader?

Es una librería moderna, asíncrona y de alto rendimiento para interactuar con la plataforma cubana **Apklis.cu**. Te permite realizar búsquedas de aplicaciones, filtrar por categorías, paginar resultados, obtener el historial completo de lanzamientos (incluyendo changelogs y capturas de pantalla) y descargar archivos APK con una barra de progreso altamente personalizable.

Además, cuenta con resolución automática de enlaces de descarga protegidos (Forbidden) usando una cuenta pública (`gid`).

---

## 📦 Instalación

```bash
pip install apklis-downloader
```

---

## 🚀 Uso Rápido

El siguiente ejemplo muestra cómo realizar consultas avanzadas y descargar un APK de forma asíncrona:

```python
import asyncio
import sys
import apklis

# Configura la terminal para soportar caracteres unicode en Windows
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

async def main():
    package = "cu.todus.android"
    
    # 1. Obtener el diccionario completo de detalles de la app
    app_details = await apklis.get_app_details(package)
    print(f"Nombre: {app_details.get('name')}")
    print(f"Descargas totales: {app_details.get('download_count')}")
    
    # 2. Obtener historial de lanzamientos
    releases = await apklis.get_releases(package, limit=2)
    print(f"Última versión disponible: {releases[0].get('version_name')}")
    
    # 3. Resolver la URL de descarga automáticamente (incluye bypass si es Forbidden)
    download_url = await apklis.get_apk_url(package)
    
    # 4. Descargar mostrando la barra de progreso
    await apklis.download_apk(download_url)

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 📚 Documentación y Recursos

Toda la información detallada sobre **autenticación, callbacks de progreso personalizados (ej. para bots de Telegram), referencia completa de APIs y utilidades** la encontrarás en nuestro sitio web oficial de documentación:

👉 **[https://eljoker63.github.io/apklis-downloader](https://eljoker63.github.io/apklis-downloader)**

- **Apklis oficial:** [Apklis](https://www.apklis.cu)
- **PyPI:** [apklis-downloader](https://pypi.org/project/apklis-downloader/)
- **Contribuir:** [CONTRIBUTING.md](CONTRIBUTING.md)

---
<p align="center">Desarrollado con ❤️ por ElJoker63. </>+☕️=z17</p>
