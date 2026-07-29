"""Application controller for the LLM Processing Assistant."""

from time import perf_counter

from config import COHERE_MODEL
from llm_client import (
    LLMClientError,
    create_client,
    generate_response,
)
from utils import (
    display_response,
    display_session_summary,
    get_user_message,
    print_banner,
    print_status,
    save_response,
)


EXIT_SUCCESS = 0
EXIT_FAILURE = 1
EXIT_INTERRUPTED = 130


def run_application() -> int:
    """Run one complete LLM-processing session.

    Returns:
        An operating-system exit code indicating whether the
        application completed successfully.
    """
    print_banner()

    try:
        user_message = get_user_message()
        session_start = perf_counter()

        print_status("Generating response...")

        client = create_client()
        result = generate_response(
            client=client,
            user_message=user_message,
        )

        display_response(result.text)

        response_file = save_response(result.text)
        print_status("Response saved successfully.")

        total_runtime = perf_counter() - session_start

        display_session_summary(
            model_name=COHERE_MODEL,
            response_time=result.response_time,
            total_runtime=total_runtime,
            response_file=response_file,
        )

    except KeyboardInterrupt:
        print_status("Application cancelled by user.")
        return EXIT_INTERRUPTED

    except ValueError as error:
        print_status(f"Input error: {error}")
        return EXIT_FAILURE

    except LLMClientError as error:
        print_status(f"LLM error: {error}")
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