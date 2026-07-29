"""Central configuration for the Voice-to-Voice AI Assistant."""

import os
from pathlib import Path

from dotenv import load_dotenv


# ---------------------------------------------------------------------------
# Project paths
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"

RECORDING_FILE = BASE_DIR / "recording.wav"
TRANSCRIPT_FILE = BASE_DIR / "transcript.txt"
LLM_RESPONSE_FILE = BASE_DIR / "response.txt"
RESPONSE_AUDIO_FILE = BASE_DIR / "response_audio.wav"


# ---------------------------------------------------------------------------
# Environment variables
# ---------------------------------------------------------------------------

load_dotenv(dotenv_path=ENV_FILE)

COHERE_API_KEY = os.getenv("COHERE_API_KEY", "").strip()
COHERE_MODEL = os.getenv(
    "COHERE_MODEL",
    "command-a-plus-05-2026",
).strip()


# ---------------------------------------------------------------------------
# Audio recording configuration
# ---------------------------------------------------------------------------

RECORDING_DURATION = 5
COUNTDOWN_SECONDS = 3

SAMPLE_RATE = 16_000
CHANNELS = 1
AUDIO_DTYPE = "int16"


# ---------------------------------------------------------------------------
# Whisper speech-to-text configuration
# ---------------------------------------------------------------------------

WHISPER_MODEL = "base"


# ---------------------------------------------------------------------------
# Cohere LLM configuration
# ---------------------------------------------------------------------------

MAX_TOKENS = 500
TEMPERATURE = 0.3

SYSTEM_MESSAGE = (
    "You are a helpful voice AI assistant. "
    "Provide clear, accurate, and concise responses that sound natural "
    "when spoken aloud."
)


# ---------------------------------------------------------------------------
# Text-to-speech configuration
# ---------------------------------------------------------------------------

TTS_DRIVER = "sapi5"

PREFERRED_VOICE_INDEX = 1
SPEECH_RATE = 170
SPEECH_VOLUME = 1.0


# ---------------------------------------------------------------------------
# Terminal interface configuration
# ---------------------------------------------------------------------------

APP_TITLE = "Voice-to-Voice AI Assistant"
DIVIDER_WIDTH = 60