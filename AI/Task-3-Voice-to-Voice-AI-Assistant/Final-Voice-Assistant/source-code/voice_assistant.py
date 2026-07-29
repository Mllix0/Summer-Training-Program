"""Application controller for the Voice-to-Voice AI Assistant."""

from time import perf_counter

from config import (
    LLM_RESPONSE_FILE,
    TRANSCRIPT_FILE,
)
from llm_client import (
    LLMClientError,
    create_client,
    generate_response,
)
from recorder import (
    AudioRecordingError,
    record_audio,
)
from transcriber import (
    TranscriptionError,
    load_whisper_model,
    transcribe_audio,
)
from tts_engine import (
    TTSEngineError,
    create_engine,
    play_audio_file,
    synthesize_to_file,
)
from utils import (
    countdown,
    display_ai_response,
    display_session_summary,
    display_transcription,
    language_code_to_name,
    print_banner,
    print_status,
    save_text_file,
    wait_for_user,
)


EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INTERRUPTED = 130


def run_application() -> int:
    """Run one complete voice-to-voice assistant session.

    Returns:
        An operating-system exit code indicating whether the
        application completed successfully.
    """
    print_banner()

    try:
        wait_for_user()
        session_start = perf_counter()

        # Stage 1: Record the user's voice.
        countdown()

        print_status("Recording...")

        recording = record_audio()

        print_status("Recording completed.")

        # Stage 2: Convert the recording into text.
        print_status("Loading Whisper...")

        loaded_model = load_whisper_model()

        print_status("Recognizing speech...")

        transcription = transcribe_audio(
            loaded_model=loaded_model,
            audio_file=recording.audio_file,
        )

        language_name = language_code_to_name(
            transcription.language_code
        )

        display_transcription(
            recognized_text=transcription.text,
            language_name=language_name,
        )

        transcript_file = save_text_file(
            text=transcription.text,
            file_path=TRANSCRIPT_FILE,
        )

        print_status("Transcript saved successfully.")

        # Stage 3: Generate an AI response.
        print_status("Generating AI response...")

        llm_client = create_client()

        llm_response = generate_response(
            client=llm_client,
            user_message=transcription.text,
        )

        display_ai_response(llm_response.text)

        response_file = save_text_file(
            text=llm_response.text,
            file_path=LLM_RESPONSE_FILE,
        )

        print_status("AI response saved successfully.")

        # Stage 4: Convert the AI response into speech.
        print_status("Initializing text-to-speech engine...")

        tts_engine, voice_info = create_engine()

        print_status("Generating response audio...")

        synthesis = synthesize_to_file(
            engine=tts_engine,
            text=llm_response.text,
            voice_info=voice_info,
        )

        print_status("Response audio generated successfully.")

        # Stage 5: Play the spoken response.
        print_status("Playing AI response...")

        playback_time = play_audio_file(
            synthesis.audio_file
        )

        total_runtime = perf_counter() - session_start

        print_status("Response playback completed.")

        # Final session information.
        display_session_summary(
            recording_time=recording.recording_time,
            model_loading_time=transcription.model_loading_time,
            transcription_time=transcription.transcription_time,
            llm_response_time=llm_response.response_time,
            synthesis_time=synthesis.synthesis_time,
            playback_time=playback_time,
            total_runtime=total_runtime,
            whisper_model=transcription.model_name,
            whisper_device=transcription.device,
            cohere_model=llm_response.model_name,
            voice_name=synthesis.voice.name,
            language_name=language_name,
            transcript_character_count=len(transcription.text),
            response_character_count=(
                llm_response.response_character_count
            ),
            recording_file=recording.audio_file,
            transcript_file=transcript_file,
            response_file=response_file,
            response_audio_file=synthesis.audio_file,
        )

    except KeyboardInterrupt:
        print_status("Application cancelled by user.")
        return EXIT_INTERRUPTED

    except ValueError as error:
        print_status(f"Input error: {error}")
        return EXIT_FAILURE

    except AudioRecordingError as error:
        print_status(f"Recording error: {error}")
        return EXIT_FAILURE

    except TranscriptionError as error:
        print_status(f"Transcription error: {error}")
        return EXIT_FAILURE

    except LLMClientError as error:
        print_status(f"LLM error: {error}")
        return EXIT_FAILURE

    except TTSEngineError as error:
        print_status(f"Text-to-speech error: {error}")
        return EXIT_FAILURE

    except OSError as error:
        print_status(f"File error: {error}")
        return EXIT_FAILURE

    return EXIT_SUCCESS


def main() -> int:
    """Provide the main application entry point.

    Returns:
        The application's exit code.
    """
    return run_application()


if __name__ == "__main__":
    raise SystemExit(main())