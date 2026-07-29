"""Terminal interface utilities for the Text-to-Speech application."""

from pathlib import Path

from config import APP_TITLE, DIVIDER_WIDTH


def print_banner() -> None:
    """Display the application title."""

    divider = "=" * DIVIDER_WIDTH

    print()
    print(divider)
    print(APP_TITLE.center(DIVIDER_WIDTH))
    print(divider)
    print()


def get_text_input() -> str:
    """Read and validate text entered by the user.

    Returns:
        Non-empty text to convert into speech.
    """
    while True:
        print("Enter the text you want to convert to speech:")
        text = input("> ").strip()

        if text:
            return text

        print()
        print("The text cannot be empty. Please try again.")
        print()


def print_status(message: str) -> None:
    """Display a processing-status message.

    Args:
        message: Status text to display.
    """
    print()
    print(message)
    print()


def display_session_summary(
    voice_name: str,
    voice_index: int,
    character_count: int,
    synthesis_time: float,
    playback_time: float,
    total_runtime: float,
    audio_file: Path,
) -> None:
    """Display information about a completed speech session.

    Args:
        voice_name: Name of the selected Windows voice.
        voice_index: Index of the selected voice.
        character_count: Number of characters converted to speech.
        synthesis_time: Time required to generate the WAV file.
        playback_time: Time required to play the WAV file.
        total_runtime: Total application processing time.
        audio_file: Path of the generated audio file.
    """
    divider = "=" * DIVIDER_WIDTH

    print("Session Summary")
    print(divider)
    print(f"Voice:             {voice_name}")
    print(f"Voice Index:       {voice_index}")
    print(f"Characters:        {character_count}")
    print(f"Synthesis Time:    {synthesis_time:.2f} seconds")
    print(f"Playback Time:     {playback_time:.2f} seconds")
    print(f"Total Runtime:     {total_runtime:.2f} seconds")
    print(f"Audio Saved:       {audio_file}")
    print(divider)
    