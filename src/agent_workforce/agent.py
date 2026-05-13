import asyncio
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

set_tracing_disabled(True)

agent = Agent(
    name="Poet",
    instructions="You are a poet!",
    model=LitellmModel(model="gemini/gemini-2.5-flash-lite"),
)
async def chat():
    result = await Runner.run(agent, "Write a short poem with the word rose")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(chat())
