from agent_workforce.chat_agent import ChatAgent
from telegram.auth import authenticate_header_secret, authenticate_user_id
from telegram.client import TelegramClient
from utils.logger import logger


async def handle_webhook(request_body: dict, request_headers: dict, agent: ChatAgent, telegram_client: TelegramClient):
    if not authenticate_header_secret(request_header=request_headers):
        logger.warning("rejected webhook: bad/missing secret header")
        return

    message = request_body.get("message")
    if not message or "chat" not in message:
        logger.info("ignoring non-message update: keys=%s", list(request_body.keys()))
        return

    if not authenticate_user_id(request_body=request_body):
        logger.warning("rejected webhook: unauthorized user")
        return

    chat_id = message["chat"]["id"]
    text = message.get("text")

    reply = (
        await agent.chat(message=text, session_id=chat_id)
        if text
        else "Whoopsie-Daisy, I can only handle text messages!"
    )
    await telegram_client.send_message(chat_id=chat_id, text=reply)


# implement slash commands
# .draft retrieves last updated draft
# .research retrieves last interesting research links
# .confirm puts draft as ready to go on linkedin
# .help lists the dot commands possible and description
# .restart clears history of agents to start over
# .list to get a list of drafts
