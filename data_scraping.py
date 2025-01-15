import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# List to store scraped data
list_quote = []

# Set a function to scrape the data from the URL above
def data_scraper(url):
    print("=== Get response from the web. ===")
    response = requests.get(url)
    if response.status_code == 200:
        print("=== Status code 200. ===")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Retrieve quotes
        quotes = soup.find_all('div', class_='quote')
        print("=== Start scraping. ===")
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            list_quote.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        print("=== Done scraping. ===")

        # Find the next page link
        next_page = soup.find('li', class_='next')
        if next_page:
            page = next_page.find('a')['href']

            if bool(re.search('/page.*', url)):
                next_url = re.sub('/page.*', page, url)
            
            else:
                next_url = url + page

            print("=== Move to the next page. ===")
            data_scraper(next_url)
        
        else:
            print("=== All pages have been covered. ===")
            print("=== Scraping completed. ===")
            print("=== Create a dataframe to store the scraped data. ===")
            df = pd.DataFrame(list_quote)
            print("=== The data have been stored in the dataframe. ===")

    else:
        print(f"=== Failed to retrieve page: {url} ===")