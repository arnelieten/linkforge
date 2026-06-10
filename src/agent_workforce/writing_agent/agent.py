from pathlib import Path

from agent_workforce.prompt import load_prompt
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

_agent = Agent(
    name="writing_agent",
    instructions=load_prompt(Path(__file__).parent / "prompt.md"),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

writing_tool = _agent.as_tool(
    tool_name="writing_agent",
    tool_description="Write a complete LinkedIn post (hook, insight, takeaway, hashtags) from a topic or angle.",
)
