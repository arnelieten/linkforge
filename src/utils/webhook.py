from config import BOTFATHER_USER_ID, BOTFATHER_WEBHOOK_SECRET, BOTFATHER_API_KEY

import secrets
import httpx
from src.agent_workforce.base_agent import BaseAgent

# Authentication for the webhook
def get_request_user_id(request_body: dict) -> str:
    message = request_body.get('message')
    chat = message.get('chat')
    return str(chat.get('id'))

def verify_user_id(user_id: str) -> bool:
    return secrets.compare_digest(user_id, BOTFATHER_USER_ID)

def authenticate_user_id(request_body: dict) -> bool:
    user_id = get_request_user_id(request_body=request_body)
    return verify_user_id(user_id=user_id)

def get_request_header_secret(request_header: dict) -> str:
    return str(request_header.get('x-telegram-bot-api-secret-token')) or None

def verify_header_secret(header_secret: str) -> bool:
    return secrets.compare_digest(header_secret, BOTFATHER_WEBHOOK_SECRET)

def authenticate_header_secret(request_header: dict) -> bool:
    header_secret = get_request_header_secret(request_header=request_header)
    return verify_header_secret(header_secret=header_secret)


# Webhook handling
async def send_telegram_message(chat_id: str, message: str) -> None:
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{BOTFATHER_API_KEY}/sendMessage",
            json={"chat_id": chat_id, "text": message},
        )


async def handle_webhook(request_body: dict, request_headers: dict, agent: BaseAgent):
    if not (
        authenticate_user_id(request_body=request_body)
        and authenticate_header_secret(request_header=request_headers)
    ):
        return

    message = request_body.get("message")
    text = message.get("text")
    reply = await agent.chat(text)
    await send_telegram_message(
        chat_id=message["chat"]["id"],
        message=reply,
    )
