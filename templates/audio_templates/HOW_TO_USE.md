# 🎤 Audio & Transcription Templates

Transcribe audio files and work with speech-to-text.

## What You Can Build

- **Audio transcription** — Convert speech to text
- **Interview processing** — Transcribe recorded interviews
- **Podcast analysis** — Get text from podcasts
- **Meeting notes** — Automatic transcription
- **Oral history projects** — Transcribe historical recordings

---

## Available Templates

### 1. `simple_transcriber.py` — Audio Transcriber (Streamlit App)
A web app to transcribe audio files using OpenAI's Whisper API.

**Features:**
- Upload audio files (mp3, wav, m4a)
- Automatic transcription
- Download transcript as text
- Support for multiple languages

**How to use:**

1. **Set up your OpenAI API key** in `.env` file:
   ```
   OPENAI_API_KEY=your_key_here
   ```

2. **Run the app:**
   ```bash
   streamlit run templates/audio_templates/simple_transcriber.py
   ```

3. **Upload an audio file** and click transcribe

---

### 2. `local_transcriber.py` — Offline Transcriber
Uses the local Whisper model (no API key needed, but slower).

**Features:**
- Works completely offline
- No API costs
- Supports all Whisper model sizes
- Batch processing

**How to use:**

1. **Install Whisper:**
   ```bash
   pip install openai-whisper
   ```

2. **Run the script:**
   ```bash
   python templates/audio_templates/local_transcriber.py
   ```

---

## Example Ideas

### Simple Ideas (Beginners)
- **Voice Memo Transcriber** — Convert voice notes to text
- **Lecture Notes** — Transcribe recorded lectures
- **Interview Transcript** — Process interview recordings
- **Language Learning** — Transcribe foreign language audio

### Medium Ideas
- **Podcast Summarizer** — Transcribe and summarize podcasts
- **Meeting Minutes** — Auto-generate meeting notes
- **Subtitle Generator** — Create subtitles with timestamps
- **Audio Search** — Search through audio by transcribing first

### Advanced Ideas
- **Oral History Archive** — Process historical recordings
- **Multi-speaker Detection** — Identify different speakers
- **Sentiment from Speech** — Analyze tone and sentiment
- **Multilingual Transcription** — Transcribe multiple languages

---

## Quick Tips

### Using OpenAI Whisper API (Easiest)
```python
from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

# Transcribe audio file
with open('audio.mp3', 'rb') as audio_file:
    transcript = client.audio.transcriptions.create(
        model="whisper-1",
        file=audio_file
    )

print(transcript.text)
```

### Get Timestamps
```python
transcript = client.audio.transcriptions.create(
    model="whisper-1",
    file=audio_file,
    response_format="verbose_json",
    timestamp_granularities=["segment"]
)

# Access segments with timestamps
for segment in transcript.segments:
    print(f"[{segment['start']:.2f}s] {segment['text']}")
```

### Translate Audio (to English)
```python
# Automatically translates non-English audio to English
translation = client.audio.translations.create(
    model="whisper-1",
    file=audio_file
)

print(translation.text)
```

### Using Local Whisper (Free, Offline)
```python
import whisper

# Load model (tiny, base, small, medium, large)
model = whisper.load_model("base")

# Transcribe
result = model.transcribe("audio.mp3")

print(result["text"])

# With timestamps
for segment in result["segments"]:
    print(f"[{segment['start']:.2f}s - {segment['end']:.2f}s] {segment['text']}")
```

### Supported Audio Formats
- MP3 (.mp3)
- WAV (.wav)
- M4A (.m4a)
- FLAC (.flac)
- OGG (.ogg)
- WebM (.webm)

### Batch Processing
```python
import glob
import os

audio_files = glob.glob('data/raw/*.mp3')

for audio_path in audio_files:
    with open(audio_path, 'rb') as audio_file:
        transcript = client.audio.transcriptions.create(
            model="whisper-1",
            file=audio_file
        )

    # Save transcript
    output_path = audio_path.replace('.mp3', '.txt')
    with open(output_path, 'w') as f:
        f.write(transcript.text)

    print(f"Transcribed: {os.path.basename(audio_path)}")
```

---

## Common Issues

### "OpenAI API key not set"
Create a `.env` file with:
```
OPENAI_API_KEY=sk-your-key-here
```

### "File too large" (API limit: 25MB)
```python
# Split audio file using pydub
from pydub import AudioSegment

audio = AudioSegment.from_mp3("large_file.mp3")

# Split into 10-minute chunks
chunk_length = 10 * 60 * 1000  # 10 minutes in milliseconds

chunks = []
for i in range(0, len(audio), chunk_length):
    chunk = audio[i:i + chunk_length]
    chunk.export(f"chunk_{i//chunk_length}.mp3", format="mp3")
```

### "Module not found: openai"
```bash
pip install openai
```

### Local Whisper too slow
```python
# Use a smaller model
model = whisper.load_model("tiny")  # Fastest
model = whisper.load_model("base")  # Good balance
# model = whisper.load_model("large")  # Most accurate but slow
```

### Audio quality issues
- Use a good microphone
- Reduce background noise
- Convert to a standard format first:
```python
from pydub import AudioSegment

audio = AudioSegment.from_file("input.m4a")
audio.export("output.mp3", format="mp3", bitrate="128k")
```

---

## Model Comparison

### OpenAI API (whisper-1)
| Pros | Cons |
|------|------|
| Very fast | Costs money |
| High accuracy | Requires internet |
| No GPU needed | 25MB file limit |

### Local Whisper
| Model | Speed | Accuracy | Memory |
|-------|-------|----------|--------|
| tiny | Fastest | Good | ~1GB |
| base | Fast | Better | ~1GB |
| small | Medium | Good | ~2GB |
| medium | Slow | Very Good | ~5GB |
| large | Slowest | Best | ~10GB |

---

## Learn More

- [OpenAI Whisper API](https://platform.openai.com/docs/guides/speech-to-text)
- [Whisper GitHub](https://github.com/openai/whisper)
- [pydub Documentation](https://github.com/jiaaro/pydub)
- [Audio Processing with Python](https://realpython.com/playing-and-recording-sound-python/)

---

**Need help?** Ask your instructor or check the main README.md
