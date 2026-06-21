from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

from agent_workforce.prompt import PromptLoader

agent_name = "writing_agent"

_agent = Agent(
    name=agent_name,
    instructions=PromptLoader(agent_name)._load_prompt(
        plugins=["linkedin_identity"], example_count=2
    ),
    model=LitellmModel(model="gemini/gemini-2.5-flash"),
)

writing_tool = _agent.as_tool(
    tool_name="writing_agent",
    tool_description="Write a complete LinkedIn post (hook, insight, takeaway, hashtags) from a topic or angle.",
)
