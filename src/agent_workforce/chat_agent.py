import asyncio
from pathlib import Path

from agent_workforce.base_agent import BaseAgent


class ChatAgent(BaseAgent):
    name = "chat_agent"
    model = "gemini/gemini-2.5-flash-lite"

if __name__ == "__main__":
    chat_agent = ChatAgent
    asyncio.run(chat_agent.chat("What can you do for me?"))
