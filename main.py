import sys
import asyncio
import apklis

# Configure stdout to use UTF-8 to prevent UnicodeEncodeError on Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

async def main():
    apps = await apklis.pays_app("0")
    
    for app in apps:
        try:
            # 1. Obtener información de la app
            icon, name, description, updated = await apklis.get_info(app["package_name"])
            release = await apklis.get_release(app["package_name"])
            public_status = '✅' if release.get('public') else '❌'
            
            text = (
                f'Nombre: {name}\n'
                f'Package: {release["package_name"]}\n'
                f'Version: {release["version_name"]}\n'
                f'SHA256: {release["sha256"]}\n'
                f'public: {public_status}'
            )
            print(text)
            
            # 2. Obtener URL de descarga resuelta automáticamente
            urldl = await apklis.get_apk_url(app["package_name"])
            
            # 3. Descargar APK con progreso
            await apklis.download_apk(urldl)
            print("-" * 50)
            
        except Exception as e:
            print(f"Error procesando {app['name']}: {e}")
            print("-" * 50)


async def search():
    apps = await apklis.search("minecraft")
    for app in apps:
        print(app)

if __name__ == "__main__":
    asyncio.run(main())
    #asyncio.run(search())