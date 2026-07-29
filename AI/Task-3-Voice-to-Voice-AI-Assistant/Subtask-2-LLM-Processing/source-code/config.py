"""Central configuration for the LLM Processing application."""

import os
from pathlib import Path

from dotenv import load_dotenv


# Project paths
BASE_DIR = Path(__file__).resolve().parent
ENV_FILE = BASE_DIR / ".env"
RESPONSE_FILE = BASE_DIR / "response.txt"

# Load environment variables from the local .env file.
load_dotenv(dotenv_path=ENV_FILE)

# Cohere configuration
COHERE_API_KEY = os.getenv("COHERE_API_KEY", "").strip()
COHERE_MODEL = os.getenv(
    "COHERE_MODEL",
    "command-a-plus-05-2026",
).strip()

# Text-generation configuration
MAX_TOKENS = 500
TEMPERATURE = 0.3

# Assistant behavior
SYSTEM_MESSAGE = (
    "You are a helpful AI assistant. "
    "Provide clear, accurate, and well-structured responses."
)

# Terminal interface configuration
APP_TITLE = "LLM Processing Assistant"
DIVIDER_WIDTH = 50