from dataclasses import dataclass

from agents import RunContextWrapper, function_tool

from agent_workforce.refining_agent import refining_tool
from agent_workforce.writing_agent import writing_tool
from database import save_current_draft


@dataclass
class ChatContext:
    chat_id: int


@function_tool
def save_draft(ctx: RunContextWrapper[ChatContext], draft: str) -> str:
    """Save the user's current LinkedIn post draft. Call whenever you write or revise a full post."""
    save_current_draft(ctx.context.chat_id, draft)
    return "Draft saved."


TOOLS = [save_draft, writing_tool, refining_tool]
