from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

from agent_workforce.prompt import PromptLoader

agent_name = "ideation_agent"

_agent = Agent(
    name=agent_name,
    instructions=PromptLoader(agent_name)._load_prompt(),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

ideation_tool = _agent.as_tool(
    tool_name="ideation_agent",
    tool_description="Explore post ideas: generate angles, split broad topics, suggest directions.",
)
