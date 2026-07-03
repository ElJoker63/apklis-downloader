import sys
import asyncio
import apklis

# Configure stdout to use UTF-8 to prevent UnicodeEncodeError on Windows terminals
if hasattr(sys.stdout, 'reconfigure'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

async def ejemplo_listar_categorias():
    print("=== Ejemplo 1: Listar Categorías en Apklis ===")
    try:
        categories = await apklis.get_categories()
        print(f"Se encontraron {len(categories)} categorías. Primeras 5:")
        for cat in categories[:5]:
            print(f" - {cat['name']} (Grupo: {cat['group']}, Código: {cat['icon']})")
        print("-" * 50)
    except Exception as e:
        print(f"Error al obtener categorías: {e}")
        print("-" * 50)

async def ejemplo_buscar_y_detalles():
    print("\n=== Ejemplo 2: Buscar y Obtener Detalles de Aplicación ===")
    query = "todus"
    try:
        print(f"Buscando apps que coincidan con '{query}'...")
        search_results = await apklis.search(query, limit=3)
        if not search_results:
            print("No se encontraron resultados.")
            return
            
        print(f"Resultados encontrados: {len(search_results)}")
        first_app = search_results[0]
        package = first_app['package_name']
        print(f"Obteniendo el diccionario completo de detalles para: {package}...")
        
        # get_app_details retorna el diccionario completo de la API sin filtrar
        details = await apklis.get_app_details(package)
        print("\nDetalles completos recibidos:")
        print(f" - Nombre: {details.get('name')}")
        print(f" - Desarrollador: {details.get('developer', 'No especificado')}")
        # En la API real el desarrollador suele estar dentro de una estructura, mostramos lo disponible
        print(f" - Precio: {details.get('price')} CUP")
        print(f" - Descargas: {details.get('download_count')}")
        print(f" - Calificación: {details.get('rating')}")
        print(f" - Base de datos integrada: {details.get('with_db')}")
        print(f" - Icono URL: {details.get('icon')}")
        print("-" * 50)
    except Exception as e:
        print(f"Error en ejemplo de detalles: {e}")
        print("-" * 50)

async def ejemplo_lanzamientos_y_descarga():
    print("\n=== Ejemplo 3: Historial de Lanzamientos y Descarga ===")
    package = "cu.todus.android"
    try:
        print(f"Obteniendo lanzamientos para: {package}...")
        releases = await apklis.get_releases(package, limit=3)
        print(f"Lanzamientos encontrados: {len(releases)}")
        
        for i, rel in enumerate(releases):
            print(f"\n[Release #{i+1}]")
            print(f" - Versión: {rel.get('version_name')} (Código: {rel.get('version_code')})")
            print(f" - Tamaño: {rel.get('size')}")
            print(f" - SDK Mínimo: {rel.get('version_sdk')}")
            print(f" - Target SDK: {rel.get('version_target_sdk')}")
            print(f" - Es pública: {rel.get('public')}")
            print(f" - Arquitecturas (ABIs): {[a.get('abi') for a in rel.get('abi', [])]}")
            # El changelog contiene HTML estructurado
            changelog_clean = rel.get('changelog', '').replace('<p>', '').replace('</p>', '\n').replace('<li>', ' - ').replace('</li>', '\n')
            print(f" - Historial de cambios (Changelog):\n{changelog_clean[:200]}...")
            
        # Intentar descargar el último lanzamiento
        print("\nObteniendo enlace de descarga directo...")
        urldl = await apklis.get_apk_url(package)
        print(f"URL resuelta: {urldl}")
        
        print("Iniciando descarga con progreso...")
        # Descargamos solo un pequeño fragmento de prueba en main
        filename = await apklis.download_apk(urldl)
        print(f"¡APK descargado con éxito!: {filename}")
        print("-" * 50)
    except Exception as e:
        print(f"Error en lanzamientos o descarga: {e}")
        print("-" * 50)

async def main():
    await ejemplo_listar_categorias()
    await ejemplo_buscar_y_detalles()
    await ejemplo_lanzamientos_y_descarga()

if __name__ == "__main__":
    asyncio.run(main())