"""Description: This file contains the implementation of the LLM class using llama.cpp.
This class provides a stateless interface to llama.cpp for language generation.
"""

import asyncio
from typing import AsyncIterator, List, Dict, Any
from llama_cpp import Llama
from loguru import logger

from .stateless_llm_interface import StatelessLLMInterface


class LLM(StatelessLLMInterface):
    def __init__(
        self,
        model_path: str,
        **kwargs,
    ):
        """
        Initializes a stateless instance of the LLM class using llama.cpp.

        Parameters:
        - model_path (str): Path to the GGUF model file
        - **kwargs: Additional arguments passed to Llama constructor
        """
        logger.info(f"Initializing llama cpp with model path: {model_path}")
        self.model_path = model_path
        try:
            self.llm = Llama(model_path=model_path, **kwargs)
        except Exception as e:
            logger.critical(f"Failed to initialize Llama model: {e}")
            raise

    async def chat_completion(
        self,
        messages: List[Dict[str, Any]],
        system: str = None,
        tools: List[Dict[str, Any]] = None,
    ) -> AsyncIterator[str]:
        """
        Generates a chat completion using llama.cpp asynchronously.

        Parameters:
        - messages (List[Dict[str, Any]]): The list of messages to send to the model.
        - system (str, optional): System prompt to use for this completion.

        Yields:
        - str: The content of each chunk from the model response.
        """
        logger.debug(f"Generating completion for messages: {messages}")
        if tools:
            logger.warning("llama_cpp_llm does not support tools; ignoring them.")

        try:
            # Add system prompt if provided
            messages_with_system = messages
            if system:
                messages_with_system = [
                    {"role": "system", "content": system},
                    *messages,
                ]

            # Create chat completion in a separate thread to avoid blocking
            loop = asyncio.get_running_loop()
            chat_completion = await loop.run_in_executor(
                None,
                lambda: self.llm.create_chat_completion(
                    messages=messages_with_system,
                    stream=True,
                ),
            )

            # Pull each chunk in the executor too: iterating the generator
            # runs synchronous inference and would otherwise block the loop
            _done = object()
            while True:
                chunk = await loop.run_in_executor(None, next, chat_completion, _done)
                if chunk is _done:
                    break
                if chunk.get("choices") and chunk["choices"][0].get("delta"):
                    content = chunk["choices"][0]["delta"].get("content", "")
                    if content:
                        yield content

        except Exception as e:
            logger.error(f"Error in chat completion: {e}")
            raise
