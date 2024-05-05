"""
Module for interacting with language models and embeddings.

This module provides functions to retrieve language models (LLMs) and embeddings
based on the specified environment variables. It supports OpenAI's GPT models and
embeddings by default, but can be extended to support other LLMs and embeddings.

Functions:
  get_llm: Retrieves the specified language model (LLM).
  get_embeddings: Retrieves the specified embeddings.

Environment Variables:
  LLM_TYPE: The type of LLM to use (default: "openai").
  EMBEDDINGS_TYPE: The type of embeddings to use (default: "openai").
  OPENAI_API_KEY: The API key for OpenAI's services.
"""

import os
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings


def get_llm(temperature: float) -> ChatOpenAI:
  """
  Retrieves the specified language model (LLM).

    Args:
      temperature: The temperature value for the LLM.

    Returns:
      The initialized language model (LLM).

    Raises:
      ValueError: If an unsupported LLM type is specified.
  """
  llm_type = os.environ.get("LLM_TYPE", "openai")

  if llm_type == "openai":
    return ChatOpenAI(temperature=temperature,
                      openai_api_key=os.environ.get("OPENAI_API_KEY"))
  else:
    raise ValueError(f"Unsupported LLM type: {llm_type}")


def get_embeddings() -> OpenAIEmbeddings:
  """
  Retrieves the specified embeddings.

    Returns:
      The initialized embeddings.

    Raises:
      ValueError: If an unsupported embeddings type is specified.
  """
  embeddings_type = os.environ.get("EMBEDDINGS_TYPE", "openai")

  if embeddings_type == "openai":
    return OpenAIEmbeddings(openai_api_key=os.environ.get("OPENAI_API_KEY"))
  else:
    raise ValueError(f"Unsupported embeddings type: {embeddings_type}")
