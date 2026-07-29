"""Microphone recording services for the Voice AI Assistant."""

from dataclasses import dataclass
from pathlib import Path
from time import perf_counter

import sounddevice as sd
from scipy.io.wavfile import write as write_wav

from config import (
    AUDIO_DTYPE,
    CHANNELS,
    RECORDING_DURATION,
    RECORDING_FILE,
    SAMPLE_RATE,
)


class AudioRecordingError(RuntimeError):
    """Raised when microphone recording cannot be completed."""


@dataclass(frozen=True)
class RecordingResult:
    """Store information about a completed microphone recording."""

    audio_file: Path
    recording_time: float
    duration: int
    sample_rate: int
    channels: int
    sample_count: int


def validate_recording_settings(
    duration: int,
    sample_rate: int,
    channels: int,
) -> None:
    """Validate the supplied audio-recording settings.

    Args:
        duration: Recording duration in seconds.
        sample_rate: Number of audio samples captured per second.
        channels: Number of audio channels.

    Raises:
        ValueError: If any recording setting is invalid.
    """
    if duration <= 0:
        raise ValueError(
            "The recording duration must be greater than zero."
        )

    if sample_rate <= 0:
        raise ValueError(
            "The sample rate must be greater than zero."
        )

    if channels <= 0:
        raise ValueError(
            "The number of audio channels must be greater than zero."
        )


def remove_previous_recording(audio_file: Path) -> None:
    """Remove an existing recording before creating a new one.

    Args:
        audio_file: Path of the recording file.

    Raises:
        AudioRecordingError: If the previous file cannot be removed.
    """
    if not audio_file.exists():
        return

    try:
        audio_file.unlink()
    except OSError as error:
        raise AudioRecordingError(
            f"The previous recording could not be removed: {error}"
        ) from error


def record_audio(
    output_file: Path = RECORDING_FILE,
    duration: int = RECORDING_DURATION,
    sample_rate: int = SAMPLE_RATE,
    channels: int = CHANNELS,
    dtype: str = AUDIO_DTYPE,
) -> RecordingResult:
    """Record microphone audio and save it as a WAV file.

    Args:
        output_file: Destination path for the WAV recording.
        duration: Recording duration in seconds.
        sample_rate: Number of samples captured per second.
        channels: Number of recording channels.
        dtype: NumPy data type used for captured samples.

    Returns:
        Information about the completed recording.

    Raises:
        ValueError: If the recording settings are invalid.
        AudioRecordingError: If recording or file creation fails.
    """
    validate_recording_settings(
        duration=duration,
        sample_rate=sample_rate,
        channels=channels,
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    remove_previous_recording(output_file)

    sample_count = int(duration * sample_rate)
    recording_start = perf_counter()

    try:
        audio_data = sd.rec(
            frames=sample_count,
            samplerate=sample_rate,
            channels=channels,
            dtype=dtype,
        )

        sd.wait()

    except sd.PortAudioError as error:
        raise AudioRecordingError(
            f"Microphone recording failed: {error}"
        ) from error

    except Exception as error:
        raise AudioRecordingError(
            f"An unexpected recording error occurred: {error}"
        ) from error

    recording_time = perf_counter() - recording_start

    try:
        write_wav(
            filename=output_file,
            rate=sample_rate,
            data=audio_data,
        )
    except (OSError, ValueError) as error:
        raise AudioRecordingError(
            f"The WAV recording could not be saved: {error}"
        ) from error

    if not output_file.exists():
        raise AudioRecordingError(
            "Recording finished without creating an audio file."
        )

    if output_file.stat().st_size == 0:
        raise AudioRecordingError(
            "The generated recording file is empty."
        )

    return RecordingResult(
        audio_file=output_file,
        recording_time=recording_time,
        duration=duration,
        sample_rate=sample_rate,
        channels=channels,
        sample_count=sample_count,
    )