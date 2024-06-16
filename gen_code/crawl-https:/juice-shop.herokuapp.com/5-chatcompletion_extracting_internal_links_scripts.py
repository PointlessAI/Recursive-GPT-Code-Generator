import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://juice-shop.herokuapp.com'

# Send GET request with headers for better crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    'Referer': 'https://www.google.com/'  # Changed Referer to Google's home page for realism
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

def extract_internal_links(url, soup):
    internal_links = set()
    for link in soup.find_all('a', href=True):
        absolute_link = urljoin(url, link['href'])
        if 'juice-shop.herokuapp.com' in absolute_link:
            internal_links.add(absolute_link)
    return internal_links

def extract_script_sources(url, soup):
    script_sources = set()
    for script in soup.find_all('script', src=True):
        absolute_source = urljoin(url, script['src'])
        script_sources.add(absolute_source)
    return script_sources

# Extract and print all internal links
internal_links = extract_internal_links(url, soup)
for link in internal_links:
    print(link)

# Extract and print all script source URLs
script_sources = extract_script_sources(url, soup)
for script in script_sources:
    print(script)
