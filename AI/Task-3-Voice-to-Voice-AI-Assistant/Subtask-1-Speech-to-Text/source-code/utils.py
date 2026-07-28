from datetime import datetime
import time

from config import (
    BANNER_WIDTH,
    COUNTDOWN_SECONDS,
    MODEL_NAME,
    TRANSCRIPT_FILE,
)


LANGUAGE_NAMES = {
    "en": "English",
    "ar": "Arabic",
    "fr": "French",
    "de": "German",
    "es": "Spanish",
    "it": "Italian",
    "ja": "Japanese",
    "ko": "Korean",
    "zh": "Chinese",
    "pt": "Portuguese",
    "ru": "Russian",
    "tr": "Turkish",
}


def print_banner() -> None:
    """Display the application title."""
    print("\n" + "=" * BANNER_WIDTH)
    print("          Voice-to-Text AI Assistant")
    print("=" * BANNER_WIDTH)


def wait_for_user() -> None:
    """Pause until the user is ready to begin."""
    input("\nPress ENTER to start recording...")


def countdown(seconds: int = COUNTDOWN_SECONDS) -> None:
    """Show a countdown before recording starts."""
    print("\nRecording starts in:")

    for number in range(seconds, 0, -1):
        print(number)
        time.sleep(1)

    print("\nSpeak now!")


def get_language_name(language_code: str) -> str:
    """Convert a Whisper language code into a readable name."""
    normalized_code = language_code.lower().strip()

    return LANGUAGE_NAMES.get(
        normalized_code,
        normalized_code.upper() if normalized_code else "Unknown",
    )


def print_result(
    recognized_text: str,
    detected_language: str,
) -> None:
    """Display the transcription result in the terminal."""
    language_name = get_language_name(detected_language)

    print("\nDetected language:")
    print(language_name)

    print("\nRecognized text:")
    print("-" * BANNER_WIDTH)

    if recognized_text:
        print(recognized_text)
    else:
        print("No clear speech was detected.")

    print("-" * BANNER_WIDTH)


def save_transcript(
    recognized_text: str,
    detected_language: str,
) -> None:
    """Save the transcription and metadata to a text file."""
    language_name = get_language_name(detected_language)
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    final_text = (
        recognized_text
        if recognized_text
        else "No clear speech was detected."
    )

    transcript_content = (
        "=" * BANNER_WIDTH
        + "\nVoice-to-Text AI Assistant\n"
        + "=" * BANNER_WIDTH
        + f"\n\nDate:\n{current_time}"
        + f"\n\nWhisper Model:\n{MODEL_NAME}"
        + f"\n\nDetected Language:\n{language_name}"
        + "\n\nRecognized Text:\n"
        + final_text
        + "\n\n"
        + "=" * BANNER_WIDTH
        + "\n"
    )

    TRANSCRIPT_FILE.write_text(
        transcript_content,
        encoding="utf-8",
    )

    print(f"\nTranscript saved as: {TRANSCRIPT_FILE}")


def print_session_summary(
    recording_time: float,
    model_loading_time: float,
    transcription_time: float,
    total_runtime: float,
    detected_language: str,
) -> None:
    """Display performance and session information."""
    language_name = get_language_name(detected_language)

    print("\n" + "=" * BANNER_WIDTH)
    print("                 Session Summary")
    print("=" * BANNER_WIDTH)

    print(f"\nRecording Time      : {recording_time:.2f} seconds")
    print(f"Model Loading Time  : {model_loading_time:.2f} seconds")
    print(f"Transcription Time  : {transcription_time:.2f} seconds")
    print(f"Total Runtime       : {total_runtime:.2f} seconds")

    print(f"\nWhisper Model       : {MODEL_NAME}")
    print(f"Language            : {language_name}")
    print(f"Transcript Saved    : {TRANSCRIPT_FILE.name}")

    print("\n" + "=" * BANNER_WIDTH)