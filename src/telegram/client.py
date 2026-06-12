import httpx
from telegramify_markdown import convert

class TelegramClient:
    def __init__(self, api_key: str, http_client: httpx.AsyncClient) -> None:
        self._base_url = f"https://api.telegram.org/bot{api_key}"
        self._http_client = http_client

    async def send_message(self, chat_id: int, message: str) -> None:
        text, entities = convert(message)
        await self._http_client.post(
            f"{self._base_url}/sendMessage",
            json={"chat_id": chat_id, "text": text, "entities": [e.to_dict() for e in entities]},
        )
