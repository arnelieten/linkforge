from agent_workforce.super_agent import SuperAgent
from database import approve_current_draft, get_current_draft
from telegram.auth import authenticate_header_secret, authenticate_user_id
from telegram.client import TelegramClient
from utils.logger import logger


async def handle_webhook(
    request_body: dict,
    request_headers: dict,
    agent: SuperAgent,
    telegram_client: TelegramClient,
):
    if not authenticate_header_secret(request_header=request_headers):
        logger.warning("rejected webhook: bad/missing secret header")
        return

    response = request_body.get("message")
    if not response or "chat" not in response:
        logger.info("ignoring non-message update: keys=%s", list(request_body.keys()))
        return

    if not authenticate_user_id(request_body=request_body):
        logger.warning("rejected webhook: unauthorized user")
        return

    chat_id = response["chat"]["id"]
    incoming_message = response.get("text")

    if not incoming_message:
        outgoing_message = "Whoopsie-Daisy, I can only handle text messages!"
    elif incoming_message.strip().startswith("."):
        outgoing_message = await handle_dot_commands(
            message=incoming_message, chat_id=chat_id
        )
    else:
        outgoing_message = await agent.chat(
            message=incoming_message, session_id=chat_id
        )

    await telegram_client.send_message(chat_id=chat_id, message=outgoing_message)


async def handle_dot_commands(message: str, chat_id: int) -> str:
    match message.strip():
        case ".draft":
            # retrieves last updated draft
            current_draft = get_current_draft(chat_id=chat_id)
            return current_draft

        case ".research":
            # retrieves last interesting research links
            return "implement research functionality"

        case ".approve":
            succeeded_message = approve_current_draft(chat_id=chat_id)
            return succeeded_message

        case ".help":
            # list all .commands
            return "implement help functionality"

        case ".restart":
            # TODO implement
            # clears history of agents (session & state draft) to start over
            return "restart functionality to be implemented"

        case _:
            return "Unknown command. Try .help."
