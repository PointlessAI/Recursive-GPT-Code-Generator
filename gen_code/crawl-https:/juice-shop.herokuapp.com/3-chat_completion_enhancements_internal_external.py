import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://juice-shop.herokuapp.com'

# Send GET request with headers for better crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': 'https://google.com'  # Change the Referer to a search engine
}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'html.parser')

# Enhancement 1: Crawl all internal links, not just relative ones
for link in soup.find_all('a', href=True):
    print(urljoin(url, link['href']))

# Enhancement 2: Extract and print all script source URLs
for script in soup.find_all('script', src=True):
    print(urljoin(url, script['src']))

# Enhancement 3: Extract and print all style source URLs
for style in soup.find_all('link', rel='stylesheet'):
    print(urljoin(url, style['href']))
