import requests
from bs4 import BeautifulSoup
import pandas as pd

# List to store scraped data
list_quote = []

# Set a function to scrape the data from the URL above
def data_scraper(url):
    response = requests.get(url)
    print("=== Get response from the web. ===")
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
            next_url = url_base + next_page.find('a')['href']
            print("=== Move to the next page. ===")
            data_scraper(next_url)

    else:
        print(f"=== Failed to retrieve page: {url} ===")

    print("=== Scraping completed. ===")
    print("=== Start storing the scraped data into a CSV file. ===")
    df = pd.DataFrame(list_quote)
    df.to_csv('quotes_raw.csv', index=False)
    print("Done. Data saved to 'quotes_raw.csv'.")