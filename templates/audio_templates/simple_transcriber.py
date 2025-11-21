"""
Simple Audio Transcriber - Streamlit Web App
Transcribe audio files using OpenAI's Whisper API.

Run with: streamlit run templates/audio_templates/simple_transcriber.py
"""

import streamlit as st
import os
import tempfile

# Try to import OpenAI
try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False

# Try to load environment variables
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Page configuration
st.set_page_config(
    page_title="Audio Transcriber",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Audio Transcriber")
st.write("Convert speech to text using AI!")

# Check for OpenAI library
if not OPENAI_AVAILABLE:
    st.error("OpenAI library not installed. Run: `pip install openai`")
    st.stop()

# --- Sidebar: API Key ---
st.sidebar.header("Settings")

# API Key input
api_key = st.sidebar.text_input(
    "OpenAI API Key",
    type="password",
    value=os.getenv('OPENAI_API_KEY', ''),
    help="Get your key at https://platform.openai.com/api-keys"
)

if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to continue.")
    st.info("""
    **How to get an API key:**
    1. Go to https://platform.openai.com/api-keys
    2. Create a new key
    3. Copy and paste it in the sidebar

    **Or** add it to your `.env` file:
    ```
    OPENAI_API_KEY=sk-your-key-here
    ```
    """)
    st.stop()

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Options
st.sidebar.subheader("Transcription Options")

task = st.sidebar.selectbox(
    "Task",
    ["Transcribe", "Translate to English"],
    help="Translate converts any language to English"
)

language = st.sidebar.text_input(
    "Language (optional)",
    placeholder="auto-detect",
    help="Leave empty for auto-detection. Use ISO codes: en, es, fr, de, etc."
)

# --- Main Interface ---
st.header("1. Upload Audio File")

uploaded_file = st.file_uploader(
    "Choose an audio file",
    type=['mp3', 'mp4', 'm4a', 'wav', 'webm', 'ogg', 'flac'],
    help="Max file size: 25MB"
)

if uploaded_file:
    # Show file info
    st.write(f"**File:** {uploaded_file.name}")
    st.write(f"**Size:** {uploaded_file.size / 1024 / 1024:.2f} MB")

    # Check file size
    if uploaded_file.size > 25 * 1024 * 1024:
        st.error("File is too large! Maximum size is 25MB.")
        st.info("Tip: You can compress or split the audio file using tools like Audacity.")
        st.stop()

    # Audio player
    st.audio(uploaded_file)

    # Transcribe button
    st.header("2. Transcribe")

    if st.button("Start Transcription", type="primary"):
        with st.spinner("Transcribing... This may take a moment."):
            try:
                # Save uploaded file to temp location
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as tmp:
                    tmp.write(uploaded_file.getvalue())
                    tmp_path = tmp.name

                # Open and transcribe
                with open(tmp_path, 'rb') as audio_file:
                    if task == "Translate to English":
                        # Translation
                        result = client.audio.translations.create(
                            model="whisper-1",
                            file=audio_file
                        )
                    else:
                        # Transcription
                        params = {
                            "model": "whisper-1",
                            "file": audio_file
                        }
                        if language:
                            params["language"] = language

                        result = client.audio.transcriptions.create(**params)

                # Clean up temp file
                os.unlink(tmp_path)

                # Store result
                st.session_state['transcript'] = result.text
                st.success("Transcription complete!")

            except Exception as e:
                st.error(f"Error during transcription: {e}")
                if "invalid_api_key" in str(e).lower():
                    st.info("Please check your API key.")

# --- Results ---
if 'transcript' in st.session_state:
    st.header("3. Results")

    transcript = st.session_state['transcript']

    # Stats
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Characters", f"{len(transcript):,}")
    with col2:
        st.metric("Words", f"{len(transcript.split()):,}")
    with col3:
        st.metric("Sentences", transcript.count('.') + transcript.count('!') + transcript.count('?'))

    # Display transcript
    st.subheader("Transcript")
    st.text_area("", transcript, height=300)

    # Download options
    st.subheader("Download")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download as TXT",
            transcript,
            file_name="transcript.txt",
            mime="text/plain"
        )

    with col2:
        # Create SRT-like format (simple)
        srt_content = f"1\n00:00:00,000 --> 00:00:00,000\n{transcript}\n"
        st.download_button(
            "Download as SRT",
            srt_content,
            file_name="transcript.srt",
            mime="text/plain"
        )

    # Clear button
    if st.button("Clear & Start Over"):
        del st.session_state['transcript']
        st.rerun()

else:
    if not uploaded_file:
        st.info("Upload an audio file to begin transcription.")

# --- Tips ---
st.markdown("---")
with st.expander("Tips & Information"):
    st.markdown("""
    **Supported Formats:**
    - MP3, MP4, M4A, WAV, WebM, OGG, FLAC

    **File Size Limit:**
    - Maximum 25MB per file
    - For larger files, split them using audio editing software

    **Languages:**
    - Whisper supports 50+ languages
    - Leave language empty for auto-detection
    - Specify for better accuracy: en, es, fr, de, ja, zh, etc.

    **Costs:**
    - Whisper API: $0.006 per minute of audio
    - 10 minutes of audio = ~$0.06

    **For Free/Offline Transcription:**
    - Install local Whisper: `pip install openai-whisper`
    - See `local_transcriber.py` template
    """)

# --- Footer ---
st.markdown("---")
st.markdown("*Built with Streamlit & OpenAI Whisper | Digital Scholarship Lab Starter Kit*")
