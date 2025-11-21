"""
Simple Text Analyzer - Streamlit Web App
Analyze text for word frequency, sentiment, and create word clouds.

Run with: streamlit run templates/text_templates/simple_text_analyzer.py
"""

import streamlit as st
import pandas as pd
from collections import Counter
import re

# Optional imports (graceful fallback if not installed)
try:
    from wordcloud import WordCloud, STOPWORDS
    WORDCLOUD_AVAILABLE = True
except ImportError:
    WORDCLOUD_AVAILABLE = False

try:
    from textblob import TextBlob
    TEXTBLOB_AVAILABLE = True
except ImportError:
    TEXTBLOB_AVAILABLE = False

import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(
    page_title="Text Analyzer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Text Analyzer")
st.write("Analyze your text for word frequency, sentiment, and more!")

# --- Sidebar ---
st.sidebar.header("Settings")
min_word_length = st.sidebar.slider("Minimum word length", 1, 10, 3)
top_n_words = st.sidebar.slider("Top N words to show", 5, 50, 20)
remove_stopwords = st.sidebar.checkbox("Remove common words (the, and, is...)", value=True)

# Common English stopwords
ENGLISH_STOPWORDS = {
    'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
    'of', 'with', 'by', 'from', 'as', 'is', 'was', 'are', 'were', 'been',
    'be', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would',
    'could', 'should', 'may', 'might', 'must', 'shall', 'can', 'need',
    'it', 'its', 'this', 'that', 'these', 'those', 'i', 'you', 'he',
    'she', 'we', 'they', 'what', 'which', 'who', 'whom', 'when', 'where',
    'why', 'how', 'all', 'each', 'every', 'both', 'few', 'more', 'most',
    'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same',
    'so', 'than', 'too', 'very', 'just', 'also', 'now', 'here', 'there'
}

# --- Input Methods ---
st.header("1. Input Your Text")

input_method = st.radio("Choose input method:", ["Paste text", "Upload file"])

text = ""

if input_method == "Paste text":
    text = st.text_area(
        "Paste your text here:",
        height=200,
        placeholder="Enter or paste your text here..."
    )
else:
    uploaded_file = st.file_uploader("Upload a text file", type=["txt"])
    if uploaded_file:
        text = uploaded_file.read().decode('utf-8')
        st.text_area("File contents:", text, height=200)

# --- Analysis ---
if text:
    st.header("2. Analysis Results")

    # Clean text
    clean_text = text.lower()
    clean_text = re.sub(r'[^\w\s]', '', clean_text)  # Remove punctuation
    clean_text = re.sub(r'\d+', '', clean_text)  # Remove numbers

    # Get words
    words = clean_text.split()

    # Filter words
    if remove_stopwords:
        words = [w for w in words if w not in ENGLISH_STOPWORDS]
    words = [w for w in words if len(w) >= min_word_length]

    # Word frequency
    word_counts = Counter(words)

    # --- Stats Row ---
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Characters", f"{len(text):,}")
    with col2:
        st.metric("Total Words", f"{len(text.split()):,}")
    with col3:
        st.metric("Unique Words", f"{len(set(words)):,}")
    with col4:
        st.metric("Sentences", f"{text.count('.') + text.count('!') + text.count('?'):,}")

    # --- Tabs for different analyses ---
    tab1, tab2, tab3, tab4 = st.tabs(["Word Frequency", "Word Cloud", "Sentiment", "Export"])

    # Tab 1: Word Frequency
    with tab1:
        st.subheader("Most Frequent Words")

        top_words = word_counts.most_common(top_n_words)

        if top_words:
            # Create DataFrame
            df = pd.DataFrame(top_words, columns=['Word', 'Count'])

            col1, col2 = st.columns([1, 2])

            with col1:
                st.dataframe(df, use_container_width=True)

            with col2:
                # Bar chart
                fig, ax = plt.subplots(figsize=(10, 6))
                ax.barh([w[0] for w in reversed(top_words[:15])],
                       [w[1] for w in reversed(top_words[:15])],
                       color='steelblue')
                ax.set_xlabel('Frequency')
                ax.set_title(f'Top {min(15, len(top_words))} Words')
                plt.tight_layout()
                st.pyplot(fig)
        else:
            st.warning("No words found after filtering. Try adjusting the settings.")

    # Tab 2: Word Cloud
    with tab2:
        st.subheader("Word Cloud Visualization")

        if WORDCLOUD_AVAILABLE:
            if words:
                # Create word cloud
                stopwords = STOPWORDS if remove_stopwords else set()
                wordcloud = WordCloud(
                    width=800,
                    height=400,
                    background_color='white',
                    stopwords=stopwords,
                    min_word_length=min_word_length,
                    colormap='viridis'
                ).generate(' '.join(words))

                fig, ax = plt.subplots(figsize=(12, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis('off')
                st.pyplot(fig)
            else:
                st.warning("No words available for word cloud.")
        else:
            st.warning("WordCloud not installed. Run: `pip install wordcloud`")

    # Tab 3: Sentiment
    with tab3:
        st.subheader("Sentiment Analysis")

        if TEXTBLOB_AVAILABLE:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity

            col1, col2 = st.columns(2)

            with col1:
                st.metric("Polarity", f"{polarity:.2f}")
                if polarity > 0.1:
                    st.success("The text appears to be **positive**")
                elif polarity < -0.1:
                    st.error("The text appears to be **negative**")
                else:
                    st.info("The text appears to be **neutral**")

                st.caption("Polarity ranges from -1 (negative) to +1 (positive)")

            with col2:
                st.metric("Subjectivity", f"{subjectivity:.2f}")
                if subjectivity > 0.5:
                    st.info("The text is more **subjective** (opinion-based)")
                else:
                    st.info("The text is more **objective** (fact-based)")

                st.caption("Subjectivity ranges from 0 (objective) to 1 (subjective)")
        else:
            st.warning("TextBlob not installed. Run: `pip install textblob`")
            st.info("After installing, run: `python -m textblob.download_corpora`")

    # Tab 4: Export
    with tab4:
        st.subheader("Export Results")

        # Create results DataFrame
        results_df = pd.DataFrame(word_counts.most_common(), columns=['Word', 'Count'])

        # CSV download
        csv = results_df.to_csv(index=False)
        st.download_button(
            "Download Word Frequencies (CSV)",
            csv,
            "word_frequencies.csv",
            "text/csv"
        )

        # Summary text
        summary = f"""Text Analysis Summary
====================
Total Characters: {len(text)}
Total Words: {len(text.split())}
Unique Words: {len(set(words))}
Sentences: {text.count('.') + text.count('!') + text.count('?')}

Top 10 Words:
"""
        for word, count in word_counts.most_common(10):
            summary += f"  {word}: {count}\n"

        st.download_button(
            "Download Summary (TXT)",
            summary,
            "analysis_summary.txt",
            "text/plain"
        )

else:
    st.info("Enter or upload text to begin analysis.")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit | Digital Scholarship Lab Starter Kit*")
