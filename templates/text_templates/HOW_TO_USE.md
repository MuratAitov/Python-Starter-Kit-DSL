# 📝 Text Analysis Templates

Analyze text documents, find patterns, and extract insights from written content.

## What You Can Build

- **Word frequency analysis** — Find most common words in texts
- **Sentiment analysis** — Determine if text is positive/negative
- **Named entity extraction** — Find people, places, dates
- **Word clouds** — Visual representation of text
- **Text comparison** — Compare multiple documents

---

## Available Templates

### 1. `simple_text_analyzer.py` — Basic Text Analysis (Streamlit App)
A web app that analyzes text you paste or upload.

**Features:**
- Word and character count
- Most frequent words
- Word cloud visualization
- Basic sentiment analysis
- Export results

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/text_templates/simple_text_analyzer.py
   ```

2. **Open in browser:**
   - Automatically opens at http://localhost:8501

3. **Try it out:**
   - Paste text or upload a .txt file
   - View word frequencies
   - See the word cloud
   - Check sentiment score

---

### 2. `text_analysis.ipynb` — Complete Text Analysis Notebook
A Jupyter notebook for deeper text analysis.

**Features:**
- Load text files
- Clean and preprocess text
- N-gram analysis (word pairs, triplets)
- Named entity recognition
- Visualization and charts

**How to use:**

1. **Open Jupyter:**
   ```bash
   jupyter notebook templates/text_templates/text_analysis.ipynb
   ```

2. **Run the cells** step by step

---

## Example Ideas

### Simple Ideas (Beginners)
- **Book Word Counter** — Analyze your favorite book
- **Tweet Analyzer** — Analyze social media posts
- **Essay Grader Helper** — Count words, find repetition
- **Lyrics Analyzer** — Find themes in song lyrics

### Medium Ideas
- **Research Paper Analyzer** — Find key terms in academic papers
- **Historical Document Analysis** — Analyze old letters/documents
- **Survey Response Analyzer** — Analyze open-ended responses
- **News Article Comparison** — Compare coverage across sources

### Advanced Ideas
- **Corpus Analysis** — Analyze entire collections of texts
- **Author Attribution** — Identify writing styles
- **Topic Modeling** — Find themes across documents
- **Sentiment Over Time** — Track mood changes

---

## Quick Tips

### Load Text Files
```python
# Read a text file
with open('data/raw/document.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Read multiple files
import glob
texts = []
for filepath in glob.glob('data/raw/*.txt'):
    with open(filepath, 'r') as f:
        texts.append(f.read())
```

### Clean Text
```python
import re

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = re.sub(r'[^\w\s]', '', text)

# Remove numbers
text = re.sub(r'\d+', '', text)

# Remove extra whitespace
text = ' '.join(text.split())
```

### Word Frequency
```python
from collections import Counter

words = text.split()
word_counts = Counter(words)

# Most common words
print(word_counts.most_common(10))
```

### Create Word Cloud
```python
from wordcloud import WordCloud
import matplotlib.pyplot as plt

wordcloud = WordCloud(width=800, height=400).generate(text)

plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()
```

### Simple Sentiment Analysis
```python
from textblob import TextBlob

blob = TextBlob(text)
sentiment = blob.sentiment

print(f"Polarity: {sentiment.polarity}")  # -1 (negative) to 1 (positive)
print(f"Subjectivity: {sentiment.subjectivity}")  # 0 (objective) to 1 (subjective)
```

---

## Common Issues

### "Module not found: wordcloud"
```bash
pip install wordcloud
```

### "Module not found: textblob"
```bash
pip install textblob
python -m textblob.download_corpora
```

### Word cloud shows common words like "the", "and"
```python
from wordcloud import WordCloud, STOPWORDS

# Add stopwords to filter out common words
stopwords = set(STOPWORDS)
wordcloud = WordCloud(stopwords=stopwords).generate(text)
```

### Text encoding errors
```python
# Try different encodings
with open('file.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Or try latin-1
with open('file.txt', 'r', encoding='latin-1') as f:
    text = f.read()
```

---

## Learn More

- [NLTK Documentation](https://www.nltk.org/) — Natural Language Toolkit
- [TextBlob Documentation](https://textblob.readthedocs.io/)
- [WordCloud Documentation](https://amueller.github.io/word_cloud/)
- [spaCy Documentation](https://spacy.io/) — Industrial NLP

---

**Need help?** Ask your instructor or check the main README.md
