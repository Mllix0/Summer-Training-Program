import time

import sounddevice as sd
import soundfile as sf

from config import (
    AUDIO_DTYPE,
    AUDIO_FILE,
    CHANNELS,
    DURATION,
    SAMPLE_RATE,
)
from utils import countdown


def record_audio() -> float:
    """
    Record microphone audio, save it as a WAV file,
    and return the actual recording time.
    """
    countdown()

    print(f"\nRecording for {DURATION} seconds...")

    try:
        recording_start = time.perf_counter()

        audio = sd.rec(
            int(DURATION * SAMPLE_RATE),
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype=AUDIO_DTYPE,
        )

        sd.wait()

        recording_time = time.perf_counter() - recording_start

        sf.write(
            str(AUDIO_FILE),
            audio,
            SAMPLE_RATE,
        )

    except sd.PortAudioError as error:
        raise RuntimeError(
            "The microphone could not be accessed. "
            "Check your Windows microphone settings and input device."
        ) from error

    print("Recording complete.")
    print(f"Audio saved as: {AUDIO_FILE}")

    return recording_time