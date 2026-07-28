from pathlib import Path


# -----------------------------
# Recording Settings
# -----------------------------
DURATION = 5
SAMPLE_RATE = 16000
CHANNELS = 1
AUDIO_DTYPE = "float32"

# -----------------------------
# Whisper Settings
# -----------------------------
MODEL_NAME = "base"

# -----------------------------
# File Paths
# -----------------------------
PROJECT_FOLDER = Path(__file__).resolve().parent
AUDIO_FILE = PROJECT_FOLDER / "recording.wav"
TRANSCRIPT_FILE = PROJECT_FOLDER / "transcript.txt"

# -----------------------------
# Interface Settings
# -----------------------------
COUNTDOWN_SECONDS = 3
BANNER_WIDTH = 50