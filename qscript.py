import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from data_scraping import data_scraper
from data_cleaning import data_cleaner

# URL of the website to scrape
url_base = "http://quotes.toscrape.com"

# Scrape the data
scraped_data = data_scraper(url_base)

# Save the raw scraped data into a CSV format
raw_file = "quotes_raw.csv"
scraped_data.to_csv(raw_file, index=False)

# Clean the CSV data: remove special characters in column `quote`
cleaned_file = "quotes_clean.csv"
data_cleaner(raw_file, cleaned_file)

# Load the cleaned data for analysis
data = pd.read_csv(cleaned_file)

# Print the first 5 rows of the data
print(data.head())