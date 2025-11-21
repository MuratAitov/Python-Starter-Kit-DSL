"""
Simple Web Scraper
A beginner-friendly script to scrape web pages and extract information.

Run with: python templates/scraping_templates/simple_scraper.py
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

# ============================================
# CONFIGURATION - Change these values!
# ============================================

# URL to scrape (start with a simple page)
URL = "https://quotes.toscrape.com"  # A website made for practicing scraping!

# Output file
OUTPUT_FILE = "data/processed/scraped_quotes.csv"

# Be respectful - wait between requests (in seconds)
DELAY_SECONDS = 1

# ============================================
# MAIN SCRAPER CODE
# ============================================

def fetch_page(url):
    """
    Fetch a webpage and return its content.
    """
    # Headers to identify ourselves
    headers = {
        'User-Agent': 'Educational Scraper (Digital Scholarship Lab)'
    }

    try:
        print(f"Fetching: {url}")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise error for bad status codes
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None


def parse_quotes_page(html):
    """
    Parse the quotes page and extract quotes, authors, and tags.
    This is specific to quotes.toscrape.com - modify for other sites!
    """
    soup = BeautifulSoup(html, 'html.parser')

    quotes_data = []

    # Find all quote containers
    quotes = soup.find_all('div', class_='quote')

    for quote in quotes:
        # Extract quote text
        text = quote.find('span', class_='text')
        text = text.text.strip() if text else ""

        # Remove quotation marks
        text = text.strip('"').strip('"').strip('"')

        # Extract author
        author = quote.find('small', class_='author')
        author = author.text.strip() if author else ""

        # Extract tags
        tags = quote.find_all('a', class_='tag')
        tags = [tag.text for tag in tags]

        quotes_data.append({
            'quote': text,
            'author': author,
            'tags': ', '.join(tags)
        })

    return quotes_data


def get_next_page_url(html, base_url):
    """
    Find the URL for the next page (if pagination exists).
    """
    soup = BeautifulSoup(html, 'html.parser')

    # Look for "next" button
    next_btn = soup.find('li', class_='next')
    if next_btn:
        next_link = next_btn.find('a')
        if next_link:
            return base_url + next_link.get('href')

    return None


def save_to_csv(data, filename):
    """
    Save the scraped data to a CSV file.
    """
    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"\nSaved {len(data)} items to {filename}")


def main():
    """
    Main scraping function.
    """
    print("=" * 50)
    print("Simple Web Scraper")
    print("=" * 50)
    print(f"\nTarget: {URL}")
    print(f"Output: {OUTPUT_FILE}")
    print()

    all_quotes = []
    current_url = URL
    page_count = 0
    max_pages = 3  # Limit pages for this demo (be respectful!)

    while current_url and page_count < max_pages:
        page_count += 1
        print(f"\n--- Page {page_count} ---")

        # Fetch the page
        html = fetch_page(current_url)
        if not html:
            break

        # Parse the content
        quotes = parse_quotes_page(html)
        print(f"Found {len(quotes)} quotes")

        # Add to our collection
        all_quotes.extend(quotes)

        # Get next page URL
        current_url = get_next_page_url(html, URL)

        # Wait before next request (be polite!)
        if current_url:
            print(f"Waiting {DELAY_SECONDS} seconds...")
            time.sleep(DELAY_SECONDS)

    # Save results
    if all_quotes:
        save_to_csv(all_quotes, OUTPUT_FILE)

        # Print sample
        print("\n--- Sample of scraped data ---")
        for quote in all_quotes[:3]:
            print(f"\n\"{quote['quote'][:50]}...\"")
            print(f"  - {quote['author']}")
            print(f"  Tags: {quote['tags']}")
    else:
        print("\nNo data was scraped.")

    print("\n" + "=" * 50)
    print("Scraping complete!")
    print("=" * 50)


if __name__ == "__main__":
    main()
