"""Application controller for the Text-to-Speech Assistant."""

from time import perf_counter

from tts_engine import (
    TTSEngineError,
    create_engine,
    play_audio_file,
    synthesize_to_file,
)
from utils import (
    display_session_summary,
    get_text_input,
    print_banner,
    print_status,
)


EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INTERRUPTED = 130


def run_application() -> int:
    """Run one complete text-to-speech session.

    Returns:
        An operating-system exit code indicating whether the
        application completed successfully.
    """
    print_banner()

    try:
        text = get_text_input()
        session_start = perf_counter()

        print_status("Initializing text-to-speech engine...")

        engine, voice_info = create_engine()

        print_status("Generating audio...")

        result = synthesize_to_file(
            engine=engine,
            text=text,
            voice_info=voice_info,
        )

        print_status("Audio generated successfully.")
        print(f"Saved to: {result.audio_file}")

        print_status("Playing audio...")

        playback_time = play_audio_file(result.audio_file)
        total_runtime = perf_counter() - session_start

        print_status("Audio playback completed.")

        display_session_summary(
            voice_name=result.voice.name,
            voice_index=result.voice.index,
            character_count=result.character_count,
            synthesis_time=result.synthesis_time,
            playback_time=playback_time,
            total_runtime=total_runtime,
            audio_file=result.audio_file,
        )

    except KeyboardInterrupt:
        print_status("Application cancelled by user.")
        return EXIT_INTERRUPTED

    except ValueError as error:
        print_status(f"Input error: {error}")
        return EXIT_FAILURE

    except TTSEngineError as error:
        print_status(f"Text-to-speech error: {error}")
        return EXIT_FAILURE

    except OSError as error:
        print_status(f"File error: {error}")
        return EXIT_FAILURE

    return EXIT_SUCCESS


def main() -> int:
    """Provide the main entry point for the application.

    Returns:
        The application's exit code.
    """
    return run_application()


if __name__ == "__main__":
    raise SystemExit(main())