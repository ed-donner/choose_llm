from abc import ABC
from anthropic import Anthropic
from openai import OpenAI
from groq import Groq
import logging
from typing import Generator, Dict, Type, Self, List
import os
from datetime import datetime
import time

logger = logging.getLogger(__name__)


class LLMException(Exception):
    pass


class LLM(ABC):
    """
    An abstract superclass for interacting with LLMs - subclass for Claude and GPT
    """

    model_names = []

    def __init__(self, model_name: str, temperature: float):
        self.model_name = model_name
        self.client = None
        self.temperature = temperature

    def send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        print("_____")
        print(f"Calling {self.model_name}")
        print("System prompt:\n"+system)
        print("User prompt:\n"+user)
        result = self.protected_send(system, user, max_tokens)
        print("Response:\n"+result)
        print("_____")
        left = result.find("{")
        right = result.rfind("}")
        if left>-1 and right>-1:
            result=result[left: right+1]
        return result

    def protected_send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        retries = 5
        done = False
        while retries:
            retries -= 1
            try:
                return self._send(system, user, max_tokens)
            except Exception as e:
                print(f"Exception on calling LLM of {e}")
                if retries:
                    print("Waiting 2s and retrying")
                    time.sleep(2)
        return "{}"

    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        pass


    @classmethod
    def model_map(cls) -> Dict[str, Type[Self]]:
        """
        Generate a mapping of Model Names to LLM classes, by looking at all subclasses of this one
        :return: a mapping dictionary from model name to LLM subclass
        """
        mapping = {}
        for llm in cls.__subclasses__():
            for model_name in llm.model_names:
                mapping[model_name] = llm
        return mapping

    @classmethod
    def all_model_names(cls) -> List[str]:
        return cls.model_map().keys()

    @classmethod
    def create(cls, model_name: str, temperature: float = 0.5) -> Self:
        """
        Return an instance of a subclass that corresponds to this model_name
        :param model_name: a string to describe this model
        :param temperature: the creativity setting
        :return: a new instance of a subclass of LLM
        """
        subclass = cls.model_map().get(model_name)
        if not subclass:
            raise LLMException(f"Unrecognized LLM model name specified: {model_name}")
        return subclass(model_name, temperature)


class Claude(LLM):
    """
    A class to act as an interface to the remote AI, in this case Claude
    """

    model_names = ["claude-3-5-sonnet-latest"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the Anthropic client
        """
        super().__init__(model_name, temperature)
        self.client = Anthropic()


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to Claude
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        response = self.client.messages.create(
            model=self.model_name,
            max_tokens=max_tokens,
            temperature=self.temperature,
            system=system,
            messages=[
                {"role": "user", "content": user},
            ],
        )
        return response.content[0].text


class GPT(LLM):
    """
    A class to act as an interface to the remote AI, in this case GPT
    """

    model_names = ["gpt-4o-mini", "gpt-4o"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(model_name, temperature)
        self.client = OpenAI()


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to GPT
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content

class O(LLM):
    """
    A class to act as an interface to the remote AI, in this case GPT
    """

    model_names = [ "o1", "o1-mini", "o3-mini"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(model_name, temperature)
        self.client = OpenAI()


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to GPT
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        message = system + "\n\n" + user
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "user", "content": message},
            ],
        )
        return response.choices[0].message.content

class Ollama(LLM):
    """
    A class to act as an interface to the remote AI, in this case Ollama via the OpenAI client
    """

    model_names = ["llama3.2 local", "gemma2 local", "qwen2.5 local", "phi4 local"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(model_name.replace(" local", ""), temperature)
        self.client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to Ollama
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
        )
        reply = response.choices[0].message.content
        if "</think>" in reply:
            print("Thoughts:\n" +reply.split("</think>")[0].replace("<think>",""))
            reply = reply.split("</think>")[1]
        return reply

class DeepSeekAPI(LLM):
    """
    A class to act as an interface to the remote AI, in this case DeepSeek via the OpenAI client
    """

    model_names = ["deepseek-V3", "deepseek-r1"]

    model_map = {"deepseek-V3": "deepseek-chat", "deepseek-r1": "deepseek-reasoner"}

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(self.model_map[model_name], temperature)
        deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
        self.client = OpenAI(api_key=deepseek_api_key, base_url="https://api.deepseek.com")


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to DeepSeek
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            # response_format={"type": "json_object"},
        )
        reply = response.choices[0].message.content
        return reply

class DeepSeekLocal(LLM):
    """
    A class to act as an interface to the remote AI, in this case Ollama via the OpenAI client
    """

    model_names = ["deepseek-r1:14b local"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(model_name.replace(' local', ''), temperature)
        self.client = OpenAI(base_url='http://localhost:11434/v1', api_key='ollama')


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to Ollama
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        system += "\nImportant: avoid overthinking. Think briefly and decisively. The final response must follow the given json format or you forfeit the game. Do not overthink. Respond with json."
        user += "\nImportant: avoid overthinking. Think briefly and decisively. The final response must follow the given json format or you forfeit the game. Do not overthink. Respond with json."
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
        )
        reply = response.choices[0].message.content
        if "</think>" in reply:
            print("Thoughts:\n" +reply.split("</think>")[0].replace("<think>",""))
            reply = reply.split("</think>")[1]
        return reply

class GroqAPI(LLM):
    """
    A class to act as an interface to the remote AI, in this case Groq
    """

    model_names = ["deepseek-r1-distill-llama-70b via Groq", "llama-3.3-70b-versatile via Groq", "mixtral-8x7b-32768 via Groq"]

    def __init__(self, model_name: str, temperature: float):
        """
        Create a new instance of the OpenAI client
        """
        super().__init__(model_name[:-9], temperature)
        self.client = Groq()


    def _send(self, system: str, user: str, max_tokens: int = 3000) -> str:
        """
        Send a message to GPT
        :param system: the context in which this message is to be taken
        :param user: the prompt
        :param max_tokens: max number of tokens to generate
        :return: the response from the AI
        """
        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {"role": "system", "content": system},
                {"role": "user", "content": user},
            ],
            response_format={"type": "json_object"},
        )
        return response.choices[0].message.content
