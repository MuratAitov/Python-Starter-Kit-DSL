# 🖼️ Image Analysis Templates

Process images, extract information, and analyze visual content.

## What You Can Build

- **Image description** — AI-powered image analysis
- **Text from images (OCR)** — Extract text from photos
- **Image metadata** — Read EXIF data from photos
- **Batch processing** — Process multiple images
- **Image comparison** — Find differences or similarities

---

## Available Templates

### 1. `simple_image_analyzer.py` — Image Analyzer (Streamlit App)
A web app that analyzes images using AI.

**Features:**
- Upload and view images
- AI-powered image description (using GPT-4 Vision)
- Extract text from images (OCR)
- View image metadata
- Download analysis results

**How to use:**

1. **Set up your OpenAI API key** in `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   ```

2. **Run the app:**
   ```bash
   streamlit run templates/image_templates/simple_image_analyzer.py
   ```

3. **Upload an image** and analyze it

---

### 2. `ocr_tool.py` — OCR Text Extractor
Extract text from images using Tesseract OCR (free, offline).

**Features:**
- Works offline (no API needed)
- Batch processing
- Multiple language support
- Save extracted text

**How to use:**

1. **Install Tesseract:**
   ```bash
   # Mac
   brew install tesseract

   # Ubuntu
   sudo apt install tesseract-ocr

   # Windows: Download from GitHub
   ```

2. **Run the script:**
   ```bash
   python templates/image_templates/ocr_tool.py
   ```

---

## Example Ideas

### Simple Ideas (Beginners)
- **Photo Organizer** — Read metadata to sort photos by date
- **Document Scanner** — Extract text from photographed documents
- **Image Describer** — Generate alt-text for images
- **Meme Text Extractor** — Get text from image memes

### Medium Ideas
- **Receipt Scanner** — Extract data from receipts
- **Business Card Reader** — Digitize business cards
- **Historical Document OCR** — Transcribe old documents
- **Artwork Analyzer** — Describe paintings and art

### Advanced Ideas
- **Visual Archive** — Auto-catalog image collections
- **Accessibility Tool** — Describe images for visually impaired
- **Research Image Analysis** — Analyze images in datasets
- **Multi-modal Search** — Search images by description

---

## Quick Tips

### AI Image Analysis (GPT-4 Vision)
```python
from openai import OpenAI
import base64

client = OpenAI()

# Read and encode image
with open("image.jpg", "rb") as f:
    image_data = base64.b64encode(f.read()).decode('utf-8')

# Analyze image
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe this image in detail."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{image_data}"
                    }
                }
            ]
        }
    ],
    max_tokens=500
)

print(response.choices[0].message.content)
```

### OCR with Tesseract (Free)
```python
import pytesseract
from PIL import Image

# Simple OCR
image = Image.open('document.png')
text = pytesseract.image_to_string(image)
print(text)

# Specify language
text = pytesseract.image_to_string(image, lang='eng+fra')  # English + French
```

### Read Image Metadata (EXIF)
```python
from PIL import Image
from PIL.ExifTags import TAGS

image = Image.open('photo.jpg')
exif = image._getexif()

if exif:
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        print(f"{tag}: {value}")
```

### Basic Image Processing
```python
from PIL import Image

# Open image
img = Image.open('photo.jpg')

# Resize
img_resized = img.resize((800, 600))

# Convert to grayscale
img_gray = img.convert('L')

# Rotate
img_rotated = img.rotate(90)

# Crop
img_cropped = img.crop((100, 100, 400, 400))

# Save
img_resized.save('resized.jpg')
```

### Batch Process Images
```python
import glob
from PIL import Image

image_files = glob.glob('data/raw/*.jpg')

for img_path in image_files:
    img = Image.open(img_path)

    # Process...
    text = pytesseract.image_to_string(img)

    # Save result
    output_path = img_path.replace('.jpg', '.txt')
    with open(output_path, 'w') as f:
        f.write(text)
```

### Improve OCR Accuracy
```python
from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('document.png')

# Convert to grayscale
img = img.convert('L')

# Increase contrast
enhancer = ImageEnhance.Contrast(img)
img = enhancer.enhance(2)

# Sharpen
img = img.filter(ImageFilter.SHARPEN)

# Now OCR
text = pytesseract.image_to_string(img)
```

---

## Common Issues

### "tesseract is not installed"
```bash
# Mac
brew install tesseract

# Ubuntu/Debian
sudo apt install tesseract-ocr

# Windows
# Download installer from:
# https://github.com/UB-Mannheim/tesseract/wiki
```

### "pytesseract not found"
```bash
pip install pytesseract Pillow
```

### OCR gives poor results
- Ensure image is high resolution
- Try preprocessing (grayscale, contrast)
- Check language setting matches document
- Use PSM modes for different layouts:
```python
# Single column of text
text = pytesseract.image_to_string(img, config='--psm 6')

# Single line
text = pytesseract.image_to_string(img, config='--psm 7')
```

### "OpenAI API error"
- Check your API key is set correctly
- GPT-4 Vision requires GPT-4 access
- Use `gpt-4o` or `gpt-4-turbo` model

### Image too large for API
```python
from PIL import Image

# Resize before sending to API
img = Image.open('large_image.jpg')
img.thumbnail((1024, 1024))  # Max 1024x1024
img.save('resized.jpg')
```

---

## Supported Formats

| Format | Extension | Notes |
|--------|-----------|-------|
| JPEG | .jpg, .jpeg | Most common |
| PNG | .png | Supports transparency |
| GIF | .gif | Animated supported |
| BMP | .bmp | Uncompressed |
| TIFF | .tiff, .tif | High quality |
| WebP | .webp | Modern format |

---

## Learn More

- [OpenAI Vision Guide](https://platform.openai.com/docs/guides/vision)
- [Tesseract Documentation](https://tesseract-ocr.github.io/)
- [Pillow Documentation](https://pillow.readthedocs.io/)
- [OCR Best Practices](https://tesseract-ocr.github.io/tessdoc/ImproveQuality.html)

---

**Need help?** Ask your instructor or check the main README.md
