import json
from time import sleep
import requests
from urllib.parse import urlparse
from bs4 import BeautifulSoup

def crawler(max_pages):
    urls = []
    start = 1
    while start <= max_pages:
        #~ print(start)
        url = 'https://afroginthefjord.com/category/culture-people/page/' + str(start)
        source_code = requests.get(url, allow_redirects=True).content
        soup = BeautifulSoup(source_code, 'html.parser')

        """Edit scrape here"""
        for scrape in soup.find_all("h1", class_="entry-title"):
            for a in scrape.find_all('a'):
                article = a.get('href')
                urls.append(article)
                print(article)
        """End scrape"""

        start += 1
        sleep(3)

    parsed = urlparse(url).netloc.split('.')[0]
    filename = parsed

    with open(filename + '.json', 'a') as file_object:
        json.dump(urls, file_object, indent=4)
        print(filename, 'exported!')

crawler(1)
