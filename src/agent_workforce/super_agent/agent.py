from agents import Agent, Runner, SessionSettings, SQLiteSession
from agents.extensions.models.litellm_model import LitellmModel

from agent_workforce.prompt import PromptLoader
from agent_workforce.tools import TOOLS, ChatContext
from config import SQLITE_DB_PATH, SQLITE_SESSION_LIMIT


class SuperAgent:
    name = "super_agent"
    model = "gemini/gemini-2.5-flash"
    prompt_loader = PromptLoader(name)

    def __init__(self) -> None:
        self.agent = Agent(
            name=self.name,
            instructions=self.prompt_loader._load_prompt(),
            model=LitellmModel(model=self.model),
            tools=TOOLS,
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
