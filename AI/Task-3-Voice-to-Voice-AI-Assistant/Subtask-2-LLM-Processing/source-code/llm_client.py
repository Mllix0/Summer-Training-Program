"""Cohere API communication for the LLM Processing application."""

from dataclasses import dataclass
from time import perf_counter
from typing import Any

import cohere

from config import (
    COHERE_API_KEY,
    COHERE_MODEL,
    MAX_TOKENS,
    SYSTEM_MESSAGE,
    TEMPERATURE,
)


class LLMClientError(RuntimeError):
    """Raised when the LLM client cannot complete a request."""


@dataclass(frozen=True)
class LLMResponse:
    """Store the generated response and its processing time."""

    text: str
    response_time: float


def create_client() -> cohere.ClientV2:
    """Create and return an authenticated Cohere client.

    Returns:
        An authenticated Cohere V2 client.

    Raises:
        LLMClientError: If the Cohere API key is missing.
    """
    if not COHERE_API_KEY:
        raise LLMClientError(
            "The Cohere API key is missing. "
            "Add COHERE_API_KEY to the .env file."
        )

    return cohere.ClientV2(api_key=COHERE_API_KEY)


def extract_response_text(response: Any) -> str:
    """Extract text from a Cohere Chat API response.

    Args:
        response: The response object returned by Cohere.

    Returns:
        The combined text contained in the response.

    Raises:
        LLMClientError: If the response contains no readable text.
    """
    try:
        content_blocks = response.message.content
    except AttributeError as error:
        raise LLMClientError(
            "Cohere returned an unexpected response format."
        ) from error

    text_parts = [
        block.text.strip()
        for block in content_blocks
        if getattr(block, "text", "").strip()
    ]

    response_text = "\n".join(text_parts).strip()

    if not response_text:
        raise LLMClientError(
            "Cohere returned a response without any readable text."
        )

    return response_text


def generate_response(
    client: cohere.ClientV2,
    user_message: str,
) -> LLMResponse:
    """Send a user message to Cohere and return the generated response.

    Args:
        client: An authenticated Cohere V2 client.
        user_message: The text entered by the user.

    Returns:
        An LLMResponse containing generated text and response time.

    Raises:
        ValueError: If the user message is empty.
        LLMClientError: If the Cohere request fails.
    """
    cleaned_message = user_message.strip()

    if not cleaned_message:
        raise ValueError("The user message cannot be empty.")

    start_time = perf_counter()

    try:
        response = client.chat(
            model=COHERE_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_MESSAGE,
                },
                {
                    "role": "user",
                    "content": cleaned_message,
                },
            ],
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
        )
    except Exception as error:
        raise LLMClientError(
            f"The Cohere request failed: {error}"
        ) from error

    response_time = perf_counter() - start_time
    response_text = extract_response_text(response)

    return LLMResponse(
        text=response_text,
        response_time=response_time,
    )