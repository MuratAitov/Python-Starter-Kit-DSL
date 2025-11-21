# 🌐 Web Scraping Templates

Collect data from websites and build datasets from online sources.

## What You Can Build

- **Data collectors** — Gather information from websites
- **Web archivers** — Save web pages for research
- **News aggregators** — Collect articles from news sites
- **Price trackers** — Monitor product prices
- **Research datasets** — Build datasets from online sources

---

## Available Templates

### 1. `simple_scraper.py` — Basic Web Scraper
A beginner-friendly script that scrapes a webpage and extracts information.

**Features:**
- Fetch webpage content
- Extract text, links, and images
- Save results to CSV
- Handle errors gracefully

**How to use:**

1. **Run the script:**
   ```bash
   python templates/scraping_templates/simple_scraper.py
   ```

2. **Modify the URL** in the script to scrape different pages

---

### 2. `web_scraper_app.py` — Interactive Web Scraper (Streamlit)
A web app that lets you scrape pages through a user interface.

**Features:**
- Enter any URL
- Preview page content
- Extract links, headings, and text
- Download extracted data

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/scraping_templates/web_scraper_app.py
   ```

2. **Enter a URL** and click "Scrape"

---

## Important: Web Scraping Ethics

Before scraping any website, please consider:

1. **Check robots.txt** — Visit `website.com/robots.txt` to see what's allowed
2. **Read Terms of Service** — Some sites prohibit scraping
3. **Be respectful** — Don't overload servers with too many requests
4. **Add delays** — Wait between requests (1-2 seconds minimum)
5. **Identify yourself** — Use a proper User-Agent header
6. **For research only** — Don't scrape for commercial purposes without permission

---

## Example Ideas

### Simple Ideas (Beginners)
- **Wikipedia Info** — Extract text from Wikipedia articles
- **Quote Collector** — Gather quotes from quote websites
- **Weather Data** — Get weather information
- **Book Lists** — Scrape book titles and authors

### Medium Ideas
- **News Headlines** — Collect headlines from news sites
- **Job Listings** — Gather job postings (with permission)
- **Recipe Collector** — Save recipes from cooking sites
- **Event Calendar** — Build a list of local events

### Advanced Ideas
- **Research Database** — Build academic resource collections
- **Archive Projects** — Preserve web content for research
- **Data Journalism** — Gather data for stories
- **Historical Records** — Collect digitized historical data

---

## Quick Tips

### Basic Request
```python
import requests

url = "https://example.com"
response = requests.get(url)

# Check if successful
if response.status_code == 200:
    html = response.text
    print(html)
```

### Parse HTML with BeautifulSoup
```python
from bs4 import BeautifulSoup
import requests

url = "https://example.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements
title = soup.find('title').text
headings = soup.find_all('h1')
links = soup.find_all('a')
```

### Extract Specific Data
```python
# Get all links
for link in soup.find_all('a'):
    href = link.get('href')
    text = link.text
    print(f"{text}: {href}")

# Get all paragraphs
paragraphs = [p.text for p in soup.find_all('p')]

# Find by class
items = soup.find_all('div', class_='item')

# Find by ID
header = soup.find(id='header')
```

### Save to CSV
```python
import pandas as pd

data = [
    {'title': 'Page 1', 'url': 'http://...'},
    {'title': 'Page 2', 'url': 'http://...'},
]

df = pd.DataFrame(data)
df.to_csv('data/processed/scraped_data.csv', index=False)
```

### Be a Good Citizen
```python
import time
import requests

# Set a proper User-Agent
headers = {
    'User-Agent': 'Research Bot (contact@university.edu)'
}

urls = ['url1', 'url2', 'url3']

for url in urls:
    response = requests.get(url, headers=headers)
    # Process response...

    # Wait between requests
    time.sleep(2)  # Wait 2 seconds
```

---

## Common Issues

### "Connection refused" or timeout
```python
# Add timeout and error handling
try:
    response = requests.get(url, timeout=10)
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
```

### Getting blocked
```python
# Use headers to look like a browser
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
}
response = requests.get(url, headers=headers)
```

### "Module not found: bs4"
```bash
pip install beautifulsoup4
pip install lxml  # Optional but faster parser
```

### Encoding issues
```python
# Specify encoding
response.encoding = 'utf-8'
text = response.text
```

---

## Learn More

- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Documentation](https://requests.readthedocs.io/)
- [Web Scraping Ethics](https://towardsdatascience.com/ethics-in-web-scraping-b96b18136f01)
- [robots.txt Guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)

---

**Need help?** Ask your instructor or check the main README.md
