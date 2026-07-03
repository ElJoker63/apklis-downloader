import time
import httpx
import sys
import asyncio
from .utils import sizeof_fmt

def default_progress_callback(downloaded, total, speed, elapsed):
    """Prints a standard command-line progress bar."""
    if total > 0:
        percent = (downloaded / total) * 100
        bar_length = 30
        filled_length = int(bar_length * downloaded // total)
        
        # Detect if terminal/stdout supports unicode block characters
        try:
            bar = '█' * filled_length + '░' * (bar_length - filled_length)
            if hasattr(sys.stdout, 'encoding') and sys.stdout.encoding:
                bar.encode(sys.stdout.encoding)
        except (UnicodeEncodeError, LookupError):
            bar = '#' * filled_length + '-' * (bar_length - filled_length)
            
        print(f"\rDownloading: |{bar}| {percent:.1f}% ({sizeof_fmt(downloaded)}/{sizeof_fmt(total)}) at {sizeof_fmt(speed, suffix='')}/s", end="", flush=True)
    else:
        print(f"\rDownloading: {sizeof_fmt(downloaded)} at {sizeof_fmt(speed, suffix='')}/s...", end="", flush=True)

async def download_apk(url, filename=None, progress_callback=default_progress_callback):
    """
    Downloads an APK from the given URL asynchronously.
    
    :param url: The direct download URL of the APK.
    :param filename: Optional filename. If not provided, it is parsed from the URL.
    :param progress_callback: A callback function (sync or async) with signature:
                              callback(downloaded_bytes: int, total_bytes: int, speed_bytes_per_sec: float, elapsed_time: float)
                              Pass None to disable progress reporting.
    """
    if not filename:
        filename = url.split('/')[-1].split('?')[0]
        
    async with httpx.AsyncClient() as client:
        try:
            async with client.stream("GET", url) as response:
                response.raise_for_status()
                total_size = int(response.headers.get('content-length', 0))
                
                written = 0
                start_time = time.time()
                
                with open(filename, "wb") as f:
                    async for chunk in response.aiter_bytes(chunk_size=1024 * 8):
                        if chunk:
                            f.write(chunk)
                            written += len(chunk)
                            
                            elapsed_time = time.time() - start_time
                            speed = written / elapsed_time if elapsed_time > 0 else 0
                            
                            if progress_callback:
                                if asyncio.iscoroutinefunction(progress_callback):
                                    await progress_callback(written, total_size, speed, elapsed_time)
                                else:
                                    progress_callback(written, total_size, speed, elapsed_time)
        except httpx.HTTPError as e:
            raise RuntimeError(f"Failed to initiate download: {e}")
            
    if progress_callback == default_progress_callback:
        print()  # Move to the next line
    return filename
