"""Central configuration for the Text-to-Speech application."""

from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent
OUTPUT_AUDIO_FILE = BASE_DIR / "response_audio.wav"

# Text-to-speech engine
TTS_DRIVER = "sapi5"

# Voice configuration
PREFERRED_VOICE_INDEX = 1
SPEECH_RATE = 170
SPEECH_VOLUME = 1.0

# Terminal interface
APP_TITLE = "Text-to-Speech Assistant"
DIVIDER_WIDTH = 50