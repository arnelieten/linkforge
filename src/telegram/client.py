import httpx

from config import BOTFATHER_API_KEY


async def send_telegram_message(chat_id: str, message: str) -> None:
    async with httpx.AsyncClient() as client:
        await client.post(
            f"https://api.telegram.org/bot{BOTFATHER_API_KEY}/sendMessage",
            json={"chat_id": chat_id, "text": message},
        )
