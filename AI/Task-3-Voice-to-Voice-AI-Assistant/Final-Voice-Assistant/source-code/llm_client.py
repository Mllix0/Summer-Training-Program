"""Cohere LLM services for the Voice-to-Voice AI Assistant."""

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
    """Raised when the language-model request cannot be completed."""


@dataclass(frozen=True)
class LLMResponse:
    """Store the result of a completed LLM request."""

    text: str
    response_time: float
    model_name: str
    prompt_character_count: int
    response_character_count: int


def create_client() -> cohere.ClientV2:
    """Create an authenticated Cohere V2 client.

    Returns:
        An authenticated Cohere client.

    Raises:
        LLMClientError: If the Cohere API key is missing.
    """
    if not COHERE_API_KEY:
        raise LLMClientError(
            "The Cohere API key is missing. "
            "Add COHERE_API_KEY to the .env file."
        )

    try:
        return cohere.ClientV2(api_key=COHERE_API_KEY)
    except Exception as error:
        raise LLMClientError(
            f"The Cohere client could not be created: {error}"
        ) from error


def extract_response_text(response: Any) -> str:
    """Extract readable text from a Cohere Chat API response.

    Args:
        response: Response object returned by Cohere.

    Returns:
        The combined text from all readable content blocks.

    Raises:
        LLMClientError: If the response format is unexpected or empty.
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
            "Cohere returned a response without readable text."
        )

    return response_text


def generate_response(
    client: cohere.ClientV2,
    user_message: str,
) -> LLMResponse:
    """Generate an AI response for recognized speech.

    Args:
        client: An authenticated Cohere V2 client.
        user_message: Text produced by the speech-to-text stage.

    Returns:
        Generated text and request information.

    Raises:
        ValueError: If the recognized text is empty.
        LLMClientError: If the Cohere request fails.
    """
    cleaned_message = user_message.strip()

    if not cleaned_message:
        raise ValueError(
            "The recognized text cannot be empty."
        )

    request_start = perf_counter()

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

    response_time = perf_counter() - request_start
    response_text = extract_response_text(response)

    return LLMResponse(
        text=response_text,
        response_time=response_time,
        model_name=COHERE_MODEL,
        prompt_character_count=len(cleaned_message),
        response_character_count=len(response_text),
    )