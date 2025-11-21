"""
Simple PDF Reader
Extract text from PDF files.

Run with: python templates/pdf_templates/simple_pdf_reader.py
"""

import os
import glob

# Try to import PyPDF2
try:
    import PyPDF2
    PYPDF2_AVAILABLE = True
except ImportError:
    PYPDF2_AVAILABLE = False
    print("PyPDF2 not installed. Run: pip install PyPDF2")

# ============================================
# CONFIGURATION - Change these values!
# ============================================

# Folder with PDF files
INPUT_FOLDER = "data/raw"

# Where to save extracted text
OUTPUT_FOLDER = "data/processed"

# Process all PDFs or just one?
SINGLE_FILE = None  # Set to "filename.pdf" to process just one file

# ============================================
# MAIN CODE
# ============================================

def extract_text_from_pdf(pdf_path):
    """
    Extract all text from a PDF file.

    Args:
        pdf_path: Path to the PDF file

    Returns:
        Extracted text as a string
    """
    if not PYPDF2_AVAILABLE:
        return None

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)

            # Get metadata
            metadata = reader.metadata
            num_pages = len(reader.pages)

            print(f"  Pages: {num_pages}")
            if metadata:
                if metadata.title:
                    print(f"  Title: {metadata.title}")
                if metadata.author:
                    print(f"  Author: {metadata.author}")

            # Extract text from all pages
            text = ""
            for i, page in enumerate(reader.pages):
                page_text = page.extract_text()
                if page_text:
                    text += f"\n--- Page {i + 1} ---\n"
                    text += page_text

            return text

    except Exception as e:
        print(f"  Error: {e}")
        return None


def get_pdf_info(pdf_path):
    """
    Get basic info about a PDF file.
    """
    if not PYPDF2_AVAILABLE:
        return None

    try:
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            return {
                'pages': len(reader.pages),
                'title': reader.metadata.title if reader.metadata else None,
                'author': reader.metadata.author if reader.metadata else None
            }
    except Exception as e:
        return {'error': str(e)}


def save_text(text, output_path):
    """
    Save extracted text to a file.
    """
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(text)

    print(f"  Saved to: {output_path}")


def process_single_pdf(pdf_path):
    """
    Process a single PDF file.
    """
    filename = os.path.basename(pdf_path)
    print(f"\nProcessing: {filename}")

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    if text:
        # Save to output folder
        output_filename = filename.replace('.pdf', '.txt').replace('.PDF', '.txt')
        output_path = os.path.join(OUTPUT_FOLDER, output_filename)
        save_text(text, output_path)

        # Show preview
        print(f"  Characters extracted: {len(text)}")
        print(f"  Preview: {text[:200]}...")
        return True
    else:
        print("  No text could be extracted (may be scanned/image PDF)")
        return False


def process_all_pdfs():
    """
    Process all PDF files in the input folder.
    """
    # Find all PDFs
    pdf_pattern = os.path.join(INPUT_FOLDER, "*.pdf")
    pdf_files = glob.glob(pdf_pattern)

    # Also check for .PDF extension
    pdf_pattern_upper = os.path.join(INPUT_FOLDER, "*.PDF")
    pdf_files.extend(glob.glob(pdf_pattern_upper))

    if not pdf_files:
        print(f"\nNo PDF files found in {INPUT_FOLDER}/")
        print("Please add some PDF files and try again.")
        return

    print(f"\nFound {len(pdf_files)} PDF file(s)")

    successful = 0
    failed = 0

    for pdf_path in pdf_files:
        if process_single_pdf(pdf_path):
            successful += 1
        else:
            failed += 1

    # Summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    print(f"Successfully processed: {successful}")
    print(f"Failed/skipped: {failed}")
    print(f"Output folder: {OUTPUT_FOLDER}/")


def main():
    """
    Main function.
    """
    print("=" * 50)
    print("PDF Text Extractor")
    print("=" * 50)

    if not PYPDF2_AVAILABLE:
        print("\nError: PyPDF2 is required.")
        print("Install it with: pip install PyPDF2")
        return

    # Create output folder
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    if SINGLE_FILE:
        # Process single file
        pdf_path = os.path.join(INPUT_FOLDER, SINGLE_FILE)
        if os.path.exists(pdf_path):
            process_single_pdf(pdf_path)
        else:
            print(f"\nFile not found: {pdf_path}")
    else:
        # Process all PDFs
        process_all_pdfs()

    print("\nDone!")


if __name__ == "__main__":
    main()
