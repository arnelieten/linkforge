from agent_workforce.chat_agent import ChatAgent
from telegram.auth import authenticate_header_secret, authenticate_user_id
from telegram.client import send_telegram_message


async def handle_webhook(request_body: dict, request_headers: dict, agent: ChatAgent):
    if not (
        authenticate_user_id(request_body=request_body)
        and authenticate_header_secret(request_header=request_headers)
    ):
        return

    message = request_body["message"]
    chat_id = message["chat"]["id"]
    text = message.get("text")

    if text:
        reply = await agent.chat(message=text, session_id=chat_id)
        await send_telegram_message(
            chat_id=chat_id,
            message=reply,
        )
    else:
        reply = "Whoopsie-Daisy, I can only handle text messages!"
        await send_telegram_message(
            chat_id=chat_id,
            message=reply,
        )


# implement slash commands
# .draft retrieves last updated draft
# .research retrieves last interesting research links
# .confirm puts draft as ready to go on linkedin
# .help lists the dot commands possible and description
# .restart clears history of agents to start over
# .list to get a list of drafts
