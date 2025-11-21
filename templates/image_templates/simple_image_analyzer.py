"""
Simple Image Analyzer - Streamlit Web App
Analyze images using AI and extract text with OCR.

Run with: streamlit run templates/image_templates/simple_image_analyzer.py
"""

import streamlit as st
import os
import base64
import io

# Try to import required libraries
try:
    from PIL import Image
    from PIL.ExifTags import TAGS
    PIL_AVAILABLE = True
except ImportError:
    PIL_AVAILABLE = False

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

try:
    import pytesseract
    TESSERACT_AVAILABLE = True
except ImportError:
    TESSERACT_AVAILABLE = False

# Try to load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Page configuration
st.set_page_config(
    page_title="Image Analyzer",
    page_icon="🖼️",
    layout="wide"
)

st.title("🖼️ Image Analyzer")
st.write("Analyze images with AI and extract text!")

# Check for PIL
if not PIL_AVAILABLE:
    st.error("Pillow library not installed. Run: `pip install Pillow`")
    st.stop()

# --- Sidebar ---
st.sidebar.header("Settings")

# API Key for AI analysis
api_key = st.sidebar.text_input(
    "OpenAI API Key (for AI analysis)",
    type="password",
    value=os.getenv('OPENAI_API_KEY', ''),
    help="Optional - needed for AI image description"
)

# --- Main Interface ---
st.header("1. Upload Image")

uploaded_file = st.file_uploader(
    "Choose an image",
    type=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'webp'],
    help="Supported formats: JPG, PNG, GIF, BMP, WebP"
)

