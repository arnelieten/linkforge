from dataclasses import dataclass

from agents import RunContextWrapper, function_tool
from database import save_current_draft


@dataclass
class ChatContext:
    chat_id: int


@function_tool
def save_draft(ctx: RunContextWrapper[ChatContext], draft: str) -> str:
    """Save the user's current LinkedIn post draft. Call whenever you write or revise a full post."""
    save_current_draft(ctx.context.chat_id, draft)
    return "Draft saved."


# voice match

# angle generator

# posts criticiser find weaknesses and technical inaccuracies

# SEO optimization

# linkedin formatter

# hashtag suggester

# humanize post

# split large post into smaller ones based on link to medium or other blogpost

# content suggestor reads database last articles and finds content that matches my goal

# hook generator

# meme visual idea generator (multimodal) the drake meme (not whatsapp but likes telegram)

# contrarian comment generator

# confirming comment generator
