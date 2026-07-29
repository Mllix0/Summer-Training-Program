"""Text-to-speech generation and playback services."""

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
import winsound

import pyttsx3
from pyttsx3.engine import Engine

from config import (
    OUTPUT_AUDIO_FILE,
    PREFERRED_VOICE_INDEX,
    SPEECH_RATE,
    SPEECH_VOLUME,
    TTS_DRIVER,
)


class TTSEngineError(RuntimeError):
    """Raised when text-to-speech processing cannot be completed."""


@dataclass(frozen=True)
class VoiceInfo:
    """Store information about the selected speech voice."""

    index: int
    name: str


@dataclass(frozen=True)
class SynthesisResult:
    """Store the result of a text-to-speech conversion."""

    audio_file: Path
    synthesis_time: float
    voice: VoiceInfo
    character_count: int


def select_voice(engine: Engine) -> VoiceInfo:
    """Select the configured voice or safely use the first voice.

    Args:
        engine: An initialized pyttsx3 engine.

    Returns:
        Information about the selected voice.

    Raises:
        TTSEngineError: If Windows has no available speech voices.
    """
    voices = engine.getProperty("voices")

    if not voices:
        raise TTSEngineError(
            "No text-to-speech voices were found on this computer."
        )

    if 0 <= PREFERRED_VOICE_INDEX < len(voices):
        selected_index = PREFERRED_VOICE_INDEX
    else:
        selected_index = 0

    selected_voice = voices[selected_index]

    try:
        engine.setProperty("voice", selected_voice.id)
    except Exception as error:
        raise TTSEngineError(
            "The selected text-to-speech voice could not be configured."
        ) from error

    voice_name = getattr(
        selected_voice,
        "name",
        f"Voice {selected_index}",
    )

    return VoiceInfo(
        index=selected_index,
        name=voice_name,
    )


def create_engine() -> tuple[Engine, VoiceInfo]:
    """Create and configure the text-to-speech engine.

    Returns:
        The configured engine and selected voice information.

    Raises:
        TTSEngineError: If the speech engine cannot be initialized.
    """
    try:
        engine = pyttsx3.init(TTS_DRIVER)

        engine.setProperty("rate", SPEECH_RATE)
        engine.setProperty("volume", SPEECH_VOLUME)

        voice_info = select_voice(engine)

    except TTSEngineError:
        raise

    except Exception as error:
        raise TTSEngineError(
            f"The text-to-speech engine could not be initialized: {error}"
        ) from error

    return engine, voice_info


def synthesize_to_file(
    engine: Engine,
    text: str,
    voice_info: VoiceInfo,
    output_file: Path = OUTPUT_AUDIO_FILE,
) -> SynthesisResult:
    """Convert text into a WAV audio file.

    Args:
        engine: A configured pyttsx3 engine.
        text: Text that will be converted into speech.
        voice_info: Information about the active speech voice.
        output_file: Destination path for the generated WAV file.

    Returns:
        Information about the completed synthesis operation.

    Raises:
        ValueError: If the supplied text is empty.
        TTSEngineError: If audio generation fails.
    """
    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError("The text-to-speech input cannot be empty.")

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    try:
        if output_file.exists():
            output_file.unlink()
    except OSError as error:
        raise TTSEngineError(
            f"The previous audio file could not be removed: {error}"
        ) from error

    synthesis_start = perf_counter()

    try:
        engine.save_to_file(
            cleaned_text,
            str(output_file),
        )
        engine.runAndWait()

    except Exception as error:
        raise TTSEngineError(
            f"Audio generation failed: {error}"
        ) from error

    synthesis_time = perf_counter() - synthesis_start

    if not output_file.exists():
        raise TTSEngineError(
            "The speech engine finished without creating an audio file."
        )

    if output_file.stat().st_size == 0:
        raise TTSEngineError(
            "The generated audio file is empty."
        )

    return SynthesisResult(
        audio_file=output_file,
        synthesis_time=synthesis_time,
        voice=voice_info,
        character_count=len(cleaned_text),
    )


def play_audio_file(audio_file: Path) -> float:
    """Play a WAV audio file and return its playback time.

    Args:
        audio_file: Path to the generated WAV file.

    Returns:
        Time spent playing the audio.

    Raises:
        TTSEngineError: If the WAV file cannot be played.
    """
    if not audio_file.exists():
        raise TTSEngineError(
            f"Audio file not found: {audio_file}"
        )

    playback_start = perf_counter()

    try:
        winsound.PlaySound(
            str(audio_file),
            winsound.SND_FILENAME,
        )
    except RuntimeError as error:
        raise TTSEngineError(
            f"Audio playback failed: {error}"
        ) from error

    return perf_counter() - playback_start