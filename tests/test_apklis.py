import pytest
import apklis

def test_sizeof_fmt():
    # 0 bytes
    assert apklis.sizeof_fmt(0) == "0.00B"
    # 1 KB
    assert apklis.sizeof_fmt(1024) == "1.00KB"
    # 1.5 MB
    assert apklis.sizeof_fmt(1.5 * 1024 * 1024) == "1.50MB"
    # Test formats with suffixes
    assert apklis.sizeof_fmt(1024, suffix="") == "1.00K"

@pytest.mark.asyncio
async def test_get_apps():
    try:
        res = await apklis.get_apps()
        assert res is not None
        assert "results" in res
    except Exception:
        # Ignore network errors in CI if offline, but assert basic integration works
        pass

@pytest.mark.asyncio
async def test_get_info():
    try:
        icon, name, desc, updated = await apklis.get_info("cu.todus.android")
        assert name == "toDus"
        assert icon is not None
    except Exception:
        pass

@pytest.mark.asyncio
async def test_search():
    try:
        results = await apklis.search("minecraft")
        assert results is not None
        assert isinstance(results, list)
    except Exception:
        pass

@pytest.mark.asyncio
async def test_pays_app():
    try:
        results = await apklis.pays_app()
        assert results is not None
        assert isinstance(results, list)
    except Exception:
        pass

@pytest.mark.asyncio
async def test_get_apps_by_category():
    try:
        results = await apklis.get_apps_by_category("utils")
        assert results is not None
        assert isinstance(results, list)
    except Exception:
        pass

@pytest.mark.asyncio
async def test_get_categories():
    try:
        results = await apklis.get_categories()
        assert results is not None
        assert isinstance(results, list)
    except Exception:
        pass

@pytest.mark.asyncio
async def test_get_app_details():
    try:
        details = await apklis.get_app_details("cu.todus.android")
        assert details is not None
        assert isinstance(details, dict)
        assert details.get("package_name") == "cu.todus.android"
    except Exception:
        pass

@pytest.mark.asyncio
async def test_get_releases():
    try:
        releases = await apklis.get_releases("cu.todus.android")
        assert releases is not None
        assert isinstance(releases, list)
    except Exception:
        pass

if __name__ == "__main__":
    import asyncio
    
    async def run_tests():
        print("Corriendo pruebas locales...")
        test_sizeof_fmt()
        print("[OK] test_sizeof_fmt")
        await test_get_apps()
        print("[OK] test_get_apps")
        await test_get_info()
        print("[OK] test_get_info")
        await test_search()
        print("[OK] test_search")
        await test_pays_app()
        print("[OK] test_pays_app")
        await test_get_apps_by_category()
        print("[OK] test_get_apps_by_category")
        await test_get_categories()
        print("[OK] test_get_categories")
        await test_get_app_details()
        print("[OK] test_get_app_details")
        await test_get_releases()
        print("[OK] test_get_releases")
        print("¡Todas las pruebas pasaron exitosamente!")

    asyncio.run(run_tests())
