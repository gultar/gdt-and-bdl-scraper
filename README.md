# Scraper for the Grand dictionnaire terminologique (GDT) and the Banque de dépannage linguistique (BDL)

This Python script, `search_vitrinelinguistique.py`, allows you to automate searches on the Vitrine linguistique website (https://vitrinelinguistique.oqlf.gouv.qc.ca/) using the Playwright library with Chromium. It is designed to search for a specific query term on the website and extract information from the search results, including term details, links, descriptions, and associated domains.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:

1. Python: Ensure you have Python 3.7 or higher installed on your system.
2. Playwright: You need to have the Playwright library installed. You can install it using pip:

   ```
   pip install playwright
   ```

3. Chromium: This script uses Chromium as the browser. Playwright will automatically download Chromium for you.

## Usage

To use the `search_vitrinelinguistique.py` script, follow these steps:

1. Import the necessary modules at the beginning of your Python script:

   ```python
   import asyncio
   from playwright.async_api import async_playwright
   from search_vitrinelinguistique import search_vitrinelinguistique
   ```

2. Create an asynchronous function to call `search_vitrinelinguistique` and pass your desired search query:

   ```python
   async def main():
       query_string = "your_search_query_here"
       results = await search_vitrinelinguistique(query_string)
       # Process and use the 'results' data as needed.
       print(results)  # You can modify this to suit your needs.
   ```

3. Run the event loop to execute the search and data extraction:

   ```python
   if __name__ == '__main__':
       loop = asyncio.get_event_loop()
       loop.run_until_complete(main())
   ```

4. Replace `"your_search_query_here"` with the actual search term you want to look up on the Vitrine linguistique website.

5. Run your Python script, and it will perform the search and extract information from the Vitrine linguistique website.

## Functionality

The script performs the following steps:

1. Launches a Chromium browser.
2. Navigates to the Vitrine linguistique website.
3. Enters the search query into the search input field.
4. Clicks the search button.
5. Extracts information from each search result, including term, link, description, and associated domains.
6. Returns the results as a list of dictionaries.

The script also handles cases where no search results are found and returns an empty array.

You can further customize the script to suit your specific needs, such as processing or displaying the extracted data differently.
