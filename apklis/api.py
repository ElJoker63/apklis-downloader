import httpx

async def get_apps():
    """Gets the categories list of applications from Apklis asynchronously."""
    api = 'https://api.apklis.cu/v2/category/?group=Applications'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        return response.json()

async def get_info(package):
    """
    Retrieves package information from Apklis asynchronously.
    
    Returns:
        tuple: (icon, name, description, updated)
    """
    api = f'https://api.apklis.cu/v2/application/?package_name={package}'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        if not data.get('results'):
            raise ValueError(f"Package '{package}' not found on Apklis.")
        
        app = data['results'][0]
        return (
            app.get('icon'),
            app.get('name'),
            app.get('description'),
            app.get('updated')
        )

async def get_release(package):
    """Retrieves the latest release details for a package asynchronously."""
    api = f"https://api.apklis.cu/v2/release/?limit=1&offset=0&package_name={package}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        if not data.get('results'):
            raise ValueError(f"No release found for package '{package}'.")
        return data['results'][0]

async def get_download_url(release_sha256):
    """Sends a request to get the download URL for a given release SHA256 asynchronously."""
    api = "https://api.apklis.cu/v2/release/get_url/"
    payload = {"release": release_sha256}
    async with httpx.AsyncClient() as client:
        response = await client.post(api, json=payload)
        if response.status_code == 403:
            return response.json()
        response.raise_for_status()
        return response.json()

def fallback_url(package_name, version, gid_token):
    """Constructs a fallback download URL using a public GID token."""
    return f'https://archive.apklis.cu/application/apk/{package_name}-v{version}.apk?{gid_token}'

async def gid():
    """Retrieves a public GID download token using a known public app asynchronously."""
    # Using the same known public release SHA256 from the original script
    lol = await get_download_url("8da7f305e9763e542b087935714b726fafa3e26105e9e6f96261074c56461ce1")
    url = lol.get('url')
    if not url or '?' not in url:
        raise ValueError("Could not extract GID query token from public package download URL.")
    return url.split('?')[1]

async def get_apk_url(package_name):
    """
    High-level function to automatically resolve the direct or fallback
    download URL for any given package name asynchronously.
    """
    release = await get_release(package_name)
    url_info = await get_download_url(release['sha256'])
    
    if url_info.get('detail') == "Forbidden" or 'url' not in url_info:
        version = release.get('version_code')
        token = await gid()
        return fallback_url(package_name, version, token)
        
    return url_info['url']

async def search(text):
    api = f'https://api.apklis.cu/v2/application/?search={text}&limit=30'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def pays_app(offset="0"):
    api = f"https://api.apklis.cu/v2/application/?price__gt=0&limit=30&offset={offset}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def get_apps_by_category(category, offset="0"):
    api = f"https://api.apklis.cu/v2/application/?categories__in={category}&limit=30&offset={offset}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']