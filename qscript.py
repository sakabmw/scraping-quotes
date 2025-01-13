import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# URL of the website to scrape
url_base = "http://quotes.toscrape.com/"

# List to store scraped data
list_quote = []

# Set a function to scrape the data from the URL above
def scrape_quote(url):
    response = requests.get(url)
    print("=== Get response from the web ===")
    if response.status_code == 200:
        print("=== Status code 200 ===")
        soup = BeautifulSoup(response.text, 'html.parser')

        # Retrieve quotes
        quotes = soup.find_all('div', class_='quote')
        print("=== Start scraping ===")
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
            list_quote.append({
                'quote': text,
                'author': author,
                'tags': ', '.join(tags)
            })
        print("=== Done scraping ===")

        # Find the next page link
        next_page = soup.find('li', class_='next')
        if next_page:
            next_url = url_base + next_page.find('a')['href']
            print("=== Move to the next page ===")
            scrape_quote(next_url)

    else:
        print(f"=== Failed to retrieve page: {url} ===")

# Start scraping by running the function
scrape_quote(url_base)

# Store list as a dataframe
df = pd.DataFrame(list_quote)

# Clean the values in `quote` by removing curly quotes, periods, and commas
# Store the cleaned values in a new column: `quote_cleaned`
quote_cleaned = [re.sub(r'[“”.,]', '', quote) for quote in df['quote']]
df['quote_cleaned'] = quote_cleaned

# Save data to a CSV file
df.to_csv('quotes.csv', index=False)
print("Scraping completed. Data saved to 'quotes.csv'.")
