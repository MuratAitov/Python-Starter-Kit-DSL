"""
Web Scraper App - Streamlit Interface
An interactive web app for scraping websites.

Run with: streamlit run templates/scraping_templates/web_scraper_app.py
"""

import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
from urllib.parse import urljoin, urlparse

# Page configuration
st.set_page_config(
    page_title="Web Scraper",
    page_icon="🌐",
    layout="wide"
)

st.title("🌐 Web Scraper")
st.write("Extract data from web pages easily!")

# --- Sidebar ---
st.sidebar.header("Settings")
timeout = st.sidebar.slider("Request timeout (seconds)", 5, 30, 10)
user_agent = st.sidebar.selectbox(
    "User Agent",
    [
        "Educational Scraper (Research)",
        "Mozilla/5.0 (compatible; ResearchBot/1.0)",
        "Custom"
    ]
)

if user_agent == "Custom":
    user_agent = st.sidebar.text_input("Custom User Agent")

# --- Main Interface ---
st.header("1. Enter URL")

url = st.text_input(
    "Website URL:",
    placeholder="https://example.com",
    help="Enter the full URL including https://"
)

# Validate URL
def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

if url and not is_valid_url(url):
    st.error("Please enter a valid URL (including https://)")
    url = None

# --- Ethics Warning ---
with st.expander("⚠️ Web Scraping Ethics (Please Read)"):
    st.markdown("""
    Before scraping any website, please consider:

    1. **Check robots.txt** — Visit `website.com/robots.txt` to see what's allowed
    2. **Read Terms of Service** — Some sites prohibit scraping
    3. **Be respectful** — Don't overload servers with requests
    4. **For research only** — This tool is for educational purposes
    5. **Respect privacy** — Don't scrape personal information

    **Recommended practice sites:**
    - `https://quotes.toscrape.com` — Quotes (made for practice)
    - `https://books.toscrape.com` — Books (made for practice)
    - `https://example.com` — Simple test page
    """)

# --- Scrape Button ---
if url:
    if st.button("🔍 Scrape Page", type="primary"):
        with st.spinner("Fetching page..."):
            try:
                headers = {'User-Agent': user_agent}
                response = requests.get(url, headers=headers, timeout=timeout)
                response.raise_for_status()

                st.success(f"Successfully fetched! (Status: {response.status_code})")

                # Parse HTML
                soup = BeautifulSoup(response.text, 'html.parser')

                # Store in session state
                st.session_state['soup'] = soup
                st.session_state['url'] = url
                st.session_state['html'] = response.text

            except requests.exceptions.RequestException as e:
                st.error(f"Error fetching page: {e}")

# --- Results ---
if 'soup' in st.session_state:
    soup = st.session_state['soup']
    base_url = st.session_state['url']

    st.header("2. Extracted Data")

    # Tabs for different data types
    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Page Info", "Links", "Headings", "Images", "Custom"
    ])

    # Tab 1: Page Info
    with tab1:
        st.subheader("Page Information")

        # Title
        title = soup.find('title')
        st.write(f"**Title:** {title.text if title else 'No title found'}")

        # Meta description
        meta_desc = soup.find('meta', attrs={'name': 'description'})
        if meta_desc:
            st.write(f"**Description:** {meta_desc.get('content', 'N/A')}")

        # Statistics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Links", len(soup.find_all('a')))
        with col2:
            st.metric("Images", len(soup.find_all('img')))
        with col3:
            st.metric("Paragraphs", len(soup.find_all('p')))
        with col4:
            st.metric("Headings", len(soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])))

        # Text preview
        st.subheader("Text Content Preview")
        all_text = soup.get_text(separator='\n', strip=True)
        st.text_area("Page text:", all_text[:2000] + "..." if len(all_text) > 2000 else all_text, height=200)

    # Tab 2: Links
    with tab2:
        st.subheader("All Links")

        links_data = []
        for link in soup.find_all('a'):
            href = link.get('href', '')
            text = link.text.strip()

            # Make absolute URL
            if href and not href.startswith(('http', 'mailto:', 'tel:', '#', 'javascript:')):
                href = urljoin(base_url, href)

            if href and text:
                links_data.append({
                    'Text': text[:100],
                    'URL': href
                })

        if links_data:
            df = pd.DataFrame(links_data)
            st.dataframe(df, use_container_width=True)

            # Download
            csv = df.to_csv(index=False)
            st.download_button("Download Links (CSV)", csv, "links.csv", "text/csv")
        else:
            st.info("No links found on this page.")

    # Tab 3: Headings
    with tab3:
        st.subheader("Page Headings")

        headings_data = []
        for level in range(1, 7):
            for heading in soup.find_all(f'h{level}'):
                headings_data.append({
                    'Level': f'H{level}',
                    'Text': heading.text.strip()
                })

        if headings_data:
            df = pd.DataFrame(headings_data)
            st.dataframe(df, use_container_width=True)

            # Download
            csv = df.to_csv(index=False)
            st.download_button("Download Headings (CSV)", csv, "headings.csv", "text/csv")
        else:
            st.info("No headings found on this page.")

    # Tab 4: Images
    with tab4:
        st.subheader("Images")

        images_data = []
        for img in soup.find_all('img'):
            src = img.get('src', '')
            alt = img.get('alt', '')

            # Make absolute URL
            if src and not src.startswith('http'):
                src = urljoin(base_url, src)

            if src:
                images_data.append({
                    'Alt Text': alt,
                    'Source URL': src
                })

        if images_data:
            df = pd.DataFrame(images_data)
            st.dataframe(df, use_container_width=True)

            # Download
            csv = df.to_csv(index=False)
            st.download_button("Download Images (CSV)", csv, "images.csv", "text/csv")
        else:
            st.info("No images found on this page.")

    # Tab 5: Custom Selector
    with tab5:
        st.subheader("Custom CSS Selector")
        st.write("Use CSS selectors to extract specific elements.")

        selector = st.text_input(
            "CSS Selector:",
            placeholder="e.g., div.content, #main, p.intro",
            help="Examples: 'div.class-name', '#id-name', 'p', 'a[href]'"
        )

        if selector:
            try:
                elements = soup.select(selector)
                st.write(f"Found **{len(elements)}** elements")

                if elements:
                    custom_data = []
                    for i, el in enumerate(elements[:100]):  # Limit to 100
                        custom_data.append({
                            'Index': i + 1,
                            'Tag': el.name,
                            'Text': el.text.strip()[:200],
                            'HTML': str(el)[:300]
                        })

                    df = pd.DataFrame(custom_data)
                    st.dataframe(df, use_container_width=True)

                    # Download
                    csv = df.to_csv(index=False)
                    st.download_button("Download Results (CSV)", csv, "custom_scrape.csv", "text/csv")
            except Exception as e:
                st.error(f"Invalid selector: {e}")

        st.markdown("---")
        st.markdown("""
        **CSS Selector Examples:**
        - `p` — All paragraphs
        - `div.classname` — Divs with specific class
        - `#idname` — Element with specific ID
        - `a[href]` — All links with href attribute
        - `ul li` — List items inside unordered lists
        - `.quote .text` — Elements with class 'text' inside class 'quote'
        """)

else:
    st.info("Enter a URL and click 'Scrape Page' to begin.")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit | Digital Scholarship Lab Starter Kit*")
