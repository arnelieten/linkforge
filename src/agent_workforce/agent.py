import asyncio
from pathlib import Path

from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel
from agent_workforce.utils.prompt import load_prompt

set_tracing_disabled(True)

agent = Agent(
    name="Poet",
    instructions=load_prompt(Path(__file__).parent / "prompts" / "prompt.md"),
    model=LitellmModel(model="gemini/gemini-2.5-flash-lite"),
)
async def chat(message: str):
    result = await Runner.run(agent, message)
    return result.final_output


if __name__ == "__main__":
    asyncio.run(chat())
