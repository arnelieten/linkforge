from pathlib import Path

from agent_workforce.prompt import load_prompt
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

_agent = Agent(
    name="ideation_agent",
    instructions=load_prompt(Path(__file__).parent / "prompt.md"),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

ideation_tool = _agent.as_tool(
    tool_name="ideation_agent",
    tool_description="Explore post ideas: generate angles, split broad topics, suggest directions.",
)
