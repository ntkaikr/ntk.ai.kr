# carded/utils.py

from urllib.parse import urlparse

def extract_favicon_url(url):
    parsed = urlparse(url)
    domain = parsed.netloc
    return f"https://www.google.com/s2/favicons?domain={domain}"

"""
def extract_favicon_url(site_url):
    try:
        parsed = urlparse(site_url)
        return f"{parsed.scheme}://{parsed.netloc}/favicon.ico"
    except:
        return ""

"""