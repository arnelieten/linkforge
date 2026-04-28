import asyncio
import os

from litellm import acompletion

import config


async def chat():
    response = await acompletion(
        model="gemini/gemini-2.5-flash-lite",
        messages=[{"role": "user", "content": "Write a short poem"}],
        stream=True,
    )
    async for chunk in response:
        print(chunk.choices[0].delta.content or "", end="")




if __name__ == "__main__":
    asyncio.run(chat())