"""Speech transcription services for the Voice AI Assistant."""

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
from typing import Any

import torch
import whisper
from whisper.model import Whisper

from config import RECORDING_FILE, WHISPER_MODEL


class TranscriptionError(RuntimeError):
    """Raised when speech transcription cannot be completed."""


@dataclass(frozen=True)
class LoadedWhisperModel:
    """Store a loaded Whisper model and its configuration details."""

    model: Whisper
    model_name: str
    device: str
    loading_time: float


@dataclass(frozen=True)
class TranscriptionResult:
    """Store the result of a completed speech transcription."""

    text: str
    language_code: str
    transcription_time: float
    model_name: str
    model_loading_time: float
    device: str


def select_processing_device() -> str:
    """Select the best available device for Whisper processing.

    Returns:
        ``"cuda"`` when a compatible GPU is available; otherwise,
        ``"cpu"``.
    """
    return "cuda" if torch.cuda.is_available() else "cpu"


def load_whisper_model(
    model_name: str = WHISPER_MODEL,
    device: str | None = None,
) -> LoadedWhisperModel:
    """Load a Whisper speech-recognition model.

    Args:
        model_name: Name of the Whisper model to load.
        device: Optional processing device. When omitted, the function
            automatically selects CUDA or CPU.

    Returns:
        The loaded model with timing and device information.

    Raises:
        ValueError: If the model name is empty.
        TranscriptionError: If Whisper cannot load the model.
    """
    cleaned_model_name = model_name.strip()

    if not cleaned_model_name:
        raise ValueError("The Whisper model name cannot be empty.")

    selected_device = device or select_processing_device()
    loading_start = perf_counter()

    try:
        model = whisper.load_model(
            cleaned_model_name,
            device=selected_device,
        )
    except Exception as error:
        raise TranscriptionError(
            f"The Whisper model could not be loaded: {error}"
        ) from error

    loading_time = perf_counter() - loading_start

    return LoadedWhisperModel(
        model=model,
        model_name=cleaned_model_name,
        device=selected_device,
        loading_time=loading_time,
    )


def validate_audio_file(audio_file: Path) -> None:
    """Verify that an audio file exists and contains data.

    Args:
        audio_file: Path to the recording that will be transcribed.

    Raises:
        TranscriptionError: If the audio file is missing or empty.
    """
    if not audio_file.exists():
        raise TranscriptionError(
            f"The recording file was not found: {audio_file}"
        )

    if not audio_file.is_file():
        raise TranscriptionError(
            f"The recording path is not a file: {audio_file}"
        )

    try:
        file_size = audio_file.stat().st_size
    except OSError as error:
        raise TranscriptionError(
            f"The recording file could not be inspected: {error}"
        ) from error

    if file_size == 0:
        raise TranscriptionError(
            "The recording file is empty."
        )


def extract_transcription(
    raw_result: dict[str, Any],
) -> tuple[str, str]:
    """Extract recognized text and language from Whisper output.

    Args:
        raw_result: Dictionary returned by Whisper.

    Returns:
        The cleaned recognized text and detected language code.

    Raises:
        TranscriptionError: If Whisper returns no recognized speech.
    """
    recognized_text = str(
        raw_result.get("text", "")
    ).strip()

    language_code = str(
        raw_result.get("language", "unknown")
    ).strip().lower()

    if not recognized_text:
        raise TranscriptionError(
            "No recognizable speech was detected in the recording."
        )

    if not language_code:
        language_code = "unknown"

    return recognized_text, language_code


def transcribe_audio(
    loaded_model: LoadedWhisperModel,
    audio_file: Path = RECORDING_FILE,
) -> TranscriptionResult:
    """Transcribe a recorded audio file using Whisper.

    Args:
        loaded_model: A model returned by ``load_whisper_model``.
        audio_file: Path to the WAV recording.

    Returns:
        Recognized text, detected language, and timing information.

    Raises:
        TranscriptionError: If the recording cannot be transcribed.
    """
    validate_audio_file(audio_file)

    transcription_start = perf_counter()

    try:
        raw_result = loaded_model.model.transcribe(
            str(audio_file),
            fp16=loaded_model.device == "cuda",
            verbose=None,
        )
    except Exception as error:
        raise TranscriptionError(
            f"Speech transcription failed: {error}"
        ) from error

    transcription_time = perf_counter() - transcription_start

    if not isinstance(raw_result, dict):
        raise TranscriptionError(
            "Whisper returned an unexpected transcription format."
        )

    recognized_text, language_code = extract_transcription(
        raw_result
    )

    return TranscriptionResult(
        text=recognized_text,
        language_code=language_code,
        transcription_time=transcription_time,
        model_name=loaded_model.model_name,
        model_loading_time=loaded_model.loading_time,
        device=loaded_model.device,
    )