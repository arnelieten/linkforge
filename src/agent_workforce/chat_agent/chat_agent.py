from pathlib import Path

from agent_workforce.prompt import load_prompt
from agent_workforce.tools import ChatContext, save_draft
from agents import Agent, Runner, SQLiteSession, SessionSettings
from agents.extensions.models.litellm_model import LitellmModel
from config import SQLITE_DB_PATH, SQLITE_SESSION_LIMIT


class ChatAgent:
    name = "chat_agent"
    model = "gemini/gemini-2.5-flash"

    def __init__(self) -> None:
        self.agent = Agent(
            name=self.name,
            instructions=load_prompt(Path(__file__).parent / f"{self.name}_prompt.md"),
            model=LitellmModel(model=self.model),
            tools=[save_draft],
        )

    async def chat(self, message: str, session_id: int) -> str:
        session = SQLiteSession(
            session_id=session_id,
            db_path=SQLITE_DB_PATH,
            session_settings=SessionSettings(limit=SQLITE_SESSION_LIMIT),
        )
        try:
            result = await Runner.run(
                self.agent,
                message,
                session=session,
                context=ChatContext(chat_id=session_id),
            )
            return result.final_output
        finally:
            session.close()
