# ===================== IMPORT REQUIRED MODULES =====================

import os                                  # For folder and file handling
import requests                            # For making HTTP requests
from bs4 import BeautifulSoup              # For parsing HTML
from urllib.parse import urljoin, urlparse # For URL manipulation
from concurrent.futures import ThreadPoolExecutor, as_completed
                                           # For concurrent (parallel) execution


# ===================== FILE SAVE FUNCTION =====================

def save_file(content, folder, filename):
    """
    Saves given text content (HTML or CSS) into a file inside the given folder.
    """

    # Create the folder if it does not already exist
    if not os.path.exists(folder):
        os.makedirs(folder)

    # Sanitize filename by allowing only safe characters
    safe_filename = "".join(
        [c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '.', '_', '-')]
    ).rstrip() or "file"   # Fallback name if filename becomes empty

    # Create full file path
    filepath = os.path.join(folder, safe_filename)

    # Write content to file using UTF-8 encoding
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved: {filepath}")


# ===================== WORKER FUNCTION FOR CSS DOWNLOAD =====================

def _fetch_and_save_css(session, headers, base_url, css_href, output_folder, i):
    """
    Downloads a single CSS file and saves it.
    This function is executed by multiple threads concurrently.
    """

    # Convert relative CSS URL to absolute URL
    absolute_css_url = urljoin(base_url, css_href)

    # Fetch CSS file with timeout (connect timeout, read timeout)
    css_response = session.get(
        absolute_css_url,
        headers=headers,
        timeout=(5, 15),
        allow_redirects=True
    )

    # Raise error if HTTP response is not successful
    css_response.raise_for_status()

    # Extract CSS filename from URL
    css_filename = os.path.basename(urlparse(absolute_css_url).path)

    # If filename is missing or invalid, generate a default name
    if not css_filename.endswith(".css") or not css_filename:
        css_filename = f"style_{i}.css"

    # Save the CSS file locally
    save_file(css_response.text, output_folder, css_filename)

    # Return URL for logging success
    return absolute_css_url


# ===================== MAIN EXTRACTION FUNCTION =====================

def extract_html_and_css(url, max_workers=10):
    """
    Downloads HTML of a webpage and all linked external CSS files using multithreading.
    """

    # HTTP headers to mimic a real browser
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/120 Safari/537.36"
        )
    }

    # Create a session to reuse HTTP connections
    session = requests.Session()

    print(f"Fetching HTML: {url}")

    # Fetch main HTML page
    html_resp = session.get(
        url,
        headers=headers,
        timeout=(5, 20),
        allow_redirects=True
    )

    # Raise error if HTML request fails
    html_resp.raise_for_status()

    # Extract HTML content
    html_content = html_resp.text

    # Create output folder based on domain name
    domain = urlparse(url).netloc
    output_folder = f"downloaded_{domain.replace('.', '_')}"

    # Save HTML file as index.html
    save_file(html_content, output_folder, "index.html")

    # Parse HTML to locate all linked CSS files
    soup = BeautifulSoup(html_content, "html.parser")
    css_links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]

    # Remove None values
    css_links = [c for c in css_links if c]

    print(f"Found {len(css_links)} external CSS files.")

    # ===================== CONCURRENT CSS FETCHING =====================

    futures = []

    # Create thread pool to download CSS files in parallel
    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        # Submit CSS download tasks
        for i, href in enumerate(css_links):
            futures.append(
                executor.submit(
                    _fetch_and_save_css,
                    session,
                    headers,
                    url,
                    href,
                    output_folder,
                    i
                )
            )

        # Track completed tasks
        completed = 0
        for fut in as_completed(futures):
            try:
                css_url = fut.result()
                completed += 1
                print(f"[{completed}/{len(css_links)}] OK: {css_url}")
            except Exception as e:
                completed += 1
                print(f"[{completed}/{len(css_links)}] FAIL: {e}")

    print("\n--- Extraction Complete ---")
    print(f"Check the folder: '{output_folder}'")


# ===================== SCRIPT ENTRY POINT =====================

if __name__ == "__main__":
    # Take website URL as input from user
    target_url = input(
        "Enter the website URL (e.g., https://www.example.com): "
    ).strip()

    # Start extraction with 12 parallel worker threads
    extract_html_and_css(target_url, max_workers=12)
