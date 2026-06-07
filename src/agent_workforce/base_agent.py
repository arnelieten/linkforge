from abc import ABC
from pathlib import Path

from agent_workforce.utils.prompt import load_prompt
from agents import Agent, Runner, SQLiteSession, SessionSettings
from agents.extensions.models.litellm_model import LitellmModel
from config import SQLITE_DB_PATH, SQLITE_SESSION_LIMIT

class BaseAgent(ABC):
    name: str
    model: str

    def __init__(self) -> None:
        self.agent = Agent(
            name=self.name,
            instructions=load_prompt(Path(__file__).parent / "prompts" / f"{self.name}_prompt.md"),
            model=LitellmModel(model=self.model),
        )


    async def chat(self, message: str, session_id: str) -> str:
        session = SQLiteSession(
            session_id=session_id,
            db_path=SQLITE_DB_PATH,
            session_settings=SessionSettings(limit=SQLITE_SESSION_LIMIT)
        )
        try:
            result = await Runner.run(self.agent, message, session=session)
            return result.final_output
        finally:
            session.close()
