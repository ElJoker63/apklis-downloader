import httpx

async def get_apps():
    """Gets the categories list of applications from Apklis asynchronously."""
    api = 'https://api.apklis.cu/v2/category/?group=Applications'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        return response.json()

async def get_categories():
    """Gets the list of all application and game categories from Apklis."""
    api = 'https://api.apklis.cu/v2/category/'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def get_applications(limit=30, offset=0, ordering=None, category=None, free=None, paid=None):
    """
    Flexible method to retrieve applications with sorting, categories and price filtering.
    
    :param limit: Number of results to return (default 30).
    :param offset: Pagination offset.
    :param ordering: Sort field, e.g. '-download_count', '-sale_count', '-rating', '-updated'.
    :param category: Category code, e.g. 'utils', 'games'.
    :param free: Filter only free apps (True/False).
    :param paid: Filter only paid apps (True/False).
    """
    api = f"https://api.apklis.cu/v2/application/?limit={limit}&offset={offset}"
    if ordering:
        api += f"&ordering={ordering}"
    if category:
        api += f"&categories__in={category}"
    if free:
        api += "&price=0"
    elif paid:
        api += "&price__gt=0"
        
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def search(text, limit=30, offset=0):
    """Searches for applications matching the query string."""
    api = f'https://api.apklis.cu/v2/application/?search={text}&limit={limit}&offset={offset}'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def get_info(package):
    """
    Backward-compatible info helper.
    Returns (icon, name, description, updated) tuple.
    """
    details = await get_app_details(package)
    return (
        details.get('icon'),
        details.get('name'),
        details.get('description'),
        details.get('updated')
    )

async def get_app_details(package):
    """Retrieves the full raw metadata dictionary of an application by its package name."""
    api = f'https://api.apklis.cu/v2/application/?package_name={package}'
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        if not data.get('results'):
            raise ValueError(f"Package '{package}' not found on Apklis.")
        return data['results'][0]

async def get_releases(package, limit=10, offset=0):
    """Retrieves the list of all releases for an application."""
    api = f"https://api.apklis.cu/v2/release/?package_name={package}&limit={limit}&offset={offset}"
    async with httpx.AsyncClient() as client:
        response = await client.get(api)
        response.raise_for_status()
        data = response.json()
        return data['results']

async def get_release(package):
    """Retrieves the latest release details for an application."""
    releases = await get_releases(package, limit=1)
    if not releases:
        raise ValueError(f"No release found for package '{package}'.")
    return releases[0]

async def get_download_url(release_sha256):
    """Sends a request to get the download URL for a given release SHA256."""
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
    """Retrieves a public GID download token using a known public app."""
    # Using the same known public release SHA256 from the original script
    lol = await get_download_url("8da7f305e9763e542b087935714b726fafa3e26105e9e6f96261074c56461ce1")
    url = lol.get('url')
    if not url or '?' not in url:
        raise ValueError("Could not extract GID query token from public package download URL.")
    return url.split('?')[1]

async def get_apk_url(package_name):
    """
    High-level function to automatically resolve the direct or fallback
    download URL for any given package name.
    """
    release = await get_release(package_name)
    url_info = await get_download_url(release['sha256'])
    
    if url_info.get('detail') == "Forbidden" or 'url' not in url_info:
        version = release.get('version_code')
        token = await gid()
        return fallback_url(package_name, version, token)
        
    return url_info['url']

# Backward compatibility functions
async def pays_app(offset="0"):
    """Backward-compatible pays_app helper."""
    return await get_applications(limit=30, offset=offset, paid=True)

async def get_apps_by_category(category, offset="0"):
    """Backward-compatible get_apps_by_category helper."""
    return await get_applications(limit=30, offset=offset, category=category)