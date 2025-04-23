from urllib.parse import urlparse

def extract_favicon_url(site_url):
    try:
        parsed = urlparse(site_url)
        return f"{parsed.scheme}://{parsed.netloc}/favicon.ico"
    except:
        return ""
