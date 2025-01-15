# Scraping Quotes 
- This is an exercise repo to scrape quotes from a web.
- The targetted web is `quotes.toscrape.com` which contains pages of quotes from many famous people.
- Some analysis will be done towards the scraped data.
- The workflow of the scraping is as follows:
    1. Data Scraping:
        
        A function will read all pages in the web and retrieve the desired data which consist of `quote`, `author`, and `tag`. The data will be stored in a CSV file.
  
  2. Data Cleaning:
    
       The cleaner function will remove some special characters in column `quote` as a preparation prior to analysis part. The cleaned data will be stored in a new CSV file, separated from the initial one.

  3. Data Analysis:

        The cleaned data will be analysed to gain insights from them. Further explanation on this section is provided in file `analysis.ipynb`.