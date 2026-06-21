from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

from agent_workforce.prompt import PromptLoader

agent_name = "refining_agent"
_agent = Agent(
    name=agent_name,
    instructions=PromptLoader(agent_name)._load_prompt(
        plugins=["self_check", "natural_voice"]
    ),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

refining_tool = _agent.as_tool(
    tool_name="refining_agent",
    tool_description="Refine a draft: critique it, humanize and format it, and suggest a visual idea.",
)
