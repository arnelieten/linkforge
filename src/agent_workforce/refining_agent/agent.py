from pathlib import Path

from agent_workforce.prompt import load_prompt
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

_agent = Agent(
    name="refining_agent",
    instructions=load_prompt(Path(__file__).parent / "prompt.jinja"),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

refining_tool = _agent.as_tool(
    tool_name="refining_agent",
    tool_description="Refine a draft: critique it, humanize and format it, and suggest a visual idea.",
)
