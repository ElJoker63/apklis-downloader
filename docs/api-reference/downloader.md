# Descargador

El módulo `apklis.downloader` se encarga de gestionar la descarga física de los archivos APK en streaming de forma asíncrona y emitir eventos de progreso a través de callbacks.

---

## `download_apk`

```python
async def download_apk(url: str, filename: str = None, progress_callback = default_progress_callback) -> str
```

Descarga un APK desde una URL específica.

**Parámetros:**
- `url` *(str)*: La URL directa de descarga (normalmente obtenida con `get_apk_url`).
- `filename` *(str, opcional)*: El nombre del archivo local con el que se guardará el APK. Si no se provee, se extrae del nombre del archivo original de la URL.
- `progress_callback` *(función, opcional)*: Un callback personalizado para supervisar el progreso de la descarga. Por defecto es `default_progress_callback`, el cual dibuja la barra de progreso en la consola. Pasa `None` para desactivar el reporte de progreso.

**Retorna:**
- `str`: El nombre del archivo en el que se guardó el APK descargado.

---

## Callbacks de Progreso Personalizados

La función que definas como `progress_callback` debe aceptar los siguientes cuatro parámetros de entrada posicionales:

```python
def mi_callback(downloaded_bytes: int, total_bytes: int, speed_bytes_per_sec: float, elapsed_time: float):
    # Lógica personalizada
    ...
```

### Ejemplo: Reportar progreso en Telegram (Telethon / Pyrogram)

El callback puede ser una función común o una **coroutine asíncrona** (`async def`). Esto es ideal para integrar la descarga con clientes de mensajería asíncronos:

```python
import apklis

async def callback_telegram(downloaded, total, speed, elapsed):
    percent = (downloaded / total) * 100 if total > 0 else 0
    # Enviar progreso solo cada 10% para no saturar los límites de la API de Telegram
    if int(percent) % 10 == 0:
        await bot.edit_message_text(
            chat_id, 
            message_id, 
            f"Descargando APK...\nProgreso: {percent:.1f}% ({apklis.sizeof_fmt(downloaded)}/{apklis.sizeof_fmt(total)})"
        )

# Descargar usando el callback asíncrono
url = await apklis.get_apk_url("cu.todus.android")
await apklis.download_apk(url, progress_callback=callback_telegram)
```
