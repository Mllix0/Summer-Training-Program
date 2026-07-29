"""Text-to-speech services for the Voice-to-Voice AI Assistant."""

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter
import winsound

import pyttsx3
from pyttsx3.engine import Engine

from config import (
    PREFERRED_VOICE_INDEX,
    RESPONSE_AUDIO_FILE,
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
    """Store information about generated speech audio."""

    audio_file: Path
    synthesis_time: float
    voice: VoiceInfo
    character_count: int
    file_size: int


def select_voice(engine: Engine) -> VoiceInfo:
    """Select the preferred Windows voice.

    The configured voice index is used when available. Otherwise,
    the first installed voice is selected as a safe fallback.

    Args:
        engine: An initialized pyttsx3 engine.

    Returns:
        Information about the selected voice.

    Raises:
        TTSEngineError: If no speech voices are available or the
            selected voice cannot be configured.
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
        engine.setProperty(
            "voice",
            selected_voice.id,
        )
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
        name=str(voice_name),
    )


def create_engine() -> tuple[Engine, VoiceInfo]:
    """Create and configure the text-to-speech engine.

    Returns:
        The configured pyttsx3 engine and selected voice information.

    Raises:
        TTSEngineError: If the speech engine cannot be initialized.
    """
    try:
        engine = pyttsx3.init(TTS_DRIVER)

        engine.setProperty(
            "rate",
            SPEECH_RATE,
        )
        engine.setProperty(
            "volume",
            SPEECH_VOLUME,
        )

        voice_info = select_voice(engine)

    except TTSEngineError:
        raise

    except Exception as error:
        raise TTSEngineError(
            f"The text-to-speech engine could not be initialized: "
            f"{error}"
        ) from error

    return engine, voice_info


def remove_previous_audio(audio_file: Path) -> None:
    """Remove the previous generated response audio.

    Args:
        audio_file: Path of the generated response audio.

    Raises:
        TTSEngineError: If the existing audio cannot be removed.
    """
    if not audio_file.exists():
        return

    try:
        audio_file.unlink()
    except OSError as error:
        raise TTSEngineError(
            f"The previous response audio could not be removed: {error}"
        ) from error


def validate_generated_audio(audio_file: Path) -> int:
    """Verify that generated speech audio exists and contains data.

    Args:
        audio_file: Path of the generated WAV file.

    Returns:
        Generated audio-file size in bytes.

    Raises:
        TTSEngineError: If the file is missing, invalid, or empty.
    """
    if not audio_file.exists():
        raise TTSEngineError(
            "The speech engine finished without creating an audio file."
        )

    if not audio_file.is_file():
        raise TTSEngineError(
            f"The generated audio path is not a file: {audio_file}"
        )

    try:
        file_size = audio_file.stat().st_size
    except OSError as error:
        raise TTSEngineError(
            f"The generated audio file could not be inspected: {error}"
        ) from error

    if file_size == 0:
        raise TTSEngineError(
            "The generated response audio file is empty."
        )

    return file_size


def synthesize_to_file(
    engine: Engine,
    text: str,
    voice_info: VoiceInfo,
    output_file: Path = RESPONSE_AUDIO_FILE,
) -> SynthesisResult:
    """Convert an AI text response into a WAV audio file.

    Args:
        engine: A configured pyttsx3 speech engine.
        text: AI response that will be converted into speech.
        voice_info: Information about the active Windows voice.
        output_file: Destination path for the generated WAV file.

    Returns:
        Information about the completed synthesis operation.

    Raises:
        ValueError: If the supplied response text is empty.
        TTSEngineError: If speech synthesis fails.
    """
    cleaned_text = text.strip()

    if not cleaned_text:
        raise ValueError(
            "The AI response cannot be empty."
        )

    try:
        output_file.parent.mkdir(
            parents=True,
            exist_ok=True,
        )
    except OSError as error:
        raise TTSEngineError(
            f"The audio output folder could not be prepared: {error}"
        ) from error

    remove_previous_audio(output_file)

    synthesis_start = perf_counter()

    try:
        engine.save_to_file(
            cleaned_text,
            str(output_file),
        )
        engine.runAndWait()

    except Exception as error:
        raise TTSEngineError(
            f"Response audio generation failed: {error}"
        ) from error

    synthesis_time = perf_counter() - synthesis_start
    file_size = validate_generated_audio(output_file)

    return SynthesisResult(
        audio_file=output_file,
        synthesis_time=synthesis_time,
        voice=voice_info,
        character_count=len(cleaned_text),
        file_size=file_size,
    )


def play_audio_file(audio_file: Path) -> float:
    """Play the generated WAV response.

    Playback is synchronous, so the function returns only after the
    spoken response finishes.

    Args:
        audio_file: Path of the generated WAV response.

    Returns:
        Time spent playing the generated audio.

    Raises:
        TTSEngineError: If the audio file cannot be played.
    """
    validate_generated_audio(audio_file)

    playback_start = perf_counter()

    try:
        winsound.PlaySound(
            str(audio_file),
            winsound.SND_FILENAME,
        )
    except RuntimeError as error:
        raise TTSEngineError(
            f"Response audio playback failed: {error}"
        ) from error

    return perf_counter() - playback_start