if uploaded_file:
    # Load image
    image = Image.open(uploaded_file)

    # Display image
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Uploaded Image")
        st.image(image, use_container_width=True)

    with col2:
        st.subheader("Image Info")
        st.write(f"**Filename:** {uploaded_file.name}")
        st.write(f"**Format:** {image.format or 'Unknown'}")
        st.write(f"**Size:** {image.size[0]} x {image.size[1]} pixels")
        st.write(f"**Mode:** {image.mode}")
        st.write(f"**File size:** {uploaded_file.size / 1024:.1f} KB")

    # Store image for analysis
    st.session_state['image'] = image
    st.session_state['image_bytes'] = uploaded_file.getvalue()

    # --- Analysis Tabs ---
    st.header("2. Analyze")

    tab1, tab2, tab3, tab4 = st.tabs(["AI Description", "Text Extraction (OCR)", "Metadata", "Export"])

    # Tab 1: AI Description
    with tab1:
        st.subheader("AI Image Description")

        if not OPENAI_AVAILABLE:
            st.warning("OpenAI library not installed. Run: `pip install openai`")
        elif not api_key:
            st.warning("Enter your OpenAI API key in the sidebar for AI analysis.")
        else:
            prompt = st.text_input(
                "What would you like to know about this image?",
                value="Describe this image in detail.",
                placeholder="Describe this image..."
            )

            if st.button("Analyze with AI", type="primary"):
                with st.spinner("Analyzing image..."):
                    try:
                        client = OpenAI(api_key=api_key)

                        # Encode image
                        image_data = base64.b64encode(st.session_state['image_bytes']).decode('utf-8')

                        # Determine image type
                        img_type = "jpeg"
                        if uploaded_file.name.lower().endswith('.png'):
                            img_type = "png"
                        elif uploaded_file.name.lower().endswith('.gif'):
                            img_type = "gif"
                        elif uploaded_file.name.lower().endswith('.webp'):
                            img_type = "webp"

                        # Call API
                        response = client.chat.completions.create(
                            model="gpt-4o",
                            messages=[
                                {
                                    "role": "user",
                                    "content": [
                                        {"type": "text", "text": prompt},
                                        {
                                            "type": "image_url",
                                            "image_url": {
                                                "url": f"data:image/{img_type};base64,{image_data}"
                                            }
                                        }
                                    ]
                                }
                            ],
                            max_tokens=1000
                        )

                        description = response.choices[0].message.content
                        st.session_state['ai_description'] = description

                        st.success("Analysis complete!")
                        st.markdown("**AI Description:**")
                        st.write(description)

                    except Exception as e:
                        st.error(f"Error: {e}")
                        if "model" in str(e).lower():
                            st.info("Try using a different model or check your API access.")

            # Show previous result
            if 'ai_description' in st.session_state and not st.button:
                st.write(st.session_state['ai_description'])

    # Tab 2: OCR
    with tab2:
        st.subheader("Text Extraction (OCR)")

        if not TESSERACT_AVAILABLE:
            st.warning("pytesseract not installed. Run: `pip install pytesseract`")
            st.info("You also need Tesseract OCR installed on your system.")
            st.code("""
# Mac
brew install tesseract

# Ubuntu
sudo apt install tesseract-ocr

# Windows: Download from GitHub
# https://github.com/UB-Mannheim/tesseract/wiki
            """)
        else:
            # OCR options
            col1, col2 = st.columns(2)
            with col1:
                ocr_lang = st.selectbox(
                    "Language",
                    ["eng", "fra", "deu", "spa", "ita", "por", "chi_sim", "jpn", "kor"],
                    help="Select the language of the text in the image"
                )
            with col2:
                preprocess = st.checkbox("Preprocess image", value=True,
                    help="Convert to grayscale and increase contrast")

            if st.button("Extract Text"):
                with st.spinner("Extracting text..."):
                    try:
                        # Preprocess if selected
                        img_for_ocr = st.session_state['image']

                        if preprocess:
                            # Convert to grayscale
                            img_for_ocr = img_for_ocr.convert('L')

                        # Run OCR
                        text = pytesseract.image_to_string(img_for_ocr, lang=ocr_lang)

                        if text.strip():
                            st.session_state['ocr_text'] = text
                            st.success("Text extracted!")
                            st.text_area("Extracted Text:", text, height=300)
                        else:
                            st.warning("No text found in image.")

                    except Exception as e:
                        st.error(f"OCR Error: {e}")
                        st.info("Make sure Tesseract is installed on your system.")

    # Tab 3: Metadata
    with tab3:
        st.subheader("Image Metadata (EXIF)")

        try:
            exif = st.session_state['image']._getexif()

            if exif:
                metadata = {}
                for tag_id, value in exif.items():
                    tag = TAGS.get(tag_id, tag_id)
                    # Skip binary data
                    if isinstance(value, bytes):
                        continue
                    metadata[tag] = str(value)[:100]  # Truncate long values

                if metadata:
                    st.write(f"Found {len(metadata)} metadata fields:")

                    # Display as table
                    import pandas as pd
                    df = pd.DataFrame(list(metadata.items()), columns=['Field', 'Value'])
                    st.dataframe(df, use_container_width=True)
                else:
                    st.info("No readable metadata found.")
            else:
                st.info("No EXIF metadata found in this image.")

        except Exception as e:
            st.info("Could not read metadata from this image.")

    # Tab 4: Export
    with tab4:
        st.subheader("Export Results")

        # Compile results
        results = f"Image Analysis Results\n"
        results += f"{'=' * 40}\n\n"
        results += f"Filename: {uploaded_file.name}\n"
        results += f"Size: {image.size[0]} x {image.size[1]} pixels\n\n"

        if 'ai_description' in st.session_state:
            results += f"AI Description:\n{st.session_state['ai_description']}\n\n"

        if 'ocr_text' in st.session_state:
            results += f"Extracted Text (OCR):\n{st.session_state['ocr_text']}\n\n"

        st.text_area("Results Preview:", results, height=200)

        st.download_button(
            "Download Results (TXT)",
            results,
            file_name=f"{uploaded_file.name.rsplit('.', 1)[0]}_analysis.txt",
            mime="text/plain"
        )

else:
    st.info("Upload an image to begin analysis.")

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit | Digital Scholarship Lab Starter Kit*")
