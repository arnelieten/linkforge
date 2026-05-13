from abc import ABC
from pathlib import Path

from agent_workforce.utils.prompt import load_prompt
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

class BaseAgent(ABC):
    name: str
    model: str

    def __init__(self) -> None:
        self.agent = Agent(
            name=self.name,
            instructions=load_prompt(Path(__file__).parent / "prompts" / f"{self.name}_prompt.md"),
            model=LitellmModel(model=self.model),
        )


    async def chat(self, message: str) -> str:
        result = await Runner.run(self.agent, message)
        return result.final_output
