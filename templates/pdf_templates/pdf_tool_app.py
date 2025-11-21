"""
PDF Tool App - Streamlit Interface
An interactive web app for working with PDF files.

Run with: streamlit run templates/pdf_templates/pdf_tool_app.py
"""

import streamlit as st
import io

# Try to import PDF libraries
try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False

# Page configuration
st.set_page_config(
    page_title="PDF Tool",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF Tool")
st.write("Extract text and information from PDF files!")

# Check for required library
if not PYPDF2_AVAILABLE:
    st.error("PyPDF2 is required. Install it with: `pip install PyPDF2`")
    st.stop()

# --- File Upload ---
st.header("1. Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF file",
    type=['pdf'],
    help="Upload a PDF file to extract text and information"
)

if uploaded_file:
    # Read PDF
    try:
        pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))

        # Store in session state
        st.session_state['pdf_reader'] = pdf_reader
        st.session_state['filename'] = uploaded_file.name

        st.success(f"Successfully loaded: {uploaded_file.name}")

    except Exception as e:
        st.error(f"Error reading PDF: {e}")
        st.stop()

# --- PDF Analysis ---
if 'pdf_reader' in st.session_state:
    reader = st.session_state['pdf_reader']
    filename = st.session_state['filename']

    st.header("2. PDF Information")

    # Basic stats
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Pages", len(reader.pages))

    with col2:
        # Try to get title
        title = "N/A"
        if reader.metadata and reader.metadata.title:
            title = reader.metadata.title[:30] + "..." if len(str(reader.metadata.title)) > 30 else reader.metadata.title
        st.metric("Title", title)

    with col3:
        author = "N/A"
        if reader.metadata and reader.metadata.author:
            author = reader.metadata.author
        st.metric("Author", author)

    # Metadata expander
    with st.expander("View All Metadata"):
        if reader.metadata:
            metadata_dict = {
                "Title": reader.metadata.title,
                "Author": reader.metadata.author,
                "Subject": reader.metadata.subject,
                "Creator": reader.metadata.creator,
                "Producer": reader.metadata.producer,
            }
            for key, value in metadata_dict.items():
                if value:
                    st.write(f"**{key}:** {value}")
        else:
            st.info("No metadata available")

    # --- Text Extraction ---
    st.header("3. Extract Text")

    # Options
    col1, col2 = st.columns(2)

    with col1:
        extraction_mode = st.radio(
            "Extraction mode:",
            ["All pages", "Specific pages"]
        )

    with col2:
        if extraction_mode == "Specific pages":
            page_range = st.text_input(
                "Page numbers (e.g., 1,3,5 or 1-5):",
                placeholder="1-3"
            )

    # Extract button
    if st.button("Extract Text", type="primary"):
        with st.spinner("Extracting text..."):
            extracted_text = ""
            pages_to_extract = []

            if extraction_mode == "All pages":
                pages_to_extract = list(range(len(reader.pages)))
            else:
                # Parse page range
                try:
                    if '-' in page_range:
                        start, end = page_range.split('-')
                        pages_to_extract = list(range(int(start)-1, int(end)))
                    elif ',' in page_range:
                        pages_to_extract = [int(p.strip())-1 for p in page_range.split(',')]
                    else:
                        pages_to_extract = [int(page_range)-1]
                except:
                    st.error("Invalid page range. Use format like '1-5' or '1,3,5'")
                    pages_to_extract = []

            # Extract text
            for i in pages_to_extract:
                if 0 <= i < len(reader.pages):
                    page_text = reader.pages[i].extract_text()
                    if page_text:
                        extracted_text += f"\n\n--- Page {i+1} ---\n\n"
                        extracted_text += page_text

            if extracted_text:
                st.session_state['extracted_text'] = extracted_text
                st.success(f"Extracted text from {len(pages_to_extract)} page(s)")
            else:
                st.warning("No text could be extracted. The PDF may be scanned/image-based.")

    # --- Display Results ---
    if 'extracted_text' in st.session_state:
        text = st.session_state['extracted_text']

        st.header("4. Results")

        # Stats
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Characters", f"{len(text):,}")
        with col2:
            st.metric("Words", f"{len(text.split()):,}")
        with col3:
            st.metric("Lines", f"{text.count(chr(10)):,}")

        # Text preview
        st.subheader("Extracted Text")
        st.text_area(
            "Preview:",
            text,
            height=400
        )

        # Download options
        st.subheader("Download")

        col1, col2 = st.columns(2)

        with col1:
            st.download_button(
                "Download as TXT",
                text,
                file_name=filename.replace('.pdf', '.txt'),
                mime="text/plain"
            )

        with col2:
            # Clean text version (remove page markers)
            clean_text = text
            import re
            clean_text = re.sub(r'\n*--- Page \d+ ---\n*', '\n\n', clean_text)

            st.download_button(
                "Download Clean Text",
                clean_text.strip(),
                file_name=filename.replace('.pdf', '_clean.txt'),
                mime="text/plain"
            )

else:
    st.info("Upload a PDF file to begin.")

# --- Tips ---
st.markdown("---")
with st.expander("Tips & Troubleshooting"):
    st.markdown("""
    **No text extracted?**
    - The PDF might be scanned/image-based
    - You'll need OCR (Optical Character Recognition) for scanned PDFs
    - Install: `pip install pytesseract pdf2image`

    **Garbled text?**
    - Some PDFs use non-standard fonts
    - Try the `pdfplumber` library instead

    **Large PDF?**
    - Extract specific pages instead of all pages
    - Process in batches
    """)

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit | Digital Scholarship Lab Starter Kit*")
