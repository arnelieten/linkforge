from functools import lru_cache

from openai import AsyncOpenAI

from config import OPENAI_API_KEY


@lru_cache(maxsize=1)
def get_async_openai_client() -> AsyncOpenAI:
    return AsyncOpenAI(api_key=OPENAI_API_KEY)