import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from concurrent.futures import ThreadPoolExecutor, as_completed

def save_file(content, folder, filename):
    if not os.path.exists(folder):
        os.makedirs(folder)

    safe_filename = "".join(
        [c for c in filename if c.isalpha() or c.isdigit() or c in (' ', '.', '_', '-')]
    ).rstrip() or "file"

    filepath = os.path.join(folder, safe_filename)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Saved: {filepath}")

def _fetch_and_save_css(session, headers, base_url, css_href, output_folder, i):
    absolute_css_url = urljoin(base_url, css_href)

    # (connect timeout, read timeout)
    css_response = session.get(absolute_css_url, headers=headers, timeout=(5, 15), allow_redirects=True)
    css_response.raise_for_status()

    css_filename = os.path.basename(urlparse(absolute_css_url).path)
    if not css_filename.endswith(".css") or not css_filename:
        css_filename = f"style_{i}.css"

    save_file(css_response.text, output_folder, css_filename)
    return absolute_css_url

def extract_html_and_css(url, max_workers=10):
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120 Safari/537.36"
    }

    # Reuse connections
    session = requests.Session()

    print(f"Fetching HTML: {url}")
    html_resp = session.get(url, headers=headers, timeout=(5, 20), allow_redirects=True)
    html_resp.raise_for_status()
    html_content = html_resp.text

    domain = urlparse(url).netloc
    output_folder = f"downloaded_{domain.replace('.', '_')}"
    save_file(html_content, output_folder, "index.html")

    soup = BeautifulSoup(html_content, "html.parser")
    css_links = [link.get("href") for link in soup.find_all("link", rel="stylesheet")]
    css_links = [c for c in css_links if c]  # remove None

    print(f"Found {len(css_links)} external CSS files.")

    # Fetch CSS concurrently
    futures = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        for i, href in enumerate(css_links):
            futures.append(executor.submit(_fetch_and_save_css, session, headers, url, href, output_folder, i))

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

if __name__ == "__main__":
    target_url = input("Enter the website URL (e.g., https://www.example.com): ").strip()
    extract_html_and_css(target_url, max_workers=12)
