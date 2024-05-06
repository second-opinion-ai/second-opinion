"""
Unit tests for the llm_interaction module.

This module contains unit tests for the functions in the llm_interaction module.
It tests the behavior of the get_llm and get_embeddings functions under different
scenarios, including valid and invalid environment variable configurations.

Classes:
  TestLLMInteraction: A test case class for the llm_interaction module.

Methods:
  test_get_llm: Tests the get_llm function with valid environment variables.
  test_get_embeddings: Tests the get_embeddings function with valid environment variables.
  test_get_llm_invalid_type: Tests the get_llm function with an invalid LLM type.
  test_get_embeddings_invalid_type: Tests the get_embeddings function with an invalid embeddings type.
"""

import os
import unittest
from unittest.mock import patch
from app.services.llm_interaction import get_llm, get_embeddings
from langchain_community.chat_models import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings


class TestLLMInteraction(unittest.TestCase):
  @patch.dict(os.environ,
              {"LLM_TYPE": "openai", "OPENAI_API_KEY": "test_api_key"})
  def test_get_llm(self):
    llm = get_llm(temperature=0.1)
    self.assertIsInstance(llm, ChatOpenAI)
    self.assertEqual(llm.temperature, 0.1)

  @patch.dict(os.environ,
              {"EMBEDDINGS_TYPE": "openai",
               "OPENAI_API_KEY": "test_api_key"}
              )
  def test_get_embeddings(self):
    embeddings = get_embeddings()
    self.assertIsInstance(embeddings, OpenAIEmbeddings)

  @patch.dict(os.environ, {"LLM_TYPE": "invalid"})
  def test_get_llm_invalid_type(self):
    with self.assertRaises(ValueError):
      get_llm(temperature=0.1)

  @patch.dict(os.environ, {"EMBEDDINGS_TYPE": "invalid"})
  def test_get_embeddings_invalid_type(self):
    with self.assertRaises(ValueError):
      get_embeddings()


if __name__ == "__main__":
  unittest.main()
