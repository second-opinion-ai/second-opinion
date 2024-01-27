"""Module to interact with OpenAI's GPT model for generating chat responses.

This module provides functionality to send requests to OpenAI's GPT model
and retrieve generated responses based on the provided message content.
It uses the OpenAI API to prompt ChatGPT with specified parameters.
"""

import os

import requests
import json


def prompt_chat_gpt(message_content: str, model: str = "gpt-3.5-turbo") -> dict:
    """Sends a request to OpenAI's GPT model to generate a chat response.

    This function takes a message content string and an optional model
    specification, sends it to the OpenAI API, and returns the generated
    response as JSON.

    Args:
        message_content (str): The message content to send to the GPT model.
        model (str, optional): The identifier of the GPT model to use.
            Defaults to 'gpt-3.5-turbo'.

    Returns:
        dict: A dictionary containing the response from the GPT model.

    Raises:
        requests.exceptions.RequestException: If the request to the OpenAI API
        fails.
    """
    openai_api_key = os.environ.get("OPENAI_API_KEY")

    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai_api_key}",
    }

    data = {
        "model": model,
        "messages": [{"role": "user", "content": message_content}],
        "temperature": 0.7,
    }

    try:
        response = requests.post(
            url, headers=headers, data=json.dumps(data), verify=False, timeout=15
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise e
