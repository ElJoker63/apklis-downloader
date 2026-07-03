# apklis-downloader

Bienvenido a la documentación oficial de **apklis-downloader**, un cliente de Python asíncrono, limpio y eficiente diseñado para interactuar con la plataforma cubana **Apklis.cu**.

## ¿Qué es apklis-downloader?

Es una librería asíncrona (basada en `httpx`) que te permite consultar información sobre aplicaciones publicadas en Apklis, obtener sus últimos lanzamientos (releases), y descargar sus archivos APK directamente. Cuenta con un sistema avanzado de barra de progreso que puedes personalizar fácilmente usando callbacks para integrarlo en otras plataformas, como bots de Telegram.

## Características Principales

- ⚡ **Asincronía Completa:** Diseñada con soporte nativo de asincronía utilizando `httpx` para un rendimiento óptimo.
- 🔧 **Manejo Automático de Enlaces Protegidos (Bypass):** Resuelve automáticamente las descargas de aplicaciones de pago o privadas (`Forbidden`) utilizando un token público (`gid`).
- 📥 **Descarga Eficiente en Streaming:** Descarga los archivos fragmento a fragmento en streaming, lo que mantiene bajo el consumo de memoria.
- 📊 **Múltiples Formatos de Progreso:** Incorpora un formateador inteligente (`sizeof_fmt`) para tamaños y velocidad de descarga (MB, KB/s, etc.).
- 🛠️ **Callback de Progreso Personalizable:** Permite pasar funciones callback para enviar el estado de la descarga a interfaces gráficas, logs, o chats de Telegram en tiempo real.

---

> Continúa con la [Instalación](getting-started/installation.md) o salta a los [Primeros Pasos](getting-started/quickstart.md).
