# 📄 PDF & Document Processing Templates

Extract text from PDFs, process documents, and work with scanned files.

## What You Can Build

- **PDF text extraction** — Get text from PDF files
- **Document converters** — Convert PDFs to text/Word
- **Batch processors** — Process multiple files at once
- **OCR tools** — Extract text from scanned documents
- **PDF mergers/splitters** — Combine or split PDF files

---

## Available Templates

### 1. `simple_pdf_reader.py` — Basic PDF Text Extractor
A simple script to extract text from PDF files.

**Features:**
- Extract text from single or multiple PDFs
- Save extracted text to files
- Handle multi-page documents
- Basic text cleaning

**How to use:**

1. **Put your PDF files** in `data/raw/` folder

2. **Run the script:**
   ```bash
   python templates/pdf_templates/simple_pdf_reader.py
   ```

3. **Find results** in `data/processed/`

---

### 2. `pdf_tool_app.py` — PDF Tool Web App (Streamlit)
An interactive web app for working with PDFs.

**Features:**
- Upload and extract text from PDFs
- Preview extracted content
- Download as text file
- Basic document statistics

**How to use:**

1. **Run the app:**
   ```bash
   streamlit run templates/pdf_templates/pdf_tool_app.py
   ```

2. **Upload a PDF** and extract text

---

## Example Ideas

### Simple Ideas (Beginners)
- **PDF to Text Converter** — Extract text from research papers
- **Page Counter** — Count pages in multiple PDFs
- **Text Search** — Search for terms across PDFs
- **Metadata Extractor** — Get PDF properties (author, date, etc.)

### Medium Ideas
- **Research Paper Processor** — Extract abstracts and references
- **Invoice Reader** — Extract data from PDF invoices
- **Form Data Extractor** — Get data from PDF forms
- **Document Indexer** — Create searchable index of PDFs

### Advanced Ideas
- **OCR Pipeline** — Extract text from scanned documents
- **Table Extractor** — Extract tables from PDFs
- **PDF Comparison** — Compare two PDF documents
- **Automated Archive** — Process and organize PDF collections

---

## Quick Tips

### Extract Text from PDF
```python
import PyPDF2

# Open PDF
with open('document.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)

    # Get number of pages
    num_pages = len(reader.pages)

    # Extract text from all pages
    text = ""
    for page in reader.pages:
        text += page.extract_text()

    print(text)
```

### Get PDF Metadata
```python
import PyPDF2

with open('document.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    metadata = reader.metadata

    print(f"Title: {metadata.title}")
    print(f"Author: {metadata.author}")
    print(f"Pages: {len(reader.pages)}")
```

### Process Multiple PDFs
```python
import PyPDF2
import glob

# Find all PDFs in folder
pdf_files = glob.glob('data/raw/*.pdf')

for pdf_path in pdf_files:
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()

        # Save extracted text
        output_path = pdf_path.replace('.pdf', '.txt')
        with open(output_path, 'w') as out:
            out.write(text)
```

### Merge PDFs
```python
from PyPDF2 import PdfMerger

merger = PdfMerger()

# Add PDFs to merge
merger.append('file1.pdf')
merger.append('file2.pdf')
merger.append('file3.pdf')

# Save merged PDF
merger.write('merged.pdf')
merger.close()
```

### Split PDF
```python
from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader('large_document.pdf')

# Extract pages 1-5 (0-indexed)
writer = PdfWriter()
for i in range(5):
    writer.add_page(reader.pages[i])

with open('first_5_pages.pdf', 'wb') as output:
    writer.write(output)
```

### OCR for Scanned PDFs (requires Tesseract)
```python
import pytesseract
from pdf2image import convert_from_path

# Convert PDF pages to images
images = convert_from_path('scanned_document.pdf')

# OCR each page
text = ""
for image in images:
    text += pytesseract.image_to_string(image)

print(text)
```

---

## Common Issues

### "Module not found: PyPDF2"
```bash
pip install PyPDF2
```

### "Cannot extract text" (scanned PDF)
Scanned PDFs are images, not text. You need OCR:
```bash
pip install pytesseract pdf2image
# Also install Tesseract OCR on your system:
# Mac: brew install tesseract
# Ubuntu: sudo apt install tesseract-ocr
```

### Extracted text is garbled
Some PDFs have non-standard fonts. Try:
```python
# Use pdfplumber instead (often better extraction)
import pdfplumber

with pdfplumber.open('document.pdf') as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        print(text)
```

### Memory issues with large PDFs
Process page by page instead of loading everything:
```python
reader = PyPDF2.PdfReader('large.pdf')
for i, page in enumerate(reader.pages):
    text = page.extract_text()
    # Process and save immediately
    with open(f'page_{i}.txt', 'w') as f:
        f.write(text)
```

---

## Library Options

| Library | Best For | Install |
|---------|----------|---------|
| PyPDF2 | Basic text extraction, merging | `pip install PyPDF2` |
| pdfplumber | Better text/table extraction | `pip install pdfplumber` |
| pytesseract | OCR for scanned docs | `pip install pytesseract` |
| pdf2image | Convert PDF to images | `pip install pdf2image` |
| reportlab | Creating new PDFs | `pip install reportlab` |

---

## Learn More

- [PyPDF2 Documentation](https://pypdf2.readthedocs.io/)
- [pdfplumber Documentation](https://github.com/jsvine/pdfplumber)
- [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
- [pdf2image Documentation](https://github.com/Belval/pdf2image)

---

**Need help?** Ask your instructor or check the main README.md
