"""Terminal interface and file utilities for the LLM application."""

from pathlib import Path

from config import APP_TITLE, DIVIDER_WIDTH, RESPONSE_FILE


def print_banner() -> None:
    """Display the application title."""

    divider = "=" * DIVIDER_WIDTH

    print()
    print(divider)
    print(APP_TITLE.center(DIVIDER_WIDTH))
    print(divider)
    print()


def get_user_message() -> str:
    """Read and validate a message entered by the user.

    Returns:
        A non-empty user message.
    """
    while True:
        print("Enter your message:")
        user_message = input("> ").strip()

        if user_message:
            return user_message

        print()
        print("The message cannot be empty. Please try again.")
        print()


def print_status(message: str) -> None:
    """Display a processing-status message.

    Args:
        message: Status text to display.
    """
    print()
    print(message)
    print()


def display_response(response_text: str) -> None:
    """Display the generated AI response.

    Args:
        response_text: Text returned by the language model.
    """
    divider = "-" * DIVIDER_WIDTH

    print("AI Response:")
    print(divider)
    print(response_text)
    print(divider)
    print()


def save_response(
    response_text: str,
    file_path: Path = RESPONSE_FILE,
) -> Path:
    """Save the generated AI response to a UTF-8 text file.

    Args:
        response_text: Text returned by the language model.
        file_path: Destination path for the response file.

    Returns:
        The path of the saved response file.

    Raises:
        OSError: If the response file cannot be written.
    """
    cleaned_response = response_text.strip()

    if not cleaned_response:
        raise ValueError("The response cannot be empty.")

    file_path.write_text(
        cleaned_response + "\n",
        encoding="utf-8",
    )

    return file_path


def display_session_summary(
    model_name: str,
    response_time: float,
    total_runtime: float,
    response_file: Path,
) -> None:
    """Display information about the completed LLM session.

    Args:
        model_name: Name of the Cohere model used.
        response_time: Time spent waiting for the LLM response.
        total_runtime: Total application runtime.
        response_file: Location of the saved response.
    """
    divider = "=" * DIVIDER_WIDTH

    print("Session Summary")
    print(divider)
    print(f"Model:           {model_name}")
    print(f"Response Time:   {response_time:.2f} seconds")
    print(f"Total Runtime:   {total_runtime:.2f} seconds")
    print(f"Response Saved:  {response_file}")
    print(divider)