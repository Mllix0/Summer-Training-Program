import time
from typing import Any

import whisper

from config import AUDIO_FILE, MODEL_NAME


def load_whisper_model() -> tuple[Any, float]:
    """
    Load the configured Whisper model.

    Returns:
        The loaded model and the model-loading time.
    """
    print("\nLoading Whisper model...")

    loading_start = time.perf_counter()

    model = whisper.load_model(MODEL_NAME)

    loading_time = time.perf_counter() - loading_start

    print("Whisper model loaded successfully.")

    return model, loading_time


def transcribe_audio(model: Any) -> tuple[str, str, float]:
    """
    Transcribe the saved audio.

    Returns:
        Recognized text, detected language, and transcription time.
    """
    if not AUDIO_FILE.exists():
        raise FileNotFoundError(
            f"The audio file was not found: {AUDIO_FILE}"
        )

    print("\nRecognizing speech...")
    print("Please wait while Whisper processes the recording.")

    transcription_start = time.perf_counter()

    result = model.transcribe(
        str(AUDIO_FILE),
        fp16=False,
        verbose=False,
    )

    transcription_time = (
        time.perf_counter() - transcription_start
    )

    recognized_text = str(
        result.get("text", "")
    ).strip()

    detected_language = str(
        result.get("language", "unknown")
    ).strip()

    return (
        recognized_text,
        detected_language,
        transcription_time,
    )