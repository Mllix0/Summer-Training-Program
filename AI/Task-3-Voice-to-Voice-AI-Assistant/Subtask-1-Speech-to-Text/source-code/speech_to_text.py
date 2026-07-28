import time

from recorder import record_audio
from transcriber import (
    load_whisper_model,
    transcribe_audio,
)
from utils import (
    print_banner,
    print_result,
    print_session_summary,
    save_transcript,
    wait_for_user,
)


def main() -> None:
    """Run the complete speech-to-text application."""
    application_start = time.perf_counter()

    try:
        print_banner()
        wait_for_user()

        recording_time = record_audio()

        model, model_loading_time = load_whisper_model()

        (
            recognized_text,
            detected_language,
            transcription_time,
        ) = transcribe_audio(model)

        print_result(
            recognized_text,
            detected_language,
        )

        save_transcript(
            recognized_text,
            detected_language,
        )

        total_runtime = (
            time.perf_counter() - application_start
        )

        print_session_summary(
            recording_time=recording_time,
            model_loading_time=model_loading_time,
            transcription_time=transcription_time,
            total_runtime=total_runtime,
            detected_language=detected_language,
        )

    except KeyboardInterrupt:
        print("\n\nProgram stopped by the user.")

    except FileNotFoundError as error:
        print("\nFile error:")
        print(error)

    except RuntimeError as error:
        print("\nAudio error:")
        print(error)

    except Exception as error:
        print("\nAn unexpected error occurred:")
        print(f"{type(error).__name__}: {error}")


if __name__ == "__main__":
    main()