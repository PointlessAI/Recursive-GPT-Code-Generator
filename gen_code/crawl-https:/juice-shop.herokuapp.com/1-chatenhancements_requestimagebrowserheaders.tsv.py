import requests
from bs4 import BeautifulSoup

url = 'https://juice-shop.herokuapp.com'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Filter out only clickable links
for link in soup.find_all('a', href=True):
    if link['href'].startswith('http'):
        print(link['href'])

# Extract and print all the images on the page
for img in soup.find_all('img'):
    print(img['src'])

# Utilize headers to mimic a real browser for better crawling
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
response_with_headers = requests.get(url, headers=headers)
soup_with_headers = BeautifulSoup(response_with_headers.content, 'html.parser')

# Print the content of the webpage with headers
print(soup_with_headers.prettify())
