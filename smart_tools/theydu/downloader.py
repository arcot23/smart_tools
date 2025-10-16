"""
downloader.py
-------------
A utility module to download any MIME type from a given URL
and save it to a specified local directory.

Usage:
    from downloader import download_file

    download_file(
        url="https://example.com/sample.pdf",
        output_dir="downloads"
    )
"""

import os
import mimetypes
import requests
from urllib.parse import urlparse


def download_file(url: str, output_dir: str = ".", chunk_size: int = 8192, **kwargs) -> str:
    """
    Downloads any file (any MIME type) from the given URL to the specified folder.

    Args:
        url (str): Direct URL to the file.
        output_dir (str): Directory to save the file. Defaults to current directory.
        chunk_size (int): Bytes per download iteration for large files.

    Returns:
        str: Absolute path to the downloaded file.

    Raises:
        ValueError: If the URL is invalid or unreachable.
        requests.RequestException: For any HTTP/network errors.
    """
    if not url or not url.startswith(("http://", "https://")):
        raise ValueError("Invalid URL provided.")

    os.makedirs(output_dir, exist_ok=True)

    try:
        with requests.get(url, stream=True, timeout=30, proxies = kwargs.get('proxies', {})) as response:
            response.raise_for_status()

            # Try to extract filename
            filename = _get_filename_from_response(response, url)
            file_path = os.path.join(output_dir, filename)

            # Stream download to avoid loading whole file in memory
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=chunk_size):
                    if chunk:
                        file.write(chunk)

        return os.path.abspath(file_path)

    except requests.RequestException as e:
        raise ValueError(f"Failed to download file: {e}")


def _get_filename_from_response(response, url: str) -> str:
    """
    Derives a sensible filename from Content-Disposition header or URL.
    """
    cd = response.headers.get("content-disposition")
    if cd and "filename=" in cd:
        filename = cd.split("filename=")[1].strip('"; ')
    else:
        parsed = urlparse(url)
        filename = os.path.basename(parsed.path)

    # Fallback for URLs without filenames (e.g., query-based downloads)
    if not filename:
        mime_type = response.headers.get("Content-Type", "application/octet-stream")
        ext = mimetypes.guess_extension(mime_type.split(";")[0].strip()) or ".bin"
        filename = f"download{ext}"

    return filename


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Download any file (any MIME type) from a given URL to a local folder."
    )
    parser.add_argument(
        "url",
        type=str,
        help="The direct URL of the file to download."
    )
    parser.add_argument(
        "-o", "--output-dir",
        type=str,
        default=".",
        help="Target directory to save the downloaded file (default: .)."
    )
    parser.add_argument(
        "-c", "--chunk-size",
        type=int,
        default=8192,
        help="Chunk size in bytes for streaming download (default: 8192)."
    )

    args = parser.parse_args()

    try:
        saved_path = download_file(
            url=args.url,
            output_dir=args.output_dir,
            chunk_size=args.chunk_size
        )
        print(f"✅ File successfully downloaded to: {saved_path}")
    except Exception as e:
        print(f"❌ Download failed: {e}")
