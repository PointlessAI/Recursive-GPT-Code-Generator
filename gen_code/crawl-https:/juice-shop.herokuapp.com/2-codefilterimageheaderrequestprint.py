import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'https://juice-shop.herokuapp.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Filter out only relative internal links with anchor ('#')
for link in soup.find_all('a', href=True):
    if not link['href'].startswith(('http', '#')):
        print(urljoin(url, link['href']))

# Extract and print all the source URLs for images
for img in soup.find_all('img', src=True):
    print(urljoin(url, img['src']))

# Update headers to mimic a real browser for better crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
    'Referer': url  # Sending Referer in headers
}
response_with_headers = requests.get(url, headers=headers)
soup_with_headers = BeautifulSoup(response_with_headers.content, 'html.parser')

# Print the entire content including formatted HTML with headers
print(soup_with_headers.prettify())
